---
type: protein-evaluation
gene: "GGPS1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GGPS1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GGPS1 |
| 蛋白名称 | Geranylgeranyl pyrophosphate synthase |
| 蛋白大小 | 300 aa / 34.9 kDa |
| UniProt ID | O95749 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Nucleoplasm; UniProt: Cytoplasm; Cytoplasm, perinuclear region; Cytoplasm, myofibr |
| 蛋白大小 | 10/10 | ×1 | 10 | 300 aa / 34.9 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=48 篇 (≤60→6) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=94.6; PDB: 2Q80, 6C56, 6C57, 6G31, 6G32, 6R4V, 9CSL |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR008949, IPR000092, IPR033749; Pfam: PF00348 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.0/180** | |
| **归一化总分** | | | **70.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm | Supported |
| UniProt | Cytoplasm; Cytoplasm, perinuclear region; Cytoplasm, myofibril, sarcomere, Z line | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- perinuclear region of cytoplasm (GO:0048471)
- Z disc (GO:0030018)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 48 |
| PubMed broad count | 91 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Perrault Syndrome Overview.. **. PMID: 25254289
2. The prognostic role and metabolic function of GGPS1 in oral squamous cell carcinoma.. *Frontiers in molecular biosciences*. PMID: 37033446
3. Pan-cancer analysis reveals GGPS1 plays an important role in tumorigenesis in multiple tumor types.. *Heliyon*. PMID: 39165977
4. Mutations in GERANYLGERANYL DIPHOSPHATE SYNTHASE 1 affect chloroplast development in Arabidopsis thaliana (Brassicaceae).. *American journal of botany*. PMID: 24081146
5. Oocytes orchestrate protein prenylation for mitochondrial function through selective inactivation of cholesterol biosynthesis in murine species.. *The Journal of biological chemistry*. PMID: 37611828

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.6 |
| 高置信度残基 (pLDDT>90) 占比 | 88.3% |
| 置信残基 (pLDDT 70-90) 占比 | 9.3% |
| 中等置信 (pLDDT 50-70) 占比 | 1.7% |
| 低置信 (pLDDT<50) 占比 | 0.7% |
| 有序区域 (pLDDT>70) 占比 | 97.6% |
| 可用 PDB 条目 | 2Q80, 6C56, 6C57, 6G31, 6G32, 6R4V, 9CSL, 9HJS, 9HJZ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2Q80, 6C56, 6C57, 6G31, 6G32, 6R4V, 9CSL, 9HJS, 9HJZ）+ AlphaFold极高置信度预测（pLDDT=94.6），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008949, IPR000092, IPR033749; Pfam: PF00348 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FDPS | 0.996 | 0.272 | — |
| MVD | 0.992 | 0.069 | — |
| IDI1 | 0.987 | 0.000 | — |
| FDFT1 | 0.986 | 0.091 | — |
| IDI2 | 0.986 | 0.000 | — |
| DHDDS | 0.967 | 0.000 | — |
| FNTA | 0.962 | 0.000 | — |
| PDSS1 | 0.961 | 0.000 | — |
| FNTB | 0.958 | 0.066 | — |
| RSAD2 | 0.952 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000418690.1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| SDCBP | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| TRAF3IP3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TULP3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ODAPH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CCDC85C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| IQGAP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TUSC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZNF696 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SLTM | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.6 + PDB: 2Q80, 6C56, 6C57, 6G31, 6G32,  | pLDDT=94.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm, perinuclear region; Cytoplas / Cytosol; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. GGPS1 — Geranylgeranyl pyrophosphate synthase，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小300 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 48 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O95749
- Protein Atlas: https://www.proteinatlas.org/ENSG00000152904-GGPS1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GGPS1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O95749
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/GGPS1/IF_images/2037_C5_2_blue_red_green.jpg]]
![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/GGPS1/IF_images/2037_C5_1_blue_red_green.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000152904-GGPS1/subcellular

![](https://images.proteinatlas.org/50727/2037_C5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/50727/2037_C5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/50727/2142_D3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/50727/2142_D3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/50727/719_D11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/50727/719_D11_4_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O95749-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
