# The Prompt Repository

All 122 prompts from the book "Claude AI for Finance Professionals", free, in full. Each one shows the same five layers: Context, Role, Action, Format, Tone.

Numbering matches the book exactly: Prompt 47 here is Prompt 47 there.

> CRAFT is this book's framework. It is not Anthropic's and it is not in the model documentation, so there is no point looking for it there.

---

## A Bad Prompt vs a Good Prompt

**The bad prompt**

```
"What's our portfolio risk? Be detailed."
```

Eleven words, and nothing in them tells the model what it has to do for you. It does not say which risk: rate, credit, currency or concentration. It does not say detailed relative to what. It does not give the portfolio state or the date. It does not say whether the answer should be prose, a table or a number. The model answers anyway, guessing each of those silently.

**The good prompt**

```
Portfolio attached (32 positions, weights in column C). Run a 2022-style
rate-shock stress test: +300bps parallel shift, equity-bond correlation
+0.6. Output: loss in dollars by position, top 5 contributors, one hedge
recommendation with cost. Format: one table + 5 lines. BCE language only.
```

**What changed**

- The vague noun "risk" became one named scenario with two parameters.
- "Detailed" became an exact deliverable: dollar losses, five contributors, one hedge with a cost attached.
- The missing format became "one table + 5 lines".
- The missing register became "BCE language only": Base Case Estimate, not advice.

Adjectives like detailed, thorough and professional ask the model to decide for you. Nouns and numbers are decisions already made.

### When a prompt fails, read the failure first

| What came back | Which layer caused it |
| --- | --- |
| Too long, or carrying sections you never asked for. | Format was vague. You wrote an adjective where a noun belonged. |
| Hedges everything, commits to nothing. | The Role was too junior, or Tone never said who reads this. |
| Confident and wrong on a number. | Action ran a multi-step calculation with no validation step under it. |
| Ignores a constraint you definitely stated. | The constraint sat in Action, where it reads as one instruction among nine. Move it to Context, where it reads as a fact of the workspace. |
| Answers a different question. | Context was missing the thing you assumed was obvious. |

Then change one layer. Change three at once and you learn nothing about which one mattered.

---

## Contents

- **Chapter 2 — The Equity Research Desk** — Prompts 1 to 8
- **Chapter 3 — The M&A Valuation Desk** — Prompts 9 to 16
- **Chapter 4 — The Macro Risk Desk** — Prompts 17 to 24
- **Chapter 5 — The Earnings Intelligence Desk** — Prompts 25 to 32
- **Chapter 6 — The Portfolio Strategy Desk** — Prompts 33 to 40
- **Chapter 7 — The Quant Trading Desk** — Prompts 41 to 48
- **Chapter 8 — The Strategy Consulting Desk** — Prompts 49 to 56
- **Chapter 9 — The Endowment Strategy Desk** — Prompts 57 to 64
- **Chapter 10 — The Sovereign Wealth Desk** — Prompts 65 to 72
- **Chapter 11 — The ESG & Climate Desk** — Prompts 73 to 80
- **Chapter 12 — The Fixed Income & Credit Desk** — Prompts 81 to 88
- **Chapter 13 — Claude Model Family** — Prompts 89 to 96
- **Chapter 14 — Claude.ai Platform** — Prompts 97 to 104
- **Chapter 15 — Claude Code for Quant Finance** — Prompts 105 to 113
- **Chapter 16 — Claude Cowork, Plugins & MCP** — Prompts 114 to 122

---

## Chapter 2 — The Equity Research Desk

### PROMPT 1 — The Benjamin Graham Margin of Safety & Net-Net Screen

```
CONTEXT: Attached: the [UNIVERSE] screening file ([FILE]) with balance sheet and ten-year earnings fields already pulled. Output feeds the value watchlist review. Data vintage: last reported fiscal year.

ROLE: Senior value analyst applying Benjamin Graham's documented Security Analysis methodology.

ACTION:
  1. Screen [N] stocks in [UNIVERSE] for deep value using Graham's documented criteria.
  2. Graham Net-Net: Current Assets minus Total Liabilities vs Market Cap
  3. Margin of Safety: minimum 33% discount to intrinsic value Financial strength: current ratio >2x, long-term debt limited Earnings stability: positive EPS in each of the last 10 years Dividend record: uninterrupted payments for at least 20 years P/E below 15x, P/Book below 1.5x, combined product <22.5 Graham Number = square root of (22.5 x EPS x Book Value Per Share)

FORMAT: Ranked list with Graham Number, margin of safety %, net-net value, one-line thesis.

Workbook:
Sheet 1 GRAHAM_SCREEN: ticker, Graham_Number, MoS_pct, net_net_value, P/E, P/Book
Sheet 2 WATCHLIST: names near threshold with specific gap to qualification

TONE: Institutional equity research. Every forward-looking figure labelled an estimate. No price targets, no buy or sell language.
```

### PROMPT 2 — The Peter Lynch PEG Ratio & GARP Discovery Framework

```
CONTEXT: You have the [UNIVERSE] fundamentals file ([FILE]) plus institutional ownership data. The list goes to a small and mid cap idea meeting, so coverage gaps matter more than precision.

ROLE: Growth-at-a-reasonable-price analyst applying Peter Lynch's documented GARP methodology.

ACTION:
  1. Screen [UNIVERSE] for GARP opportunities using Lynch's documented framework.
  2. PEG ratio: P/E divided by earnings growth rate. Target: PEG <1.0 Lynch categories: Stalwarts (8-12% growers), Fast Growers (20-25%), Turnarounds, Cyclicals Hidden gems: small/mid-cap with <30% institutional ownership Ten-bagger potential assessment: can this company grow 10x in 10 years?
  3. Avoid: >60% institutional ownership (Lynch's 'overfollowed' warning) Insider ownership: management skin in the game preferred

FORMAT: Categorised GARP list with PEG ratios, Lynch categories, and ten-bagger assessments.

Workbook:
Sheet 1 GARP_SCREEN: ticker, Lynch_category, PEG, EPS_growth, inst_ownership_pct
Sheet 2 TEN_BAGGER_CANDIDATES: names with specific 10x mechanism documented

TONE: Institutional equity research. Every forward-looking figure labelled an estimate. No price targets, no buy or sell language.
```

### PROMPT 3 — The Buffett Owner Earnings & Economic Moat Framework

```
CONTEXT: Available: ten years of [COMPANY] annual filings ([FILE]) including cash flow statements and capex detail. Maintenance capex is not disclosed separately, so state how you split it.

ROLE: Long-term quality investor applying Warren Buffett's documented owner earnings methodology.

ACTION:
  1. Evaluate [COMPANY] using Buffett's documented owner earnings and moat framework. Standing rule: after any multi-step numerical work, write and run a Python script recomputing every derived figure from stated inputs; print PASS/FAIL per check; correct and rerun until all pass.
  2. Owner Earnings = Net Income + D&A - Maintenance Capex (Buffett 1986 annual letter) Moat types: Brand, Cost advantage, Network effect, Switching cost ROE consistently above 15% for 10 years without excessive leverage ROIC above WACC sustained for 10 years Pricing power: has the company raised prices without losing volume in 5 years?
  3. Intrinsic value: 10-year owner earnings projection discounted at 9-10%

FORMAT: Owner earnings calculation, moat type, durability score, and intrinsic value range.

Workbook:
Sheet 1 OWNER_EARNINGS: 10yr net_income, D&A, maint_capex, owner_earnings
Sheet 2 MOAT_SCORECARD: moat_type, evidence, durability_1to10
Sheet 3 INTRINSIC_VALUE: 10yr projection at base/bull/bear growth rates

TONE: Institutional equity research. Every forward-looking figure labelled an estimate. No price targets, no buy or sell language.
```

### PROMPT 4 — The AQR Quality-Value-Momentum Multi-Factor Ranking

```
CONTEXT: Working from the [UNIVERSE] factor data file ([FILE]), fundamentals and twelve-month price history included. Ranking feeds a quarterly portfolio rebalance. Data vintage: month end [DATE].

ROLE: Quantitative analyst applying publicly documented multi-factor investing research.

ACTION:
  1. Apply AQR's documented QVM multi-factor model to rank [UNIVERSE]. Standing rule: after any multi-step numerical work, write and run a Python script recomputing every derived figure from stated inputs; print PASS/FAIL per check; correct and rerun until all pass.
  2. Quality factor (per AQR Asness et al. published research): Profitability: gross profits/assets, ROE, ROA, cash flow/assets Growth: 5yr growth in profitability measures
  3. Safety: low beta, low leverage, high Altman Z-score Value factor: book-to-market, earnings yield, cash flow yield Momentum factor: 12-1 month return (excluding last month) Composite: equal-weight Quality + Value + Momentum z-scores Flag: stocks in top quintile of ALL three factors simultaneously

FORMAT: Factor scores, composite ranking, and triple-overlap identification.

Workbook:
Sheet 1 FACTOR_SCORES: ticker, quality_z, value_z, momentum_z, composite_z, rank
Sheet 2 TRIPLE_OVERLAP: names in top quintile of all three factors

TONE: Institutional equity research. Every forward-looking figure labelled an estimate. No price targets, no buy or sell language.
```

### PROMPT 5 — The Macro-Aware Earnings-Yield Spread & Valuation Framework

```
CONTEXT: Given [MARKET/SECTOR/COMPANY] forward earnings estimates and the sovereign curve as of [DATE] close ([FILE]). Twenty years of history is available. The read feeds an asset allocation discussion.

ROLE: Senior strategist applying PIMCO's publicly documented macro-aware equity valuation approach.

ACTION:
  1. Assess the earnings-yield spread and relative value of [MARKET/SECTOR/COMPANY]. Standing rule: after any multi-step numerical work, write and run a Python script recomputing every derived figure from stated inputs; print PASS/FAIL per check; correct and rerun until all pass.
  2. Earnings-yield spread: forward earnings yield minus risk-free rate Historical context: current spread vs 20-year average Forward ERP for cost of equity: state the source and date separately from the spread Real yield analysis: nominal yield minus inflation expectations Cross-asset relative value: equities vs credit vs bonds vs commodities

FORMAT: Spread analysis with cross-asset relative value and positioning context.

Workbook:
Sheet 1 SPREAD_ANALYSIS: date, earnings_yield, RF_rate, spread, historical_avg, z_score
Sheet 2 RELATIVE_VALUE: asset_class, yield, real_yield, vs_history

TONE: Institutional equity research. Every forward-looking figure labelled an estimate. No price targets, no buy or sell language.
```

### PROMPT 6 — The Quantitative Pattern & Market Anomaly Detection

```
CONTEXT: Attached: daily prices, volume and short interest for [TICKER] over [TIME PERIOD] ([FILE]). Sample sizes are small in places. Nothing here becomes a position without a stated economic reason.

ROLE: Quantitative researcher identifying statistically significant, economically-justified patterns.

ACTION:
  1. Identify statistically significant patterns for [TICKER] over [TIME PERIOD].
  2. Seasonal patterns: best/worst calendar months with p-value and sample size Earnings window: pre-announcement drift, post-earnings persistence, reversal Macro event correlations: Fed meetings, CPI releases, index rebalancing Short interest dynamics: squeeze potential via days-to-cover ratio Statistical edge summary: lowest p-value pattern that also has an economic rationale CRITICAL: every pattern must have an economic rationale, not just statistical significance

FORMAT: Pattern table with p-values, sample sizes, and economic rationale per pattern.

Workbook:
Sheet 1 SEASONAL_PATTERNS: month, avg_return, p_value, sample_n, economic_reason
Sheet 2 EVENT_ANALYSIS: event_type, avg_return, p_value, tradeable
Sheet 3 EDGE_SUMMARY: pattern, p_value, n, edge_size, economic_rationale

TONE: Institutional equity research. Every forward-looking figure labelled an estimate. No price targets, no buy or sell language.
```

### PROMPT 7 — The Macro-Driven Sector Rotation & Cycle Positioning

```
CONTEXT: You have current sector multiples, consensus growth estimates and the macro dashboard in [FILE]. Positioning goes to the monthly strategy meeting and is reviewed again in six months.

ROLE: Chief equity strategist with expertise in economic cycle analysis and sector allocation.

ACTION:
  1. Optimal sector positioning for next 6-12 months given current macro environment.
  2. Economic cycle stage: Early / Mid / Late expansion or Contraction For each of the 11 GICS sectors: Historical performance in current cycle stage Current EV/EBITDA vs 5yr historical average NTM EPS growth consensus estimate Specific macro catalyst with timing estimate Specific invalidating condition Conviction: HIGH / MEDIUM / LOW Recommend: 3 overweights, 2 underweights My macro view: [DESCRIBE IN 2-3 SENTENCES]

FORMAT: Sector rotation brief. Overweight/underweight table with conviction levels.

Workbook:
Sheet 1 ROTATION_TABLE: sector, OW_UW, current_mult, 5yr_avg, NTM_EPS, conviction
Sheet 2 CATALYST_TRACKER: sector, catalyst, timeline, invalidating_condition

TONE: Institutional equity research. Every forward-looking figure labelled an estimate. No price targets, no buy or sell language.
```

### PROMPT 8 — The Buy-Side Full Due Diligence Research Note

```
CONTEXT: Attached: [COMPANY] filings, transcripts and the peer file ([FILE]) for [TICKER]. The note goes to the investment committee, so every derived figure needs a traceable source.

ROLE: Managing Director at a large sell-side firm preparing a full IC package for a new position. Apply the standard you would defend to the committee.

ACTION:
  1. Full institutional due diligence on [COMPANY], [TICKER]. Standing rule: after any multi-step numerical work, write and run a Python script recomputing every derived figure from stated inputs; print PASS/FAIL per check; correct and rerun until all pass.
  2. Ask Claude: 'Using the latest publicly available financials for [COMPANY]:'
  3. Business quality: revenue model, moat type, moat trajectory Financial quality: Revenue CAGR 3yr, EBITDA margin, FCF conversion, leverage Management: capital allocation track record, insider ownership, succession Valuation: DCF with WACC + TGR sensitivity, EV/EBITDA vs peers, P/FCF vs history Three 12-month catalysts with magnitude and probability each Two bear cases: specific mechanistic path to loss, probability, magnitude Position size: core 3-5%, standard 1-3%, watch <1% Pre-mortem: most credible path to being wrong

FORMAT: IC-ready research note. Assumption log required.

Workbook:
Sheet 1 FINANCIAL_MODEL: 5yr P&L, FCF schedule (all with formulas)
Sheet 2 DCF_SENSITIVITY: WACC x TGR 3x3 grid (auto-calculating)
Sheet 3 PEER_COMPS: 6 peers, all multiples, target vs median
Sheet 4 ASSUMPTION_LOG: assumption, base, bull, bear, sensitivity_rating

TONE: Institutional equity research. Every forward-looking figure labelled an estimate. No price targets, no buy or sell language.
```

## Chapter 3 — The M&A Valuation Desk

### PROMPT 9 — The Institutional Buy-Side DCF Valuation Model

