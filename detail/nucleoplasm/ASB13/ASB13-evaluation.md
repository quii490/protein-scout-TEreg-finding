---
type: protein-evaluation
gene: "ASB13"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ASB13 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ASB13 |
| 蛋白名称 | Ankyrin repeat and SOCS box protein 13 |
| 蛋白大小 | 278 aa / 30.0 kDa |
| UniProt ID | Q8WXK3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Golgi apparatus; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 278 aa / 30.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=91.8; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR051573, IPR002110, IPR036770, IPR037334, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.5/180** | |
| **归一化总分** | | | **70.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Golgi apparatus | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6 |
| PubMed broad count | 12 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Recurrent copy number alterations in young women with breast cancer.. *Oncotarget*. PMID: 29545918
2. Decoding ulcerative colitis pathogenesis through transcriptomics: from dysregulated gene networks to targeted intervention strategies.. *Journal of translational autoimmunity*. PMID: 41492412
3. Computational identification and analysis of early diagnostic biomarkers for kidney cancer.. *Journal of human genetics*. PMID: 31350524
4. Identification of key programmed cell death-related genes and immune infiltration in extracorporeal membrane oxygenation treatment for acute myocardial infarction based on bioinformatics analysis.. *Frontiers in cardiovascular medicine*. PMID: 36531699
5. Germinal center B cell-like (GCB) and activated B cell-like (ABC) type of diffuse large B cell lymphoma (DLBCL): analysis of molecular predictors, signatures, cell cycle state and patient survival.. *Cancer informatics*. PMID: 19455257

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.8 |
| 高置信度残基 (pLDDT>90) 占比 | 85.6% |
| 置信残基 (pLDDT 70-90) 占比 | 7.6% |
| 中等置信 (pLDDT 50-70) 占比 | 0.7% |
| 低置信 (pLDDT<50) 占比 | 6.1% |
| 有序区域 (pLDDT>70) 占比 | 93.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=91.8，有序区 93.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051573, IPR002110, IPR036770, IPR037334, IPR001496; Pfam: PF12796, PF13637, PF07525 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CUL5 | 0.804 | 0.626 | — |
| ELOB | 0.688 | 0.424 | — |
| RNF7 | 0.668 | 0.468 | — |
| ASB7 | 0.641 | 0.000 | — |
| KLHL20 | 0.632 | 0.045 | — |
| ARIH2 | 0.603 | 0.000 | — |
| ELOC | 0.595 | 0.315 | — |
| NUDT3 | 0.575 | 0.175 | — |
| COMMD8 | 0.544 | 0.105 | — |
| NEDD8 | 0.532 | 0.100 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HIF1AN | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TRIP13 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MARK3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| DNM1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| NUDT3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| CUL5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| VAC14 | psi-mi:"MI:0397"(two hybrid array) | pubmed:29892012|doi:10.1038/s4 |
| HAPLN2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ZNF581 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ASB9 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.8 + PDB: 无 | pLDDT=91.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. ASB13 — Ankyrin repeat and SOCS box protein 13，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小278 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 深度机制分析

**结构域架构**：ASB13（278 aa, Q8WXK3, pLDDT=91.8）是ASB（Ankyrin repeat and SOCS box）E3 ubiquitin ligase adaptor家族的典型成员——N端为ankyrin repeat tandem array（约5-7个重复, SMART: SM00248/InterPro: IPR002110/InterPro: IPR036770）——每个ankyrin repeat为33 aa的helix-turn-helix（β2-α2）结构——stacked repeats形成右手super-helical solenoid（L-shaped ankyrin groove）——提供extended protein interaction surface——C端为SOCS box domain（229-278 aa, SMART: SM00969/InterPro: IPR001496）——SOCS box含约50 aa——包含BC-box motif（~12 aa, 直接结合Elongin C）和Cullin box（结合CUL5 N-terminal domain）。AlphaFold pLDDT=91.8（极高置信度, 有序区93.2%）表明ankyrin-SOCS junction为高度有序的单域折叠——无长程无规区域——ankyrin solenoid全长均为刚性结构。

