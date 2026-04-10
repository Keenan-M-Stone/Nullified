#!/usr/bin/env python3
"""
Nullified: SCN-Filtered QFT — Main Comparison Script

Generates comparison plots between:
- Standard QFT predictions
- SCN-filtered predictions
- Experimental data

Run: python -m src.run_comparison
"""

import sys
import os
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.diagrams import (
    get_all_one_loop_qed,
    get_all_one_loop_qcd,
    make_tree_ee_to_mumu,
)
from src.scn_filter import scn_report, scn_filter
from src.cross_sections import (
    sigma_ee_to_mumu_tree,
    sigma_ee_to_mumu_1loop_standard,
    sigma_ee_to_mumu_1loop_scn,
    r_ratio_tree,
    r_ratio_1loop_standard,
    r_ratio_1loop_scn,
    alpha_s_running_standard,
    alpha_s_running_scn,
    alpha_running_standard,
    generate_energy_scan,
    ALPHA,
)
from src.experimental_data import (
    get_electron_g2_data,
    get_r_ratio_data,
    get_ee_to_mumu_data,
    get_alpha_s_data,
)


def run_scn_filter_report():
    """Print the SCN filter analysis for QED and QCD diagrams."""
    print("\n" + "=" * 60)
    print("PART 1: SCN DIAGRAM CLASSIFICATION")
    print("=" * 60)

    print("\n--- QED One-Loop Diagrams ---")
    qed_diagrams = get_all_one_loop_qed()
    print(scn_report(qed_diagrams))

    print("\n--- QCD One-Loop Diagrams ---")
    qcd_diagrams = get_all_one_loop_qcd()
    print(scn_report(qcd_diagrams))


def run_g2_comparison():
    """Compare electron g-2 predictions."""
    print("\n" + "=" * 60)
    print("PART 2: ELECTRON g-2 COMPARISON")
    print("=" * 60)

    g2_data = get_electron_g2_data()

    exp_val = g2_data["experiment"]["value"]
    exp_unc = g2_data["experiment"]["uncertainty"]

    # One-loop values
    a1_std = g2_data["standard_qed"]["1-loop"]
    a1_scn = g2_data["scn_qed"]["1-loop"]

    # Two-loop contribution (standard)
    c2_std = g2_data["standard_qed"]["2-loop_coefficient"]
    a2_std = c2_std * (ALPHA / np.pi) ** 2

    # Two-loop contribution (SCN estimate)
    c2_scn = g2_data["scn_qed"]["2-loop_coefficient_estimate"]
    a2_scn = c2_scn * (ALPHA / np.pi) ** 2

    print(f"\nExperimental value:    a_e = {exp_val:.14e} ± {exp_unc:.1e}")
    print(f"\nStandard QED:")
    print(f"  1-loop (Schwinger):  a_e^(1) = {a1_std:.14e}")
    print(f"  2-loop coefficient:  C_2 = {c2_std:.9f}")
    print(f"  2-loop contribution: a_e^(2) = {a2_std:.6e}")
    print(f"  Total (to 4-loop):   a_e = {g2_data['standard_qed']['total_to_4loop']:.14e}")

    print(f"\nSCN-Filtered QED:")
    print(f"  1-loop (Schwinger):  a_e^(1) = {a1_scn:.14e}  [IDENTICAL]")
    print(f"  2-loop coefficient:  C_2_SCN ≈ {c2_scn:.2f}  [ESTIMATED]")
    print(f"  2-loop contribution: a_e^(2) = {a2_scn:.6e}")
    total_scn_est = a1_scn + a2_scn
    print(f"  Total (to 2-loop):   a_e ≈ {total_scn_est:.14e}")

    print(f"\nDifference (SCN - std) at 2-loop: Δa_e ≈ {a2_scn - a2_std:.6e}")
    print(f"Experimental precision:           ±{exp_unc:.1e}")
    print(f"Ratio (Δa_e / uncertainty):       {abs(a2_scn - a2_std) / exp_unc:.0f}σ")
    print(f"\n⚠ The 2-loop SCN coefficient is estimated. If it differs significantly")
    print(f"  from standard QED, this is a critical test of the SCN framework.")


def run_cross_section_comparison():
    """Compare e+e- → μ+μ- cross-sections."""
    print("\n" + "=" * 60)
    print("PART 3: e+e- → μ+μ- CROSS-SECTION COMPARISON")
    print("=" * 60)

    exp_data = get_ee_to_mumu_data()

    print(f"\n{'√s (GeV)':>10} {'σ_tree (nb)':>12} {'σ_std (nb)':>12} "
          f"{'σ_SCN (nb)':>12} {'σ_exp (nb)':>12} {'Δ(SCN-std)/std':>15}")
    print("-" * 75)

    for sqrt_s, sigma_exp, sigma_err in zip(
        exp_data["sqrt_s"], exp_data["sigma"], exp_data["sigma_err"]
    ):
        s = sqrt_s ** 2
        sig_tree = sigma_ee_to_mumu_tree(s)
        sig_std = sigma_ee_to_mumu_1loop_standard(s)
        sig_scn = sigma_ee_to_mumu_1loop_scn(s)
        delta = (sig_scn - sig_std) / sig_std if sig_std > 0 else 0

        print(f"{sqrt_s:10.1f} {sig_tree:12.6f} {sig_std:12.6f} "
              f"{sig_scn:12.6f} {sigma_exp:12.6f} {delta:15.6f}")


