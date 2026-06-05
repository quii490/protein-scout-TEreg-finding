---
type: protein-evaluation
gene: "CRX"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CRX — REJECTED (研究热度过高 (PubMed strict=519，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CRX / CORD2 |
| 蛋白名称 | Cone-rod homeobox protein |
| 蛋白大小 | 299 aa / 32.3 kDa |
| UniProt ID | O43186 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoli fibrillar center; 额外: Nucleoplasm, Primary cilium, ; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 299 aa / 32.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=519 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.5; PDB: 9B8U |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001356, IPR017970, IPR009057, IPR013851; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.5/180** | |
| **归一化总分** | | | **49.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli fibrillar center; 额外: Nucleoplasm, Primary cilium, Cytosol | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)
- RNA polymerase II transcription regulator complex (GO:0090575)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 519 |
| PubMed broad count | 879 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CORD2 |

**关键文献**:
1. Genetic characteristics of retinitis pigmentosa in 1204 Japanese patients.. *Journal of medical genetics*. PMID: 31213501
2. Leber congenital amaurosis.. *Molecular genetics and metabolism*. PMID: 10527670
3. Structural and functional analysis of the human cone-rod homeobox transcription factor.. *Proteins*. PMID: 35255174
4. Gene Augmentation for Autosomal Dominant CRX-Associated Retinopathies.. *Advances in experimental medicine and biology*. PMID: 37440026
5. Nonsyndromic Leber Congenital Amaurosis / Early-Onset Severe Retinal Dystrophy Overview.. **. PMID: 30285347

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.5 |
| 高置信度残基 (pLDDT>90) 占比 | 19.1% |
| 置信残基 (pLDDT 70-90) 占比 | 3.3% |
| 中等置信 (pLDDT 50-70) 占比 | 37.8% |
| 低置信 (pLDDT<50) 占比 | 39.8% |
| 有序区域 (pLDDT>70) 占比 | 22.4% |
| 可用 PDB 条目 | 9B8U |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=60.5），有序残基占 22.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001356, IPR017970, IPR009057, IPR013851; Pfam: PF00046, PF03529 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NRL | 0.990 | 0.322 | — |
| NR2E3 | 0.972 | 0.329 | — |
| RHO | 0.937 | 0.000 | — |
| AIPL1 | 0.928 | 0.000 | — |
| ATXN7 | 0.922 | 0.514 | — |
| RCVRN | 0.914 | 0.000 | — |
| TPRX1 | 0.885 | 0.091 | — |
| GUCY2D | 0.882 | 0.000 | — |
| RPE65 | 0.875 | 0.000 | — |
| FIZ1 | 0.864 | 0.051 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| M1AP | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MDFI | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| M | psi-mi:"MI:0018"(two hybrid) | imex:IM-13585|pubmed:20064372 |
| ABI2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:29892012|doi:10.1038/s4 |
| GCM2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:29892012|doi:10.1038/s4 |
| CA8 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| SOX5 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| ROR2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| PRKAB2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| PPP1R16B | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.5 + PDB: 9B8U | pLDDT=60.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoli fibrillar center; 额外: Nucleoplasm, Primar | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CRX — Cone-rod homeobox protein，研究基础较多，新颖性有限。
2. 蛋白大小299 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 519 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=60.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 519 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O43186
- Protein Atlas: https://www.proteinatlas.org/ENSG00000105392-CRX/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CRX
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O43186
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli fibrillar center (approved)。来源: https://www.proteinatlas.org/ENSG00000105392-CRX/subcellular

![](https://images.proteinatlas.org/36763/542_E11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/36763/542_E11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/36763/544_E11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/36763/544_E11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/36763/571_E11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/36763/571_E11_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O43186-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
