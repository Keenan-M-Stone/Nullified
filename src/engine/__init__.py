"""
SCN Simulation Engine.

Automated pipeline for computing QED observables under Physical SCN
(skeleton expansion):

  process  →  diagrams  →  classify  →  integrate  →  observables

Modules:
    process     — Scattering process definitions and kinematics
    topology    — QED Feynman diagram topologies at 1- and 2-loop
    classify    — Physical SCN classification (skeleton vs non-skeleton)
    integrals   — Passarino-Veltman scalar loop integrals
    amplitudes  — Diagram amplitude computation
    pipeline    — End-to-end orchestration
"""

from .process import Process, Particle
from .topology import DiagramTopology, qed_vertex_diagrams
from .classify import classify_physical_scn
from .pipeline import compute_g2, compute_cross_section
