---
type: protein-evaluation
gene: "TES"
date: 2026-06-28
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TES — REJECTED (核定位证据不足 (核定位得分 0/10))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | TES |
| 蛋白名称 | Testin (TES, LIM domain protein, focal adhesion protein) |
| 蛋白大小 | 421 aa / ~48 kDa |
| UniProt ID | Q9UGI8 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 0/10 | ×4 | 0 | 定位于黏着斑，胞质蛋白 |
| 蛋白大小 | 4/10 | ×1 | 4 | 421 aa |
| 研究新颖性 | 5/10 | ×5 | 25 | PubMed=~120 |
| 三维结构 | 5/10 | ×3 | 15 | AlphaFold中等覆盖 |
| 调控结构域 | 4/10 | ×2 | 8 | 3× LIM domains |
| PPI 网络 | 5/10 | ×3 | 15 | PPI degree=30 |
| **加权总分** | | | **67/180** | |
| **归一化总分** | | | **37/100** | |

### 3. 详细分析

#### 3.1 核定位证据

**GO Cellular Component**:
- focal adhesion (GO:0005925)
- cytoplasm (GO:0005737)
- stress fiber (GO:0001725)

**结论**: 该蛋白定位于黏着斑和应力纤维，作为细胞-基质黏附的重要支架蛋白，含三个LIM结构域。胞质定位明确，无核定位信号，HPA、UniProt均显示胞质/黏着斑定位。

#### 3.2 蛋白大小、研究现状、结构、结构域、PPI（各1-2行简要说明）

- **蛋白大小**: 421 aa，中等偏小，适合体外生化实验。
- **研究现状**: PubMed约120篇，主要功能为肿瘤抑制因子，参与细胞黏附和迁移。
- **三维结构**: AlphaFold整体覆盖良好，LIM结构域为锌指折叠。
- **结构域**: 三个LIM结构域，负责蛋白-蛋白相互作用。
- **PPI**: PPI度=30，与黏着斑蛋白、细胞骨架蛋白有广泛相互作用。

### 4. 总体评价

**推荐等级**: REJECTED

**核心结论**: TES — 黏着斑蛋白testin。该蛋白定位于胞质的黏着斑和应力纤维，作为细胞骨架-细胞外基质连接的支架蛋白，无核定位证据。不建议作为核蛋白研究目标。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UGI8
- Protein Atlas: https://www.proteinatlas.org/search/TES
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TES
- AlphaFold: https://alphafold.ebi.ac.uk/search/text/TES
