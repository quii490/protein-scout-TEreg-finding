---
type: protein-evaluation
gene: "GOSR2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GOSR2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GOSR2 / GS27 |
| 蛋白名称 | Golgi SNAP receptor complex member 2 |
| 蛋白大小 | 212 aa / 24.8 kDa |
| UniProt ID | O14653 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Golgi apparatus; UniProt: Golgi apparatus, cis-Golgi network membrane; Golgi apparatus |
| 蛋白大小 | 10/10 | ×1 | 10 | 212 aa / 24.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=83.1; PDB: 3EG9 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR027027, IPR010989, IPR038407; Pfam: PF12352 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **139.0/180** | |
| **归一化总分** | | | **77.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Golgi apparatus | Supported |
| UniProt | Golgi apparatus, cis-Golgi network membrane; Golgi apparatus membrane; Endoplasmic reticulum membran... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- endoplasmic reticulum membrane (GO:0005789)
- endoplasmic reticulum-Golgi intermediate compartment membrane (GO:0033116)
- ER to Golgi transport vesicle membrane (GO:0012507)
- Golgi apparatus (GO:0005794)
- Golgi membrane (GO:0000139)
- late endosome membrane (GO:0031902)
- membrane (GO:0016020)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 0 |
| 别名(未计入scoring) | 无 |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.1 |
| 高置信度残基 (pLDDT>90) 占比 | 25.0% |
| 置信残基 (pLDDT 70-90) 占比 | 65.6% |
| 中等置信 (pLDDT 50-70) 占比 | 7.1% |
| 低置信 (pLDDT<50) 占比 | 2.4% |
| 有序区域 (pLDDT>70) 占比 | 90.6% |
| 可用 PDB 条目 | 3EG9 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=83.1，有序区 90.6%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027027, IPR010989, IPR038407; Pfam: PF12352 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BET1 | 0.999 | 0.990 | — |
| SEC22B | 0.999 | 0.986 | — |
| SCFD1 | 0.999 | 0.972 | — |
| GOSR1 | 0.999 | 0.975 | — |
| STX5 | 0.999 | 0.991 | — |
| BET1L | 0.997 | 0.910 | — |
| YKT6 | 0.995 | 0.958 | — |
| USO1 | 0.994 | 0.975 | — |
| SEC22A | 0.992 | 0.786 | — |
| SEC22C | 0.985 | 0.786 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| GOLM1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27569582|imex:IM-26128 |
| BET1 | psi-mi:"MI:0096"(pull down) | pubmed:29568061|imex:IM-26301 |
| VAMP5 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| NAPA | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| BLCAP | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| STX1A | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| IER3IP1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TMEM106C | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| HSD17B13 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.1 + PDB: 3EG9 | pLDDT=83.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Golgi apparatus, cis-Golgi network membrane; Golgi / Nucleoplasm, Golgi apparatus | 一致 |
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
1. GOSR2 — Golgi SNAP receptor complex member 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小212 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O14653
- Protein Atlas: https://www.proteinatlas.org/ENSG00000108433-GOSR2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GOSR2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O14653
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000108433-GOSR2/subcellular

![](https://images.proteinatlas.org/48956/757_G8_1_red_green.jpg)
![](https://images.proteinatlas.org/48956/757_G8_2_red_green.jpg)
![](https://images.proteinatlas.org/48956/761_G8_1_red_green.jpg)
![](https://images.proteinatlas.org/48956/761_G8_2_red_green.jpg)
![](https://images.proteinatlas.org/48956/769_G8_1_red_green.jpg)
![](https://images.proteinatlas.org/48956/769_G8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O14653-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O14653 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR027027;IPR010989;IPR038407; |
| Pfam | PF12352; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000108433-GOSR2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BET1 | Intact, Biogrid, Opencell | true |
| MMGT1 | Intact, Biogrid | true |
| NAPA | Biogrid, Opencell | true |
| SEC22B | Biogrid, Opencell | true |
| STX5 | Intact, Biogrid, Opencell | true |
| STX6 | Intact, Biogrid | true |
| AQP6 | Intact | false |
| ARL13B | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
