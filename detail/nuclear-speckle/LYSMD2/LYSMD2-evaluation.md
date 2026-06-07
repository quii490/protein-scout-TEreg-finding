---
type: protein-evaluation
gene: "LYSMD2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LYSMD2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LYSMD2 |
| 蛋白名称 | LysM and putative peptidoglycan-binding domain-containing protein 2 |
| 蛋白大小 | 215 aa / 23.5 kDa |
| UniProt ID | Q8IV50 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Mitochondria; 额外: Nuclear bodies; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 215 aa / 23.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR018392, IPR045030, IPR036779; Pfam: PF01476 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 3 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **117.5/180** | |
| **归一化总分** | | | **65.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria; 额外: Nuclear bodies | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 2 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. LYSMD proteins promote activation of Rab32-family GTPases for lysosome-related organelle biogenesis.. *The Journal of cell biology*. PMID: 39078368
2. Genome-wide based model predicting recovery from portosystemic shunting after liver shunt attenuation in dogs.. *Journal of veterinary internal medicine*. PMID: 29770973

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.9 |
| 高置信度残基 (pLDDT>90) 占比 | 15.8% |
| 置信残基 (pLDDT 70-90) 占比 | 24.2% |
| 中等置信 (pLDDT 50-70) 占比 | 40.9% |
| 低置信 (pLDDT<50) 占比 | 19.1% |
| 有序区域 (pLDDT>70) 占比 | 40.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=66.9），有序残基占 40.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR018392, IPR045030, IPR036779; Pfam: PF01476 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LYSMD4 | 0.626 | 0.000 | — |
| TNFAIP8L3 | 0.444 | 0.000 | — |
| LYSMD3 | 0.432 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| LCN9 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| DUSP4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CEP19 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| Kif5b | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Klc3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| SLAIN2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| TWNK | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Ppp2r3a | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Mtcl2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| MZT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 3，IntAct interactions: 15
- 调控相关比例: 0 / 3 = 0%

**评价**: STRING 3 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.9 + PDB: 无 | pLDDT=66.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Mitochondria; 额外: Nuclear bodies | 待确认 |
| PPI | STRING + IntAct | 3 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. LYSMD2 — LysM and putative peptidoglycan-binding domain-containing protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小215 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=66.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IV50
- Protein Atlas: https://www.proteinatlas.org/ENSG00000140280-LYSMD2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LYSMD2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IV50
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Mitochondria (approved)。来源: https://www.proteinatlas.org/ENSG00000140280-LYSMD2/subcellular

![](https://images.proteinatlas.org/40460/484_G7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/40460/484_G7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/40460/489_G7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/40460/489_G7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/40460/492_G7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/40460/492_G7_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IV50-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8IV50 |
| SMART | SM00257; |
| UniProt Domain [FT] | DOMAIN 71..115; /note="LysM"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01118" |
| InterPro | IPR018392;IPR045030;IPR036779; |
| Pfam | PF01476; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000140280-LYSMD2/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
