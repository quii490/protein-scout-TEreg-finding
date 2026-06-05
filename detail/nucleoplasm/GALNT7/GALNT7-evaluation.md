---
type: protein-evaluation
gene: "GALNT7"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GALNT7 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GALNT7 |
| 蛋白名称 | N-acetylgalactosaminyltransferase 7 |
| 蛋白大小 | 657 aa / 75.4 kDa |
| UniProt ID | Q86SF2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Golgi apparatus; 额外: Nucleoplasm; UniProt: Golgi apparatus membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 657 aa / 75.4 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=39 篇 (≤40→8) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=87.7; PDB: 6IWQ, 6IWR |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR045885, IPR001173, IPR029044, IPR035992, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.0/180** | |
| **归一化总分** | | | **66.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Nucleoplasm | Approved |
| UniProt | Golgi apparatus membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- extracellular exosome (GO:0070062)
- Golgi apparatus (GO:0005794)
- Golgi membrane (GO:0000139)
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 39 |
| PubMed broad count | 66 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Glycosylation-Related Genes and Prognostic Signatures in Diabetic Nephropathy.. *International journal of general medicine*. PMID: 41311665
2. GALNT7 Stratifies dMMR/MSI Colorectal Cancer into Distinct Molecular Subsets Associated with Prognosis and PD-L1 Expression.. *Cancer research communications*. PMID: 40824763
3. MicroRNA-214 suppresses growth and invasiveness of cervical cancer cells by targeting UDP-N-acetyl-α-D-galactosamine:polypeptide N-acetylgalactosaminyltransferase 7.. *The Journal of biological chemistry*. PMID: 22399294
4. Prenatal Cadmium Exposure Alters Proliferation in Mouse CD4(+) T Cells via LncRNA Snhg7.. *Frontiers in immunology*. PMID: 35087510
5. Genome-Wide Study of Diabetes Mellitus (Type 2)-Associated Genes in Homo sapiens (Human).. *The journal of gene medicine*. PMID: 40462586

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.7 |
| 高置信度残基 (pLDDT>90) 占比 | 77.3% |
| 置信残基 (pLDDT 70-90) 占比 | 8.4% |
| 中等置信 (pLDDT 50-70) 占比 | 2.1% |
| 低置信 (pLDDT<50) 占比 | 12.2% |
| 有序区域 (pLDDT>70) 占比 | 85.7% |
| 可用 PDB 条目 | 6IWQ, 6IWR |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（6IWQ, 6IWR）+ AlphaFold高质量预测（pLDDT=87.7），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR045885, IPR001173, IPR029044, IPR035992, IPR000772; Pfam: PF00535, PF00652 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GCNT1 | 0.925 | 0.000 | — |
| ST6GALNAC1 | 0.920 | 0.000 | — |
| B3GNT6 | 0.913 | 0.000 | — |
| C1GALT1 | 0.771 | 0.000 | — |
| GALNT4 | 0.755 | 0.691 | — |
| C1GALT1C1 | 0.711 | 0.000 | — |
| C1GALT1C1L | 0.708 | 0.000 | — |
| GALNT12 | 0.616 | 0.521 | — |
| MUC1 | 0.460 | 0.000 | — |
| ADPGK | 0.459 | 0.456 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MAPK6 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| MME | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ANTXR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DEFA5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TCTN2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NCEH1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| REEP5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GAA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SLC9A1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MAN2A2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.7 + PDB: 6IWQ, 6IWR | pLDDT=87.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Golgi apparatus membrane / Golgi apparatus; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. GALNT7 — N-acetylgalactosaminyltransferase 7，非常新颖，仅有少数基础研究。
2. 蛋白大小657 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 39 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86SF2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000109586-GALNT7/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GALNT7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86SF2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/GALNT7/IF_images/1591_G8_3_blue_red_green.jpg]]
![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/GALNT7/IF_images/1591_G8_2_blue_red_green.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (approved)。来源: https://www.proteinatlas.org/ENSG00000109586-GALNT7/subcellular

![](https://images.proteinatlas.org/64243/1283_A3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/64243/1283_A3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/64243/1591_G8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/64243/1591_G8_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/65317/1283_E6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/65317/1283_E6_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86SF2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
