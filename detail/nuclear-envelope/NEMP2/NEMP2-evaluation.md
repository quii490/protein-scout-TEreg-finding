---
type: protein-evaluation
gene: "NEMP2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NEMP2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NEMP2 / TMEM194B |
| 蛋白名称 | Nuclear envelope integral membrane protein 2 |
| 蛋白大小 | 417 aa / 48.7 kDa |
| UniProt ID | A6NFY4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus inner membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 417 aa / 48.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=80.2; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR019358; Pfam: PF10225 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 11 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **135.5/180** | |
| **归一化总分** | | | **75.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus inner membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nuclear envelope (GO:0005635)
- nuclear inner membrane (GO:0005637)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 4 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TMEM194B |

**关键文献**:
1. A Group of Weakly Bound to Neurons Extracellular Metallopeptidases (NEMPs).. *Neurochemical research*. PMID: 27350576
2. [Screening for Characteristic Genes of Different Traditional Chinese Medicine Syndromes of Psoriasis Vulgaris: A Study Based on Bioinformatics and Machine Learning].. *Sichuan da xue xue bao. Yi xue ban = Journal of Sichuan University. Medical science edition*. PMID: 38645867

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.2 |
| 高置信度残基 (pLDDT>90) 占比 | 23.0% |
| 置信残基 (pLDDT 70-90) 占比 | 58.3% |
| 中等置信 (pLDDT 50-70) 占比 | 12.0% |
| 低置信 (pLDDT<50) 占比 | 6.7% |
| 有序区域 (pLDDT>70) 占比 | 81.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=80.2，有序区 81.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019358; Pfam: PF10225 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ANKAR | 0.675 | 0.000 | — |
| OSGEPL1 | 0.565 | 0.000 | — |
| MFSD6 | 0.535 | 0.000 | — |
| DIRC1 | 0.526 | 0.000 | — |
| HIBCH | 0.507 | 0.000 | — |
| ORMDL1 | 0.479 | 0.000 | — |
| PHGR1 | 0.475 | 0.000 | — |
| RAN | 0.468 | 0.442 | — |
| BANF1 | 0.468 | 0.091 | — |
| INPP1 | 0.436 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RAN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CHRNA4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 11，IntAct interactions: 2
- 调控相关比例: 0 / 11 = 0%

**评价**: STRING 11 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.2 + PDB: 无 | pLDDT=80.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus inner membrane / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 11 + 2 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. NEMP2 — Nuclear envelope integral membrane protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小417 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A6NFY4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000189362-NEMP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NEMP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A6NFY4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000189362-NEMP2/subcellular

![](https://images.proteinatlas.org/57719/1006_G6_1_red_green.jpg)
![](https://images.proteinatlas.org/57719/1006_G6_2_red_green.jpg)
![](https://images.proteinatlas.org/57719/1011_G6_1_red_green.jpg)
![](https://images.proteinatlas.org/57719/1011_G6_7_red_green.jpg)
![](https://images.proteinatlas.org/57719/1203_C12_1_red_green.jpg)
![](https://images.proteinatlas.org/57719/1203_C12_5_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-A6NFY4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | A6NFY4 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR019358; |
| Pfam | PF10225; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000189362-NEMP2/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
