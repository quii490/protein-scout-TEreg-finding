---
type: protein-evaluation
gene: "ANKRD42"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ANKRD42 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ANKRD42 |
| 蛋白名称 | Ankyrin repeat domain-containing protein 42 |
| 蛋白大小 | 389 aa / 43.1 kDa |
| UniProt ID | Q8N9B4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; 额外: Plasma membrane; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 389 aa / 43.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=77.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR050776, IPR002110, IPR036770, IPR018247; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Plasma membrane | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 4 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Lost and Found: The Family of NF-κB Inhibitors Is Larger than Assumed in Salmonid Fish.. *International journal of molecular sciences*. PMID: 37373375
2. A transcriptomic signature predicting septic outcome in patients undergoing autologous stem cell transplantation.. *Experimental hematology*. PMID: 29885947
3. hnRNPL-activated circANKRD42 back-splicing and circANKRD42-mediated crosstalk of mechanical stiffness and biochemical signal in lung fibrosis.. *Molecular therapy : the journal of the American Society of Gene Therapy*. PMID: 35278674
4. Genome-wide CRISPR screening identifies the pivotal role of ANKRD42 in colorectal cancer metastasis through EMT regulation.. *IUBMB life*. PMID: 38822625

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.5 |
| 高置信度残基 (pLDDT>90) 占比 | 52.2% |
| 置信残基 (pLDDT 70-90) 占比 | 17.5% |
| 中等置信 (pLDDT 50-70) 占比 | 10.0% |
| 低置信 (pLDDT<50) 占比 | 20.3% |
| 有序区域 (pLDDT>70) 占比 | 69.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=77.5，有序区 69.7%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050776, IPR002110, IPR036770, IPR018247; Pfam: PF12796 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SFRP5 | 0.835 | 0.048 | — |
| SFRP2 | 0.786 | 0.048 | — |
| SFRP1 | 0.687 | 0.048 | — |
| FRZB | 0.654 | 0.048 | — |
| IQUB | 0.624 | 0.091 | — |
| DNAAF1 | 0.599 | 0.048 | — |
| ZBBX | 0.594 | 0.000 | — |
| PCF11 | 0.592 | 0.067 | — |
| CCDC90B | 0.537 | 0.000 | — |
| HSDL2 | 0.511 | 0.099 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| H3C1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 2
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 2 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.5 + PDB: 无 | pLDDT=77.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Cytosol; 额外: Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 2 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. ANKRD42 — Ankyrin repeat domain-containing protein 42，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小389 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N9B4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000137494-ANKRD42/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ANKRD42
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N9B4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ANKRD42/IF_images/ANKRD42_IF_39917.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000137494-ANKRD42/subcellular

![](https://images.proteinatlas.org/39917/2177_E7_108_red_green.jpg)
![](https://images.proteinatlas.org/39917/2177_E7_83_red_green.jpg)
![](https://images.proteinatlas.org/39917/2178_E8_19_red_green.jpg)
![](https://images.proteinatlas.org/39917/2178_E8_31_red_green.jpg)
![](https://images.proteinatlas.org/39917/468_E2_1_red_green.jpg)
![](https://images.proteinatlas.org/39917/468_E2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8N9B4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8N9B4 |
| SMART | SM00248; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR050776;IPR002110;IPR036770;IPR018247; |
| Pfam | PF12796; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000137494-ANKRD42/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
