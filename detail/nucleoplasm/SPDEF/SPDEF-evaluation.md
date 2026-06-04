---
type: protein-evaluation
gene: "SPDEF"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SPDEF — REJECTED (研究热度过高 (PubMed strict=149，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SPDEF / PDEF, PSE |
| 蛋白名称 | SAM pointed domain-containing Ets transcription factor |
| 蛋白大小 | 335 aa / 37.5 kDa |
| UniProt ID | O95238 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Nucleoli, Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 335 aa / 37.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=149 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=69.0; PDB: 1YO5, 2DKX |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000418, IPR046328, IPR003118, IPR013761, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.5/180** | |
| **归一化总分** | | | **49.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli, Cytosol | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 149 |
| PubMed broad count | 312 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PDEF, PSE |

**关键文献**:
1. Identification of spatially-resolved markers of malignant transformation in Intraductal Papillary Mucinous Neoplasms.. *Nature communications*. PMID: 38553466
2. Goblet cell differentiation subgroups in colorectal cancer.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 39401352
3. SPDEF ameliorates UUO-induced renal fibrosis by transcriptional activation of NR4A1.. *Molecular medicine (Cambridge, Mass.)*. PMID: 39736520
4. Regulation of SPDEF expression by DNA methylation in advanced prostate cancer.. *Frontiers in endocrinology*. PMID: 37900138
5. ZBTB46, SPDEF, and ETV6: Novel Potential Biomarkers and Therapeutic Targets in Castration-Resistant Prostate Cancer.. *International journal of molecular sciences*. PMID: 31181727

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.0 |
| 高置信度残基 (pLDDT>90) 占比 | 46.9% |
| 置信残基 (pLDDT 70-90) 占比 | 9.6% |
| 中等置信 (pLDDT 50-70) 占比 | 3.3% |
| 低置信 (pLDDT<50) 占比 | 40.3% |
| 有序区域 (pLDDT>70) 占比 | 56.5% |
| 可用 PDB 条目 | 1YO5, 2DKX |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=69.0），有序残基占 56.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000418, IPR046328, IPR003118, IPR013761, IPR036388; Pfam: PF00178, PF02198 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NKX3-1 | 0.880 | 0.475 | — |
| NKX2-1 | 0.858 | 0.094 | — |
| C5orf30 | 0.793 | 0.793 | — |
| STAT6 | 0.786 | 0.000 | — |
| AGR2 | 0.784 | 0.000 | — |
| AR | 0.728 | 0.292 | — |
| FOXA1 | 0.709 | 0.000 | — |
| MUC5AC | 0.697 | 0.000 | — |
| IL13 | 0.693 | 0.000 | — |
| UNC119 | 0.657 | 0.657 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| IMMP2L | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| STX16 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| CEP57 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TTC23 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| KDM5B | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:24937458|imex:IM-22991 |
| SNX20 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| FAM161B | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ENKD1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| COX5A | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SLC4A2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=69.0 + PDB: 1YO5, 2DKX | pLDDT=69.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Nucleoli, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. SPDEF — SAM pointed domain-containing Ets transcription factor，研究基础较多，新颖性有限。
2. 蛋白大小335 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 149 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=69.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 149 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O95238
- Protein Atlas: https://www.proteinatlas.org/ENSG00000124664-SPDEF/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SPDEF
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O95238
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
