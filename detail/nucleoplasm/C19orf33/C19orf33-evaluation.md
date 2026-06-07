---
type: protein-evaluation
gene: "C19orf33"
date: 2026-06-01
tags: [protein-scout, nucleoplasm, evaluation]
status: scored
---

## C19orf33 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | C19orf33 |
| 蛋白全名 | Immortalization up-regulated protein |
| 蛋白大小 | 106 aa / 10.9 kDa |
| UniProt ID | Q9GZP8 |
| 别名 | 无 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | 28.0 | UniProt Nucleus (ECO:0000269); GO nucleoplasm IDA:HPA + nucleus IDA:HGNC-UCL |
| 蛋白大小 | 10/10 | ×1 | 10.0 | 106 aa, 10.9 kDa — 极小型蛋白 |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed strict=11 (≤20) |
| 三维结构 | 5/10 | ×3 | 15.0 | AlphaFold pLDDT 62.4; 无 PDB 实验结构 |
| 调控结构域 | 3/10 | ×2 | 6.0 | IPR026621 单一家族; Pfam PF15761; 功能未表征 |
| PPI 网络 | 3/10 | ×3 | 9.0 | STRING 弱 (textmining为主); IntAct 1条 (DVL2 coIP) |
| **加权总分** | | | **118/180**** | |
| 互证加分 | | | +1.0 | UniProt experimental + GO IDA:HPA 双源互证 |
| **归一化总分 (÷1.83)** | | | **64.5/100**** | |

PubMed strict: 11

### 3. 核定位证据

#### 3.1 定位来源

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt | Nucleus (ECO:0000269) | Experimental |
| GO-CC | cytosol IDA:HPA; nucleolus IEA:Ensembl; **nucleoplasm IDA:HPA**; nucleus IDA:HGNC-UCL; plasma membrane IDA:HPA | Direct assay (nucleoplasm) |
| HPA IF | Nucleoplasm (main), Plasma membrane (additional) | HPA localization available |

#### 3.2 HPA IF 数据

- **HPA reliability**: HPA subcellular localization available (antibody-based IF)
- **Main location**: Nucleoplasm
- **Additional location**: Plasma membrane
- **IF image**: Full red_green IF image acquired from HPA (antibody HPA044206, cell line U-2 OS)

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/C19orf33/IF_images/C19orf33_IF_red_green.jpg]]

**IF image note**: HPA IF 原图已成功获取 (red_green channel, 482 KB)。图像显示明确的核质染色信号，与 GO nucleoplasm IDA:HPA 注释一致。

C19orf33 具有双源实验级核定位证据：UniProt 实验级 Nucleus 注释 (ECO:0000269) 和 GO nucleoplasm IDA:HPA。HPA IF 图像提供了视觉确认。同时 GO-CC 包含 cytosol、nucleolus (IEA only) 和 plasma membrane，提示多区室分布可能。

### 4. 蛋白大小

106 aa / 10.9 kDa。极小型蛋白，适合作为研究靶标。无信号肽或跨膜结构域预测。

### 5. 研究现状

| 指标 | 数值 |
|---|---|
| PubMed strict (Title/Abstract) | 11 |
| PubMed broad | 23 |
| 关键文献 | |

| PMID | 期刊 | 日期 | 标题 |
|---|---|---|---|
| 29271998 | Eur Rev Med Pharmacol Sci | 2017 Dec | Identification of multifocal breast cancer-associated lncRNAs |
| 38071887 | Pathol Res Pract | 2024 Jan | Dedifferentiation and metastasis in pancreatic ductal adenocarcinoma |
| 38542276 | Int J Mol Sci | 2024 Mar | Gene regulatory network in azacitidine-sensitive/resistant cells |
| 37397364 | Front Oncol | 2023 | Cancer-associated fibroblasts gene landscape in prognosis |
| 34245600 | Neurourol Urodyn | 2021 Sep | Key genes in urothelial cells in interstitial cystitis |

文献均为癌症/疾病基因组关联分析，C19orf33 出现在差异表达基因列表或预后模型中。无独立功能研究。蛋白功能完全未知。

### 6. 三维结构

| 指标 | 数值 |
|---|---|
| AlphaFold entry | AF-Q9GZP8-F1 |
| mean pLDDT | 62.4 |
| pLDDT >90 | 0.0% |
| pLDDT 70–90 | 15.1% |
| pLDDT 50–70 | 81.1% |
| pLDDT <50 | 3.8% |
| PDB | 无实验结构 |


