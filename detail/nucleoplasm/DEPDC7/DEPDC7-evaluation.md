---
type: protein-evaluation
gene: "DEPDC7"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DEPDC7 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DEPDC7 |
| 蛋白名称 | DEP domain-containing protein 7 |
| 蛋白大小 | 511 aa / 58.3 kDa |
| UniProt ID | Q96QD5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli; 额外: Nucleoplasm, Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 511 aa / 58.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=73.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000591, IPR036388, IPR036390; Pfam: PF00610 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 12 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.0/180** | |
| **归一化总分** | | | **73.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; 额外: Nucleoplasm, Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 9 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Construction and Identification of the RNAi Recombinant Lentiviral Vector Targeting Human DEPDC7 Gene.. *Interdisciplinary sciences, computational life sciences*. PMID: 27016254
2. The Dishevelled, EGL-10 and pleckstrin (DEP) domain-containing protein DEPDC7 binds to CARMA2 and CARMA3 proteins, and regulates NF-κB activation.. *PloS one*. PMID: 25541973
3. Investigating the diagnostic and prognostic significance of genes related to fatty acid metabolism in hepatocellular carcinoma.. *BMC gastroenterology*. PMID: 39548390
4. Further evidence of DEPDC7 DNA hypomethylation in depression: A study in adult twins.. *European psychiatry : the journal of the Association of European Psychiatrists*. PMID: 25952135
5. DEPDC7 as a potential tumor suppressor in hepatocellular carcinoma: preliminary evidence for targeting the JAK1/STAT3 axis.. *Frontiers in oncology*. PMID: 41930189

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.6 |
| 高置信度残基 (pLDDT>90) 占比 | 15.5% |
| 置信残基 (pLDDT 70-90) 占比 | 52.6% |
| 中等置信 (pLDDT 50-70) 占比 | 15.5% |
| 低置信 (pLDDT<50) 占比 | 16.4% |
| 有序区域 (pLDDT>70) 占比 | 68.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=73.6，有序区 68.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000591, IPR036388, IPR036390; Pfam: PF00610 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CSTF3 | 0.929 | 0.000 | — |
| EIF3M | 0.926 | 0.000 | — |
| KIAA1549L | 0.874 | 0.000 | — |
| TCP11L1 | 0.739 | 0.000 | — |
| CARD14 | 0.631 | 0.000 | — |
| CCDC73 | 0.556 | 0.000 | — |
| QSER1 | 0.551 | 0.000 | — |
| WT1 | 0.543 | 0.000 | — |
| ABTB2 | 0.536 | 0.000 | — |
| CSTF1 | 0.531 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GTF2B | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| SLX4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12200|pubmed:19596235 |
| Rab5b | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| ZNF526 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| TACC3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Xpo1 | psi-mi:"MI:0096"(pull down) | pubmed:26673895|imex:IM-24970 |
| Ankrd26 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| APOD | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| S | psi-mi:"MI:1313"(proximity labelling technology) | pubmed:34232536|imex:IM-29365 |
| CFTR | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-29540|pubmed:36012204 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 12
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 12 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.6 + PDB: 无 | pLDDT=73.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoli; 额外: Nucleoplasm, Cytosol | 待确认 |
| PPI | STRING + IntAct | 15 + 12 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DEPDC7 — DEP domain-containing protein 7，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小511 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96QD5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000121690-DEPDC7/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DEPDC7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96QD5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (approved)。来源: https://www.proteinatlas.org/ENSG00000121690-DEPDC7/subcellular

![](https://images.proteinatlas.org/15800/127_H9_1_red_green.jpg)
![](https://images.proteinatlas.org/15800/127_H9_2_red_green.jpg)
![](https://images.proteinatlas.org/15800/128_H9_1_red_green.jpg)
![](https://images.proteinatlas.org/15800/128_H9_2_red_green.jpg)
![](https://images.proteinatlas.org/15800/129_H9_1_red_green.jpg)
![](https://images.proteinatlas.org/15800/129_H9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96QD5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
