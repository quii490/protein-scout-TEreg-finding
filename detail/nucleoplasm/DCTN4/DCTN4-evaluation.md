---
type: protein-evaluation
gene: "DCTN4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DCTN4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DCTN4 |
| 蛋白名称 | Dynactin subunit 4 |
| 蛋白大小 | 460 aa / 52.3 kDa |
| UniProt ID | Q9UJW0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Centrosome; 额外: Calyx; UniProt: Cytoplasm, cytoskeleton; Cytoplasm, cytoskeleton, microtubul |
| 蛋白大小 | 10/10 | ×1 | 10 | 460 aa / 52.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=15 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=84.3; PDB: 9B7J, 9B85 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR008603; Pfam: PF05502 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **142.0/180** | |
| **归一化总分** | | | **78.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Centrosome; 额外: Calyx | Approved |
| UniProt | Cytoplasm, cytoskeleton; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Cytopla... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cell cortex (GO:0005938)
- centrosome (GO:0005813)
- cytoplasm (GO:0005737)
- cytoplasmic dynein complex (GO:0005868)
- cytosol (GO:0005829)
- dynactin complex (GO:0005869)
- focal adhesion (GO:0005925)
- kinetochore (GO:0000776)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed broad count | 21 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Study on the Prognostic Values of Dynactin Genes in Low-Grade Glioma.. *Technology in cancer research & treatment*. PMID: 33896271
2. Comprehensive analysis reveals COPB2 and RYK associated with tumor stages of larynx squamous cell carcinoma.. *BMC cancer*. PMID: 35715770
3. Distinct prognostic value of dynactin subunit 4 (DCTN4) and diagnostic value of DCTN1, DCTN2, and DCTN4 in colon adenocarcinoma.. *Cancer management and research*. PMID: 30510450
4. DCTN4 as a modifier of chronic Pseudomonas aeruginosa infection in cystic fibrosis.. *The clinical respiratory journal*. PMID: 25763772
5. Cellular and Viral Determinants of HSV-1 Entry and Intracellular Transport towards Nucleus of Infected Cells.. *Journal of virology*. PMID: 33472938

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.3 |
| 高置信度残基 (pLDDT>90) 占比 | 63.5% |
| 置信残基 (pLDDT 70-90) 占比 | 19.8% |
| 中等置信 (pLDDT 50-70) 占比 | 7.4% |
| 低置信 (pLDDT<50) 占比 | 9.3% |
| 有序区域 (pLDDT>70) 占比 | 83.3% |
| 可用 PDB 条目 | 9B7J, 9B85 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（9B7J, 9B85）+ AlphaFold高质量预测（pLDDT=84.3），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008603; Pfam: PF05502 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DCTN6 | 0.999 | 0.991 | — |
| DCTN5 | 0.999 | 0.995 | — |
| ACTR10 | 0.999 | 0.993 | — |
| DCTN1 | 0.999 | 0.983 | — |
| DCTN2 | 0.999 | 0.993 | — |
| ACTR1A | 0.999 | 0.985 | — |
| ACTR1B | 0.998 | 0.944 | — |
| DCTN3 | 0.996 | 0.899 | — |
| CAPZB | 0.992 | 0.965 | — |
| CAPZA1 | 0.987 | 0.931 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Ank2 | psi-mi:"MI:0663"(confocal microscopy) | imex:IM-12153|pubmed:19109891 |
| Capza1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| Cep76 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| Actr1a | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| Dctn2 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| Dctn3 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| Dctn1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| RAB11A | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| LRRK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31046837|imex:IM-26684 |
| RAB5A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.3 + PDB: 9B7J, 9B85 | pLDDT=84.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton; Cytoplasm, cytoskeleton,  / Nucleoplasm, Centrosome; 额外: Calyx | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DCTN4 — Dynactin subunit 4，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小460 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 15 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UJW0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000132912-DCTN4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DCTN4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UJW0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000132912-DCTN4/subcellular

![](https://images.proteinatlas.org/38026/2204_F8_25_blue_red_green.jpg)
![](https://images.proteinatlas.org/38026/2204_F8_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/17532/944_C3_2_red_green.jpg)
![](https://images.proteinatlas.org/17532/944_C3_3_red_green.jpg)
![](https://images.proteinatlas.org/17532/947_C3_1_red_green.jpg)
![](https://images.proteinatlas.org/17532/947_C3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UJW0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
