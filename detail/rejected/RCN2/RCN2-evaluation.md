---
type: protein-evaluation
gene: "RCN2"
date: 2026-06-28
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## RCN2 — REJECTED (核定位证据不足 (核定位得分 1/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | RCN2 |
| 蛋白名称 | Reticulocalbin-2 (ERC-55 calcium-binding protein) |
| 蛋白大小 | 317 aa / ~37 kDa |
| UniProt ID | Q14257 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 1/10 | ×4 | 4 | ER腔: 内质网钙结合蛋白, N端信号肽→ER腔定位 |
| 蛋白大小 | 5/10 | ×1 | 5 | 317 aa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed≈90篇 |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold预测良好, 6个EF-hand结构域规则折叠 |
| 调控结构域 | 5/10 | ×2 | 10 | 信号肽 + 6×EF-hand钙结合模体(IPR002048) |
| PPI 网络 | 6/10 | ×3 | 18 | PPI degree=35 |
| **加权总分** | | | **88/180** | |
| **归一化总分** | | | **48.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

**GO Cellular Component**:
- endoplasmic reticulum lumen (GO:0005788)
- ER-Golgi intermediate compartment (GO:0005793)

**结论**: 该蛋白含N端信号肽，定位于内质网腔，作为EF-hand钙结合蛋白参与ER钙稳态调控。UniProt GO-CC明确指向ER区室，非核蛋白。

#### 3.2 蛋白大小、研究现状、结构、结构域、PPI（各1-2行简要说明）

- **蛋白大小**: 317 aa，含信号肽，成熟蛋白约300 aa，较小。
- **研究现状**: PubMed约90篇，以内质网钙结合蛋白(CREC家族)功能研究为主。
- **三维结构**: AlphaFold预测良好，6个EF-hand结构域规则排列，高置信度。
- **结构域**: N端信号肽(1-22) + 6个串联EF-hand钙结合模体(IPR002048)。
- **PPI**: 35个互作配体(source STRING)，钙结合蛋白CREC家族网络密度较高。

### 4. 总体评价

**推荐等级**: REJECTED

**核心结论**: RCN2 — 内质网钙结合蛋白(Reticulocalbin-2)，定位于ER腔，参与ER钙稳态和蛋白质折叠。CREC家族成员，无核定位可能，不建议作为核蛋白研究目标。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q14257
- Protein Atlas: https://www.proteinatlas.org/search/RCN2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RCN2
- AlphaFold: https://alphafold.ebi.ac.uk/search/text/RCN2
