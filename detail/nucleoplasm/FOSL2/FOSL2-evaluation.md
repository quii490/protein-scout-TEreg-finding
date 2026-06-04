---
type: protein-evaluation
gene: "FOSL2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FOSL2 — REJECTED (研究热度过高 (PubMed strict=231，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FOSL2 / FRA2 |
| 蛋白名称 | Fos-related antigen 2 |
| 蛋白大小 | 326 aa / 35.2 kDa |
| UniProt ID | P15408 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 326 aa / 35.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=231 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000837, IPR004827, IPR046347; Pfam: PF00170 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.0/180** | |
| **归一化总分** | | | **48.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- RNA polymerase II transcription regulator complex (GO:0090575)
- transcription factor AP-1 complex (GO:0035976)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 231 |
| PubMed broad count | 512 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FRA2 |

**关键文献**:
1. Fosl2 facilitates chromatin accessibility to determine developmental events during follicular maturation.. *Nature communications*. PMID: 41062456
2. Characterization of a pathogenic subpopulation of human glioma associated macrophages linked to glioma progression.. *Cancer cell*. PMID: 41529664
3. Identification of core genes in intervertebral disc degeneration using bioinformatics and machine learning algorithms.. *Frontiers in immunology*. PMID: 39050860
4. Short-chain fatty acid-butyric acid ameliorates granulosa cells inflammation through regulating METTL3-mediated N6-methyladenosine modification of FOSL2 in polycystic ovarian syndrome.. *Clinical epigenetics*. PMID: 37179374
5. Identification of transcription factors responsible for dysregulated networks in human osteoarthritis cartilage by global gene expression analysis.. *Osteoarthritis and cartilage*. PMID: 30081074

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.7 |
| 高置信度残基 (pLDDT>90) 占比 | 19.3% |
| 置信残基 (pLDDT 70-90) 占比 | 6.4% |
| 中等置信 (pLDDT 50-70) 占比 | 38.3% |
| 低置信 (pLDDT<50) 占比 | 35.9% |
| 有序区域 (pLDDT>70) 占比 | 25.7% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=61.7），有序残基占 25.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000837, IPR004827, IPR046347; Pfam: PF00170 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| JUND | 0.999 | 0.872 | — |
| JUNB | 0.999 | 0.880 | — |
| JUN | 0.999 | 0.956 | — |
| FOS | 0.998 | 0.000 | — |
| FOSB | 0.998 | 0.000 | — |
| FOSL1 | 0.998 | 0.000 | — |
| MAPK8 | 0.946 | 0.174 | — |
| MAPK9 | 0.936 | 0.174 | — |
| ATF7 | 0.918 | 0.843 | — |
| CREB5 | 0.836 | 0.824 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| GOPC | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| FHL3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| LHX8 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| NME7 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| LRIF1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CREB5 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| POLR2G | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| CYTH1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.7 + PDB: 无 | pLDDT=61.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
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
1. FOSL2 — Fos-related antigen 2，研究基础较多，新颖性有限。
2. 蛋白大小326 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 231 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=61.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 231 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P15408
- Protein Atlas: https://www.proteinatlas.org/ENSG00000075426-FOSL2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FOSL2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P15408
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
