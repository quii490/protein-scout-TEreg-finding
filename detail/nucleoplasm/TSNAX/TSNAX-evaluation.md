---
type: protein-evaluation
gene: "TSNAX"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TSNAX 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TSNAX / TRAX |
| 蛋白名称 | Translin-associated protein X |
| 蛋白大小 | 290 aa / 33.1 kDa |
| UniProt ID | Q99598 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Golgi apparatus, Cytosol; UniProt: Cytoplasm, perinuclear region; Golgi apparatus; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 290 aa / 33.1 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=21 篇 (≤40→8) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=82.7; PDB: 3PJA, 3QB5 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR016069, IPR002848, IPR016068, IPR036081; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **132.0/180** | |
| **归一化总分** | | | **73.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Golgi apparatus, Cytosol | Enhanced |
| UniProt | Cytoplasm, perinuclear region; Golgi apparatus; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- endoribonuclease complex (GO:1902555)
- Golgi apparatus (GO:0005794)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- perinuclear region of cytoplasm (GO:0048471)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 21 |
| PubMed broad count | 83 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TRAX |

**关键文献**:
1. DISC1-TSNAX and DAOA genes in major depression and citalopram efficacy.. *Journal of affective disorders*. PMID: 25043320
2. The associations between cognitive functions and TSNAX genetic variations in patients with schizophrenia.. *Pharmacology, biochemistry, and behavior*. PMID: 37030547
3. TSNAXIP1 is required for sperm head formation and male fertility.. *Reproductive medicine and biology*. PMID: 37389156
4. Testis-specific proteins, TSNAXIP1 and 1700010I14RIK, are important for sperm motility and male fertility in mice.. *Andrology*. PMID: 36598146
5. Genetic inactivation of the translin/trax microRNA-degrading enzyme phenocopies the robust adiposity induced by Translin (Tsn) deletion.. *Molecular metabolism*. PMID: 32408014

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.7 |
| 高置信度残基 (pLDDT>90) 占比 | 59.7% |
| 置信残基 (pLDDT 70-90) 占比 | 16.9% |
| 中等置信 (pLDDT 50-70) 占比 | 10.3% |
| 低置信 (pLDDT<50) 占比 | 13.1% |
| 有序区域 (pLDDT>70) 占比 | 76.6% |
| 可用 PDB 条目 | 3PJA, 3QB5 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（3PJA, 3QB5）+ AlphaFold高质量预测（pLDDT=82.7），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016069, IPR002848, IPR016068, IPR036081; Pfam: PF01997 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TSN | 0.999 | 0.997 | — |
| AGO2 | 0.958 | 0.325 | — |
| DISC1 | 0.915 | 0.000 | — |
| TSNAXIP1 | 0.884 | 0.095 | — |
| GOLGA3 | 0.848 | 0.505 | — |
| DICER1 | 0.837 | 0.000 | — |
| KIF2A | 0.813 | 0.774 | — |
| PTGER3 | 0.738 | 0.045 | — |
| C1D | 0.732 | 0.292 | — |
| AGO1 | 0.708 | 0.087 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PBXIP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MRFAP1L1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| GADD45G | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| IKBKE | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EP300 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| CKAP4 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| Q81K27 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| fumC | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| gltA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| uvrA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.7 + PDB: 3PJA, 3QB5 | pLDDT=82.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, perinuclear region; Golgi apparatus; Nu / Nucleoplasm; 额外: Golgi apparatus, Cytosol | 一致 |
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
1. TSNAX — Translin-associated protein X，非常新颖，仅有少数基础研究。
2. 蛋白大小290 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 21 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q99598
- Protein Atlas: https://www.proteinatlas.org/ENSG00000116918-TSNAX/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TSNAX
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q99598
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000116918-TSNAX/subcellular

![](https://images.proteinatlas.org/24613/1800_E5_1_red_green.jpg)
![](https://images.proteinatlas.org/24613/1800_E5_2_red_green.jpg)
![](https://images.proteinatlas.org/24613/1835_B3_1_red_green.jpg)
![](https://images.proteinatlas.org/24613/1835_B3_2_red_green.jpg)
![](https://images.proteinatlas.org/24613/1893_E4_16_cr5bbdefb0846fe_red_green.jpg)
![](https://images.proteinatlas.org/24613/1893_E4_6_cr5bbdefb083e71_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q99598-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q99598 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR016069;IPR002848;IPR016068;IPR036081; |
| Pfam | PF01997; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000116918-TSNAX/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| KLC3 | Intact, Biogrid | true |
| LDB2 | Intact, Biogrid | true |
| PMF1 | Intact, Biogrid | true |
| TSN | Intact, Biogrid, Bioplex | true |
| AIMP1 | Intact | false |
| BEX3 | Intact | false |
| BLOC1S5 | Intact | false |
| C1D | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