def run_alpha_s_comparison():
    """Compare running strong coupling."""
    print("\n" + "=" * 60)
    print("PART 4: RUNNING αs COMPARISON")
    print("=" * 60)

    exp_data = get_alpha_s_data()

    print(f"\n{'Q (GeV)':>10} {'αs_std':>10} {'αs_SCN':>10} "
          f"{'αs_exp':>10} {'Δ(SCN-std)':>12}")
    print("-" * 55)

    for q, alpha_exp, alpha_err in zip(
        exp_data["Q"], exp_data["alpha_s"], exp_data["alpha_s_err"]
    ):
        q2 = q ** 2
        a_std = alpha_s_running_standard(q2)
        a_scn = alpha_s_running_scn(q2)
        delta = a_scn - a_std

        print(f"{q:10.1f} {a_std:10.4f} {a_scn:10.4f} "
              f"{alpha_exp:10.4f} {delta:12.4f}")

    print(f"\n⚠ SCN uses β₀_SCN = C_A/3 - 2nf/3 = 1 - 2nf/3")
    print(f"  Standard uses β₀ = 11 - 2nf/3")
    print(f"  SCN predicts αs INCREASES with energy for nf ≥ 2")
    print(f"  This contradicts asymptotic freedom → major issue for SCN-QCD")


def run_r_ratio_comparison():
    """Compare R-ratio predictions."""
    print("\n" + "=" * 60)
    print("PART 5: R-RATIO COMPARISON")
    print("=" * 60)

    exp_data = get_r_ratio_data()

    print(f"\n{'√s (GeV)':>10} {'R_tree':>8} {'R_std':>8} "
          f"{'R_SCN':>8} {'R_exp':>8}")
    print("-" * 50)

    for sqrt_s, r_exp, r_err in zip(
        exp_data["sqrt_s"], exp_data["R"], exp_data["R_err"]
    ):
        s = sqrt_s ** 2
        r_tree = r_ratio_tree(s)
        r_std = r_ratio_1loop_standard(s)
        r_scn = r_ratio_1loop_scn(s)

        print(f"{sqrt_s:10.1f} {r_tree:8.3f} {r_std:8.3f} "
              f"{r_scn:8.3f} {r_exp:8.3f}")


