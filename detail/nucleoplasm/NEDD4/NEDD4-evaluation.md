---
type: protein-evaluation
gene: "NEDD4"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## NEDD4 — REJECTED (研究热度过高 (PubMed strict=1310，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NEDD4 / KIAA0093, NEDD4-1, RPF1 |
| 蛋白名称 | E3 ubiquitin-protein ligase NEDD4 |
| 蛋白大小 | 1319 aa / 149.1 kDa |
| UniProt ID | P46934 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; 额外: Plasma membrane; UniProt: Cytoplasm; Nucleus; Cell membrane |
| 蛋白大小 | 5/10 | ×1 | 5 | 1319 aa / 149.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1310 篇 (>100→REJECTED) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v6 pLDDT=0; PDB: 2KPZ, 2KQ0, 2M3O, 2XBB, 2XBF, 3B7Y, 4BBN |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR035892, IPR050409, IPR000569, IPR035983, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **70.0/180** | |
| **归一化总分** | | | **38.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Plasma membrane | Supported |
| UniProt | Cytoplasm; Nucleus; Cell membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- apicolateral plasma membrane (GO:0016327)
- cell cortex (GO:0005938)
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- glutamatergic synapse (GO:0098978)
- Golgi apparatus (GO:0005794)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1310 |
| PubMed broad count | 1923 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0093, NEDD4-1, RPF1 |

**关键文献**:
1. Nedd4 ubiquitylates VDAC2/3 to suppress erastin-induced ferroptosis in melanoma.. *Nature communications*. PMID: 31974380
2. NEDD4-Mediated GSNOR Degradation Aggravates Cardiac Hypertrophy and Dysfunction.. *Circulation research*. PMID: 39846173
3. NEDD4 lactylation promotes APAP induced liver injury through Caspase11 dependent non-canonical pyroptosis.. *International journal of biological sciences*. PMID: 38385085
4. Rsp5/NEDD4 and ESCRT regulate TDP-43 toxicity and turnover via an endolysosomal clearance mechanism.. *The Journal of cell biology*. PMID: 41498748
5. NEDD4-2 and salt-sensitive hypertension.. *Current opinion in nephrology and hypertension*. PMID: 25602517

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 2KPZ, 2KQ0, 2M3O, 2XBB, 2XBF, 3B7Y, 4BBN, 4BE8, 4N7F, 4N7H |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR035892, IPR050409, IPR000569, IPR035983, IPR001202; Pfam: PF00632, PF00397 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NDFIP1 | 0.999 | 0.671 | — |
| NDFIP2 | 0.998 | 0.860 | — |
| SCNN1B | 0.996 | 0.968 | — |
| UBC | 0.995 | 0.989 | — |
| RPS27A | 0.992 | 0.984 | — |
| ARRDC3 | 0.992 | 0.875 | — |
| PTEN | 0.984 | 0.909 | — |
| ISG15 | 0.981 | 0.570 | — |
| UBE2L3 | 0.979 | 0.929 | — |
| UBB | 0.979 | 0.951 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Bean1 | psi-mi:"MI:0400"(affinity technology) | imex:IM-17722|pubmed:11042109| |
| Ndfip1 | psi-mi:"MI:0400"(affinity technology) | imex:IM-17722|pubmed:11042109| |
| Pmepa1 | psi-mi:"MI:0400"(affinity technology) | imex:IM-17722|pubmed:11042109| |
| Rnf11 | psi-mi:"MI:0400"(affinity technology) | imex:IM-17722|pubmed:11042109| |
| Prrg2 | psi-mi:"MI:0400"(affinity technology) | imex:IM-17722|pubmed:11042109| |
| Litaf | psi-mi:"MI:0400"(affinity technology) | imex:IM-17722|pubmed:11042109| |
| NDFIP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ptc | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| Amph | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| RPL18A | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 2KPZ, 2KQ0, 2M3O, 2XBB, 2XBF,  | pLDDT=0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Cell membrane / Nucleoplasm, Cytosol; 额外: Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. NEDD4 — E3 ubiquitin-protein ligase NEDD4，研究基础较多，新颖性有限。
2. 蛋白大小1319 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 1310 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1310 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P46934
- Protein Atlas: https://www.proteinatlas.org/ENSG00000069869-NEDD4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NEDD4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P46934
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000069869-NEDD4/subcellular

![](https://images.proteinatlas.org/46793/2253_F7_68_blue_red_green.jpg)
![](https://images.proteinatlas.org/46793/2253_F7_89_blue_red_green.jpg)
![](https://images.proteinatlas.org/46793/856_E11_1_red_green.jpg)
![](https://images.proteinatlas.org/46793/856_E11_2_red_green.jpg)
![](https://images.proteinatlas.org/46793/981_A10_1_red_green.jpg)
![](https://images.proteinatlas.org/46793/981_A10_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P46934-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P46934 |
| SMART | SM00119;SM00456; |
| UniProt Domain [FT] | DOMAIN 610..643; /note="WW 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00224"; DOMAIN 767..800; /note="WW 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00224"; DOMAIN 840..873; /note="WW 3"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00224"; DOMAIN 892..925; /note="WW 4"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00224"; DOMAIN 984..1318; /note="HECT"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00104" |
| InterPro | IPR035892;IPR050409;IPR000569;IPR035983;IPR001202;IPR036020; |
| Pfam | PF00632;PF00397; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000069869-NEDD4/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ARRDC3 | Intact, Biogrid | true |
| EGFR | Intact, Biogrid | true |
| ENTREP1 | Intact, Biogrid | true |
| FGFR1 | Intact, Biogrid | true |
| GABARAP | Intact, Biogrid | true |
| GABARAPL1 | Intact, Biogrid | true |
| GABARAPL2 | Intact, Biogrid | true |
| LAPTM5 | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
