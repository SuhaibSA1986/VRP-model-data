# VRP Regime Signal — Pre-Registration 2026

**Filing date:** 24 March 2026  
**Filed by:** Suhaib Syed Ahmad  
**OSF DOI:** https://doi.org/10.17605/OSF.IO/T4Y2S
**Patent:** Provisional application 64/015,162 filed 24 March 2026, USPTO  
**SSRN paper:** [ADD WHEN LIVE]  

---

## Model Description

Proprietary 30-year cycle calendar regime classifier applied to the
S&P 500 options volatility risk premium (VRP = CBOE VIX minus 21-day
forward SPX realised volatility). Twelve regime classes: C-01 through C-12.

- Training data: 1990-2009
- Parameters frozen: 31 December 2009
- Algorithm: proprietary, patent pending (64/015,162)
- Supplementary data (9,096 daily regime labels): SSRN paper

---

## Global Validation (blind test 2010-2026)

- Kruskal-Wallis: H=138.573, p=3.18e-24
- C-12 annual consistency: 16/16 years positive
- Block bootstrap p (annual means > 0): < 0.000001
- Permutation test: Z=2.23, p=0.0076
- Fisher combined (3 tests): p < 1e-30

---

## Prospective Predictions — Gregorian dates

### PERIOD 1: 19 March – 16 April 2026 — REGIME C-10 — SELL SIGNAL

- **Prediction:** mean daily VRP > 0 during this period
- Historical: +4.68 vol pts, win 85.1%, p=0.000, CI=[+3.50,+5.58], n=323
- **Result:** [TO BE LOGGED 17 APRIL 2026]

---

### PERIOD 2: 17 April – 16 May 2026 — REGIME C-11 — NO POSITION

- No prediction. Historical p=0.527 (not significant).
- **Result:** [TO BE LOGGED 17 MAY 2026]

---

### PERIOD 3: 17 May – 15 June 2026 — REGIME C-12 — SELL SIGNAL ★ PRIMARY

- **Prediction:** mean daily VRP > +3.65 (overall baseline average)
- Historical: +6.04 vol pts, win 89.4%, p=0.000, CI=[+5.42,+6.66], n=321
- Annual consistency: 16/16 years positive in blind test (p < 0.000001)
- Four decades: +4.44 / +4.35 / +5.57 / +6.84
- **FALSIFICATION CRITERION:** mean VRP <= 0 over 17 May – 15 Jun 2026
- Pre-registered here: [ADD OSF DOI]
- **Result:** [TO BE LOGGED 16 JUNE 2026]

---

### PERIOD 4: 16 June – 15 July 2026 — REGIME C-01 — NO POSITION

- No prediction. Historical p=0.009 (below Bonferroni threshold).
- **Result:** [TO BE LOGGED 16 JULY 2026]

---

### PERIOD 5: 16 July – 13 August 2026 — REGIME C-02 — NO POSITION

- No prediction. Historical p=0.110 (not significant).
- **Result:** [TO BE LOGGED 14 AUGUST 2026]

---

### PERIOD 6: 14 August – 12 September 2026 — REGIME C-03 — NO POSITION

- No prediction. Historical p=0.474 (not significant).
- **Result:** [TO BE LOGGED 12 SEPTEMBER 2026]

---

## Stop-Loss Rule (pre-registered)

If VIX > 40 on any day during a SELL period, treat that day as flat (zero P&L).

---

## Risk Disclosure (pre-registered)

- C-12: VaR(99%) = -3.57, worst day = -6.56, worst month mean = -4.25
- C-10: VaR(99%) = -18.72, worst month mean = -26.55 (Aug 2015 VIX spike)

---

## Methodology

- VRP = CBOE VIX close minus 21-day forward SPX realised vol (annualised %)
- Tests: Kruskal-Wallis, Mann-Whitney U, block bootstrap (100K resamples)
- No parameters updated during prospective period

---

## Amendment Policy

Predictions are locked and cannot be changed.  
Statistical methodology clarifications are permitted with timestamp.  

**Signed:** [YOUR FULL LEGAL NAME] — 24 March 2026
