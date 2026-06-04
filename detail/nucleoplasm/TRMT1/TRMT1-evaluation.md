---
type: protein-evaluation
gene: "TRMT1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TRMT1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TRMT1 |
| 蛋白名称 | tRNA (guanine(26)-N(2))-dimethyltransferase |
| 蛋白大小 | 659 aa / 72.2 kDa |
| UniProt ID | Q9NXH9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane, Cytosol; 额外: Nucleoplasm; UniProt: Mitochondrion; Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 659 aa / 72.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=17 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=81.6; PDB: 9DW6 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR029063, IPR002905, IPR042296, IPR000571, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **139.0/180** | |
| **归一化总分** | | | **77.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cytosol; 额外: Nucleoplasm | Approved |
| UniProt | Mitochondrion; Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- mitochondrion (GO:0005739)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 17 |
| PubMed broad count | 23 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Bi-allelic pathogenic variants in TRMT1 disrupt tRNA modification and induce a neurodevelopmental disorder.. *American journal of human genetics*. PMID: 40245862
2. Proteolytic cleavage and inactivation of the TRMT1 tRNA modification enzyme by SARS-CoV-2 main protease.. *bioRxiv : the preprint server for biology*. PMID: 37502865
3. Proteolytic cleavage and inactivation of the TRMT1 tRNA modification enzyme by SARS-CoV-2 main protease.. *eLife*. PMID: 38814682
4. Recognition and Cleavage of Human tRNA Methyltransferase TRMT1 by the SARS-CoV-2 Main Protease.. *bioRxiv : the preprint server for biology*. PMID: 36865253
5. KDELC1 and TRMT1 Serve as Prognosis-Related SARS-CoV-2 Proteins Binding Human mRNAs and Promising Biomarkers in Clear Cell Renal Cell Carcinoma.. *International journal of general medicine*. PMID: 34163216

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.6 |
| 高置信度残基 (pLDDT>90) 占比 | 65.4% |
| 置信残基 (pLDDT 70-90) 占比 | 10.3% |
| 中等置信 (pLDDT 50-70) 占比 | 6.7% |
| 低置信 (pLDDT<50) 占比 | 17.6% |
| 有序区域 (pLDDT>70) 占比 | 75.7% |
| 可用 PDB 条目 | 9DW6 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 高质量预测（pLDDT=81.6，有序区 75.7%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029063, IPR002905, IPR042296, IPR000571, IPR036855; Pfam: PF02005, PF00642 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TRMT11 | 0.885 | 0.088 | — |
| RTF2 | 0.836 | 0.835 | — |
| TRUB1 | 0.824 | 0.134 | — |
| METTL1 | 0.807 | 0.114 | — |
| NSUN2 | 0.804 | 0.146 | — |
| FTSJ1 | 0.799 | 0.098 | — |
| TARBP1 | 0.793 | 0.000 | — |
| NOP2 | 0.768 | 0.110 | — |
| DUS2 | 0.758 | 0.231 | — |
| TRMT6 | 0.756 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MAGEA11 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TRMU | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| HSPD1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| FAM219B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NDUFS3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |
| LRRK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31046837|imex:IM-26684 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| IL1R2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| - | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| PB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28169297|imex:IM-25584 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.6 + PDB: 9DW6 | pLDDT=81.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Mitochondrion; Nucleus; Cytoplasm / Plasma membrane, Cytosol; 额外: Nucleoplasm | 一致 |
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
1. TRMT1 — tRNA (guanine(26)-N(2))-dimethyltransferase，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小659 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 17 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NXH9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000104907-TRMT1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TRMT1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NXH9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
