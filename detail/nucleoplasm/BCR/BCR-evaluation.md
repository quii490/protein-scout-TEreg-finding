---
type: protein-evaluation
gene: "BCR"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## BCR — REJECTED (研究热度过高 (PubMed strict=9904，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BCR / BCR1, D22S11 |
| 蛋白名称 | Breakpoint cluster region protein |
| 蛋白大小 | 1271 aa / 142.8 kDa |
| UniProt ID | P11274 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Plasma membrane, Cytosol; 额外: Nucleoplasm; UniProt: Postsynaptic density; Cell projection, dendritic spine; Cell |
| 蛋白大小 | 5/10 | ×1 | 5 | 1271 aa / 142.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=9904 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.8; PDB: 1K1F, 2AIN, 5N6R, 5N7E, 5OC7 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR037769, IPR015123, IPR036481, IPR000008, IPR035 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **64.5/180** | |
| **归一化总分** | | | **35.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cytosol; 额外: Nucleoplasm | Approved |
| UniProt | Postsynaptic density; Cell projection, dendritic spine; Cell projection, axon; Synapse | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- axon (GO:0030424)
- cytosol (GO:0005829)
- dendritic spine (GO:0043197)
- extracellular exosome (GO:0070062)
- glutamatergic synapse (GO:0098978)
- membrane (GO:0016020)
- plasma membrane (GO:0005886)
- postsynaptic density (GO:0014069)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9904 |
| PubMed broad count | 48213 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BCR1, D22S11 |

**关键文献**:
1. BCR-ABL: The molecular mastermind behind chronic myeloid leukemia.. *Cytokine & growth factor reviews*. PMID: 40360311
2. BCR-ABL gene variants.. *Bailliere's clinical haematology*. PMID: 9376660
3. [JAK2, CALR].. *Rinsho byori. The Japanese journal of clinical pathology*. PMID: 30695513
4. Diagnosis- and Prognosis-Related Gene Alterations in BCR::ABL1-Negative Myeloproliferative Neoplasms.. *International journal of molecular sciences*. PMID: 37629188
5. The BCR/ABL hybrid gene.. *Bailliere's clinical haematology*. PMID: 3332859

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.8 |
| 高置信度残基 (pLDDT>90) 占比 | 21.5% |
| 置信残基 (pLDDT 70-90) 占比 | 32.7% |
| 中等置信 (pLDDT 50-70) 占比 | 7.4% |
| 低置信 (pLDDT<50) 占比 | 38.4% |
| 有序区域 (pLDDT>70) 占比 | 54.2% |
| 可用 PDB 条目 | 1K1F, 2AIN, 5N6R, 5N7E, 5OC7 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=64.8），有序残基占 54.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR037769, IPR015123, IPR036481, IPR000008, IPR035892; Pfam: PF09036, PF00168, PF19057 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ABL1 | 0.996 | 0.737 | — |
| GRB2 | 0.994 | 0.887 | — |
| CRKL | 0.975 | 0.624 | — |
| CBL | 0.971 | 0.683 | — |
| CRK | 0.945 | 0.395 | — |
| STAT5B | 0.936 | 0.000 | — |
| SHC1 | 0.925 | 0.163 | — |
| STAT5A | 0.924 | 0.000 | — |
| SHC3 | 0.901 | 0.000 | — |
| SHC2 | 0.900 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Ighm | psi-mi:"MI:0813"(proximity ligation assay) | imex:IM-23964|pubmed:24963139 |
| Cd79a | psi-mi:"MI:0813"(proximity ligation assay) | imex:IM-23964|pubmed:24963139 |
| TP53 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| UNC119 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| IGSF21 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| jbug | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| CFTR | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12000|pubmed:17110338 |
| GRB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15417|pubmed:21706016 |
| TNKS2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:22153077|imex:IM-16612 |
| EBI-1380972 | psi-mi:"MI:0096"(pull down) | pubmed:17721511|imex:IM-19952 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.8 + PDB: 1K1F, 2AIN, 5N6R, 5N7E, 5OC7 | pLDDT=64.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Postsynaptic density; Cell projection, dendritic s / Plasma membrane, Cytosol; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. BCR — Breakpoint cluster region protein，研究基础较多，新颖性有限。
2. 蛋白大小1271 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 9904 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=64.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 9904 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P11274
- Protein Atlas: https://www.proteinatlas.org/ENSG00000186716-BCR/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BCR
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P11274
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
