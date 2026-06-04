---
type: protein-evaluation
gene: "AHR"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## AHR — REJECTED (研究热度过高 (PubMed strict=6137，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | AHR / BHLHE76 |
| 蛋白名称 | Aryl hydrocarbon receptor |
| 蛋白大小 | 848 aa / 96.1 kDa |
| UniProt ID | P35869 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Nucleoplasm; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 848 aa / 96.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=6137 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=56.5; PDB: 5NJ8, 7ZUB, 8QMO |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039091, IPR033348, IPR011598, IPR036638, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **79.0/180** | |
| **归一化总分** | | | **43.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- aryl hydrocarbon receptor complex (GO:0034751)
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- cytosolic aryl hydrocarbon receptor complex (GO:0034752)
- nuclear aryl hydrocarbon receptor complex (GO:0034753)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6137 |
| PubMed broad count | 31010 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BHLHE76 |

**关键文献**:
1. Structural basis for the ligand-dependent activation of heterodimeric AHR-ARNT complex.. *Nature communications*. PMID: 39900897
2. Gene and Protein Expression in Subjects With a Nystagmus-Associated AHR Mutation.. *Frontiers in genetics*. PMID: 33193710
3. DNA binding and protein interactions of the AHR/ARNT heterodimer that facilitate gene activation.. *Chemico-biological interactions*. PMID: 12213385
4. Sphingosine Kinase 2 Regulates Aryl Hydrocarbon Receptor Nuclear Translocation and Target Gene Activation.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 39207053
5. The AHR-NRF2-JDP2 gene battery: Ligand-induced AHR transcriptional activation.. *Biochemical pharmacology*. PMID: 39855429

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 56.5 |
| 高置信度残基 (pLDDT>90) 占比 | 21.7% |
| 置信残基 (pLDDT 70-90) 占比 | 13.1% |
| 中等置信 (pLDDT 50-70) 占比 | 10.5% |
| 低置信 (pLDDT<50) 占比 | 54.7% |
| 有序区域 (pLDDT>70) 占比 | 34.8% |
| 可用 PDB 条目 | 5NJ8, 7ZUB, 8QMO |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=56.5），有序残基占 34.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039091, IPR033348, IPR011598, IPR036638, IPR001610; Pfam: PF00010, PF00989, PF08447 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| AIP | 0.999 | 0.986 | — |
| ARNT | 0.999 | 0.996 | — |
| HSP90AB1 | 0.995 | 0.927 | — |
| HSP90AA1 | 0.992 | 0.869 | — |
| CYP1A1 | 0.973 | 0.000 | — |
| ARNT2 | 0.940 | 0.692 | — |
| PTGES3 | 0.908 | 0.544 | — |
| ESR1 | 0.906 | 0.833 | — |
| ENSP00000490530 | 0.904 | 0.800 | — |
| CYP1A2 | 0.866 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=56.5 + PDB: 5NJ8, 7ZUB, 8QMO | pLDDT=56.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Cytosol; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. AHR — Aryl hydrocarbon receptor，研究基础较多，新颖性有限。
2. 蛋白大小848 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 6137 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=56.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 6137 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P35869
- Protein Atlas: https://www.proteinatlas.org/ENSG00000106546-AHR/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AHR
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P35869
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