```
CONTEXT: Attached: [COMPANY] segment disclosures, five years of filings and the current capital structure ([FILE]). The output number sits in a board pack. Data vintage: filings dated [DATE].

ROLE: Managing Director at a large sell-side firm building the M&A DCF, the number the board pack rests on. Apply the standard you would defend in that room.

ACTION:
  1. Build a complete DCF for [COMPANY], [TICKER]. Five-year revenue projections by segment. Standing rule: after any multi-step numerical work, write and run a Python script recomputing every derived figure from stated inputs; print PASS/FAIL per check; correct and rerun until all pass.

FORMAT: Investment banking valuation memo. BCE only. Source every assumption.

Workbook:
Sheet 1 DCF_MODEL: revenue, EBIT, NOPAT, D&A, Capex, NWC, FCF
Sheet 2 WACC_BUILD: RF, ERP, beta, Ke, Kd, weights, WACC

TONE: Deal-side analytical. State what is assumed versus what is disclosed. No recommendation on whether to transact.
```

### PROMPT 10 — The Institutional Cost of Capital Construction

```
CONTEXT: You have [COMPANY] market data, debt schedules and [COUNTRY/MARKET] sovereign yields in [FILE]. This WACC will be challenged line by line, so each input needs a date.

ROLE: Senior financial analyst specialising in defensible WACC estimation.

ACTION:
  1. Build a fully sourced WACC for [COMPANY] in [COUNTRY/MARKET]. RF rate with exact source and date. Standing rule: after any multi-step numerical work, write and run a Python script recomputing every derived figure from stated inputs; print PASS/FAIL per check; correct and rerun until all pass.

FORMAT: WACC table with every component sourced. Sensitivity analysis included.

Workbook:
Sheet 1 WACC_BUILD: component, value, source, date, methodology_note
Sheet 2 BETA_REGRESSION: returns, index, R-squared, regression period

TONE: Deal-side analytical. State what is assumed versus what is disclosed. No recommendation on whether to transact.
```

### PROMPT 11 — The Institutional Peer Group Valuation Framework

```
CONTEXT: Given [TARGET] financials and a candidate peer list of [N] companies ([FILE]). Some candidates are poor matches on size or mix. Market data as of [DATE] close.

ROLE: Senior equity analyst building a sourced peer group valuation.

ACTION:
  1. Comparable company analysis for [TARGET] vs [N]-company peer group. State peer inclusion/exclusion rationale. Standing rule: after any multi-step numerical work, write and run a Python script recomputing every derived figure from stated inputs; print PASS/FAIL per check; correct and rerun until all pass.

FORMAT: Comps table with implied valuation range and premium/discount analysis.

Workbook:
Sheet 1 COMPS_TABLE: peers, EV/Rev, EV/EBITDA, P/E, P/FCF, growth, margins
Sheet 2 IMPLIED_VALUATION: target BCE at peer min/25th/median/75th/max

TONE: Deal-side analytical. State what is assumed versus what is disclosed. No recommendation on whether to transact.
```

### PROMPT 12 — The Private Equity Leveraged Buyout Returns Analysis

```
CONTEXT: Available: [COMPANY] historical financials and indicative debt terms from the lender file ([FILE]). Sponsor entry range is [X] to [X] times EBITDA. Hold period assumption: five years.

ROLE: Private equity analyst building sponsor acquisition returns analysis.

ACTION:
  1. Complete LBO analysis for [COMPANY]. Entry EV/EBITDA: [X]-[X]x. Standing rule: after any multi-step numerical work, write and run a Python script recomputing every derived figure from stated inputs; print PASS/FAIL per check; correct and rerun until all pass.

FORMAT: Returns matrix as primary output with DSCR table.

Workbook:
Sheet 1 LBO_MODEL: sources/uses, P&L, debt schedule, equity bridge
Sheet 2 RETURNS_MATRIX: IRR/MOIC grid (auto-calculating)

TONE: Deal-side analytical. State what is assumed versus what is disclosed. No recommendation on whether to transact.
```

### PROMPT 13 — The M&A Control Premium & Transaction Multiple Framework

```
CONTEXT: Working from announced [SECTOR] deals above [CUR][X] over the last [N] years ([FILE]). Disclosure is uneven across deals. Missing multiples must be marked, not estimated.

ROLE: Senior M&A banker analysing transaction multiples and control premiums.

ACTION:
  1. Precedent transactions for [SECTOR], last [N] years, deal >[CUR][X]. For each: acquirer, target, date, EV, EV/EBITDA, EV/Revenue, control premium.

FORMAT: Transaction table with control premium analysis and implied target range.

Workbook:
Sheet 1 TRANSACTIONS: acquirer, target, date, EV, EV/EBITDA, premiums
Sheet 2 STATISTICS: median, mean, 25th, 75th by buyer type

TONE: Deal-side analytical. State what is assumed versus what is disclosed. No recommendation on whether to transact.
```

### PROMPT 14 — The Conglomerate SOTP & Break-Up Value Analysis

```
CONTEXT: Segment reporting for [COMPANY]'s [N] businesses is in [FILE], along with the pure play comparable set. Corporate costs are unallocated. Output supports a break up discussion.

ROLE: Managing Director at a large sell-side firm applying SOTP methodology. Value each segment as you would defend it to the board.

ACTION:
  1. SOTP valuation for [COMPANY] with [N] business segments. Per segment: appropriate methodology and pure-play comparable. Standing rule: after any multi-step numerical work, write and run a Python script recomputing every derived figure from stated inputs; print PASS/FAIL per check; correct and rerun until all pass.

FORMAT: SOTP table with conglomerate discount and implied value vs current market cap.

Workbook:
Sheet 1 SOTP_TABLE: segment, EBITDA, multiple, EV, comparable_used
Sheet 2 COMPS_PER_SEGMENT: pure-play peers per segment

TONE: Deal-side analytical. State what is assumed versus what is disclosed. No recommendation on whether to transact.
```

### PROMPT 15 — The M&A Deal Economics & EPS Impact Framework

```
CONTEXT: You have [ACQUIRER] and [TARGET] standalone financials plus the proposed [X]% cash and [X]% stock structure ([FILE]). Synergy estimates are management supplied and unaudited.

ROLE: M&A banker assessing deal economics and EPS impact for the acquirer.

ACTION:
  1. Accretion/dilution analysis for [ACQUIRER] acquiring [TARGET]. Standing rule: after any multi-step numerical work, write and run a Python script recomputing every derived figure from stated inputs; print PASS/FAIL per check; correct and rerun until all pass.
  2. Deal: [X]% cash / [X]% stock.

FORMAT: Accretion/dilution table by year with synergy sensitivity.

Workbook:
Sheet 1 ACC_DIL: standalone_EPS, pro_forma_EPS, accretion_pct by year
Sheet 2 SYNERGY_SENSITIVITY: accretion at 0/50/75/100% synergy realisation

TONE: Deal-side analytical. State what is assumed versus what is disclosed. No recommendation on whether to transact.
```

### PROMPT 16 — The Investment Banking Fairness Opinion Analytical Structure

```
CONTEXT: Given the [CONSIDERATION] offer for [TARGET] and the full valuation file ([FILE]). The board reviews this before voting, so methodology weightings must be stated and defended.

ROLE: Managing Director at a large sell-side firm preparing the analytical structure for a board fairness opinion. Apply the standard you would defend in that room.

ACTION:
  1. Fairness opinion analytical framework for [TARGET] at [CONSIDERATION]. Methods: DCF, comparable companies, precedent transactions, LBO floor, 52-week trading range. Standing rule: after any multi-step numerical work, write and run a Python script recomputing every derived figure from stated inputs; print PASS/FAIL per check; correct and rerun until all pass.

FORMAT: Football field with methodology ranges and majority fairness assessment.

Workbook:
Sheet 1 FOOTBALL_FIELD: methodology, low, high, consideration, in_range
Sheet 2 METHODOLOGY_DETAIL: assumptions, source, date per method

TONE: Deal-side analytical. State what is assumed versus what is disclosed. No recommendation on whether to transact.
```

## Chapter 4 — The Macro Risk Desk

### PROMPT 17 — The Ray Dalio All-Weather Portfolio Environment Assessment

```
CONTEXT: Attached: the current holdings file with weights and asset class tags ([FILE]). Growth and inflation regime indicators are in tab two. Output feeds the quarterly allocation review.

ROLE: Senior risk analyst applying the Dalio All-Weather portfolio framework.

ACTION:
  1. Assess current portfolio against Dalio's four economic environments: rising growth/rising inflation, rising growth/falling inflation, falling growth/rising inflation, falling growth/falling inflation. Map each major position to its environment sensitivity. Standing rule: after any multi-step numerical work, write and run a Python script recomputing every derived figure from stated inputs; print PASS/FAIL per check; correct and rerun until all pass.

FORMAT: All-Weather assessment with environment mapping and rebalancing recommendation.

Workbook:
Sheet 1 ENV_MAPPING: position, weight, growth_sensitivity, inflation_sensitivity
Sheet 2 SCENARIO_MATRIX: environment, portfolio_return_est, key_driver

TONE: Macro strategist. Scenarios, not forecasts. Attach a probability or say the probability is unknown.
```

### PROMPT 18 — The Macro Hedge Fund Risk Assessment

```
CONTEXT: You have [PORTFOLIO] positions, benchmark weights and three years of factor returns ([FILE]). Mandate caps active factor exposure at [X]% of tracking error budget.

ROLE: Macro hedge fund risk analyst assessing systematic factor exposures.

ACTION:
  1. Systematic risk assessment for [PORTFOLIO]. Factor exposures: growth, value, quality, momentum, duration, currency. Standing rule: after any multi-step numerical work, write and run a Python script recomputing every derived figure from stated inputs; print PASS/FAIL per check; correct and rerun until all pass.

FORMAT: Risk assessment with factor exposures and stress test results.

Workbook:
Sheet 1 FACTOR_EXPOSURE: factor, active_weight, vs_benchmark, risk_contribution
Sheet 2 STRESS_RESULTS: scenario, portfolio_return, worst_position, loss

TONE: Macro strategist. Scenarios, not forecasts. Attach a probability or say the probability is unknown.
```

### PROMPT 19 — The Deep Portfolio Vulnerability & Assumption Challenge

```
CONTEXT: Available: the current portfolio, the written investment thesis for each core position and recent performance ([FILE]). This review goes to the risk committee, which expects disconfirming evidence.

ROLE: Portfolio manager applying radical transparency to stress-test core assumptions.

ACTION:
  1. Challenge five key portfolio assumptions. For each: state the assumption, the evidence supporting it, the evidence against it, and what happens to the portfolio if the assumption is wrong.

FORMAT: Assumption challenge table with portfolio impact per assumption.

Workbook:
Sheet 1 ASSUMPTION_REVIEW: assumption, evidence_for, evidence_against, confidence
Sheet 2 PORTFOLIO_IMPACT: assumption_wrong, P&L_impact, positions_affected

TONE: Macro strategist. Scenarios, not forecasts. Attach a probability or say the probability is unknown.
```

### PROMPT 20 — The Multi-Scenario Historical & Hypothetical Stress Test

```
CONTEXT: Given [PORTFOLIO] position level exposures and asset class betas ([FILE]). The board sees these numbers, so each scenario shock must map to a stated historical reference.

ROLE: Managing Director at a large sell-side firm running the stress scenarios the board will see. Apply the standard you would defend in that room.

ACTION:
  1. Multi-scenario stress test for [PORTFOLIO]: 2022 Rate Shock (equities -18%, long bonds -31%), 2008 GFC (equities -38%, credit spread +300bps), 2020 COVID Crash (equities -34%, recovery V-shaped), custom scenario [DESCRIBE]. Portfolio P&L per position in each. Standing rule: after any multi-step numerical work, write and run a Python script recomputing every derived figure from stated inputs; print PASS/FAIL per check; correct and rerun until all pass.

FORMAT: Stress test results by position and scenario with comparison table.

Workbook:
Sheet 1 STRESS_TEST: position, weight, 2022_pl, 2008_pl, 2020_pl, custom_pl
Sheet 2 SCENARIO_SUMMARY: scenario, total_loss, worst_position, recovery_est

TONE: Macro strategist. Scenarios, not forecasts. Attach a probability or say the probability is unknown.
```

### PROMPT 21 — The Institutional Tail Risk Quantification & Hedging Framework

```
CONTEXT: Working from [PORTFOLIO] daily returns over [PERIOD] ([FILE]) and current option pricing in tab two. Hedging budget is capped at [X]% of assets per year.

ROLE: Institutional risk analyst quantifying tail risk and hedging costs.

ACTION:
  1. Tail risk quantification for [PORTFOLIO]. CVaR at 95% and 99%. Standing rule: after any multi-step numerical work, write and run a Python script recomputing every derived figure from stated inputs; print PASS/FAIL per check; correct and rerun until all pass.

FORMAT: Tail risk metrics with hedging recommendations and cost analysis.

Workbook:
Sheet 1 TAIL_METRICS: VaR_95, VaR_99, CVaR_95, CVaR_99, max_drawdown
Sheet 2 DISTRIBUTION: skewness, kurtosis, fat_tail_indicator

TONE: Macro strategist. Scenarios, not forecasts. Attach a probability or say the probability is unknown.
```

### PROMPT 22 — The Multi-Currency Portfolio FX Exposure & Hedging Strategy

```
CONTEXT: Attached: [PORTFOLIO] holdings with listing currency, plus revenue by geography for the largest positions ([FILE]). Base currency is [CUR]. Hedging policy permits forwards only.

ROLE: Portfolio strategist managing multi-currency FX exposure and hedge ratios.

ACTION:
  1. FX exposure analysis for [PORTFOLIO]. Map all positions to underlying currency exposures including indirect (e.g.

FORMAT: FX exposure map with hedge ratio recommendation and instrument selection.

Workbook:
Sheet 1 FX_EXPOSURE: position, base_currency, revenue_currency, indirect_fx_pct
Sheet 2 NET_EXPOSURE: currency_pair, gross, natural_hedge, net, recommendation

TONE: Macro strategist. Scenarios, not forecasts. Attach a probability or say the probability is unknown.
```

### PROMPT 23 — The Portfolio Liquidity Profile & Redemption Risk Analysis

```
CONTEXT: Every [PORTFOLIO] position carries average daily traded volume and bid ask spreads in [FILE]. The fund offers [FREQUENCY] redemption, so exit timelines bound the answer.

ROLE: Liquidity risk analyst profiling portfolio exit timelines and redemption capacity.

ACTION:
  1. Liquidity profile for [PORTFOLIO]. For each position: daily ADTV, days to liquidate at 20% ADTV, market impact estimate.

FORMAT: Liquidity profile with exit timeline by position and redemption scenario.

Workbook:
Sheet 1 LIQUIDITY_PROFILE: position, weight, ADTV, days_to_exit, liquidity_score
Sheet 2 REDEMPTION_SCENARIO: pct_redemption, liquidatable_1d, 5d, 20d, shortfall

TONE: Macro strategist. Scenarios, not forecasts. Attach a probability or say the probability is unknown.
```

### PROMPT 24 — The Portfolio Drawdown Attribution & Recovery Analysis

```
CONTEXT: Position level returns for [PORTFOLIO] over [PERIOD] are in [FILE], with benchmark and factor return series. The committee wants factor losses separated from selection losses.

ROLE: Managing Director at a large sell-side firm attributing drawdown sources for the board. Separate factor losses from selection losses as you would defend them in that room.

ACTION:
  1. Drawdown attribution for [PORTFOLIO] over [PERIOD]. Decompose total drawdown into: factor contributions (growth, value, quality, momentum), sector contributions, and idiosyncratic stock contributions. Standing rule: after any multi-step numerical work, write and run a Python script recomputing every derived figure from stated inputs; print PASS/FAIL per check; correct and rerun until all pass.

FORMAT: Drawdown attribution table with factor and stock decomposition.

Workbook:
Sheet 1 DRAWDOWN_ATTRIBUTION: source, contribution_bps, pct_of_total
Sheet 2 FACTOR_CONTRIBUTION: factor, factor_return, portfolio_exposure, P&L

TONE: Macro strategist. Scenarios, not forecasts. Attach a probability or say the probability is unknown.
```

