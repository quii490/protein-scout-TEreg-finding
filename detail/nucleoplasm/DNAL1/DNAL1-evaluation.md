---
type: protein-evaluation
gene: "DNAL1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DNAL1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DNAL1 / C14orf168 |
| 蛋白名称 | Dynein axonemal light chain 1 |
| 蛋白大小 | 190 aa / 21.5 kDa |
| UniProt ID | Q4LDG9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Basal body, Cytosol, Principal piece; 额外: Centr; UniProt: Cytoplasm, cytoskeleton, cilium axoneme |
| 蛋白大小 | 8/10 | ×1 | 8 | 190 aa / 21.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=94.8; PDB: 8J07 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001611, IPR025875, IPR032675; Pfam: PF12799 |
| PPI 网络 | 10/10 | ×3 | 30 | STRING 15 partners; IntAct 6 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **146.0/180** | |
| **归一化总分** | | | **81.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Basal body, Cytosol, Principal piece; 额外: Centriolar satellite, Centrosome, Acrosome, Mid piece, End piece | Approved |
| UniProt | Cytoplasm, cytoskeleton, cilium axoneme | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- microtubule (GO:0005874)
- outer dynein arm (GO:0036157)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 34 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C14orf168 |

**关键文献**:
1. Primary Ciliary Dyskinesia.. **. PMID: 20301301
2. BAG5 regulates HSPA8-mediated protein folding required for sperm head-tail coupling apparatus assembly.. *EMBO reports*. PMID: 38454159
3. Characterization of pathogenic genetic variants in Russian patients with primary ciliary dyskinesia using gene panel sequencing and transcript analysis.. *Orphanet journal of rare diseases*. PMID: 39180133
4. Identification and analysis of axonemal dynein light chain 1 in primary ciliary dyskinesia patients.. *American journal of respiratory cell and molecular biology*. PMID: 15845866
5. Obesity impairs ciliary function and mucociliary clearance in the murine airway epithelium.. *American journal of physiology. Lung cellular and molecular physiology*. PMID: 39104315

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.8 |
| 高置信度残基 (pLDDT>90) 占比 | 93.7% |
| 置信残基 (pLDDT 70-90) 占比 | 2.1% |
| 中等置信 (pLDDT 50-70) 占比 | 1.6% |
| 低置信 (pLDDT<50) 占比 | 2.6% |
| 有序区域 (pLDDT>70) 占比 | 95.8% |
| 可用 PDB 条目 | 8J07 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=94.8，有序区 95.8%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001611, IPR025875, IPR032675; Pfam: PF12799 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FTCD | 0.979 | 0.000 | — |
| DNAH5 | 0.968 | 0.174 | — |
| SEPSECS | 0.874 | 0.000 | — |
| MAP1B | 0.872 | 0.048 | — |
| DNAI2 | 0.863 | 0.130 | — |
| DNAH7 | 0.833 | 0.174 | — |
| MAP1LC3A | 0.813 | 0.000 | — |
| DNAH3 | 0.811 | 0.174 | — |
| CCDC114 | 0.805 | 0.000 | — |
| DNAH2 | 0.805 | 0.174 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| LRRC40 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| RAP1GDS1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RHOA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MFHAS1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ALOX12B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ENST00000311089 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 6
- 调控相关比例: 7 / 15 = 47%

**评价**: STRING 15 个预测互作，IntAct 6 个实验互作。调控相关配体占比 47%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.8 + PDB: 8J07 | pLDDT=94.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, cilium axoneme / Nucleoplasm, Basal body, Cytosol, Principal piece; | 一致 |
| PPI | STRING + IntAct | 15 + 6 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DNAL1 — Dynein axonemal light chain 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小190 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q4LDG9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000119661-DNAL1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DNAL1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q4LDG9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
