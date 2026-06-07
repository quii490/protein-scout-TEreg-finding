---
type: protein-evaluation
gene: "TTC9"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TTC9 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TTC9 / KIAA0227, TTC9A |
| 蛋白名称 | Tetratricopeptide repeat protein 9A |
| 蛋白大小 | 222 aa / 24.4 kDa |
| UniProt ID | Q92623 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear bodies; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 222 aa / 24.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=8 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=78.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR050754, IPR011990, IPR013105, IPR019734; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.0/180** | |
| **归一化总分** | | | **73.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies | Approved |
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
| PubMed strict count | 8 |
| PubMed broad count | 19 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0227, TTC9A |

**关键文献**:
1. Identification of tetratricopeptide repeat domain 9, a hormonally regulated protein.. *Biochemical and biophysical research communications*. PMID: 16678794
2. Knockdown of TTC9 inhibits the proliferation, migration and invasion, but induces the apoptosis of lung adenocarcinoma cells.. *Heliyon*. PMID: 36339754
3. DNA methylation-based diagnostic and prognostic biomarkers of nasopharyngeal carcinoma patients.. *Medicine*. PMID: 32541515
4. The local microenvironment instigates the regulation of mammary tetratricopeptide repeat domain 9A during lactation and involution through local regulation of the activity of estrogen receptor α.. *Biochemical and biophysical research communications*. PMID: 22917536
5. Effect of dietary supplementation with yeast cell wall extracts on performance and gut response in broiler chickens.. *Journal of animal science and biotechnology*. PMID: 32377338

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.6 |
| 高置信度残基 (pLDDT>90) 占比 | 60.4% |
| 置信残基 (pLDDT 70-90) 占比 | 7.2% |
| 中等置信 (pLDDT 50-70) 占比 | 5.0% |
| 低置信 (pLDDT<50) 占比 | 27.5% |
| 有序区域 (pLDDT>70) 占比 | 67.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=78.6，有序区 67.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050754, IPR011990, IPR013105, IPR019734; Pfam: PF07719 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PGR | 0.641 | 0.055 | — |
| C6orf132 | 0.581 | 0.067 | — |
| WDR17 | 0.518 | 0.110 | — |
| INSYN2B | 0.491 | 0.000 | — |
| ADM5 | 0.478 | 0.000 | — |
| GRAMD1C | 0.473 | 0.000 | — |
| OR13C8 | 0.472 | 0.000 | — |
| MAPK14 | 0.447 | 0.043 | — |
| TMEM191B | 0.445 | 0.000 | — |
| RASEF | 0.440 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NUP98 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| PRIMA1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| MAPT | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:35063084|imex:IM-29773 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 3
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.6 + PDB: 无 | pLDDT=78.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nuclear bodies | 待确认 |
| PPI | STRING + IntAct | 15 + 3 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TTC9 — Tetratricopeptide repeat protein 9A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小222 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q92623
- Protein Atlas: https://www.proteinatlas.org/ENSG00000133985-TTC9/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TTC9
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q92623
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (approved)。来源: https://www.proteinatlas.org/ENSG00000133985-TTC9/subcellular

![](https://images.proteinatlas.org/79473/2043_C5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/79473/2043_C5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/79473/2053_F4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/79473/2053_F4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/79473/2059_F2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/79473/2059_F2_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q92623-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q92623 |
| SMART | SM00028; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR050754;IPR011990;IPR013105;IPR019734; |
| Pfam | PF07719; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000133985-TTC9/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