## Chapter 5 — The Earnings Intelligence Desk

### PROMPT 25 — The Institutional Pre-Earnings Intelligence Brief

```
CONTEXT: [COMPANY] reports in [N] days. Available: the last four transcripts, current consensus estimates and the desk model ([FILE]). Actions must be committed before the print, not after.

ROLE: Managing Director at a large sell-side firm signing off on the pre-earnings brief before the print. Apply the standard you would defend after the result is known.

ACTION:
  1. Pre-earnings intelligence brief for [COMPANY], reporting in [N] days. Three thesis-critical KPIs with consensus estimate and your estimate.

FORMAT: Pre-earnings brief with decision matrix. Commit all actions before the print.

Workbook:
Sheet 1 KPI_TRACKER: KPI, consensus, my_estimate, bull_level, bear_level
Sheet 2 DECISION_MATRIX: scenario, trigger_condition, pre_committed_action

TONE: Earnings desk. Separate what management said from what the numbers show. No surprise predictions stated as fact.
```

### PROMPT 26 — The Management Tone Trajectory Analysis

```
CONTEXT: Attached: the last four [COMPANY] earnings call transcripts ([FILE]), prepared remarks and Q&A separated. Ratings feed a coverage note, so each one needs a quoted line.

ROLE: Senior research analyst applying systematic management tone analysis.

ACTION:
  1. Analyse last four earnings call transcripts for [COMPANY]. Per quarter: rate CONSTRUCTIVE/NEUTRAL/CAUTIOUS/MORE CAUTIOUS.

FORMAT: Tone trajectory table with keyword frequency shifts and synthesis.

Workbook:
Sheet 1 TONE_TRACKER: quarter, rating, positive_count, negative_count
Sheet 2 KEYWORD_ANALYSIS: word, Q-3, Q-2, Q-1, Q0, trend_direction

TONE: Earnings desk. Separate what management said from what the numbers show. No surprise predictions stated as fact.
```

### PROMPT 27 — The Management Guidance Reliability Scorecard

```
CONTEXT: You have eight quarters of [COMPANY] guidance statements and reported actuals ([FILE]). Guided ranges changed definition midway. The scorecard informs how much weight next quarter's guidance carries.

ROLE: Equity analyst building a guidance quality and credibility scorecard.

ACTION:
  1. Guidance quality analysis for [COMPANY] over last 8 quarters. For each: guided metric, guided range, actual result, beat/miss, magnitude.

FORMAT: Guidance accuracy scorecard with credibility rating and bias assessment.

Workbook:
Sheet 1 GUIDANCE_HISTORY: quarter, metric, guided, actual, beat_miss, magnitude
Sheet 2 CREDIBILITY_SCORE: metric, hit_rate, avg_magnitude, bias_direction

TONE: Earnings desk. Separate what management said from what the numbers show. No surprise predictions stated as fact.
```

### PROMPT 28 — The Institutional Segment-Level Revenue Intelligence Framework

```
CONTEXT: Given [COMPANY] segment disclosures across the last eight quarters plus matching management commentary ([FILE]). Segment definitions were restated once. Output feeds a thesis check on mix.

ROLE: Sector analyst decomposing segment-level revenue and mix dynamics.

ACTION:
  1. Segment revenue intelligence for [COMPANY]. For each segment: revenue, growth rate, margin, management commentary. Standing rule: after any multi-step numerical work, write and run a Python script recomputing every derived figure from stated inputs; print PASS/FAIL per check; correct and rerun until all pass.

FORMAT: Segment decomposition with emphasis analysis and mix attribution.

Workbook:
Sheet 1 SEGMENT_TABLE: segment, revenue, growth, margin, mgmt_emphasis_flag
Sheet 2 MIX_ANALYSIS: geography, organic_vs_acq, price_vs_volume

TONE: Earnings desk. Separate what management said from what the numbers show. No surprise predictions stated as fact.
```

### PROMPT 29 — The Forensic Earnings Quality & Cash Conversion Analysis

```
CONTEXT: Working from [COMPANY] income statements, cash flow statements and balance sheets for [N] years ([FILE]). Only audited figures are available; restatement history sits in tab two.

ROLE: Forensic analyst assessing earnings quality and cash conversion.

ACTION:
  1. Forensic earnings quality analysis for [COMPANY]. Sloan accruals ratio (should be near zero). Standing rule: after any multi-step numerical work, write and run a Python script recomputing every derived figure from stated inputs; print PASS/FAIL per check; correct and rerun until all pass.

FORMAT: Earnings quality scorecard with red flags and cash conversion analysis.

Workbook:
Sheet 1 ACCRUALS_ANALYSIS: year, net_income, CFO, accruals, sloan_ratio
Sheet 2 CASH_CONVERSION: year, net_income, FCF, conversion_pct, trend

TONE: Earnings desk. Separate what management said from what the numbers show. No surprise predictions stated as fact.
```

### PROMPT 30 — The Consensus Estimate Positioning & Expectations Framework

```
CONTEXT: Attached: analyst ratings, estimate revisions and short interest for [COMPANY] ahead of [EVENT] ([FILE]). Positioning data lags by [N] days. The read informs sizing, not direction.

ROLE: Senior analyst mapping consensus positioning and sentiment extremes.

ACTION:
  1. Consensus positioning analysis for [COMPANY] before [EVENT]. % of analysts with buy/hold/sell ratings.

FORMAT: Consensus positioning map with sentiment extremes identified.

Workbook:
Sheet 1 ANALYST_RATINGS: buy_pct, hold_pct, sell_pct, vs_sector_avg
Sheet 2 SHORT_INTEREST: short_float_pct, days_to_cover, trend_3m

TONE: Earnings desk. Separate what management said from what the numbers show. No surprise predictions stated as fact.
```

### PROMPT 31 — The Institutional Post-Earnings Position Management

```
CONTEXT: [COMPANY] has reported [RESULT]. The pre-committed decision matrix and thesis document are in [FILE]. The record must show the matrix decided, so no new reasoning is introduced.

ROLE: Managing Director at a large sell-side firm executing the pre-committed post-earnings protocol. Apply the standard you would defend to the committee: the matrix decides, the record shows it.

ACTION:
  1. Post-earnings position management protocol for [COMPANY] following [RESULT]. Assess: did KPIs meet pre-committed thresholds? Apply pre-committed decision matrix.

FORMAT: Post-earnings decision record with thesis update and position action.

Workbook:
Sheet 1 RESULT_VS_MATRIX: KPI, threshold, actual, pass_fail, action_triggered
Sheet 2 THESIS_UPDATE: thesis_element, pre_earnings, post_earnings, change

TONE: Earnings desk. Separate what management said from what the numbers show. No surprise predictions stated as fact.
```

### PROMPT 32 — The Multi-Company Earnings Season Monitoring

```
CONTEXT: Available: reporting dates for [N] coverage names and the existing thesis file ([FILE]). Several names report on the same day. The dashboard is updated daily through the season.

ROLE: Research team lead managing multi-company earnings season monitoring.

ACTION:
  1. Earnings season monitoring dashboard for [N] coverage names. Build a calendar with reporting dates, KPI thresholds, and pre-committed actions for each.

FORMAT: Earnings season dashboard with all coverage names and running theme tracker.

Workbook:
Sheet 1 EARNINGS_CALENDAR: company, report_date, key_KPIs, pre_committed_action
Sheet 2 RESULTS_TRACKER: company, beat_miss, guidance_direction, thesis_impact

TONE: Earnings desk. Separate what management said from what the numbers show. No surprise predictions stated as fact.
```

## Chapter 6 — The Portfolio Strategy Desk

### PROMPT 33 — The Institutional Investment Policy Statement Construction

```
CONTEXT: Available: [CLIENT/FUND] financial position, stated objectives and the trustee minutes covering constraints ([FILE]). The client signs this document, so every constraint needs a clause reference.

ROLE: Managing Director at a large sell-side firm constructing the Investment Policy Statement the client will sign. Apply the standard you would defend to the investment committee.

ACTION:
  1. Build a complete Investment Policy Statement for [CLIENT/FUND].
  2. RRTTLLU framework: Return objective (specific % or benchmark+X%), Risk tolerance (max drawdown, tracking error), Time horizon (years), Tax (jurisdiction and treatment), Liquidity (annual needs), Legal (mandate constraints), Unique (specific exclusions/requirements).

FORMAT: IPS policy document with all seven RRTTLLU dimensions documented.

Workbook:
Sheet 1 RRTTLLU: factor, constraint, rationale, IPS_clause_reference
Sheet 2 PROHIBITED_INSTRUMENTS: instrument, reason, exception_process

TONE: Portfolio strategy. Positions framed against a stated policy benchmark. No performance promises.
```

### PROMPT 34 — The Strategic Asset Allocation & Risk Budgeting Framework

```
CONTEXT: You have the [FUND] IPS, long term capital market assumptions and a correlation matrix ([FILE]). Alternatives are capped at [X]% by mandate. Assumptions carry a stated vintage.

ROLE: Senior portfolio manager building strategic asset allocation and risk budget.

ACTION:
  1. Strategic Asset Allocation for [FUND]. Asset classes: global equity, fixed income, alternatives, real assets, cash. Standing rule: after any multi-step numerical work, write and run a Python script recomputing every derived figure from stated inputs; print PASS/FAIL per check; correct and rerun until all pass.

FORMAT: SAA with efficient frontier analysis and risk budget allocation.

Workbook:
Sheet 1 SAA_TABLE: asset_class, target_wt, exp_return, exp_vol, benchmark
Sheet 2 CORRELATION_MATRIX: pairwise correlations across all asset classes

TONE: Portfolio strategy. Positions framed against a stated policy benchmark. No performance promises.
```

### PROMPT 35 — The Tactical Asset Allocation & Factor Tilt Protocol

```
CONTEXT: Attached: the [FUND] strategic allocation and current market conditions summary ([FILE]). Tactical deviation is limited to [X]% per asset class. Tilts are reviewed at the next quarterly meeting.

ROLE: Tactical strategist designing active tilts around the strategic allocation.

ACTION:
  1. Tactical asset allocation overlay for [FUND] vs SAA. Current market conditions: [DESCRIBE BRIEFLY].

FORMAT: TAA overlay with specific tilts, rationale, and reversal conditions.

Workbook:
Sheet 1 TAA_TILTS: asset_class, SAA_weight, TAA_weight, active_tilt, rationale
Sheet 2 FACTOR_TILTS: factor, direction, magnitude, time_horizon, reversal_trigger

TONE: Portfolio strategy. Positions framed against a stated policy benchmark. No performance promises.
```

### PROMPT 36 — The GIPS-Compliant Performance Reporting Framework

```
CONTEXT: Given [COMPOSITE] account level returns, cash flows and fee schedules for [DATES] ([FILE]). The report goes to prospective clients, so required disclosures cannot be abbreviated.

ROLE: GIPS-compliant performance reporting specialist.

ACTION:
  1. GIPS-compliant performance reporting for [COMPOSITE] for period [DATES]. Time-weighted return calculation. Standing rule: after any multi-step numerical work, write and run a Python script recomputing every derived figure from stated inputs; print PASS/FAIL per check; correct and rerun until all pass.

FORMAT: GIPS-compliant performance report with all required disclosures.

Workbook:
Sheet 1 PERFORMANCE: TWR, benchmark, active_return, information_ratio
Sheet 2 COMPOSITE_STATS: accounts, assets, dispersion, composite_definition

TONE: Portfolio strategy. Positions framed against a stated policy benchmark. No performance promises.
```

### PROMPT 37 — The Institutional Portfolio Rebalancing Policy & Execution

```
CONTEXT: Working from [FUND] current weights, target weights and broker cost estimates ([FILE]). The policy band is [X]% per asset class. Trades settle before the quarter end reporting date.

ROLE: Portfolio operations analyst managing rebalancing policy and execution.

ACTION:
  1. Portfolio rebalancing analysis for [FUND]. Current weights vs SAA targets.

FORMAT: Rebalancing trade list with cost analysis and execution priority.

Workbook:
Sheet 1 DRIFT_ANALYSIS: asset_class, current_wt, target_wt, drift, band_breach
Sheet 2 TRADE_LIST: instrument, direction, size, est_cost_bps, priority

TONE: Portfolio strategy. Positions framed against a stated policy benchmark. No performance promises.
```

### PROMPT 38 — The Multi-Asset Portfolio Construction & Optimisation

```
CONTEXT: [MANDATE] terms, the eligible instrument list and available return assumptions are in [FILE]. The blueprint goes to the investment committee for approval before any capital is deployed.

ROLE: Multi-asset portfolio construction specialist.

ACTION:
  1. Multi-asset portfolio construction for [MANDATE]. Asset class selection rationale.

FORMAT: Portfolio construction blueprint with diversification analysis.

Workbook:
Sheet 1 PORTFOLIO_BLUEPRINT: asset_class, instrument, weight, rationale
Sheet 2 DIVERSIFICATION: pairwise_correlations, concentration_flags

TONE: Portfolio strategy. Positions framed against a stated policy benchmark. No performance promises.
```

### PROMPT 39 — The Client Portfolio Review & Communication Framework

```
CONTEXT: Attached: [CLIENT] portfolio performance, the signed IPS and stated goals with target dates ([FILE]). The client's investment committee reads this, so plain language matters as much as accuracy.

ROLE: Managing Director at a large sell-side firm presenting the portfolio review to the client's investment committee. Apply the standard you would defend in that room.

ACTION:
  1. Client portfolio review for [CLIENT]. Performance vs IPS return objective.

FORMAT: Client review package with performance, risk, goals, and recommendations.

Workbook:
Sheet 1 PERFORMANCE_VS_IPS: metric, target, actual, on_track
Sheet 2 GOAL_TRACKER: goal, target_date, current_status, probability

TONE: Portfolio strategy. Positions framed against a stated policy benchmark. No performance promises.
```

### PROMPT 40 — The Institutional Risk-Adjusted Return Analysis

```
CONTEXT: You have [PORTFOLIO] and benchmark return series over [PERIOD] plus holdings history ([FILE]). Attribution feeds a manager review, so factor returns and selection returns stay separate.

ROLE: Risk-adjusted performance analyst decomposing attribution by decision type.

ACTION:
  1. Risk-adjusted return analysis for [PORTFOLIO] over [PERIOD]. Standing rule: after any multi-step numerical work, write and run a Python script recomputing every derived figure from stated inputs; print PASS/FAIL per check; correct and rerun until all pass.
  2. Sharpe ratio, Sortino ratio, Calmar ratio, Information ratio vs benchmark.

FORMAT: Risk-adjusted return report with full attribution decomposition.

Workbook:
Sheet 1 RISK_METRICS: Sharpe, Sortino, Calmar, IR, max_drawdown, beta
Sheet 2 ATTRIBUTION: beta_return, factor_return, selection_return, total

TONE: Portfolio strategy. Positions framed against a stated policy benchmark. No performance promises.
```

## Chapter 7 — The Quant Trading Desk

### PROMPT 41 — The Statistical Edge Discovery & Pattern Analysis

