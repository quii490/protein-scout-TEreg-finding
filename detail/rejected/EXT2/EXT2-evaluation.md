---
type: protein-evaluation
gene: "EXT2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EXT2 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=289，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EXT2 |
| 蛋白名称 | Exostosin-2 |
| 蛋白大小 | 718 aa / 82.3 kDa |
| UniProt ID | Q93063 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Golgi apparatus; UniProt: Golgi apparatus membrane; Golgi apparatus, cis-Golgi network |
| 蛋白大小 | 10/10 | ×1 | 10 | 718 aa / 82.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=289 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=87.5; PDB: 7SCH, 7SCJ, 7SCK, 7UQX, 7UQY, 7ZAY |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR004263, IPR040911, IPR015338, IPR029044; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **76.0/180** | |
| **归一化总分** | | | **42.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus | Supported |
| UniProt | Golgi apparatus membrane; Golgi apparatus, cis-Golgi network membrane; Endoplasmic reticulum membran... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- catalytic complex (GO:1902494)
- endoplasmic reticulum (GO:0005783)
- extracellular exosome (GO:0070062)
- Golgi apparatus (GO:0005794)
- Golgi membrane (GO:0000139)
- membrane (GO:0016020)
- UDP-N-acetylglucosamine transferase complex (GO:0043541)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 289 |
| PubMed broad count | 476 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Genetics of short stature.. *Current opinion in pediatrics*. PMID: 40658013
2. Structure of the human heparan sulfate polymerase complex EXT1-EXT2.. *Nature communications*. PMID: 36402845
3. Association between variants of EXT2 and type 2 diabetes: a replication and meta-analysis.. *Human genetics*. PMID: 23052945
4. Protocadherin 7-Associated Membranous Nephropathy.. *Journal of the American Society of Nephrology : JASN*. PMID: 33833079
5. EXT2: a novel prognostic and predictive biomarker for head and neck squamous cell carcinoma.. *Oral surgery, oral medicine, oral pathology and oral radiology*. PMID: 38155009

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.5 |
| 高置信度残基 (pLDDT>90) 占比 | 66.9% |
| 置信残基 (pLDDT 70-90) 占比 | 21.6% |
| 中等置信 (pLDDT 50-70) 占比 | 5.6% |
| 低置信 (pLDDT<50) 占比 | 6.0% |
| 有序区域 (pLDDT>70) 占比 | 88.5% |
| 可用 PDB 条目 | 7SCH, 7SCJ, 7SCK, 7UQX, 7UQY, 7ZAY |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（7SCH, 7SCJ, 7SCK, 7UQX, 7UQY, 7ZAY）+ AlphaFold极高置信度预测（pLDDT=87.5），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004263, IPR040911, IPR015338, IPR029044; Pfam: PF03016, PF09258 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EXT1 | 0.999 | 0.957 | — |
| NDST1 | 0.946 | 0.095 | — |
| ALX4 | 0.912 | 0.000 | — |
| ACCS | 0.873 | 0.000 | — |
| ACCSL | 0.818 | 0.000 | — |
| HHEX | 0.783 | 0.000 | — |
| HS2ST1 | 0.783 | 0.000 | — |
| SLC30A8 | 0.769 | 0.000 | — |
| TRAP1 | 0.760 | 0.313 | — |
| NDST2 | 0.757 | 0.091 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| sotv | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| ttv | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:14998928 |
| STK16 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| SNCG | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| HYOU1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| CNTF | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| FABP4 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| CRB1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ELOC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ENSP00000508361.1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.5 + PDB: 7SCH, 7SCJ, 7SCK, 7UQX, 7UQY,  | pLDDT=87.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Golgi apparatus membrane; Golgi apparatus, cis-Gol / Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. EXT2 — Exostosin-2，研究基础较多，新颖性有限。
2. 蛋白大小718 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 289 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q93063
- Protein Atlas: https://www.proteinatlas.org/ENSG00000151348-EXT2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EXT2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q93063
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
