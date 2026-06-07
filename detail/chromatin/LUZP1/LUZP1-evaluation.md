---
type: protein-evaluation
gene: "LUZP1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LUZP1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LUZP1 |
| 蛋白名称 | Leucine zipper protein 1 |
| 蛋白大小 | 1076 aa / 120.3 kDa |
| UniProt ID | Q86V48 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Actin filaments; 额外: Vesicles, Plasma membrane, Cytokinetic ; UniProt: Cytoplasm, cytoskeleton, microtubule organizing center, cent |
| 蛋白大小 | 8/10 | ×1 | 8 | 1076 aa / 120.3 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=25 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=56.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR050719 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **106.0/180** | |
| **归一化总分** | | | **58.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Actin filaments; 额外: Vesicles, Plasma membrane, Cytokinetic bridge, Centrosome, Cytosol | Approved |
| UniProt | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Cytoplasm, cytoskeleton, cilium ... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- actin cytoskeleton (GO:0015629)
- actin filament (GO:0005884)
- bicellular tight junction (GO:0005923)
- centrosome (GO:0005813)
- CERF complex (GO:0090537)
- chromosome, centromeric region (GO:0000775)
- ciliary basal body (GO:0036064)
- dendrite (GO:0030425)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 25 |
| PubMed broad count | 35 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Leucine zipper protein 1 prevents doxorubicin-induced cardiotoxicity in mice.. *Redox biology*. PMID: 37354826
2. Leucine zipper protein 1 attenuates pressure overload-induced cardiac hypertrophy through inhibiting Stat3 signaling.. *Journal of advanced research*. PMID: 37806546
3. Death-associated protein kinase 3 modulates migration and invasion of triple-negative breast cancer cells.. *PNAS nexus*. PMID: 39319326
4. CEP76 impairment at the centrosome-cilium interface contributes to a spectrum of ciliopathies.. *Science advances*. PMID: 41105778
5. LUZP1: A new player in the actin-microtubule cross-talk.. *European journal of cell biology*. PMID: 35738212

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 56.4 |
| 高置信度残基 (pLDDT>90) 占比 | 23.4% |
| 置信残基 (pLDDT 70-90) 占比 | 3.5% |
| 中等置信 (pLDDT 50-70) 占比 | 9.1% |
| 低置信 (pLDDT<50) 占比 | 63.9% |
| 有序区域 (pLDDT>70) 占比 | 26.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=56.4），有序残基占 26.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050719 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DAPK3 | 0.994 | 0.994 | — |
| FLNA | 0.649 | 0.187 | — |
| ACTR2 | 0.583 | 0.420 | — |
| LIMA1 | 0.573 | 0.161 | — |
| KATNA1 | 0.537 | 0.000 | — |
| SALL1 | 0.524 | 0.000 | — |
| PLEC | 0.502 | 0.165 | — |
| SLITRK1 | 0.471 | 0.000 | — |
| MYC | 0.468 | 0.216 | — |
| ARHGAP32 | 0.463 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GRB2 | psi-mi:"MI:0096"(pull down) | pubmed:12577067|mint:MINT-5216 |
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |
| Q0WDV6 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| CUL5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| HSPB1 | psi-mi:"MI:0097"(reverse ras recruitment system) | imex:IM-20864|pubmed:25277244 |
| YWHAH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SEC31A | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=56.4 + PDB: 无 | pLDDT=56.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, microtubule organizing ce / Actin filaments; 额外: Vesicles, Plasma membrane, Cy | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. LUZP1 — Leucine zipper protein 1，非常新颖，仅有少数基础研究。
2. 蛋白大小1076 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 25 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=56.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86V48
- Protein Atlas: https://www.proteinatlas.org/ENSG00000169641-LUZP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LUZP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86V48
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Actin filaments (supported)。来源: https://www.proteinatlas.org/ENSG00000169641-LUZP1/subcellular

![](https://images.proteinatlas.org/28506/394_A11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/28506/394_A11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/28506/395_A11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/28506/395_A11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/28506/399_A11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/28506/399_A11_4_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86V48-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q86V48 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR050719; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000169641-LUZP1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DAPK3 | Intact, Biogrid, Opencell | true |
| ANLN | Biogrid | false |
| CALD1 | Opencell | false |
| CALM3 | Opencell | false |
| CAPZB | Opencell | false |
| CDC14A | Biogrid | false |
| CEP135 | Biogrid | false |
| CTTN | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
