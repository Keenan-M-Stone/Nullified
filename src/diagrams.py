"""
Feynman diagram representation and graph operations.

Diagrams are represented as labeled graphs where:
- Nodes are vertices (interaction points)
- Edges are propagators (particle lines)
- Labels carry particle type and momentum information
"""

from dataclasses import dataclass, field
from typing import Optional
from .particles import ParticleType, InteractionType, propagator_family


@dataclass
class Propagator:
    """An edge in a Feynman diagram representing a particle propagator."""
    id: int
    particle_type: ParticleType
    vertex_from: int  # vertex id
    vertex_to: int    # vertex id
    is_external: bool = False
    momentum: Optional[tuple] = None

    @property
    def family(self) -> str:
        return propagator_family(self.particle_type)


@dataclass
class Vertex:
    """A node in a Feynman diagram representing an interaction vertex."""
    id: int
    interaction_type: InteractionType
    propagator_ids: list = field(default_factory=list)


@dataclass
class FeynmanDiagram:
    """
    A Feynman diagram represented as a labeled graph.

    Attributes:
        name: Human-readable name for the diagram
        vertices: Dict of vertex_id -> Vertex
        propagators: Dict of propagator_id -> Propagator
        loop_order: Number of independent loops
        process: Description of the physical process
        correction_type: What this diagram corrects (propagator type or vertex type)
        correction_family: The propagator family being corrected (for self-containment check)
    """
    name: str
    vertices: dict = field(default_factory=dict)
    propagators: dict = field(default_factory=dict)
    loop_order: int = 0
    process: str = ""
    correction_type: str = ""       # "self-energy", "vacuum-polarization", "vertex", "tree"
    correction_family: str = ""     # e.g., "electron", "photon", "gluon"

    def add_vertex(self, vid: int, interaction_type: InteractionType) -> Vertex:
        v = Vertex(id=vid, interaction_type=interaction_type)
        self.vertices[vid] = v
        return v

    def add_propagator(self, pid: int, ptype: ParticleType,
                       v_from: int, v_to: int,
                       is_external: bool = False) -> Propagator:
        p = Propagator(id=pid, particle_type=ptype,
                       vertex_from=v_from, vertex_to=v_to,
                       is_external=is_external)
        self.propagators[pid] = p
        if v_from in self.vertices:
            self.vertices[v_from].propagator_ids.append(pid)
        if v_to in self.vertices:
            self.vertices[v_to].propagator_ids.append(pid)
        return p

    def internal_propagators(self) -> list:
        return [p for p in self.propagators.values() if not p.is_external]

    def external_propagators(self) -> list:
        return [p for p in self.propagators.values() if p.is_external]

    def internal_families(self) -> set:
        """Return the set of propagator families used in internal lines."""
        return {p.family for p in self.internal_propagators()}

    def contains_family_internally(self, family: str) -> bool:
        """Check if the diagram contains an internal propagator of the given family."""
        return family in self.internal_families()


# ============================================================
# Standard QED diagrams at one loop
# ============================================================

def make_tree_ee_to_mumu() -> FeynmanDiagram:
    """Tree-level e+e- → μ+μ- via virtual photon."""
    d = FeynmanDiagram(
        name="e+e- → γ* → μ+μ- (tree)",
        loop_order=0,
        process="e+e- → μ+μ-",
        correction_type="tree",
    )
    d.add_vertex(1, InteractionType.QED_VERTEX)
    d.add_vertex(2, InteractionType.QED_VERTEX)
    # External legs
    d.add_propagator(1, ParticleType.ELECTRON, -1, 1, is_external=True)
    d.add_propagator(2, ParticleType.POSITRON, -1, 1, is_external=True)
    d.add_propagator(3, ParticleType.MUON, 2, -1, is_external=True)
    d.add_propagator(4, ParticleType.ANTIMUON, 2, -1, is_external=True)
    # Internal photon
    d.add_propagator(5, ParticleType.PHOTON, 1, 2)
    return d


def make_electron_self_energy() -> FeynmanDiagram:
    """One-loop electron self-energy: e → eγ → e."""
    d = FeynmanDiagram(
        name="Electron self-energy (1-loop)",
        loop_order=1,
        process="electron propagator correction",
        correction_type="self-energy",
        correction_family="electron",
    )
    d.add_vertex(1, InteractionType.QED_VERTEX)
    d.add_vertex(2, InteractionType.QED_VERTEX)
    # External electron legs
    d.add_propagator(1, ParticleType.ELECTRON, -1, 1, is_external=True)
    d.add_propagator(2, ParticleType.ELECTRON, 2, -1, is_external=True)
    # Internal lines: electron + photon loop
    d.add_propagator(3, ParticleType.ELECTRON, 1, 2)  # internal electron
    d.add_propagator(4, ParticleType.PHOTON, 1, 2)    # internal photon (loop)
    return d


def make_vacuum_polarization() -> FeynmanDiagram:
    """One-loop vacuum polarization: γ → e+e- → γ."""
    d = FeynmanDiagram(
        name="Vacuum polarization (1-loop)",
        loop_order=1,
        process="photon propagator correction",
        correction_type="vacuum-polarization",
        correction_family="photon",
    )
    d.add_vertex(1, InteractionType.QED_VERTEX)
    d.add_vertex(2, InteractionType.QED_VERTEX)
    # External photon legs
    d.add_propagator(1, ParticleType.PHOTON, -1, 1, is_external=True)
    d.add_propagator(2, ParticleType.PHOTON, 2, -1, is_external=True)
    # Internal electron-positron loop
    d.add_propagator(3, ParticleType.ELECTRON, 1, 2)
    d.add_propagator(4, ParticleType.POSITRON, 2, 1)
    return d


