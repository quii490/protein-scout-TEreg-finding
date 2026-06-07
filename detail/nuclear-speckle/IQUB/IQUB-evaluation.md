---
type: protein-evaluation
gene: "IQUB"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## IQUB 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | IQUB |
| 蛋白名称 | IQ motif and ubiquitin-like domain-containing protein |
| 蛋白大小 | 791 aa / 92.6 kDa |
| UniProt ID | Q8NA54 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nuclear speckles, Mid piece, Principal piece, End piece; 额外:; UniProt: Cytoplasm, cytoskeleton, flagellum axoneme; Cell projection, |
| 蛋白大小 | 10/10 | ×1 | 10 | 791 aa / 92.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=75.3; PDB: 2DAF, 8J07 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR037695, IPR057887, IPR000626, IPR029071; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.0/180** | |
| **归一化总分** | | | **71.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles, Mid piece, Principal piece, End piece; 额外: Nucleoplasm, Cytosol | Approved |
| UniProt | Cytoplasm, cytoskeleton, flagellum axoneme; Cell projection, cilium | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 9+2 motile cilium (GO:0097729)
- acrosomal vesicle (GO:0001669)
- motile cilium (GO:0031514)
- radial spoke (GO:0001534)
- sperm flagellum (GO:0036126)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 18 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. IQUB deficiency causes male infertility by affecting the activity of p-ERK1/2/RSPH3.. *Human reproduction (Oxford, England)*. PMID: 36355624
2. IQUB mutation induces radial spoke 1 deficiency causing asthenozoospermia with normal sperm morphology in humans and mice.. *Cell communication and signaling : CCS*. PMID: 39849482
3. Combining bioinformatics, network pharmacology and artificial intelligence to predict the mechanism of celastrol in the treatment of type 2 diabetes.. *Frontiers in endocrinology*. PMID: 36339449
4. Differential requirements of IQUB for the assembly of radial spoke 1 and the motility of mouse cilia and flagella.. *Cell reports*. PMID: 36417862
5. Transcriptome-wide profile of 1α,25 dihydroxyvitamin D(3) in HTR-8/SVneo cells.. *The journal of obstetrics and gynaecology research*. PMID: 37277920

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.3 |
| 高置信度残基 (pLDDT>90) 占比 | 26.5% |
| 置信残基 (pLDDT 70-90) 占比 | 45.0% |
| 中等置信 (pLDDT 50-70) 占比 | 11.9% |
| 低置信 (pLDDT<50) 占比 | 16.6% |
| 有序区域 (pLDDT>70) 占比 | 71.5% |
| 可用 PDB 条目 | 2DAF, 8J07 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2DAF, 8J07）+ AlphaFold高质量预测（pLDDT=75.3），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR037695, IPR057887, IPR000626, IPR029071; Pfam: PF25805, PF00240 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ARMC4 | 0.692 | 0.265 | — |
| ARMC3 | 0.678 | 0.265 | — |
| DNALI1 | 0.658 | 0.315 | — |
| EFCAB1 | 0.646 | 0.126 | — |
| C4orf47 | 0.642 | 0.000 | — |
| ANKRD42 | 0.624 | 0.091 | — |
| CCDC96 | 0.606 | 0.073 | — |
| IQCD | 0.597 | 0.000 | — |
| C9orf116 | 0.558 | 0.053 | — |
| RSPH9 | 0.551 | 0.183 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000417769.1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| proA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| BTBD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TLR6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| IHO1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| TRIM23 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| TRIM54 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| ZNF526 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TRAF6 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| KRT76 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.3 + PDB: 2DAF, 8J07 | pLDDT=75.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, flagellum axoneme; Cell p / Nuclear speckles, Mid piece, Principal piece, End  | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. IQUB — IQ motif and ubiquitin-like domain-containing protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小791 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NA54
- Protein Atlas: https://www.proteinatlas.org/ENSG00000164675-IQUB/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=IQUB
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NA54
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (approved)。来源: https://www.proteinatlas.org/ENSG00000164675-IQUB/subcellular

![](https://images.proteinatlas.org/49626/2217_D5_13_blue_red_green.jpg)
![](https://images.proteinatlas.org/49626/2217_D5_9_blue_red_green.jpg)
![](https://images.proteinatlas.org/49626/1789_F3_20_cr598d919867186_red_green.jpg)
![](https://images.proteinatlas.org/49626/1789_F3_29_cr596f1f58dd5ed_red_green.jpg)
![](https://images.proteinatlas.org/49626/2042_G4_2_red_green.jpg)
![](https://images.proteinatlas.org/49626/2042_G4_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8NA54-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8NA54 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 131..207; /note="Ubiquitin-like"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00214"; DOMAIN 338..367; /note="IQ" |
| InterPro | IPR037695;IPR057887;IPR000626;IPR029071; |
| Pfam | PF25805;PF00240; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000164675-IQUB/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| MDFI | Intact, Biogrid | true |
| ALX4 | Intact | false |
| ANKRD23 | Intact | false |
| BLZF1 | Intact | false |
| CALCOCO2 | Intact | false |
| CEP70 | Intact | false |
| CEP76 | Intact | false |
| CYSRT1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
