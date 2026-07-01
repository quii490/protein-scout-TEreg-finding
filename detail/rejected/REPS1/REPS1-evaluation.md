---
type: protein-evaluation
gene: "REPS1"
date: 2026-06-28
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## REPS1 — REJECTED (核定位证据不足 (核定位得分 1/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | REPS1 |
| 蛋白名称 | RalBP1-associated Eps domain-containing protein 1 |
| 蛋白大小 | 796 aa / ~87 kDa |
| UniProt ID | Q96D71 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 1/10 | ×4 | 4 | 内体/胞质: EH结构域介导内吞作用, 胞质定位 |
| 蛋白大小 | 8/10 | ×1 | 8 | 796 aa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed≈80篇 |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold中等置信度, 含长段无序区域 |
| 调控结构域 | 6/10 | ×2 | 12 | EH结构域(IPR000261) + 中央脯氨酸富集区 + EF-hand |
| PPI 网络 | 4/10 | ×3 | 12 | PPI degree=13 |
| **加权总分** | | | **84/180** | |
| **归一化总分** | | | **46.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- endocytic vesicle membrane (GO:0030666)
- clathrin-coated pit (GO:0005905)

**结论**: 该蛋白含EH(Eps15 Homology)结构域，参与网格蛋白介导的内吞作用，定位于内吞囊泡膜和胞质。作为内吞衔接蛋白，非核定位。

#### 3.2 蛋白大小、研究现状、结构、结构域、PPI（各1-2行简要说明）

- **蛋白大小**: 796 aa，较大蛋白，含多个无序区域。
- **研究现状**: PubMed约80篇，以内吞和受体回收功能研究为主。
- **三维结构**: AlphaFold预测整体中等置信度，EH结构域折叠明确，中央区域含长无序区。
- **结构域**: EH结构域(N端,内吞衔接) + 中央脯氨酸富集区 + EF-hand钙结合模体(C端)。
- **PPI**: 13个互作配体(source STRING)，主要与内吞机制蛋白(RALBP1, EPS15等)互作。

### 4. 总体评价

**推荐等级**: REJECTED

**核心结论**: REPS1 — RalBP1相关Eps结构域蛋白1，内吞衔接蛋白，定位于内吞囊泡/胞质，参与网格蛋白介导的内吞和受体回收。无核定位证据，不建议作为核蛋白研究目标。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96D71
- Protein Atlas: https://www.proteinatlas.org/search/REPS1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=REPS1
- AlphaFold: https://alphafold.ebi.ac.uk/search/text/REPS1
