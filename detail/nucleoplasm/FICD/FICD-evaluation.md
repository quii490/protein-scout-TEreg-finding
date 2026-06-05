---
type: protein-evaluation
gene: "FICD"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FICD 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FICD / HIP13, HYPE |
| 蛋白名称 | Protein adenylyltransferase FICD |
| 蛋白大小 | 458 aa / 51.8 kDa |
| UniProt ID | Q9BVA6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; UniProt: Endoplasmic reticulum membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 458 aa / 51.8 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=51 篇 (≤60→6) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=83.6; PDB: 4U04, 4U07, 4U0S, 4U0U, 4U0Z, 6I7G, 6I7H |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR003812, IPR036597, IPR040198, IPR011990, IPR019 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **114.0/180** | |
| **归一化总分** | | | **63.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Endoplasmic reticulum membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum membrane (GO:0005789)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 51 |
| PubMed broad count | 123 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HIP13, HYPE |

**关键文献**:
1. Small molecule FICD inhibitors suppress endogenous and pathologic FICD-mediated protein AMPylation.. *bioRxiv : the preprint server for biology*. PMID: 39071275
2. AMPylation and Endoplasmic Reticulum Protein Folding Homeostasis.. *Cold Spring Harbor perspectives in biology*. PMID: 36041787
3. Small-Molecule FICD Inhibitors Suppress Endogenous and Pathologic FICD-Mediated Protein AMPylation.. *ACS chemical biology*. PMID: 40036289
4. AMPylation Regulates 5'-3' Exonuclease PLD3 Processing.. *Molecular & cellular proteomics : MCP*. PMID: 40816421
5. From Young to Old: AMPylation Hits the Brain.. *Cell chemical biology*. PMID: 32521229

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.6 |
| 高置信度残基 (pLDDT>90) 占比 | 70.1% |
| 置信残基 (pLDDT 70-90) 占比 | 8.5% |
| 中等置信 (pLDDT 50-70) 占比 | 6.3% |
| 低置信 (pLDDT<50) 占比 | 15.1% |
| 有序区域 (pLDDT>70) 占比 | 78.6% |
| 可用 PDB 条目 | 4U04, 4U07, 4U0S, 4U0U, 4U0Z, 6I7G, 6I7H, 6I7I, 6I7J, 6I7K |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（4U04, 4U07, 4U0S, 4U0U, 4U0Z, 6I7G, 6I7H, 6I7I, 6I7J, 6I7K）+ AlphaFold极高置信度预测（pLDDT=83.6），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003812, IPR036597, IPR040198, IPR011990, IPR019734; Pfam: PF02661 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HSPA5 | 0.963 | 0.939 | — |
| HTT | 0.865 | 0.239 | — |
| MAP1LC3A | 0.833 | 0.000 | — |
| PRPF40B | 0.833 | 0.000 | — |
| PRPF40A | 0.659 | 0.000 | — |
| MAGEA3 | 0.601 | 0.000 | — |
| OAT | 0.570 | 0.000 | — |
| CDC42 | 0.546 | 0.292 | — |
| ATP8B1 | 0.522 | 0.000 | — |
| SETD2 | 0.436 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ADK | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| HTT | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:32814053|imex:IM-28217| |
| TMEM169 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| HCN1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:37207277|imex:IM-29810 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 4
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 4 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.6 + PDB: 4U04, 4U07, 4U0S, 4U0U, 4U0Z,  | pLDDT=83.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 4 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FICD — Protein adenylyltransferase FICD，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小458 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 51 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BVA6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000198855-FICD/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FICD
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BVA6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000198855-FICD/subcellular

![](https://images.proteinatlas.org/71134/1433_G10_1_red_green.jpg)
![](https://images.proteinatlas.org/71134/1433_G10_2_red_green.jpg)
![](https://images.proteinatlas.org/71134/1435_G10_2_red_green.jpg)
![](https://images.proteinatlas.org/71134/1435_G10_7_red_green.jpg)
![](https://images.proteinatlas.org/71134/1533_A2_1_red_green.jpg)
![](https://images.proteinatlas.org/71134/1533_A2_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BVA6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