```
CONTEXT: Attached: [TICKER] daily price history covering [PERIOD] ([FILE]) plus the event calendar. Findings feed the research committee, so any pattern without sample size stays out.

ROLE: Quantitative researcher identifying statistically significant, economically-justified patterns.

ACTION:
  1. Identify statistically significant patterns for [TICKER] over [TIME PERIOD]. Seasonal patterns: best/worst calendar months with p-value and sample size.

FORMAT: Pattern table with p-values, sample sizes, and economic rationale. Exclude any pattern without a credible economic explanation.

Workbook:
Sheet 1 SEASONAL_PATTERNS: month, avg_return, p_value, sample_n, economic_reason
Sheet 2 EVENT_ANALYSIS: event_type, avg_return, p_value, tradeable

TONE: Quant reviewer who must defend the verdict, not the strategy. Paper results labelled paper. No annualised-return promises.
```

### PROMPT 42 — The Technical Analysis & Chart Pattern Recognition Protocol

```
CONTEXT: You have daily, weekly and monthly price series for [TICKER] in [FILE], nothing fundamental. The desk trades this book intraday, so levels must be current as of [DATE].

ROLE: Technical analyst applying multi-timeframe trend and momentum analysis.

ACTION:
  1. Technical analysis for [TICKER]. Trend identification: daily/weekly/monthly alignment.

FORMAT: Technical analysis brief with entry/stop/target and R:R flagged if below 2:1.

Workbook:
Sheet 1 TREND_ANALYSIS: timeframe, direction, key_levels, momentum_signal
Sheet 2 TRADE_SETUP: entry_zone, stop_level, target_1, target_2, R_R

TONE: Quant reviewer who must defend the verdict, not the strategy. Paper results labelled paper. No annualised-return promises.
```

### PROMPT 43 — The Options Strategy & Derivatives Analysis

```
CONTEXT: Available: the option chain for [UNDERLYING] as of [DATE] close, plus 30 and 90 day realised volatility. Mandate permits defined-risk structures only; naked short options are excluded.

ROLE: Derivatives specialist analysing options strategies and Greeks.

ACTION:
  1. Options strategy analysis for [UNDERLYING]. Current implied vol vs historical vol: is optionality cheap or expensive? Relevant strategies: covered call, protective put, collar, straddle/strangle.

FORMAT: Options strategy comparison with P&L profiles and Greeks.

Workbook:
Sheet 1 VOL_ANALYSIS: impl_vol, hist_vol_30d, hist_vol_90d, vol_premium
Sheet 2 STRATEGIES: strategy, debit/credit, max_profit, max_loss, breakeven

TONE: Quant reviewer who must defend the verdict, not the strategy. Paper results labelled paper. No annualised-return promises.
```

### PROMPT 44 — The Institutional Investment Strategy Backtesting Engine

```
CONTEXT: Price and signal data for [UNIVERSE] across [PERIOD] sit in [FILE]. Results go to the risk committee, which rejects any backtest without an untouched out-of-sample window.

ROLE: Quantitative strategist running systematic backtesting with walk-forward validation.

ACTION:
  1. Backtest [STRATEGY] on [UNIVERSE] over [PERIOD]. Signal: [DESCRIBE LOGIC].

FORMAT: Backtest results with walk-forward validation. In-sample and out-of-sample reported separately.

Workbook:
Sheet 1 BACKTEST_RESULTS: period, ann_return, Sharpe, max_DD, turnover
Sheet 2 WALK_FORWARD: in_sample_Sharpe, out_sample_Sharpe, degradation_pct

TONE: Quant reviewer who must defend the verdict, not the strategy. Paper results labelled paper. No annualised-return promises.
```

### PROMPT 45 — The High-Frequency Signal & Market Microstructure Analysis

```
CONTEXT: Order book snapshots, the trade tape and short interest for [TICKER] are in [FILE], vintage [DATE]. The execution desk uses this before sizing the next order.

ROLE: Market microstructure analyst assessing order flow and institutional positioning.

ACTION:
  1. Market microstructure analysis for [TICKER]. Bid-ask spread: current vs historical average.

FORMAT: Microstructure signals with order flow and short interest analysis.

Workbook:
Sheet 1 SPREAD_ANALYSIS: date, bid_ask_bps, vs_30d_avg, liquidity_flag
Sheet 2 ORDER_FLOW: date, buy_vol_pct, sell_vol_pct, imbalance_signal

TONE: Quant reviewer who must defend the verdict, not the strategy. Paper results labelled paper. No annualised-return promises.
```

### PROMPT 46 — The Cross-Asset Momentum & Relative Value Framework

```
CONTEXT: Attached: twenty years of yield and valuation history for [ASSET CLASS 1] and [ASSET CLASS 2] ([FILE]). Output feeds the quarterly asset allocation meeting.

ROLE: Cross-asset strategist building relative value and momentum frameworks.

ACTION:
  1. Cross-asset relative value analysis. Compare [ASSET CLASS 1] vs [ASSET CLASS 2] on: yield/earnings yield, real yield, z-score vs 20yr history, current positioning (crowded or under-owned).

FORMAT: Cross-asset relative value table with positioning recommendation.

Workbook:
Sheet 1 RELATIVE_VALUE: asset, yield, real_yield, z_score, crowding_flag
Sheet 2 HISTORICAL_CONTEXT: asset, current, 5yr_avg, 10yr_avg, percentile

TONE: Quant reviewer who must defend the verdict, not the strategy. Paper results labelled paper. No annualised-return promises.
```

### PROMPT 47 — The Quantitative Portfolio Optimisation

```
CONTEXT: Expected returns, the covariance matrix and current holdings for [UNIVERSE] are supplied in [FILE]. Mandate caps any single position at [X]% and any sector at [X]%.

ROLE: Portfolio optimisation specialist applying mean-variance with constraints.

ACTION:
  1. Quantitative portfolio optimisation for [UNIVERSE]. Inputs: expected returns (factor model), covariance matrix (historical + shrinkage), constraints (max position [X]%, max sector [X]%, min diversification).

FORMAT: Optimal portfolio weights with efficient frontier and sensitivity analysis.

Workbook:
Sheet 1 OPTIMAL_WEIGHTS: ticker, weight, expected_contribution, risk_contribution
Sheet 2 EFFICIENT_FRONTIER: portfolio, return, vol, Sharpe, max_drawdown

TONE: Quant reviewer who must defend the verdict, not the strategy. Paper results labelled paper. No annualised-return promises.
```

### PROMPT 48 — The Institutional Trade Plan & Risk Management

```
CONTEXT: Nothing has been bought yet. Research, price levels and position limits for [TICKER] sit in [FILE]; the plan is defended at the risk committee before any order goes out.

ROLE: Head of trading at a multi-strategy fund, constructing the pre-committed trade plan to be defended before the risk committee.

ACTION:
  1. Complete trade plan for [TICKER] before initiating any position.
  2. Investment thesis: 2 sentences.

FORMAT: Complete pre-committed trade plan. All levels documented before any position is taken.

Workbook:
Sheet 1 TRADE_PLAN: entry_zone, stop, T1, T2, R_R, position_size, rationale
Sheet 2 MONITORING_KPIS: KPI, current_level, confirm_at, reject_at

TONE: Quant reviewer who must defend the verdict, not the strategy. Paper results labelled paper. No annualised-return promises.
```

## Chapter 8 — The Strategy Consulting Desk

### PROMPT 49 — The Institutional Competitive Landscape & Market Structure

```
CONTEXT: Attached: filings and revenue disclosures for the largest listed players in [SECTOR] ([FILE]). Figures are last reported fiscal year. The map feeds an initiation report.

ROLE: Senior strategy analyst mapping competitive landscape and market structure.

ACTION:
  1. Competitive landscape analysis for [SECTOR/INDUSTRY]. Top 5-7 companies by revenue/market cap.

FORMAT: Competitive landscape table with moat assessment and trajectory.

Workbook:
Sheet 1 COMPETITIVE_TABLE: company, revenue, market_share, margin, moat_type, trajectory
Sheet 2 SHARE_TRENDS: company, channel, Q1_to_Q8, direction, inflection_date

TONE: Consulting register. Recommendations tied to stated evidence. Flag every assumption that carries the conclusion.
```

### PROMPT 50 — The Porter Five Forces Industry Attractiveness Framework

```
CONTEXT: You have industry revenue, margin and capacity data for [INDUSTRY] in [FILE]. The scorecard supports a sector weighting decision, so each rating needs named evidence behind it.

ROLE: Industry analyst applying Porter's Five Forces framework.

ACTION:
  1. Porter Five Forces analysis for [INDUSTRY]. Each force: rate intensity LOW/MEDIUM/HIGH with specific evidence.

FORMAT: Five Forces scorecard with attractiveness rating and investment implication.

Workbook:
Sheet 1 FIVE_FORCES: force, intensity, key_driver, trend, evidence
Sheet 2 ATTRACTIVENESS: overall_score, vs_adjacent_industries, trend

TONE: Consulting register. Recommendations tied to stated evidence. Flag every assumption that carries the conclusion.
```

### PROMPT 51 — The Competitive Advantage Period & Moat Width Assessment

```
CONTEXT: Ten years of returns on capital, pricing and market share for [COMPANY] are available in [FILE]. The estimate drives the fade period in a valuation model.

ROLE: Equity analyst assessing competitive advantage period and moat durability.

ACTION:
  1. Competitive advantage period (CAP) assessment for [COMPANY]. For each moat type present (brand, cost, network, switching): evidence, durability (years), trajectory.

FORMAT: Moat width assessment with CAP estimate and durability evidence.

Workbook:
Sheet 1 MOAT_SCORECARD: moat_type, evidence, durability_yrs, trajectory
Sheet 2 ROIC_VS_WACC: year, ROIC, WACC, spread, trend

TONE: Consulting register. Recommendations tied to stated evidence. Flag every assumption that carries the conclusion.
```

### PROMPT 52 — The Channel-Level Market Share & Competitive Dynamics Framework

```
CONTEXT: Distributor and retailer shipment data covering eight quarters for [COMPANY] and [COMPETITOR] sit in [FILE]. Channel definitions vary by region and must be stated before comparison.

ROLE: Channel intelligence analyst tracking market share at the distribution level.

ACTION:
  1. Channel-level market share analysis for [COMPANY] vs [COMPETITOR].
  2. Distribution channels: [LIST].

FORMAT: Channel market share table with 8-quarter trend and divergence analysis.

Workbook:
Sheet 1 CHANNEL_SHARE: company, channel, Q1_to_Q8, trend
Sheet 2 DIVERGENCE_ANALYSIS: channel, share_delta, EBITDA_lag_correlation

TONE: Consulting register. Recommendations tied to stated evidence. Flag every assumption that carries the conclusion.
```

### PROMPT 53 — The Institutional SWOT & Strategic Position Assessment

```
CONTEXT: Attached: [COMPANY]'s latest annual report, the peer comparison in [FILE] and recent management commentary. Output goes into a client strategy review, so generic statements will be rejected.

ROLE: Strategic analyst building an evidence-backed SWOT assessment.

ACTION:
  1. SWOT analysis for [COMPANY]. Each item must have specific evidence and a magnitude estimate, not a generic statement.

FORMAT: Evidence-backed SWOT with strategic priorities and threat mitigation plan.

Workbook:
Sheet 1 SWOT_TABLE: category, item, specific_evidence, magnitude, rank
Sheet 2 STRATEGIC_PRIORITIES: priority, rationale, KPI_to_monitor, timeline

TONE: Consulting register. Recommendations tied to stated evidence. Flag every assumption that carries the conclusion.
```

### PROMPT 54 — The Technology Disruption & Business Model

```
CONTEXT: Available: [COMPANY]'s segment revenue breakdown plus competitor product announcements collected through [DATE]. The assessment feeds a position review scheduled for the next research meeting.

ROLE: Technology disruption analyst evaluating competitive threat timelines.

ACTION:
  1. Technology disruption assessment for [COMPANY]. Identify 3-4 technology threats: what technology, which competitor is deploying it, timeline, potential revenue impact.

FORMAT: Disruption threat assessment with timeline and response capability rating.

Workbook:
Sheet 1 DISRUPTION_THREATS: technology, deployer, timeline, revenue_impact_pct, severity
Sheet 2 RESPONSE_CAPABILITY: threat, internal_capability, partnership_option, M&A_option

TONE: Consulting register. Recommendations tied to stated evidence. Flag every assumption that carries the conclusion.
```

### PROMPT 55 — The Institutional Pricing Power & Revenue Quality Analysis

```
CONTEXT: Five years of revenue, volume and gross margin detail for [COMPANY] and its peer set are in [FILE]. Segment reporting changed once inside the window.

ROLE: Revenue quality analyst decomposing pricing power and margin flow-through.

ACTION:
  1. Pricing power analysis for [COMPANY]. Revenue decomposition: price contribution vs volume contribution last 5 years.

FORMAT: Pricing power scorecard with margin flow-through and peer comparison.

Workbook:
Sheet 1 PRICE_VOLUME: year, revenue_growth, price_contribution, volume_contribution
Sheet 2 MARGIN_FLOWTHROUGH: year, price_increase, gross_margin_change, flowthrough_pct

TONE: Consulting register. Recommendations tied to stated evidence. Flag every assumption that carries the conclusion.
```

### PROMPT 56 — The Single Best Investment Thesis Construction

```
CONTEXT: Prior work on [COMPANY] sits in [FILE], including the model and the competitive review. The thesis is defended at investment committee, where the invalidating condition is asked for first.

ROLE: Managing Director at a large sell-side firm, constructing the single best investment thesis to be defended before the investment committee.

ACTION:
  1. Single best investment thesis for [COMPANY]. What: one paragraph describing the business and why it is mispriced.

FORMAT: Investment thesis document with catalyst, KPIs, and invalidating condition.

Workbook:
Sheet 1 THESIS_SUMMARY: what, why_1, why_2, why_3, why_now, catalyst_date
Sheet 2 KPI_MONITOR: KPI, current, confirm_level, deny_level, monitoring_freq

TONE: Consulting register. Recommendations tied to stated evidence. Flag every assumption that carries the conclusion.
```

## Chapter 9 — The Endowment Strategy Desk

### PROMPT 57 — The Yale/Harvard Endowment SAA Framework

```
CONTEXT: You have [INSTITUTION]'s current allocation, spending policy and liquidity schedule in [FILE]. The proposed allocation goes to the investment committee at its next quarterly meeting.

ROLE: CIO of the endowment, applying the Yale/Harvard SAA framework and presenting the allocation to the investment committee.

ACTION:
  1. Yale/Harvard endowment SAA framework for [INSTITUTION], [AUM].
  2. Asset classes: public equity, fixed income, PE/VC, real assets, hedge funds, real estate.

FORMAT: Endowment SAA with spending policy sustainability analysis.

Workbook:
Sheet 1 SAA_TABLE: asset_class, target_wt, exp_return, liquidity_bucket, benchmark
Sheet 2 SPENDING_SUSTAINABILITY: spending_rate, real_return_assumed, 20yr_projection

TONE: Endowment committee. Long-horizon language. Spending policy stated as a constraint, not an outcome.
```

### PROMPT 58 — The Illiquidity Premium & Alternative Asset Allocation Protocol

