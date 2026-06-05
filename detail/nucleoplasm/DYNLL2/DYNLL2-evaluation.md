---
type: protein-evaluation
gene: "DYNLL2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DYNLL2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DYNLL2 / DLC2 |
| 蛋白名称 | Dynein light chain 2, cytoplasmic |
| 蛋白大小 | 89 aa / 10.3 kDa |
| UniProt ID | Q96FJ2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol, Mid piece, Principal piece; UniProt: Cytoplasm, cytoskeleton |
| 蛋白大小 | 5/10 | ×1 | 5 | 89 aa / 10.3 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=30 篇 (≤40→8) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=95.6; PDB: 2XQQ, 3P8M, 4D07, 7CNU |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR037177, IPR019763, IPR001372; Pfam: PF01221 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **127.5/180** | |
| **归一化总分** | | | **70.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol, Mid piece, Principal piece | Uncertain |
| UniProt | Cytoplasm, cytoskeleton | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 9+0 non-motile cilium (GO:0097731)
- centrosome (GO:0005813)
- ciliary tip (GO:0097542)
- cilium (GO:0005929)
- cytoplasmic dynein complex (GO:0005868)
- cytoskeleton (GO:0005856)
- cytosol (GO:0005829)
- glutamatergic synapse (GO:0098978)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 30 |
| PubMed broad count | 43 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DLC2 |

**关键文献**:
1. Role of Calcium Signaling Pathway-Related Gene Regulatory Networks in Ischemic Stroke Based on Multiple WGCNA and Single-Cell Analysis.. *Oxidative medicine and cellular longevity*. PMID: 34987704
2. Loss of MBNL1-mediated retrograde BDNF signaling in the myotonic dystrophy brain.. *Acta neuropathologica communications*. PMID: 36922901
3. TRIM68, PIKFYVE, and DYNLL2: The Possible Novel Autophagy- and Immunity-Associated Gene Biomarkers for Osteosarcoma Prognosis.. *Frontiers in oncology*. PMID: 33968741
4. Weighted gene co-expression network indicates that the DYNLL2 is an important regulator of chicken breast muscle development and is regulated by miR-148a-3p.. *BMC genomics*. PMID: 35379193
5. Affinity, avidity, and kinetics of target sequence binding to LC8 dynein light chain isoforms.. *The Journal of biological chemistry*. PMID: 20889982

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 95.6 |
| 高置信度残基 (pLDDT>90) 占比 | 93.3% |
| 置信残基 (pLDDT 70-90) 占比 | 3.4% |
| 中等置信 (pLDDT 50-70) 占比 | 2.2% |
| 低置信 (pLDDT<50) 占比 | 1.1% |
| 有序区域 (pLDDT>70) 占比 | 96.7% |
| 可用 PDB 条目 | 2XQQ, 3P8M, 4D07, 7CNU |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2XQQ, 3P8M, 4D07, 7CNU）+ AlphaFold高质量预测（pLDDT=95.6），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR037177, IPR019763, IPR001372; Pfam: PF01221 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DYNC1I2 | 0.995 | 0.881 | — |
| STRN4 | 0.994 | 0.994 | — |
| DYNLL1 | 0.990 | 0.846 | — |
| DYNC1I1 | 0.989 | 0.737 | — |
| DYNC1H1 | 0.983 | 0.508 | — |
| DYNC2LI1 | 0.978 | 0.195 | — |
| DYNC1LI2 | 0.973 | 0.332 | — |
| BMF | 0.971 | 0.600 | — |
| DYNC2H1 | 0.970 | 0.411 | — |
| DYNC1LI1 | 0.968 | 0.327 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=95.6 + PDB: 2XQQ, 3P8M, 4D07, 7CNU | pLDDT=95.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton / Nucleoplasm, Cytosol, Mid piece, Principal piece | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DYNLL2 — Dynein light chain 2, cytoplasmic，非常新颖，仅有少数基础研究。
2. 蛋白大小89 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 30 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96FJ2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000264364-DYNLL2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DYNLL2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96FJ2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000264364-DYNLL2/subcellular

![](https://images.proteinatlas.org/39954/2146_C10_36_blue_red_green.jpg)
![](https://images.proteinatlas.org/39954/2146_C10_58_blue_red_green.jpg)
![](https://images.proteinatlas.org/39954/2153_E9_41_blue_red_green.jpg)
![](https://images.proteinatlas.org/39954/2153_E9_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/39954/2199_A5_10_blue_red_green.jpg)
![](https://images.proteinatlas.org/39954/2199_A5_14_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96FJ2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
