"""
Physical SCN classification (skeleton expansion).

Determines which Feynman diagrams survive under Physical SCN:
- Skeleton diagrams (no self-energy insertions) → SURVIVE
- Diagrams with self-energy sub-insertions → NULLIFIED

This replaces the hand-coded classify() in scn_models.py with
proper subdiagram analysis.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from .topology import DiagramTopology, CorrectionType


class Verdict(Enum):
    SURVIVES = "survives"
    NULLIFIED = "nullified"


@dataclass
class ClassificationResult:
    diagram_name: str
    verdict: Verdict
    reason: str
    weight: float   # 1.0 for survives, 0.0 for nullified

    @property
    def survives(self) -> bool:
        return self.verdict == Verdict.SURVIVES


def classify_physical_scn(diagram: DiagramTopology) -> ClassificationResult:
    """
    Classify a diagram under Physical SCN (skeleton expansion).

    Rules:
    1. Tree-level diagrams always survive.
    2. 1-loop diagrams always survive (all are 1PI/skeleton).
    3. ≥ 2-loop diagrams survive iff they have NO self-energy
       sub-insertions (i.e., they are skeleton diagrams).

    This is equivalent to: use only bare propagators G₀ and 1PI
    self-energy Σ, without iterating the Dyson equation.
    """
    # Tree-level: always survives
    if diagram.loop_order == 0:
        return ClassificationResult(
            diagram.name, Verdict.SURVIVES,
            "Tree-level diagram", 1.0,
        )

    # 1-loop: all diagrams are skeleton (no room for nested insertions)
    if diagram.loop_order == 1:
        return ClassificationResult(
            diagram.name, Verdict.SURVIVES,
            "1-loop diagram — all are 1PI/skeleton by construction", 1.0,
        )

    # ≥ 2-loop: check for self-energy sub-insertions
    if diagram.has_se_insertion:
        se_subs = [
            sd for sd in diagram.subdiagrams
            if sd.correction_type == CorrectionType.SELF_ENERGY
        ]
        reasons = [sd.label or f"SE insertion on {sd.corrected_propagator.value}"
                   for sd in se_subs]
        return ClassificationResult(
            diagram.name, Verdict.NULLIFIED,
            f"Contains self-energy insertion(s): {'; '.join(reasons)}",
            0.0,
        )

    # Skeleton diagram (may contain VP insertions, which are fine)
    if diagram.is_skeleton is not None and not diagram.is_skeleton:
        # Explicit non-skeleton marking (safety catch)
        return ClassificationResult(
            diagram.name, Verdict.NULLIFIED,
            "Explicitly marked as non-skeleton", 0.0,
        )

    return ClassificationResult(
        diagram.name, Verdict.SURVIVES,
        "Skeleton diagram — no self-energy insertions", 1.0,
    )


def classify_all(diagrams: list[DiagramTopology]) -> list[ClassificationResult]:
    """Classify a list of diagrams under Physical SCN."""
    return [classify_physical_scn(d) for d in diagrams]


def partition(diagrams: list[DiagramTopology]) -> tuple[list[DiagramTopology],
                                                         list[DiagramTopology]]:
    """Split diagrams into (surviving, nullified) under Physical SCN."""
    surviving = []
    nullified = []
    for d in diagrams:
        result = classify_physical_scn(d)
        if result.survives:
            surviving.append(d)
        else:
            nullified.append(d)
    return surviving, nullified
