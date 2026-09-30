#!/usr/bin/env python3
from pathlib import Path
import hashlib, re, sys, yaml

root = Path(__file__).resolve().parents[1]
fail=[]
checks=0

def check(cond,msg):
    global checks
    checks += 1
    if not cond: fail.append(msg)

def sha(p):
    h=hashlib.sha256(); h.update(p.read_bytes()); return h.hexdigest()

skill=root/'SKILL.md'
ref1=root/'references'/'01_股票研究与证据验证方法论.md'
ref2=root/'references'/'02_股票深度研究分析框架.md'
ref3=root/'references'/'03_预测、估值与预期差建模规范.md'
yamlp=root/'agents'/'openai.yaml'
required=[skill,ref1,ref2,ref3,yamlp,root/'README.md',root/'evals'/'cases.jsonl',root/'evals'/'SCORECARD.md',root/'evals'/'PBT_RUNBOOK.md',root/'evals'/'FORECAST_VALUATION_REGRESSION.md']
for p in required:
    check(p.exists(),f'missing: {p.relative_to(root)}')

s=skill.read_text(encoding='utf-8')
check(s.startswith('---\n'),'SKILL.md missing YAML frontmatter')
m=re.match(r'^---\n(.*?)\n---\n',s,re.S)
if m:
    meta=yaml.safe_load(m.group(1))
    check(meta.get('name')=='a-stock-investment-analysis','frontmatter name mismatch')
    desc=meta.get('description','')
    check('global' in desc.lower() and 'A-share' in desc,'description must express global + A-share enhanced scope')

# Frozen references 01/02 must remain exact baseline bytes.
check(sha(ref1)=='1b7ecd5081dc84c037dd1e57fa4df88c3ec47a7e433bc059100a0e090c139e7f','Reference 01 hash changed')
check(sha(ref2)=='4908764eb357b139e200c2fd8b1c457f72a264fc3380d2fd83a25697cafe47c9','Reference 02 hash changed')

must=[
'Multi-Lens','Fact / Rumor Verification','Valuation','Market Expectations','Counterevidence',
'references/01_股票研究与证据验证方法论.md','references/02_股票深度研究分析框架.md','references/03_预测、估值与预期差建模规范.md',
'有产品≠量产','订单≠收入','利润≠现金流','A股10步强化执行',
'Issuer + Security + Listing Venue + Reporting Jurisdiction','Verified Consensus','Market Narrative',
'valuation shopping','Evidence Reuse','Research-to-Action','不得因为某一命题没有完全闭环，就自动停止完整股票研究',
'Financial Analysis → Forecast → Valuation → Price-in → Bull/Bear → Investment Judgment',
'不得假设存在 ChatGPT Project Instructions','禁止把完整股票研究退化',
'Forward Earnings','Normalized Earnings','Price-in'
]
for x in must: check(x in s,f'missing contract: {x}')

r3=ref3.read_text(encoding='utf-8')
r3must=[
'Forecast Anchor','Earnings Bridge','Base / Bull / Bear','Normalized Earnings','valuation shopping',
'Consensus 与 Own Model','Price-in','估值时间点与每股口径','没有新证据时，不得静默大幅改变中央情景',
'稳定的目标是**方法、口径和因果桥稳定**，不是固定答案'
]
for x in r3must: check(x in r3,f'Reference03 missing contract: {x}')

# Anti-overfit: no frozen-company answers / fixed values from the failing samples.
for banned in ['新易盛','洛阳钼业','中际旭创','Broadcom','中芯国际','423元','18.15元','335亿元','230亿元','12倍PE']:
    check(banned not in r3,f'Reference03 appears overfit to test sample: {banned}')

# Runtime must not hard-call another Skill or contain R&D governance machinery.
check('$a-stock-evidence-research' not in s,'runtime external Skill invocation dependency detected')
for banned in ['Red Team','Blind Evaluator','Release Gate','Design Expert Panel','Independent Review']:
    check(banned not in s,f'R&D governance leaked into runtime: {banned}')

refs='\n'.join(p.read_text(encoding='utf-8') for p in [ref1,ref2,ref3])
for banned in ['Red Team','Blind Evaluator','Design Expert Panel']:
    check(banned not in refs,f'governance leaked into refs: {banned}')

# No runtime deterministic valuation script in rc2.
check(not (root/'scripts').exists(),'rc2 unexpectedly introduced runtime scripts directory')

meta=yaml.safe_load(yamlp.read_text(encoding='utf-8'))
check(meta.get('policy',{}).get('allow_implicit_invocation') is True,'implicit invocation not enabled')
check('$a-stock-investment-analysis' in meta.get('interface',{}).get('default_prompt',''),'default prompt missing skill invocation')

cases=(root/'evals'/'cases.jsonl').read_text(encoding='utf-8').strip().splitlines()
check(len(cases)==6,f'expected 6 fixed PBT cases, got {len(cases)}')

if fail:
    print('FAIL')
    for x in fail: print('-',x)
    sys.exit(1)
print('PASS')
print('Reference01',sha(ref1))
print('Reference02',sha(ref2))
print('Reference03',sha(ref3))
print('checks',checks)
