"""
Scattering process definitions and kinematics.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Optional

import numpy as np


class ParticleID(Enum):
    ELECTRON = "e"
    POSITRON = "e+"
    MUON = "mu"
    ANTIMUON = "mu+"
    PHOTON = "gamma"
    TAU = "tau"
    ANTITAU = "tau+"


@dataclass(frozen=True)
class Particle:
    pid: ParticleID
    mass: float       # GeV
    charge: float     # units of |e|
    spin: float

    @property
    def name(self) -> str:
        return self.pid.value

    @property
    def is_fermion(self) -> bool:
        return self.spin == 0.5

    @property
    def is_photon(self) -> bool:
        return self.pid == ParticleID.PHOTON


# Standard QED particles
ELECTRON = Particle(ParticleID.ELECTRON, mass=0.000510999, charge=-1.0, spin=0.5)
POSITRON = Particle(ParticleID.POSITRON, mass=0.000510999, charge=+1.0, spin=0.5)
MUON = Particle(ParticleID.MUON, mass=0.105658, charge=-1.0, spin=0.5)
ANTIMUON = Particle(ParticleID.ANTIMUON, mass=0.105658, charge=+1.0, spin=0.5)
PHOTON = Particle(ParticleID.PHOTON, mass=0.0, charge=0.0, spin=1.0)


# Physical constants
ALPHA = 1.0 / 137.035999084
ALPHA_OVER_PI = ALPHA / np.pi


@dataclass
class Process:
    """A scattering process with initial and final state particles."""
    initial: tuple[Particle, ...]
    final: tuple[Particle, ...]
    sqrt_s: Optional[float] = None   # GeV, center-of-mass energy

    @property
    def s(self) -> Optional[float]:
        return self.sqrt_s**2 if self.sqrt_s else None

    @property
    def label(self) -> str:
        ini = " ".join(p.name for p in self.initial)
        fin = " ".join(p.name for p in self.final)
        return f"{ini} -> {fin}"

    def mandelstam(self, cos_theta: float) -> dict:
        """Compute Mandelstam variables for 2→2 scattering."""
        if len(self.initial) != 2 or len(self.final) != 2:
            raise ValueError("Mandelstam variables defined for 2→2 only")
        if self.sqrt_s is None:
            raise ValueError("sqrt_s not set")
        s = self.s
        m1, m2 = self.initial[0].mass, self.initial[1].mass
        m3, m4 = self.final[0].mass, self.final[1].mass
        # CM momentum
        pcm2 = (s - (m3 + m4)**2) * (s - (m3 - m4)**2) / (4 * s)
        if pcm2 < 0:
            raise ValueError(f"Below threshold: sqrt_s={self.sqrt_s}")
        pcm = np.sqrt(pcm2)
        E3 = np.sqrt(pcm2 + m3**2)
        E1 = self.sqrt_s / 2  # massless approx for incoming
        t = m1**2 + m3**2 - 2 * E1 * E3 + 2 * pcm * np.sqrt(E1**2 - m1**2) * cos_theta
        u = m1**2 + m2**2 + m3**2 + m4**2 - s - t
        return {"s": s, "t": t, "u": u}


# Common processes
def ee_to_mumu(sqrt_s: float) -> Process:
    return Process(
        initial=(ELECTRON, POSITRON),
        final=(MUON, ANTIMUON),
        sqrt_s=sqrt_s,
    )

def ee_to_ee(sqrt_s: float) -> Process:
    return Process(
        initial=(ELECTRON, POSITRON),
        final=(ELECTRON, POSITRON),
        sqrt_s=sqrt_s,
    )
