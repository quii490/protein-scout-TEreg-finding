---
type: protein-evaluation
gene: "STAT5B"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## STAT5B — REJECTED (研究热度过高 (PubMed strict=949，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | STAT5B |
| 蛋白名称 | Signal transducer and activator of transcription 5B |
| 蛋白大小 | 787 aa / 89.9 kDa |
| UniProt ID | P51692 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 787 aa / 89.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=949 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=85.2; PDB: 6MBW, 6MBZ |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR008967, IPR000980, IPR036860, IPR001217, IPR046 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **92.0/180** | |
| **归一化总分** | | | **51.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- RNA polymerase II transcription regulator complex (GO:0090575)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 949 |
| PubMed broad count | 1554 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Dual STAT3/STAT5 inhibition as a novel treatment strategy in T-prolymphocytic leukemia.. *Leukemia*. PMID: 40234614
2. QSOX2 Deficiency-induced short stature, gastrointestinal dysmotility and immune dysfunction.. *Nature communications*. PMID: 39341815
3. Stafiba: A STAT5-Selective Small-Molecule Inhibitor.. *Chembiochem : a European journal of chemical biology*. PMID: 36300584
4. STAT5b deficiency: lessons from STAT5b gene mutations.. *Best practice & research. Clinical endocrinology & metabolism*. PMID: 21396575
5. The theory of APL.. *Oncogene*. PMID: 11704849

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.2 |
| 高置信度残基 (pLDDT>90) 占比 | 65.4% |
| 置信残基 (pLDDT 70-90) 占比 | 19.2% |
| 中等置信 (pLDDT 50-70) 占比 | 5.0% |
| 低置信 (pLDDT<50) 占比 | 10.4% |
| 有序区域 (pLDDT>70) 占比 | 84.6% |
| 可用 PDB 条目 | 6MBW, 6MBZ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（6MBW, 6MBZ）+ AlphaFold高质量预测（pLDDT=85.2），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008967, IPR000980, IPR036860, IPR001217, IPR046994; Pfam: PF00017, PF01017, PF02864 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| JAK2 | 0.999 | 0.718 | — |
| JAK1 | 0.999 | 0.472 | — |
| STAT3 | 0.998 | 0.387 | — |
| EGFR | 0.997 | 0.787 | — |
| JAK3 | 0.997 | 0.425 | — |
| ERBB4 | 0.993 | 0.628 | — |
| IL2RA | 0.989 | 0.292 | — |
| TYK2 | 0.984 | 0.285 | — |
| CRKL | 0.983 | 0.000 | — |
| ABL1 | 0.983 | 0.439 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000513924.1 | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:31175292|imex:IM-27733 |
| EPOR | psi-mi:"MI:0231"(mammalian protein protein interac | pubmed:15644415 |
| AFTPH | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| DMRTA1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| TFG | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| HAX1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| IL15 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| VCAM1 | psi-mi:"MI:0030"(cross-linking study) | imex:IM-17358|pubmed:22623428 |
| NMI | psi-mi:"MI:0018"(two hybrid) | pubmed:9989503 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.2 + PDB: 6MBW, 6MBZ | pLDDT=85.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. STAT5B — Signal transducer and activator of transcription 5B，研究基础较多，新颖性有限。
2. 蛋白大小787 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 949 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 949 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P51692
- Protein Atlas: https://www.proteinatlas.org/search/STAT5B
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=STAT5B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P51692
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000173757-STAT5B/subcellular

![](https://images.proteinatlas.org/5418/1972_G8_22_cr5e16e0102e57e_blue_red_green.jpg)
![](https://images.proteinatlas.org/5418/1972_G8_29_cr5e16e010302bf_blue_red_green.jpg)
![](https://images.proteinatlas.org/5418/1993_C7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/5418/1993_C7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/5418/2009_C3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/5418/2009_C3_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P51692-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
