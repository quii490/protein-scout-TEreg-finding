---
type: protein-evaluation
gene: "HEATR3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## HEATR3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HEATR3 |
| 蛋白名称 | HEAT repeat-containing protein 3 |
| 蛋白大小 | 680 aa / 74.6 kDa |
| UniProt ID | Q7Z4Q2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 680 aa / 74.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=83.1; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011989, IPR016024, IPR052616, IPR057990; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **135.0/180** | |
| **归一化总分** | | | **75.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 18 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. DBA Syndrome.. **. PMID: 20301769
2. A Trans-Ethnic Genome-Wide Association Study of Uterine Fibroids.. *Frontiers in genetics*. PMID: 31249589
3. HEATR3 variants impair nuclear import of uL18 (RPL5) and drive Diamond-Blackfan anemia.. *Blood*. PMID: 35213692
4. HEATR3 recognizes membrane rupture and facilitates xenophagy in response to Salmonella invasion.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 40178893
5. HEATR3 involved in the cell proliferation, metastasis and cell cycle development of bladder cancer acts as a tumor suppressor.. *Molecular genetics and genomics : MGG*. PMID: 37518364

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.1 |
| 高置信度残基 (pLDDT>90) 占比 | 65.6% |
| 置信残基 (pLDDT 70-90) 占比 | 16.0% |
| 中等置信 (pLDDT 50-70) 占比 | 3.1% |
| 低置信 (pLDDT<50) 占比 | 15.3% |
| 有序区域 (pLDDT>70) 占比 | 81.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=83.1，有序区 81.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011989, IPR016024, IPR052616, IPR057990; Pfam: PF13513, PF25567 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RPL5 | 0.943 | 0.510 | — |
| RPL11 | 0.902 | 0.439 | — |
| GRWD1 | 0.829 | 0.000 | — |
| RPF2 | 0.806 | 0.268 | — |
| TSR2 | 0.717 | 0.000 | — |
| SSX2 | 0.697 | 0.000 | — |
| SSX1 | 0.653 | 0.000 | — |
| RRS1 | 0.649 | 0.268 | — |
| SS18 | 0.596 | 0.000 | — |
| TSR1 | 0.568 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TRAF6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MYC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| GSTK1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| PTP4A3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| 616370" | psi-mi:"MI:0096"(pull down) | pubmed:23606334|imex:IM-21247 |
| TMEM186 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LRRK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31046837|imex:IM-26684 |
| NONO | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| UNC93B1 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| DISC1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.1 + PDB: 无 | pLDDT=83.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Cytosol | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. HEATR3 — HEAT repeat-containing protein 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小680 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7Z4Q2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000155393-HEATR3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HEATR3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7Z4Q2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000155393-HEATR3/subcellular

![](https://images.proteinatlas.org/58579/2268_C8_15_blue_red_green.jpg)
![](https://images.proteinatlas.org/58579/2268_C8_35_blue_red_green.jpg)
![](https://images.proteinatlas.org/58579/1100_C5_1_red_green.jpg)
![](https://images.proteinatlas.org/58579/1100_C5_2_red_green.jpg)
![](https://images.proteinatlas.org/58579/1308_C5_3_red_green.jpg)
![](https://images.proteinatlas.org/58579/1308_C5_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q7Z4Q2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q7Z4Q2 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR011989;IPR016024;IPR052616;IPR057990; |
| Pfam | PF13513;PF25567; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000155393-HEATR3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| RPL11 | Biogrid, Opencell | true |
| RPL5 | Biogrid, Opencell, Bioplex | true |
| ACADM | Opencell | false |
| ACAT1 | Opencell | false |
| AIFM1 | Opencell | false |
| ALDH1B1 | Opencell | false |
| ATP5PF | Opencell | false |
| ATP5PO | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
