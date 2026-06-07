---
type: protein-evaluation
gene: "SYCP2L"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SYCP2L 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SYCP2L / C6orf177, NO145 |
| 蛋白名称 | Synaptonemal complex protein 2-like |
| 蛋白大小 | 812 aa / 93.6 kDa |
| UniProt ID | Q5T4T6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus; Chromosome, centromere |
| 蛋白大小 | 8/10 | ×1 | 8 | 812 aa / 93.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR024835, IPR041322, IPR040560; Pfam: PF18581, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 13 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **136.0/180** | |
| **归一化总分** | | | **75.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus; Chromosome, centromere | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- condensed chromosome, centromeric region (GO:0000779)
- female germ cell nucleus (GO:0001674)
- lateral element (GO:0000800)
- nucleoplasm (GO:0005654)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 14 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C6orf177, NO145 |

**关键文献**:
1. Involvement of SYCP2L and TDRD3 gene variants on ovarian reserve and reproductive outcomes: a cross-sectional study.. *JBRA assisted reproduction*. PMID: 37417852
2. Comparative transcriptome analysis of Indian domestic duck reveals candidate genes associated with egg production.. *Scientific reports*. PMID: 35768515
3. Accelerated reproductive aging in females lacking a novel centromere protein SYCP2L.. *Human molecular genetics*. PMID: 26362258
4. Testicular transcriptome alterations in zebrafish (Danio rerio) exposure to 17β-estradiol.. *Chemosphere*. PMID: 30465971
5. Prostate tumor DNA methylation is associated with cigarette smoking and adverse prostate cancer outcomes.. *Cancer*. PMID: 27142338

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.9 |
| 高置信度残基 (pLDDT>90) 占比 | 34.9% |
| 置信残基 (pLDDT 70-90) 占比 | 19.8% |
| 中等置信 (pLDDT 50-70) 占比 | 6.2% |
| 低置信 (pLDDT<50) 占比 | 39.2% |
| 有序区域 (pLDDT>70) 占比 | 54.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=65.9），有序残基占 54.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR024835, IPR041322, IPR040560; Pfam: PF18581, PF18584 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TMEM150B | 0.610 | 0.000 | — |
| MCM8 | 0.599 | 0.000 | — |
| SCP2 | 0.598 | 0.000 | — |
| ELOVL2 | 0.554 | 0.000 | — |
| TMEM200C | 0.542 | 0.000 | — |
| MCM8-2 | 0.513 | 0.000 | — |
| BRSK1 | 0.506 | 0.000 | — |
| UIMC1 | 0.479 | 0.000 | — |
| HK3 | 0.479 | 0.000 | — |
| ELOVL5 | 0.474 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000283141.6 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| CCT2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| PARP1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 13，IntAct interactions: 3
- 调控相关比例: 0 / 13 = 0%

**评价**: STRING 13 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.9 + PDB: 无 | pLDDT=65.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Chromosome, centromere / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 13 + 3 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. SYCP2L — Synaptonemal complex protein 2-like，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小812 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=65.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5T4T6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000153157-SYCP2L/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SYCP2L
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5T4T6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000153157-SYCP2L/subcellular

![](https://images.proteinatlas.org/34679/1182_A4_1_red_green.jpg)
![](https://images.proteinatlas.org/34679/1182_A4_2_red_green.jpg)
![](https://images.proteinatlas.org/34679/433_H2_1_red_green.jpg)
![](https://images.proteinatlas.org/34679/433_H2_2_red_green.jpg)
![](https://images.proteinatlas.org/34679/440_H2_1_red_green.jpg)
![](https://images.proteinatlas.org/34679/440_H2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5T4T6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q5T4T6 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR024835;IPR041322;IPR040560; |
| Pfam | PF18581;PF18584; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000153157-SYCP2L/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
