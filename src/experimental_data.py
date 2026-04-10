"""
Experimental data for comparison with SCN predictions.

Contains measured values for key QED/QCD observables with uncertainties.
Sources: PDG (Particle Data Group), precision QED experiments.
"""

import numpy as np


def get_electron_g2_data() -> dict:
    """
    Electron anomalous magnetic moment experimental data and theory values.
    """
    return {
        "experiment": {
            "value": 0.00115965218059,
            "uncertainty": 0.00000000000013,
            "source": "Hanneke, Fogwell, Gabrielse (2008), updated 2023",
        },
        "standard_qed": {
            "1-loop": 0.5 * (1/137.035999) / np.pi,  # α/(2π)
            "2-loop_coefficient": -0.328478965,
            "3-loop_coefficient": 1.181241456,
            "total_to_4loop": 0.00115965218178,
            "source": "Aoyama et al. (2019)",
        },
        "scn_qed": {
            "1-loop": 0.5 * (1/137.035999) / np.pi,  # same as standard
            "2-loop_coefficient_estimate": -0.17,  # estimated, SE diagrams removed
            "note": "SCN removes self-energy-containing 2-loop diagrams",
        },
    }


def get_r_ratio_data() -> dict:
    """
    R-ratio experimental data at various energies.

    R = σ(e+e- → hadrons) / σ(e+e- → μ+μ-)

    Selected data points from various experiments.
    """
    # (√s in GeV, R value, R uncertainty)
    data_points = np.array([
        # Below charm threshold
        [1.5, 2.2, 0.2],
        [2.0, 2.2, 0.15],
        [2.5, 2.3, 0.15],
        [3.0, 2.2, 0.1],
        # Charm region (J/ψ excluded — continuum only)
        [3.5, 2.4, 0.15],
        [4.0, 4.2, 0.3],
        [4.5, 3.8, 0.25],
        [5.0, 3.9, 0.2],
        # Between charm and bottom
        [6.0, 3.8, 0.2],
        [7.0, 3.8, 0.15],
        [8.0, 3.8, 0.15],
        [9.0, 3.7, 0.15],
        # Above bottom threshold
        [10.5, 3.9, 0.1],
        [12.0, 3.9, 0.1],
        [14.0, 3.85, 0.1],
        [22.0, 3.9, 0.1],
        [34.0, 3.9, 0.08],
        [44.0, 3.95, 0.08],
        # LEP energies
        [57.0, 4.0, 0.1],
        # Near Z pole — resonance (not included — off-shell only)
        [130.0, 4.1, 0.15],
        [172.0, 4.1, 0.15],
        [189.0, 4.1, 0.2],
    ])

    return {
        "sqrt_s": data_points[:, 0],
        "R": data_points[:, 1],
        "R_err": data_points[:, 2],
        "source": "PDG compilation, various e+e- experiments",
    }


def get_alpha_s_data() -> dict:
    """
    Strong coupling constant measurements at various scales.
    """
    # (Q in GeV, αs value, αs uncertainty)
    data_points = np.array([
        [1.78, 0.332, 0.017],    # τ decays
        [5.0, 0.215, 0.012],     # Υ decays
        [10.0, 0.179, 0.008],    # e+e- event shapes
        [22.0, 0.151, 0.006],    # PETRA
        [35.0, 0.143, 0.007],    # PETRA/PEP
        [44.0, 0.139, 0.005],    # TRISTAN
        [58.0, 0.132, 0.008],    # SLC
        [91.2, 0.1179, 0.0010],  # LEP (Z pole)
        [133.0, 0.113, 0.005],   # LEP-2
        [172.0, 0.105, 0.006],   # LEP-2
        [189.0, 0.109, 0.004],   # LEP-2
        [206.0, 0.110, 0.005],   # LEP-2
    ])

    return {
        "Q": data_points[:, 0],
        "alpha_s": data_points[:, 1],
        "alpha_s_err": data_points[:, 2],
        "source": "PDG 2023 compilation",
    }


def get_ee_to_mumu_data() -> dict:
    """
    e+e- → μ+μ- cross-section measurements at various √s.
    """
    # (√s in GeV, σ in nb, σ_err in nb)
    data_points = np.array([
        [10.0, 0.0587, 0.003],
        [14.0, 0.0300, 0.002],
        [22.0, 0.0122, 0.001],
        [29.0, 0.00700, 0.0005],
        [34.0, 0.00510, 0.0004],
        [44.0, 0.00305, 0.0003],
        [57.0, 0.00182, 0.0002],
    ])

    return {
        "sqrt_s": data_points[:, 0],
        "sigma": data_points[:, 1],
        "sigma_err": data_points[:, 2],
        "source": "PDG compilation, below Z resonance",
    }
