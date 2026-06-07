---
type: protein-evaluation
gene: "PRRT4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PRRT4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PRRT4 |
| 蛋白名称 | Proline-rich transmembrane protein 4 |
| 蛋白大小 | 899 aa / 92.7 kDa |
| UniProt ID | C9JH25 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Peroxisomes, Plasma membrane; UniProt: Membrane |
| 蛋白大小 | 8/10 | ×1 | 8 | 899 aa / 92.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=52.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR059081, IPR052836; Pfam: PF25987 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 6 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.0/180** | |
| **归一化总分** | | | **64.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Peroxisomes, Plasma membrane | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 4 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Pan-cancer analysis reveals PRRT4 is a potential prognostic factor of AML.. *Hematology (Amsterdam, Netherlands)*. PMID: 40277163
2. Bioinformatics analysis of potential Key lncRNA-miRNA-mRNA molecules as prognostic markers and important ceRNA axes in gastric cancer.. *American journal of cancer research*. PMID: 35693096
3. Whole Exome Sequencing Revealed Variants That Predict Pulmonary Artery Involvement in Patients with Takayasu Arteritis.. *Journal of inflammation research*. PMID: 36046661
4. Identification of Ultrasound-Sensitive Prognostic Markers of LAML and Construction of Prognostic Risk Model Based on WGCNA.. *Journal of oncology*. PMID: 36816364

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 52.6 |
| 高置信度残基 (pLDDT>90) 占比 | 11.2% |
| 置信残基 (pLDDT 70-90) 占比 | 16.7% |
| 中等置信 (pLDDT 50-70) 占比 | 8.6% |
| 低置信 (pLDDT<50) 占比 | 63.5% |
| 有序区域 (pLDDT>70) 占比 | 27.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=52.6），有序残基占 27.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR059081, IPR052836; Pfam: PF25987 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KIAA0825 | 0.474 | 0.000 | — |
| RBM28 | 0.463 | 0.000 | — |
| ANKDD1B | 0.447 | 0.000 | — |
| ARMH4 | 0.434 | 0.000 | — |
| SMIM1 | 0.430 | 0.000 | — |
| KLHDC8A | 0.416 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CEACAM8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| KCNJ2 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:32541000|imex:IM-29166 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 6，IntAct interactions: 2
- 调控相关比例: 0 / 6 = 0%

**评价**: STRING 6 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=52.6 + PDB: 无 | pLDDT=52.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoplasm; 额外: Peroxisomes, Plasma membrane | 一致 |
| PPI | STRING + IntAct | 6 + 2 interactions | 数据充分 |

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
1. PRRT4 — Proline-rich transmembrane protein 4，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小899 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=52.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/C9JH25
- Protein Atlas: https://www.proteinatlas.org/ENSG00000224940-PRRT4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PRRT4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/C9JH25
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000224940-PRRT4/subcellular

![](https://images.proteinatlas.org/46373/1006_B3_3_red_green.jpg)
![](https://images.proteinatlas.org/46373/1006_B3_4_red_green.jpg)
![](https://images.proteinatlas.org/46373/1043_D1_1_red_green.jpg)
![](https://images.proteinatlas.org/46373/1043_D1_2_red_green.jpg)
![](https://images.proteinatlas.org/46373/1220_B7_5_red_green.jpg)
![](https://images.proteinatlas.org/46373/1220_B7_7_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-C9JH25-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | C9JH25 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR059081;IPR052836; |
| Pfam | PF25987; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000224940-PRRT4/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
