---
type: protein-evaluation
gene: "RAI2"
date: 2026-06-28
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## RAI2 — REJECTED (核定位证据不足 (核定位得分 1/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | RAI2 |
| 蛋白名称 | Retinoic acid-induced protein 2 |
| 蛋白大小 | 530 aa / ~57 kDa |
| UniProt ID | Q9Y5P3 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 1/10 | ×4 | 4 | 胞质: 维甲酸诱导蛋白, CtBP共抑制因子结合, 细胞质定位 |
| 蛋白大小 | 8/10 | ×1 | 8 | 530 aa |
| 研究新颖性 | 5/10 | ×5 | 25 | PubMed≈90篇, 新颖度中等 |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold预测中等置信度, 含无序区域 |
| 调控结构域 | 4/10 | ×2 | 8 | 富含脯氨酸区域 + SLiM模体(CtBP结合) |
| PPI 网络 | 3/10 | ×3 | 9 | PPI degree=4 |
| **加权总分** | | | **72/180** | |
| **归一化总分** | | | **40.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)

**结论**: 该蛋白为维甲酸诱导蛋白2，定位于细胞质，作为CtBP共抑制因子的结合蛋白参与转录调控(非直接核定位)，功能表现为肿瘤转移抑制因子。非核蛋白。

#### 3.2 蛋白大小、研究现状、结构、结构域、PPI（各1-2行简要说明）

- **蛋白大小**: 530 aa，中等大小。
- **研究现状**: PubMed约90篇，以乳腺癌/前列腺癌转移抑制功能为主，2025年最新研究发现其在同源重组DNA修复中重要角色。
- **三维结构**: AlphaFold预测中等置信度，含长段无序区域，无实验结构。
- **结构域**: 中心富含脯氨酸区域，含重复SLiM模体介导CtBP聚合。
- **PPI**: 4个互作配体(source STRING)，主要与CtBP1/CtBP2共抑制因子复合物互作。

### 4. 总体评价

**推荐等级**: REJECTED

**核心结论**: RAI2 — 维甲酸诱导蛋白2，定位于细胞质，作为CtBP共抑制因子调节蛋白参与转录调控，非直接核蛋白。无核定位证据，不建议作为核蛋白研究目标。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y5P3
- Protein Atlas: https://www.proteinatlas.org/search/RAI2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RAI2
- AlphaFold: https://alphafold.ebi.ac.uk/search/text/RAI2
