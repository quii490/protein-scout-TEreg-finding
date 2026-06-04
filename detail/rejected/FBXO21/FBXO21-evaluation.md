---
type: protein-evaluation
gene: "FBXO21"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FBXO21 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FBXO21 / FBX21, KIAA0875 |
| 蛋白名称 | F-box only protein 21 |
| 蛋白大小 | 628 aa / 72.3 kDa |
| UniProt ID | O94952 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Centrosome, Cytosol; 额外: Primary cilium, Primary cilium tip,; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 628 aa / 72.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=20 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=85.3; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR036047, IPR001810, IPR011722, IPR036623, IPR032 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.5/180** | |
| **归一化总分** | | | **65.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Centrosome, Cytosol; 额外: Primary cilium, Primary cilium tip, Basal body | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- cytosol (GO:0005829)
- ubiquitin ligase complex (GO:0000151)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 20 |
| PubMed broad count | 26 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FBX21, KIAA0875 |

**关键文献**:
1. FBXO21 mediated degradation of p85α regulates proliferation and survival of acute myeloid leukemia.. *Leukemia*. PMID: 37689825
2. SCFFBXO21-mediated ubiquitination and degradation of NMNAT2 regulates axon survival in nerve injury.. *The Journal of cell biology*. PMID: 41026098
3. Fbxo21 regulates the epithelial-to-mesenchymal transition through ubiquitination of Nr2f2 in gastric cancer.. *Journal of Cancer*. PMID: 33531987
4. F-box protein FBXO21 overexpression inhibits the proliferation and metastasis of clear cell renal cell carcinoma and is closely related to the CREB pathway and tumor immune cell infiltration.. *Journal of translational medicine*. PMID: 40089779
5. FBXO21 mediates the ubiquitylation and proteasomal degradation of EID1.. *Genes to cells : devoted to molecular & cellular mechanisms*. PMID: 26085330

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.3 |
| 高置信度残基 (pLDDT>90) 占比 | 55.9% |
| 置信残基 (pLDDT 70-90) 占比 | 30.6% |
| 中等置信 (pLDDT 50-70) 占比 | 7.6% |
| 低置信 (pLDDT<50) 占比 | 5.9% |
| 有序区域 (pLDDT>70) 占比 | 86.5% |
| 可用 PDB 条目 | 无 |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=85.3，有序区 86.5%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036047, IPR001810, IPR011722, IPR036623, IPR032698; Pfam: PF12937, PF13369, PF08755 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CUL1 | 0.978 | 0.810 | — |
| SKP1 | 0.976 | 0.610 | — |
| RBX1 | 0.804 | 0.615 | — |
| EID1 | 0.786 | 0.627 | — |
| NUDCD1 | 0.674 | 0.619 | — |
| CAND1 | 0.644 | 0.000 | — |
| UBE2M | 0.636 | 0.292 | — |
| NEDD8 | 0.593 | 0.074 | — |
| NAE1 | 0.547 | 0.071 | — |
| SSC4D | 0.534 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CNTNAP4 | psi-mi:"MI:0018"(two hybrid) | pubmed:12421765 |
| CUL1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| NEDD8 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| COPS6 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| COPS5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| ARSG | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KERA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PRKCA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| EID1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| IDS | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.3 + PDB: 无 | pLDDT=85.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Centrosome, Cytosol; 额外: Primary cilium, Primary c | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. FBXO21 — F-box only protein 21，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小628 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 20 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O94952
- Protein Atlas: https://www.proteinatlas.org/ENSG00000135108-FBXO21/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FBXO21
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O94952
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
