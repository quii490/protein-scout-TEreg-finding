---
type: protein-evaluation
gene: "GOLGA6D"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GOLGA6D 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GOLGA6D |
| 蛋白名称 | Golgin subfamily A member 6D |
| 蛋白大小 | 693 aa / 79.9 kDa |
| UniProt ID | P0CG33 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Vesicles; 额外: Nucleoplasm, Centrosome; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 693 aa / 79.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=72.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR024858, IPR043976; Pfam: PF15070 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 3 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.5/180** | |
| **归一化总分** | | | **67.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Nucleoplasm, Centrosome | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cis-Golgi network (GO:0005801)
- Golgi cis cisterna (GO:0000137)
- Golgi cisterna membrane (GO:0032580)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 0 |
| 别名(未计入scoring) | 无 |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.9 |
| 高置信度残基 (pLDDT>90) 占比 | 47.0% |
| 置信残基 (pLDDT 70-90) 占比 | 14.9% |
| 中等置信 (pLDDT 50-70) 占比 | 6.9% |
| 低置信 (pLDDT<50) 占比 | 31.2% |
| 有序区域 (pLDDT>70) 占比 | 61.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=72.9，有序区 61.9%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR024858, IPR043976; Pfam: PF15070 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GOLGB1 | 0.489 | 0.420 | — |
| STX5 | 0.482 | 0.420 | — |
| GOSR1 | 0.459 | 0.420 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 3，IntAct interactions: 1
- 调控相关比例: 0 / 3 = 0%

**评价**: STRING 3 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.9 + PDB: 无 | pLDDT=72.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Vesicles; 额外: Nucleoplasm, Centrosome | 一致 |
| PPI | STRING + IntAct | 3 + 1 interactions | 数据充分 |

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
1. GOLGA6D — Golgin subfamily A member 6D，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小693 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P0CG33
- Protein Atlas: https://www.proteinatlas.org/ENSG00000140478-GOLGA6D/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GOLGA6D
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P0CG33
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (approved)。来源: https://www.proteinatlas.org/ENSG00000140478-GOLGA6D/subcellular

![](https://images.proteinatlas.org/72134/1961_F10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/72134/1961_F10_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/72134/1968_G6_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/72134/1968_G6_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/72134/1980_F5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/72134/1980_F5_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P0CG33-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P0CG33 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR024858;IPR043976; |
| Pfam | PF15070; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000140478-GOLGA6D/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
