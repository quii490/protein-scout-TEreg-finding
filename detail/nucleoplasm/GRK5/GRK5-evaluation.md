---
type: protein-evaluation
gene: "GRK5"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GRK5 — REJECTED (研究热度过高 (PubMed strict=491，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GRK5 / GPRK5 |
| 蛋白名称 | G protein-coupled receptor kinase 5 |
| 蛋白大小 | 590 aa / 67.8 kDa |
| UniProt ID | P34947 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear membrane, Nuclear speckles; 额外: Plasma membrane; UniProt: Cytoplasm; Nucleus; Cell membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 590 aa / 67.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=491 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=90.4; PDB: 4TNB, 4TND, 6PJX, 8UAP, 8UAQ, 9BRE, 9BRF |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000961, IPR000239, IPR011009, IPR000719, IPR017 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear membrane, Nuclear speckles; 额外: Plasma membrane | Supported |
| UniProt | Cytoplasm; Nucleus; Cell membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nuclear membrane (GO:0031965)
- nuclear speck (GO:0016607)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 491 |
| PubMed broad count | 573 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GPRK5 |

**关键文献**:
1. Effect of phosphorylation barcodes on arrestin binding to a chemokine receptor.. *Nature*. PMID: 40399676
2. GRK5 Controls SAP97-Dependent Cardiotoxic β(1) Adrenergic Receptor-CaMKII Signaling in Heart Failure.. *Circulation research*. PMID: 32507058
3. Targeting GRK2 and GRK5 for treating chronic degenerative diseases: Advances and future perspectives.. *European journal of medicinal chemistry*. PMID: 36055000
4. GRK2 and GRK5 as therapeutic targets and their role in maladaptive and pathological cardiac hypertrophy.. *Expert opinion on therapeutic targets*. PMID: 30701991
5. GRK specificity and Gβγ dependency determines the potential of a GPCR for arrestin-biased agonism.. *Communications biology*. PMID: 38956302

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.4 |
| 高置信度残基 (pLDDT>90) 占比 | 79.2% |
| 置信残基 (pLDDT 70-90) 占比 | 11.9% |
| 中等置信 (pLDDT 50-70) 占比 | 3.6% |
| 低置信 (pLDDT<50) 占比 | 5.4% |
| 有序区域 (pLDDT>70) 占比 | 91.1% |
| 可用 PDB 条目 | 4TNB, 4TND, 6PJX, 8UAP, 8UAQ, 9BRE, 9BRF, 9BRG, 9BRH, 9BRI |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（4TNB, 4TND, 6PJX, 8UAP, 8UAQ, 9BRE, 9BRF, 9BRG, 9BRH, 9BRI）+ AlphaFold极高置信度预测（pLDDT=90.4），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000961, IPR000239, IPR011009, IPR000719, IPR017441; Pfam: PF00069, PF00615 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GIT1 | 0.997 | 0.000 | — |
| ARRB1 | 0.976 | 0.294 | — |
| ARRB2 | 0.972 | 0.045 | — |
| CALM3 | 0.952 | 0.905 | — |
| OPRM1 | 0.948 | 0.097 | — |
| GIT2 | 0.934 | 0.000 | — |
| CALM1 | 0.933 | 0.930 | — |
| ADRB2 | 0.910 | 0.333 | — |
| CALM2 | 0.908 | 0.905 | — |
| RHO | 0.869 | 0.567 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GRK6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ENST00000392870 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 2
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.4 + PDB: 4TNB, 4TND, 6PJX, 8UAP, 8UAQ,  | pLDDT=90.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Cell membrane / Nuclear membrane, Nuclear speckles; 额外: Plasma mem | 一致 |
| PPI | STRING + IntAct | 15 + 2 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GRK5 — G protein-coupled receptor kinase 5，研究基础较多，新颖性有限。
2. 蛋白大小590 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 491 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 491 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P34947
- Protein Atlas: https://www.proteinatlas.org/ENSG00000198873-GRK5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GRK5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P34947
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear membrane (supported)。来源: https://www.proteinatlas.org/ENSG00000198873-GRK5/subcellular

![](https://images.proteinatlas.org/46838/1752_G8_18_cr5804e4de4d29f_red_green.jpg)
![](https://images.proteinatlas.org/46838/1752_G8_8_cr5804e4d4a9726_red_green.jpg)
![](https://images.proteinatlas.org/46838/692_D8_1_red_green.jpg)
![](https://images.proteinatlas.org/46838/692_D8_2_red_green.jpg)
![](https://images.proteinatlas.org/46838/763_H3_1_red_green.jpg)
![](https://images.proteinatlas.org/46838/763_H3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P34947-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