```
CONTEXT: Attached: [PORTFOLIO] holdings with commitment and distribution history ([FILE]). Realised premium figures are net of fees. Governance constraints on lock-up length sit in the policy statement.

ROLE: Alternative investments specialist quantifying illiquidity premium and budget.

ACTION:
  1. Illiquidity premium analysis for [PORTFOLIO]. For each illiquid asset class (PE, VC, real estate, infrastructure): expected return premium over liquid equivalent, historical realised premium, time horizon required, governance requirements.

FORMAT: Illiquidity premium table with budget calculation and governance requirements.

Workbook:
Sheet 1 ILLIQ_PREMIUM: asset_class, liquid_equivalent, expected_premium, hist_premium
Sheet 2 ILLIQUIDITY_BUDGET: annual_ops, emergency_reserve, total_liquid_required, max_illiquid_pct

TONE: Endowment committee. Long-horizon language. Spending policy stated as a constraint, not an outcome.
```

### PROMPT 59 — The Private Equity & Venture Capital Allocation Framework

```
CONTEXT: Existing fund commitments by vintage year for [ENDOWMENT/FUND] are listed in [FILE]. The programme runs against an annual commitment budget approved by the trustees.

ROLE: PE and VC allocation specialist designing vintage diversification strategy.

ACTION:
  1. PE and VC allocation framework for [ENDOWMENT/FUND]. Vintage year diversification: target number of commitments per year.

FORMAT: PE/VC allocation framework with vintage diversification and manager selection criteria.

Workbook:
Sheet 1 PE_VC_FRAMEWORK: strategy, target_pct, geography_mix, stage_mix
Sheet 2 VINTAGE_CALENDAR: year, target_commitments, stage, geography_focus

TONE: Endowment committee. Long-horizon language. Spending policy stated as a constraint, not an outcome.
```

### PROMPT 60 — The Endowment Spending Policy & Perpetuity Assessment

```
CONTEXT: Available: [INSTITUTION]'s spending history, gift inflows and long-run return assumptions ([FILE]). Trustees have asked whether the current rate survives a decade of lower real returns.

ROLE: CIO of the endowment, stress-testing spending policy sustainability for the investment committee.

ACTION:
  1. Endowment spending policy analysis for [INSTITUTION]. Current spending rate vs long-run real return assumption.

FORMAT: Spending policy sustainability model with three scenarios and rule options.

Workbook:
Sheet 1 SPENDING_MODEL: scenario, spending_rate, real_return, real_growth_yr, 20yr_real_value
Sheet 2 RULE_OPTIONS: rule_type, description, pros, cons, sustainability_under_stress

TONE: Endowment committee. Long-horizon language. Spending policy stated as a constraint, not an outcome.
```

### PROMPT 61 — The Real Assets & Infrastructure Allocation Framework

```
CONTEXT: Current real asset exposure and the inflation assumptions used by [PORTFOLIO] are in [FILE]. Direct holdings and listed proxies are recorded separately and should not be merged.

ROLE: Real assets allocation specialist mapping inflation linkage and income.

ACTION:
  1. Real assets allocation analysis for [PORTFOLIO]. Asset classes: listed infrastructure, direct infrastructure, farmland, timber, commodities, TIPS.

FORMAT: Real assets allocation with inflation linkage and liquidity analysis.

Workbook:
Sheet 1 REAL_ASSETS: asset, inflation_linkage, yield, liquidity_score, equity_correlation
Sheet 2 TARGET_ALLOCATION: asset_class, target_pct, instrument, listed_vs_unlisted

TONE: Endowment committee. Long-horizon language. Spending policy stated as a constraint, not an outcome.
```

### PROMPT 62 — The Manager Selection & Due Diligence Protocol

```
CONTEXT: Attached: the manager's track record, team biographies and fee terms for [STRATEGY/ASSET CLASS] ([FILE]). The scorecard is tabled at the alternatives committee alongside two competing candidates.

ROLE: Alternatives due diligence specialist scoring manager selection criteria.

ACTION:
  1. Manager selection due diligence for [STRATEGY/ASSET CLASS].
  2. Evaluation framework: track record (length, market cycles covered), team (tenure, key person risk), process (repeatable, documented), risk management (drawdown history, risk controls), fees (management fee, carry, hurdle).

FORMAT: Manager evaluation scorecard with weighted scores and selection recommendation.

Workbook:
Sheet 1 DUE_DILIGENCE: dimension, weight, score_1to5, evidence, red_flags
Sheet 2 TRACK_RECORD: period, return, benchmark, alpha, sharpe, max_drawdown

TONE: Endowment committee. Long-horizon language. Spending policy stated as a constraint, not an outcome.
```

### PROMPT 63 — The Endowment Rebalancing & Liquidity Management

```
CONTEXT: Holdings, target bands, pending capital calls and expected distributions for [INSTITUTION] are in [FILE], priced as of [DATE]. Cash balances cover operating needs for one quarter.

ROLE: Endowment operations analyst managing rebalancing and liquidity.

ACTION:
  1. Endowment rebalancing and liquidity management for [INSTITUTION].
  2. Rebalancing triggers: which asset classes have drifted beyond bands? Cash generation: which illiquid positions have distributions pending? Capital calls: which commitments are due in next 12 months? Net liquidity position: surplus or deficit?

FORMAT: Rebalancing priority list with liquidity position and capital call schedule.

Workbook:
Sheet 1 REBALANCING_NEEDS: asset_class, current, target, drift, priority
Sheet 2 LIQUIDITY_POSITION: source, amount, timing, certainty

TONE: Endowment committee. Long-horizon language. Spending policy stated as a constraint, not an outcome.
```

### PROMPT 64 — The Multi-Generational Wealth Preservation Framework

```
CONTEXT: The investment policy statement and beneficiary obligations for [FAMILY/INSTITUTION] sit in [FILE]. Family governance is informal today, and the framework has to work without full-time staff.

ROLE: Family office or endowment strategist designing multi-generational framework.

ACTION:
  1. Multi-generational wealth preservation framework for [FAMILY/INSTITUTION]. Objectives across three time horizons: current generation (10yr), next generation (30yr), perpetuity.

FORMAT: Multi-generational framework with time-horizon allocation and governance structure.

Workbook:
Sheet 1 HORIZON_ALLOCATION: horizon, asset_class, target_wt, rationale
Sheet 2 GOVERNANCE_STRUCTURE: decision_type, decision_maker, review_frequency

TONE: Endowment committee. Long-horizon language. Spending policy stated as a constraint, not an outcome.
```

## Chapter 10 — The Sovereign Wealth Desk

### PROMPT 65 — The NBIM Norway GPFG Total Portfolio Framework

```
CONTEXT: Attached: [SOVEREIGN FUND]'s current holdings, benchmark definitions and the mandate letter ([FILE]). The framework is presented to the board, which approves benchmarks rather than individual positions.

ROLE: CIO of the sovereign wealth fund, presenting the total portfolio framework to the board.

ACTION:
  1. Total portfolio framework for [SOVEREIGN FUND], [$AUM]. SAA: equity/fixed income/real assets target weights with rationale.

FORMAT: Total portfolio framework document with geographic allocation and mandate rationale.

Workbook:
Sheet 1 SAA_TABLE: asset_class, target_wt, benchmark, rebalancing_rule
Sheet 2 GEOGRAPHIC_ALLOCATION: region, target_wt, GDP_weight, home_bias_analysis

TONE: Sovereign fund governance. Mandate language. Public accountability assumed for every figure.
```

### PROMPT 66 — The Responsible Investment & ESG Integration Protocol

```
CONTEXT: You have [INSTITUTION]'s existing exclusion list, voting record and the ethics council guidance in [FILE]. The policy is published, so every criterion must be testable by an outsider.

ROLE: Responsible investment officer designing ESG integration and engagement policy.

ACTION:
  1. Responsible investment and ESG integration protocol for [INSTITUTION]. Exclusion criteria: define categories and specific tests.

FORMAT: Responsible investment policy with exclusion criteria, engagement protocol, and reporting framework.

Workbook:
Sheet 1 EXCLUSION_CRITERIA: category, specific_test, review_frequency, data_source
Sheet 2 ENGAGEMENT_POLICY: issue, escalation_steps, voting_stance, reporting_requirement

TONE: Sovereign fund governance. Mandate language. Public accountability assumed for every figure.
```

### PROMPT 67 — The Geographic Diversification & Home Bias Analysis

```
CONTEXT: Regional weights for [PORTFOLIO] and the corresponding global market cap and GDP weights are in [FILE], as of [DATE]. Domestic holdings carry a statutory floor.

ROLE: Global portfolio strategist quantifying geographic diversification and home bias.

ACTION:
  1. Geographic diversification analysis for [PORTFOLIO]. Current geographic weights vs global market cap weights.

FORMAT: Geographic diversification table with home bias quantification and recommendation.

Workbook:
Sheet 1 GEO_WEIGHTS: region, current_wt, market_cap_wt, GDP_wt, active_position
Sheet 2 CORRELATION_MATRIX: region_pairs, 10yr_correlation, 3yr_correlation, change

TONE: Sovereign fund governance. Mandate language. Public accountability assumed for every figure.
```

### PROMPT 68 — The Long-Horizon Factor Allocation Framework

```
CONTEXT: Available: long-run factor return series and [SOVEREIGN FUND]'s current factor exposures ([FILE]). The fund has a multi-decade horizon and tolerates long stretches of factor underperformance.

ROLE: Long-horizon factor allocation specialist applying sovereign mandate design.

ACTION:
  1. Long-horizon factor allocation framework for [SOVEREIGN FUND].
  2. Factors: market, size, value, quality, low volatility, momentum.

FORMAT: Factor allocation framework with academic evidence and implementation guidance.

Workbook:
Sheet 1 FACTOR_ANALYSIS: factor, academic_premium, realised_premium, academic_source
Sheet 2 ALLOCATION_FRAMEWORK: factor, target_allocation, instrument, capacity_est

TONE: Sovereign fund governance. Mandate language. Public accountability assumed for every figure.
```

### PROMPT 69 — The CPPIB Total Portfolio Approach

```
CONTEXT: [INSTITUTION] currently runs an asset class budgeting model; the holdings and risk figures are in [FILE]. Total fund tracking error is capped at [X] basis points.

ROLE: Total portfolio approach specialist implementing the CPPIB framework.

ACTION:
  1. CPPIB Total Portfolio Approach implementation for [INSTITUTION].
  2. Reference portfolio: passive market cap-weighted equivalent.

FORMAT: Total Portfolio Approach framework with reference portfolio and active risk budget.

Workbook:
Sheet 1 REFERENCE_PORTFOLIO: asset_class, passive_weight, benchmark
Sheet 2 ACTIVE_RISK_BUDGET: strategy, tracking_error_allocated, current_TE, headroom

TONE: Sovereign fund governance. Mandate language. Public accountability assumed for every figure.
```

### PROMPT 70 — The Sovereign Credit & Fixed Income Allocation Protocol

```
CONTEXT: Yield curves, spreads and ratings for the eligible universe sit in [FILE], marked as of [DATE]. [FUND]'s policy sets a minimum average credit quality and a duration band.

ROLE: Fixed income strategist building sovereign credit and yield curve allocation.

ACTION:
  1. Sovereign credit and fixed income allocation for [FUND]. Universe: developed market sovereigns, EM sovereigns, IG credit.

FORMAT: Fixed income allocation with duration analysis and yield curve positioning.

Workbook:
Sheet 1 FIXED_INCOME_ALLOCATION: segment, target_wt, duration_contribution, yield
Sheet 2 YIELD_CURVE_POSITIONING: maturity, current_weight, target_weight, rationale

TONE: Sovereign fund governance. Mandate language. Public accountability assumed for every figure.
```

### PROMPT 71 — The Currency Overlay & FX Risk Management

```
CONTEXT: Attached: [PORTFOLIO] exposures by currency, including look-through on foreign revenue ([FILE]), plus forward points as of [DATE]. Base currency is [CUR] and hedging is centralised.

ROLE: Currency overlay specialist managing multi-currency exposure and hedging.

ACTION:
  1. Currency overlay framework for [PORTFOLIO]. Identify all currency exposures including indirect.

FORMAT: Currency overlay design with cost-benefit analysis per currency pair.

Workbook:
Sheet 1 CURRENCY_EXPOSURE: currency_pair, direct_pct, indirect_pct, total_exposure
Sheet 2 HEDGE_DECISION: pair, hedge_ratio, instrument, cost_bps, rationale

TONE: Sovereign fund governance. Mandate language. Public accountability assumed for every figure.
```

### PROMPT 72 — The Governance & Accountability Reporting System

```
CONTEXT: Current committee terms of reference and delegation limits for [SOVEREIGN INSTITUTION] are in [FILE]. Reporting is scrutinised publicly, and the framework has to survive that scrutiny.

ROLE: Governance officer designing accountability and transparency reporting.

ACTION:
  1. Governance and accountability reporting framework for [SOVEREIGN INSTITUTION]. Decision-making: investment committee structure, delegation authority, escalation path.

FORMAT: Governance framework with decision-making structure and reporting requirements.

Workbook:
Sheet 1 GOVERNANCE_STRUCTURE: decision_type, authority_level, escalation_path
Sheet 2 PERFORMANCE_ACCOUNTABILITY: KPI, measurement, frequency, consequence

TONE: Sovereign fund governance. Mandate language. Public accountability assumed for every figure.
```

## Chapter 11 — The ESG & Climate Desk

### PROMPT 73 — The TCFD Four-Pillar Climate Disclosure Framework

```
CONTEXT: Attached: [COMPANY]'s annual report, sustainability report and proxy statement ([FILE]), all for fiscal [DATE]. Disclosure quality varies by pillar and gaps matter as much as content.

ROLE: ESG analyst applying the TCFD four-pillar climate risk framework.

ACTION:
  1. TCFD four-pillar analysis for [COMPANY]. Pillar 1 Governance: board oversight, management roles, compensation links.

FORMAT: TCFD four-pillar disclosure table with scenario analysis and metrics.

Workbook:
Sheet 1 TCFD_PILLARS: pillar, disclosure_item, current_status, gap_to_best_practice
Sheet 2 SCENARIO_ANALYSIS: scenario, carbon_price, financial_impact_pct, timeline

TONE: ESG and climate. Distinguish disclosed data from modelled data. No greenwashing, no unstated proxies.
```

### PROMPT 74 — The EU SFDR Article Classification Protocol

```
CONTEXT: You have [FUND]'s prospectus, investment process description and current holdings in [FILE]. The classification is filed with the regulator, so an unsupported claim creates a disclosure liability.

ROLE: Regulatory compliance analyst determining SFDR Article classification.

ACTION:
  1. SFDR Article classification analysis for [FUND]. Determine whether the fund qualifies as Article 6 (no ESG integration), Article 8 (ESG characteristics), or Article 9 (ESG primary objective).

FORMAT: SFDR classification recommendation with evidence and disclosure obligations.

Workbook:
Sheet 1 SFDR_CLASSIFICATION: criterion, Article_6, Article_8, Article_9, current_fund
Sheet 2 EVIDENCE: classification, supporting_evidence, gaps, actions_required

TONE: ESG and climate. Distinguish disclosed data from modelled data. No greenwashing, no unstated proxies.
```

### PROMPT 75 — The Carbon Intensity & Net-Zero Pathway Analysis

```
CONTEXT: Holdings and reported emissions for [PORTFOLIO] are in [FILE], with revenue figures for intensity denominators. Coverage is incomplete; estimated data must be labelled as estimated.

ROLE: Climate investment specialist calculating WACI and net-zero pathway.

ACTION:
  1. Carbon intensity and net-zero pathway analysis for [PORTFOLIO].
  2. Calculate WACI (Weighted Average Carbon Intensity) for the portfolio.

FORMAT: WACI calculation with net-zero pathway and top contributor identification.

Workbook:
Sheet 1 WACI_CALCULATION: company, weight, scope_1_2_intensity, contribution_to_WACI
Sheet 2 PATHWAY_ANALYSIS: year, portfolio_WACI, paris_pathway, gap

TONE: ESG and climate. Distinguish disclosed data from modelled data. No greenwashing, no unstated proxies.
```

