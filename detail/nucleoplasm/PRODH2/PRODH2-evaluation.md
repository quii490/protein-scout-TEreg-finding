---
type: protein-evaluation
gene: "PRODH2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PRODH2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PRODH2 / HSPOX1, HYPDH |
| 蛋白名称 | Hydroxyproline dehydrogenase |
| 蛋白大小 | 460 aa / 50.9 kDa |
| UniProt ID | Q9UF12 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 460 aa / 50.9 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=23 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=87.6; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR029041, IPR002872, IPR015659; Pfam: PF01619 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.5/180** | |
| **归一化总分** | | | **64.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- mitochondrial inner membrane (GO:0005743)
- mitochondrion (GO:0005739)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 23 |
| PubMed broad count | 40 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HSPOX1, HYPDH |

**关键文献**:
1. A genome-scale gain-of-function CRISPR screen in CD8 T cells identifies proline metabolism as a means to enhance CAR-T therapy.. *Cell metabolism*. PMID: 35276062
2. Non-redundant functions of two proline dehydrogenase isoforms in Arabidopsis.. *BMC plant biology*. PMID: 20403182
3. Genetic cause and prevalence of hydroxyprolinemia.. *Journal of inherited metabolic disease*. PMID: 27139199
4. Differential control and function of Arabidopsis ProDH1 and ProDH2 genes on infection with biotrophic and necrotrophic pathogens.. *Molecular plant pathology*. PMID: 27526663
5. The new insight into the role of hydroxyproline in metabolism of cancer cells.. *Frontiers in cell and developmental biology*. PMID: 40454316

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.6 |
| 高置信度残基 (pLDDT>90) 占比 | 65.9% |
| 置信残基 (pLDDT 70-90) 占比 | 23.0% |
| 中等置信 (pLDDT 50-70) 占比 | 6.5% |
| 低置信 (pLDDT<50) 占比 | 4.6% |
| 有序区域 (pLDDT>70) 占比 | 88.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=87.6，有序区 88.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029041, IPR002872, IPR015659; Pfam: PF01619 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ALDH4A1 | 0.983 | 0.075 | — |
| PYCR3 | 0.924 | 0.071 | — |
| PYCR1 | 0.918 | 0.071 | — |
| PYCR2 | 0.917 | 0.071 | — |
| P4HA1 | 0.917 | 0.000 | — |
| P4HA2 | 0.915 | 0.000 | — |
| OAT | 0.785 | 0.000 | — |
| MT-CO2 | 0.735 | 0.000 | — |
| MT-CO1 | 0.722 | 0.091 | — |
| MT-CO3 | 0.721 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PRODH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SLC23A3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 2
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.6 + PDB: 无 | pLDDT=87.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 2 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PRODH2 — Hydroxyproline dehydrogenase，非常新颖，仅有少数基础研究。
2. 蛋白大小460 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 23 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UF12
- Protein Atlas: https://www.proteinatlas.org/ENSG00000250799-PRODH2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PRODH2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UF12
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UF12-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000250799-PRODH2/subcellular

![](https://images.proteinatlas.org/51287/1293_A11_1_red_green.jpg)
![](https://images.proteinatlas.org/51287/1293_A11_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O43272 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR029041;IPR002872;IPR015659; |
| Pfam | PF01619; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000250799-PRODH2/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
