---
type: protein-evaluation
gene: "NRDE2"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NRDE2 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | NRDE2 / FLJ14051 |
| 蛋白名称 | Nuclear exosome regulator NRDE2 |
| 蛋白大小 | 1164 aa |
| UniProt ID | Q9H7Z3 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 加权 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | **24** | 核+胞质，有核定位证据 |
| 📏 蛋白大小 | 8/10 | ×1 | **8** | 1164 aa，可接受范围 |
| 🆕 研究新颖性 | 10/10 | ×5 | **50** | PubMed 12篇，极度新颖 |
| 🏗️ 三维结构 | 8/10 | ×3 | **24** | 1 个 PDB 实验结构 + AlphaFold 预测 |
| 🧬 调控结构域 | 7/10 | ×2 | **14** | 3 个结构域注释，新颖蛋白基线（存在新域发现潜力） |
| 🔗 PPI 网络 | 4/10 | ×3 | **12** | STRING 15 partners，调控比例较低 |
| ➕ 互证加分 | — | — | **+1.0** | 三维结构: AlphaFold + PDB 双源 (+0.5); PPI: IntAct + STRING 双源 (+0.5) |
| **原始总分** |  |  | **132.5/183** |  |
| **归一化总分** |  |  | **72.4/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_conserved_high_confidence | 高置信度保守 |
| Protein Atlas (IF) | IF image available (embedded below) | See IF_images/ |
| UniProt | N/A | 实验/预测 |
| GO Cellular Component | N/A | N/A |


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NRDE2/IF_images/HEK293_HPA047050_1.jpg|HEK293]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NRDE2/IF_images/MCF-7_HPA047050_2.jpg|MCF-7]]

**结论**: 核+胞质，有核定位证据

#### 3.2 蛋白大小评估

**评价**: 1164 aa，1164 aa，可接受范围。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 12 |
| 核定位分数 (weighted max) | 6 |
| Research hotness | 3.6396 |

**评价**: PubMed 12篇，极度新颖

**关键文献**:
1. Wang Y et al. (2024). "NRDE2 deficiency impairs homologous recombination repair and sensitizes hepatocellular carcinoma to PARP inhibitors". *Cell Genom*. PMID: 38697125
2. Srbic M et al. (2025). "NRDE2 Interacts with an Early Transcription Elongation Complex and Widely Impacts Gene Expression". *Int J Mol Sci*. PMID: 41097056
3. Ding YH et al. (2023). "The nuclear Argonaute HRDE-1 directs target gene re-localization and shuttles to nuage to promote small RNA-mediated inherited silencing". *Cell Rep*. PMID: 37083324
4. Wang Y & Chan YW (2024). "Rare-variant association study unveils the Achilles' heel for HCC". *Cell Genom*. PMID: 38723605
5. Wang J et al. (2019). "NRDE2 negatively regulates exosome functions by inhibiting MTR4 recruitment and exosome interaction". *Genes Dev*. PMID: 30842217
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 1164 aa |
| PDB 条目数 | 1 |
| UniProt 注释结构域数 | 3 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NRDE2/NRDE2-PAE.png]]

**评价**: 1 个 PDB 实验结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | NRDE-2 |
| InterPro | TPR-like_helical_dom_sf |
| Pfam | NRDE-2 |

**染色质调控潜力分析**: 3 个结构域注释，新颖蛋白基线（存在新域发现潜力）

#### 3.6 PPI 网络

**实验验证互作** (IntAct):

IntAct 实验互作: 41 条

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| MTREX | 0 |  | 否 |
| PPP2R2A | 0 |  | 否 |
| PPP2R2B | 0 |  | 否 |
| ZFC3H1 | 0 |  | 否 |
| ZCCHC8 | 0 |  | 否 |
| CCDC174 | 0 |  | 否 |
| GPATCH1 | 0 |  | 否 |
| CRNKL1 | 0 |  | 否 |
| PSMC1 | 0 |  | 否 |
| TBC1D10B | 0 |  | 否 |

**已知复合体成员** (GO Cellular Component):

- P:regulatory ncRNA-mediated heterochromatin formation (GO:0031048, IBA:GO_Central)

**PPI 互证分析**: STRING 15 partners，调控比例较低

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 1 entries | 一致 |
| 结构域 | UniProt / InterPro / Pfam | 3 domains | 多库一致 |
| PPI | STRING + IntAct | 15 STRING + 41 IntAct | 双源 |
| 定位 | Protein Atlas / UniProt / GO | Nucleus | 多源一致 |

**互证加分明细**:
三维结构: AlphaFold + PDB 双源 (+0.5)
PPI: IntAct + STRING 双源 (+0.5)
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ★★★★☆ (4/5)

**核心优势**:
1. 新颖性: PubMed 12 篇，极度新颖
2. 核定位: 部分核定位

**风险/不确定性**:
1. HPA IF 数据可进一步验证
2. 1 PDB 结构可用

**下一步建议**:
- [ ] 验证核定位: IF 实验确认亚核定位
- [ ] 功能研究: 基于 PPI 网络设计功能实验
- [ ] 结构分析: 基于 PDB 结构设计功能实验

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=NRDE2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000119720-NRDE2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22NRDE2%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q9H7Z3
- STRING: https://string-db.org/network/9606.ENSG00000119720
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H7Z3


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[NRDE2-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NRDE2/NRDE2-PAE.png]]




