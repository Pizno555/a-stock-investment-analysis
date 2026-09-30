# a-stock-investment-analysis v1.0.0-rc2｜Production Blind Test Runbook

## 目标

验证 rc2 是否在保持 Frozen Project v1.1.0 既有能力不退化的前提下，修复 rc1 已重复出现的 Forecast / Valuation 稳定性回归。

## 被测对象

只安装/启用：`a-stock-investment-analysis-v1.0.0-rc2.zip`。

第一阶段不要安装或调用 `a-stock-evidence-research`，继续验证本 Skill 自包含。

## Fresh Runtime 控制

- 每题使用全新独立对话/线程；
- 不提供华尔街 Project Instructions；
- 不上传 Project Sources；
- 不提供 rc1 失败原因、03设计意图、历史答案或预期结论；
- Memory / 项目上下文尽量关闭或隔离；
- 工具权限、模型与思考档位在各次运行保持一致；
- 统一使用 `cases.jsonl` 中题目自己的 2026-09-13 11:00 北京时间截止；
- 保存完整输出；如环境可见，保存搜索/工具/Reference读取 telemetry。

## 固定回归集

仍使用 rc1 的 6 个固定 PBT，不改题、不泄漏答案：

1. 中际旭创复合传闻 / Provenance；
2. 新易盛完整研究 / 高成长 Forecast + Valuation；
3. Broadcom 全球财报 / Consensus + Guidance + Valuation；
4. 中芯国际 A/H / Capital-intensive valuation；
5. 洛阳钼业 / Cyclical Normalized Earnings；
6. 新易盛一句话 / Output compression。

> 6题 × 3次独立运行 = 18样本。

## rc2重点判定

### PBT-2 新易盛
不要求三次输出完全相同的2027/2028利润或目标价值；要求：
- Forecast Anchor一致；
- Base变化必须能追溯到Volume / ASP / Mix / margin / capacity / share等明确变量；
- 与可靠Consensus的差异必须解释；
- Base不允许无新证据地大幅漂移到足以反转一阶投资动作；
- 估值时间点、股本和Forward年度必须清楚。

### PBT-5 洛阳钼业
要求：
- 当前高景气利润与Normalized Earnings分开；
- 正常化铜价/销量/成本/钴可售量等核心假设可见；
- 不混用高景气盈利与中周期低倍数；
- Base正常化利润如跨Run明显变化，必须有明确假设差异；
- 一阶结论至少不弱于Frozen Project的周期估值纪律。

### PBT-3 / PBT-4
作为 opposite-side / non-regression：
- Ref03不能把所有公司机械变成同一种PE模型；
- AVGO、SMIC应继续使用与经济特征匹配的估值框架；
- 不得因强化估值而削弱Actual/Consensus/Guidance、A/H routing或技术→盈利分层。

### PBT-1 / PBT-6
作为非目标维度回归：
- PBT-1 Evidence能力不能下降；
- PBT-6必须仍严格一句话，Ref03不能造成输出膨胀。

## Reference Trigger 观察

如 runtime 提供 telemetry：
- PBT-1：Ref01；Ref03通常不需要；
- PBT-2：Ref01 + Ref02 + Ref03；
- PBT-3：Ref01 + Ref02 + Ref03；
- PBT-4：Ref01 + Ref02 + Ref03；
- PBT-5：Ref01 + Ref02 + Ref03；
- PBT-6：后台可使用三份Reference，但前台必须一句话。

不可观察Reference telemetry时，使用输出行为做黑盒判定，不自动FAIL。

## Freeze Gate

- 16维逐项 ≥ Frozen Project Baseline；
- P0=0；P1=0；
- Forecast / Valuation target regression被修复；
- 6个一阶结论跨3轮稳定，且任何差异可解释；
- 无 Evidence-Auditor regression；
- 无外部Skill依赖；
- Search/Output成本无系统性无意义膨胀；
- 才能 Freeze 为 `a-stock-investment-analysis v1.0.0`。
