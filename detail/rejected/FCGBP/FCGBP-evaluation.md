---
type: protein-evaluation
gene: "FCGBP"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FCGBP — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=106，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FCGBP |
| 蛋白名称 | IgGFc-binding protein |
| 蛋白大小 | 5405 aa / 572.0 kDa |
| UniProt ID | Q9Y6R7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Plasma membrane; 额外: Golgi apparatus, Cytokinetic bridge; UniProt: Secreted |
| 蛋白大小 | 0/10 | ×1 | 0 | 5405 aa / 572.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=106 篇 (>100→REJECTED) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 8QCI |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000742, IPR003645, IPR035234, IPR050780, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **44.0/180** | |
| **归一化总分** | | | **24.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane; 额外: Golgi apparatus, Cytokinetic bridge | Approved |
| UniProt | Secreted | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- extracellular exosome (GO:0070062)
- extracellular matrix (GO:0031012)
- extracellular space (GO:0005615)
- Golgi lumen (GO:0005796)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 106 |
| PubMed broad count | 161 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. FCGBP functions as a tumor suppressor gene in head and neck squamous cell carcinoma.. *Discover oncology*. PMID: 39580769
2. Role of the mucin-like glycoprotein FCGBP in mucosal immunity and cancer.. *Frontiers in immunology*. PMID: 35936008
3. Whole-Exome Sequencing Among Chinese Patients With Hereditary Diffuse Gastric Cancer.. *JAMA network open*. PMID: 36484990
4. Revealing the role of necroptosis microenvironment: FCGBP + tumor-associated macrophages drive primary liver cancer differentiation towards cHCC-CCA or iCCA.. *Apoptosis : an international journal on programmed cell death*. PMID: 38017206
5. FCGBP Is a Prognostic Biomarker and Associated With Immune Infiltration in Glioma.. *Frontiers in oncology*. PMID: 35047393

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v? |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 8QCI |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000742, IPR003645, IPR035234, IPR050780, IPR036084; Pfam: PF08742, PF17517, PF01826 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TFF3 | 0.938 | 0.628 | — |
| MUC2 | 0.885 | 0.000 | — |
| CLCA1 | 0.846 | 0.396 | — |
| FAU | 0.806 | 0.789 | — |
| ZG16 | 0.780 | 0.000 | — |
| PIGR | 0.588 | 0.000 | — |
| AGR2 | 0.547 | 0.000 | — |
| A2M | 0.543 | 0.422 | — |
| MUC12 | 0.464 | 0.091 | — |
| GKN2 | 0.464 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Anpep | psi-mi:"MI:0276"(blue native page) | imex:IM-11844|pubmed:17205597 |
| MLH1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15124|pubmed:20706999 |
| O95784 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| TFAP2A | psi-mi:"MI:0018"(two hybrid) | imex:IM-22985|pubmed:24835590 |
| DDX19B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TFAP2C | psi-mi:"MI:0018"(two hybrid) | imex:IM-22985|pubmed:24835590 |
| CCR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| NRSN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PPP2R2B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| C18orf21 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 8QCI | pLDDT=0, v? | 预测+实验 |
| 定位 | UniProt + HPA | Secreted / Plasma membrane; 额外: Golgi apparatus, Cytokinetic  | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐ (REJECTED)

**核心优势**:
1. FCGBP — IgGFc-binding protein，研究基础较多，新颖性有限。
2. 蛋白大小5405 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 106 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y6R7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000275395-FCGBP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FCGBP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y6R7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
