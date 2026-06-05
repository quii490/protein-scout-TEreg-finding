---
type: protein-evaluation
gene: "JMY"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## JMY 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | JMY |
| 蛋白名称 | Junction-mediating and -regulatory protein |
| 蛋白大小 | 988 aa / 111.4 kDa |
| UniProt ID | Q8N9B5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Cytoplasmic vesicle; Cytoplasm, cytoskeleton; Endom |
| 蛋白大小 | 8/10 | ×1 | 8 | 988 aa / 111.4 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=58 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR031738, IPR031808, IPR003124; Pfam: PF15871, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **108.0/180** | |
| **归一化总分** | | | **60.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Uncertain |
| UniProt | Nucleus; Cytoplasmic vesicle; Cytoplasm, cytoskeleton; Endomembrane system; Cytoplasmic vesicle, aut... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- autophagosome membrane (GO:0000421)
- cell leading edge (GO:0031252)
- cytoplasm (GO:0005737)
- cytoplasmic vesicle (GO:0031410)
- cytoskeleton (GO:0005856)
- endomembrane system (GO:0012505)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 58 |
| PubMed broad count | 226 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Regulation of JMY's actin nucleation activity by TTC5/STRAP and LC3 during autophagy.. *Autophagy*. PMID: 30593260
2. WASH, WHAMM and JMY: regulation of Arp2/3 complex and beyond.. *Trends in cell biology*. PMID: 20888769
3. WAVE regulatory complex.. *Current biology : CB*. PMID: 34033782
4. The Role of JMY in p53 Regulation.. *Cancers*. PMID: 29857553
5. Junction-mediating and regulatory protein (JMY) is essential for early porcine embryonic development.. *The Journal of reproduction and development*. PMID: 26052154

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.6 |
| 高置信度残基 (pLDDT>90) 占比 | 30.9% |
| 置信残基 (pLDDT 70-90) 占比 | 19.0% |
| 中等置信 (pLDDT 50-70) 占比 | 10.8% |
| 低置信 (pLDDT<50) 占比 | 39.3% |
| 有序区域 (pLDDT>70) 占比 | 49.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=65.6），有序残基占 49.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR031738, IPR031808, IPR003124; Pfam: PF15871, PF15920 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EP300 | 0.995 | 0.522 | — |
| TP53 | 0.940 | 0.294 | — |
| TTC5 | 0.929 | 0.292 | — |
| WAS | 0.836 | 0.113 | — |
| WASF1 | 0.802 | 0.058 | — |
| MDM2 | 0.693 | 0.302 | — |
| PRMT5 | 0.640 | 0.052 | — |
| COBL | 0.620 | 0.107 | — |
| GOLGA2 | 0.614 | 0.052 | — |
| SPIRE2 | 0.599 | 0.098 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EP300 | psi-mi:"MI:0018"(two hybrid) | pubmed:10518217|imex:IM-19160 |
| TP53 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:10518217|imex:IM-19160 |
| HSPE1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| SERPINH1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| CDC5L | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| CEP63 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| MAB21L2 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| RINT1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MTUS2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CCDC136 | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-23318|pubmed:25416956 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.6 + PDB: 无 | pLDDT=65.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasmic vesicle; Cytoplasm, cytoskele / Nucleoplasm | 一致 |
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
1. JMY — Junction-mediating and -regulatory protein，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小988 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 58 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=65.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N9B5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000152409-JMY/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=JMY
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N9B5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000152409-JMY/subcellular

![](https://images.proteinatlas.org/37508/1162_G12_1_red_green.jpg)
![](https://images.proteinatlas.org/37508/1162_G12_2_red_green.jpg)
![](https://images.proteinatlas.org/37508/1281_D7_2_red_green.jpg)
![](https://images.proteinatlas.org/37508/1281_D7_3_red_green.jpg)
![](https://images.proteinatlas.org/37508/1313_D7_1_red_green.jpg)
![](https://images.proteinatlas.org/37508/1313_D7_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8N9B5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
