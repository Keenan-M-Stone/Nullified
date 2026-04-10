"""
Particle state representations for SCN-filtered QFT.

Each particle is modeled as a set of quantum numbers.
Multi-particle states are sets of particle states.
"""

from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Optional


class ParticleType(Enum):
    ELECTRON = auto()
    POSITRON = auto()
    MUON = auto()
    ANTIMUON = auto()
    TAU = auto()
    ANTITAU = auto()
    PHOTON = auto()
    GLUON = auto()
    UP = auto()
    ANTI_UP = auto()
    DOWN = auto()
    ANTI_DOWN = auto()
    STRANGE = auto()
    ANTI_STRANGE = auto()
    CHARM = auto()
    ANTI_CHARM = auto()
    BOTTOM = auto()
    ANTI_BOTTOM = auto()
    TOP = auto()
    ANTI_TOP = auto()
    GHOST = auto()
    ANTIGHOST = auto()


class InteractionType(Enum):
    QED_VERTEX = auto()         # e-γ-e vertex
    QCD_QQG_VERTEX = auto()     # q-g-q vertex
    QCD_GGG_VERTEX = auto()     # triple-gluon vertex
    QCD_GGGG_VERTEX = auto()    # four-gluon vertex
    QCD_GHOST_VERTEX = auto()   # ghost-gluon vertex


# Particle groups for self-containment checking
FERMION_TYPES = {
    ParticleType.ELECTRON, ParticleType.POSITRON,
    ParticleType.MUON, ParticleType.ANTIMUON,
    ParticleType.TAU, ParticleType.ANTITAU,
    ParticleType.UP, ParticleType.ANTI_UP,
    ParticleType.DOWN, ParticleType.ANTI_DOWN,
    ParticleType.STRANGE, ParticleType.ANTI_STRANGE,
    ParticleType.CHARM, ParticleType.ANTI_CHARM,
    ParticleType.BOTTOM, ParticleType.ANTI_BOTTOM,
    ParticleType.TOP, ParticleType.ANTI_TOP,
}

LEPTON_TYPES = {
    ParticleType.ELECTRON, ParticleType.POSITRON,
    ParticleType.MUON, ParticleType.ANTIMUON,
    ParticleType.TAU, ParticleType.ANTITAU,
}

QUARK_TYPES = FERMION_TYPES - LEPTON_TYPES

GAUGE_BOSON_TYPES = {
    ParticleType.PHOTON,
    ParticleType.GLUON,
}

GHOST_TYPES = {
    ParticleType.GHOST,
    ParticleType.ANTIGHOST,
}


def antiparticle(ptype: ParticleType) -> ParticleType:
    """Return the antiparticle of a given particle type."""
    pairs = {
        ParticleType.ELECTRON: ParticleType.POSITRON,
        ParticleType.MUON: ParticleType.ANTIMUON,
        ParticleType.TAU: ParticleType.ANTITAU,
        ParticleType.UP: ParticleType.ANTI_UP,
        ParticleType.DOWN: ParticleType.ANTI_DOWN,
        ParticleType.STRANGE: ParticleType.ANTI_STRANGE,
        ParticleType.CHARM: ParticleType.ANTI_CHARM,
        ParticleType.BOTTOM: ParticleType.ANTI_BOTTOM,
        ParticleType.TOP: ParticleType.ANTI_TOP,
        ParticleType.GHOST: ParticleType.ANTIGHOST,
    }
    if ptype in pairs:
        return pairs[ptype]
    inv = {v: k for k, v in pairs.items()}
    if ptype in inv:
        return inv[ptype]
    return ptype  # self-conjugate (photon, gluon)


def propagator_family(ptype: ParticleType) -> str:
    """
    Return the propagator family for self-containment checking.
    Two particle types are 'same family' if a propagator correction
    for one can contain the other as an internal line creating
    self-containment.
    """
    if ptype in LEPTON_TYPES:
        # Distinguish by generation for precise tracking
        if ptype in {ParticleType.ELECTRON, ParticleType.POSITRON}:
            return "electron"
        if ptype in {ParticleType.MUON, ParticleType.ANTIMUON}:
            return "muon"
        return "tau"
    if ptype in QUARK_TYPES:
        for name, (p, ap) in {
            "up": (ParticleType.UP, ParticleType.ANTI_UP),
            "down": (ParticleType.DOWN, ParticleType.ANTI_DOWN),
            "strange": (ParticleType.STRANGE, ParticleType.ANTI_STRANGE),
            "charm": (ParticleType.CHARM, ParticleType.ANTI_CHARM),
            "bottom": (ParticleType.BOTTOM, ParticleType.ANTI_BOTTOM),
            "top": (ParticleType.TOP, ParticleType.ANTI_TOP),
        }.items():
            if ptype in {p, ap}:
                return name
    if ptype == ParticleType.PHOTON:
        return "photon"
    if ptype == ParticleType.GLUON:
        return "gluon"
    if ptype in GHOST_TYPES:
        return "ghost"
    return "unknown"


@dataclass
class Particle:
    """A particle with its quantum numbers (the 'set' representation)."""
    ptype: ParticleType
    momentum: Optional[tuple] = None  # 4-momentum (E, px, py, pz)
    color: Optional[int] = None       # color index (1,2,3 for quarks; 1-8 for gluons)
    spin: Optional[float] = None      # spin projection

    @property
    def mass(self) -> float:
        """Return particle mass in GeV."""
        masses = {
            "electron": 0.000511, "muon": 0.10566, "tau": 1.777,
            "up": 0.0022, "down": 0.0047, "strange": 0.095,
            "charm": 1.275, "bottom": 4.18, "top": 173.0,
            "photon": 0.0, "gluon": 0.0, "ghost": 0.0,
        }
        return masses.get(propagator_family(self.ptype), 0.0)

    @property
    def charge(self) -> float:
        """Return electric charge in units of e."""
        charges = {
            ParticleType.ELECTRON: -1, ParticleType.POSITRON: +1,
            ParticleType.MUON: -1, ParticleType.ANTIMUON: +1,
            ParticleType.TAU: -1, ParticleType.ANTITAU: +1,
            ParticleType.UP: 2/3, ParticleType.ANTI_UP: -2/3,
            ParticleType.DOWN: -1/3, ParticleType.ANTI_DOWN: 1/3,
            ParticleType.STRANGE: -1/3, ParticleType.ANTI_STRANGE: 1/3,
            ParticleType.CHARM: 2/3, ParticleType.ANTI_CHARM: -2/3,
            ParticleType.BOTTOM: -1/3, ParticleType.ANTI_BOTTOM: 1/3,
            ParticleType.TOP: 2/3, ParticleType.ANTI_TOP: -2/3,
            ParticleType.PHOTON: 0, ParticleType.GLUON: 0,
            ParticleType.GHOST: 0, ParticleType.ANTIGHOST: 0,
        }
        return charges.get(self.ptype, 0.0)

    @property
    def family(self) -> str:
        return propagator_family(self.ptype)

    def is_fermion(self) -> bool:
        return self.ptype in FERMION_TYPES

    def is_boson(self) -> bool:
        return self.ptype in GAUGE_BOSON_TYPES

    def is_ghost(self) -> bool:
        return self.ptype in GHOST_TYPES
