---
type: protein-evaluation
gene: "TWISTNB"
date: 2026-06-28
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TWISTNB — REJECTED (核定位证据不足 (核定位得分 0/10))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | TWISTNB |
| 蛋白名称 | TWIST neighbor (TWISTNB, POLR1F-like, RNA polymerase I subunit-associated) |
| 蛋白大小 | 328 aa / ~37 kDa |
| UniProt ID | Q5T6N3 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 0/10 | ×4 | 0 | 核仁相关但hpa_nuclear=False |
| 蛋白大小 | 3/10 | ×1 | 3 | 328 aa |
| 研究新颖性 | 7/10 | ×5 | 35 | PubMed=~15 |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold中等 |
| 调控结构域 | 3/10 | ×2 | 6 | RPOLD domain-like |
| PPI 网络 | 4/10 | ×3 | 12 | PPI degree=17 |
| **加权总分** | | | **68/180** | |
| **归一化总分** | | | **38/100** | |

### 3. 详细分析

#### 3.1 核定位证据

**GO Cellular Component**:
- RNA polymerase I complex (GO:0005736)
- nucleolus (predicted by association, not confirmed)

**结论**: 虽然TWISTNB与RNA聚合酶I相关（POLR1F样蛋白），理论上为核仁蛋白，但在当前筛选中因hpa_nuclear=False且未列为核蛋白准入基因，故按标准拒绝。该蛋白参与rRNA转录，涉及45S pre-rRNA的合成，但核仁定位缺乏直接的HPA实验验证。

#### 3.2 蛋白大小、研究现状、结构、结构域、PPI（各1-2行简要说明）

- **蛋白大小**: 328 aa，较小蛋白。
- **研究现状**: 很少研究（PubMed约15篇），主要因基因组位置与TWIST1基因相邻而命名，功能研究不足。
- **三维结构**: 无实验结构，AlphaFold预测覆盖中等。
- **结构域**: RPOLD（RNA polymerase Rpc34-like）结构域。
- **PPI**: PPI度=17，与RNA Pol I亚基有一定相互作用网络。

### 4. 总体评价

**推荐等级**: REJECTED

**核心结论**: TWISTNB — POLR1F样蛋白，与RNA聚合酶I相关。虽然功能上可能涉及核仁rRNA转录，但按照当前筛选标准（hpa_nuclear=False），核定位证据不足。不建议作为核蛋白研究目标。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5T6N3
- Protein Atlas: https://www.proteinatlas.org/search/TWISTNB
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TWISTNB
- AlphaFold: https://alphafold.ebi.ac.uk/search/text/TWISTNB
