---
type: protein-evaluation
gene: "CENPH"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CENPH 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CENPH / Centromere protein H |
| 蛋白大小 | 247 aa / 28.5 kDa |
| UniProt ID | Q9H3R5 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 9/10 | ×4 | 36 | Nucleus; Chromosome, centromere, kinetochore |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 247 aa / 28.5 kDa |
| 🆕 研究新颖性 | 4/10 | ×5 | 30 | PubMed 65 篇 |
| 🏗️ 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=81.8，PDB: 7PB4, 7PKN, 7QOO, 7R5S, 7R5V, 7XHN, 7XHO, 7YWX, 7YYH |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR040034 - CENP-H; InterPro: IPR008426 - CENP-H_C |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 20 partners, IntAct 196 interactions |
| ➕ 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
|  | **原始总分** |  | **124/183** | **121.0/183** |  |  |  |
|  | **归一化总分** |  | **67.8/100** | **66.1/100** |  |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| UniProt | Nucleus; Chromosome, centromere, kinetochore | Swiss-Prot/TrEMBL |
| Protein Atlas (IF) | Nucleoli; Nucleoplasm | Approved |

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CENPH/IF_images/434_H10_1_blue_red_green.jpg|434_H10_1_blue_red]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CENPH/IF_images/434_H10_2_blue_red_green.jpg|434_H10_2_blue_red]]

**结论**: 主要定位于细胞核，HPA Approved。

#### 3.2 蛋白大小评估

**评价**: 大小适中，适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 65 |
| 研究方向 | 待补充关键文献摘要 |

**评价**: 有一定研究基础，但仍存在未探索的niche空间。

**关键文献**:
1. Zhang C et al. (2026). "Genetic architecture and phenotypic diversity of oocyte and early embryo competence defects in female infertility". *Nat Med*. PMID: 41102564
2. Wu X et al. (2015). "Upregulation of centromere protein H is associated with progression of renal cell carcinoma". *J Mol Histol*. PMID: 26248586
3. Zhao WF et al. (2012). "Sp1 and Sp3 are involved in the full transcriptional activity of centromere protein H in human nasopharyngeal carcinoma cells". *FEBS J*. PMID: 22682030
4. Wang Y et al. (2023). "The predictive value of plasma exosomal lncRNAs/mRNAs in NSCLC patients receiving immunotherapy". *Adv Med Sci*. PMID: 36801676
5. Li Q et al. (2023). "CENPH overexpression promotes the progression, cisplatin resistance, and poor prognosis of lung adenocarcinoma via the AKT and ERK/P38 pathways". *Am J Cancer Res*. PMID: 37293159
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.8 |
| 高置信度残基 (pLDDT>90) 占比 | 46.2% |
| 置信残基 (pLDDT 70-90) 占比 | 34.0% |
| 有序区域 (pLDDT>70) 占比 | 80.2% |
| 可用 PDB 条目 | 7PB4, 7PKN, 7QOO, 7R5S, 7R5V, 7XHN, 7XHO, 7YWX, 7YYH |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CENPH/CENPH-PAE.png]]

**评价**: PDB 实验结构（7PB4, 7PKN, 7QOO, 7R5S, 7R5V, 7XHN, 7XHO, 7YWX, 7YYH）+ AlphaFold 高质量预测（pLDDT=81.8），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR040034 - CENP-H; InterPro: IPR008426 - CENP-H_C; Pfam: PF05837 - CENP-H |

**染色质调控潜力分析**: 含明确的核酸结合/染色质相关结构域，多库确认。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| CENPQ | 0.999 | — | — |
| CENPU | 0.999 | — | — |
| CENPK | 0.999 | — | — |
| CENPT | 0.999 | — | — |
| CENPC | 0.999 | — | — |
| CENPL | 0.999 | — | — |
| CENPI | 0.999 | — | — |
| CENPN | 0.999 | — | — |
| CENPP | 0.999 | — | — |
| CENPO | 0.999 | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| intact:EBI-1003700|uniprotkb:A8K3Y1|ensembl:ENSP00000283006.2 | — | — | — | — |
| intact:EBI-2132248 | — | — | — | — |
| intact:EBI-1003677|ensembl:ENSGALP00010014558.1 | — | — | — | — |
| intact:EBI-21633908 | — | — | — | — |
| intact:EBI-747505|uniprotkb:Q8N8N6|uniprotkb:D3DPS1|ensembl:ENSP00000425166.1 | — | — | — | — |

**已知复合体成员** (GO Cellular Component):
- 无 GO-CC 注释

**PPI 互证分析**:
- STRING + IntAct 共同确认: 0
- 仅 STRING 预测: 20
- 仅 IntAct 实验: 196
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 20 个预测互作，IntAct 196 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.8 + PDB: 7PB4, 7PKN, 7QOO, 7R5S, 7R5V, 7XHN, 7XHO, 7YWX, 7YYH | pLDDT=81.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome, centromere, kinetochore | 一致 |
| PPI | STRING + IntAct | 20 + 196 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致: +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. CENPH — Centromere protein H，有一定研究基础，但仍存在未探索的niche空间。
2. 蛋白大小247 aa，大小适中，适合常规生化实验和结构解析。

**风险/不确定性**:
1. 已有一定研究，需确认独特研究角度
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新 5 篇关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外 DNA/染色质结合实验

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H3R5
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CENPH
- AlphaFold: https://alphafold.ebi.ac.uk/entry/CENPH


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[CENPH-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CENPH/CENPH-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H3R5 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR040034;IPR008426; |
| Pfam | PF05837; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000153044-CENPH/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CCDC40 | Intact, Biogrid | true |
| CENPI | Biogrid, Bioplex | true |
| CENPK | Intact, Biogrid, Bioplex | true |
| CENPM | Biogrid, Opencell | true |
| DCTN2 | Intact, Biogrid | true |
| H2AP | Intact, Biogrid | true |
| NDC80 | Intact, Biogrid | true |
| TEKT2 | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