def generate_plots():
    """Generate comparison plots if matplotlib is available."""
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("\n[matplotlib not available — skipping plot generation]")
        print("Install with: pip install matplotlib")
        return

    os.makedirs("plots", exist_ok=True)

    # --- Plot 1: e+e- → μ+μ- cross-section ---
    fig, ax = plt.subplots(figsize=(10, 6))
    sqrt_s_arr = generate_energy_scan(2.0, 200.0, 300)
    s_arr = sqrt_s_arr ** 2

    sig_tree = np.array([sigma_ee_to_mumu_tree(s) for s in s_arr])
    sig_std = np.array([sigma_ee_to_mumu_1loop_standard(s) for s in s_arr])
    sig_scn = np.array([sigma_ee_to_mumu_1loop_scn(s) for s in s_arr])

    ax.loglog(sqrt_s_arr, sig_tree, 'b--', label='Tree level', alpha=0.5)
    ax.loglog(sqrt_s_arr, sig_std, 'r-', label='Standard QED (1-loop)', linewidth=2)
    ax.loglog(sqrt_s_arr, sig_scn, 'g-', label='SCN QED (1-loop)', linewidth=2)

    exp = get_ee_to_mumu_data()
    ax.errorbar(exp["sqrt_s"], exp["sigma"], yerr=exp["sigma_err"],
                fmt='ko', capsize=3, label='Experimental data', zorder=5)

    ax.set_xlabel('√s (GeV)', fontsize=12)
    ax.set_ylabel('σ (nb)', fontsize=12)
    ax.set_title('e⁺e⁻ → μ⁺μ⁻ Cross-Section: Standard vs SCN', fontsize=14)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig('plots/ee_to_mumu.png', dpi=150)
    print("Saved: plots/ee_to_mumu.png")
    plt.close(fig)

    # --- Plot 2: Running αs ---
    fig, ax = plt.subplots(figsize=(10, 6))
    q_arr = np.geomspace(1.5, 300, 300)
    q2_arr = q_arr ** 2

    as_std = np.array([alpha_s_running_standard(q2) for q2 in q2_arr])
    as_scn = np.array([alpha_s_running_scn(q2) for q2 in q2_arr])

    ax.plot(q_arr, as_std, 'r-', label='Standard QCD', linewidth=2)
    ax.plot(q_arr, as_scn, 'g-', label='SCN QCD', linewidth=2)

    exp_as = get_alpha_s_data()
    ax.errorbar(exp_as["Q"], exp_as["alpha_s"], yerr=exp_as["alpha_s_err"],
                fmt='ko', capsize=3, label='Experimental data', zorder=5)

    ax.set_xlabel('Q (GeV)', fontsize=12)
    ax.set_ylabel('αs(Q)', fontsize=12)
    ax.set_title('Running Strong Coupling: Standard vs SCN', fontsize=14)
    ax.set_xscale('log')
    ax.set_ylim(0, 0.5)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig('plots/alpha_s_running.png', dpi=150)
    print("Saved: plots/alpha_s_running.png")
    plt.close(fig)

    # --- Plot 3: R-ratio ---
    fig, ax = plt.subplots(figsize=(10, 6))
    sqrt_s_r = np.geomspace(1.5, 200, 500)
    s_r = sqrt_s_r ** 2

    r_tree_arr = np.array([r_ratio_tree(s) for s in s_r])
    r_std_arr = np.array([r_ratio_1loop_standard(s) for s in s_r])
    r_scn_arr = np.array([r_ratio_1loop_scn(s) for s in s_r])

    ax.plot(sqrt_s_r, r_tree_arr, 'b--', label='Tree level', alpha=0.5)
    ax.plot(sqrt_s_r, r_std_arr, 'r-', label='Standard QCD (1-loop)', linewidth=2)
    ax.plot(sqrt_s_r, r_scn_arr, 'g-', label='SCN QCD (1-loop)', linewidth=2)

    exp_r = get_r_ratio_data()
    ax.errorbar(exp_r["sqrt_s"], exp_r["R"], yerr=exp_r["R_err"],
                fmt='ko', capsize=3, label='Experimental data', zorder=5)

    # Draw quark threshold lines
    thresholds = {"uds": 1.0, "c": 3.7, "b": 10.5}
    for name, thresh in thresholds.items():
        ax.axvline(thresh, color='gray', linestyle=':', alpha=0.5)
        ax.text(thresh * 1.05, 5.5, name, fontsize=8, color='gray')

    ax.set_xlabel('√s (GeV)', fontsize=12)
    ax.set_ylabel('R', fontsize=12)
    ax.set_title('R-Ratio: Standard vs SCN', fontsize=14)
    ax.set_xscale('log')
    ax.set_ylim(0, 6)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig('plots/r_ratio.png', dpi=150)
    print("Saved: plots/r_ratio.png")
    plt.close(fig)

    # --- Plot 4: SCN vs Standard deviation ---
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # QED deviation
    sig_delta = (sig_scn - sig_std) / sig_std * 100
    ax1.semilogx(sqrt_s_arr, sig_delta, 'g-', linewidth=2)
    ax1.set_xlabel('√s (GeV)', fontsize=12)
    ax1.set_ylabel('(σ_SCN - σ_std) / σ_std  (%)', fontsize=12)
    ax1.set_title('QED: SCN Deviation from Standard', fontsize=12)
    ax1.axhline(0, color='k', linestyle='-', alpha=0.3)
    ax1.grid(True, alpha=0.3)

    # QCD αs deviation
    as_delta = (as_scn - as_std) / np.where(as_std > 0, as_std, 1) * 100
    mask = as_std < 0.9  # exclude non-perturbative
    ax2.semilogx(q_arr[mask], as_delta[mask], 'g-', linewidth=2)
    ax2.set_xlabel('Q (GeV)', fontsize=12)
    ax2.set_ylabel('(αs_SCN - αs_std) / αs_std  (%)', fontsize=12)
    ax2.set_title('QCD: SCN Deviation from Standard', fontsize=12)
    ax2.axhline(0, color='k', linestyle='-', alpha=0.3)
    ax2.grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig('plots/scn_deviations.png', dpi=150)
    print("Saved: plots/scn_deviations.png")
    plt.close(fig)


def main():
    print("╔══════════════════════════════════════════════════════════╗")
    print("║  NULLIFIED: SCN-Filtered Quantum Field Theory           ║")
    print("║  Self-Containment Nullification Applied to QED & QCD    ║")
    print("╚══════════════════════════════════════════════════════════╝")

    run_scn_filter_report()
    run_g2_comparison()
    run_cross_section_comparison()
    run_alpha_s_comparison()
    run_r_ratio_comparison()

    print("\n" + "=" * 60)
    print("PART 6: GENERATING PLOTS")
    print("=" * 60)
    generate_plots()

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print("""
Key findings:
1. QED at one-loop: SCN is largely consistent with experiment
   - Schwinger g-2 term preserved  ✓
   - Running α from VP preserved   ✓
   - Self-energy removed (Z₂=1)    → small deviation from standard QED

2. QED at two-loop: SCN makes TESTABLE predictions
   - Modified C₂ coefficient in g-2
   - Experimental precision sufficient to distinguish

3. QCD: SCN faces CHALLENGES
   - Modified β₀ loses asymptotic freedom
   - Running αs goes the wrong direction
   - Confinement argument is qualitatively appealing

4. Next steps: See Theory/06_open_questions.md
""")


if __name__ == "__main__":
    main()
