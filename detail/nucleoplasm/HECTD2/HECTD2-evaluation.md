---
type: protein-evaluation
gene: "HECTD2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## HECTD2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HECTD2 |
| 蛋白名称 | Probable E3 ubiquitin-protein ligase HECTD2 |
| 蛋白大小 | 776 aa / 88.1 kDa |
| UniProt ID | Q5U5R9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 776 aa / 88.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=20 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=80.3; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR044611, IPR000569, IPR035983; Pfam: PF00632 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 6 partners; IntAct 5 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.5/180** | |
| **归一化总分** | | | **68.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 20 |
| PubMed broad count | 27 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Lactylation-Driven HECTD2 Limits the Response of Hepatocellular Carcinoma to Lenvatinib.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 39976163
2. Rare loss-of-function variants in HECTD2 and AKAP11 confer risk of bipolar disorder.. *Nature genetics*. PMID: 40133559
3. The proinflammatory role of HECTD2 in innate immunity and experimental lung injury.. *Science translational medicine*. PMID: 26157031
4. Liver and Kidney Surgical Anatomy to Verify the Effect of miR-221 on Organ Damage in Septic Rats.. *Journal of healthcare engineering*. PMID: 35186224
5. E3 ubiquitin ligase HECTD2 mediates melanoma progression and immune evasion.. *Oncogene*. PMID: 34145398

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.3 |
| 高置信度残基 (pLDDT>90) 占比 | 58.6% |
| 置信残基 (pLDDT 70-90) 占比 | 22.9% |
| 中等置信 (pLDDT 50-70) 占比 | 1.5% |
| 低置信 (pLDDT<50) 占比 | 16.9% |
| 有序区域 (pLDDT>70) 占比 | 81.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=80.3，有序区 81.5%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR044611, IPR000569, IPR035983; Pfam: PF00632 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RNF8 | 0.466 | 0.000 | — |
| UBE2N | 0.451 | 0.049 | — |
| PCGF5 | 0.448 | 0.045 | — |
| PRR20B | 0.434 | 0.000 | — |
| PIAS1 | 0.430 | 0.301 | — |
| ZNF688 | 0.400 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CALR | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| RNF166 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ACKR3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| HSPA8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| BTG3 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:35914814|imex:IM-27626 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 6，IntAct interactions: 5
- 调控相关比例: 0 / 6 = 0%

**评价**: STRING 6 个预测互作，IntAct 5 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.3 + PDB: 无 | pLDDT=80.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 6 + 5 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. HECTD2 — Probable E3 ubiquitin-protein ligase HECTD2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小776 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 20 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5U5R9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000165338-HECTD2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HECTD2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5U5R9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000165338-HECTD2/subcellular

![](https://images.proteinatlas.org/37767/422_H10_1_red_green.jpg)
![](https://images.proteinatlas.org/37767/422_H10_2_red_green.jpg)
![](https://images.proteinatlas.org/37767/423_H10_1_red_green.jpg)
![](https://images.proteinatlas.org/37767/423_H10_2_red_green.jpg)
![](https://images.proteinatlas.org/37767/426_H10_1_red_green.jpg)
![](https://images.proteinatlas.org/37767/426_H10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5U5R9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q5U5R9 |
| SMART | SM00119; |
| UniProt Domain [FT] | DOMAIN 437..776; /note="HECT"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00104" |
| InterPro | IPR044611;IPR000569;IPR035983; |
| Pfam | PF00632; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000165338-HECTD2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PIAS1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
