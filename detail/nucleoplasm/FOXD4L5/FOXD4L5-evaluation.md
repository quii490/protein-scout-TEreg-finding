---
type: protein-evaluation
gene: "FOXD4L5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FOXD4L5 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FOXD4L5 |
| 蛋白名称 | Forkhead box protein D4-like 5 |
| 蛋白大小 | 416 aa / 45.8 kDa |
| UniProt ID | Q5VV16 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 416 aa / 45.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=56.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001766, IPR050211, IPR018122, IPR030456, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 2 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **137.5/180** | |
| **归一化总分** | | | **76.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 1 |
| 别名(未计入scoring) | 无 |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 56.2 |
| 高置信度残基 (pLDDT>90) 占比 | 15.9% |
| 置信残基 (pLDDT 70-90) 占比 | 7.9% |
| 中等置信 (pLDDT 50-70) 占比 | 21.2% |
| 低置信 (pLDDT<50) 占比 | 55.0% |
| 有序区域 (pLDDT>70) 占比 | 23.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=56.2），有序残基占 23.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001766, IPR050211, IPR018122, IPR030456, IPR036388; Pfam: PF00250 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ANKRD20A2 | 0.658 | 0.059 | — |
| ZNF595 | 0.535 | 0.096 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 2，IntAct interactions: 0
- 调控相关比例: 0 / 2 = 0%

**评价**: STRING 2 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=56.2 + PDB: 无 | pLDDT=56.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 2 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. FOXD4L5 — Forkhead box protein D4-like 5，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小416 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=56.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5VV16
- Protein Atlas: https://www.proteinatlas.org/ENSG00000204779-FOXD4L5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FOXD4L5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5VV16
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FOXD4L5/IF_images/A-431_1.jpg]]
![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FOXD4L5/IF_images/U-251MG_1.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000204779-FOXD4L5/subcellular

![](https://images.proteinatlas.org/12836/136_F8_1_red_green.jpg)
![](https://images.proteinatlas.org/12836/136_F8_2_red_green.jpg)
![](https://images.proteinatlas.org/12836/97_F8_1_red_green.jpg)
![](https://images.proteinatlas.org/12836/97_F8_2_red_green.jpg)
![](https://images.proteinatlas.org/12836/99_F8_1_red_green.jpg)
![](https://images.proteinatlas.org/12836/99_F8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5VV16-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q5VV16 |
| SMART | SM00339; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR001766;IPR050211;IPR018122;IPR030456;IPR036388;IPR036390; |
| Pfam | PF00250; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000204779-FOXD4L5/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
