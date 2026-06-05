---
type: protein-evaluation
gene: "GPR171"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GPR171 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPR171 / H963 |
| 蛋白名称 | G-protein coupled receptor 171 |
| 蛋白大小 | 319 aa / 36.8 kDa |
| UniProt ID | O14626 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Vesicles, Plasma membrane; UniProt: Cell membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 319 aa / 36.8 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=39 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=87.7; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000276, IPR017452, IPR048077; Pfam: PF00001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 5 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **108.5/180** | |
| **归一化总分** | | | **60.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles, Plasma membrane | Approved |
| UniProt | Cell membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- membrane (GO:0016020)
- plasma membrane (GO:0005886)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 39 |
| PubMed broad count | 47 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: H963 |

**关键文献**:
1. GPR171 restrains intestinal inflammation by suppressing FABP5-mediated Th17 cell differentiation and lipid metabolism.. *Gut*. PMID: 40074327
2. The GPR171 pathway suppresses T cell activation and limits antitumor immunity.. *Nature communications*. PMID: 34615877
3. ProSAAS neuropeptides and receptors GPR171 and GPR83: Potential therapeutic applications for pain, anxiety, and body weight regulation.. *The Journal of pharmacology and experimental therapeutics*. PMID: 40450835
4. The role of orphan G protein-coupled receptors in pain.. *Heliyon*. PMID: 38590871
5. Orphan neuropeptides and receptors: Novel therapeutic targets.. *Pharmacology & therapeutics*. PMID: 29174650

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.7 |
| 高置信度残基 (pLDDT>90) 占比 | 57.1% |
| 置信残基 (pLDDT 70-90) 占比 | 35.1% |
| 中等置信 (pLDDT 50-70) 占比 | 6.6% |
| 低置信 (pLDDT<50) 占比 | 1.3% |
| 有序区域 (pLDDT>70) 占比 | 92.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=87.7，有序区 92.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000276, IPR017452, IPR048077; Pfam: PF00001 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PCSK1N | 0.861 | 0.000 | — |
| GPR83 | 0.726 | 0.000 | — |
| GZMK | 0.676 | 0.000 | — |
| TRAT1 | 0.624 | 0.000 | — |
| CD3D | 0.605 | 0.000 | — |
| CD2 | 0.580 | 0.000 | — |
| GPR152 | 0.578 | 0.000 | — |
| ITK | 0.542 | 0.000 | — |
| LCK | 0.521 | 0.000 | — |
| VIP | 0.506 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DAZAP1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| NME2P1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| RAMP2 | psi-mi:"MI:0947"(bead aggregation assay) | pubmed:39083597|imex:IM-30383 |
| RAMP3 | psi-mi:"MI:0947"(bead aggregation assay) | pubmed:39083597|imex:IM-30383 |
| RAMP1 | psi-mi:"MI:0947"(bead aggregation assay) | pubmed:39083597|imex:IM-30383 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 5
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 5 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.7 + PDB: 无 | pLDDT=87.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane / Vesicles, Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 5 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GPR171 — G-protein coupled receptor 171，非常新颖，仅有少数基础研究。
2. 蛋白大小319 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 39 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O14626
- Protein Atlas: https://www.proteinatlas.org/ENSG00000174946-GPR171/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPR171
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O14626
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (approved)。来源: https://www.proteinatlas.org/ENSG00000174946-GPR171/subcellular

![](https://images.proteinatlas.org/67323/2158_G2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/67323/2158_G2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/67323/2214_D4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/67323/2214_D4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/67323/2227_H2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/67323/2227_H2_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O14626-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
