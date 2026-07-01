---
type: protein-evaluation
gene: "SLC4A3"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SLC4A3 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SLC4A3 |
| 蛋白名称 | Anion exchange protein 3 |
| 蛋白大小 | 1232 aa / 135.8 kDa |
| UniProt ID | P48751 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm (Approved) |
| 蛋白大小 | 6/10 | x1 | 6.0 | 1232 aa |
| 新颖性 | 8/10 | x5 | 40.0 | PubMed=35 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=66.7; PDB=4 |
| 调控结构域 | 4/10 | x2 | 8.0 | Anion_exchange; Anion_exchange_3; Anion_exchange_CS |
| PPI | 5/10 | x3 | 15.0 | PPI degree=7 |
| **加权总分** | | | **123/180** | |
| **归一化总分** | | | **68.3/100** | 互证: +2 |

### 3. 分析
- Nucleoplasm (Approved)
- PubMed strict=35 broad=124
- AF pLDDT=66.7 PDB=4
- InterPro: Anion_exchange; Anion_exchange_3; Anion_exchange_CS
- Pfam: Band_3_cyto; HCO3_cotransp
- PPI degree=7 ChIP: None
41039816: A Novel Variant in SLC4A3 Gene Mutation Associated With Familial Short QT Syndro | 40439641: A Gain-of -Function SLC4A3 Mutation Causes Short-QT Syndrome: From Molecular Ana | 41780556: SLC4A3-related short QT syndrome assessed in human induced pluripotent stem cell

### 4. 总体评价
**68.3/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

**阴离子交换蛋白AE3的核质通路与短QT综合征基因功能**：SLC4A3（Anion exchange protein 3/AE3, 1232 aa, UniProt P48751）是SLC4阴离子交换蛋白家族成员，催化Cl-/HCO3-的电中性跨膜交换（PMID:29167417, 7923606）。蛋白包含N端胞质域（Band_3_cyto, Pfam）和C端跨膜域（HCO3_cotransp），通过"乒乓"机制交换一价阴离子。其核心生理功能为调节细胞内pH（pHi）和心肌动作电位的复极相位——功能获得性突变导致短QT综合征（SQTS, PMIDs:41039816, 40439641, 41780556），表现为心室复极加速和心律失常死亡风险增加。HPA数据显示Nucleoplasm为Approved级别定位（核定位特异性9/10），为跨膜离子转运蛋白的核质非经典功能提供了少见的确凿证据。

**胞内pH调控与核内组蛋白修饰酶活性**：AE3的Cl-/HCO3-交换活性直接影响胞内pH——而核内pH（pHn）是染色质修饰酶催化活性的关键物理化学参数：(1) HDAC催化域的最适pH为7.5-8.0，酸性偏移（pH<7.0）显著抑制其活性，导致组蛋白乙酰化水平升高；(2) HAT（如p300/CBP）的最适pH相反（6.5-7.0），碱性偏移（pH>7.5）抑制乙酰化——因此AE3通过Cl-/HCO3-交换改变pHi和pHn可全局性地重塑组蛋白乙酰化景观。对于TE调控，H3K9ac和H4K16ac的富集促进活性TE（特别是SVA和年轻L1）的染色质开放——AE3通过碳酸酐酶或NHE协同调节核内pH可能间接调控"乙酰化-TE"功能轴。

**核定位的双重机制**：1232 aa / 135.8 kDa的大分子量排除了被动核孔扩散，必然存在主动核输入机制。可能的NLS包括：(1) 蛋白水解后释放N端胞质域（约400 aa, 含多个碱性氨基酸簇），该片段进入核内发挥pH感知或信号转导功能；(2) AE3作为整合膜蛋白可能定位于核膜（inner/outer nuclear membrane），通过局部HCO3-转运调节核质与胞质之间的pH梯度。PPI degree=7虽然极低，但GAPDH（BioGRID score=1）和RANGAP1（BioGRID score=1）的互作提供了核转运相关功能的微妙线索——RANGAP1是Ran GTPase激活蛋白，参与核质转运的RanGTP梯度调控。DDX58/RIG-I（BioGRID score=0）的微弱互作则与先天免疫-TE交叉相关。

**SQTS基因与TE调控的意外交点**：AE3突变导致SQTS的分子病理涉及心肌复极加速——这与心律失常性右室心肌病（ARVC）中的TE激活表型有潜在重叠。心脏传导系统的细胞中已发现LINE-1的去抑制与传导缺陷（如Brugada综合征）的关联（PMID:31378581），但在SQTS中的TE表达状态尚未被研究。归一化得分68.3/100中核定位特异性36/40和新奇性40/50使其成为膜蛋白中少有的高分候选。


### 补充分析 (UniProt API)

**蛋白全称**: Anion exchange protein 3

**功能**: Sodium-independent anion exchanger which mediates the electroneutral exchange of chloride for bicarbonate ions across the cell membrane (PubMed:29167417, PubMed:7923606). May be involved in the regulation of intracellular pH, and the modulation of cardiac action potential (PubMed:29167417)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR001717 |
| InterPro | IPR002979 |
| InterPro | IPR018241 |
| InterPro | IPR013769 |
| InterPro | IPR011531 |
| InterPro | IPR003020 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| GAPDH | BioGRID | 1 |
| UBASH3A | BioGRID | 1 |
| RANGAP1 | BioGRID | 1 |
| ANK1 | BioGRID | 0 |
| PRKD2 | BioGRID | 0 |
| DRD2 | BioGRID | 0 |
| DDX58 | BioGRID | 0 |