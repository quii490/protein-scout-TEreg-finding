---
type: protein-evaluation
gene: "MARS1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MARS1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MARS1 / MARS |
| 蛋白名称 | Methionine--tRNA ligase, cytoplasmic |
| 蛋白大小 | 900 aa / 101.1 kDa |
| UniProt ID | P56192 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Mid piece, Principal piece, End piece; UniProt: Cytoplasm, cytosol; Nucleus, nucleolus |
| 蛋白大小 | 8/10 | ×1 | 8 | 900 aa / 101.1 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=36 篇 (≤40→8) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=90.3; PDB: 2DJV, 4BL7, 4BVX, 4BVY, 5GL7, 5GOY, 5Y6L |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001412, IPR041872, IPR010987, IPR036282, IPR004 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.5/180** | |
| **归一化总分** | | | **72.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Mid piece, Principal piece, End piece | Supported |
| UniProt | Cytoplasm, cytosol; Nucleus, nucleolus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- aminoacyl-tRNA synthetase multienzyme complex (GO:0017101)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- membrane (GO:0016020)
- nucleolus (GO:0005730)
- sperm end piece (GO:0097229)
- sperm midpiece (GO:0097225)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 36 |
| PubMed broad count | 73 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MARS |

**关键文献**:
1. Classification of patients with sepsis according to blood genomic endotype: a prospective cohort study.. *The Lancet. Respiratory medicine*. PMID: 28864056
2. Charcot-Marie-Tooth Hereditary Neuropathy Overview.. **. PMID: 20301532
3. Homocysitaconate controls inflammation through reshaping methionine metabolism and N-homocysteinylation.. *Cell metabolism*. PMID: 40876449
4. Expanding the genotypes and phenotypes for 19 rare diseases by exome sequencing performed in pediatric intensive care unit.. *Human mutation*. PMID: 34298581
5. Host and Microbe Blood Metagenomics Reveals Key Pathways Characterizing Critical Illness Phenotypes.. *American journal of respiratory and critical care medicine*. PMID: 38190719

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.3 |
| 高置信度残基 (pLDDT>90) 占比 | 73.1% |
| 置信残基 (pLDDT 70-90) 占比 | 21.3% |
| 中等置信 (pLDDT 50-70) 占比 | 1.2% |
| 低置信 (pLDDT<50) 占比 | 4.3% |
| 有序区域 (pLDDT>70) 占比 | 94.4% |
| 可用 PDB 条目 | 2DJV, 4BL7, 4BVX, 4BVY, 5GL7, 5GOY, 5Y6L |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2DJV, 4BL7, 4BVX, 4BVY, 5GL7, 5GOY, 5Y6L）+ AlphaFold极高置信度预测（pLDDT=90.3），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001412, IPR041872, IPR010987, IPR036282, IPR004046; Pfam: PF19303, PF00043, PF18485 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MAP3K3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| NFKB2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| RELA | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| IKBKG | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| MAP3K1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| HNRNPUL1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| PPM1F | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| MCC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ILK | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MYC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.3 + PDB: 2DJV, 4BL7, 4BVX, 4BVY, 5GL7,  | pLDDT=90.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol; Nucleus, nucleolus / Cytosol; 额外: Mid piece, Principal piece, End piece | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. MARS1 — Methionine--tRNA ligase, cytoplasmic，非常新颖，仅有少数基础研究。
2. 蛋白大小900 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 36 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P56192
- Protein Atlas: https://www.proteinatlas.org/ENSG00000166986-MARS1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MARS1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P56192
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000166986-MARS1/subcellular

![](https://images.proteinatlas.org/17097/612_G6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17097/612_G6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/17097/615_G6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/17097/615_G6_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/17097/621_G6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17097/621_G6_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P56192-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P56192 |
| SMART | SM00991; |
| UniProt Domain [FT] | DOMAIN 74..198; /note="GST C-terminal"; DOMAIN 841..897; /note="WHEP-TRS" |
| InterPro | IPR001412;IPR041872;IPR010987;IPR036282;IPR004046;IPR041598;IPR023458;IPR014758;IPR015413;IPR033911;IPR029038;IPR014729;IPR009080;IPR009068;IPR000738; |
| Pfam | PF19303;PF00043;PF18485;PF09334;PF00458; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000166986-MARS1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| IARS1 | Biogrid, Bioplex | true |
| LARS1 | Biogrid, Bioplex | true |
| MYC | Intact, Biogrid | true |
| QARS1 | Biogrid, Bioplex | true |
| AIMP1 | Biogrid | false |
| AIMP2 | Biogrid | false |
| ANLN | Biogrid | false |
| ATG13 | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
