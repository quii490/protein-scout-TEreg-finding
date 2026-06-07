---
type: protein-evaluation
gene: "ST6GALNAC4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ST6GALNAC4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ST6GALNAC4 / SIAT3C, SIAT7D |
| 蛋白名称 | Alpha-N-acetyl-neuraminyl-2,3-beta-galactosyl-1,3-N-acetyl-galactosaminide alpha-2,6-sialyltransferase |
| 蛋白大小 | 302 aa / 34.2 kDa |
| UniProt ID | Q9H4F1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Golgi apparatus; 额外: Nucleoplasm; UniProt: Golgi apparatus membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 302 aa / 34.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=18 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=89.2; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001675, IPR038578; Pfam: PF00777 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.5/180** | |
| **归一化总分** | | | **70.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Nucleoplasm | Approved |
| UniProt | Golgi apparatus membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- Golgi membrane (GO:0000139)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 18 |
| PubMed broad count | 27 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SIAT3C, SIAT7D |

**关键文献**:
1. Multiple-omics analysis of aggrephagy-related cellular patterns and development of an aggrephagy-related signature for hepatocellular carcinoma.. *World journal of surgical oncology*. PMID: 40307857
2. ST6GALNAC4 promotes hepatocellular carcinogenesis by inducing abnormal glycosylation.. *Journal of translational medicine*. PMID: 37381011
3. Identification and Experimental Validation of the Prognostic Significance and Immunological Correlation of Glycosylation-Related Signature and ST6GALNAC4 in Hepatocellular Carcinoma.. *Journal of hepatocellular carcinoma*. PMID: 37034303
4. Prognostic and immunological implications of sialylation-associated gene signatures in hepatocellular carcinoma.. *Annals of medicine*. PMID: 41398172
5. Reduction in disialyl-T antigen levels in mice deficient for both St6galnac3 and St6galnac4 results in blood filling of lymph nodes.. *Scientific reports*. PMID: 37386100

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.2 |
| 高置信度残基 (pLDDT>90) 占比 | 74.2% |
| 置信残基 (pLDDT 70-90) 占比 | 15.6% |
| 中等置信 (pLDDT 50-70) 占比 | 3.6% |
| 低置信 (pLDDT<50) 占比 | 6.6% |
| 有序区域 (pLDDT>70) 占比 | 89.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=89.2，有序区 89.8%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001675, IPR038578; Pfam: PF00777 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ST3GAL1 | 0.941 | 0.000 | — |
| ST3GAL2 | 0.936 | 0.000 | — |
| AHSG | 0.825 | 0.000 | — |
| ST8SIA2 | 0.788 | 0.000 | — |
| MUC1 | 0.561 | 0.000 | — |
| ST6GALNAC2 | 0.560 | 0.000 | — |
| C1GALT1 | 0.557 | 0.000 | — |
| GCNT3 | 0.554 | 0.000 | — |
| MUC16 | 0.501 | 0.000 | — |
| MUC4 | 0.501 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SPATA20 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| KLRG2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| VTN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FBXO2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PTCH1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| HSPA5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CLTCL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TRIP6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| GALNT10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| OR6C4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.2 + PDB: 无 | pLDDT=89.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus membrane / Golgi apparatus; 额外: Nucleoplasm | 一致 |
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
1. ST6GALNAC4 — Alpha-N-acetyl-neuraminyl-2,3-beta-galactosyl-1,3-N-acetyl-galactosaminide alpha-2,6-sialyltransferase，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小302 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 18 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H4F1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000136840-ST6GALNAC4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ST6GALNAC4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H4F1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (approved)。来源: https://www.proteinatlas.org/ENSG00000136840-ST6GALNAC4/subcellular

![](https://images.proteinatlas.org/9042/1144_B3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/9042/1144_B3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/9042/47_G4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/9042/47_G4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/9042/48_G4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/9042/48_G4_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H4F1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H4F1 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR001675;IPR038578; |
| Pfam | PF00777; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000136840-ST6GALNAC4/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| FBXO2 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
