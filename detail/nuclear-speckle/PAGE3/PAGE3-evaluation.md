---
type: protein-evaluation
gene: "PAGE3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PAGE3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PAGE3 / GAGED1 |
| 蛋白名称 | P antigen family member 3 |
| 蛋白大小 | 113 aa / 12.5 kDa |
| UniProt ID | Q5JUK9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles; 额外: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 113 aa / 12.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR031320, IPR008625; Pfam: PF05831 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 3 partners; IntAct 5 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **127.5/180** | |
| **归一化总分** | | | **70.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles; 额外: Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 5 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GAGED1 |

**关键文献**:
1. Cancer-testis antigen expression in canine melanoma and healthy tissues.. *Veterinary immunology and immunopathology*. PMID: 40359694
2. Detection of autoantibodies against cancer-testis antigens in non-small cell lung cancer.. *Lung cancer (Amsterdam, Netherlands)*. PMID: 30429015
3. ProPred: prediction of HLA-DR binding sites.. *Bioinformatics (Oxford, England)*. PMID: 11751237
4. Spectrin oligomerization is cooperatively coupled to membrane assembly: a linkage targeted by many hereditary hemolytic anemias?. *Experimental and molecular pathology*. PMID: 11418000

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.9 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 22.1% |
| 中等置信 (pLDDT 50-70) 占比 | 77.9% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 22.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=63.9），有序残基占 22.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR031320, IPR008625; Pfam: PF05831 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| C12orf54 | 0.662 | 0.000 | — |
| VCX | 0.507 | 0.000 | — |
| MAGEB1 | 0.474 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SGTA | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SPHAR | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SGTB | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| MEOX1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| FAM9B | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 3，IntAct interactions: 5
- 调控相关比例: 0 / 3 = 0%

**评价**: STRING 3 个预测互作，IntAct 5 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.9 + PDB: 无 | pLDDT=63.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nuclear speckles; 额外: Nucleoplasm | 待确认 |
| PPI | STRING + IntAct | 3 + 5 interactions | 数据充分 |

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
1. PAGE3 — P antigen family member 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小113 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=63.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5JUK9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000204279-PAGE3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PAGE3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5JUK9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (approved)。来源: https://www.proteinatlas.org/ENSG00000204279-PAGE3/subcellular

![](https://images.proteinatlas.org/45032/1954_D5_45_cr5dfcaf99547b0_red_green.jpg)
![](https://images.proteinatlas.org/45032/1954_D5_56_cr5dfcaf9954fee_red_green.jpg)
![](https://images.proteinatlas.org/45032/1976_F10_1_red_green.jpg)
![](https://images.proteinatlas.org/45032/1976_F10_2_red_green.jpg)
![](https://images.proteinatlas.org/62248/1954_A4_51_cr5dfc9d98335ab_red_green.jpg)
![](https://images.proteinatlas.org/62248/1954_A4_58_cr5dfc9d9835621_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5JUK9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
