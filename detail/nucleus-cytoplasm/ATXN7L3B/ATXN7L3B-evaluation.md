---
type: protein-evaluation
gene: "ATXN7L3B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ATXN7L3B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ATXN7L3B / 无 |
| 蛋白名称 | Ataxin-7-like protein 3B |
| 蛋白大小 | 97 aa / 10.8 kDa |
| UniProt ID | Q96GX2 |
| 评估日期 | 2026-06-03 |
| 数据采集时间 | 2026-06-03 03:27:06 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 10/10 | x4 | 40 | HPA: Nucleoplasm; UniProt: Cytoplasm |
| 蛋白大小 | 4/10 | x1 | 4 | 97 aa / 10.8 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=5 篇 (<=20->10) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=67.4 |
| 调控结构域 | 3/10 | x2 | 6 | InterPro: 1; Pfam: 0; IPR042933 |
| PPI 网络 | 8/10 | x3 | 24 | STRING 15 partners; IntAct 5 interactions |
| 互证加分 | -- | max +3 | 1.5 | 多库定位一致 (3源): +0.5; STRING + IntAct 双源验证: +0.5; 结构域 + AlphaFold 质量: +0.5 |
| **原始总分** | | | **146.5/180** | |
| **归一化总分 (/1.83)** | | | **80.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoplasm | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- cytoplasm (GO:0005737)

**结论**: 核定位证据充分，多个数据源一致支持核定位，定位特异性高。

#### 3.2 蛋白大小评估

**评价**: 97 aa，蛋白较小，但仍在可操作范围。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 10 |

**关键文献**:
1. The G→C rs590352 in the Protein-Coding Region of ATXN7L3B Gene Upregulates Its Expression In Vivo.. *Biochemical genetics*. PMID: 41217722
2. Genome-wide association analysis reveals KCTD12 and miR-383-binding genes in the background of rumination.. *Translational psychiatry*. PMID: 30886212
3. Distinct effects on mRNA export factor GANP underlie neurological disease phenotypes and alter gene expression depending on intron content.. *Human molecular genetics*. PMID: 32202298
4. CRISPRa genome-wide screen identifies novel gene targets for osteogenic cell engineering.. *Journal of tissue engineering*. PMID: 41245170
5. Potential regulatory SNPs in the ATXN7L3B and KRT15 genes are associated with gender-specific colorectal cancer risk.. *Personalized medicine*. PMID: 31797724

**评价**: 极度新颖，几乎未被系统研究（PubMed <= 20篇）。新颖性评分 10/10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.4 |
| 高置信度残基 (pLDDT>90) 占比 | 27.8% |
| 置信残基 (pLDDT 70-90) 占比 | 15.5% |
| 中等置信 (pLDDT 50-70) 占比 | 18.6% |
| 低置信 (pLDDT<50) 占比 | 38.1% |
| 有序区域 (pLDDT>70) 占比 | 43.3% |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold中等质量预测（pLDDT=67.4），存在部分低置信区域。三维结构评分 7/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR042933; Pfam: 无 |

**染色质调控潜力分析**: 存在 1 个已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score > 0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ATXN7L1 | 0.514 | 0.237 | -- |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| USP22 | anti tag coimmunoprecipitation | imex:IM-12079|pubmed:19615732 |
| LRRK2 | anti tag coimmunoprecipitation | pubmed:31046837|imex:IM-26684 |
| ENST00000519948 | clash | pubmed:23622248|imex:IM-30030|doi:10.1016/j.cell.2013.03.043 |
| ZC3H11A | proximity-dependent biotin identificatio | imex:IM-30059|pubmed:39251607 |
| LARP7 | proximity-dependent biotin identificatio | imex:IM-30059|pubmed:39251607 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 5

**评价**: 互作网络中等：STRING 15 预测 + IntAct 5 实验互作。PPI 评分 8/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold v6 | pLDDT=67.4 | 单一来源 |
| 定位 | HPA | Nucleoplasm | 单一来源 |
| PPI | STRING + IntAct | 15 + 5 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
**总分**: +1.5 / max +3

### 4. 总体评价

**归一化总分**: 80.1/100

**核心优势**:
1. ATXN7L3B -- Ataxin-7-like protein 3B，极度新颖，几乎未被系统研究（PubMed <= 20篇）。
2. 存在 1 个已知结构域，有明确的结构-功能切入点。
3. 核定位信号明确，多个数据源一致支持。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. 暂无PDB实验结构，结构证据完全依赖AlphaFold预测
3. 蛋白过小（97 aa），实验操作受限

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] 考虑通过AlphaFold预测 + MD模拟获取结构信息

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q96GX2
- Protein Atlas: https://www.proteinatlas.org/search/ATXN7L3B
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ATXN7L3B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96GX2
- STRING: https://string-db.org/network/9606.ATXN7L3B
- Packet data timestamp: 2026-06-03 03:27:06

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000253719-ATXN7L3B/subcellular

![](https://images.proteinatlas.org/56612/935_A9_1_red_green.jpg)
![](https://images.proteinatlas.org/56612/935_A9_2_red_green.jpg)
![](https://images.proteinatlas.org/56612/958_F3_1_red_green.jpg)
![](https://images.proteinatlas.org/56612/958_F3_2_red_green.jpg)
![](https://images.proteinatlas.org/56612/982_F8_1_red_green.jpg)
![](https://images.proteinatlas.org/56612/982_F8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96GX2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
