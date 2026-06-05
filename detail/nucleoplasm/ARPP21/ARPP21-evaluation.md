---
type: protein-evaluation
gene: "ARPP21"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ARPP21 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ARPP21 / TARPP |
| 蛋白名称 | cAMP-regulated phosphoprotein 21 |
| 蛋白大小 | 812 aa / 89.2 kDa |
| UniProt ID | Q9UBL0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoli; 额外: Cytosol; UniProt: Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 812 aa / 89.2 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=48 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=51.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001374, IPR036867, IPR051937, IPR024771; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; 额外: Cytosol | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 48 |
| PubMed broad count | 63 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TARPP |

**关键文献**:
1. The thymocyte-specific RNA-binding protein Arpp21 provides TCR repertoire diversity by binding to the 3'-UTR and promoting Rag1 mRNA expression.. *Nature communications*. PMID: 38467629
2. Genetic analysis of GLT8D1 and ARPP21 in Australian familial and sporadic amyotrophic lateral sclerosis.. *Neurobiology of aging*. PMID: 33581934
3. Recent progress of the genetics of amyotrophic lateral sclerosis and challenges of gene therapy.. *Frontiers in neuroscience*. PMID: 37250416
4. The RNA-binding protein ARPP21 controls dendritic branching by functionally opposing the miRNA it hosts.. *Nature communications*. PMID: 29581509
5. Mutation analysis of GLT8D1 and ARPP21 genes in amyotrophic lateral sclerosis patients from mainland China.. *Neurobiology of aging*. PMID: 31653410

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 51.5 |
| 高置信度残基 (pLDDT>90) 占比 | 11.0% |
| 置信残基 (pLDDT 70-90) 占比 | 8.5% |
| 中等置信 (pLDDT 50-70) 占比 | 12.1% |
| 低置信 (pLDDT<50) 占比 | 68.5% |
| 有序区域 (pLDDT>70) 占比 | 19.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=51.5），有序残基占 19.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001374, IPR036867, IPR051937, IPR024771; Pfam: PF01424, PF12752 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ARPP19 | 0.890 | 0.000 | — |
| PPP1R1B | 0.844 | 0.000 | — |
| ENSA | 0.670 | 0.000 | — |
| CAMK1 | 0.642 | 0.000 | — |
| CAMK2A | 0.555 | 0.000 | — |
| PCP4 | 0.554 | 0.000 | — |
| SLC6A1 | 0.543 | 0.000 | — |
| DRD1 | 0.532 | 0.000 | — |
| BCL11B | 0.530 | 0.051 | — |
| SV2B | 0.523 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SPRED1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 1
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=51.5 + PDB: 无 | pLDDT=51.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoli; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 1 interactions | 数据充分 |

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
1. ARPP21 — cAMP-regulated phosphoprotein 21，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小812 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 48 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=51.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UBL0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000172995-ARPP21/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ARPP21
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UBL0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ARPP21/IF_images/Rh30_1.jpg]]
![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ARPP21/IF_images/Rh30_2.jpg]]
![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ARPP21/IF_images/U2OS_1.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (approved)。来源: https://www.proteinatlas.org/ENSG00000172995-ARPP21/subcellular

![](https://images.proteinatlas.org/17303/1161_G10_2_red_green.jpg)
![](https://images.proteinatlas.org/17303/1161_G10_3_red_green.jpg)
![](https://images.proteinatlas.org/17303/139_B10_1_red_green.jpg)
![](https://images.proteinatlas.org/17303/139_B10_2_red_green.jpg)
![](https://images.proteinatlas.org/17303/166_B10_1_red_green.jpg)
![](https://images.proteinatlas.org/17303/166_B10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UBL0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