**PAE**: PAE 图像已获取。pLDDT 62.4 表明蛋白整体折叠置信度中等，大部分残基在 50–70 范围（低置信度折叠），无高置信度 (>90) 区域。3.8% 残基 pLDDT <50（无序区）。

#### 结构域

| 数据库 | ID | 描述 |
|---|---|---|
| InterPro | IPR026621 | C19orf33 family |
| Pfam | PF15761 | DUF4684 (Domain of Unknown Function) |

单一未表征结构域 (DUF4684)，无已知功能注释。无 Pfam clan 关联。

### 7. PPI 网络

#### 实验验证互作

| Partner | 来源 | 方法 | PMID | 功能类别 |
|---|---|---|---|---|
| DVL2 | IntAct | anti tag coimmunoprecipitation | 26496610 | Wnt signaling (Dishevelled) |

#### STRING 互作 (top 5)

| Partner | Score | Experimental | Database | 功能类别 |
|---|---|---|---|---|
| SPINT2 | 0.882 | 0 | 0 | Serine peptidase inhibitor (textmining) |
| PPP1R14A | 0.780 | 0 | 0 | Protein phosphatase 1 inhibitor (textmining) |
| OR14A16 | 0.433 | 0 | 0 | Olfactory receptor (textmining) |
| PPP1R12A | 0.428 | 0 | 0 | Protein phosphatase 1 regulatory (textmining) |
| PPP1CB | 0.425 | 0 | 0 | Protein phosphatase catalytic (textmining) |

**PPI 评述**: PPI 网络极弱。IntAct 仅 1 条 coIP 记录 (DVL2, Wnt 信号 Dishevelled 蛋白)。STRING 高分互作 (SPINT2 0.882, PPP1R14A 0.780) 均为 textmining 驱动，无实验或数据库支持。UniProt 无 curated interaction。DVL2 是 Wnt 通路胞质信号蛋白，其与 C19orf33 的 coIP 需要独立验证。PPI 网络不支持特定核功能或复合体。

### 8. 总体评价

C19orf33 是极小型 (106 aa) 核蛋白，具有双源实验级核定位证据 (UniProt ECO:0000269 + GO nucleoplasm IDA:HPA)。HPA IF 原图已成功获取并嵌入，显示核质染色信号。

主要弱项：
- AlphaFold pLDDT 仅 62.4，蛋白整体折叠置信度低
- 唯一结构域 DUF4684 功能完全未知
- PPI 网络极弱 (1 IntAct + textmining-only STRING)
- 无独立功能研究，仅以列表基因形式出现在癌症预后模型中

归一化总分 65.0/100。建议作为低-中置信度 nucleoplasm 候选。主要优势是核定位证据质量 (实验级 + IF 图像) 和蛋白极小 (10.9 kDa)。后续应优先进行功能实验。

### 9. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q9GZP8
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9GZP8
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=C19orf33
- HPA: https://www.proteinatlas.org/search/C19orf33


#### PPI 网络
| Partner | Source | Score/Evidence |
|---|---|---|
| SPINT2 | STRING | 0.882 |
| PPP1R14A | STRING | 0.78 |
| OR14A16 | STRING | 0.433 |
| PPP1R12A | STRING | 0.428 |
| PPP1CB | STRING | 0.425 |
| DVL2 | IntAct | psi-mi:"MI:0007"(anti tag coim |


#### 关键文献
| PMID | 标题 |
|---|---|
| 29271998 | The identification of multifocal breast cancer-associated long non-coding RNAs. |
| 38071887 | Unraveling dedifferentiation and metastasis traces in pancreatic ductal adenocarcinoma ductal cells: |
| 38542276 | Differential Gene Regulatory Network Analysis between Azacitidine-Sensitive and -Resistant Cell Line |
| 37397364 | Development and validation of cancer-associated fibroblasts-related gene landscape in prognosis and  |
| 34245600 | Identification of key genes in human urothelial cells corresponding to interstitial cystitis/bladder |

HPA IF 图像已本地嵌入。



**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。



<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9GZP8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9GZP8 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR026621; |
| Pfam | PF15761; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000167644-C19orf33/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| NPM1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
