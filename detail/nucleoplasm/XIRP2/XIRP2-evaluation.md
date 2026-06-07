---
type: protein-evaluation
gene: "XIRP2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## XIRP2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | XIRP2 / CMYA3 |
| 蛋白名称 | Xin actin-binding repeat-containing protein 2 |
| 蛋白大小 | 3374 aa / 382.3 kDa |
| UniProt ID | A4UGR9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Plasma membrane; 额外: Nucleoplasm; UniProt: Cell junction |
| 蛋白大小 | 0/10 | ×1 | 0 | 3374 aa / 382.3 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=51 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=49.4; PDB: 4F14 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR012510, IPR030072; Pfam: PF08043 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.5/180** | |
| **归一化总分** | | | **49.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane; 额外: Nucleoplasm | Approved |
| UniProt | Cell junction | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cell-cell junction (GO:0005911)
- Z disc (GO:0030018)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 51 |
| PubMed broad count | 75 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CMYA3 |

**关键文献**:
1. Single-cell and spatial transcriptomics of the infarcted heart define the dynamic onset of the border zone in response to mechanical destabilization.. *Nature cardiovascular research*. PMID: 39086770
2. Interleukin 11 therapy causes acute left ventricular dysfunction.. *Cardiovascular research*. PMID: 39383190
3. Identifying modifier genes for hypertrophic cardiomyopathy.. *Journal of molecular and cellular cardiology*. PMID: 32470469
4. XIRP2, an actin-binding protein essential for inner ear hair-cell stereocilia.. *Cell reports*. PMID: 25772365
5. Identification of Clinical Value and Biological Effects of XIRP2 Mutation in Hepatocellular Carcinoma.. *Biology*. PMID: 39194571

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 49.4 |
| 高置信度残基 (pLDDT>90) 占比 | 6.7% |
| 置信残基 (pLDDT 70-90) 占比 | 11.0% |
| 中等置信 (pLDDT 50-70) 占比 | 15.6% |
| 低置信 (pLDDT<50) 占比 | 66.6% |
| 有序区域 (pLDDT>70) 占比 | 17.7% |
| 可用 PDB 条目 | 4F14 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=49.4），有序残基占 17.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR012510, IPR030072; Pfam: PF08043 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FSCN2 | 0.885 | 0.046 | — |
| CSRP3 | 0.881 | 0.049 | — |
| TRIOBP | 0.868 | 0.000 | — |
| ACTN2 | 0.860 | 0.094 | — |
| PLS1 | 0.857 | 0.045 | — |
| LMOD2 | 0.853 | 0.000 | — |
| MYH7 | 0.849 | 0.100 | — |
| MYO7A | 0.839 | 0.045 | — |
| CLIC5 | 0.839 | 0.053 | — |
| MYH9 | 0.838 | 0.100 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DYSF | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| NSMAF | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| H2BC9 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| PNPT1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H1-5 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H1-4 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| CRY1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27254|pubmed:23133559 |
| LRRK2 | psi-mi:"MI:0089"(protein array) | pubmed:24510904|imex:IM-22223 |
| ATE1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| BAG3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=49.4 + PDB: 4F14 | pLDDT=49.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell junction / Plasma membrane; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐

**核心优势**:
1. XIRP2 — Xin actin-binding repeat-containing protein 2，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小3374 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 51 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=49.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A4UGR9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163092-XIRP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=XIRP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A4UGR9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000163092-XIRP2/subcellular

![](https://images.proteinatlas.org/74599/1708_B2_28_cr57eaad1ed1b55_red_green.jpg)
![](https://images.proteinatlas.org/74599/1708_B2_8_cr57eaad0f887c3_red_green.jpg)
![](https://images.proteinatlas.org/74599/1751_G4_5_cr57fd2fa615234_red_green.jpg)
![](https://images.proteinatlas.org/74599/1751_G4_8_cr57fd2faf1a9d9_red_green.jpg)
![](https://images.proteinatlas.org/74599/1767_C5_18_cr594ba87eefaa4_red_green.jpg)
![](https://images.proteinatlas.org/74599/1767_C5_7_cr594ba87eeebaf_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | A4UGR9 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR012510;IPR030072; |
| Pfam | PF08043; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000163092-XIRP2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| NEB | Intact, Biogrid | false |
| NEBL | Intact, Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
