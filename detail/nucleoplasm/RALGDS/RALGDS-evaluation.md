---
type: protein-evaluation
gene: "RALGDS"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## RALGDS — REJECTED (研究热度过高 (PubMed strict=218，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RALGDS / KIAA1308, RGF |
| 蛋白名称 | Ral guanine nucleotide dissociation stimulator |
| 蛋白大小 | 914 aa / 100.6 kDa |
| UniProt ID | Q12967 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 914 aa / 100.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=218 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.0; PDB: 1RAX, 2B3A, 2RGF, 3KH0 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000159, IPR015758, IPR008937, IPR000651, IPR019 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **79.5/180** | |
| **归一化总分** | | | **44.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Uncertain |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- brush border (GO:0005903)
- cytosol (GO:0005829)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 218 |
| PubMed broad count | 283 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1308, RGF |

**关键文献**:
1. G-protein binding features and regulation of the RalGDS family member, RGL2.. *The Biochemical journal*. PMID: 18540861
2. Structure characterization of human RalGDS gene, and the identification of its novel variant.. *Molecular biology reports*. PMID: 11455956
3. RAS-mediated oncogenic signaling pathways in human malignancies.. *Seminars in cancer biology*. PMID: 29524560
4. Cloning and evaluation of RALGDS as a candidate for the tuberous sclerosis gene TSC1.. *Annals of human genetics*. PMID: 9365783
5. RalGDS-like factor (Rlf) is a novel Ras and Rap 1A-associating protein.. *Oncogene*. PMID: 8710374

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.0 |
| 高置信度残基 (pLDDT>90) 占比 | 23.7% |
| 置信残基 (pLDDT 70-90) 占比 | 24.7% |
| 中等置信 (pLDDT 50-70) 占比 | 7.5% |
| 低置信 (pLDDT<50) 占比 | 44.0% |
| 有序区域 (pLDDT>70) 占比 | 48.4% |
| 可用 PDB 条目 | 1RAX, 2B3A, 2RGF, 3KH0 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=63.0），有序残基占 48.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000159, IPR015758, IPR008937, IPR000651, IPR019804; Pfam: PF00788, PF00617, PF00618 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KRAS | 0.999 | 0.716 | — |
| RALA | 0.999 | 0.302 | — |
| RRAS | 0.999 | 0.435 | — |
| RAP1A | 0.999 | 0.757 | — |
| HRAS | 0.999 | 0.989 | — |
| RALB | 0.996 | 0.302 | — |
| LRPAP1 | 0.996 | 0.230 | — |
| NRAS | 0.988 | 0.302 | — |
| RAP1B | 0.987 | 0.697 | — |
| MRAS | 0.986 | 0.580 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Rit2 | psi-mi:"MI:0018"(two hybrid) | pubmed:10545207 |
| RIT1 | psi-mi:"MI:0018"(two hybrid) | pubmed:10545207 |
| Oog1 | psi-mi:"MI:0018"(two hybrid) | pubmed:16580637|imex:IM-19876 |
| HRAS | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:9628477 |
| RAP1B | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| RRAS2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| KRAS | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| CD68 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| MAPK3 | psi-mi:"MI:0813"(proximity ligation assay) | pubmed:25241761|imex:IM-18707 |
| CC2D2B | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.0 + PDB: 1RAX, 2B3A, 2RGF, 3KH0 | pLDDT=63.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. RALGDS — Ral guanine nucleotide dissociation stimulator，研究基础较多，新颖性有限。
2. 蛋白大小914 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 218 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=63.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 218 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q12967
- Protein Atlas: https://www.proteinatlas.org/ENSG00000160271-RALGDS/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RALGDS
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q12967
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000160271-RALGDS/subcellular

![](https://images.proteinatlas.org/25961/258_F4_1_red_green.jpg)
![](https://images.proteinatlas.org/25961/258_F4_3_red_green.jpg)
![](https://images.proteinatlas.org/25961/259_F4_1_red_green.jpg)
![](https://images.proteinatlas.org/25961/259_F4_2_red_green.jpg)
![](https://images.proteinatlas.org/25961/260_F4_1_red_green.jpg)
![](https://images.proteinatlas.org/25961/260_F4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q12967-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q12967 |
| SMART | SM00314;SM00147;SM00229; |
| UniProt Domain [FT] | DOMAIN 112..249; /note="N-terminal Ras-GEF"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00135"; DOMAIN 386..648; /note="Ras-GEF"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00168"; DOMAIN 798..885; /note="Ras-associating"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00166" |
| InterPro | IPR000159;IPR015758;IPR008937;IPR000651;IPR019804;IPR023578;IPR001895;IPR036964;IPR029071; |
| Pfam | PF00788;PF00617;PF00618; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000160271-RALGDS/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| HRAS | Intact, Biogrid | true |
| ARRB2 | Biogrid | false |
| BRAF | Intact | false |
| KRAS | Biogrid | false |
| MRAS | Biogrid | false |
| RAP1A | Biogrid | false |
| RAP1B | Intact | false |
| RAP2A | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
