---
type: protein-evaluation
gene: "DCLK3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DCLK3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DCLK3 / DCAMKL3, DCDC3C, KIAA1765 |
| 蛋白名称 | Serine/threonine-protein kinase DCLK3 |
| 蛋白大小 | 648 aa / 73.8 kDa |
| UniProt ID | Q9C098 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Vesicles; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 648 aa / 73.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011009, IPR000719, IPR017441, IPR008271; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 9 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Vesicles | Approved |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 21 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DCAMKL3, DCDC3C, KIAA1765 |

**关键文献**:
1. Genome-wide association study of more than 40,000 bipolar disorder cases provides new insights into the underlying biology.. *Nature genetics*. PMID: 34002096
2. Genomic regulatory sequences in the pathogenesis of bipolar disorder.. *Frontiers in psychiatry*. PMID: 36824672
3. Insights from homozygous signatures of cervus nippon revealed genetic architecture for components of fitness.. *Mammalian genome : official journal of the International Mammalian Genome Society*. PMID: 39191871
4. The striatal kinase DCLK3 produces neuroprotection against mutant huntingtin.. *Brain : a journal of neurology*. PMID: 29534157
5. Deciphering the unique autoregulatory mechanisms and substrate specificity of the understudied DCLK3 kinase linked to neurodegenerative diseases.. *The Journal of biological chemistry*. PMID: 40902973

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.0 |
| 高置信度残基 (pLDDT>90) 占比 | 34.9% |
| 置信残基 (pLDDT 70-90) 占比 | 12.0% |
| 中等置信 (pLDDT 50-70) 占比 | 4.3% |
| 低置信 (pLDDT<50) 占比 | 48.8% |
| 有序区域 (pLDDT>70) 占比 | 46.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=63.0），有序残基占 46.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011009, IPR000719, IPR017441, IPR008271; Pfam: PF00069 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KLRB1 | 0.829 | 0.049 | — |
| DCX | 0.727 | 0.114 | — |
| SHOC2 | 0.632 | 0.000 | — |
| ZNF366 | 0.545 | 0.245 | — |
| INPPL1 | 0.495 | 0.000 | — |
| BMP1 | 0.491 | 0.000 | — |
| ZNF12 | 0.467 | 0.245 | — |
| TRANK1 | 0.462 | 0.062 | — |
| DNPH1 | 0.453 | 0.000 | — |
| CRYM | 0.452 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| 39071" | psi-mi:"MI:0096"(pull down) | pubmed:17721511|imex:IM-19952 |
| CDK5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:23602568|imex:IM-17935 |
| BTBD9 | psi-mi:"MI:0018"(two hybrid) | pubmed:29534157|imex:IM-26152 |
| SALL1 | psi-mi:"MI:0018"(two hybrid) | pubmed:29534157|imex:IM-26152 |
| TRIM39 | psi-mi:"MI:0018"(two hybrid) | pubmed:29534157|imex:IM-26152 |
| TADA3 | psi-mi:"MI:0018"(two hybrid) | pubmed:29534157|imex:IM-26152 |
| ZNF12 | psi-mi:"MI:0018"(two hybrid) | pubmed:29534157|imex:IM-26152 |
| ZNF292 | psi-mi:"MI:0018"(two hybrid) | pubmed:29534157|imex:IM-26152 |
| ZNF366 | psi-mi:"MI:0018"(two hybrid) | pubmed:29534157|imex:IM-26152 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 9
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 9 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.0 + PDB: 无 | pLDDT=63.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Cytosol; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 9 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DCLK3 — Serine/threonine-protein kinase DCLK3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小648 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=63.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9C098
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163673-DCLK3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DCLK3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9C098
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/DCLK3/IF_images/DCLK3_IF_blue_red_green.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000163673-DCLK3/subcellular

![](https://images.proteinatlas.org/53234/2019_E6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/53234/2019_E6_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/53234/2036_C6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/53234/2036_C6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/53234/2042_A7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/53234/2042_A7_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9C098-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
