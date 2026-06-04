---
type: protein-evaluation
gene: "BCL9"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## BCL9 — REJECTED (研究热度过高 (PubMed strict=165，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BCL9 |
| 蛋白名称 | B-cell CLL/lymphoma 9 protein |
| 蛋白大小 | 1426 aa / 149.3 kDa |
| UniProt ID | O00512 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nuclear bodies; 额外: Cytosol; UniProt: Nucleus |
| 蛋白大小 | 5/10 | ×1 | 5 | 1426 aa / 149.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=165 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=42.6; PDB: 2GL7, 2VP7, 2VPB, 2VPD, 2VPE, 2VPG, 3SL9 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR015668, IPR024670, IPR013083; Pfam: PF11502 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **76.5/180** | |
| **归一化总分** | | | **42.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear bodies; 额外: Cytosol | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- beta-catenin-TCF complex (GO:1990907)
- cis-Golgi network (GO:0005801)
- nucleoplasm (GO:0005654)
- sarcoplasm (GO:0016528)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 165 |
| PubMed broad count | 280 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Human Genetics of Ventricular Septal Defect.. *Advances in experimental medicine and biology*. PMID: 38884729
2. Genomic analyses identify recurrent MEF2D fusions in acute lymphoblastic leukaemia.. *Nature communications*. PMID: 27824051
3. Multi‑layered prevention and treatment of chronic inflammation, organ fibrosis and cancer associated with canonical WNT/β‑catenin signaling activation (Review).. *International journal of molecular medicine*. PMID: 29786110
4. Recent advances in β-catenin/BCL9 protein-protein interaction inhibitors.. *Future medicinal chemistry*. PMID: 33849283
5. β-Catenin Drives Butyrophilin-like Molecule Loss and γδ T-cell Exclusion in Colon Cancer.. *Cancer immunology research*. PMID: 37309673

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 42.6 |
| 高置信度残基 (pLDDT>90) 占比 | 2.5% |
| 置信残基 (pLDDT 70-90) 占比 | 4.1% |
| 中等置信 (pLDDT 50-70) 占比 | 7.5% |
| 低置信 (pLDDT<50) 占比 | 86.0% |
| 有序区域 (pLDDT>70) 占比 | 6.6% |
| 可用 PDB 条目 | 2GL7, 2VP7, 2VPB, 2VPD, 2VPE, 2VPG, 3SL9, 8Y0P |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=42.6），有序残基占 6.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR015668, IPR024670, IPR013083; Pfam: PF11502 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CTNNB1 | 0.999 | 0.979 | — |
| PYGO1 | 0.999 | 0.977 | — |
| PYGO2 | 0.999 | 0.718 | — |
| HNF4A | 0.979 | 0.000 | — |
| TCF7L2 | 0.976 | 0.893 | — |
| BCL9L | 0.963 | 0.221 | — |
| TCF4 | 0.930 | 0.292 | — |
| TLE1 | 0.925 | 0.000 | — |
| LDB1 | 0.920 | 0.221 | — |
| H3C12 | 0.916 | 0.800 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| lgs | psi-mi:"MI:0018"(two hybrid) | pubmed:11955446 |
| CTNNB1 | psi-mi:"MI:0018"(two hybrid) | pubmed:11955446 |
| arm | psi-mi:"MI:0018"(two hybrid) | pubmed:11955446 |
| pygo | psi-mi:"MI:0018"(two hybrid) | pubmed:11955446 |
| TCF4 | psi-mi:"MI:0096"(pull down) | pubmed:11955446 |
| CDC73 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:16630820|imex:IM-11820 |
| PYGO2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:17113272|imex:IM-19196 |
| ENSP00000234739.3 | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:18498752|imex:IM-17354 |
| PYGO1 | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:18498752|imex:IM-17354 |
| Trpm7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:24855944|imex:IM-22990 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=42.6 + PDB: 2GL7, 2VP7, 2VPB, 2VPD, 2VPE,  | pLDDT=42.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Nuclear bodies; 额外: Cytosol | 一致 |
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
1. BCL9 — B-cell CLL/lymphoma 9 protein，研究基础较多，新颖性有限。
2. 蛋白大小1426 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 165 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=42.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 165 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O00512
- Protein Atlas: https://www.proteinatlas.org/ENSG00000116128-BCL9/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BCL9
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O00512
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
