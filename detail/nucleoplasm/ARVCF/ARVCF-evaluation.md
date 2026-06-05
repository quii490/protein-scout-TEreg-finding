---
type: protein-evaluation
gene: "ARVCF"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ARVCF 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ARVCF |
| 蛋白名称 | Splicing regulator ARVCF |
| 蛋白大小 | 962 aa / 104.6 kDa |
| UniProt ID | O00192 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane, Cell Junctions; UniProt: Cell junction, adherens junction; Nucleus; Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 962 aa / 104.6 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=78 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011989, IPR016024, IPR000225, IPR028435; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **98.0/180** | |
| **归一化总分** | | | **54.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cell Junctions | Enhanced |
| UniProt | Cell junction, adherens junction; Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- adherens junction (GO:0005912)
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 78 |
| PubMed broad count | 113 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Integrating RNA-seq and scRNA-seq to explore the prognostic features and immune landscape of exosome-related genes in breast cancer metastasis.. *Annals of medicine*. PMID: 39847423
2. Differential expression pattern of protein ARVCF in nephron segments of human and mouse kidney.. *Histochemistry and cell biology*. PMID: 18600340
3. p53-induced ARVCF modulates the splicing landscape and supports the tumor suppressive function of p53.. *Oncogene*. PMID: 31827232
4. Vertebrate development requires ARVCF and p120 catenins and their interplay with RhoA and Rac.. *The Journal of cell biology*. PMID: 15067024
5. Identification and validation of a novel gene ARVCF associated with alcohol dependence among Chinese population.. *iScience*. PMID: 39429782

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.9 |
| 高置信度残基 (pLDDT>90) 占比 | 40.3% |
| 置信残基 (pLDDT 70-90) 占比 | 8.0% |
| 中等置信 (pLDDT 50-70) 占比 | 5.3% |
| 低置信 (pLDDT<50) 占比 | 46.4% |
| 有序区域 (pLDDT>70) 占比 | 48.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=64.9），有序残基占 48.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011989, IPR016024, IPR000225, IPR028435; Pfam: PF00514 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| COMT | 0.897 | 0.000 | — |
| TXNRD2 | 0.860 | 0.000 | — |
| ERBIN | 0.831 | 0.396 | — |
| CTNNB1 | 0.804 | 0.657 | — |
| FMR1 | 0.797 | 0.050 | — |
| PKP1 | 0.795 | 0.000 | — |
| PKP3 | 0.759 | 0.000 | — |
| FRMPD2 | 0.755 | 0.000 | — |
| CPEB2 | 0.720 | 0.000 | — |
| CDH17 | 0.714 | 0.134 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TACR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| S1PR2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GJB7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| P4HA2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PROZ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CDH8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CPA5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CTNNA3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CDH5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CYP2S1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.9 + PDB: 无 | pLDDT=64.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell junction, adherens junction; Nucleus; Cytopla / Plasma membrane, Cell Junctions | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. ARVCF — Splicing regulator ARVCF，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小962 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 78 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=64.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O00192
- Protein Atlas: https://www.proteinatlas.org/ENSG00000099889-ARVCF/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ARVCF
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O00192
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (enhanced)。来源: https://www.proteinatlas.org/ENSG00000099889-ARVCF/subcellular

![](https://images.proteinatlas.org/55264/1036_F2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/55264/1036_F2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/55264/893_G7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/55264/893_G7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/55264/895_G7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/55264/895_G7_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O00192-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
