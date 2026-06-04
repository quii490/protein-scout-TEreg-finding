---
type: protein-evaluation
gene: "ABAT"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ABAT — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=109，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ABAT / GABAT |
| 蛋白名称 | 4-aminobutyrate aminotransferase, mitochondrial |
| 蛋白大小 | 500 aa / 56.4 kDa |
| UniProt ID | P80404 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Mitochondria; UniProt: Mitochondrion matrix |
| 蛋白大小 | 10/10 | ×1 | 10 | 500 aa / 56.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=109 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=93.8; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR004631, IPR005814, IPR049704, IPR015424, IPR015 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 14 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **68.5/180** | |
| **归一化总分** | | | **38.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria | Supported |
| UniProt | Mitochondrion matrix | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 4-aminobutyrate transaminase complex (GO:0032144)
- mitochondrial matrix (GO:0005759)
- mitochondrion (GO:0005739)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 109 |
| PubMed broad count | 457 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GABAT |

**关键文献**:
1. Decoding sunitinib resistance in ccRCC: Metabolic-reprogramming-induced ABAT and GABAergic system shifts.. *iScience*. PMID: 39100925
2. Mitochondrial DNA maintenance defects.. *Biochimica et biophysica acta. Molecular basis of disease*. PMID: 28215579
3. A crucial exosome-related gene pair (AAMP and ABAT) is associated with inflammatory cells in intervertebral disc degeneration.. *Frontiers in immunology*. PMID: 37122729
4. Epigenetic dysregulation of articular cartilage during progression of hip femoroacetabular impingement disease.. *Journal of orthopaedic research : official publication of the Orthopaedic Research Society*. PMID: 36606425
5. ABAT and ALDH6A1, regulated by transcription factor HNF4A, suppress tumorigenic capability in clear cell renal cell carcinoma.. *Journal of translational medicine*. PMID: 32093682

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.8 |
| 高置信度残基 (pLDDT>90) 占比 | 92.0% |
| 置信残基 (pLDDT 70-90) 占比 | 0.4% |
| 中等置信 (pLDDT 50-70) 占比 | 0.4% |
| 低置信 (pLDDT<50) 占比 | 7.2% |
| 有序区域 (pLDDT>70) 占比 | 92.4% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=93.8，有序区 92.4%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004631, IPR005814, IPR049704, IPR015424, IPR015421; Pfam: PF00202 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ALDH5A1 | 0.994 | 0.134 | — |
| GAD2 | 0.976 | 0.092 | — |
| GAD1 | 0.975 | 0.092 | — |
| ALDH6A1 | 0.963 | 0.000 | — |
| UPB1 | 0.956 | 0.000 | — |
| ALDH7A1 | 0.954 | 0.267 | — |
| GADL1 | 0.949 | 0.092 | — |
| ALDH1B1 | 0.949 | 0.099 | — |
| ALDH3A2 | 0.947 | 0.099 | — |
| CNDP1 | 0.947 | 0.058 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| - | psi-mi:"MI:0096"(pull down) | pubmed:19805454|imex:IM-19495 |
| CRK | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| EBI-2696342 | psi-mi:"MI:0096"(pull down) | pubmed:19834914|imex:IM-20484 |
| ARMH1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZSCAN29 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SEC22C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ASGR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| EPHX1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SERINC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| NUFIP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 14
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 14 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.8 + PDB: 无 | pLDDT=93.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Mitochondrion matrix / Mitochondria | 一致 |
| PPI | STRING + IntAct | 15 + 14 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. ABAT — 4-aminobutyrate aminotransferase, mitochondrial，研究基础较多，新颖性有限。
2. 蛋白大小500 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 109 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P80404
- Protein Atlas: https://www.proteinatlas.org/ENSG00000183044-ABAT/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ABAT
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P80404
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
