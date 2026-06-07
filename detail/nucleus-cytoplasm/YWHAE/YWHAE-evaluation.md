---
type: protein-evaluation
gene: "YWHAE"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## YWHAE — REJECTED (研究热度过高 (PubMed strict=254，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | YWHAE |
| 蛋白名称 | 14-3-3 protein epsilon |
| 蛋白大小 | 255 aa / 29.2 kDa |
| UniProt ID | P62258 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Nucleus; Cytoplasm; Melanosome |
| 蛋白大小 | 10/10 | ×1 | 10 | 255 aa / 29.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=254 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=92.9; PDB: 2BR9, 3UAL, 3UBW, 6EIH, 7C8E, 7V9B, 8DGM |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000308, IPR023409, IPR036815, IPR023410; Pfam:  |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **92.5/180** | |
| **归一化总分** | | | **51.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm; Melanosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- endoplasmic reticulum (GO:0005783)
- extracellular exosome (GO:0070062)
- focal adhesion (GO:0005925)
- melanosome (GO:0042470)
- membrane (GO:0016020)
- mitochondrial membrane (GO:0031966)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 254 |
| PubMed broad count | 425 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. NAT10-mediated ac(4)C-modified ANKZF1 promotes tumor progression and lymphangiogenesis in clear-cell renal cell carcinoma by attenuating YWHAE-driven cytoplasmic retention of YAP1.. *Cancer communications (London, England)*. PMID: 38407929
2. SPI1-mediated MIR222HG transcription promotes proneural-to-mesenchymal transition of glioma stem cells and immunosuppressive polarization of macrophages.. *Theranostics*. PMID: 37351164
3. The duplication 17p13.3 phenotype: analysis of 21 families delineates developmental, behavioral and brain abnormalities, and rare variant phenotypes.. *American journal of medical genetics. Part A*. PMID: 23813913
4. YWHAE loss of function causes a rare neurodevelopmental disease with brain abnormalities in human and mouse.. *Genetics in medicine : official journal of the American College of Medical Genetics*. PMID: 36999555
5. Deep clinical and genetic analysis of 17p13.3 region: 38 pediatric patients diagnosed using next-generation sequencing and literature review.. *BMC medical genomics*. PMID: 40390087

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.9 |
| 高置信度残基 (pLDDT>90) 占比 | 85.1% |
| 置信残基 (pLDDT 70-90) 占比 | 8.6% |
| 中等置信 (pLDDT 50-70) 占比 | 2.4% |
| 低置信 (pLDDT<50) 占比 | 3.9% |
| 有序区域 (pLDDT>70) 占比 | 93.7% |
| 可用 PDB 条目 | 2BR9, 3UAL, 3UBW, 6EIH, 7C8E, 7V9B, 8DGM, 8DGN, 8DGP, 8DP5 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2BR9, 3UAL, 3UBW, 6EIH, 7C8E, 7V9B, 8DGM, 8DGN, 8DGP, 8DP5）+ AlphaFold极高置信度预测（pLDDT=92.9），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000308, IPR023409, IPR036815, IPR023410; Pfam: PF00244 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000487356.1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| SORBS2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| GPRIN2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MAP3K5 | psi-mi:"MI:0018"(two hybrid) | pubmed:15023544 |
| EGFR | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:15657067 |
| MAP3K3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| RIPK3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| TAB2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| MAP3K1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| CDKN1B | psi-mi:"MI:0096"(pull down) | pubmed:15057270 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.9 + PDB: 2BR9, 3UAL, 3UBW, 6EIH, 7C8E,  | pLDDT=92.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Melanosome / Cytosol | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. YWHAE — 14-3-3 protein epsilon，研究基础较多，新颖性有限。
2. 蛋白大小255 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 254 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 254 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P62258
- Protein Atlas: https://www.proteinatlas.org/ENSG00000108953-YWHAE/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=YWHAE
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P62258
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/YWHAE/IF_images/YWHAE_IF_blue_red_green.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000108953-YWHAE/subcellular

![](https://images.proteinatlas.org/61603/1118_D4_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/61603/1118_D4_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/61603/1153_D4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/61603/1153_D4_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/61603/1319_A11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/61603/1319_A11_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P62258-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P62258 |
| SMART | SM00101; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR000308;IPR023409;IPR036815;IPR023410; |
| Pfam | PF00244; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000108953-YWHAE/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ABL1 | Intact, Biogrid, Opencell | true |
| ABLIM1 | Intact, Biogrid, Opencell | true |
| ACTB | Biogrid, Opencell | true |
| AFDN | Biogrid, Opencell | true |
| AKAP13 | Biogrid, Opencell | true |
| ALS2 | Biogrid, Opencell | true |
| ARAF | Intact, Biogrid, Opencell | true |
| ARHGAP32 | Biogrid, Opencell | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
