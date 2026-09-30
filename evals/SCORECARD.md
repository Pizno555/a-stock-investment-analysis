# Project → Skill Parity Scorecard｜16维｜rc2

Reference Baseline：`华尔街股票研究分析师 Project v1.1.0 Frozen`。

评分仅用于定位差异；**Release Gate 不看平均分**。任一关键维度明确低于 Frozen Project Baseline 即 NO-GO。

评分定义：5=极强/历史Best级；4=强，允许P2但不影响一阶决策；3=可用但明显弱于强基线；2=存在结构性缺陷；1=缺失/反向。

| # | 维度 | Frozen Project v1.1.0 | rc1实测 | rc2目标/静态状态 |
|---|---|---:|---|---|
| 1 | Discovery Recall | 5 | P2波动 | Ref01冻结；不得因本轮修估值而改变 |
| 2 | Claim Decomposition | 5 | PASS | Ref01原字节冻结 |
| 3 | Provenance / Independence | 4 | PASS / P2 recall watch | Ref01原字节冻结 |
| 4 | Claim Adjudication / Precision | 5 | PASS | Ref01原字节冻结 |
| 5 | Temporal Validity / Freshness | 5 | PASS | Ref01 + SKILL硬规则保留 |
| 6 | Counterevidence | 5 | PASS | 冻结 |
| 7 | Earnings Realization Chain | 5 | PASS | Ref01/02冻结；Ref03只接续Forward建模 |
| 8 | Business / Industry / Moat | 5 | PASS | Ref02原字节冻结 |
| 9 | Financial Analysis | 5 | PASS | Ref02原字节冻结 |
| 10 | Forecast / Scenario | 5 | **低于Baseline：跨Run漂移** | Ref03主修目标，PBT必须恢复≥5 |
| 11 | Peer / Valuation | 5 | **低于Baseline：参数漂移** | Ref03主修目标，PBT必须恢复≥5 |
| 12 | Consensus / Price-in | 5 | 定性PASS，方法偏薄 | Ref03强化；不得低于Baseline |
| 13 | Bull-Bear / Risk / Invalidation | 5 | PASS | Ref02冻结；Ref03不得削弱 |
| 14 | Investment Judgment / Research-to-Action | 5 | 受Forecast/Valuation漂移影响 | 修上游后必须恢复一阶语义稳定 |
| 15 | Output Efficiency / Search Cost | 4 | PASS | 新Reference不得造成系统性膨胀 |
| 16 | Stability / Auditability / Compatibility | 4 | Forecast/Valuation不足 | rc2目标：方法和关键假设可追溯 |

## rc2硬门

- Reference 01 / 02 字节变化：FAIL。
- 通过固定盈利/倍数或固定公司答案换稳定性：P1 / NO-GO。
- Forecast / Valuation / Price-in / Investment Judgment 仍明确低于 Project：P1 / NO-GO。
- Evidence-Auditor regression：P1 / NO-GO。
- 新增运行时外部 Skill 依赖：P1 / NO-GO。
- Runtime Python 成为研究判断的必要依赖：P1 / NO-GO（本版不允许）。
- Search / Output 因 Ref03 出现系统性无意义膨胀：P1 / NO-GO。
- Base 发生足以改变动作的明显变化却没有可追溯假设变化：P1 / NO-GO。
