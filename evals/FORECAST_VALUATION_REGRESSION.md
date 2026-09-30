# rc2｜Forecast / Valuation Targeted Regression

此文件是研发/验证资产，不属于生产运行流程。

## Target Fix

使用 PBT-2（新易盛）与 PBT-5（洛阳钼业）验证：
- 相同截止时间和核心证据下，中央盈利情景不再发生无法解释的巨大漂移；
- 估值方法、Forward年度、倍数、股本、时间点一致且可审计；
- 差异必须来自显式经营假设，而不是隐式“更保守/更乐观”。

## Non-Regression

使用 PBT-3（AVGO）与 PBT-4（SMIC）验证：
- 不强迫所有公司使用同一估值法；
- Global routing / A-H routing不退化；
- Actual / Consensus / Guidance / Model Estimate分类不退化；
- DCF、PE、PB、EV、Normalized Earnings、SOTP仍按企业经济特征选择。

## Opposite-Side Counterexample

Ref03不能把稳定性变成固定答案：
- 新证据真的改变Volume / price / margin / capacity / commodity mid-cycle等核心变量时，Base必须允许变化；
- 市场一致预期明显失真时，Own Model可以偏离Consensus，但必须解释差异；
- 周期中枢发生结构变化时，Normalized Earnings允许上修或下修，但必须给出证明旧中枢失效的证据。

## Resource / Output Guardrail

- 简短问题不机械输出完整估值模型；
- 不因为Ref03多一次Reference读取，就重复搜索已经在Ref01/02获取的事实；
- 不为了稳定而增加固定行业倍数库、固定增长率表或股票答案表。