### PROMPT 76 — The Physical Climate Risk & Stranded Asset Assessment

```
CONTEXT: Available: [PORTFOLIO] holdings with facility locations where disclosed ([FILE]) and hazard maps by region. Many issuers report no asset-level detail, which itself is a finding.

ROLE: Physical risk analyst mapping asset-level climate hazard exposure.

ACTION:
  1. Physical climate risk assessment for [PORTFOLIO]. Asset locations: map each holding's key physical assets to climate hazard exposure.

FORMAT: Physical risk map with hazard exposure by asset and time horizon.

Workbook:
Sheet 1 PHYSICAL_RISK_MAP: company, asset_location, hazard_type, current, 2030, 2050
Sheet 2 STRANDED_ASSET_RISK: company, asset, stranding_scenario, book_value_at_risk

TONE: ESG and climate. Distinguish disclosed data from modelled data. No greenwashing, no unstated proxies.
```

### PROMPT 77 — The ESG Score Integration & Factor Analysis

```
CONTEXT: Scores from [PROVIDER] and matching return history for [PORTFOLIO] are supplied in [FILE]. Provider methodology changed during the sample, and coverage differs across small caps.

ROLE: ESG factor analyst integrating scores with financial attribution.

ACTION:
  1. ESG score integration for [PORTFOLIO]. Data source: [PROVIDER].

FORMAT: ESG score integration with factor analysis and engagement priorities.

Workbook:
Sheet 1 ESG_SCORES: company, E_score, S_score, G_score, composite, vs_sector
Sheet 2 FACTOR_ANALYSIS: ESG_decile, avg_return, Sharpe, correlation_with_alpha

TONE: ESG and climate. Distinguish disclosed data from modelled data. No greenwashing, no unstated proxies.
```

### PROMPT 78 — The Shareholder Engagement & Voting Policy Framework

```
CONTEXT: Attached: [INSTITUTION]'s prior voting record, engagement log and the current policy text ([FILE]). Votes are disclosed publicly, so each default stance needs a stated rationale.

ROLE: Responsible investment officer designing engagement and voting policy.

ACTION:
  1. Shareholder engagement and voting policy for [INSTITUTION].
  2. Priority engagement issues: climate, executive compensation, board composition, human rights.

FORMAT: Engagement policy with voting stances and escalation framework.

Workbook:
Sheet 1 ENGAGEMENT_ISSUES: issue, priority, stance, escalation_path
Sheet 2 VOTING_POLICY: resolution_type, default_stance, override_conditions

TONE: ESG and climate. Distinguish disclosed data from modelled data. No greenwashing, no unstated proxies.
```

### PROMPT 79 — The Impact Measurement & SDG Alignment Protocol

```
CONTEXT: Portfolio holdings and reported impact metrics for [FUND/PORTFOLIO] sit in [FILE], covering fiscal [DATE]. Most of the book is listed secondary market exposure, not primary capital.

ROLE: Impact measurement specialist aligning portfolio to UN SDG goals.

ACTION:
  1. Impact measurement framework for [FUND/PORTFOLIO]. Select 3-5 SDG goals most relevant to portfolio.

FORMAT: Impact measurement framework with SDG alignment and additionality assessment.

Workbook:
Sheet 1 SDG_ALIGNMENT: SDG, relevance, metric, measurement_method, data_source
Sheet 2 IMPACT_RESULTS: SDG, metric, current_year, baseline, change, attribution

TONE: ESG and climate. Distinguish disclosed data from modelled data. No greenwashing, no unstated proxies.
```

### PROMPT 80 — The Climate Scenario Analysis & Portfolio Stress Test

```
CONTEXT: Sector exposures for [PORTFOLIO] and the carbon price paths for each scenario are in [FILE]. The stress test is tabled at investment committee next to the risk report.

ROLE: Head of responsible investment, presenting the climate stress test and positioning recommendation to the investment committee.

ACTION:
  1. Climate scenario analysis and portfolio stress test for [PORTFOLIO]. Scenarios: Orderly transition (Net Zero 2050), Disorderly transition (Delayed action then sudden), Hot house world (No action, physical risk dominates).

FORMAT: Climate scenario portfolio stress test with sector analysis and positioning recommendation.

Workbook:
Sheet 1 SCENARIO_RESULTS: scenario, portfolio_return_impact, timeline
Sheet 2 SECTOR_ANALYSIS: sector, orderly, disorderly, hothouse, winner_or_loser

TONE: ESG and climate. Distinguish disclosed data from modelled data. No greenwashing, no unstated proxies.
```

## Chapter 12 — The Fixed Income & Credit Desk

### PROMPT 81 — The Institutional Credit Analysis & Scoring Framework

```
CONTEXT: Attached: [COMPANY]'s last five annual filings and the peer credit metrics file ([FILE]). Output feeds the quarterly credit review. Mandate floor: minimum [RATING] at purchase.

ROLE: Credit analyst applying institutional credit assessment and scorecard.

ACTION:
  1. Credit analysis for [COMPANY] using institutional framework.
  2. Scorecard: Net Debt/EBITDA, interest coverage, FCF/total debt, Altman Z-Score.

FORMAT: Credit scorecard with trend analysis and rating recommendation.

Workbook:
Sheet 1 CREDIT_SCORECARD: metric, actual, IG_threshold, assessment, 5yr_trend
Sheet 2 ALTMAN_Z: year, working_capital, retained_earnings, EBIT, equity, sales, Z_score

TONE: Credit analytical. Downside first. State recovery assumptions explicitly and label them assumptions.
```

### PROMPT 82 — The Duration & Convexity Risk Management

```
CONTEXT: You have the holdings file for [FIXED INCOME PORTFOLIO] ([FILE]) with position-level cash flows, plus the benchmark curve as of [DATE] close. Mandate duration band: [X] years.

ROLE: Fixed income portfolio manager managing duration and convexity risk.

ACTION:
  1. Duration and convexity analysis for [FIXED INCOME PORTFOLIO]. DV01 per position.

FORMAT: Duration profile with key rate durations and liability matching analysis.

Workbook:
Sheet 1 DURATION_PROFILE: position, maturity, modified_duration, DV01, weight
Sheet 2 KEY_RATE_DURATIONS: maturity_bucket, KRD, P&L_per_100bps

TONE: Credit analytical. Downside first. State recovery assumptions explicitly and label them assumptions.
```

### PROMPT 83 — The Credit Spread Attribution & Curve Analysis

```
CONTEXT: Position-level returns for [FIXED INCOME PORTFOLIO] over [PERIOD] are in [FILE], alongside duration-matched Treasury returns. The attribution goes into the monthly performance pack for the CIO.

ROLE: Credit attribution specialist decomposing spread return components.

ACTION:
  1. Credit spread attribution for [FIXED INCOME PORTFOLIO] over [PERIOD]. Total excess return vs duration-matched Treasuries.

FORMAT: Credit spread attribution by source, sector, and rating.

Workbook:
Sheet 1 ATTRIBUTION_SUMMARY: source, bps_contribution, pct_of_total
Sheet 2 SECTOR_ATTRIBUTION: sector, weight, spread_change, P&L_bps

TONE: Credit analytical. Downside first. State recovery assumptions explicitly and label them assumptions.
```

### PROMPT 84 — The Covenant Analysis & Distressed Credit Framework

```
CONTEXT: Attached: the indenture and credit agreement for [COMPANY/BOND ISSUE] ([FILE]) plus the last four quarters of reported financials. Covenant levels must tie to filings dated [DATE].

ROLE: Distressed credit analyst mapping covenant headroom and breach scenarios.

ACTION:
  1. Covenant analysis for [COMPANY/BOND ISSUE]. List all financial covenants: type (maintenance vs incurrence), metric, threshold, current level, headroom.

FORMAT: Covenant analysis with headroom calculation and breach scenario.

Workbook:
Sheet 1 COVENANT_TABLE: covenant, type, threshold, current, headroom, breach_risk
Sheet 2 BREACH_SCENARIOS: scenario, EBITDA_level, covenant_tripped, lender_remedy

TONE: Credit analytical. Downside first. State recovery assumptions explicitly and label them assumptions.
```

### PROMPT 85 — The LDI & Liability-Matching Portfolio Construction

```
CONTEXT: The actuarial liability schedule for [PENSION FUND/INSTITUTION] and the current asset holdings sit in [FILE], both valued at [DATE]. Output supports the trustee hedging discussion.

ROLE: Pension fund analyst applying liability-driven investing (LDI) framework.

ACTION:
  1. LDI liability matching analysis for [PENSION FUND/INSTITUTION].
  2. Liability profile: present value, duration, key rate exposures.

FORMAT: Liability matching analysis with duration gap and hedging instruments.

Workbook:
Sheet 1 LIABILITY_PROFILE: liability, PV, duration, KRD_2yr, KRD_10yr, KRD_30yr
Sheet 2 ASSET_LIABILITY_GAP: measure, liability, asset, gap, hedge_ratio

TONE: Credit analytical. Downside first. State recovery assumptions explicitly and label them assumptions.
```

### PROMPT 86 — The Fixed Income Portfolio Construction & Optimisation

```
CONTEXT: Working from the [MANDATE] investment guidelines ([FILE]) and the eligible bond universe with current spreads. Concentration caps and minimum quality are set by the guidelines, not by you.

ROLE: Fixed income portfolio construction specialist applying credit mandate rules.

ACTION:
  1. Fixed income portfolio construction for [MANDATE]. Credit quality minimum.

FORMAT: Fixed income portfolio blueprint with credit quality, duration, and concentration rules.

Workbook:
Sheet 1 PORTFOLIO_BLUEPRINT: sector, target_wt, min_quality, benchmark
Sheet 2 CONCENTRATION_LIMITS: dimension, limit, current_level, flag

TONE: Credit analytical. Downside first. State recovery assumptions explicitly and label them assumptions.
```

### PROMPT 87 — The Yield Curve Strategy & Positioning

```
CONTEXT: Curve levels for [CUR] government bonds as of [DATE] close are in [FILE], with the current portfolio positioning on tab two. Output goes to the investment committee.

ROLE: Managing Director on the rates desk at a large sell-side firm, recommending curve positioning to the investment committee.

ACTION:
  1. Yield curve strategy for [FIXED INCOME PORTFOLIO]. Current curve shape: flat/steep/inverted/humped.

FORMAT: Yield curve positioning strategy with carry analysis and instrument selection.

Workbook:
Sheet 1 CURVE_ANALYSIS: maturity, yield, real_yield, carry, roll_down
Sheet 2 POSITIONING_RECOMMENDATION: strategy, rationale, duration_impact, instruments

TONE: Credit analytical. Downside first. State recovery assumptions explicitly and label them assumptions.
```

### PROMPT 88 — The Credit Default Probability & Recovery Analysis

```
CONTEXT: Available for [ISSUER]: equity price history, balance sheet leverage, the CDS quote sheet ([FILE]), and capital structure seniority. All market inputs are as of [DATE] close.

ROLE: Credit risk analyst modelling default probability and recovery rates.

ACTION:
  1. Credit default probability and recovery analysis for [ISSUER].
  2. Default probability: Merton model (equity vol and leverage), market-implied (CDS spread / (1-Recovery)), rating agency historical default rates by rating.

FORMAT: Default probability with recovery analysis and expected loss calculation.

Workbook:
Sheet 1 DEFAULT_PROBABILITY: method, 1yr_PD, 5yr_PD, inputs
Sheet 2 RECOVERY_ANALYSIS: seniority, historical_recovery, current_assumption, range

TONE: Credit analytical. Downside first. State recovery assumptions explicitly and label them assumptions.
```

## Chapter 13 — Claude Model Family

### PROMPT 89 — Model Selection and Cost Optimisation

```
CONTEXT: You have the desk's weekly task inventory ([FILE]) with volumes per task type and current published per-token pricing. The routing rule goes to the desk meeting for sign-off.

ROLE: Institutional AI deployment specialist, covering Claude model selection and cost optimisation.

ACTION:
  1. Select the optimal Claude model for each task in your finance workflow. For bulk extraction (N>20 items): Haiku 4.5.

FORMAT: Model routing framework with cost analysis and team routing rules.

Workbook:
Sheet 1 TASK_ROUTING: task_type, right_model, cost_per_1k_tokens, quality_difference
Sheet 2 COST_ANALYSIS: task_volume, model_used, monthly_cost, vs_opus_cost, saving

TONE: Plain and technical. Describe model behaviour, not model marketing. Note that capabilities change.
```

### PROMPT 90 — The High-Speed Universe Screening & Data Extraction Framework

```
CONTEXT: Available: [N] filings for [UNIVERSE] sitting in a watched folder, plus the field schema already agreed with the research team. The run happens overnight, unattended.

ROLE: Research operations lead, designing Haiku bulk extraction pipelines.

ACTION:
  1. Design a Haiku 4.5 bulk screening pipeline. Input: [N] company annual reports or filings.

FORMAT: Bulk extraction pipeline design with quality validation and overnight scheduling.

Workbook:
Sheet 1 EXTRACTION_SCHEMA: metric_to_extract, location_in_doc, validation_rule
Sheet 2 EXTRACTION_RESULTS: company, metric_1, metric_2, confidence_flag

TONE: Plain and technical. Describe model behaviour, not model marketing. Note that capabilities change.
```

### PROMPT 91 — Output Standards Configuration

```
CONTEXT: Attached: the firm's compliance language policy ([FILE]) and ten sample outputs from live sessions. The configured standard applies to every analyst session, so ambiguity fails the test.

ROLE: Compliance and AI standards officer, configuring institutional output standards.

ACTION:
  1. Configure Sonnet 5 output standards for institutional finance use. System prompt elements: BCE-only language, assumption log required, risk caveats on forward-looking statements, compliance footer.

FORMAT: Configured output standard with compliance verification results.

Workbook:
Sheet 1 SYSTEM_PROMPT_ELEMENTS: element, purpose, example_clause
Sheet 2 COMPLIANCE_TEST: output_item, compliant, issue_found, fix_applied

TONE: Plain and technical. Describe model behaviour, not model marketing. Note that capabilities change.
```

### PROMPT 92 — The Extended Multi-Layer Reasoning Framework

```
CONTEXT: The research file on [COMPANY] ([FILE]) is loaded, with competing analyst views already noted. The memo goes to the investment committee, so the reasoning chain has to be auditable.

ROLE: Managing Director at a large sell-side firm, reviewing this Opus 4.8 extended-reasoning memo before it goes to the investment committee.

ACTION:
  1. Apply Opus 4.8 extended reasoning to a complex IC memo for [COMPANY]. Use extended thinking mode: the model shows its reasoning chain before the conclusion.

FORMAT: IC memo with extended reasoning chain and quality comparison vs Sonnet.

Workbook:
Sheet 1 IC_SUMMARY: thesis, scenarios, KPIs, position_size, exit_triggers
Sheet 2 REASONING_CHAIN: step, reasoning, assumption, confidence

TONE: Plain and technical. Describe model behaviour, not model marketing. Note that capabilities change.
```

### PROMPT 93 — The Claude Finance Agent Capability Assessment

