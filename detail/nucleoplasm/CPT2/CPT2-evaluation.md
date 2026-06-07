---
type: protein-evaluation
gene: "CPT2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CPT2 — REJECTED (研究热度过高 (PubMed strict=405，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CPT2 / CPT1 |
| 蛋白名称 | Carnitine O-palmitoyltransferase 2, mitochondrial |
| 蛋白大小 | 658 aa / 73.8 kDa |
| UniProt ID | P23786 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoplasm, Mitochondria; 额外: Nucleoli; UniProt: Mitochondrion inner membrane |
| 蛋白大小 | 10/10 | x1 | 10 | 658 aa / 73.8 kDa |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=405 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=94.1; PDB: 无 |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR000542, IPR042572, IPR023213, IPR039551, IPR042 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.0/180** | |
| **归一化总分** | | | **48.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Mitochondria; 额外: Nucleoli | Approved |
| UniProt | Mitochondrion inner membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- mitochondrial inner membrane (GO:0005743)
- mitochondrial matrix (GO:0005759)
- mitochondrion (GO:0005739)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 405 |
| PubMed broad count | 676 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CPT1 |

**关键文献**:
1. Hypoxia induces mitochondrial protein lactylation to limit oxidative phosphorylation.. *Cell research*. PMID: 38163844
2. NFIA regulates articular chondrocyte fatty acid metabolism and joint homeostasis.. *Science translational medicine*. PMID: 40737429
3. 18-[(18)F]Fluoro-4-thia-palmitate.. **. PMID: 21210569
4. AARS2-catalyzed lactylation induces follicle development and premature ovarian insufficiency.. *Cell death discovery*. PMID: 40301335
5. Muscle-generated BDNF (brain derived neurotrophic factor) maintains mitochondrial quality control in female mice.. *Autophagy*. PMID: 34689722

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.1 |
| 高置信度残基 (pLDDT>90) 占比 | 92.4% |
| 置信残基 (pLDDT 70-90) 占比 | 2.6% |
| 中等置信 (pLDDT 50-70) 占比 | 0.5% |
| 低置信 (pLDDT<50) 占比 | 4.6% |
| 有序区域 (pLDDT>70) 占比 | 95.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度（pLDDT=94.1，有序区 95.0%）。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000542, IPR042572, IPR023213, IPR039551, IPR042231; Pfam: PF00755 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SLC25A20 | 0.996 | 0.000 | — |
| ACADVL | 0.995 | 0.099 | — |
| ACADL | 0.982 | 0.098 | — |
| ACOX1 | 0.982 | 0.074 | — |
| CPT1A | 0.963 | 0.000 | — |
| ACOX3 | 0.961 | 0.074 | — |
| CPT1B | 0.942 | 0.000 | — |
| CPT1C | 0.942 | 0.000 | — |
| ACADS | 0.922 | 0.098 | — |
| AASDH | 0.921 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.1 + PDB: 无 | pLDDT=94.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Mitochondrion inner membrane / Nucleoplasm, Mitochondria; 额外: Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

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
1. CPT2 -- Carnitine O-palmitoyltransferase 2, mitochondrial，研究基础较多，新颖性有限。
2. 蛋白大小658 aa，大小适中（200-800 aa），适合常规生化实验。

**风险/不确定性**:
1. PubMed 405 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 405 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P23786
- Protein Atlas: https://www.proteinatlas.org/ENSG00000157184-CPT2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CPT2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P23786
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000157184-CPT2/subcellular

![](https://images.proteinatlas.org/28214/497_E8_1_red_green.jpg)
![](https://images.proteinatlas.org/28214/497_E8_2_red_green.jpg)
![](https://images.proteinatlas.org/28214/507_E8_2_red_green.jpg)
![](https://images.proteinatlas.org/28214/507_E8_4_red_green.jpg)
![](https://images.proteinatlas.org/28214/511_E8_1_red_green.jpg)
![](https://images.proteinatlas.org/28214/511_E8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P23786-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P23786 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR000542;IPR042572;IPR023213;IPR039551;IPR042231; |
| Pfam | PF00755; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000157184-CPT2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| MCUR1 | Intact, Biogrid | true |
| AK4 | Bioplex | false |
| CYSRT1 | Intact | false |
| GCAT | Bioplex | false |
| OTX1 | Intact | false |
| QRSL1 | Bioplex | false |
| SPRED2 | Bioplex | false |
| YARS2 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
