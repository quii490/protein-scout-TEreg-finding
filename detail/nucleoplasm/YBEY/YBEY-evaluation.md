---
type: protein-evaluation
gene: "YBEY"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## YBEY 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | YBEY / C21orf57 |
| 蛋白名称 | Endoribonuclease YbeY |
| 蛋白大小 | 167 aa / 19.3 kDa |
| UniProt ID | P58557 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 167 aa / 19.3 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=43 篇 (≤60→6) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=96.2; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR023091, IPR002036, IPR020549; Pfam: PF02130 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.0/180** | |
| **归一化总分** | | | **62.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- mitochondrion (GO:0005739)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 43 |
| PubMed broad count | 53 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C21orf57 |

**关键文献**:
1. YbeY, éminence grise of ribosome biogenesis.. *Biochemical Society transactions*. PMID: 33929506
2. Identification of YbeY-Protein Interactions Involved in 16S rRNA Maturation and Stress Regulation in Escherichia coli.. *mBio*. PMID: 27834201
3. Endoribonuclease YbeY Is Essential for RNA Processing and Virulence in Pseudomonas aeruginosa.. *mBio*. PMID: 32605982
4. YbeY controls the type III and type VI secretion systems and biofilm formation through RetS in Pseudomonas aeruginosa.. *Applied and environmental microbiology*. PMID: 33310711
5. Genome-wide gene by sleepiness interaction analysis for sleep apnea.. *Sleep*. PMID: 40736211

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 96.2 |
| 高置信度残基 (pLDDT>90) 占比 | 95.8% |
| 置信残基 (pLDDT 70-90) 占比 | 3.0% |
| 中等置信 (pLDDT 50-70) 占比 | 1.2% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 98.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=96.2，有序区 98.8%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR023091, IPR002036, IPR020549; Pfam: PF02130 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ybeZ | psi-mi:"MI:0096"(pull down) | pubmed:15690043|mint:MINT-5217 |
| bipA | psi-mi:"MI:0096"(pull down) | pubmed:15690043|mint:MINT-5217 |
| rpsE | psi-mi:"MI:0096"(pull down) | pubmed:16606699 |
| rof | psi-mi:"MI:0096"(pull down) | pubmed:16606699 |
| yciA | psi-mi:"MI:0096"(pull down) | pubmed:16606699 |
| rplB | psi-mi:"MI:0096"(pull down) | pubmed:16606699 |
| rpsD | psi-mi:"MI:0096"(pull down) | pubmed:16606699 |
| yfdP | psi-mi:"MI:0096"(pull down) | pubmed:16606699 |
| yghW | psi-mi:"MI:0096"(pull down) | pubmed:16606699 |
| rplP | psi-mi:"MI:0096"(pull down) | pubmed:16606699 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=96.2 + PDB: 无 | pLDDT=96.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. YBEY — Endoribonuclease YbeY，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小167 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 43 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P58557
- Protein Atlas: https://www.proteinatlas.org/ENSG00000182362-YBEY/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=YBEY
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P58557
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000182362-YBEY/subcellular

![](https://images.proteinatlas.org/16593/112_D9_1_red_green.jpg)
![](https://images.proteinatlas.org/16593/112_D9_2_red_green.jpg)
![](https://images.proteinatlas.org/16593/113_D9_1_red_green.jpg)
![](https://images.proteinatlas.org/16593/113_D9_2_red_green.jpg)
![](https://images.proteinatlas.org/16593/161_D9_1_red_green.jpg)
![](https://images.proteinatlas.org/16593/161_D9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P58557-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P58557 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR023091;IPR002036;IPR020549; |
| Pfam | PF02130; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000182362-YBEY/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BCAT2 | Intact | false |
| CARTPT | Bioplex | false |
| CLPP | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
