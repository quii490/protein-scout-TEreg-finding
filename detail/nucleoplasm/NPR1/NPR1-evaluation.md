---
type: protein-evaluation
gene: "NPR1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## NPR1 — REJECTED (研究热度过高 (PubMed strict=1106，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NPR1 / ANPRA |
| 蛋白名称 | Atrial natriuretic peptide receptor 1 |
| 蛋白大小 | 1061 aa / 118.9 kDa |
| UniProt ID | P16066 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoli; 额外: Nucleoplasm, Plasma membrane; UniProt: Membrane |
| 蛋白大小 | 8/10 | ×1 | 8 | 1061 aa / 118.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1106 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=84.6; PDB: 8TG9, 8TGA, 9BCL, 9BCN, 9BCO, 9BCP, 9BCQ |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001054, IPR018297, IPR001828, IPR001170, IPR050 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **82.0/180** | |
| **归一化总分** | | | **45.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; 额外: Nucleoplasm, Plasma membrane | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- ANPR-A receptor complex (GO:1990620)
- plasma membrane (GO:0005886)
- receptor complex (GO:0043235)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1106 |
| PubMed broad count | 1530 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ANPRA |

**关键文献**:
1. NPR1, a key immune regulator for plant survival under biotic and abiotic stresses.. *Molecular cell*. PMID: 38103555
2. Formation of NPR1 Condensates Promotes Cell Survival during the Plant Immune Response.. *Cell*. PMID: 32810437
3. Opposite Roles of Salicylic Acid Receptors NPR1 and NPR3/NPR4 in Transcriptional Regulation of Plant Immunity.. *Cell*. PMID: 29656896
4. Diverse Roles of the Salicylic Acid Receptors NPR1 and NPR3/NPR4 in Plant Immunity.. *The Plant cell*. PMID: 33037144
5. Next-generation mapping of the salicylic acid signaling hub and transcriptional cascade.. *Molecular plant*. PMID: 39180213

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.6 |
| 高置信度残基 (pLDDT>90) 占比 | 54.8% |
| 置信残基 (pLDDT 70-90) 占比 | 31.2% |
| 中等置信 (pLDDT 50-70) 占比 | 6.6% |
| 低置信 (pLDDT<50) 占比 | 7.4% |
| 有序区域 (pLDDT>70) 占比 | 86.0% |
| 可用 PDB 条目 | 8TG9, 8TGA, 9BCL, 9BCN, 9BCO, 9BCP, 9BCQ, 9BCS, 9BCV |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（8TG9, 8TGA, 9BCL, 9BCN, 9BCO, 9BCP, 9BCQ, 9BCS, 9BCV）+ AlphaFold极高置信度预测（pLDDT=84.6），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001054, IPR018297, IPR001828, IPR001170, IPR050401; Pfam: PF01094, PF00211, PF07714 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NPPB | 0.999 | 0.510 | — |
| NPPA | 0.999 | 0.884 | — |
| NPPC | 0.971 | 0.550 | — |
| NPR2 | 0.949 | 0.000 | — |
| GCG | 0.920 | 0.000 | — |
| GNAS | 0.920 | 0.185 | — |
| VIP | 0.916 | 0.000 | — |
| ADCYAP1 | 0.914 | 0.000 | — |
| POMC | 0.914 | 0.000 | — |
| TSHB | 0.910 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ACC1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| ACT1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| ATP2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| BRR2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| DNM1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| EFT1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| ERG1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| GCN1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| GCN20 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| GFA1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.6 + PDB: 8TG9, 8TGA, 9BCL, 9BCN, 9BCO,  | pLDDT=84.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Membrane / Nucleoli; 额外: Nucleoplasm, Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. NPR1 — Atrial natriuretic peptide receptor 1，研究基础较多，新颖性有限。
2. 蛋白大小1061 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 1106 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1106 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P16066
- Protein Atlas: https://www.proteinatlas.org/ENSG00000169418-NPR1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NPR1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P16066
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (approved)。来源: https://www.proteinatlas.org/ENSG00000169418-NPR1/subcellular

![](https://images.proteinatlas.org/31087/1061_E3_1_red_green.jpg)
![](https://images.proteinatlas.org/31087/1061_E3_2_red_green.jpg)
![](https://images.proteinatlas.org/31087/330_F1_1_red_green.jpg)
![](https://images.proteinatlas.org/31087/330_F1_2_red_green.jpg)
![](https://images.proteinatlas.org/31087/331_F1_1_red_green.jpg)
![](https://images.proteinatlas.org/31087/331_F1_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P16066-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P16066 |
| SMART | SM00044; |
| UniProt Domain [FT] | DOMAIN 528..805; /note="Protein kinase"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00159"; DOMAIN 876..1006; /note="Guanylate cyclase"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00099" |
| InterPro | IPR001054;IPR018297;IPR001828;IPR001170;IPR050401;IPR011009;IPR029787;IPR028082;IPR000719;IPR001245; |
| Pfam | PF01094;PF00211;PF07714; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000169418-NPR1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| NPPB | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