```
CONTEXT: Five representative tasks from [SPECIFIC FINANCE WORKFLOW] are prepared in [FILE], each with a known correct answer. The assessment decides whether this workflow gets deployed to the team.

ROLE: AI workflow auditor, assessing Claude capability fit for finance use cases.

ACTION:
  1. Assess Claude's capability for [SPECIFIC FINANCE WORKFLOW]. Test cases: 5 representative tasks from this workflow.

FORMAT: Capability assessment scorecard with hit rate and workflow fit evaluation.

Workbook:
Sheet 1 TEST_CASES: task_description, input_summary, output_quality, edit_required
Sheet 2 HIT_RATE: task_category, n_tested, usable_pct, minor_edit_pct, major_edit_pct

TONE: Plain and technical. Describe model behaviour, not model marketing. Note that capabilities change.
```

### PROMPT 94 — The Institutional AI Cost Management & Budget Framework

```
CONTEXT: Available: [TEAM/INSTITUTION] usage logs for the last [PERIOD] and the approved annual technology budget. The framework goes to finance operations, so every figure must reconcile to stated inputs.

ROLE: Finance operations manager, building AI cost management and governance.

ACTION:
  1. Design an AI cost management framework for [TEAM/INSTITUTION]. Map all AI tasks by volume and complexity. Standing rule: after the budget model is built, write and run a Python script recomputing every derived figure (monthly costs, savings, volume totals) from stated inputs; print PASS/FAIL per check; correct and rerun until all pass.

FORMAT: AI cost management framework with budget model and governance rules.

Workbook:
Sheet 1 TASK_INVENTORY: task, monthly_volume, complexity, current_model, optimal_model
Sheet 2 BUDGET_MODEL: model, volume, cost_per_unit, monthly_cost, vs_optimised

TONE: Plain and technical. Describe model behaviour, not model marketing. Note that capabilities change.
```

### PROMPT 95 — Multi-Model Pipeline Architecture

```
CONTEXT: Current manual steps for [FINANCE WORKFLOW] are documented in [FILE], with per-step volumes and turnaround times. Nothing leaves the pipeline without a named human approver.

ROLE: AI infrastructure architect, designing multi-model pipeline for finance teams.

ACTION:
  1. Design a multi-model pipeline for [FINANCE WORKFLOW]. Stage 1 (Haiku): extraction and classification.

FORMAT: Multi-model pipeline architecture with data flow and quality gates.

Workbook:
Sheet 1 PIPELINE_STAGES: stage, model, input, output, quality_gate
Sheet 2 DATA_FLOW: stage_from, stage_to, data_format, validation_rule

TONE: Plain and technical. Describe model behaviour, not model marketing. Note that capabilities change.
```

### PROMPT 96 — The Norway GPFG AI-at-Scale Institutional Deployment Framework

```
CONTEXT: Scope: [INSTITUTION] holds [N] portfolio companies, and the overnight screening window is fixed. Governance policy requires a named owner and an audit trail for every automated stage.

ROLE: Institutional AI deployment lead, NBIM-inspired at-scale model architecture.

ACTION:
  1. Design an AI-at-scale institutional deployment for [INSTITUTION] covering [N] portfolio companies. Three-stage architecture: Haiku for overnight bulk, Sonnet for escalation reports, Opus for complex analysis. Standing rule: write and run a Python script recomputing every cost figure (per-stage totals, saving versus single-model routing) from stated inputs; print PASS/FAIL per check; correct and rerun until all pass.

FORMAT: AI deployment architecture with governance, cost model, and efficiency analysis.

Workbook:
Sheet 1 DEPLOYMENT_ARCHITECTURE: stage, model, input_volume, output, time_required
Sheet 2 COST_MODEL: stage, model, volume_per_qtr, cost_per_qtr, total_annual

TONE: Plain and technical. Describe model behaviour, not model marketing. Note that capabilities change.
```

## Chapter 14 — Claude.ai Platform

### PROMPT 97 — The Institutional Claude Project Configuration Framework

```
CONTEXT: The Project is empty apart from [FUND]'s mandate document, the benchmark definition, and the firm's compliance language policy ([FILE]). Every later session inherits what you write here.

ROLE: Research team lead — configuring Claude Projects for coverage universe.

ACTION:
  1. Configure a Claude Project for [YOUR COVERAGE UNIVERSE / FUND].
  2. System prompt: fund mandate, benchmark, investment philosophy, BCE-only language rule, output format preferences, compliance footer.

FORMAT: Project configuration with system prompt and verification test results.

Workbook:
Sheet 1 SYSTEM_PROMPT_DESIGN: element, content, purpose, example_output
Sheet 2 VERIFICATION_TESTS: query, expected_behaviour, actual_output, pass_fail

TONE: Practical and platform-neutral. Describe what the interface does today and say when a step may differ.
```

### PROMPT 98 — The Claude Deep Research Sector Initiation Framework

```
CONTEXT: No internal coverage of [SECTOR] exists yet. Web research is available; no proprietary documents are uploaded. Output starts the initiation file, so every claim needs a dated source.

ROLE: Senior analyst — using Deep Research for sector initiation.

ACTION:
  1. Use Claude Deep Research for a sector initiation on [SECTOR].
  2. Query: summarise the competitive landscape, key players, growth drivers, and main risks for this sector.

FORMAT: Sector initiation research output with source verification and gap analysis.

Workbook:
Sheet 1 RESEARCH_SUMMARY: topic, finding, source, confidence
Sheet 2 SOURCE_VERIFICATION: source, type, credibility, date

TONE: Practical and platform-neutral. Describe what the interface does today and say when a step may differ.
```

### PROMPT 99 — The Multi-Quarter Transcript Intelligence Framework

```
CONTEXT: [N] consecutive earnings transcripts for [COMPANY] are uploaded to the Project, together with the reported results for each of those quarters. Nothing outside those files is available.

ROLE: Equity analyst — multi-quarter transcript intelligence in a Project.

ACTION:
  1. Load [N] earnings call transcripts for [COMPANY] into a Project.
  2. Query: build a management credibility scorecard. Did management's language in each quarter predict the subsequent quarter's results?
  3. Track specific language shifts vs subsequent guidance changes.

FORMAT: Multi-quarter transcript intelligence with management credibility scorecard.

Workbook:
Sheet 1 TRANSCRIPT_ANALYSIS: quarter, tone_rating, key_language_shifts
Sheet 2 CREDIBILITY_SCORECARD: quarter, language_signal, next_qtr_outcome, correct_prediction

TONE: Practical and platform-neutral. Describe what the interface does today and say when a step may differ.
```

### PROMPT 100 — The Automated Prior Period vs Current Period Document Analysis

```
CONTEXT: Two annual reports for [COMPANY], FY[X] and FY[Y], are the only documents in the Project. Findings feed a thesis review, so each change needs a section reference.

ROLE: Research analyst — automated prior vs current period document comparison.

ACTION:
  1. Upload [COMPANY]'s FY[X] and FY[Y] annual reports into a Project.
  2. Query: what changed between the two years? Focus on: risk factor additions/removals, business description changes, forward-looking language shifts.

FORMAT: Prior period vs current period document comparison with financial significance flags.

Workbook:
Sheet 1 CHANGE_LOG: section, FY_prior_summary, FY_current_summary, change_type
Sheet 2 RISK_FACTOR_CHANGES: risk, status (new/removed/modified), significance

TONE: Practical and platform-neutral. Describe what the interface does today and say when a step may differ.
```

### PROMPT 101 — The Full Sector Initiation & Coverage Launch Framework

```
CONTEXT: Uploaded to the Project: annual reports, recent transcripts, and industry primers for [N] companies in [SECTOR]. The pack is signed off before coverage launches, so figures must reconcile.

ROLE: Managing Director at a large sell-side firm — signing off the sector initiation before coverage launches.

ACTION:
  1. Launch full coverage on [SECTOR] using a Project with all available annual reports, recent earnings transcripts, and industry primers uploaded. Build: competitive landscape, financial comparison across [N] companies, sector risks, and a ranking of companies by investment attractiveness. Standing rule: after the financial comparison is built, write and run a Python script recomputing every derived figure (margins, medians, ranking inputs) from stated inputs; print PASS/FAIL per check; correct and rerun until all pass.

FORMAT: Full sector coverage launch pack with competitive analysis and company ranking.

Workbook:
Sheet 1 COVERAGE_UNIVERSE: company, market_cap, revenue, EBITDA_margin, moat_rating
Sheet 2 FINANCIAL_COMPARISON: metric, company_1, company_2, company_3, sector_median

TONE: Practical and platform-neutral. Describe what the interface does today and say when a step may differ.
```

### PROMPT 102 — The Long-Running Project Context Optimisation

```
CONTEXT: An existing Project has run for [PERIOD]. Available: its current system prompt, the uploaded document list ([FILE]), and session query history. Storage and context budget are finite.

ROLE: AI workflow optimiser — auditing and improving Project context configuration.

ACTION:
  1. Audit the context configuration of an existing Project. What is in the system prompt? What documents are loaded? Is context being used efficiently? Are any documents rarely queried? Propose optimisations: what to add, remove, or restructure to make each session more productive.

FORMAT: Project context audit with optimisation recommendations.

Workbook:
Sheet 1 CONTEXT_AUDIT: element, current_state, utilisation_assessment, recommendation
Sheet 2 DOCUMENT_USAGE: document, last_queried, query_frequency, keep_or_remove

TONE: Practical and platform-neutral. Describe what the interface does today and say when a step may differ.
```

### PROMPT 103 — The Real-Time Portfolio Event & Signal Monitoring

```
CONTEXT: The Project holds the coverage universe list ([FILE]) with position sizes and thesis notes per name. A daily feed of filings, news, and price moves arrives each morning.

ROLE: Portfolio monitoring lead — real-time event and signal monitoring workflow.

ACTION:
  1. Configure a real-time portfolio monitoring workflow in a Project.
  2. Daily trigger: new filings, news, or price moves for coverage universe.

FORMAT: Portfolio monitoring workflow with materiality filter and PM alert template.

Workbook:
Sheet 1 MONITORING_UNIVERSE: company, watch_categories, threshold_for_material
Sheet 2 EVENT_LOG: date, company, event_type, materiality, thesis_impact, action

TONE: Practical and platform-neutral. Describe what the interface does today and say when a step may differ.
```

### PROMPT 104 — The Multi-Source Intelligence Aggregation & Synthesis

```
CONTEXT: Loaded into the Project: [COMPANY]'s latest 10-K, the last four earnings transcripts, and three external research notes. Sources disagree in places, and the disagreement itself is the finding.

ROLE: Research synthesis specialist — multi-source intelligence aggregation.

ACTION:
  1. Multi-source synthesis task: load [COMPANY]'s 10-K, last 4 earnings transcripts, and 3 recent sell-side research notes into a Project. Query: synthesise the bull and bear case from all sources.

FORMAT: Multi-source synthesis with agreement/disagreement analysis and coverage gaps.

Workbook:
Sheet 1 BULL_CASE: argument, source, strength_of_evidence
Sheet 2 BEAR_CASE: argument, source, strength_of_evidence

TONE: Practical and platform-neutral. Describe what the interface does today and say when a step may differ.
```

## Chapter 15 — Claude Code for Quant Finance

### PROMPT 105 — The Institutional Monte Carlo Portfolio VaR Implementation

```
CONTEXT: The repo holds position-level holdings for [PORTFOLIO] and a daily return history covering [DATE RANGE]. CLAUDE.md already carries the standing validation rule. Python environment is set up.

ROLE: Quantitative risk engineer — specifying and reviewing Monte Carlo VaR in Python.

ACTION:
  1. Ask Claude Code to write a complete Monte Carlo VaR engine in Python. Specification: 10,000 simulations, 252-day horizon, Student-t distribution (dof=5), Cholesky decomposition for correlations, 2022 stress scenario (equity-bond correlation = +0.60). Validation lives in the repo's CLAUDE.md standing rule: every derived figure (VaR, CVaR, drawdowns) recomputed by a Python script from stated inputs, PASS/FAIL per check.

FORMAT: Claude Code writes complete Python. Review: validate Student-t distribution choice, Cholesky inputs, stress scenario calibration. Run unit tests before use in production.

Workbook:
Sheet 1 VAR_RESULTS: scenario, VaR_95, VaR_99, CVaR_95, max_drawdown
Sheet 2 SCENARIO_COMPARISON: normal_market, 2022_stress, difference

TONE: Engineering register. Report failures as failures. Paper results labelled paper.
```

### PROMPT 106 — The Python DCF Model

```
CONTEXT: Working in a repo where [COMPANY]'s segment revenue history and the WACC input sheet ([FILE]) already sit. Output has to export to Excel for the modelling team to check.

ROLE: Financial modeller — specifying and validating DCF automation in Python.

ACTION:
  1. Ask Claude Code to build a complete Python DCF model for [COMPANY]. Specification: 5-year revenue projections by segment, WACC calculation with sourced inputs, terminal value via two methods (Gordon Growth + exit multiple), 3x3 sensitivity table (WACC x TGR), formatted Excel export. The repo's CLAUDE.md standing rule applies: every derived figure (WACC, terminal value, per-share bridge) recomputed by script, PASS/FAIL per check.

FORMAT: Claude Code builds the DCF scaffolding. Analyst verifies: revenue growth assumptions, WACC inputs, terminal value methodology, sensitivity table logic.

Workbook:
Sheet 1 DCF_MODEL: revenue_5yr, EBIT, FCF, terminal_value, enterprise_value
Sheet 2 WACC_INPUTS: RF_rate, ERP, beta, Ke, Kd, WACC (all sourced)

TONE: Engineering register. Report failures as failures. Paper results labelled paper.
```

### PROMPT 107 — The Options Pricing & Greeks Calculator Framework

```
CONTEXT: Available in the repo: a position file of European options with strikes, expiries, and market prices, plus the current risk-free curve. No pricing library is installed.

ROLE: Derivatives quant — specifying and reviewing Black-Scholes options pricer.

ACTION:
  1. Ask Claude Code to build a Black-Scholes options pricer in Python.
  2. Specification: European call and put pricing, all five Greeks (Delta, Gamma, Theta, Vega, Rho), implied volatility solver (Newton-Raphson), portfolio Greeks aggregation across multiple positions.

FORMAT: Claude Code implements the pricer. Analyst verifies: Black-Scholes assumptions match market conventions, IV solver convergence, Greeks calculation against textbook solutions.

Workbook:
Sheet 1 OPTION_PRICER: option, S, K, T, r, sigma, price, Delta, Gamma, Theta
Sheet 2 IV_SOLVER: option, market_price, implied_vol, iterations_to_converge

TONE: Engineering register. Report failures as failures. Paper results labelled paper.
```

### PROMPT 108 — The Fama-French Multi-Factor Model

```
CONTEXT: The repo contains monthly portfolio returns for [DATE RANGE] and a downloaded factor file with Mkt-RF, SMB, HML, and MOM columns. Factor definitions must match the source documentation.

ROLE: Factor model specialist — specifying and validating Fama-French implementation.

ACTION:
  1. Ask Claude Code to implement the Carhart four-factor model in Python (Fama-French three factors plus momentum). Specification: regress portfolio returns on Mkt-RF, SMB, HML and MOM.

FORMAT: Claude Code runs the regression. Analyst verifies: data period and source, factor definitions match Fama-French documentation, alpha is statistically meaningful.

Workbook:
Sheet 1 FACTOR_REGRESSION: factor, loading, t_stat, p_value, R_squared
Sheet 2 ROLLING_BETAS: date, market_beta, SMB_beta, HML_beta, rolling_alpha

TONE: Engineering register. Report failures as failures. Paper results labelled paper.
```

