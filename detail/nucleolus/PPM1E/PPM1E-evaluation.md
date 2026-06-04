---
type: protein-evaluation
gene: "PPM1E"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PPM1E 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PPM1E / CAMKN, KIAA1072, POPX1 |
| 蛋白名称 | Protein phosphatase 1E |
| 蛋白大小 | 755 aa / 84.0 kDa |
| UniProt ID | Q8WY54 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli; 额外: Nucleoplasm; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 755 aa / 84.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=34 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR015655, IPR000222, IPR036457, IPR001932; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.0/180** | |
| **归一化总分** | | | **66.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; 额外: Nucleoplasm | Approved |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- protein-containing complex (GO:0032991)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 34 |
| PubMed broad count | 48 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CAMKN, KIAA1072, POPX1 |

**关键文献**:
1. Metal-dependent Ser/Thr protein phosphatase PPM family: Evolution, structures, diseases and inhibitors.. *Pharmacology & therapeutics*. PMID: 32650009
2. Functions and dysfunctions of Ca(2+)/calmodulin-dependent protein kinase phosphatase (CaMKP/PPM1F) and CaMKP-N/PPM1E.. *Archives of biochemistry and biophysics*. PMID: 29317228
3. Reduced Expression Level of Protein Phosphatase PPM1E Serves to Maintain Insulin Secretion in Type 2 Diabetes.. *Diabetes*. PMID: 36662636
4. Transcriptomic analysis of transformed small-cell lung cancer from EGFR-mutated lung adenocarcinoma reveals distinct subgroups and precision therapy opportunities.. *Biomarker research*. PMID: 40437627
5. The DACH1 Gene Transcriptional Activation and Protein Degradation Mediated by Transactivator Tas of Prototype Foamy Virus.. *Viruses*. PMID: 37766305

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.5 |
| 高置信度残基 (pLDDT>90) 占比 | 41.7% |
| 置信残基 (pLDDT 70-90) 占比 | 6.6% |
| 中等置信 (pLDDT 50-70) 占比 | 3.4% |
| 低置信 (pLDDT<50) 占比 | 48.2% |
| 有序区域 (pLDDT>70) 占比 | 48.3% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=64.5），有序残基占 48.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR015655, IPR000222, IPR036457, IPR001932; Pfam: PF00481 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CAMK4 | 0.814 | 0.072 | — |
| CALM1 | 0.775 | 0.126 | — |
| ARHGEF6 | 0.561 | 0.045 | — |
| ARAP1 | 0.556 | 0.000 | — |
| TEX14 | 0.457 | 0.000 | — |
| ARHGEF7 | 0.455 | 0.294 | — |
| PRKAA2 | 0.452 | 0.414 | — |
| PRKAA1 | 0.439 | 0.414 | — |
| PRMT2 | 0.436 | 0.433 | — |
| IQSEC3 | 0.436 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DISC1 | psi-mi:"MI:0018"(two hybrid) | pubmed:17043677|imex:IM-16650 |
| TNIK | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| PPM1M | psi-mi:"MI:0434"(phosphatase assay) | pubmed:31663853|imex:IM-27498 |
| PRMT2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ICMT | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NDUFAF5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SERPINB4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| BRCA2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PSME3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TRO | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.5 + PDB: 无 | pLDDT=64.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoli; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PPM1E — Protein phosphatase 1E，非常新颖，仅有少数基础研究。
2. 蛋白大小755 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 34 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=64.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WY54
- Protein Atlas: https://www.proteinatlas.org/ENSG00000175175-PPM1E/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PPM1E
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WY54
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
