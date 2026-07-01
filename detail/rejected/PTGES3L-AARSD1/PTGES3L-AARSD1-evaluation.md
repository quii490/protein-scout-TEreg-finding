---
type: protein-evaluation
gene: "PTGES3L-AARSD1"
date: 2026-06-28
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PTGES3L-AARSD1 — REJECTED (核定位证据不足 (核定位得分 1/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | PTGES3L-AARSD1 |
| 蛋白名称 | PTGES3L-AARSD1 readthrough transcript protein |
| 蛋白大小 | 586 aa / ~65 kDa |
| UniProt ID | Q9BTE6 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 1/10 | ×4 | 4 | 细胞质: 前列腺素E合酶+丙氨酰tRNA合成酶结构域 |
| 蛋白大小 | 8/10 | ×1 | 8 | 586 aa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed≈12篇 (≤20→10) |
| 三维结构 | 5/10 | ×3 | 15 | AlphaFold readthrough融合蛋白, 结构域预测中等置信度 |
| 调控结构域 | 4/10 | ×2 | 8 | 融合蛋白: 谷胱甘肽S-转移酶结构域 + tRNA合成酶结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | PPI degree=9 |
| **加权总分** | | | **94/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)

**结论**: 该蛋白为PTGES3L和AARSD1基因间的readthrough转录产物，定位于细胞质，参与前列腺素合成与tRNA氨酰化。非核蛋白。

#### 3.2 蛋白大小、研究现状、结构、结构域、PPI（各1-2行简要说明）

- **蛋白大小**: 586 aa，中等大小，适合生化研究。
- **研究现状**: 仅约12篇PubMed文章提及此基因，多为高通量互作组或GWAS研究，无靶向功能研究。
- **三维结构**: 融合蛋白无实验结构，AlphaFold预测中等置信度，长柔性链接区域。
- **结构域**: 谷胱甘肽S-转移酶N端结构域(PTGES3L端) + tRNA合成酶编辑结构域(AARSD1端)。
- **PPI**: 9个互作配体(source STRING)，主要为共分级分离或双杂交筛选中检测到的互作。

### 4. 总体评价

**推荐等级**: REJECTED

**核心结论**: PTGES3L-AARSD1 — readthrough融合转录产物，定位于细胞质，参与前列腺素合成与tRNA代谢。无核定位证据，不建议作为核蛋白研究目标。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BTE6
- Protein Atlas: https://www.proteinatlas.org/search/PTGES3L-AARSD1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PTGES3L-AARSD1
- AlphaFold: https://alphafold.ebi.ac.uk/search/text/PTGES3L-AARSD1
