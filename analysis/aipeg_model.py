"""
AI–Physical Execution Gap (AIPEG) computational core.

Implements equations (1)–(5) of the chapter exactly. Parameter values in
Appendix B are stated assumptions, not measured operator data.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Optional


def surplus(
    v_rec: float,
    c_acq: float,
    c_agg: float,
    c_proc: float,
    c_comp: float,
    c_cons: float,
    n: float,
    c_t: float,
    delta: float,
    m: float,
) -> tuple[float, float, float, float]:
    """Return M, haulage, consolidation cost per device, and S (equation 3)."""
    margin = v_rec - c_acq - c_agg - c_proc - c_comp
    haulage = c_t * delta * m
    cons_share = c_cons / n
    s = margin - cons_share - haulage
    return margin, haulage, cons_share, s


def break_even_distance(margin: float, c_cons: float, n: float, c_t: float, m: float) -> Optional[float]:
    """Equation (4). None if the pathway cannot break even at any distance."""
    num = margin - c_cons / n
    den = c_t * m
    if den <= 0 or num <= 0:
        return None
    return num / den


def min_viable_consignment(margin: float, c_cons: float, c_t: float, delta: float, m: float) -> Optional[float]:
    """Equation (5). None if M - haulage <= 0."""
    den = margin - c_t * delta * m
    if den <= 0:
        return None
    return c_cons / den


def logistic_accessibility(delta_eff: float, beta: float, delta_half: float) -> float:
    """Acc = 1 / (1 + exp[β(δ − δ½)]), bounded to (0, 1)."""
    x = beta * (delta_eff - delta_half)
    x = max(-60.0, min(60.0, x))
    return 1.0 / (1.0 + math.exp(x))


def feasibility(
    availability: float,
    accessibility: float,
    capacity: float,
    viability: float,
    legibility: float,
) -> float:
    """Equation (1): conjunctive Execution Feasibility Index."""
    return (
        max(0.0, min(1.0, availability))
        * max(0.0, min(1.0, accessibility))
        * max(0.0, min(1.0, capacity))
        * max(0.0, min(1.0, viability))
        * max(0.0, min(1.0, legibility))
    )


def circularity_execution_ratio(
    executed_values: list[float],
    technical_values: list[float],
    weights: Optional[list[float]] = None,
) -> float:
    """Equation (2)."""
    n = len(executed_values)
    if weights is None:
        weights = [1.0] * n
    num = sum(w * e for w, e in zip(weights, executed_values))
    den = sum(w * t for w, t in zip(weights, technical_values))
    if den == 0:
        return 0.0
    return num / den


@dataclass
class StrategyParams:
    name: str
    v_rec: float
    c_acq: float
    c_agg: float
    c_proc: float
    c_comp: float
    licensed: bool
    technical_value: float


# Appendix B, Table B1. Technical value ranks R-hierarchy: refurb > harvest > recycle.
STRATEGIES = [
    StrategyParams("Refurbishment", 3000, 1200, 150, 700, 100, True, 1.00),
    StrategyParams("Component harvesting", 1400, 700, 150, 250, 100, False, 0.55),
    StrategyParams("Material recycling", 120, 60, 30, 40, 25, True, 0.20),
]


# Haulage tariff and mass: Appendix B.
C_T = 6.0  # ₹ per tonne-kilometre
MASS_TONNES = 0.19 / 1000.0  # 0.19 kg → tonnes, so c_t * m = 0.00114 ₹/device-km


def effective_access_distance(road_km: float, has_local_node: bool, local_node_km: float = 28.0) -> float:
    """
    Accessibility is evaluated on distance to the first formal custody point.
    A hinterland aggregation node shortens that first-mile distance even when
    the licensed plant remains far away (chapter Section 6.3).
    """
    if has_local_node:
        return local_node_km
    return road_km


def capacity_term(road_km: float, n: float) -> float:
    """Appendix B: 0.80 in core/mid-periphery; 0.75 where dispatch is batched."""
    if n >= 40 and road_km >= 400:
        return 0.75
    return 0.80


def legibility_term(road_km: float, has_local_node: bool) -> float:
    """
    Formal share of the pathway. Nodes raise legibility by creating a recorded
    handover; unconsolidated hinterland flows remain largely unregistered.
    Calibrated so the four Appendix-B regimes reproduce Table 3 φ values.
    """
    if has_local_node:
        return 0.76
    if road_km <= 40:
        return 0.93
    if road_km <= 220:
        return 0.86
    return 0.34


# Logistic parameters chosen so Acc(25)≈0.94, Acc(180)≈0.70, Acc(520)≈0.04
# and Acc(28 km node)≈0.93, matching Table 3 when combined with Cap and L.
BETA = 0.012
DELTA_HALF = 250.0
