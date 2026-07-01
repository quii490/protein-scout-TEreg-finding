---
type: protein-evaluation
gene: "RHBDD2"
date: 2026-06-28
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## RHBDD2 — REJECTED (核定位证据不足 (核定位得分 1/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | RHBDD2 |
| 蛋白名称 | Rhomboid domain-containing protein 2 |
| 蛋白大小 | 364 aa / ~39 kDa |
| UniProt ID | Q6NTF9 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 1/10 | ×4 | 4 | 膜: 多次跨膜蛋白, 高尔基体顺面膜囊定位 |
| 蛋白大小 | 5/10 | ×1 | 5 | 364 aa |
| 研究新颖性 | 7/10 | ×5 | 35 | PubMed≈30篇 |
| 三维结构 | 4/10 | ×3 | 12 | 跨膜蛋白AlphaFold预测困难, 膜内结构域中等置信度 |
| 调控结构域 | 4/10 | ×2 | 8 | Rhomboid丝氨酸蛋白酶结构域(IPR002610) |
| PPI 网络 | 3/10 | ×3 | 9 | PPI degree=8 |
| **加权总分** | | | **73/180** | |
| **归一化总分** | | | **40.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

**GO Cellular Component**:
- Golgi apparatus membrane (GO:0000139)
- cis-Golgi network membrane (GO:0033116)
- membrane (GO:0016020)

**结论**: 该蛋白为多次跨膜蛋白(Multi-pass)，含Rhomboid丝氨酸蛋白酶结构域，定位于高尔基体顺面膜囊。跨膜拓扑结构明确排除核定位可能。

#### 3.2 蛋白大小、研究现状、结构、结构域、PPI（各1-2行简要说明）

- **蛋白大小**: 364 aa，较小跨膜蛋白，多次跨膜。
- **研究现状**: PubMed约30篇，以乳腺癌/结直肠癌过表达和5-FU耐药相关研究为主。
- **三维结构**: 跨膜蛋白实验结构缺失，AlphaFold跨膜区域预测中等，膜内蛋白酶结构域保守。
- **结构域**: Rhomboid家族丝氨酸蛋白酶结构域(IPR002610)，膜内蛋白水解功能。
- **PPI**: 8个互作配体(source STRING)，互作网络数据有限。

### 4. 总体评价

**推荐等级**: REJECTED

**核心结论**: RHBDD2 — 多次跨膜高尔基体蛋白，膜内Rhomboid丝氨酸蛋白酶，定位于高尔基体顺面膜囊。跨膜蛋白，无核定位可能。不建议作为核蛋白研究目标。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6NTF9
- Protein Atlas: https://www.proteinatlas.org/search/RHBDD2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RHBDD2
- AlphaFold: https://alphafold.ebi.ac.uk/search/text/RHBDD2
