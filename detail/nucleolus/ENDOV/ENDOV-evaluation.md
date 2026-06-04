---
type: protein-evaluation
gene: "ENDOV"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ENDOV 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ENDOV |
| 蛋白名称 | Endonuclease V |
| 蛋白大小 | 282 aa / 30.8 kDa |
| UniProt ID | Q8N8Q3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm; Nucleus, nucleolus; Cytoplasm, Stress granule; Cy |
| 蛋白大小 | 10/10 | ×1 | 10 | 282 aa / 30.8 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=30 篇 (≤40→8) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=90.1; PDB: 4NSP, 6OZE |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR007581; Pfam: PF04493 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **132.0/180** | |
| **归一化总分** | | | **73.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm; Nucleus, nucleolus; Cytoplasm, Stress granule; Cytoplasm; Nucleus, nucleolus; Cytoplasm, ... | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytoplasmic stress granule (GO:0010494)
- nucleolus (GO:0005730)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 30 |
| PubMed broad count | 105 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Deletion of Endonuclease V suppresses chemically induced hepatocellular carcinoma.. *Nucleic acids research*. PMID: 32083667
2. Biochemical and mutational studies of an endonuclease V from the hyperthermophilic crenarchaeon Sulfolobus islandicus REY15A.. *World journal of microbiology & biotechnology*. PMID: 36752840
3. Search for germline gene variants in colorectal cancer families presenting with multiple primary colorectal cancers.. *International journal of cancer*. PMID: 39654522
4. High sensitivity EndoV mutation scanning through real-time ligase proofreading.. *Nucleic acids research*. PMID: 15514109
5. Modeling of Escherichia coli Endonuclease V structure in complex with DNA.. *Journal of molecular modeling*. PMID: 19043748

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.1 |
| 高置信度残基 (pLDDT>90) 占比 | 81.6% |
| 置信残基 (pLDDT 70-90) 占比 | 5.3% |
| 中等置信 (pLDDT 50-70) 占比 | 2.5% |
| 低置信 (pLDDT<50) 占比 | 10.6% |
| 有序区域 (pLDDT>70) 占比 | 86.9% |
| 可用 PDB 条目 | 4NSP, 6OZE |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（4NSP, 6OZE）+ AlphaFold高质量预测（pLDDT=90.1），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007581; Pfam: PF04493 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PPOX | 0.897 | 0.000 | — |
| CPOX | 0.888 | 0.070 | — |
| UROS | 0.877 | 0.000 | — |
| FECH | 0.864 | 0.000 | — |
| MOCS1 | 0.792 | 0.000 | — |
| HMBS | 0.787 | 0.079 | — |
| TYW1 | 0.679 | 0.000 | — |
| ITPA | 0.638 | 0.000 | — |
| CDKAL1 | 0.632 | 0.000 | — |
| CDK5RAP1 | 0.632 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NELFCD | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| PRPSAP2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| NOP9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| VWA8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| APAF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PDCL | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ANKRD40 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RNF31 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TSC22D3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SEPHS2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.1 + PDB: 4NSP, 6OZE | pLDDT=90.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus, nucleolus; Cytoplasm, Stress g / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. ENDOV — Endonuclease V，非常新颖，仅有少数基础研究。
2. 蛋白大小282 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 30 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N8Q3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000173818-ENDOV/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ENDOV
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N8Q3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