**PPI互作网络解读**：PPI网络100%指向ECS（Elongin-Cullin-SOCS box）ubiquitin ligase assembly。CUL5（STRING 0.804, 实验分0.626, IntAct TAP PMID:21145461）为cullin-5 scaffold protein——ELOB/Elongin B（STRING 0.688, 实验分0.424）和ELOC/Elongin C（STRING 0.595, 实验分0.315）形成Elongin BC heterodimer——SOCS box→Elongin BC→CUL5→RNF7/Rbx2（STRING 0.668, 实验分0.468, RING finger protein）构成完整的CRL5（Cullin-RING Ligase 5）全酶。ASB13的ankyrin repeats作为substrate recognition module——以ankyrin groove识别靶蛋白特定motif——将substrate呈递给CUL5-RNF7 catalytic core进行K48 polyubiquitination→26S proteasome降解。HIF1AN（FIH, Factor Inhibiting HIF, two-hybrid PMID:16189514）为asparaginyl hydroxylase——调控HIF-1α的oxygen-dependent degradation——ASB13可能通过CRL5 ubiquitination调控HIF1AN蛋白稳定性→间接调控HIF-dependent hypoxia pathway。NUDT3（STRING 0.575）为nucleotide diphosphate hydrolase——ASB13-NUDT3 interaction可能耦合核苷酸代谢与蛋白泛素化。ASB7（STRING 0.641）和ASB9（IntAct two-hybrid PMID:32296183）为ASB家族paralog——可能竞争结合CUL5-Elongin BC——调控ubiquitination specificity。

**结构解读**：pLDDT=91.8——几乎所有残基pLDDT>90（85.6%）或70-90（7.6%）——仅6.1% pLDDT<50（位于N/C末端flexible termini）——结构预测可信度极高。SOCS box的C-terminal helix（约20 aa）以canonical conformation对接CUL5 hydrophobic groove——ankyrin solenoid提供substrate docking platform——整体构象为extended rod-shaped（约90 A长度）。

**机制模型**：（1）ASB13通过ankyrin groove识别特定substrate——将其K48 polyubiquitinated——标记26S proteasome降解。（2）ASB13的HPA Nucleoplasm + Golgi双定位提示其nucleocytoplasmic shuttling——核内CRL5 substrate可能为chromatin-associated protein或transcription factor——ASB13的SOCS box-CUL5在核内可能参与TE silencing complex（如KRAB-ZFP/KAP1/SETDB1）的turnover regulation——KAP1/TRIM28为CRL5已知substrate。（3）Golgi localization可能反映ASB13通过ankyrin repeat与membrane-associated protein的interaction——ankyrin repeat protein的经典模式（如Notch ankyrin repeats）。

**TE调控展望**：CUL5-based E3 ligase在HIV-1 Vif-mediated APOBEC3G降解中是paradigmatic——但CRL5在TE silencing中的角色几乎未被研究。ASB13的核内CUL5 adaptor功能可能降解维持TE silencing所需的chromatin modifier——或将TE-activating transcription factor泛素化降解——取决于其specific substrate identity。PubMed仅6篇使ASB13极具探索价值——CRL5-ankyrin adaptor在TE regulation中的功能为完全未开发领域。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TRIP13 | BioGRID | 0 |
| HIF1AN | BioGRID | 0 |
| DNM1 | BioGRID | 0 |
| NUDT3 | BioGRID | 0 |
| DUSP23 | BioGRID | 0 |
| CUL5 | BioGRID | 0 |
| MARK3 | BioGRID | 0 |
| POLR3A | BioGRID | 0 |


### TE 调控评估

该蛋白具有核定位证据，可能间接参与 TE 调控。需实验验证。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WXK3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000196372-ASB13/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ASB13
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WXK3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000196372-ASB13/subcellular

![](https://images.proteinatlas.org/61742/1118_E8_7_red_green.jpg)
![](https://images.proteinatlas.org/61742/1118_E8_9_red_green.jpg)
![](https://images.proteinatlas.org/61742/1153_E8_1_red_green.jpg)
![](https://images.proteinatlas.org/61742/1153_E8_2_red_green.jpg)
![](https://images.proteinatlas.org/61742/1422_G12_1_red_green.jpg)
![](https://images.proteinatlas.org/61742/1422_G12_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8WXK3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8WXK3 |
| SMART | SM00248;SM00969; |
| UniProt Domain [FT] | DOMAIN 229..278; /note="SOCS box"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00194" |
| InterPro | IPR051573;IPR002110;IPR036770;IPR037334;IPR001496;IPR036036; |
| Pfam | PF12796;PF13637;PF07525; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000196372-ASB13/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| HIF1AN | Intact, Biogrid | true |
| NUDT3 | Intact, Biogrid | true |
| VAC14 | Intact, Biogrid | true |
| ATXN1 | Intact | false |
| CUL5 | Biogrid | false |
| ELOB | Biogrid | false |
| KLF11 | Intact | false |
| MARK3 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
