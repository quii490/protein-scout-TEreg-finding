---
type: protein-evaluation
gene: "EFCC1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EFCC1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EFCC1 / C3orf73, CCDC48 |
| 蛋白名称 | EF-hand and coiled-coil domain-containing protein 1 |
| 蛋白大小 | 598 aa / 65.7 kDa |
| UniProt ID | Q9HA90 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 598 aa / 65.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR031601, IPR002048; Pfam: PF15799 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **129.5/180** | |
| **归一化总分** | | | **71.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3 |
| PubMed broad count | 5 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C3orf73, CCDC48 |

**关键文献**:
1. Whole-Exome Sequencing for Identification of Potential Sex-Biased Variants in Kawasaki Disease Patients.. *Inflammation*. PMID: 37462885
2. Clinical response under MEK inhibitor alone in metastatic melanoma with a novel fusion involving the RAF1 gene.. *Melanoma research*. PMID: 36866640
3. Decreased expression of EFCC1 and its prognostic value in lung adenocarcinoma.. *Annals of translational medicine*. PMID: 31930073

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.6 |
| 高置信度残基 (pLDDT>90) 占比 | 25.1% |
| 置信残基 (pLDDT 70-90) 占比 | 25.1% |
| 中等置信 (pLDDT 50-70) 占比 | 20.6% |
| 低置信 (pLDDT<50) 占比 | 29.3% |
| 有序区域 (pLDDT>70) 占比 | 50.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=68.6），有序残基占 50.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR031601, IPR002048; Pfam: PF15799 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ISY1 | 0.600 | 0.000 | — |
| ISY1-RAB43 | 0.581 | 0.000 | — |
| TMEM89 | 0.580 | 0.000 | — |
| HDHD5 | 0.571 | 0.000 | — |
| PET100 | 0.536 | 0.000 | — |
| EFCAB11 | 0.508 | 0.000 | — |
| FAM71E1 | 0.483 | 0.000 | — |
| EFHC2 | 0.473 | 0.000 | — |
| ACBD5 | 0.461 | 0.000 | — |
| ACBD4 | 0.461 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CUL1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 1
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.6 + PDB: 无 | pLDDT=68.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Cytosol | 待确认 |
| PPI | STRING + IntAct | 15 + 1 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. EFCC1 — EF-hand and coiled-coil domain-containing protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小598 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=68.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9HA90
- Protein Atlas: https://www.proteinatlas.org/ENSG00000114654-EFCC1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EFCC1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9HA90
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000114654-EFCC1/subcellular

![](https://images.proteinatlas.org/50888/2231_G4_1_red_green.jpg)
![](https://images.proteinatlas.org/50888/2231_G4_4_red_green.jpg)
![](https://images.proteinatlas.org/50888/2235_G2_3_red_green.jpg)
![](https://images.proteinatlas.org/50888/2235_G2_5_red_green.jpg)
![](https://images.proteinatlas.org/76069/2231_A5_2_red_green.jpg)
![](https://images.proteinatlas.org/76069/2231_A5_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9HA90-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9HA90 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 54..89; /note="EF-hand"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00448" |
| InterPro | IPR031601;IPR002048; |
| Pfam | PF15799; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000114654-EFCC1/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
