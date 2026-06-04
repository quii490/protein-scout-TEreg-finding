---
type: protein-evaluation
gene: "CILP2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CILP2 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CILP2 |
| 蛋白名称 | Cartilage intermediate layer protein 2 |
| 蛋白大小 | 1156 aa / 126.3 kDa |
| UniProt ID | Q8IUL8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Secreted, extracellular space, extracellular matrix |
| 蛋白大小 | 8/10 | ×1 | 8 | 1156 aa / 126.3 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=63 篇 (≤80→4) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=80.1; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR008969, IPR056257, IPR056256, IPR056258, IPR056 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.0/180** | |
| **归一化总分** | | | **44.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Secreted, extracellular space, extracellular matrix | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- extracellular exosome (GO:0070062)
- extracellular space (GO:0005615)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 63 |
| PubMed broad count | 80 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Inhibition of CILP2 Improves Glucose Metabolism and Mitochondrial Dysfunction in Sarcopenia via the Wnt Signalling Pathway.. *Journal of cachexia, sarcopenia and muscle*. PMID: 39385717
2. The Prognostic and Immune Significance of CILP2 in Pan-Cancer and Its Relationship with the Progression of Pancreatic Cancer.. *Cancers*. PMID: 38136386
3. Proteogenomic Analysis of Coronary Artery Calcification in Human Populations.. *Arteriosclerosis, thrombosis, and vascular biology*. PMID: 41924874
4. CILP2 promotes hypertrophic scar through Snail acetylation by interaction with ACLY.. *Biochimica et biophysica acta. Molecular basis of disease*. PMID: 38670440
5. Association of the NCAN-TM6SF2-CILP2-PBX4-SUGP1-MAU2 SNPs and gene-gene and gene-environment interactions with serum lipid levels.. *Aging*. PMID: 32568739

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.1 |
| 高置信度残基 (pLDDT>90) 占比 | 34.7% |
| 置信残基 (pLDDT 70-90) 占比 | 46.0% |
| 中等置信 (pLDDT 50-70) 占比 | 10.9% |
| 低置信 (pLDDT<50) 占比 | 8.4% |
| 有序区域 (pLDDT>70) 占比 | 80.7% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=80.1，有序区 80.7%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008969, IPR056257, IPR056256, IPR056258, IPR056255; Pfam: PF13620, PF23591, PF23708 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| VWCE | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DEFA5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DEFA1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MATN4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LY86 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| FBXO2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SFTPC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TMEM106A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| BTNL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| NCR3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.1 + PDB: 无 | pLDDT=80.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Secreted, extracellular space, extracellular matri / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CILP2 — Cartilage intermediate layer protein 2，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小1156 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 63 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IUL8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000160161-CILP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CILP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IUL8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
