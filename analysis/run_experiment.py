#!/usr/bin/env python3
"""Reproduce Table 3, extend the AIPEG model to a 30-origin Indian panel, and write figures."""

from __future__ import annotations

import csv
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "analysis"))

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

from aipeg_model import (
    BETA,
    C_T,
    DELTA_HALF,
    MASS_TONNES,
    STRATEGIES,
    break_even_distance,
    capacity_term,
    circularity_execution_ratio,
    effective_access_distance,
    feasibility,
    legibility_term,
    logistic_accessibility,
    min_viable_consignment,
    surplus,
)

RESULTS = ROOT / "results"
FIG = RESULTS / "figures"
RESULTS.mkdir(exist_ok=True)
FIG.mkdir(parents=True, exist_ok=True)

ROAD_CIRCUITY = 1.30  # road km ≈ 1.3 × great-circle km


def haversine_km(lat1, lon1, lat2, lon2) -> float:
    r = 6371.0
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dl = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * r * math.asin(math.sqrt(a))


def load_csv(name: str) -> list[dict]:
    with open(ROOT / "data" / name, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def evaluate_strategy(strategy, delta, n, c_cons, has_node: bool):
    m, haul, cons_share, s = surplus(
        strategy.v_rec,
        strategy.c_acq,
        strategy.c_agg,
        strategy.c_proc,
        strategy.c_comp,
        c_cons,
        n,
        C_T,
        delta,
        MASS_TONNES,
    )
    a = 1.0 if strategy.licensed else 0.0
    d_acc = effective_access_distance(delta, has_node)
    acc = logistic_accessibility(d_acc, BETA, DELTA_HALF)
    cap = capacity_term(delta, n)
    v = 1.0 if s > 0 else 0.0
    L = legibility_term(delta, has_node)
    phi = feasibility(a, acc, cap, v, L)
    if a == 0:
        bind = "Availability"
    elif v == 0:
        bind = "Viability"
    elif acc < 0.15:
        bind = "Accessibility"
    elif L < 0.5:
        bind = "Legibility"
    else:
        bind = "—"
    return {
        "strategy": strategy.name,
        "delta_km": round(delta, 1),
        "n": n,
        "c_cons": c_cons,
        "M": round(m, 2),
        "haulage": round(haul, 2),
        "cons_share": round(cons_share, 2),
        "transport": round(haul + cons_share, 2),
        "S": round(s, 2),
        "A": a,
        "Acc": round(acc, 4),
        "Cap": cap,
        "V": v,
        "L": round(L, 4),
        "phi": round(phi, 4),
        "bind": bind,
        "technical_value": strategy.technical_value,
        "licensed": strategy.licensed,
    }


def appendix_b_regimes():
    return [
        dict(regime="Metropolitan core", delta=25, n=200, c_cons=400, has_node=True),
        dict(regime="Mid-periphery", delta=180, n=40, c_cons=900, has_node=False),
        dict(regime="Hinterland, no node", delta=520, n=1, c_cons=250, has_node=False),
        dict(regime="Hinterland with node", delta=520, n=60, c_cons=1400, has_node=True),
    ]


def run_table3():
    rows = []
    for reg in appendix_b_regimes():
        for st in STRATEGIES:
            r = evaluate_strategy(st, reg["delta"], reg["n"], reg["c_cons"], reg["has_node"])
            r["regime"] = reg["regime"]
            rows.append(r)
    df = pd.DataFrame(rows)
    df.to_csv(RESULTS / "table3_reproduction.csv", index=False)
    return df


def run_districts():
    origins = load_csv("district_origins.csv")
    hubs = load_csv("facility_hubs.csv")
    rows = []
    for o in origins:
        lat, lon = float(o["lat"]), float(o["lon"])
        nearest = min(
            hubs,
            key=lambda h: haversine_km(lat, lon, float(h["lat"]), float(h["lon"])),
        )
        gc = haversine_km(lat, lon, float(nearest["lat"]), float(nearest["lon"]))
        road = gc * ROAD_CIRCUITY
        klass = o["settlement_class"]
        if klass == "metropolitan":
            specs = [(True, 200, 400, "observed_metro_density")]
        elif klass == "mid_periphery":
            # State capitals are treated as having a formal collection point (n=40),
            # matching the mid-periphery regime in Appendix B.
            specs = [(True, 40, 900, "state_capital_collection")]
        else:
            specs = [
                (False, 1, 250, "no_node"),
                (True, 60, 1400, "with_aggregation_node"),
            ]
        for has_node, n, c_cons, scenario in specs:
            for st in STRATEGIES:
                r = evaluate_strategy(st, road, n, c_cons, has_node)
                r.update(
                    {
                        "place": o["place"],
                        "state": o["state"],
                        "lat": lat,
                        "lon": lon,
                        "class": klass,
                        "nearest_hub": nearest["hub"],
                        "great_circle_km": round(gc, 1),
                        "road_km": round(road, 1),
                        "scenario": scenario,
                    }
                )
                rows.append(r)
    df = pd.DataFrame(rows)
    df.to_csv(RESULTS / "district_phi.csv", index=False)
    return df


def run_sensitivity():
    rows = []
    st = STRATEGIES[0]  # refurbishment
    for n in [1, 5, 10, 20, 40, 60, 100, 200]:
        for delta in [25, 100, 180, 300, 520, 800]:
            c_cons = 250 if n == 1 else (400 if n >= 200 else 900)
            r = evaluate_strategy(st, delta, n, c_cons, has_node=(n >= 40))
            r["n_grid"] = n
            r["delta_grid"] = delta
            rows.append(r)
    df = pd.DataFrame(rows)
    df.to_csv(RESULTS / "sensitivity_refurbishment.csv", index=False)
    return df


def cer_by_group(df: pd.DataFrame, group_cols: list[str]) -> pd.DataFrame:
    out = []
    for keys, g in df.groupby(group_cols, dropna=False):
        if not isinstance(keys, tuple):
            keys = (keys,)
        # Unconstrained optimiser picks highest technical-value strategy (refurbishment).
        # Executable choice: highest technical value among rows with phi > 0.10.
        places = g.groupby("place")
        exec_vals, tech_vals = [], []
        for _, pg in places:
            tech_vals.append(pg["technical_value"].max())
            feasible = pg[pg["phi"] > 0.10]
            if feasible.empty:
                exec_vals.append(0.0)
            else:
                exec_vals.append(feasible.loc[feasible["technical_value"].idxmax(), "technical_value"])
        cer = circularity_execution_ratio(exec_vals, tech_vals)
        rec = {c: k for c, k in zip(group_cols, keys)}
        rec["CER"] = round(cer, 4)
        rec["AIPEG"] = round(1 - cer, 4)
        rec["n_places"] = len(exec_vals)
        rec["share_executable"] = round(sum(1 for e in exec_vals if e > 0) / len(exec_vals), 4)
        out.append(rec)
    return pd.DataFrame(out)


def make_figures(table3: pd.DataFrame, districts: pd.DataFrame, sens: pd.DataFrame):
    plt.rcParams.update(
        {
            "font.family": "DejaVu Serif",
            "axes.spines.top": False,
            "axes.spines.right": False,
            "figure.dpi": 140,
        }
    )

    # Figure 1: haulage vs consolidation
    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    t = table3[table3["strategy"] == "Refurbishment"].drop_duplicates("regime")
    x = range(len(t))
    ax.bar([i - 0.18 for i in x], t["haulage"], 0.36, label="Haulage (c_t · δ · m)", color="#4C6A92")
    ax.bar([i + 0.18 for i in x], t["cons_share"], 0.36, label="Consolidation (C_cons / n)", color="#C46B3A")
    ax.set_xticks(list(x))
    ax.set_xticklabels([r.replace(" ", "\n") for r in t["regime"]], fontsize=8)
    ax.set_ylabel("₹ per device")
    ax.set_title("Transport cost decomposition for refurbishment (Appendix B parameters)")
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(FIG / "fig1_transport_decomposition.png")
    plt.close()

    # Figure 2: phi by strategy and regime
    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    regimes = table3["regime"].unique()
    width = 0.25
    colors = ["#2F6F4E", "#C46B3A", "#4C6A92"]
    for i, st in enumerate(["Refurbishment", "Component harvesting", "Material recycling"]):
        sub = table3[table3["strategy"] == st]
        ax.bar([j + (i - 1) * width for j in range(len(regimes))], sub["phi"], width, label=st, color=colors[i])
    ax.set_xticks(range(len(regimes)))
    ax.set_xticklabels([r.replace(" ", "\n") for r in regimes], fontsize=8)
    ax.set_ylabel("Execution Feasibility Index φ")
    ax.set_title("φ is zero wherever availability or viability fails")
    ax.legend(frameon=False, fontsize=8)
    fig.tight_layout()
    fig.savefig(FIG / "fig2_phi_by_regime.png")
    plt.close()

    # Figure 3: district map-like scatter (lon/lat coloured by phi refurb no extra node)
    d = districts[(districts["strategy"] == "Refurbishment") & (~districts["scenario"].eq("with_aggregation_node"))]
    fig, ax = plt.subplots(figsize=(7.2, 6.2))
    sc = ax.scatter(d["lon"], d["lat"], c=d["phi"], cmap="RdYlGn", vmin=0, vmax=0.8, s=55, edgecolors="k", linewidths=0.3)
    for _, row in d.iterrows():
        ax.annotate(row["place"], (row["lon"], row["lat"]), fontsize=6, xytext=(3, 3), textcoords="offset points")
    cb = fig.colorbar(sc, ax=ax, fraction=0.035)
    cb.set_label("φ (refurbishment, without added hinterland node)")
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    ax.set_title("Geographic structure of executability (30 origins, nearest hub)")
    ax.set_aspect("equal", adjustable="box")
    fig.tight_layout()
    fig.savefig(FIG / "fig3_district_phi_map.png")
    plt.close()

    # Figure 4: sensitivity heatmap of S for refurbishment
    pivot = sens.pivot_table(index="n_grid", columns="delta_grid", values="S")
    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    im = ax.imshow(pivot.values, aspect="auto", cmap="RdBu", vmin=-400, vmax=900)
    ax.set_xticks(range(len(pivot.columns)))
    ax.set_xticklabels(list(pivot.columns))
    ax.set_yticks(range(len(pivot.index)))
    ax.set_yticklabels(list(pivot.index))
    ax.set_xlabel("Road distance δ (km)")
    ax.set_ylabel("Consolidation factor n")
    ax.set_title("Net surplus S (₹/device), refurbishment: n dominates δ")
    fig.colorbar(im, ax=ax, fraction=0.035, label="S (₹)")
    fig.tight_layout()
    fig.savefig(FIG / "fig4_surplus_sensitivity.png")
    plt.close()

    # Figure 5: CER comparison
    hinter = districts[districts["class"] == "hinterland"]
    cer_no = cer_by_group(hinter[hinter["scenario"] == "no_node"], ["class"])
    cer_yes = cer_by_group(hinter[hinter["scenario"] == "with_aggregation_node"], ["class"])
    metro = cer_by_group(districts[districts["class"] == "metropolitan"], ["class"])
    mid = cer_by_group(districts[districts["class"] == "mid_periphery"], ["class"])
    labels = ["Metropolitan", "Mid-periphery", "Hinterland\nno node", "Hinterland\nwith node"]
    vals = [
        float(metro["CER"].iloc[0]),
        float(mid["CER"].iloc[0]),
        float(cer_no["CER"].iloc[0]),
        float(cer_yes["CER"].iloc[0]),
    ]
    fig, ax = plt.subplots(figsize=(7.0, 4.0))
    ax.bar(labels, vals, color=["#2F6F4E", "#4C6A92", "#A33B3B", "#C46B3A"])
    ax.set_ylim(0, 1.05)
    ax.set_ylabel("Circularity Execution Ratio")
    ax.set_title("CER on the 30-origin panel (threshold φ > 0.10)")
    for i, v in enumerate(vals):
        ax.text(i, v + 0.03, f"{v:.2f}", ha="center", fontsize=9)
    fig.tight_layout()
    fig.savefig(FIG / "fig5_cer_by_class.png")
    plt.close()
    return labels, vals


def main():
    table3 = run_table3()
    districts = run_districts()
    sens = run_sensitivity()
    labels, cer_vals = make_figures(table3, districts, sens)

    # Headline tests of the theory
    ref = table3[table3["strategy"] == "Refurbishment"]
    haul_min, haul_max = ref["haulage"].min(), ref["haulage"].max()
    cons_min, cons_max = ref["cons_share"].min(), ref["cons_share"].max()
    ratio = (cons_max - cons_min) / max(haul_max - haul_min, 1e-9)

    harvest_phi_max = table3[table3["strategy"] == "Component harvesting"]["phi"].max()
    recycle_s_max = table3[table3["strategy"] == "Material recycling"]["S"].max()

    hinter = districts[(districts["class"] == "hinterland") & (districts["strategy"] == "Refurbishment")]
    phi_no = hinter[hinter["scenario"] == "no_node"]["phi"].mean()
    phi_yes = hinter[hinter["scenario"] == "with_aggregation_node"]["phi"].mean()

    summary = {
        "table3_rows": len(table3),
        "district_rows": len(districts),
        "haulage_spread_inr": round(float(haul_max - haul_min), 4),
        "consolidation_spread_inr": round(float(cons_max - cons_min), 2),
        "consolidation_over_haulage": round(float(ratio), 1),
        "harvest_phi_max": round(float(harvest_phi_max), 4),
        "recycle_S_max": round(float(recycle_s_max), 2),
        "hinterland_mean_phi_no_node": round(float(phi_no), 4),
        "hinterland_mean_phi_with_node": round(float(phi_yes), 4),
        "CER_metropolitan": cer_vals[0],
        "CER_mid": cer_vals[1],
        "CER_hinter_no": cer_vals[2],
        "CER_hinter_node": cer_vals[3],
        "break_even_refurb_n1": break_even_distance(850, 250, 1, C_T, MASS_TONNES),
        "break_even_refurb_n60": break_even_distance(850, 1400, 60, C_T, MASS_TONNES),
        "nmin_520_refurb": min_viable_consignment(850, 250, C_T, 520, MASS_TONNES),
        "nmin_recycle_25": min_viable_consignment(-35, 400, C_T, 25, MASS_TONNES),
    }
    pd.Series(summary).to_csv(RESULTS / "headline_tests.csv")
    cer_by_group(districts[districts["scenario"] != "with_aggregation_node"], ["class"]).to_csv(
        RESULTS / "cer_without_added_nodes.csv", index=False
    )
    print("SUMMARY")
    for k, v in summary.items():
        print(f"  {k}: {v}")
    print("Wrote", RESULTS)


if __name__ == "__main__":
    main()
