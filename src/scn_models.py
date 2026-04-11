"""
SCN Formulation Models.

Implements four interpretations of Self-Containment Nullification,
each with hard and soft variants:

1. Literal    — S ∈ S strictly; only resummed/Dyson structures are self-referential
2. Structural — diagram contains sub-structure isomorphic to what it corrects
3. Diagrammatic — self-energy of X contains internal X propagator (original)
4. Physical   — self-containment at the Dyson/dressed-propagator level

Each model provides:
- classify(diagram, mu) → SCNResult  — fate of a single diagram
- filter(diagrams, mu) → dict        — batch classification
- beta_0_qcd(nf) → float            — QCD beta-function coefficient
- g2_components(loop_order) → dict   — g-2 survival table
- lamb_shift_components() → dict     — Lamb-shift survival table
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Optional

import numpy as np

from .diagrams import FeynmanDiagram


# ── Result types ────────────────────────────────────────────

class SCNVerdict(Enum):
    SURVIVES = "survives"
    NULLIFIED = "nullified"
    SUPPRESSED = "suppressed"


@dataclass
class SCNResult:
    verdict: SCNVerdict
    suppression: float      # 1.0 = full pass, 0.0 = nullified, (0,1) = soft
    reason: str

    @property
    def survives(self) -> bool:
        return self.verdict == SCNVerdict.SURVIVES

    @property
    def amplitude_weight(self) -> float:
        return self.suppression


# ── QCD constants ───────────────────────────────────────────

C_A = 3.0
T_F = 0.5

# Standard β₀ decomposition at one loop:
#   gluon loop: 10 C_A / 3
#   ghost loop:  C_A / 3
#   quark loop: -4 T_F n_f / 3
# total: (11 C_A - 4 T_F n_f) / 3
GLUON_LOOP_COEFF = 10 * C_A / 3   # 10
GHOST_LOOP_COEFF = C_A / 3        # 1
QUARK_LOOP_COEFF_PER_NF = -4 * T_F / 3  # -2/3


# ── Base class ──────────────────────────────────────────────

class SCNModel:
    """Base SCN formulation. Subclass and override _is_self_containing."""

    key: str = "base"

    def __init__(self, *, soft: bool = False, lambda_scn: float = 0.1):
        self.soft = soft
        self.lambda_scn = lambda_scn   # GeV, soft-suppression scale

    # ── public API ──────────────────────────────────────────

    @property
    def name(self) -> str:
        mode = f"Soft (Λ={self.lambda_scn} GeV)" if self.soft else "Hard"
        return f"{self._label} — {mode}"

    @property
    def short_name(self) -> str:
        suffix = "S" if self.soft else "H"
        return f"{self.key.upper()}-{suffix}"

    def classify(self, diagram: FeynmanDiagram, mu: Optional[float] = None) -> SCNResult:
        is_sc, reason = self._is_self_containing(diagram)
        if not is_sc:
            return SCNResult(SCNVerdict.SURVIVES, 1.0, reason)
        if self.soft and mu is not None:
            eta = self._soft_factor(mu)
            return SCNResult(
                SCNVerdict.SUPPRESSED, eta,
                f"{reason} | η({mu:.2f} GeV) = {eta:.4f}",
            )
        if self.soft and mu is None:
            return SCNResult(
                SCNVerdict.SUPPRESSED, 0.5,
                f"{reason} | soft, no μ given (using η=0.5)",
            )
        return SCNResult(SCNVerdict.NULLIFIED, 0.0, reason)

    def filter(self, diagrams: list[FeynmanDiagram],
               mu: Optional[float] = None) -> dict[str, SCNResult]:
        return {d.name: self.classify(d, mu) for d in diagrams}

    def beta_0_qcd(self, nf: int) -> float:
        raise NotImplementedError

    def g2_components(self, loop_order: int = 1) -> dict:
        """Return dict of diagram-type → survives/nullified at given loop order."""
        raise NotImplementedError

    def lamb_shift_components(self) -> dict:
        """Return dict with Lamb-shift component survival status."""
        raise NotImplementedError

    # ── internals ───────────────────────────────────────────

    _label: str = "Base SCN"

    def _is_self_containing(self, diagram: FeynmanDiagram) -> tuple[bool, str]:
        raise NotImplementedError

    def _soft_factor(self, mu: float) -> float:
        return 1.0 - np.exp(-(mu / self.lambda_scn) ** 2)

    def __repr__(self):
        return f"<{self.name}>"


# ── 1. Literal SCN ─────────────────────────────────────────

class LiteralSCN(SCNModel):
    """
    S ∈ S in the strictest sense.

    In perturbation theory every diagram is a *finite* combinatorial
    object — it cannot literally contain itself as a sub-object.
    Only the Dyson-resummed full propagator G = G₀ + G₀ Σ G is
    genuinely self-referential (G appears on both sides).

    Consequence: **no** perturbative diagram is nullified. Only
    non-perturbative / resummed structures are affected.
    """

    key = "lit"
    _label = "Literal"

    def _is_self_containing(self, diagram):
        # A perturbative diagram is never literally self-containing.
        # Mark if it carries a "resummed" flag (we add this for Dyson tests).
        if getattr(diagram, "is_resummed", False):
            return True, "Resummed / Dyson structure — literally self-referential"
        return False, "Finite perturbative diagram — not literally self-containing"

    def beta_0_qcd(self, nf):
        # Everything survives → standard result
        return (11 * C_A - 4 * T_F * nf) / 3

    def g2_components(self, loop_order=1):
        # Everything survives at every perturbative order
        return {
            "self_energy": {"survives": True, "weight": 1.0},
            "vacuum_pol": {"survives": True, "weight": 1.0},
            "vertex": {"survives": True, "weight": 1.0},
        }

    def lamb_shift_components(self):
        return {
            "self_energy": {"survives": True, "weight": 1.0,
                            "standard_MHz": 1017.0},
            "vacuum_pol": {"survives": True, "weight": 1.0,
                           "standard_MHz": -27.1},
            "vertex": {"survives": True, "weight": 1.0,
                       "standard_MHz": 67.0},
        }


# ── 2. Structural SCN ──────────────────────────────────────

class StructuralSCN(SCNModel):
    """
    A diagram is self-containing when it contains a sub-structure
    *isomorphic* to what it is correcting.

    For self-energy diagrams: any internal sub-graph that is itself a
    self-energy correction of the *same* correction type counts.
    At 1-loop this matches Diagrammatic (an internal propagator of the
    same family IS a sub-structure of the required type).

    For vertex corrections at 2+ loops: a nested vertex correction of
    the same interaction type is also self-containing (broader than
    Diagrammatic).
    """

    key = "str"
    _label = "Structural"

    def _is_self_containing(self, diagram):
        if diagram.loop_order == 0:
            return False, "Tree-level"

        # Self-energy: contains same-family propagator → isomorphic sub-structure
        if diagram.correction_type == "self-energy":
            if diagram.contains_family_internally(diagram.correction_family):
                return True, (
                    f"Self-energy of '{diagram.correction_family}' has internal "
                    f"'{diagram.correction_family}' propagator (isomorphic sub-structure)"
                )

        # Vertex: contains nested vertex correction of same type (2+ loops)
        if diagram.correction_type == "vertex" and diagram.loop_order >= 2:
            if getattr(diagram, "has_nested_vertex", False):
                return True, (
                    "Vertex correction contains nested vertex correction "
                    "of same interaction type"
                )

        return False, f"No isomorphic sub-structure for '{diagram.correction_type}'"

    def beta_0_qcd(self, nf):
        # Same as Diagrammatic at 1-loop:
        #   gluon-loop self-energy nullified, ghost + quark-loop survive
        return GHOST_LOOP_COEFF + QUARK_LOOP_COEFF_PER_NF * nf

    def g2_components(self, loop_order=1):
        if loop_order == 1:
            return {
                "self_energy": {"survives": False, "weight": 0.0},
                "vacuum_pol": {"survives": True, "weight": 1.0},
                "vertex": {"survives": True, "weight": 1.0},
            }
        # At 2-loop: structural also catches nested vertex corrections
        return {
            "self_energy": {"survives": False, "weight": 0.0},
            "vacuum_pol": {"survives": True, "weight": 1.0},
            "vertex": {"survives": False, "weight": 0.0,
                        "note": "nested vertex correction nullified"},
        }

    def lamb_shift_components(self):
        return {
            "self_energy": {"survives": False, "weight": 0.0,
                            "standard_MHz": 1017.0},
            "vacuum_pol": {"survives": True, "weight": 1.0,
                           "standard_MHz": -27.1},
            "vertex": {"survives": True, "weight": 1.0,
                       "standard_MHz": 67.0},
        }


# ── 3. Diagrammatic SCN ────────────────────────────────────

class DiagrammaticSCN(SCNModel):
    """
    The original/default formulation.

    A self-energy diagram for propagator family X is self-containing
    iff it has an internal propagator of family X.

    Vertex and vacuum-polarization diagrams are never self-containing
    at any order (they correct different objects than what appears
    internally).
    """

    key = "dia"
    _label = "Diagrammatic"

    def _is_self_containing(self, diagram):
        if diagram.loop_order == 0:
            return False, "Tree-level"
        if diagram.correction_type != "self-energy":
            return False, f"'{diagram.correction_type}' is not a self-energy"
        if not diagram.correction_family:
            return False, "No correction family set"
        if diagram.contains_family_internally(diagram.correction_family):
            return True, (
                f"Self-energy of '{diagram.correction_family}' uses internal "
                f"'{diagram.correction_family}' propagator"
            )
        internal = diagram.internal_families()
        return False, (
            f"Self-energy of '{diagram.correction_family}' but internals "
            f"are {internal}"
        )

    def beta_0_qcd(self, nf):
        # Gluon-loop gluon self-energy is nullified.
        # Ghost loop (VP) and quark loop (VP) survive.
        return GHOST_LOOP_COEFF + QUARK_LOOP_COEFF_PER_NF * nf

    def g2_components(self, loop_order=1):
        return {
            "self_energy": {"survives": False, "weight": 0.0},
            "vacuum_pol": {"survives": True, "weight": 1.0},
            "vertex": {"survives": True, "weight": 1.0},
        }

    def lamb_shift_components(self):
        return {
            "self_energy": {"survives": False, "weight": 0.0,
                            "standard_MHz": 1017.0},
            "vacuum_pol": {"survives": True, "weight": 1.0,
                           "standard_MHz": -27.1},
            "vertex": {"survives": True, "weight": 1.0,
                       "standard_MHz": 67.0},
        }


# ── 4. Physical SCN ────────────────────────────────────────

class PhysicalSCN(SCNModel):
    """
    Self-containment at the dressed-propagator / Dyson-equation level.

    G = G₀ + G₀ Σ G   ← self-referential (G on both sides).

    In perturbation theory, 1-loop self-energy contributions use
    *bare* propagators G₀ only, so they are NOT self-referential
    and **survive**.  Higher-loop diagrams with *nested* self-energy
    insertions (which effectively use corrected propagators) **are**
    self-referential and get nullified.

    This is the most conservative formulation at low orders: standard
    QED is recovered at 1-loop, with deviations appearing at 2+ loops.
    """

    key = "phy"
    _label = "Physical"

    def _is_self_containing(self, diagram):
        if diagram.loop_order == 0:
            return False, "Tree-level"

        if diagram.correction_type == "self-energy":
            if diagram.loop_order == 1:
                return False, (
                    "1-loop self-energy uses bare propagators — "
                    "not self-referential at the dressed level"
                )
            # ≥ 2-loop self-energy: assume nested self-energy insertions
            if getattr(diagram, "has_nested_self_energy", True):
                return True, (
                    f"{diagram.loop_order}-loop self-energy contains nested "
                    "self-energy insertion → uses corrected propagator"
                )

        return False, f"'{diagram.correction_type}' — not self-referential at physical level"

    def beta_0_qcd(self, nf):
        # At 1-loop: everything survives (bare propagators only)
        return (11 * C_A - 4 * T_F * nf) / 3

    def g2_components(self, loop_order=1):
        if loop_order == 1:
            return {
                "self_energy": {"survives": True, "weight": 1.0,
                                "note": "uses bare propagators"},
                "vacuum_pol": {"survives": True, "weight": 1.0},
                "vertex": {"survives": True, "weight": 1.0},
            }
        return {
            "self_energy": {"survives": False, "weight": 0.0,
                            "note": "nested self-energy insertion nullified"},
            "vacuum_pol": {"survives": True, "weight": 1.0},
            "vertex": {"survives": True, "weight": 1.0},
        }

    def lamb_shift_components(self):
        # 1-loop dominant self-energy survives
        return {
            "self_energy": {"survives": True, "weight": 1.0,
                            "standard_MHz": 1017.0,
                            "note": "1-loop; uses bare propagators"},
            "vacuum_pol": {"survives": True, "weight": 1.0,
                           "standard_MHz": -27.1},
            "vertex": {"survives": True, "weight": 1.0,
                       "standard_MHz": 67.0},
        }


# ── Factory helpers ─────────────────────────────────────────

ALL_MODEL_CLASSES = [LiteralSCN, StructuralSCN, DiagrammaticSCN, PhysicalSCN]


def make_all_models(*, soft: bool = False, lambda_scn: float = 0.1) -> list[SCNModel]:
    return [cls(soft=soft, lambda_scn=lambda_scn) for cls in ALL_MODEL_CLASSES]


def make_model(key: str, *, soft: bool = False, lambda_scn: float = 0.1) -> SCNModel:
    """Create a model by short key: 'lit', 'str', 'dia', 'phy'."""
    for cls in ALL_MODEL_CLASSES:
        if cls.key == key:
            return cls(soft=soft, lambda_scn=lambda_scn)
    raise ValueError(f"Unknown model key '{key}'. Choose from: "
                     f"{[c.key for c in ALL_MODEL_CLASSES]}")
