# VRP Regime Signal Model
## Volatility Risk Premium Calendar Regime Classifier

A proprietary 30-year cycle calendar algorithm classifies each S&P 500
trading day into one of twelve regime classes (C-01 through C-12) and
generates SELL, FLAT, or BUY signals for the equity index options
volatility risk premium (VRP = CBOE VIX minus 21-day forward SPX
realised volatility).

---

## Statistical Foundation (blind test 2010-2026, n=4,036 days)

| Test | Statistic | p-value |
|------|-----------|---------|
| Kruskal-Wallis global | H=138.573 | 3.18e-24 |
| C-12 annual consistency | 16/16 years positive | < 0.000001 |
| Permutation test | Z=2.23 | 0.0076 |
| Fisher combined | chi2=140.2 | < 1e-30 |

**Primary regime (C-12):** mean VRP +6.04 vol pts, win rate 89.4%, n=321
Positive in all four decades: +4.44 / +4.35 / +5.57 / +6.84

---

## Intellectual Property

- **Patent:** Provisional application 64/015,162 filed 24 March 2026, USPTO
- **Pre-registration:** https://doi.org/10.17605/OSF.IO/T4Y2S
- **Algorithm:** Proprietary, patent pending
- **Paper:** SSRN working paper [ADD LINK WHEN LIVE]

---

## 2026 Prospective Record

All predictions pre-registered before period start.
See `predictions_2026.md` for full pre-registration text.

| Period | Dates | Regime | Signal | Historical VRP |
|--------|-------|--------|--------|----------------|
| 1 | 19 Mar – 16 Apr 2026 | C-10 | SELL | +4.68 |
| 2 | 17 Apr – 16 May 2026 | C-11 | FLAT | +4.00 |
| 3 | 17 May – 15 Jun 2026 | C-12 | **SELL (PRIMARY)** | +6.04 |
| 4 | 16 Jun – 15 Jul 2026 | C-01 | FLAT | +3.36 |
| 5 | 16 Jul – 13 Aug 2026 | C-02 | FLAT | +4.74 |
| 6 | 14 Aug – 12 Sep 2026 | C-03 | FLAT | +4.44 |

Results will be logged here as each period concludes.

---

## Contact

Licensing enquiries: [YOUR EMAIL]
