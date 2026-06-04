---
type: protein-evaluation
gene: "PRRX1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PRRX1 — REJECTED (研究热度过高 (PubMed strict=208，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PRRX1 / PMX1 |
| 蛋白名称 | Paired mesoderm homeobox protein 1 |
| 蛋白大小 | 245 aa / 27.3 kDa |
| UniProt ID | P54821 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 245 aa / 27.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=208 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001356, IPR017970, IPR009057, IPR003654, IPR043 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 7 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.0/180** | |
| **归一化总分** | | | **44.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 208 |
| PubMed broad count | 570 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PMX1 |

**关键文献**:
1. Itm2a expression marks periosteal skeletal stem cells that contribute to bone fracture healing.. *The Journal of clinical investigation*. PMID: 39225088
2. A population of stem cells with strong regenerative potential discovered in deer antlers.. *Science (New York, N.Y.)*. PMID: 36821675
3. Neuroblastoma is composed of two super-enhancer-associated differentiation states.. *Nature genetics*. PMID: 28650485
4. Transcription factor Twist1 drives fibroblast activation to promote kidney fibrosis via signaling proteins Prrx1/TNC.. *Kidney international*. PMID: 39181396
5. H3K36 methyltransferase NSD1 protects against osteoarthritis through regulating chondrocyte differentiation and cartilage homeostasis.. *Cell death and differentiation*. PMID: 38012390

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.8 |
| 高置信度残基 (pLDDT>90) 占比 | 22.9% |
| 置信残基 (pLDDT 70-90) 占比 | 11.4% |
| 中等置信 (pLDDT 50-70) 占比 | 33.1% |
| 低置信 (pLDDT<50) 占比 | 32.7% |
| 有序区域 (pLDDT>70) 占比 | 34.3% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=64.8），有序残基占 34.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001356, IPR017970, IPR009057, IPR003654, IPR043378; Pfam: PF00046, PF03826 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EEF1AKNMT | 0.844 | 0.000 | — |
| NUP98 | 0.842 | 0.000 | — |
| TWIST1 | 0.794 | 0.000 | — |
| PAX9 | 0.718 | 0.000 | — |
| HOXD13 | 0.683 | 0.063 | — |
| HOXB13 | 0.662 | 0.063 | — |
| DDX10 | 0.658 | 0.046 | — |
| HAND2 | 0.653 | 0.048 | — |
| SIX1 | 0.646 | 0.051 | — |
| HOXD11 | 0.637 | 0.063 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RBL2 | psi-mi:"MI:0018"(two hybrid) | pubmed:9464541|imex:IM-19934 |
| SUOX | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CINP | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| - | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| FKBP5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| Alx4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| ALX3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 7
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 7 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.8 + PDB: 无 | pLDDT=64.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 7 interactions | 数据充分 |

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
1. PRRX1 — Paired mesoderm homeobox protein 1，研究基础较多，新颖性有限。
2. 蛋白大小245 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 208 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=64.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 208 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P54821
- Protein Atlas: https://www.proteinatlas.org/ENSG00000116132-PRRX1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PRRX1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P54821
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
