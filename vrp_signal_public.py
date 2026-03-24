"""
VRP Regime Signal Model — Public Interface
==========================================
Patent pending: provisional application 64/015,162
Filed: 24 March 2026, USPTO

This file provides the public-facing signal output for the
pre-registered 2026 prospective record.

The classification algorithm is proprietary and patent-pending.
This file shows signal outputs and period definitions only.

Pre-registration: OSF.io [DOI: ADD WHEN CONFIRMED]
SSRN paper: [ADD WHEN LIVE]
"""

from datetime import date, timedelta
from typing import Optional


# ── PRE-REGISTERED 2026 SIGNAL PERIODS ───────────────────────────────────────
# All dates Gregorian. All signals pre-registered 24 March 2026.
# Patent: provisional 64/015,162.

SIGNAL_PERIODS_2026 = [
    {
        "period": 1,
        "start": date(2026, 3, 19),
        "end":   date(2026, 4, 16),
        "regime": "C-10",
        "signal": "SELL",
        "historical_vrp": +4.68,
        "historical_win_pct": 85.1,
        "p_value": 0.000,
        "ci_99": [+3.50, +5.58],
        "n_obs": 323,
        "result_vrp": None,        # fill in after period ends
        "result_outcome": None,    # "CONFIRMED" or "FALSIFIED"
    },
    {
        "period": 2,
        "start": date(2026, 4, 17),
        "end":   date(2026, 5, 16),
        "regime": "C-11",
        "signal": "FLAT",
        "historical_vrp": +4.00,
        "historical_win_pct": None,
        "p_value": 0.527,
        "ci_99": None,
        "n_obs": 335,
        "result_vrp": None,
        "result_outcome": None,
    },
    {
        "period": 3,
        "start": date(2026, 5, 17),
        "end":   date(2026, 6, 15),
        "regime": "C-12",
        "signal": "SELL",
        "primary": True,           # flagship prediction
        "historical_vrp": +6.04,
        "historical_win_pct": 89.4,
        "p_value": 0.000,
        "ci_99": [+5.42, +6.66],
        "n_obs": 321,
        "annual_consistency": "16/16 years positive (2010-2025)",
        "bootstrap_p": "< 0.000001",
        "falsification": "mean VRP <= 0 over 17 May - 15 Jun 2026",
        "result_vrp": None,
        "result_outcome": None,
    },
    {
        "period": 4,
        "start": date(2026, 6, 16),
        "end":   date(2026, 7, 15),
        "regime": "C-01",
        "signal": "FLAT",
        "historical_vrp": +3.36,
        "p_value": 0.009,
        "n_obs": 347,
        "result_vrp": None,
        "result_outcome": None,
    },
    {
        "period": 5,
        "start": date(2026, 7, 16),
        "end":   date(2026, 8, 13),
        "regime": "C-02",
        "signal": "FLAT",
        "historical_vrp": +4.74,
        "p_value": 0.110,
        "n_obs": 337,
        "result_vrp": None,
        "result_outcome": None,
    },
    {
        "period": 6,
        "start": date(2026, 8, 14),
        "end":   date(2026, 9, 12),
        "regime": "C-03",
        "signal": "FLAT",
        "historical_vrp": +4.44,
        "p_value": 0.474,
        "n_obs": 347,
        "result_vrp": None,
        "result_outcome": None,
    },
]


def get_current_period(today: Optional[date] = None) -> Optional[dict]:
    """Return the signal period containing today's date, or None."""
    if today is None:
        today = date.today()
    for period in SIGNAL_PERIODS_2026:
        if period["start"] <= today <= period["end"]:
            return period
    return None


def get_current_signal(today: Optional[date] = None) -> str:
    """Return today's signal: SELL, FLAT, or NO_PERIOD."""
    period = get_current_period(today)
    if period is None:
        return "NO_PERIOD"
    return period["signal"]


def print_status(today: Optional[date] = None):
    """Print current signal status."""
    if today is None:
        today = date.today()

    print("=" * 60)
    print("VRP REGIME SIGNAL MODEL — STATUS")
    print(f"Date: {today}")
    print(f"Patent: provisional 64/015,162 (filed 24 March 2026)")
    print("=" * 60)

    period = get_current_period(today)

    if period is None:
        print("Status: NO ACTIVE SIGNAL PERIOD")
        print("Between pre-registered periods — no trade.")
    else:
        print(f"Period:  {period['period']} of 6")
        print(f"Dates:   {period['start']} to {period['end']}")
        print(f"Regime:  {period['regime']}")
        print(f"Signal:  {period['signal']}")
        if period['signal'] == "SELL":
            print(f"Hist VRP: {period['historical_vrp']:+.2f} vol pts")
            print(f"Win rate: {period.get('historical_win_pct', 'N/A')}%")
            if period.get('primary'):
                print("*** PRIMARY FLAGSHIP SIGNAL ***")
        if period.get('result_outcome'):
            print(f"Result:  {period['result_outcome']} "
                  f"(actual VRP: {period['result_vrp']:+.2f})")

    print()
    print("Pre-registration: OSF.io [ADD DOI]")
    print("Paper: [ADD SSRN LINK]")
    print("=" * 60)


def print_full_record():
    """Print the complete 2026 prospective record."""
    print("=" * 60)
    print("VRP REGIME SIGNAL — 2026 PROSPECTIVE RECORD")
    print("Pre-registered: 24 March 2026")
    print("Patent: 64/015,162 (provisional)")
    print("=" * 60)
    for p in SIGNAL_PERIODS_2026:
        status = p.get('result_outcome', 'PENDING')
        vrp_str = (f"Actual: {p['result_vrp']:+.2f}"
                   if p['result_vrp'] is not None
                   else f"Hist: {p['historical_vrp']:+.2f}")
        flag = " *** PRIMARY ***" if p.get('primary') else ""
        print(f"  Period {p['period']}  {p['start']} - {p['end']}"
              f"  [{p['signal']:4s}]  {vrp_str}  {status}{flag}")
    print("=" * 60)


if __name__ == "__main__":
    print_status()
    print()
    print_full_record()
