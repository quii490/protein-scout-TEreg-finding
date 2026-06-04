---
type: protein-evaluation
gene: "GORASP2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GORASP2 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GORASP2 / GOLPH6 |
| 蛋白名称 | Golgi reassembly-stacking protein 2 |
| 蛋白大小 | 452 aa / 47.1 kDa |
| UniProt ID | Q9H8Y8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Golgi apparatus; UniProt: Golgi apparatus membrane; Endoplasmic reticulum membrane; Go |
| 蛋白大小 | 10/10 | ×1 | 10 | 452 aa / 47.1 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=26 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.5; PDB: 3RLE, 4EDJ |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR007583, IPR024958, IPR036034; Pfam: PF04495 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **100.5/180** | |
| **归一化总分** | | | **55.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus | Enhanced |
| UniProt | Golgi apparatus membrane; Endoplasmic reticulum membrane; Golgi apparatus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cis-Golgi network (GO:0005801)
- endoplasmic reticulum membrane (GO:0005789)
- Golgi apparatus (GO:0005794)
- Golgi membrane (GO:0000139)
- membrane (GO:0016020)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 26 |
| PubMed broad count | 78 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GOLPH6 |

**关键文献**:
1. Autophagy-based unconventional secretion of HMGB1 by keratinocytes plays a pivotal role in psoriatic skin inﬂammation.. *Autophagy*. PMID: 32019420
2. TRIM16 mediates secretory autophagy in head and neck cancer-associated fibroblasts.. *Autophagy*. PMID: 40383937
3. GORASP2 promotes phagophore closure and autophagosome maturation into autolysosomes.. *Autophagy*. PMID: 39056394
4. Golgi Reassembly Stacking Protein 2 Modulates Myometrial Contractility during Labor by Affecting ATP Production.. *International journal of molecular sciences*. PMID: 37373263
5. The Golgi Stacking Protein GORASP2 Regulates Mouse Primordial Follicle Activation by Suppressing the Autophagy Lysosome Pathway via RAP1 Competing With mTOR for RAPTOR Binding.. *FASEB journal : official publication of the Federation of American Societies for Experimental Biology*. PMID: 40522147

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.5 |
| 高置信度残基 (pLDDT>90) 占比 | 32.1% |
| 置信残基 (pLDDT 70-90) 占比 | 11.7% |
| 中等置信 (pLDDT 50-70) 占比 | 8.2% |
| 低置信 (pLDDT<50) 占比 | 48.0% |
| 有序区域 (pLDDT>70) 占比 | 43.8% |
| 可用 PDB 条目 | 3RLE, 4EDJ |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=64.5），有序残基占 43.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007583, IPR024958, IPR036034; Pfam: PF04495 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BLZF1 | 0.999 | 0.855 | — |
| GOLGA2 | 0.994 | 0.836 | — |
| RAB2A | 0.986 | 0.457 | — |
| SMU1 | 0.881 | 0.000 | — |
| RAB1A | 0.868 | 0.322 | — |
| TMED7 | 0.829 | 0.734 | — |
| JAM3 | 0.825 | 0.797 | — |
| JAM2 | 0.823 | 0.797 | — |
| TMED2 | 0.770 | 0.623 | — |
| GORASP1 | 0.763 | 0.124 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PCBD1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| PRPS1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| NQO2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| NUP62 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TRAF2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| RAD54B | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CBLB | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MIF | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TSC22D4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| NME1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.5 + PDB: 3RLE, 4EDJ | pLDDT=64.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Golgi apparatus membrane; Endoplasmic reticulum me / Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GORASP2 — Golgi reassembly-stacking protein 2，非常新颖，仅有少数基础研究。
2. 蛋白大小452 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 26 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=64.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H8Y8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000115806-GORASP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GORASP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H8Y8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
