"""
QED Feynman diagram topologies at 1-loop and 2-loop.

Rather than a general-purpose diagram generator, this module encodes
the known QED diagram topologies for the anomalous magnetic moment
and e+e- → μ+μ- at 1- and 2-loop order.

Each topology is described by its structure (what propagators appear,
what subdiagrams it contains) — enough for Physical SCN classification
and amplitude computation.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class CorrectionType(Enum):
    SELF_ENERGY = "self-energy"
    VACUUM_POL = "vacuum-polarization"
    VERTEX = "vertex"
    BOX = "box"
    TREE = "tree"


class PropagatorType(Enum):
    FERMION = "fermion"
    PHOTON = "photon"


@dataclass
class SubDiagram:
    """A sub-diagram embedded within a larger diagram."""
    correction_type: CorrectionType
    corrected_propagator: PropagatorType
    loop_order: int
    label: str = ""


@dataclass
class DiagramTopology:
    """
    A Feynman diagram topology with enough structure for SCN classification.

    Attributes:
        name:           Human-readable identifier (e.g. "III(a)")
        loop_order:     Number of independent loops
        correction_type: What this diagram is (vertex, SE, VP, ...)
        internal_propagators: Types of internal propagators
        subdiagrams:    List of identifiable sub-diagrams
        is_skeleton:    Whether this is a skeleton diagram (no SE insertions)
        standard_contribution: Known contribution to the observable (if available)
        description:    Free-form description
    """
    name: str
    loop_order: int
    correction_type: CorrectionType
    internal_propagators: list[PropagatorType] = field(default_factory=list)
    subdiagrams: list[SubDiagram] = field(default_factory=list)
    is_skeleton: Optional[bool] = None
    standard_contribution: Optional[float] = None
    description: str = ""

    @property
    def has_se_insertion(self) -> bool:
        """Check if any subdiagram is a self-energy insertion."""
        return any(
            sd.correction_type == CorrectionType.SELF_ENERGY
            for sd in self.subdiagrams
        )

    @property
    def has_vp_insertion(self) -> bool:
        return any(
            sd.correction_type == CorrectionType.VACUUM_POL
            for sd in self.subdiagrams
        )


# ── Known QED vertex diagrams (g-2) ────────────────────────

def qed_vertex_diagrams(loop_order: int) -> list[DiagramTopology]:
    """Return all QED vertex diagrams at the given loop order."""
    if loop_order == 1:
        return _one_loop_vertex_diagrams()
    elif loop_order == 2:
        return _two_loop_vertex_diagrams()
    else:
        raise ValueError(f"Loop order {loop_order} not implemented")


def _one_loop_vertex_diagrams() -> list[DiagramTopology]:
    return [
        DiagramTopology(
            name="Schwinger",
            loop_order=1,
            correction_type=CorrectionType.VERTEX,
            internal_propagators=[PropagatorType.FERMION, PropagatorType.FERMION,
                                  PropagatorType.PHOTON],
            subdiagrams=[],
            is_skeleton=True,
            standard_contribution=0.5,  # coefficient of α/π
            description="One-loop vertex correction (triangle diagram). "
                        "Gives a_e = α/(2π) = 0.5 × (α/π).",
        ),
    ]


def _two_loop_vertex_diagrams() -> list[DiagramTopology]:
    """
    The 7 two-loop QED vertex diagrams contributing to a_e.

    Standard labeling follows Petermann (1957) / Sommerfield (1957):
      I(a), I(b), I(c)  — self-energy insertion diagrams
      II                 — vacuum polarization insertion
      III(a)             — crossed photon exchange
      III(b)             — ladder (uncrossed double photon)
      III(c)             — light-by-light scattering insertion

    Individual contributions from Laporta & Remiddi (1996) and
    Petermann (1957), in units of (α/π)²:

    The TOTAL is C₂ = 197/144 + π²(½ ln 2 - 3/4)/3 + 3ζ(3)/4 - π²/2
                     = -0.328478965579...

    Individual diagram contributions (gauge-dependent in general;
    these are in Feynman gauge, on-shell scheme):
    """

    # Individual 2-loop contributions to a_e / (α/π)²
    # From Petermann (1957) table, Feynman gauge, on-shell renormalization:
    #
    # The SE-insertion diagrams I(a-c) together with their mass/wavefunction
    # counterterms contribute a known combined amount.
    # The remaining skeleton diagrams (II, III(a-c)) contribute the rest.
    #
    # Splitting: (values from Laporta 1993, Czarnecki & Melnikov 2000)
    #   SE insertions (I(a) + I(b) + I(c)) + counterterms:
    #     Combined finite remainder ≈ 0.7714... in units of (α/π)²
    #   Skeleton diagrams (II + III(a) + III(b) + III(c)):
    #     Combined ≈ -1.0999... in units of (α/π)²
    #   Total: -0.3285...
    #
    # NOTE: Individual diagram values are scheme- and gauge-dependent.
    # Only the total C₂ and the skeleton vs non-skeleton split are
    # physically meaningful under Physical SCN.

    SE_INSERTION_TOTAL = 0.7714    # SE insertions + counterterms (approx)
    C2_TOTAL = -0.328478965579
    SKELETON_TOTAL = C2_TOTAL - SE_INSERTION_TOTAL  # ≈ -1.0999

    return [
        # Group I: Self-energy insertions
        DiagramTopology(
            name="I(a)",
            loop_order=2,
            correction_type=CorrectionType.VERTEX,
            internal_propagators=[PropagatorType.FERMION, PropagatorType.PHOTON,
                                  PropagatorType.FERMION, PropagatorType.PHOTON],
            subdiagrams=[SubDiagram(
                CorrectionType.SELF_ENERGY, PropagatorType.FERMION, 1,
                "1-loop electron SE on upper fermion line",
            )],
            is_skeleton=False,
            standard_contribution=None,  # individual value gauge-dependent
            description="SE insertion on upper external fermion line.",
        ),
        DiagramTopology(
            name="I(b)",
            loop_order=2,
            correction_type=CorrectionType.VERTEX,
            internal_propagators=[PropagatorType.FERMION, PropagatorType.PHOTON,
                                  PropagatorType.FERMION, PropagatorType.PHOTON],
            subdiagrams=[SubDiagram(
                CorrectionType.SELF_ENERGY, PropagatorType.FERMION, 1,
                "1-loop electron SE on lower fermion line",
            )],
            is_skeleton=False,
            standard_contribution=None,
            description="SE insertion on lower external fermion line.",
        ),
        DiagramTopology(
            name="I(c)",
            loop_order=2,
            correction_type=CorrectionType.VERTEX,
            internal_propagators=[PropagatorType.FERMION, PropagatorType.PHOTON,
                                  PropagatorType.FERMION, PropagatorType.PHOTON],
            subdiagrams=[SubDiagram(
                CorrectionType.SELF_ENERGY, PropagatorType.FERMION, 1,
                "1-loop electron SE on internal fermion line",
            )],
            is_skeleton=False,
            standard_contribution=None,
            description="SE insertion on internal fermion line.",
        ),

        # Group II: Vacuum polarization insertion
        DiagramTopology(
            name="II",
            loop_order=2,
            correction_type=CorrectionType.VERTEX,
            internal_propagators=[PropagatorType.FERMION, PropagatorType.PHOTON,
                                  PropagatorType.FERMION],
            subdiagrams=[SubDiagram(
                CorrectionType.VACUUM_POL, PropagatorType.PHOTON, 1,
                "1-loop vacuum polarization on internal photon",
            )],
            is_skeleton=True,  # VP insertion is a skeleton diagram
            standard_contribution=None,
            description="VP insertion on internal photon line. "
                        "Skeleton: VP is 1PI, no fermion SE insertion.",
        ),

        # Group III: Genuine two-loop vertex topologies
        DiagramTopology(
            name="III(a)",
            loop_order=2,
            correction_type=CorrectionType.VERTEX,
            internal_propagators=[PropagatorType.FERMION, PropagatorType.PHOTON,
                                  PropagatorType.FERMION, PropagatorType.PHOTON,
                                  PropagatorType.FERMION],
            subdiagrams=[],
            is_skeleton=True,
            standard_contribution=None,
            description="Crossed photon exchange (two virtual photons, crossed).",
        ),
        DiagramTopology(
            name="III(b)",
            loop_order=2,
            correction_type=CorrectionType.VERTEX,
            internal_propagators=[PropagatorType.FERMION, PropagatorType.PHOTON,
                                  PropagatorType.FERMION, PropagatorType.PHOTON,
                                  PropagatorType.FERMION],
            subdiagrams=[],
            is_skeleton=True,
            standard_contribution=None,
            description="Ladder diagram (two virtual photons, uncrossed).",
        ),
        DiagramTopology(
            name="III(c)",
            loop_order=2,
            correction_type=CorrectionType.VERTEX,
            internal_propagators=[PropagatorType.FERMION, PropagatorType.PHOTON,
                                  PropagatorType.FERMION, PropagatorType.PHOTON,
                                  PropagatorType.FERMION, PropagatorType.PHOTON,
                                  PropagatorType.FERMION],
            subdiagrams=[SubDiagram(
                CorrectionType.VACUUM_POL, PropagatorType.PHOTON, 1,
                "Light-by-light fermion box",
            )],
            is_skeleton=True,
            standard_contribution=None,
            description="Light-by-light scattering insertion. "
                        "Skeleton: the fermion box is a new topology, not a SE insertion.",
        ),
    ]


# ── Known QED self-energy diagrams ──────────────────────────

def qed_self_energy_diagrams(loop_order: int) -> list[DiagramTopology]:
    """Return QED electron self-energy diagrams."""
    if loop_order == 1:
        return [
            DiagramTopology(
                name="Σ₁",
                loop_order=1,
                correction_type=CorrectionType.SELF_ENERGY,
                internal_propagators=[PropagatorType.FERMION, PropagatorType.PHOTON],
                subdiagrams=[],
                is_skeleton=True,
                description="1-loop electron self-energy. 1PI → skeleton.",
            ),
        ]
    raise ValueError(f"Loop order {loop_order} SE diagrams not implemented")


def qed_vacuum_pol_diagrams(loop_order: int) -> list[DiagramTopology]:
    """Return QED vacuum polarization diagrams."""
    if loop_order == 1:
        return [
            DiagramTopology(
                name="Π₁",
                loop_order=1,
                correction_type=CorrectionType.VACUUM_POL,
                internal_propagators=[PropagatorType.FERMION, PropagatorType.FERMION],
                subdiagrams=[],
                is_skeleton=True,
                description="1-loop vacuum polarization (fermion loop).",
            ),
        ]
    raise ValueError(f"Loop order {loop_order} VP diagrams not implemented")
