---
type: protein-evaluation
gene: "DLG4"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DLG4 — REJECTED (研究热度过高 (PubMed strict=179，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DLG4 / PSD95 |
| 蛋白名称 | Disks large homolog 4 |
| 蛋白大小 | 724 aa / 80.5 kDa |
| UniProt ID | P78352 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Nucleoplasm, Centrosome, Basal body; 额外: Plasma membrane, Pr; UniProt: Cell membrane; Postsynaptic density; Synapse; Cytoplasm; Cel |
| 蛋白大小 | 10/10 | x1 | 10 | 724 aa / 80.5 kDa |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=179 篇 (>100->REJECTED) |
| 三维结构 | 10/10 | x3 | 30 | AlphaFold v6 pLDDT=77.6; PDB: 1KEF, 2MES, 3I4W, 3K82, 3ZRT, 5J7J, 5JXB |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR019583, IPR016313, IPR019590, IPR008145, IPR008 |
| PPI 网络 | 2/10 | x3 | 6 | STRING 0 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **78.5/180** | |
| **归一化总分** | | | **43.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Centrosome, Basal body; 额外: Plasma membrane, Primary cilium, Primary cilium tip, Cytosol | Uncertain |
| UniProt | Cell membrane; Postsynaptic density; Synapse; Cytoplasm; Cell projection, axon; Cell projection, den... | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- adherens junction (GO:0005912)
- AMPA glutamate receptor complex (GO:0032281)
- cell junction (GO:0030054)
- cerebellar mossy fiber (GO:0044300)
- cortical cytoskeleton (GO:0030863)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- dendrite cytoplasm (GO:0032839)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 179 |
| PubMed broad count | 2025 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PSD95 |

**关键文献**:
1. Impaired lipophagy induced-microglial lipid droplets accumulation contributes to the buildup of TREM1 in diabetes-associated cognitive impairment.. *Autophagy*. PMID: 37204119
2. DLG4-related synaptopathy: a new rare brain disorder.. *Genetics in medicine : official journal of the American College of Medical Genetics*. PMID: 33597769
3. Endothelial TFEB signaling-mediated autophagic disturbance initiates microglial activation and cognitive dysfunction.. *Autophagy*. PMID: 36588318
4. Activation of PPARA-mediated autophagy reduces Alzheimer disease-like pathology and cognitive decline in a murine model.. *Autophagy*. PMID: 30898012
5. MLKL-USP7-UBA52 signaling is indispensable for autophagy in brain through maintaining ubiquitin homeostasis.. *Autophagy*. PMID: 39193909

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.6 |
| 高置信度残基 (pLDDT>90) 占比 | 51.2% |
| 置信残基 (pLDDT 70-90) 占比 | 23.3% |
| 中等置信 (pLDDT 50-70) 占比 | 5.5% |
| 低置信 (pLDDT<50) 占比 | 19.9% |
| 有序区域 (pLDDT>70) 占比 | 74.5% |
| 可用 PDB 条目 | 1KEF, 2MES, 3I4W, 3K82, 3ZRT, 5J7J, 5JXB, 6QJD, 6QJF, 6QJG |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1KEF, 2MES, 3I4W, 3K82, 3ZRT, 5J7J, 5JXB, 6QJD, 6QJF, 6QJG）+ AlphaFold极高置信度预测（pLDDT=77.6），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019583, IPR016313, IPR019590, IPR008145, IPR008144; Pfam: PF00625, PF10608, PF00595 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Cript | psi-mi:"MI:0405"(competition binding) | pubmed:9786987 |
| Nrxn1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-11694|pubmed:19455133 |
| Nlgn2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-11694|pubmed:19455133 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 3
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.6 + PDB: 1KEF, 2MES, 3I4W, 3K82, 3ZRT,  | pLDDT=77.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane; Postsynaptic density; Synapse; Cyto / Nucleoplasm, Centrosome, Basal body; 额外: Plasma me | 一致 |
| PPI | STRING + IntAct | 0 + 3 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (>=3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ** (REJECTED)

**核心优势**:
1. DLG4 -- Disks large homolog 4，研究基础较多，新颖性有限。
2. 蛋白大小724 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 179 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 179 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P78352
- Protein Atlas: https://www.proteinatlas.org/ENSG00000132535-DLG4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DLG4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P78352
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P78352-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P78352 |
| SMART | SM00072;SM01277;SM00228;SM00326; |
| UniProt Domain [FT] | DOMAIN 65..151; /note="PDZ 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00143"; DOMAIN 160..246; /note="PDZ 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00143"; DOMAIN 313..393; /note="PDZ 3"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00143"; DOMAIN 428..498; /note="SH3"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00192"; DOMAIN 534..709; /note="Guanylate kinase-like"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00100" |
| InterPro | IPR019583;IPR016313;IPR019590;IPR008145;IPR008144;IPR020590;IPR027417;IPR001478;IPR036034;IPR036028;IPR001452;IPR050614; |
| Pfam | PF00625;PF10608;PF00595;PF10600;PF00018; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000132535-DLG4/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CRIPT | Intact, Biogrid | true |
| DLGAP1 | Intact, Biogrid | true |
| ERBB4 | Intact, Biogrid | true |
| GRIN2A | Intact, Biogrid | true |
| GRIN2B | Intact, Biogrid | true |
| GRIN2C | Intact, Biogrid | true |
| KCNA1 | Intact, Biogrid | true |
| KCNA4 | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
