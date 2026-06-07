---
type: protein-evaluation
gene: "SSX2B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SSX2B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SSX2B / SSX2A |
| 蛋白名称 | Protein SSX2 |
| 蛋白大小 | 188 aa / 21.6 kDa |
| UniProt ID | Q16385 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm, Nucleoli; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 188 aa / 21.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.6; PDB: 8HQY |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR003655, IPR001909, IPR036051, IPR019041; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **136.5/180** | |
| **归一化总分** | | | **75.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 3 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SSX2A |

**关键文献**:
1. Placental Gene Expression Associated With Early Childhood Growth Trajectories and Obesity Risk.. *Obesity (Silver Spring, Md.)*. PMID: 40709507
2. Clinical application of RNA sequencing in sarcoma diagnosis: An institutional experience.. *Medicine*. PMID: 31232935

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.6 |
| 高置信度残基 (pLDDT>90) 占比 | 26.1% |
| 置信残基 (pLDDT 70-90) 占比 | 15.4% |
| 中等置信 (pLDDT 50-70) 占比 | 41.5% |
| 低置信 (pLDDT<50) 占比 | 17.0% |
| 有序区域 (pLDDT>70) 占比 | 41.5% |
| 可用 PDB 条目 | 8HQY |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=68.6），有序残基占 41.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003655, IPR001909, IPR036051, IPR019041; Pfam: PF01352, PF09514 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SS18 | 0.918 | 0.000 | — |
| SSX2IP | 0.815 | 0.000 | — |
| SSX2 | 0.783 | 0.000 | — |
| CTAG1B | 0.772 | 0.000 | — |
| SS18L2 | 0.750 | 0.000 | — |
| SS18L1 | 0.711 | 0.000 | — |
| MAGEA4 | 0.706 | 0.000 | — |
| MAGEC1 | 0.692 | 0.000 | — |
| MAGEA3 | 0.691 | 0.000 | — |
| MAGEA1 | 0.679 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RAB3IP | psi-mi:"MI:0018"(two hybrid) | pubmed:12007189|imex:IM-20236| |
| SSX2IP | psi-mi:"MI:0018"(two hybrid) | pubmed:12007189|imex:IM-20236| |
| SSX2 | psi-mi:"MI:0096"(pull down) | pubmed:12007189|imex:IM-20236| |
| SSX3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FLACC1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| PHLDA2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TRAPPC2L | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| FTSJ3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| LRRC45 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TNPO3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.6 + PDB: 8HQY | pLDDT=68.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. SSX2B — Protein SSX2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小188 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=68.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q16385
- Protein Atlas: https://www.proteinatlas.org/ENSG00000268447-SSX2B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SSX2B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q16385
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000268447-SSX2B/subcellular

![](https://images.proteinatlas.org/45683/1397_A4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/45683/1397_A4_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/45683/1402_A4_10_blue_red_green.jpg)
![](https://images.proteinatlas.org/45683/1402_A4_11_blue_red_green.jpg)
![](https://images.proteinatlas.org/45683/1440_H11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/45683/1440_H11_5_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q16385-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q16385 |
| SMART | SM00349; |
| UniProt Domain [FT] | DOMAIN 20..83; /note="KRAB-related"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00120" |
| InterPro | IPR003655;IPR001909;IPR036051;IPR019041; |
| Pfam | PF01352;PF09514; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000268447-SSX2B/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BLZF1 | Intact | false |
| KRT40 | Intact | false |
| MAGEC2 | Intact | false |
| RAB3IP | Intact | false |
| SPRED1 | Intact | false |
| SSX2IP | Intact | false |
| SYCE1 | Intact | false |
| TAX1BP1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