### PROMPT 109 — The Institutional Investment Strategy Backtesting Engine

```
CONTEXT: Price and fundamental history for [UNIVERSE] sits in the repo as dated CSVs. Results feed a strategy review, so the walk-forward split has to be fixed before any run.

ROLE: Quantitative strategist — specifying and reviewing backtesting engine.

ACTION:
  1. Ask Claude Code to build an investment strategy backtesting engine in Python. Specification: signal generation from [DESCRIBE], position sizing (equal weight or [RULE]), transaction costs ([X]bps per trade), performance metrics (annualised return, Sharpe, Sortino, max drawdown, turnover, hit rate).

FORMAT: Claude Code builds the engine. Analyst verifies: no look-ahead bias in signal calculation, transaction costs realistic, walk-forward split discipline enforced.

Workbook:
Sheet 1 BACKTEST_RESULTS: period, ann_return, Sharpe, Sortino, max_DD, turnover
Sheet 2 WALK_FORWARD: in_sample_Sharpe, out_sample_Sharpe, degradation

TONE: Engineering register. Report failures as failures. Paper results labelled paper.
```

### PROMPT 110 — The Python Portfolio Risk Attribution & Decomposition

```
CONTEXT: You have current portfolio weights, the benchmark weights, and a factor covariance matrix dated [DATE] in the repo. Existing risk code is in the same package and must not break.

ROLE: Risk attribution engineer — specifying and validating portfolio risk decomposition.

ACTION:
  1. Ask Claude Code to build a portfolio risk attribution tool in Python. Specification: Marginal Contribution to Risk (MCTR) per position, systematic vs idiosyncratic decomposition using a factor model, concentration flags (top 5 positions % of total risk), tracking error vs benchmark.

FORMAT: Claude Code builds the attribution tool. Analyst verifies: factor model covariance matrix is current, MCTR calculation matches analytical formula, results sum to total portfolio risk.

Workbook:
Sheet 1 RISK_ATTRIBUTION: position, weight, MCTR, systematic_risk, idiosyncratic_risk
Sheet 2 CONCENTRATION_ANALYSIS: top_5_names, risk_contribution_pct, concentration_flag

TONE: Engineering register. Report failures as failures. Paper results labelled paper.
```

### PROMPT 111 — The Institutional Performance Analytics & Attribution

```
CONTEXT: Available: dated cash flows, valuations, and sector weights for [PORTFOLIO] and its benchmark. The output supports a composite report, so methodology choices have to be documented in code.

ROLE: Performance analytics engineer — specifying GIPS-compatible performance suite.

ACTION:
  1. Ask Claude Code to build a GIPS-compatible performance analytics suite in Python. Specification: time-weighted return (TWR) calculation, money-weighted return (MWR/IRR), Brinson-Hood-Beebower (BHB) attribution (allocation + selection + interaction effects), formatted report output.

FORMAT: Claude Code builds the analytics suite. Analyst verifies: TWR methodology matches GIPS requirements, BHB attribution sums correctly to active return, data inputs are clean.

Workbook:
Sheet 1 PERFORMANCE_RETURNS: period, TWR, MWR, benchmark, active_return
Sheet 2 BHB_ATTRIBUTION: sector, allocation_effect, selection_effect, interaction, total

TONE: Engineering register. Report failures as failures. Paper results labelled paper.
```

### PROMPT 112 — The Financial Data Extraction & Processing Pipeline

```
CONTEXT: Raw files arrive in [DATA SOURCE FORMAT] with inconsistent headers and missing rows. Downstream models in the same repo read the cleaned output, so schema changes break them.

ROLE: Data engineering lead — specifying financial data ingestion pipeline.

ACTION:
  1. Ask Claude Code to build a financial data ingestion and processing pipeline in Python. Specification: ingest [DATA SOURCE FORMAT: CSV/Excel/JSON/API], validate schema, handle missing data, calculate derived metrics ([LIST]), export to structured Excel.

FORMAT: Claude Code builds the pipeline. Analyst verifies: data validation catches real errors, derived metrics match manual calculations on sample rows, Excel output is formatted correctly.

Workbook:
Sheet 1 INGESTION_LOG: file, rows_loaded, rows_failed, validation_errors
Sheet 2 PROCESSED_DATA: company, metric_1, metric_2, derived_metric, quality_flag

TONE: Engineering register. Report failures as failures. Paper results labelled paper.
```

### PROMPT 113 — The Scheduled Weekly Run and Its Self-Checking Loop

```
CONTEXT: The Monday risk refresh runs the same steps every week. The repo already holds the inputs and CLAUDE.md carries the standing validation rule. No analyst is present at run time.

ROLE: Quantitative analyst specifying a recurring unattended job. You own the failure modes, not only the path where everything works.

ACTION:
  1. Turn the standing weekly task [TASK NAME] into a scheduled job that runs at [DAY/TIME] with no analyst present. Standing rule: after any multi-step numerical work, write and run a Python script recomputing every derived figure from stated inputs; print PASS/FAIL per check; correct and rerun until all pass.
  2. Write the run as a loop that ends on its own verdict: refresh inputs, recompute, validate, write output, stop. Each pass finishes on the validation result, not on the output file.
  3. Name the halt conditions explicitly: a failed validation check, an input file older than [N] days, a row count outside [RANGE], or an unhandled exception. On any halt, write the reason to the run log and send nothing onward.
  4. Separate what the job may do alone from what needs a person. It may refresh, recompute and file. It may not overwrite the prior week's output, change a parameter, or distribute anything to a reader.
  5. Log every run: timestamp, each input and its vintage, checks passed, checks failed, output path, and the halt reason where one applies.
  6. Run it first as a dry run against last week's inputs and reconcile every figure to what was already published.

FORMAT: Scheduled job with its validation loop, halt conditions and run log. Analyst verifies the dry run reproduces last week's published figures before the schedule is switched on.

Workbook:
Sheet 1 RUN_LOG: run_timestamp, input_file, input_vintage, checks_passed, checks_failed, halt_reason
Sheet 2 DRY_RUN_RECON: figure, published_value, recomputed_value, difference, status

TONE: Engineering register. Report failures as failures. Paper results labelled paper.
```

## Chapter 16 — Claude Cowork, Plugins & MCP

### PROMPT 114 — The Cowork Earnings Flash Note

```
CONTEXT: A watched folder receives filing PDFs for [N] covered names during reporting season. Consensus estimates are available in [FILE]. Nothing reaches distribution without the analyst approving the draft.

ROLE: Research operations, configuring the Cowork earnings flash pipeline.

ACTION:
  1. Configure a Cowork earnings flash note pipeline. Trigger: new PDF in /Earnings_Releases/ folder.

FORMAT: Earnings flash pipeline configuration with timing log and PM approval gate.

Workbook:
Sheet 1 PIPELINE_CONFIG: step, model, input, output, time_target
Sheet 2 FLASH_NOTE_TEMPLATE: section, content_rule, compliance_requirement

TONE: Operational. Name what is automated and what still needs a person. No claims about vendor relationships.
```

### PROMPT 115 — The Real-Time News Classification & Alert System

```
CONTEXT: A news feed covering [UNIVERSE] runs continuously, and the thesis notes for each holding sit in the Project. Most items are noise; the alert path is for material ones.

ROLE: Research operations, configuring the news classification and monitoring pipeline.

ACTION:
  1. Configure a Cowork news classification pipeline. Trigger: scheduled run every [N] hours.

FORMAT: News classification pipeline with materiality filter and PM alert protocol.

Workbook:
Sheet 1 NEWS_LOG: date, company, headline, classification, thesis_impact, urgency
Sheet 2 MATERIAL_ALERTS: company, summary, thesis_impact, draft_pm_alert

TONE: Operational. Name what is automated and what still needs a person. No claims about vendor relationships.
```

### PROMPT 116 — The Automated Portfolio Risk Limit Breach Detection

```
CONTEXT: Overnight position files and the mandate limit table ([FILE]) are available each morning before open. The project CLAUDE.md carries the recompute-before-alert rule. Alerts go to the CIO directly.

ROLE: Risk operations, configuring automated portfolio risk limit monitoring.

ACTION:
  1. Configure a Cowork daily risk limit monitoring pipeline. Trigger: daily at market open. Validation lives in the project CLAUDE.md standing rule: every dashboard figure recomputed by a Python script from position data, PASS/FAIL per check, before any alert is sent.

FORMAT: Risk limit monitoring pipeline with breach detection and CIO alert template.

Workbook:
Sheet 1 RISK_DASHBOARD: dimension, current, limit, breach_flag, magnitude
Sheet 2 BREACH_LOG: date, dimension, magnitude, corrective_trade, urgency

TONE: Operational. Name what is automated and what still needs a person. No claims about vendor relationships.
```

### PROMPT 117 — Claude's Five Finance Plugins: Selection and Configuration

```
CONTEXT: All five finance plugins are installed and none is active. [YOUR TASK] is defined in [FILE], with the deliverable format the receiving desk expects already specified.

ROLE: Finance analyst, selecting and configuring the right Claude finance plugin.

ACTION:
  1. Select the appropriate Claude finance plugin for [YOUR TASK]. Five options: Financial Analysis (DuPont, Altman Z, ratios), Investment Banking (LBO, accretion/dilution), Equity Research (research note format, sector KPIs), Private Equity (IC memo, IRR/MOIC), Wealth Management (IPS, RRTTLLU, client letters).

FORMAT: Plugin selection rationale and verification that domain conventions are applied.

Workbook:
Sheet 1 PLUGIN_SELECTION: task, selected_plugin, rationale, domain_conventions_applied
Sheet 2 OUTPUT_VERIFICATION: expected_convention, present_in_output, pass_fail

TONE: Operational. Name what is automated and what still needs a person. No claims about vendor relationships.
```

### PROMPT 118 — HNI Client Advisory Using Claude Wealth Management

```
CONTEXT: Client facts for [CLIENT] are captured in the onboarding file ([FILE]): age, risk profile, assets, horizon, and tax jurisdiction. Compliance reviews the letter before the client sees it.

ROLE: Senior wealth advisor, reviewing the plugin-generated HNI package before it goes to the client and compliance.

ACTION:
  1. Use the Claude Wealth Management Plugin for a complete HNI client advisory package. Client: [AGE], [RISK PROFILE], [AUM], [TIME HORIZON], [TAX JURISDICTION].

FORMAT: Complete HNI advisory package: RRTTLLU assessment, IPS draft, and compliant client letter.

Workbook:
Sheet 1 RRTTLLU_MATRIX: factor, constraint, rationale, IPS_clause
Sheet 2 SAA_TABLE: asset_class, target_wt, range, benchmark, rebalancing_trigger

TONE: Operational. Name what is automated and what still needs a person. No claims about vendor relationships.
```

### PROMPT 119 — The FactSet / LSEG / PitchBook Live Data Integration Framework

```
CONTEXT: Three MCP data connectors are authorised on this workspace. [SPECIFIC USE CASE] currently runs on manual exports. Refresh frequency and field mapping are not defined yet.

ROLE: Data infrastructure lead, configuring MCP live data connectors.

ACTION:
  1. Configure a FactSet/LSEG/PitchBook MCP connector for [SPECIFIC USE CASE]. Define the data elements needed, which connector provides them, refresh frequency, and how data flows into Claude's analytical output.

FORMAT: MCP connector configuration with data flow design and live test results.

Workbook:
Sheet 1 DATA_MAP: data_element, mcp_connector, field_name, refresh_frequency
Sheet 2 WORKFLOW_STEPS: step, data_source, claude_action, output

TONE: Operational. Name what is automated and what still needs a person. No claims about vendor relationships.
```

### PROMPT 120 — The Investment Committee Presentation Preparation Pipeline

```
CONTEXT: Current portfolio weights and the prior week's IC deck are both in the shared folder. The weekly run happens the night before the meeting, and the PM reviews everything.

ROLE: Research team lead, automating IC deck preparation via Cowork.

ACTION:
  1. Automate IC deck preparation using a Cowork weekly workflow. Step 1 (Haiku): pull current portfolio weights, compare to last IC, then calculate all position changes.

FORMAT: IC deck automation pipeline with position change analysis and PM review gate.

Workbook:
Sheet 1 POSITION_CHANGES: ticker, prior_weight, current_weight, delta, rationale
Sheet 2 BCE_UPDATES: ticker, prior_BCE, current_BCE, delta, driver

TONE: Operational. Name what is automated and what still needs a person. No claims about vendor relationships.
```

### PROMPT 121 — The Automated Client Communication & Quarterly Letter System

```
CONTEXT: Quarter-end holdings, cash flows, and benchmark returns for [CLIENT] are available in [FILE]. The project CLAUDE.md requires every performance figure recomputed and passing before compliance sees the draft.

ROLE: Client relations manager, automating the quarterly client communication pipeline.

ACTION:
  1. Build an automated quarterly client communication pipeline. Step 1 (Haiku): pull quarterly performance data, calculate TWR, benchmark, active return, top 3 contributors and detractors. The project CLAUDE.md standing rule applies: every performance figure recomputed by a Python script from holdings data, PASS/FAIL per check, before the draft reaches compliance.

FORMAT: Quarterly client letter pipeline with performance calculation and compliance check.

Workbook:
Sheet 1 PERFORMANCE_SUMMARY: metric, fund, benchmark, active, vs_target
Sheet 2 CONTRIBUTORS: name, contribution_bps, direction, one_line_commentary

TONE: Operational. Name what is automated and what still needs a person. No claims about vendor relationships.
```

### PROMPT 122 — The Connector Audit: What Is Reachable, What Is Missing, What Is Stale

```
CONTEXT: This workspace has accumulated connectors, watched folders and plugins over [PERIOD]. Nobody has checked what each one still reaches. Several pipelines depend on them without saying so.

ROLE: Operations lead auditing the data plumbing behind the desk's automated work. Report what is true today, not what was configured.

ACTION:
  1. Audit every connector, watched folder and plugin authorised on this workspace. For each one: what it reaches, which pipeline depends on it, when it last returned data, and who owns it.
  2. Test reachability rather than reading configuration. Request one known field from each source and record what came back, including an empty result.
  3. Classify each source: LIVE (returned current data), STALE (returned data older than [N] days), BROKEN (no response or an authorisation error), or UNUSED (authorised, no pipeline depends on it).
  4. List what is missing: every field a pipeline needs that no authorised source supplies, and the manual step currently filling the gap.
  5. For every STALE or BROKEN source, state which downstream output silently degrades and whether that output would still look correct to its reader.
  6. Recommend removals. An UNUSED connector is standing access nobody is watching, and it is a governance finding whether or not it is a technical one.

FORMAT: Connector inventory with a live test result per source, the dependency map, the missing-field list, and the removals recommended.

Workbook:
Sheet 1 CONNECTOR_INVENTORY: source, fields_reached, test_result, last_data_date, status, owner
Sheet 2 DEPENDENCY_MAP: pipeline, source, field_used, degrades_silently_yes_no
Sheet 3 GAPS: pipeline, missing_field, manual_workaround, owner

TONE: Operational. Name what is automated and what still needs a person. No claims about vendor relationships.
```

---

The prompts are the smallest part of the book. The finance context behind each one, why a layer is written the way it is, what the output looks like when it is right, and where it goes wrong are in the chapters, not on this page. Everything here is illustrative. Validate every figure before it reaches a live workflow. Nothing on this page is investment advice.

