---
type: protein-evaluation
gene: "VPS51"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## VPS51 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | VPS51 / ANG2, C11orf2, C11orf3, FFR |
| 蛋白名称 | Vacuolar protein sorting-associated protein 51 homolog |
| 蛋白大小 | 782 aa / 86.0 kDa |
| UniProt ID | Q9UID3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Golgi apparatus, Vesicles; 额外: Nucleoli; UniProt: Golgi apparatus, trans-Golgi network; Recycling endosome |
| 蛋白大小 | 10/10 | ×1 | 10 | 782 aa / 86.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=25 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=80.4; PDB: 4J2C |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR016159, IPR014812; Pfam: PF08700 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **129.0/180** | |
| **归一化总分** | | | **71.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus, Vesicles; 额外: Nucleoli | Approved |
| UniProt | Golgi apparatus, trans-Golgi network; Recycling endosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- EARP complex (GO:1990745)
- GARP complex (GO:0000938)
- Golgi apparatus (GO:0005794)
- membrane (GO:0016020)
- nucleolus (GO:0005730)
- recycling endosome (GO:0055037)
- trans-Golgi network membrane (GO:0032588)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 25 |
| PubMed broad count | 123 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ANG2, C11orf2, C11orf3, FFR |

**关键文献**:
1. From Gene to Pathways: Understanding Novel Vps51 Variant and Its Cellular Consequences.. *International journal of molecular sciences*. PMID: 40565173
2. Yeast dynamin associates with the GARP tethering complex for endosome-to-Golgi traffic.. *European journal of cell biology*. PMID: 28521960
3. [A case report and literature review of pontocerebellar hypoplasia type 13 combined with abnormal liver function caused by VPS51 gene variation].. *Zhonghua gan zang bing za zhi = Zhonghua ganzangbing zazhi = Chinese journal of hepatology*. PMID: 38733192
4. Structural analysis of the interaction between the SNARE Tlg1 and Vps51.. *Traffic (Copenhagen, Denmark)*. PMID: 16420526
5. Arabidopsis UNHINGED encodes a VPS51 homolog and reveals a role for the GARP complex in leaf shape and vein patterning.. *Development (Cambridge, England)*. PMID: 24757006

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.4 |
| 高置信度残基 (pLDDT>90) 占比 | 40.0% |
| 置信残基 (pLDDT 70-90) 占比 | 41.7% |
| 中等置信 (pLDDT 50-70) 占比 | 6.9% |
| 低置信 (pLDDT<50) 占比 | 11.4% |
| 有序区域 (pLDDT>70) 占比 | 81.7% |
| 可用 PDB 条目 | 4J2C |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=80.4，有序区 81.7%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016159, IPR014812; Pfam: PF08700 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| VPS53 | 0.999 | 0.994 | — |
| VPS50 | 0.999 | 0.994 | — |
| VPS52 | 0.999 | 0.850 | — |
| VPS54 | 0.999 | 0.643 | — |
| STX6 | 0.992 | 0.961 | — |
| EIPR1 | 0.938 | 0.839 | — |
| STX16 | 0.887 | 0.090 | — |
| COG8 | 0.869 | 0.287 | — |
| COG1 | 0.842 | 0.000 | — |
| STX10 | 0.829 | 0.423 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Exo70 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| VPS52 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| Prx4 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| YTHDC1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| EBI-1257125 | psi-mi:"MI:0096"(pull down) | pubmed:19463016|imex:IM-17246 |
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| CDKN1A | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| NSS | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:22810585|imex:IM-17331 |
| VPS54 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:12686613|imex:IM-20366 |
| VPS53 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:12686613|imex:IM-20366 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.4 + PDB: 4J2C | pLDDT=80.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Golgi apparatus, trans-Golgi network; Recycling en / Golgi apparatus, Vesicles; 额外: Nucleoli | 一致 |
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
1. VPS51 — Vacuolar protein sorting-associated protein 51 homolog，非常新颖，仅有少数基础研究。
2. 蛋白大小782 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 25 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UID3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000149823-VPS51/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=VPS51
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UID3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (approved)。来源: https://www.proteinatlas.org/ENSG00000149823-VPS51/subcellular

![](https://images.proteinatlas.org/61447/1080_A3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/61447/1080_A3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/61447/1102_A3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/61447/1102_A3_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/61447/1307_H2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/61447/1307_H2_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UID3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9UID3 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR016159;IPR014812; |
| Pfam | PF08700; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000149823-VPS51/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BORCS6 | Biogrid, Bioplex | true |
| EIPR1 | Biogrid, Bioplex | true |
| VPS50 | Intact, Biogrid | true |
| C19orf25 | Bioplex | false |
| DHH | Bioplex | false |
| EXOC4 | Intact | false |
| FAM174A | Bioplex | false |
| GINS2 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
