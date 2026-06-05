---
type: protein-evaluation
gene: "GPRIN3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GPRIN3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPRIN3 / KIAA2027 |
| 蛋白名称 | G protein-regulated inducer of neurite outgrowth 3 |
| 蛋白大小 | 776 aa / 82.4 kDa |
| UniProt ID | Q6ZVF9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoli; 额外: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 776 aa / 82.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=46.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026646, IPR032745; Pfam: PF15235 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 9 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; 额外: Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- plasma membrane (GO:0005886)
- synapse (GO:0045202)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 17 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA2027 |

**关键文献**:
1. Identifying novel risk genes in intracranial aneurysm by integrating human proteomes and genetics.. *Brain : a journal of neurology*. PMID: 39084678
2. Predicting diagnostic gene biomarkers in allergic asthma.. *Medicine*. PMID: 42065182
3. GPRIN3 Controls Neuronal Excitability, Morphology, and Striatal-Dependent Behaviors in the Indirect Pathway of the Striatum.. *The Journal of neuroscience : the official journal of the Society for Neuroscience*. PMID: 31363062
4. Identification of Novel Equine (Equus caballus) Tendon Markers Using RNA Sequencing.. *Genes*. PMID: 27834918
5. Genome-Wide Association Analysis of Growth Traits in Hu Sheep.. *Genes*. PMID: 39766904

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 46.9 |
| 高置信度残基 (pLDDT>90) 占比 | 2.3% |
| 置信残基 (pLDDT 70-90) 占比 | 4.1% |
| 中等置信 (pLDDT 50-70) 占比 | 18.7% |
| 低置信 (pLDDT<50) 占比 | 74.9% |
| 有序区域 (pLDDT>70) 占比 | 6.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=46.9），有序残基占 6.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026646, IPR032745; Pfam: PF15235 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GNAZ | 0.648 | 0.000 | — |
| GRIN1 | 0.648 | 0.000 | — |
| GPRIN2 | 0.632 | 0.000 | — |
| GNAO1 | 0.597 | 0.000 | — |
| ZNF644 | 0.511 | 0.000 | — |
| TIGD2 | 0.488 | 0.000 | — |
| UBOX5 | 0.458 | 0.000 | — |
| SH3BGRL2 | 0.454 | 0.000 | — |
| PSMG1 | 0.450 | 0.000 | — |
| CNKSR3 | 0.439 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NLN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| KCNJ2 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:32541000|imex:IM-29166 |
| IGF1R | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:35384245|imex:IM-29494 |
| EPHB2 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:35384245|imex:IM-29494 |
| FGFR1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:35384245|imex:IM-29494 |
| EGFR | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:35384245|imex:IM-29494 |
| FGFR4 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:35384245|imex:IM-29494 |
| FGFR2 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:35384245|imex:IM-29494 |
| NTRK2 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:35384245|imex:IM-29494 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 9
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 9 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=46.9 + PDB: 无 | pLDDT=46.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoli; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 9 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. GPRIN3 — G protein-regulated inducer of neurite outgrowth 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小776 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=46.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6ZVF9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000185477-GPRIN3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPRIN3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6ZVF9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/GPRIN3/IF_images/A-549_1.jpg]]
![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/GPRIN3/IF_images/HEK293_1.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (approved)。来源: https://www.proteinatlas.org/ENSG00000185477-GPRIN3/subcellular

![](https://images.proteinatlas.org/43148/1468_B2_1_red_green.jpg)
![](https://images.proteinatlas.org/43148/1468_B2_2_red_green.jpg)
![](https://images.proteinatlas.org/43148/1470_B2_2_red_green.jpg)
![](https://images.proteinatlas.org/43148/1470_B2_3_red_green.jpg)
![](https://images.proteinatlas.org/43148/1564_E6_2_red_green.jpg)
![](https://images.proteinatlas.org/43148/1564_E6_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6ZVF9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
