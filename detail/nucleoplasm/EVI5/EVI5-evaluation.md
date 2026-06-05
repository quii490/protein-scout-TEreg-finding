---
type: protein-evaluation
gene: "EVI5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EVI5 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EVI5 / NB4S |
| 蛋白名称 | Ecotropic viral integration site 5 protein homolog |
| 蛋白大小 | 810 aa / 92.9 kDa |
| UniProt ID | O60447 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Golgi apparatus; 额外: Vesicles; UniProt: Nucleus; Cytoplasm, cytoskeleton, microtubule organizing cen |
| 蛋白大小 | 8/10 | ×1 | 8 | 810 aa / 92.9 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=58 篇 (≤60→6) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=74.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000195, IPR035969, IPR050302; Pfam: PF00566 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.5/180** | |
| **归一化总分** | | | **61.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Vesicles | Approved |
| UniProt | Nucleus; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Cytoplasm, cytoskeleton... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centrosome (GO:0005813)
- cytosol (GO:0005829)
- nucleus (GO:0005634)
- spindle (GO:0005819)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 58 |
| PubMed broad count | 81 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NB4S |

**关键文献**:
1. The Evi5 family in cellular physiology and pathology.. *FEBS letters*. PMID: 23669355
2. Endocytosis restricts dendrite branching via removing ectopically localized branching ligands.. *Nature communications*. PMID: 39511227
3. EVI5 is a novel centrosomal protein that binds to alpha- and gamma-tubulin.. *Genomics*. PMID: 16033705
4. EVI5 protein associates with the INCENP-aurora B kinase-survivin chromosomal passenger complex and is involved in the completion of cytokinesis.. *Experimental cell research*. PMID: 16764853
5. EVI5 is an oncogene that regulates the proliferation and metastasis of NSCLC cells.. *Journal of experimental & clinical cancer research : CR*. PMID: 32393392

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.1 |
| 高置信度残基 (pLDDT>90) 占比 | 41.1% |
| 置信残基 (pLDDT 70-90) 占比 | 28.3% |
| 中等置信 (pLDDT 50-70) 占比 | 5.9% |
| 低置信 (pLDDT<50) 占比 | 24.7% |
| 有序区域 (pLDDT>70) 占比 | 69.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=74.1，有序区 69.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000195, IPR035969, IPR050302; Pfam: PF00566 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RAB11A | 0.936 | 0.650 | — |
| FBXO5 | 0.898 | 0.292 | — |
| ODF2 | 0.793 | 0.000 | — |
| PLK1 | 0.778 | 0.425 | — |
| HLA-DRB1 | 0.694 | 0.000 | — |
| NBPF1 | 0.659 | 0.000 | — |
| EIF2AK4 | 0.658 | 0.000 | — |
| GMNN | 0.649 | 0.000 | — |
| HAUS2 | 0.645 | 0.000 | — |
| CNTRL | 0.633 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Rab6 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| pyc | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| FBXO5 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:16439210|imex:IM-11819 |
| PLK1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:16439210|imex:IM-11819 |
| EBI-95286 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| EBI-28983653 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| Rac1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| DLG1 | psi-mi:"MI:0900"(p8 filamentous phage display) | imex:IM-26482|pubmed:30126976 |
| HSP90B1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| HNRNPM | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.1 + PDB: 无 | pLDDT=74.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, cytoskeleton, microtubule orga / Golgi apparatus; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. EVI5 — Ecotropic viral integration site 5 protein homolog，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小810 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 58 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O60447
- Protein Atlas: https://www.proteinatlas.org/ENSG00000067208-EVI5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EVI5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O60447
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (approved)。来源: https://www.proteinatlas.org/ENSG00000067208-EVI5/subcellular

![](https://images.proteinatlas.org/27339/604_D11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/27339/604_D11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/27339/607_D11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/27339/607_D11_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/27339/609_D11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/27339/609_D11_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O60447-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
