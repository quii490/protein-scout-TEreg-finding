---
type: protein-evaluation
gene: "FBXO28"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FBXO28 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FBXO28 / CENP-30, KIAA0483 |
| 蛋白名称 | F-box only protein 28 |
| 蛋白大小 | 368 aa / 41.1 kDa |
| UniProt ID | Q9NVF7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: Nucleoplasm; 额外: Focal adhesion sites; UniProt: Chromosome, centromere, kinetochore; Nucleus; Chromosome |
| 蛋白大小 | 10/10 | ×1 | 10 | 368 aa / 41.1 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=33 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=76.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036047, IPR001810, IPR039719; Pfam: PF00646 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **127.5/180** | |
| **归一化总分** | | | **70.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Focal adhesion sites | Supported |
| UniProt | Chromosome, centromere, kinetochore; Nucleus; Chromosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- kinetochore (GO:0000776)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 33 |
| PubMed broad count | 45 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CENP-30, KIAA0483 |

**关键文献**:
1. FBXO28 suppresses liver cancer invasion and metastasis by promoting PKA-dependent SNAI2 degradation.. *Oncogene*. PMID: 37596321
2. SCF(FBXO28)-mediated self-ubiquitination of FBXO28 promotes its degradation.. *Cellular signalling*. PMID: 31678254
3. Role for the F-box proteins in heart diseases.. *Pharmacological research*. PMID: 39577754
4. FBXO28 promotes proliferation, invasion, and metastasis of pancreatic cancer cells through regulation of SMARCC2 ubiquitination.. *Aging*. PMID: 37348029
5. MYC Modulation around the CDK2/p27/SKP2 Axis.. *Genes*. PMID: 28665315

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.0 |
| 高置信度残基 (pLDDT>90) 占比 | 51.1% |
| 置信残基 (pLDDT 70-90) 占比 | 12.8% |
| 中等置信 (pLDDT 50-70) 占比 | 8.2% |
| 低置信 (pLDDT<50) 占比 | 28.0% |
| 有序区域 (pLDDT>70) 占比 | 63.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=76.0，有序区 63.9%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036047, IPR001810, IPR039719; Pfam: PF00646 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SKP1 | 0.943 | 0.796 | — |
| CUL1 | 0.942 | 0.781 | — |
| KLHL28 | 0.679 | 0.000 | — |
| ARHGEF6 | 0.615 | 0.615 | — |
| FBXO34 | 0.597 | 0.000 | — |
| RNF166 | 0.584 | 0.000 | — |
| PAK2 | 0.551 | 0.510 | — |
| FAM199X | 0.535 | 0.000 | — |
| FBXO45 | 0.514 | 0.000 | — |
| SPRTN | 0.509 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000355827.5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TRAF2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| GK | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| Cep55 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| PAK1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-17578|pubmed:23455922 |
| SKP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:22632967|imex:IM-17368 |
| HSP90AB1 | psi-mi:"MI:0729"(luminescence based mammalian inte | imex:IM-17906|pubmed:22939624| |
| CKAP4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NEDD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| EML1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.0 + PDB: 无 | pLDDT=76.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Chromosome, centromere, kinetochore; Nucleus; Chro / Nucleoplasm; 额外: Focal adhesion sites | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. FBXO28 — F-box only protein 28，非常新颖，仅有少数基础研究。
2. 蛋白大小368 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 33 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NVF7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000143756-FBXO28/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FBXO28
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NVF7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FBXO28/IF_images/A-431_1.jpg]]
![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FBXO28/IF_images/U-251MG_1.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000143756-FBXO28/subcellular

![](https://images.proteinatlas.org/3289/1772_B8_1_red_green.jpg)
![](https://images.proteinatlas.org/3289/1772_B8_4_red_green.jpg)
![](https://images.proteinatlas.org/3289/79_A8_1_red_green.jpg)
![](https://images.proteinatlas.org/3289/79_A8_2_red_green.jpg)
![](https://images.proteinatlas.org/3289/80_A8_1_red_green.jpg)
![](https://images.proteinatlas.org/3289/80_A8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NVF7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
