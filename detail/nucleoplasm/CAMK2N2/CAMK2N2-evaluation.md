---
type: protein-evaluation
gene: "CAMK2N2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CAMK2N2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CAMK2N2 |
| 蛋白名称 | Calcium/calmodulin-dependent protein kinase II inhibitor 2 |
| 蛋白大小 | 79 aa / 8.7 kDa |
| UniProt ID | Q96S95 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Centrosome, Basal body; UniProt: Nucleus; Cytoplasm, cytosol; Synapse |
| 📏 蛋白大小 | 5/10 | ×1 | 5 | 79 aa / 8.7 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=11 篇 (≤20→10) |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=69.9; PDB: 无 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026779; Pfam: PF15170 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 2 interactions |
| ➕ 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **125.0/180** | |
| **归一化总分** | | | **69.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Centrosome, Basal body | Approved |
| UniProt | Nucleus; Cytoplasm, cytosol; Synapse | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleus (GO:0005634)
- synapse (GO:0045202)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11 |
| PubMed broad count | 25 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Astragaloside IV ameliorates autism-like behaviors in BTBR mice by modulating Camk2n2-dependent OXPHOS and neurotransmission in the mPFC.. *Journal of advanced research*. PMID: 39862907
2. CaMKII inhibitor 1 (CaMK2N1) mRNA is upregulated following LTP induction in hippocampal slices.. *Synapse (New York, N.Y.)*. PMID: 32320502
3. Identification of key candidate genes and biological pathways in neuropathic pain.. *Computers in biology and medicine*. PMID: 36166989
4. Prevention of long-term memory loss after retrieval by an endogenous CaMKII inhibitor.. *Scientific reports*. PMID: 28642476
5. Identification of candidate lncRNAs and circRNAs regulating WNT3/β-catenin signaling in essential hypertension.. *Aging*. PMID: 32392180

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.9 |
| 高置信度残基 (pLDDT>90) 占比 | 3.8% |
| 置信残基 (pLDDT 70-90) 占比 | 40.5% |
| 中等置信 (pLDDT 50-70) 占比 | 55.7% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 44.3% |
| 可用 PDB 条目 | 无 |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=69.9），有序残基占 44.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026779; Pfam: PF15170 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CAMK2B | 0.840 | 0.091 | — |
| CAMK2A | 0.799 | 0.091 | — |
| CALM3 | 0.682 | 0.000 | — |
| CALML4 | 0.648 | 0.000 | — |
| CALML5 | 0.648 | 0.000 | — |
| CALML3 | 0.648 | 0.000 | — |
| CALML6 | 0.648 | 0.000 | — |
| RIMBP2 | 0.470 | 0.000 | — |
| LRRC7 | 0.467 | 0.000 | — |
| DUSP8 | 0.447 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| P | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:unassigned2293|imex:IM- |
| CAMK2G | psi-mi:"MI:0096"(pull down) | pubmed:32707033|imex:IM-29257| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 2
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=69.9 + PDB: 无 | pLDDT=69.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, cytosol; Synapse / Nucleoplasm; 额外: Centrosome, Basal body | 一致 |
| PPI | STRING + IntAct | 15 + 2 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CAMK2N2 — Calcium/calmodulin-dependent protein kinase II inhibitor 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小79 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 11 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=69.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96S95
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163888-CAMK2N2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CAMK2N2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96S95
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 04:30:10

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000163888-CAMK2N2/subcellular

![](https://images.proteinatlas.org/50835/1070_A3_5_red_green.jpg)
![](https://images.proteinatlas.org/50835/1070_A3_8_red_green.jpg)
![](https://images.proteinatlas.org/50835/1076_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/50835/1076_A3_2_red_green.jpg)
![](https://images.proteinatlas.org/50835/1248_A1_3_red_green.jpg)
![](https://images.proteinatlas.org/50835/1248_A1_6_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
