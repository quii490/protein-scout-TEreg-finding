---
type: protein-evaluation
gene: "CSTF3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CSTF3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CSTF3 |
| 蛋白名称 | Cleavage stimulation factor subunit 3 |
| 蛋白大小 | 717 aa / 82.9 kDa |
| UniProt ID | Q12996 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | x4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | x1 | 10 | 717 aa / 82.9 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 9/10 | x3 | 27 | AlphaFold v6 pLDDT=86.0; PDB: 6B3X, 6URO, 7ZY4 |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR003107, IPR045243, IPR008847, IPR011990; Pfam:  |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **150.5/180** | |
| **归一化总分** | | | **83.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- mRNA cleavage stimulating factor complex (GO:0005848)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 24 |
| 别名(未计入scoring) |  |

**关键文献**:
1. YTHDC1 as a tumor progression suppressor through modulating FSP1-dependent ferroptosis suppression in lung cancer.. *Cell death and differentiation*. PMID: 37903990
2. Splicing targeting drugs highlight intron retention as an actionable vulnerability in advanced prostate cancer.. *Journal of experimental & clinical cancer research : CR*. PMID: 38413979
3. CSTF3 contributes to platinum resistance in ovarian cancer through alternative polyadenylation of lncRNA NEAT1 and generating the short isoform NEAT1_1.. *Cell death & disease*. PMID: 38898019
4. Association of expression of ZNF606 gene from monocytes with the risk of coronary artery disease.. *Clinical biochemistry*. PMID: 30130524
5. Alternative Polyadenylation in Triple-Negative Breast Tumors Allows NRAS and c-JUN to Bypass PUMILIO Posttranscriptional Regulation.. *Cancer research*. PMID: 27758885

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.0 |
| 高置信度残基 (pLDDT>90) 占比 | 67.2% |
| 置信残基 (pLDDT 70-90) 占比 | 18.0% |
| 中等置信 (pLDDT 50-70) 占比 | 4.6% |
| 低置信 (pLDDT<50) 占比 | 10.2% |
| 有序区域 (pLDDT>70) 占比 | 85.2% |
| 可用 PDB 条目 | 6B3X, 6URO, 7ZY4 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构 + AlphaFold高质量（pLDDT=86.0），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003107, IPR045243, IPR008847, IPR011990; Pfam: PF05843 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CSTF1 | 0.999 | 0.971 | — |
| CPSF1 | 0.999 | 0.975 | — |
| FIP1L1 | 0.999 | 0.997 | — |
| SYMPK | 0.999 | 0.985 | — |
| CSTF2 | 0.999 | 0.964 | — |
| CSTF2T | 0.998 | 0.972 | — |
| PCF11 | 0.998 | 0.966 | — |
| WDR33 | 0.998 | 0.955 | — |
| CPSF4 | 0.995 | 0.908 | — |
| CPSF3 | 0.993 | 0.717 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.0 + PDB: 6B3X, 6URO, 7ZY4 | pLDDT=86.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (>=3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. CSTF3 -- Cleavage stimulation factor subunit 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小717 aa，大小适中（200-800 aa），适合常规生化实验。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q12996
- Protein Atlas: https://www.proteinatlas.org/ENSG00000176102-CSTF3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CSTF3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q12996
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CSTF3/IF_images/A-431_2.jpg]]
![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CSTF3/IF_images/A-431_1.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000176102-CSTF3/subcellular

![](https://images.proteinatlas.org/39743/534_H9_1_red_green.jpg)
![](https://images.proteinatlas.org/39743/534_H9_2_red_green.jpg)
![](https://images.proteinatlas.org/39743/539_H9_1_red_green.jpg)
![](https://images.proteinatlas.org/39743/539_H9_3_red_green.jpg)
![](https://images.proteinatlas.org/39743/552_H9_2_red_green.jpg)
![](https://images.proteinatlas.org/39743/552_H9_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q12996-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
