---
type: protein-evaluation
gene: "FSIP1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FSIP1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FSIP1 |
| 蛋白名称 | Fibrous sheath-interacting protein 1 |
| 蛋白大小 | 581 aa / 66.1 kDa |
| UniProt ID | Q8NA03 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Flagellar centriole, Annulus; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 581 aa / 66.1 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=22 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026246; Pfam: PF15554 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **107.5/180** | |
| **归一化总分** | | | **59.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Flagellar centriole, Annulus | Approved |
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
| PubMed strict count | 22 |
| PubMed broad count | 28 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. FSIP1 is correlated with estrogen receptor status and poor prognosis.. *Molecular carcinogenesis*. PMID: 31713931
2. FSIP1 regulates autophagy in breast cancer.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 30509973
3. FSIP1 binds HER2 directly to regulate breast cancer growth and invasiveness.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 28674022
4. Bi-allelic mutation in Fsip1 impairs acrosome vesicle formation and attenuates flagellogenesis in mice.. *Redox biology*. PMID: 33901807
5. Expression and clinicopathological significance of FSIP1 in breast cancer.. *Oncotarget*. PMID: 25826084

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.5 |
| 高置信度残基 (pLDDT>90) 占比 | 12.6% |
| 置信残基 (pLDDT 70-90) 占比 | 17.6% |
| 中等置信 (pLDDT 50-70) 占比 | 28.2% |
| 低置信 (pLDDT<50) 占比 | 41.7% |
| 有序区域 (pLDDT>70) 占比 | 30.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=60.5），有序残基占 30.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026246; Pfam: PF15554 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HSD17B10 | 0.982 | 0.000 | — |
| DHRS11 | 0.886 | 0.000 | — |
| TRMT10C | 0.836 | 0.000 | — |
| PRORP | 0.805 | 0.000 | — |
| AKAP4 | 0.803 | 0.230 | — |
| HADH | 0.630 | 0.000 | — |
| GPR176 | 0.610 | 0.000 | — |
| HUWE1 | 0.594 | 0.000 | — |
| ESR1 | 0.483 | 0.000 | — |
| ELAC2 | 0.479 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PHB1 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| POLR2A | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| S100P | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 3
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.5 + PDB: 无 | pLDDT=60.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Flagellar centriole, Annulus | 待确认 |
| PPI | STRING + IntAct | 15 + 3 interactions | 数据充分 |

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
1. FSIP1 — Fibrous sheath-interacting protein 1，非常新颖，仅有少数基础研究。
2. 蛋白大小581 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 22 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=60.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NA03
- Protein Atlas: https://www.proteinatlas.org/ENSG00000150667-FSIP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FSIP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NA03
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000150667-FSIP1/subcellular

![](https://images.proteinatlas.org/41002/2199_E6_13_blue_red_green.jpg)
![](https://images.proteinatlas.org/41002/2199_E6_39_blue_red_green.jpg)
![](https://images.proteinatlas.org/41002/2122_B2_1_red_green.jpg)
![](https://images.proteinatlas.org/41002/2122_B2_2_red_green.jpg)
![](https://images.proteinatlas.org/41002/477_B12_1_red_green.jpg)
![](https://images.proteinatlas.org/41002/477_B12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8NA03-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8NA03 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR026246; |
| Pfam | PF15554; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000150667-FSIP1/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