def make_vertex_correction() -> FeynmanDiagram:
    """One-loop QED vertex correction (Schwinger term)."""
    d = FeynmanDiagram(
        name="Vertex correction (1-loop, Schwinger)",
        loop_order=1,
        process="QED vertex correction",
        correction_type="vertex",
        correction_family="qed-vertex",
    )
    d.add_vertex(1, InteractionType.QED_VERTEX)
    d.add_vertex(2, InteractionType.QED_VERTEX)
    d.add_vertex(3, InteractionType.QED_VERTEX)
    # External legs
    d.add_propagator(1, ParticleType.ELECTRON, -1, 1, is_external=True)
    d.add_propagator(2, ParticleType.ELECTRON, 3, -1, is_external=True)
    d.add_propagator(3, ParticleType.PHOTON, 2, -1, is_external=True)
    # Internal: triangle with virtual photon
    d.add_propagator(4, ParticleType.ELECTRON, 1, 2)  # fermion line
    d.add_propagator(5, ParticleType.ELECTRON, 2, 3)  # fermion line
    d.add_propagator(6, ParticleType.PHOTON, 1, 3)    # virtual photon
    return d


# ============================================================
# Standard QCD diagrams at one loop
# ============================================================

def make_quark_self_energy() -> FeynmanDiagram:
    """One-loop quark self-energy: q → qg → q."""
    d = FeynmanDiagram(
        name="Quark self-energy (1-loop)",
        loop_order=1,
        process="quark propagator correction",
        correction_type="self-energy",
        correction_family="up",  # representative quark
    )
    d.add_vertex(1, InteractionType.QCD_QQG_VERTEX)
    d.add_vertex(2, InteractionType.QCD_QQG_VERTEX)
    d.add_propagator(1, ParticleType.UP, -1, 1, is_external=True)
    d.add_propagator(2, ParticleType.UP, 2, -1, is_external=True)
    d.add_propagator(3, ParticleType.UP, 1, 2)       # internal quark
    d.add_propagator(4, ParticleType.GLUON, 1, 2)    # internal gluon
    return d


def make_gluon_self_energy_quark_loop() -> FeynmanDiagram:
    """One-loop gluon self-energy: g → qq̄ → g (quark loop)."""
    d = FeynmanDiagram(
        name="Gluon self-energy – quark loop (1-loop)",
        loop_order=1,
        process="gluon propagator correction (quark loop)",
        correction_type="vacuum-polarization",
        correction_family="gluon",
    )
    d.add_vertex(1, InteractionType.QCD_QQG_VERTEX)
    d.add_vertex(2, InteractionType.QCD_QQG_VERTEX)
    d.add_propagator(1, ParticleType.GLUON, -1, 1, is_external=True)
    d.add_propagator(2, ParticleType.GLUON, 2, -1, is_external=True)
    d.add_propagator(3, ParticleType.UP, 1, 2)
    d.add_propagator(4, ParticleType.ANTI_UP, 2, 1)
    return d


def make_gluon_self_energy_gluon_loop() -> FeynmanDiagram:
    """One-loop gluon self-energy: g → gg → g (gluon loop)."""
    d = FeynmanDiagram(
        name="Gluon self-energy – gluon loop (1-loop)",
        loop_order=1,
        process="gluon propagator correction (gluon loop)",
        correction_type="self-energy",
        correction_family="gluon",
    )
    d.add_vertex(1, InteractionType.QCD_GGG_VERTEX)
    d.add_vertex(2, InteractionType.QCD_GGG_VERTEX)
    d.add_propagator(1, ParticleType.GLUON, -1, 1, is_external=True)
    d.add_propagator(2, ParticleType.GLUON, 2, -1, is_external=True)
    d.add_propagator(3, ParticleType.GLUON, 1, 2)  # internal gluon
    d.add_propagator(4, ParticleType.GLUON, 2, 1)  # internal gluon
    return d


def make_gluon_self_energy_ghost_loop() -> FeynmanDiagram:
    """One-loop gluon self-energy: g → cc̄ → g (ghost loop)."""
    d = FeynmanDiagram(
        name="Gluon self-energy – ghost loop (1-loop)",
        loop_order=1,
        process="gluon propagator correction (ghost loop)",
        correction_type="vacuum-polarization",
        correction_family="gluon",
    )
    d.add_vertex(1, InteractionType.QCD_GHOST_VERTEX)
    d.add_vertex(2, InteractionType.QCD_GHOST_VERTEX)
    d.add_propagator(1, ParticleType.GLUON, -1, 1, is_external=True)
    d.add_propagator(2, ParticleType.GLUON, 2, -1, is_external=True)
    d.add_propagator(3, ParticleType.GHOST, 1, 2)
    d.add_propagator(4, ParticleType.ANTIGHOST, 2, 1)
    return d


def get_all_one_loop_qed() -> list:
    """Return all one-loop QED diagrams."""
    return [
        make_electron_self_energy(),
        make_vacuum_polarization(),
        make_vertex_correction(),
    ]


def get_all_one_loop_qcd() -> list:
    """Return all one-loop QCD gluon self-energy diagrams."""
    return [
        make_quark_self_energy(),
        make_gluon_self_energy_quark_loop(),
        make_gluon_self_energy_gluon_loop(),
        make_gluon_self_energy_ghost_loop(),
    ]
