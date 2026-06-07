---
type: protein-evaluation
gene: "TENT5A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TENT5A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TENT5A / C6orf37, FAM46A, XTP11 |
| 蛋白名称 | Terminal nucleotidyltransferase 5A |
| 蛋白大小 | 442 aa / 49.7 kDa |
| UniProt ID | Q96IP4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 442 aa / 49.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=79.6; PDB: 8EXE, 8EXF |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR012937; Pfam: PF07984 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.0/180** | |
| **归一化总分** | | | **71.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 36 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C6orf37, FAM46A, XTP11 |

**关键文献**:
1. Update on the Genetics of Osteogenesis Imperfecta.. *Calcified tissue international*. PMID: 39127989
2. TENT5A mediates the cancer-inhibiting effects of EGR1 by suppressing the protein stability of RPL35 in hepatocellular carcinoma.. *Cellular oncology (Dordrecht, Netherlands)*. PMID: 39570560
3. TENT5-mediated polyadenylation of mRNAs encoding secreted proteins is essential for gametogenesis in mice.. *Nature communications*. PMID: 38909026
4. 3' RNA Uridylation in Epitranscriptomics, Gene Regulation, and Disease.. *Frontiers in molecular biosciences*. PMID: 30057901
5. Tent5a modulates muscle fiber formation in adolescent idiopathic scoliosis via maintenance of myogenin expression.. *Cell proliferation*. PMID: 35137485

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.6 |
| 高置信度残基 (pLDDT>90) 占比 | 60.4% |
| 置信残基 (pLDDT 70-90) 占比 | 14.0% |
| 中等置信 (pLDDT 50-70) 占比 | 6.6% |
| 低置信 (pLDDT<50) 占比 | 19.0% |
| 有序区域 (pLDDT>70) 占比 | 74.4% |
| 可用 PDB 条目 | 8EXE, 8EXF |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（8EXE, 8EXF）+ AlphaFold高质量预测（pLDDT=79.6），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR012937; Pfam: PF07984 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ELOVL4 | 0.922 | 0.000 | — |
| BCCIP | 0.808 | 0.538 | — |
| MTO1 | 0.660 | 0.234 | — |
| TRAFD1 | 0.574 | 0.173 | — |
| TMEM38B | 0.573 | 0.000 | — |
| FNDC3B | 0.569 | 0.422 | — |
| ZFYVE9 | 0.565 | 0.132 | — |
| IFITM5 | 0.511 | 0.000 | — |
| FAM214B | 0.508 | 0.000 | — |
| CRTAP | 0.507 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ATXN1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| CD93 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| TMEM131L | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| EIF4G3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| WDR62 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| POLR1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| POLR2J | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| POLE2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HDLBP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| USP4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.6 + PDB: 8EXE, 8EXF | pLDDT=79.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoplasm; 额外: Cytosol | 一致 |
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
1. TENT5A — Terminal nucleotidyltransferase 5A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小442 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96IP4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000112773-TENT5A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TENT5A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96IP4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000112773-TENT5A/subcellular

![](https://images.proteinatlas.org/51067/1027_B12_3_red_green.jpg)
![](https://images.proteinatlas.org/51067/1027_B12_8_red_green.jpg)
![](https://images.proteinatlas.org/51067/740_G1_1_red_green.jpg)
![](https://images.proteinatlas.org/51067/740_G1_2_red_green.jpg)
![](https://images.proteinatlas.org/51067/784_G1_1_red_green.jpg)
![](https://images.proteinatlas.org/51067/784_G1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96IP4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96IP4 |
| SMART | SM01153; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR012937; |
| Pfam | PF07984; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000112773-TENT5A/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ATXN1 | Intact, Biogrid | true |
| SH2D2A | Intact, Biogrid | true |
| SYK | Intact, Biogrid | true |
| BCCIP | Biogrid | false |
| DCAF6 | Biogrid | false |
| FNDC3A | Biogrid | false |
| FNDC3B | Biogrid | false |
| HDLBP | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
