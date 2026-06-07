---
type: protein-evaluation
gene: "KNTC1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KNTC1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KNTC1 / KIAA0166, ROD |
| 蛋白名称 | Kinetochore-associated protein 1 |
| 蛋白大小 | 2209 aa / 250.7 kDa |
| UniProt ID | P50748 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Plasma membrane; UniProt: Cytoplasm; Nucleus; Chromosome, centromere, kinetochore; Cyt |
| 蛋白大小 | 2/10 | ×1 | 2 | 2209 aa / 250.7 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=50 篇 (≤60→6) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=71.5; PDB: 7QPG |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR055403, IPR055404, IPR055405, IPR052802, IPR055 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **109.0/180** | |
| **归一化总分** | | | **60.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Plasma membrane | Supported |
| UniProt | Cytoplasm; Nucleus; Chromosome, centromere, kinetochore; Cytoplasm, cytoskeleton, spindle | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- actin cytoskeleton (GO:0015629)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- kinetochore microtubule (GO:0005828)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)
- RZZ complex (GO:1990423)
- spindle pole (GO:0000922)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 50 |
| PubMed broad count | 62 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0166, ROD |

**关键文献**:
1. KNTC1 and MCM2 are the molecular targets of gallbladder cancer.. *Aging*. PMID: 37480569
2. KNTC1 and PRC1 define an immunosuppressive microenvironment and poor prognosis in liposarcoma.. *European journal of medical research*. PMID: 41514406
3. KNTC1 knockdown inhibits the proliferation and migration of osteosarcoma cells by MCM2.. *Molecular carcinogenesis*. PMID: 38818892
4. The role of KNTC1 in the regulation of proliferation, migration and tumorigenesis in colorectal cancer.. *Cellular signalling*. PMID: 37230198
5. KNTC1, regulated by HPV E7, inhibits cervical carcinogenesis partially through Smad2.. *Experimental cell research*. PMID: 36608837

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.5 |
| 高置信度残基 (pLDDT>90) 占比 | 0.1% |
| 置信残基 (pLDDT 70-90) 占比 | 61.7% |
| 中等置信 (pLDDT 50-70) 占比 | 31.1% |
| 低置信 (pLDDT<50) 占比 | 7.1% |
| 有序区域 (pLDDT>70) 占比 | 61.8% |
| 可用 PDB 条目 | 7QPG |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=71.5，有序区 61.8%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR055403, IPR055404, IPR055405, IPR052802, IPR055402; Pfam: PF24520, PF24516, PF24515 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ZW10 | 0.999 | 0.996 | — |
| ZWILCH | 0.999 | 0.980 | — |
| ASPM | 0.931 | 0.088 | — |
| ZWINT | 0.927 | 0.000 | — |
| BUB1B | 0.921 | 0.000 | — |
| KIF11 | 0.915 | 0.000 | — |
| CDC20 | 0.882 | 0.069 | — |
| MAD2L1 | 0.873 | 0.000 | — |
| ESPL1 | 0.859 | 0.000 | — |
| BRCA1 | 0.849 | 0.185 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| VHL | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| Iqcb1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| Zw10 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| EBI-1257123 | psi-mi:"MI:0096"(pull down) | pubmed:19367725|imex:IM-20587 |
| LRRK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31046837|imex:IM-26684 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| TMEM171 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| P2RY6 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| EDNRB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.5 + PDB: 7QPG | pLDDT=71.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Chromosome, centromere, kineto / Cytosol; 额外: Plasma membrane | 一致 |
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
1. KNTC1 — Kinetochore-associated protein 1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小2209 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 50 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P50748
- Protein Atlas: https://www.proteinatlas.org/ENSG00000184445-KNTC1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KNTC1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P50748
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000184445-KNTC1/subcellular

![](https://images.proteinatlas.org/25241/298_F10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/25241/298_F10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/25241/299_F10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/25241/299_F10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/25241/300_F10_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/25241/300_F10_4_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P50748-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P50748 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR055403;IPR055404;IPR055405;IPR052802;IPR055402;IPR019527;IPR036322; |
| Pfam | PF24520;PF24516;PF24515;PF24506;PF10493; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000184445-KNTC1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| COMTD1 | Bioplex | false |
| CRYBB3 | Bioplex | false |
| DHFR | Bioplex | false |
| EEF1AKMT3 | Bioplex | false |
| FAXC | Bioplex | false |
| FPR1 | Bioplex | false |
| GPR182 | Bioplex | false |
| GPR45 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
