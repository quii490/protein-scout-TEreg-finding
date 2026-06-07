---
type: protein-evaluation
gene: "ESD"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ESD — REJECTED (研究热度过高 (PubMed strict=446，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ESD |
| 蛋白名称 | S-formylglutathione hydrolase |
| 蛋白大小 | 282 aa / 31.5 kDa |
| UniProt ID | P10768 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Golgi apparatus; 额外: Nucleoplasm, Cytosol; UniProt: Cytoplasm; Cytoplasmic vesicle |
| 蛋白大小 | 10/10 | ×1 | 10 | 282 aa / 31.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=446 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=98.2; PDB: 3FCX |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR029058, IPR000801, IPR014186; Pfam: PF00756 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **77.0/180** | |
| **归一化总分** | | | **42.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Nucleoplasm, Cytosol | Approved |
| UniProt | Cytoplasm; Cytoplasmic vesicle | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- cytoplasmic vesicle (GO:0031410)
- cytosol (GO:0005829)
- endoplasmic reticulum lumen (GO:0005788)
- extracellular exosome (GO:0070062)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 446 |
| PubMed broad count | 8547 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Protein Structure Databases.. *Methods in molecular biology (Clifton, N.J.)*. PMID: 27115626
2. Ershen Dan attenuates atherosclerosis by modulating the NOTCH1/NF-κB/NLRP3 signaling pathway to suppress M1 macrophage polarization.. *Chinese medicine*. PMID: 41131540
3. Clinical utility of a novel anchor pronged clip for mucosal defect closure after colorectal endoscopic submucosal dissection (with video).. *Endoscopy international open*. PMID: 39398446
4. Hippocampal proteomic changes of susceptibility and resilience to depression or anxiety in a rat model of chronic mild stress.. *Translational psychiatry*. PMID: 31624233
5. Where the Ends Meet: An Overview of Sex Determination in Atheriniform Fishes.. *Sexual development : genetics, molecular biology, evolution, endocrinology, embryology, and pathology of sex determination and differentiation*. PMID: 33951664

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 98.2 |
| 高置信度残基 (pLDDT>90) 占比 | 99.3% |
| 置信残基 (pLDDT 70-90) 占比 | 0.4% |
| 中等置信 (pLDDT 50-70) 占比 | 0.4% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 99.7% |
| 可用 PDB 条目 | 3FCX |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=98.2，有序区 99.7%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029058, IPR000801, IPR014186; Pfam: PF00756 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ADH5 | 0.998 | 0.438 | — |
| CES5A | 0.925 | 0.062 | — |
| GLO1 | 0.904 | 0.000 | — |
| ADH6 | 0.900 | 0.071 | — |
| ADH4 | 0.891 | 0.071 | — |
| SORD | 0.889 | 0.000 | — |
| ADH1A | 0.874 | 0.071 | — |
| CES2 | 0.872 | 0.062 | — |
| ADH1B | 0.864 | 0.071 | — |
| ADH1C | 0.863 | 0.071 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000367992.3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| HLA-B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| TRAF6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MCC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| VCAM1 | psi-mi:"MI:0030"(cross-linking study) | imex:IM-17358|pubmed:22623428 |
| GRB2 | psi-mi:"MI:0018"(two hybrid) | pubmed:18624398|imex:IM-19021 |
| DDA1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| HDAC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-18733|pubmed:23752268 |
| SMARCB1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-26463|pubmed:30108113 |
| LRRK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31046837|imex:IM-26684 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=98.2 + PDB: 3FCX | pLDDT=98.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasmic vesicle / Golgi apparatus; 额外: Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. ESD — S-formylglutathione hydrolase，研究基础较多，新颖性有限。
2. 蛋白大小282 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 446 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 446 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P10768
- Protein Atlas: https://www.proteinatlas.org/ENSG00000139684-ESD/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ESD
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P10768
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P10768-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P10768 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR029058;IPR000801;IPR014186; |
| Pfam | PF00756; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000139684-ESD/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| FSD2 | Intact, Biogrid | true |
| GAPDH | Biogrid, Opencell | true |
| ACADM | Opencell | false |
| ACO2 | Biogrid | false |
| ACTR2 | Opencell | false |
| DCTN1 | Opencell | false |
| DIAPH2 | Opencell | false |
| HEATR3 | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
