---
type: protein-evaluation
gene: "TRMT11"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TRMT11 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TRMT11 / C6orf75 |
| 蛋白名称 | tRNA (guanine(10)-N(2))-methyltransferase TRMT11 |
| 蛋白大小 | 463 aa / 53.4 kDa |
| UniProt ID | Q7Z4G4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nuclear bodies; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 463 aa / 53.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=11 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=88.4; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR002052, IPR000241, IPR029063, IPR016691, IPR059 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.5/180** | |
| **归一化总分** | | | **70.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- mitochondrion (GO:0005739)
- tRNA (m2G10) methyltransferase complex (GO:0043528)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11 |
| PubMed broad count | 13 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C6orf75 |

**关键文献**:
1. N 2-methylguanosine modifications on human tRNAs and snRNA U6 are important for cell proliferation, protein translation and pre-mRNA splicing.. *Nucleic acids research*. PMID: 37283053
2. Mitochondrial RNA modification-based signature to predict prognosis of lower grade glioma: a multi-omics exploration and verification study.. *Scientific reports*. PMID: 38824202
3. Germline predictors of androgen deprivation therapy response in advanced prostate cancer.. *Mayo Clinic proceedings*. PMID: 22386179
4. Downregulation of LRRC19 Is Associated with Poor Prognosis in Colorectal Cancer.. *Journal of oncology*. PMID: 35794979
5. Identification of recurrent fusion genes across multiple cancer types.. *Scientific reports*. PMID: 30705370

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.4 |
| 高置信度残基 (pLDDT>90) 占比 | 68.7% |
| 置信残基 (pLDDT 70-90) 占比 | 19.2% |
| 中等置信 (pLDDT 50-70) 占比 | 9.3% |
| 低置信 (pLDDT<50) 占比 | 2.8% |
| 有序区域 (pLDDT>70) 占比 | 87.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=88.4，有序区 87.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002052, IPR000241, IPR029063, IPR016691, IPR059073; Pfam: PF25904, PF01170 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TRMT112 | 0.999 | 0.835 | — |
| TRMT1 | 0.885 | 0.088 | — |
| BUD23 | 0.847 | 0.099 | — |
| WDR36 | 0.836 | 0.000 | — |
| DUS1L | 0.821 | 0.000 | — |
| N6AMT1 | 0.814 | 0.000 | — |
| TRMT61A | 0.806 | 0.000 | — |
| TRMT6 | 0.788 | 0.099 | — |
| METTL1 | 0.772 | 0.099 | — |
| ALKBH8 | 0.769 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| WDR48 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| HSPD1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| MGST3 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| TRMT61B | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| RPL27A | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| DCDC2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PDK1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| HSCB | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28380382|imex:IM-25655 |
| LHX4 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| VTN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.4 + PDB: 无 | pLDDT=88.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Nuclear bodies | 一致 |
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
1. TRMT11 — tRNA (guanine(10)-N(2))-methyltransferase TRMT11，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小463 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 11 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7Z4G4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000066651-TRMT11/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TRMT11
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7Z4G4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (approved)。来源: https://www.proteinatlas.org/ENSG00000066651-TRMT11/subcellular

![](https://images.proteinatlas.org/30473/1466_A10_3_red_green.jpg)
![](https://images.proteinatlas.org/30473/1466_A10_4_red_green.jpg)
![](https://images.proteinatlas.org/30473/1521_A10_3_red_green.jpg)
![](https://images.proteinatlas.org/30473/1521_A10_4_red_green.jpg)
![](https://images.proteinatlas.org/30473/1528_B12_1_red_green.jpg)
![](https://images.proteinatlas.org/30473/1528_B12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q7Z4G4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q7Z4G4 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR002052;IPR000241;IPR029063;IPR016691;IPR059073; |
| Pfam | PF25904;PF01170; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000066651-TRMT11/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DCDC2 | Intact | false |
| HSPD1 | Biogrid | false |
| LHX4 | Intact | false |
| TRMT112 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
