---
type: protein-evaluation
gene: "FHAD1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FHAD1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FHAD1 / KIAA1937 |
| 蛋白名称 | Forkhead-associated domain-containing protein 1 |
| 蛋白大小 | 1412 aa / 161.9 kDa |
| UniProt ID | B1AJZ9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Nuclear bodies; UniProt: Cell projection, cilium, flagellum |
| 蛋白大小 | 5/10 | ×1 | 5 | 1412 aa / 161.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=71.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR052642, IPR000253, IPR008984; Pfam: PF00498 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 5 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.5/180** | |
| **归一化总分** | | | **64.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear bodies | Approved |
| UniProt | Cell projection, cilium, flagellum | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- sperm flagellum (GO:0036126)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 11 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1937 |

**关键文献**:
1. Variable phenotypes and penetrance between and within different zebrafish ciliary transition zone mutants.. *Disease models & mechanisms*. PMID: 36533556
2. Forkhead-associated phosphopeptide binding domain 1 (FHAD1) deficiency impaired murine sperm motility.. *PeerJ*. PMID: 38563001
3. Combining long-read DNA and RNA sequencing to enhance molecular understanding of structural variations leading to copy gains.. *Computational and structural biotechnology journal*. PMID: 40421160
4. The transcription factor, Nuclear factor, erythroid 2 (Nfe2), is a regulator of the oxidative stress response during Danio rerio development.. *Aquatic toxicology (Amsterdam, Netherlands)*. PMID: 27716579
5. Genomic Signatures of Selection along a Climatic Gradient in the Northern Range Margin of the White-Footed Mouse (Peromyscus leucopus).. *The Journal of heredity*. PMID: 31300816

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.2 |
| 高置信度残基 (pLDDT>90) 占比 | 20.5% |
| 置信残基 (pLDDT 70-90) 占比 | 48.1% |
| 中等置信 (pLDDT 50-70) 占比 | 6.9% |
| 低置信 (pLDDT<50) 占比 | 24.4% |
| 有序区域 (pLDDT>70) 占比 | 68.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=71.2，有序区 68.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052642, IPR000253, IPR008984; Pfam: PF00498 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KLHL8 | 0.668 | 0.000 | — |
| PI15 | 0.540 | 0.000 | — |
| ATP11A | 0.507 | 0.000 | — |
| ZNF407 | 0.499 | 0.000 | — |
| SUSD4 | 0.495 | 0.000 | — |
| SEL1L3 | 0.490 | 0.000 | — |
| TTC34 | 0.483 | 0.000 | — |
| ARMC3 | 0.478 | 0.000 | — |
| OR5J2 | 0.452 | 0.000 | — |
| FAM181B | 0.451 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| H2BC9 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| HIST2H2BF | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| GTF2IRD1 | psi-mi:"MI:0018"(two hybrid) | pubmed:26275350|imex:IM-25509 |
| KLF8 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:35140242|imex:IM-28767 |
| EPHA3 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:35384245|imex:IM-29494 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 5
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 5 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.2 + PDB: 无 | pLDDT=71.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell projection, cilium, flagellum / Nucleoplasm, Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 15 + 5 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FHAD1 — Forkhead-associated domain-containing protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1412 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/B1AJZ9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000142621-FHAD1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FHAD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/B1AJZ9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000142621-FHAD1/subcellular

![](https://images.proteinatlas.org/54284/1300_D2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/54284/1300_D2_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/54284/1365_D2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/54284/1365_D2_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/54284/1511_C3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/54284/1511_C3_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-B1AJZ9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
