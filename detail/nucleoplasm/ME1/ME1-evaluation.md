---
type: protein-evaluation
gene: "ME1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ME1 — REJECTED (研究热度过高 (PubMed strict=378，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ME1 |
| 蛋白名称 | NADP-dependent malic enzyme |
| 蛋白大小 | 572 aa / 64.2 kDa |
| UniProt ID | P48163 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Plasma membrane; 额外: Cytosol; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 572 aa / 64.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=378 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=95.4; PDB: 2AW5, 3WJA, 7X11, 7X12 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR046346, IPR015884, IPR012301, IPR037062, IPR012 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.0/180** | |
| **归一化总分** | | | **45.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Plasma membrane; 额外: Cytosol | Uncertain |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- mitochondrion (GO:0005739)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 378 |
| PubMed broad count | 795 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Inactivation of Malic Enzyme 1 in Endothelial Cells Alleviates Pulmonary Hypertension.. *Circulation*. PMID: 38314588
2. Dynamic Regulation of ME1 Phosphorylation and Acetylation Affects Lipid Metabolism and Colorectal Tumorigenesis.. *Molecular cell*. PMID: 31735643
3. JMJD6 Rewires ATF4-Dependent Glutathione Metabolism to Confer Ferroptosis Resistance in SPOP-Mutated Prostate Cancer.. *Cancer research*. PMID: 39903850
4. G6PD and ACSL3 are synthetic lethal partners of NF2 in Schwann cells.. *Nature communications*. PMID: 38879607
5. Metal coordination in kinases and pseudokinases.. *Biochemical Society transactions*. PMID: 28620027

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 95.4 |
| 高置信度残基 (pLDDT>90) 占比 | 90.9% |
| 置信残基 (pLDDT 70-90) 占比 | 7.7% |
| 中等置信 (pLDDT 50-70) 占比 | 0.9% |
| 低置信 (pLDDT<50) 占比 | 0.5% |
| 有序区域 (pLDDT>70) 占比 | 98.6% |
| 可用 PDB 条目 | 2AW5, 3WJA, 7X11, 7X12 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2AW5, 3WJA, 7X11, 7X12）+ AlphaFold高质量预测（pLDDT=95.4），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR046346, IPR015884, IPR012301, IPR037062, IPR012302; Pfam: PF00390, PF03949 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PC | 0.997 | 0.447 | — |
| FH | 0.989 | 0.000 | — |
| MDH2 | 0.980 | 0.071 | — |
| PKM | 0.974 | 0.262 | — |
| CS | 0.972 | 0.000 | — |
| PKLR | 0.969 | 0.097 | — |
| LDHA | 0.958 | 0.065 | — |
| LDHAL6A | 0.954 | 0.065 | — |
| LDHAL6B | 0.954 | 0.065 | — |
| PDHB | 0.951 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000358719.3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ci | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| Ir60a | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG15177 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| dl | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Men | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| ARPC1B | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| HTRA3 | psi-mi:"MI:0435"(protease assay) | imex:IM-27346|pubmed:26110759 |
| CDK15 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZSCAN12 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=95.4 + PDB: 2AW5, 3WJA, 7X11, 7X12 | pLDDT=95.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoplasm, Plasma membrane; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. ME1 — NADP-dependent malic enzyme，研究基础较多，新颖性有限。
2. 蛋白大小572 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 378 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 378 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P48163
- Protein Atlas: https://www.proteinatlas.org/ENSG00000065833-ME1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ME1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P48163
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000065833-ME1/subcellular

![](https://images.proteinatlas.org/6493/1253_A2_1_red_green.jpg)
![](https://images.proteinatlas.org/6493/1253_A2_2_red_green.jpg)
![](https://images.proteinatlas.org/6493/41_H3_1_red_green.jpg)
![](https://images.proteinatlas.org/6493/41_H3_2_red_green.jpg)
![](https://images.proteinatlas.org/6493/42_H3_1_red_green.jpg)
![](https://images.proteinatlas.org/6493/42_H3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P48163-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
