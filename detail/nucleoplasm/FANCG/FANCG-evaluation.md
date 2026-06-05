---
type: protein-evaluation
gene: "FANCG"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FANCG — REJECTED (研究热度过高 (PubMed strict=209，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FANCG / XRCC9 |
| 蛋白名称 | Fanconi anemia group G protein |
| 蛋白大小 | 622 aa / 68.6 kDa |
| UniProt ID | O15287 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 622 aa / 68.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=209 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=83.1; PDB: 7KZP, 7KZQ, 7KZR, 7KZS, 7KZT, 7KZV |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR039684, IPR011990, IPR019734 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytosol (GO:0005829)
- Fanconi anaemia nuclear complex (GO:0043240)
- mitochondrion (GO:0005739)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 209 |
| PubMed broad count | 310 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: XRCC9 |

**关键文献**:
1. Pathogenic mutations identified by a multimodality approach in 117 Japanese Fanconi anemia patients.. *Haematologica*. PMID: 30792206
2. Fanconi Anemia.. **. PMID: 20301575
3. Molecular analysis of Fanconi anemia: the experience of the Bone Marrow Failure Study Group of the Italian Association of Pediatric Onco-Hematology.. *Haematologica*. PMID: 24584348
4. [Fanconi anemia].. *Nihon rinsho. Japanese journal of clinical medicine*. PMID: 10921325
5. Pathogenic variants reveal candidate genes for prostate cancer germline testing for men of African ancestry.. *Nature communications*. PMID: 41038821

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.1 |
| 高置信度残基 (pLDDT>90) 占比 | 53.1% |
| 置信残基 (pLDDT 70-90) 占比 | 29.3% |
| 中等置信 (pLDDT 50-70) 占比 | 7.9% |
| 低置信 (pLDDT<50) 占比 | 9.8% |
| 有序区域 (pLDDT>70) 占比 | 82.4% |
| 可用 PDB 条目 | 7KZP, 7KZQ, 7KZR, 7KZS, 7KZT, 7KZV |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（7KZP, 7KZQ, 7KZR, 7KZS, 7KZT, 7KZV）+ AlphaFold极高置信度预测（pLDDT=83.1），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039684, IPR011990, IPR019734 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FANCF | 0.999 | 0.998 | — |
| FAAP20 | 0.999 | 0.994 | — |
| CENPS | 0.999 | 0.994 | — |
| CENPX | 0.999 | 0.994 | — |
| FANCE | 0.999 | 0.955 | — |
| FANCL | 0.999 | 0.998 | — |
| FANCI | 0.999 | 0.800 | — |
| FANCC | 0.999 | 0.998 | — |
| FANCB | 0.999 | 0.998 | — |
| FANCM | 0.999 | 0.994 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| USHBP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| KRT19 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ZBED1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| GABPB1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| FANCF | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:11063725 |
| FANCA | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:11063725 |
| SAMD3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| FANCD2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-14933|pubmed:18212739 |
| EBI-1639774 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-14933|pubmed:18212739 |
| FTSJ3 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-11695|pubmed:19447967 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.1 + PDB: 7KZP, 7KZQ, 7KZR, 7KZS, 7KZT,  | pLDDT=83.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nuclear speckles | 一致 |
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
1. FANCG — Fanconi anemia group G protein，研究基础较多，新颖性有限。
2. 蛋白大小622 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 209 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 209 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O15287
- Protein Atlas: https://www.proteinatlas.org/ENSG00000221829-FANCG/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FANCG
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O15287
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O15287-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
