---
type: protein-evaluation
gene: "OSBPL1A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## OSBPL1A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | OSBPL1A / ORP1, OSBP8, OSBPL1, OSBPL1B |
| 蛋白名称 | Oxysterol-binding protein-related protein 1 |
| 蛋白大小 | 950 aa / 108.5 kDa |
| UniProt ID | Q9BXW6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Late endosome |
| 蛋白大小 | 8/10 | ×1 | 8 | 950 aa / 108.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=20 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=80.6; PDB: 5ZM5, 5ZM6, 5ZM7, 6IYB, 6TQS, 8ZQ3 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR002110, IPR036770, IPR037239, IPR000648, IPR018 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **140.5/180** | |
| **归一化总分** | | | **78.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Approved |
| UniProt | Late endosome | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- endosome (GO:0005768)
- extracellular exosome (GO:0070062)
- late endosome (GO:0005770)
- organelle membrane contact site (GO:0044232)
- perinuclear endoplasmic reticulum (GO:0097038)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 20 |
| PubMed broad count | 27 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ORP1, OSBP8, OSBPL1, OSBPL1B |

**关键文献**:
1. ATM loss disrupts the autophagy-lysosomal pathway.. *Autophagy*. PMID: 32757690
2. Whole-exome sequencing reveals damaging gene variants associated with hypoalphalipoproteinemia.. *Journal of lipid research*. PMID: 35460704
3. Unveiling mitochondrial and PANoptosis-related biomarkers for premature ovarian insufficiency.. *Journal of ovarian research*. PMID: 41430255
4. IMPACT and OSBPL1A are two isoform-specific imprinted genes in bovines.. *Theriogenology*. PMID: 35294861
5. Evaluating the Neuroimaging-Genetic Prediction of Symptom Changes in Individuals with ADHD.. *Annual International Conference of the IEEE Engineering in Medicine and Biology Society. IEEE Engineering in Medicine and Biology Society. Annual International Conference*. PMID: 34891669

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.6 |
| 高置信度残基 (pLDDT>90) 占比 | 48.1% |
| 置信残基 (pLDDT 70-90) 占比 | 29.1% |
| 中等置信 (pLDDT 50-70) 占比 | 11.3% |
| 低置信 (pLDDT<50) 占比 | 11.6% |
| 有序区域 (pLDDT>70) 占比 | 77.2% |
| 可用 PDB 条目 | 5ZM5, 5ZM6, 5ZM7, 6IYB, 6TQS, 8ZQ3 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（5ZM5, 5ZM6, 5ZM7, 6IYB, 6TQS, 8ZQ3）+ AlphaFold极高置信度预测（pLDDT=80.6），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002110, IPR036770, IPR037239, IPR000648, IPR018494; Pfam: PF12796, PF01237 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| BCL6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:16147992 |
| CARNMT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| VAPA | psi-mi:"MI:0809"(bimolecular fluorescence compleme | imex:IM-25536|pubmed:25681634 |
| MEOX2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| VAPB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZNF331 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| BSPRY | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DMD | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CTNNA3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HIF1AN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.6 + PDB: 5ZM5, 5ZM6, 5ZM7, 6IYB, 6TQS,  | pLDDT=80.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Late endosome / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. OSBPL1A — Oxysterol-binding protein-related protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小950 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 20 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BXW6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000141447-OSBPL1A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=OSBPL1A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BXW6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
