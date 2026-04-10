"""
Self-Containment Nullification (SCN) filter for Feynman diagrams.

Implements the core SCN axiom: diagrams whose radiative corrections
internally reference the same propagator family being corrected are
classified as self-containing and nullified.
"""

from .diagrams import FeynmanDiagram


def is_self_containing(diagram: FeynmanDiagram) -> bool:
    """
    Check if a Feynman diagram is self-containing under SCN.

    A diagram is self-containing if:
    1. It is a radiative correction to a propagator (correction_type == "self-energy")
    2. It contains an internal propagator of the SAME family as the propagator
       being corrected (correction_family).

    Tree-level diagrams and vacuum-polarization diagrams (where the internal
    loop is a different particle type) are never self-containing.

    Vertex corrections are not self-containing at one loop (they contain
    tree-level vertices, not nested vertex corrections).
    """
    # Tree-level: never self-containing
    if diagram.loop_order == 0:
        return False

    # Only self-energy corrections can be self-containing
    # Vacuum polarization (loop of different particle type) is not self-containing
    if diagram.correction_type != "self-energy":
        return False

    # Check if any internal propagator matches the corrected propagator family
    corrected_family = diagram.correction_family
    if not corrected_family:
        return False

    return diagram.contains_family_internally(corrected_family)


def scn_filter(diagrams: list) -> tuple:
    """
    Apply SCN filter to a list of Feynman diagrams.

    Returns:
        (surviving, nullified): Two lists of diagrams
    """
    surviving = []
    nullified = []

    for d in diagrams:
        if is_self_containing(d):
            nullified.append(d)
        else:
            surviving.append(d)

    return surviving, nullified


def scn_report(diagrams: list) -> str:
    """Generate a human-readable report of SCN filtering results."""
    surviving, nullified = scn_filter(diagrams)

    lines = ["=" * 60]
    lines.append("SCN FILTER REPORT")
    lines.append("=" * 60)
    lines.append(f"Total diagrams:     {len(diagrams)}")
    lines.append(f"Surviving:          {len(surviving)}")
    lines.append(f"Nullified:          {len(nullified)}")
    lines.append("")

    if surviving:
        lines.append("--- SURVIVING DIAGRAMS ---")
        for d in surviving:
            lines.append(f"  ✓ {d.name}")
            lines.append(f"    Type: {d.correction_type}, Family: {d.correction_family}")
            lines.append(f"    Internal families: {d.internal_families()}")
            lines.append("")

    if nullified:
        lines.append("--- NULLIFIED DIAGRAMS (self-containing) ---")
        for d in nullified:
            lines.append(f"  ✗ {d.name}")
            lines.append(f"    Type: {d.correction_type}, Family: {d.correction_family}")
            lines.append(f"    Internal families: {d.internal_families()}")
            reason = f"    Reason: correction to '{d.correction_family}' propagator "
            reason += f"uses internal '{d.correction_family}' propagator"
            lines.append(reason)
            lines.append("")

    lines.append("=" * 60)
    return "\n".join(lines)
