---
type: protein-evaluation
gene: "CD72"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CD72 — REJECTED (研究热度过高 (PubMed strict=144，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CD72 |
| 蛋白名称 | B-cell differentiation antigen CD72 |
| 蛋白大小 | 359 aa / 40.2 kDa |
| UniProt ID | P21854 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Mitochondria; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 359 aa / 40.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=144 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=76.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001304, IPR016186, IPR039689, IPR016187; Pfam:  |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **68.0/180** | |
| **归一化总分** | | | **37.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Mitochondria | Uncertain |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 144 |
| PubMed broad count | 354 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Phosphorylation stabilized TET1 acts as an oncoprotein and therapeutic target in B cell acute lymphoblastic leukemia.. *Science translational medicine*. PMID: 36989375
2. Receptor Functions of Semaphorin 4D.. *Biochemistry. Biokhimiia*. PMID: 31693461
3. Soluble CD72 concurrently impairs T cell functions while enhances inflammatory response in sepsis.. *International immunopharmacology*. PMID: 39793226
4. Differential Gene Expression Involved in Bone Turnover of Mice Expressing Constitutively Active TGFβ Receptor Type I.. *International journal of molecular sciences*. PMID: 38892016
5. CD72, a negative regulator of B-cell responsiveness.. *Immunological reviews*. PMID: 11043769

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.1 |
| 高置信度残基 (pLDDT>90) 占比 | 47.4% |
| 置信残基 (pLDDT 70-90) 占比 | 17.0% |
| 中等置信 (pLDDT 50-70) 占比 | 13.9% |
| 低置信 (pLDDT<50) 占比 | 21.7% |
| 有序区域 (pLDDT>70) 占比 | 64.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=76.1，有序区 64.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001304, IPR016186, IPR039689, IPR016187; Pfam: PF00059 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CD5 | psi-mi:"MI:0054"(fluorescence-activated cell sorti | pubmed:1711157 |
| HMGA1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| GRAMD1C | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SPACA1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| LHFPL5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| NRG1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MS4A3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CGRRF1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| BIK | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CLDN7 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.1 + PDB: 无 | pLDDT=76.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoplasm, Mitochondria | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CD72 — B-cell differentiation antigen CD72，研究基础较多，新颖性有限。
2. 蛋白大小359 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 144 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 144 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P21854
- Protein Atlas: https://www.proteinatlas.org/ENSG00000137101-CD72/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CD72
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P21854
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000137101-CD72/subcellular

![](https://images.proteinatlas.org/44658/1377_H2_1_red_green.jpg)
![](https://images.proteinatlas.org/44658/1377_H2_3_red_green.jpg)
![](https://images.proteinatlas.org/44658/1475_F4_4_red_green.jpg)
![](https://images.proteinatlas.org/44658/1475_F4_5_red_green.jpg)
![](https://images.proteinatlas.org/44658/2144_C3_1_red_green.jpg)
![](https://images.proteinatlas.org/44658/2144_C3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P21854-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P21854 |
| SMART | SM00034; |
| UniProt Domain [FT] | DOMAIN 232..352; /note="C-type lectin"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00040" |
| InterPro | IPR001304;IPR016186;IPR039689;IPR016187; |
| Pfam | PF00059; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000137101-CD72/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ATP6AP2 | Intact | false |
| BIK | Intact | false |
| CGRRF1 | Intact | false |
| CLDN7 | Intact | false |
| CREB3L1 | Intact | false |
| GPR152 | Intact | false |
| GRAMD1C | Intact | false |
| LHFPL5 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
