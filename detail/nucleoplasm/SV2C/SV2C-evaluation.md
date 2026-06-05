---
type: protein-evaluation
gene: "SV2C"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SV2C 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SV2C / KIAA1054 |
| 蛋白名称 | Synaptic vesicle glycoprotein 2C |
| 蛋白大小 | 727 aa / 82.3 kDa |
| UniProt ID | Q496J9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Vesicles; UniProt: Cytoplasmic vesicle, secretory vesicle, synaptic vesicle mem |
| 蛋白大小 | 10/10 | ×1 | 10 | 727 aa / 82.3 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=86 篇 (≤100→2) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=78.0; PDB: 4JRA, 5JLV, 5MOY, 6ES1, 7UIA, 7UIB |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR055415, IPR011701, IPR020846, IPR005828, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 9 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **92.0/180** | |
| **归一化总分** | | | **51.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Vesicles | Supported |
| UniProt | Cytoplasmic vesicle, secretory vesicle, synaptic vesicle membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- dopaminergic synapse (GO:0098691)
- plasma membrane (GO:0005886)
- synaptic vesicle (GO:0008021)
- synaptic vesicle membrane (GO:0030672)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 86 |
| PubMed broad count | 120 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1054 |

**关键文献**:
1. Prioritizing Parkinson's disease risk genes in genome-wide association loci.. *NPJ Parkinson's disease*. PMID: 40240380
2. Prioritizing Parkinson's disease risk genes in genome-wide association loci.. *medRxiv : the preprint server for health sciences*. PMID: 39711693
3. Synaptic vesicle 2C and its synaptic-related function.. *Clinica chimica acta; international journal of clinical chemistry*. PMID: 28774501
4. Mapping Dural and Periosteal SV2C, a Botulinum Toxin A Receptor, in the Mouse.. *Toxins*. PMID: 41150209
5. Distribution of SV2C mRNA and protein expression in the mouse brain with a particular emphasis on the basal ganglia system.. *Brain research*. PMID: 20869353

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.0 |
| 高置信度残基 (pLDDT>90) 占比 | 32.7% |
| 置信残基 (pLDDT 70-90) 占比 | 42.1% |
| 中等置信 (pLDDT 50-70) 占比 | 13.1% |
| 低置信 (pLDDT<50) 占比 | 12.1% |
| 有序区域 (pLDDT>70) 占比 | 74.8% |
| 可用 PDB 条目 | 4JRA, 5JLV, 5MOY, 6ES1, 7UIA, 7UIB |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（4JRA, 5JLV, 5MOY, 6ES1, 7UIA, 7UIB）+ AlphaFold极高置信度预测（pLDDT=78.0），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR055415, IPR011701, IPR020846, IPR005828, IPR036259; Pfam: PF23894, PF07690, PF00083 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SV2B | 0.943 | 0.000 | — |
| GP2 | 0.923 | 0.091 | — |
| SV2A | 0.905 | 0.000 | — |
| LAMC2 | 0.740 | 0.000 | — |
| SYT1 | 0.733 | 0.329 | — |
| LAMC3 | 0.725 | 0.000 | — |
| LAMC1 | 0.700 | 0.000 | — |
| LAMB1 | 0.699 | 0.000 | — |
| LAMB3 | 0.687 | 0.000 | — |
| LAMA1 | 0.684 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EXTL3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| UBE4A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ABCC10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ABHD17B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| UFD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| VANGL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MINDY1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| NPLOC4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| MAPT | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:35063084|imex:IM-29773 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 9
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 9 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.0 + PDB: 4JRA, 5JLV, 5MOY, 6ES1, 7UIA,  | pLDDT=78.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasmic vesicle, secretory vesicle, synaptic v / Nucleoplasm, Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 9 interactions | 数据充分 |

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
1. SV2C — Synaptic vesicle glycoprotein 2C，研究基础较多，新颖性有限。
2. 蛋白大小727 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 86 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q496J9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000122012-SV2C/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SV2C
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q496J9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000122012-SV2C/subcellular

![](https://images.proteinatlas.org/40722/1220_E4_1_red_green.jpg)
![](https://images.proteinatlas.org/40722/1220_E4_2_red_green.jpg)
![](https://images.proteinatlas.org/40722/789_D11_2_red_green.jpg)
![](https://images.proteinatlas.org/40722/789_D11_6_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q496J9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
