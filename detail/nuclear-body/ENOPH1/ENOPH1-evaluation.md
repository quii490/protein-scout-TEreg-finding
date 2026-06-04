---
type: protein-evaluation
gene: "ENOPH1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ENOPH1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ENOPH1 / MASA |
| 蛋白名称 | Enolase-phosphatase E1 |
| 蛋白大小 | 261 aa / 28.9 kDa |
| UniProt ID | Q9UHY7 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-body/ENOPH1/IF_images/Hep-G2_1.jpg|Hep-G2]]
![[Projects/TEreg-finding/protein-interested/detail/nuclear-body/ENOPH1/IF_images/NIH-3T3_1.jpg|NIH 3T3]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nucleoli, Nuclear bodies; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 261 aa / 28.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=17 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=95.4; PDB: 1YNS, 1ZS9 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR023943, IPR027511, IPR036412, IPR006439, IPR023 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **142.0/180** | |
| **归一化总分** | | | **78.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli, Nuclear bodies | Approved |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 17 |
| PubMed broad count | 22 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MASA |

**关键文献**:
1. 4q21.2q21.3 Duplication: Molecular and Neuropsychological Aspects.. *Current genomics*. PMID: 29606904
2. Integration of metabolomics and expression of enolase-phosphatase 1 links to hepatocellular carcinoma progression.. *Theranostics*. PMID: 31281503
3. Evidence that enolase-phosphatase 1 exacerbates early cerebral ischemia injury and blood-brain barrier breakdown by enhancing extracellular matrix destruction and inhibiting the interaction between ADI1 and MT1-MMP.. *Experimental neurology*. PMID: 37075968
4. Mapping multitissue regulatory variants reveals a liver-centric coexpression network associated with duck egg-laying performance.. *Genome research*. PMID: 40930983
5. Enolase-phosphatase 1 as a novel potential malignant glioma indicator promotes cell proliferation and migration.. *Oncology reports*. PMID: 30066900

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 95.4 |
| 高置信度残基 (pLDDT>90) 占比 | 93.1% |
| 置信残基 (pLDDT 70-90) 占比 | 4.6% |
| 中等置信 (pLDDT 50-70) 占比 | 1.9% |
| 低置信 (pLDDT<50) 占比 | 0.4% |
| 有序区域 (pLDDT>70) 占比 | 97.7% |
| 可用 PDB 条目 | 1YNS, 1ZS9 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-body/ENOPH1/ENOPH1-PAE.png]]

**评价**: PDB实验结构（1YNS, 1ZS9）+ AlphaFold高质量预测（pLDDT=95.4），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR023943, IPR027511, IPR036412, IPR006439, IPR023214; Pfam: PF00702 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| APIP | 0.999 | 0.000 | — |
| ADI1 | 0.997 | 0.000 | — |
| MRI1 | 0.975 | 0.000 | — |
| CSTF3 | 0.760 | 0.000 | — |
| RNF41 | 0.746 | 0.746 | — |
| ADD3 | 0.721 | 0.000 | — |
| ADD2 | 0.719 | 0.000 | — |
| ADD1 | 0.719 | 0.000 | — |
| THEM4 | 0.711 | 0.595 | — |
| SMS | 0.657 | 0.453 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RPS27 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| THEM4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| VPS52 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CARD9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RNF41 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ERBB3 | psi-mi:"MI:0112"(ubiquitin reconstruction) | pubmed:31980649|imex:IM-26434 |
| ZNF280A | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| BAG6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| TMEM63B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Syce2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=95.4 + PDB: 1YNS, 1ZS9 | pLDDT=95.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm; 额外: Nucleoli, Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. ENOPH1 — Enolase-phosphatase E1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小261 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 17 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UHY7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000145293-ENOPH1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ENOPH1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UHY7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-body/ENOPH1/ENOPH1-PAE.png]]




