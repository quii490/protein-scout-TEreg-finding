---
type: protein-evaluation
gene: "FANCC"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FANCC — REJECTED (研究热度过高 (PubMed strict=304，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FANCC / FAC, FACC |
| 蛋白名称 | Fanconi anemia group C protein |
| 蛋白大小 | 558 aa / 63.4 kDa |
| UniProt ID | Q00597 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 558 aa / 63.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=304 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=82.1; PDB: 7KZP, 7KZQ, 7KZR, 7KZS, 7KZT, 7KZV |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000686; Pfam: PF02106 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- Fanconi anaemia nuclear complex (GO:0043240)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 304 |
| PubMed broad count | 510 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FAC, FACC |

**关键文献**:
1. Fanconi Anemia.. **. PMID: 20301575
2. Pathogenic mutations identified by a multimodality approach in 117 Japanese Fanconi anemia patients.. *Haematologica*. PMID: 30792206
3. Contribution of Germline Predisposition Gene Mutations to Breast Cancer Risk in African American Women.. *Journal of the National Cancer Institute*. PMID: 32427313
4. Gemcitabine and cisplatin plus nivolumab as organ-sparing treatment for muscle-invasive bladder cancer: a phase 2 trial.. *Nature medicine*. PMID: 37783966
5. Molecular analysis of Fanconi anemia: the experience of the Bone Marrow Failure Study Group of the Italian Association of Pediatric Onco-Hematology.. *Haematologica*. PMID: 24584348

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.1 |
| 高置信度残基 (pLDDT>90) 占比 | 30.3% |
| 置信残基 (pLDDT 70-90) 占比 | 54.7% |
| 中等置信 (pLDDT 50-70) 占比 | 11.5% |
| 低置信 (pLDDT<50) 占比 | 3.6% |
| 有序区域 (pLDDT>70) 占比 | 85.0% |
| 可用 PDB 条目 | 7KZP, 7KZQ, 7KZR, 7KZS, 7KZT, 7KZV |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（7KZP, 7KZQ, 7KZR, 7KZS, 7KZT, 7KZV）+ AlphaFold极高置信度预测（pLDDT=82.1），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000686; Pfam: PF02106 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FANCI | 0.999 | 0.800 | — |
| FANCL | 0.999 | 0.998 | — |
| FANCE | 0.999 | 0.998 | — |
| CENPX | 0.999 | 0.994 | — |
| CENPS | 0.999 | 0.994 | — |
| FAAP20 | 0.999 | 0.994 | — |
| FANCF | 0.999 | 0.998 | — |
| FANCD2 | 0.999 | 0.911 | — |
| FANCA | 0.999 | 0.998 | — |
| FAAP100 | 0.999 | 0.998 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CAPN10 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| FANCE | psi-mi:"MI:0018"(two hybrid) | pubmed:12649160|imex:IM-19947 |
| LASP1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| FANCB | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| FAAP100 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| DNAJC5 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:29997244|imex:IM-26441| |
| HNRNPCL2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| FANCM | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17289582|imex:IM-25488 |
| FANCG | psi-mi:"MI:0231"(mammalian protein protein interac | imex:IM-23318|pubmed:25416956 |
| MEOX2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:26871637|imex:IM-25013| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.1 + PDB: 7KZP, 7KZQ, 7KZR, 7KZS, 7KZT,  | pLDDT=82.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. FANCC — Fanconi anemia group C protein，研究基础较多，新颖性有限。
2. 蛋白大小558 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 304 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 304 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q00597
- Protein Atlas: https://www.proteinatlas.org/ENSG00000158169-FANCC/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FANCC
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q00597
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q00597-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
