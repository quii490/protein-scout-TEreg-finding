---
type: protein-evaluation
gene: "KYAT3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KYAT3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KYAT3 / CCBL2, KAT3 |
| 蛋白名称 | Kynurenine--oxoglutarate transaminase 3 |
| 蛋白大小 | 454 aa / 51.4 kDa |
| UniProt ID | Q6YP21 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Cytosol; 额外: Nucleoli, Cytokinetic bridge; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 454 aa / 51.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=91.3; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR004839, IPR051326, IPR015424, IPR015421, IPR015 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 13 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.0/180** | |
| **归一化总分** | | | **68.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoli, Cytokinetic bridge | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- mitochondrion (GO:0005739)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 10 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CCBL2, KAT3 |

**关键文献**:
1. Protective Effects of Lactobacillus gasseri against High-Cholesterol Diet-Induced Fatty Liver and Regulation of Host Gene Expression Profiles.. *International journal of molecular sciences*. PMID: 36768377
2. Superior neurometabolic protection by 8-hydroxy-dihydromyricetin over dihydromyricetin in diabetic zebrafish: insights from integrated metabolomics and transcriptomics.. *Food & function*. PMID: 40878641
3. Serum Small Extracellular Vesicles Proteome of Tuberculosis Patients Demonstrated Deregulated Immune Response.. *Proteomics. Clinical applications*. PMID: 31532894
4. Higher mitochondrial protein-Succinylation detected in lung tissues of idiopathic pulmonary fibrosis patients.. *Journal of proteomics*. PMID: 39938635
5. Effects of two longevity interventions, calorie restriction and rapamycin treatment, on the kynurenine-aryl hydrocarbon receptor pathway in aging skeletal muscle.. *Biochimie*. PMID: 41274338

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.3 |
| 高置信度残基 (pLDDT>90) 占比 | 81.3% |
| 置信残基 (pLDDT 70-90) 占比 | 9.5% |
| 中等置信 (pLDDT 50-70) 占比 | 1.3% |
| 低置信 (pLDDT<50) 占比 | 7.9% |
| 有序区域 (pLDDT>70) 占比 | 90.8% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=91.3，有序区 90.8%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004839, IPR051326, IPR015424, IPR015421, IPR015422; Pfam: PF00155 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RABIF | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| GABARAPL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| GABARAP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| MAP1LC3A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| MAP1LC3B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| GABARAPL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| CUL1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| COPS5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| CUL4B | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| TRUB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 13
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 13 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.3 + PDB: 无 | pLDDT=91.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Cytosol; 额外: Nucleoli, Cytokinetic bridge | 一致 |
| PPI | STRING + IntAct | 0 + 13 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. KYAT3 — Kynurenine--oxoglutarate transaminase 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小454 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6YP21
- Protein Atlas: https://www.proteinatlas.org/ENSG00000137944-KYAT3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KYAT3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6YP21
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
