---
type: protein-evaluation
gene: "TET3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TET3 — REJECTED (研究热度过高 (PubMed strict=435，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TET3 / CXXC10, KIAA0401 |
| 蛋白名称 | Methylcytosine dioxygenase TET3 |
| 蛋白大小 | 1795 aa / 193.7 kDa |
| UniProt ID | O43151 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Vesicles, Cytosol; UniProt: Nucleus; Cytoplasm; Chromosome |
| 蛋白大小 | 5/10 | ×1 | 5 | 1795 aa / 193.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=435 篇 (>100→REJECTED) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v6 pLDDT=0; PDB: 4Z3C, 8U2Y |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR024779, IPR040175, IPR046942, IPR002857; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **69.0/180** | |
| **归一化总分** | | | **38.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles, Cytosol | Approved |
| UniProt | Nucleus; Cytoplasm; Chromosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromosome (GO:0005694)
- cytoplasm (GO:0005737)
- female pronucleus (GO:0001939)
- male pronucleus (GO:0001940)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 435 |
| PubMed broad count | 794 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CXXC10, KIAA0401 |

**关键文献**:
1. Mechanisms that regulate the activities of TET proteins.. *Cellular and molecular life sciences : CMLS*. PMID: 35705880
2. Maternal inheritance of glucose intolerance via oocyte TET3 insufficiency.. *Nature*. PMID: 35585240
3. Integrative Genomic and Transcriptomic Analysis Reveals Targetable Vulnerabilities in Angioimmunoblastic T-Cell Lymphoma.. *American journal of hematology*. PMID: 40510016
4. The evolving epigenome.. *Human molecular genetics*. PMID: 23900077
5. MYC/TET3-Regulated TMEM65 Activates OXPHOS-SERPINB3 Pathway to Promote Progression and Cisplatin Resistance in Triple-Negative Breast Cancer.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 40546127

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 4Z3C, 8U2Y |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR024779, IPR040175, IPR046942, IPR002857; Pfam: PF12851, PF02008 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| OGT | 0.975 | 0.513 | — |
| TET2 | 0.964 | 0.130 | — |
| NANOG | 0.886 | 0.125 | — |
| PRMT5 | 0.882 | 0.000 | — |
| DNMT1 | 0.881 | 0.000 | — |
| SIN3A | 0.860 | 0.295 | — |
| TDG | 0.809 | 0.000 | — |
| DNMT3A | 0.802 | 0.000 | — |
| DNMT3B | 0.783 | 0.000 | — |
| TET1 | 0.779 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| A0A0F7RCF4 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| RPL13A | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| EXOSC4 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| RPL14 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| Kctd5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| BAG3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| LTN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| MLF1 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |
| MLF2 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 4Z3C, 8U2Y | pLDDT=0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Chromosome / Nucleoplasm; 额外: Vesicles, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. TET3 — Methylcytosine dioxygenase TET3，研究基础较多，新颖性有限。
2. 蛋白大小1795 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 435 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 435 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O43151
- Protein Atlas: https://www.proteinatlas.org/ENSG00000187605-TET3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TET3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O43151
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000187605-TET3/subcellular

![](https://images.proteinatlas.org/50845/1055_A1_2_red_green.jpg)
![](https://images.proteinatlas.org/50845/1055_A1_4_red_green.jpg)
![](https://images.proteinatlas.org/50845/1462_E2_4_red_green.jpg)
![](https://images.proteinatlas.org/50845/1462_E2_7_red_green.jpg)
![](https://images.proteinatlas.org/50845/2253_D8_150_red_green.jpg)
![](https://images.proteinatlas.org/50845/2253_D8_68_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O43151-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O43151 |
| SMART | SM01333; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR024779;IPR040175;IPR046942;IPR002857; |
| Pfam | PF12851;PF02008; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000187605-TET3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| NONO | Opencell | false |
| OGT | Intact | false |
| PSPC1 | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
