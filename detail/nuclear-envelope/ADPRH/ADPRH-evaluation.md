---
type: protein-evaluation
gene: "ADPRH"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ADPRH 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ADPRH / ARH1 |
| 蛋白名称 | ADP-ribosylhydrolase ARH1 |
| 蛋白大小 | 357 aa / 39.5 kDa |
| UniProt ID | P54922 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nuclear membrane; 额外: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 357 aa / 39.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=98.4; PDB: 3HFW, 6G28, 6G2A, 6IUX |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR012108, IPR050792, IPR005502, IPR036705; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 12 partners; IntAct 9 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **131.0/180** | |
| **归一化总分** | | | **72.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear membrane; 额外: Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- extracellular space (GO:0005615)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6 |
| PubMed broad count | 7 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ARH1 |

**关键文献**:
1. Enhanced sensitivity to cholera toxin in ADP-ribosylarginine hydrolase-deficient mice.. *Molecular and cellular biology*. PMID: 17526733
2. Genomic organization and promoter analysis of the mouse ADP-ribosylarginine hydrolase gene.. *Gene*. PMID: 15893437
3. Cloning, expression, purification and crystallization as well as X-ray fluorescence and preliminary X-ray diffraction analyses of human ADP-ribosylhydrolase 1.. *Acta crystallographica. Section F, Structural biology and crystallization communications*. PMID: 19407395
4. Signatures of Crested Ibis MHC Revealed by Recombination Screening and Short-Reads Assembly Strategy.. *PloS one*. PMID: 27997612
5. (ADP-ribosyl)hydrolases: Structural Basis for Differential Substrate Recognition and Inhibition.. *Cell chemical biology*. PMID: 30472116

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 98.4 |
| 高置信度残基 (pLDDT>90) 占比 | 99.4% |
| 置信残基 (pLDDT 70-90) 占比 | 0.6% |
| 中等置信 (pLDDT 50-70) 占比 | 0.0% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 100.0% |
| 可用 PDB 条目 | 3HFW, 6G28, 6G2A, 6IUX |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（3HFW, 6G28, 6G2A, 6IUX）+ AlphaFold高质量预测（pLDDT=98.4），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR012108, IPR050792, IPR005502, IPR036705; Pfam: PF03747 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ADPRHL2 | 0.668 | 0.000 | — |
| ART5 | 0.628 | 0.000 | — |
| MACROD2 | 0.533 | 0.000 | — |
| TRIM72 | 0.505 | 0.000 | — |
| ITGA7 | 0.476 | 0.000 | — |
| ART1 | 0.463 | 0.000 | — |
| MACROD1 | 0.457 | 0.000 | — |
| NECAP2 | 0.443 | 0.000 | — |
| OARD1 | 0.431 | 0.000 | — |
| CUL1 | 0.404 | 0.311 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SRPK1 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:23602568|imex:IM-17935 |
| SRPK2 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:23602568|imex:IM-17935 |
| SPSB1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| OBSL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| BCAT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| XRN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TFCP2 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-23318|pubmed:25416956 |
| ZNF286A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| COQ8A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 12，IntAct interactions: 9
- 调控相关比例: 0 / 12 = 0%

**评价**: STRING 12 个预测互作，IntAct 9 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=98.4 + PDB: 3HFW, 6G28, 6G2A, 6IUX | pLDDT=98.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nuclear membrane; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 12 + 9 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. ADPRH — ADP-ribosylhydrolase ARH1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小357 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P54922
- Protein Atlas: https://www.proteinatlas.org/ENSG00000144843-ADPRH/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ADPRH
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P54922
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
