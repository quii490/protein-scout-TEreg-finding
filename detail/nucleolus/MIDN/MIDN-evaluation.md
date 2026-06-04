---
type: protein-evaluation
gene: "MIDN"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MIDN 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MIDN |
| 蛋白名称 | Midnolin |
| 蛋白大小 | 468 aa / 49.2 kDa |
| UniProt ID | Q504T8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus, nucleolus; Nucleus; Cytoplasm, cytosol |
| 蛋白大小 | 10/10 | ×1 | 10 | 468 aa / 49.2 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=25 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.0; PDB: 9NKG, 9NKI |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039336, IPR000626, IPR029071; Pfam: PF00240 |
| PPI 网络 | 8/10 | ×3 | 24 | STRING 8 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **135.5/180** | |
| **归一化总分** | | | **75.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus, nucleolus; Nucleus; Cytoplasm, cytosol | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleolus (GO:0005730)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 25 |
| PubMed broad count | 53 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Structural insights into the ubiquitin-independent midnolin-proteasome pathway.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 40339123
2. Viable mutations of mouse midnolin suppress B cell malignancies.. *The Journal of experimental medicine*. PMID: 38625151
3. Midnolin, a Genetic Risk Factor for Parkinson's Disease, Promotes Neurite Outgrowth Accompanied by Early Growth Response 1 Activation in PC12 Cells.. *Molecular and cellular biology*. PMID: 39264361
4. Midnolin is a novel regulator of parkin expression and is associated with Parkinson's Disease.. *Scientific reports*. PMID: 28724963
5. Molecular Function of Midnolin and Its Relevance to Parkinson's Disease.. *Molecular and cellular biology*. PMID: 40693841

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.0 |
| 高置信度残基 (pLDDT>90) 占比 | 28.0% |
| 置信残基 (pLDDT 70-90) 占比 | 15.6% |
| 中等置信 (pLDDT 50-70) 占比 | 13.0% |
| 低置信 (pLDDT<50) 占比 | 43.4% |
| 有序区域 (pLDDT>70) 占比 | 43.6% |
| 可用 PDB 条目 | 9NKG, 9NKI |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=65.0），有序残基占 43.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039336, IPR000626, IPR029071; Pfam: PF00240 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PSMC1 | 0.547 | 0.547 | — |
| CSRNP1 | 0.542 | 0.000 | — |
| EGR1 | 0.507 | 0.445 | — |
| SBNO2 | 0.492 | 0.000 | — |
| SERTAD1 | 0.478 | 0.000 | — |
| NR4A1 | 0.438 | 0.409 | — |
| UBL7 | 0.434 | 0.000 | — |
| PSMC2 | 0.405 | 0.405 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SYNGR3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CMTM4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PLEKHF2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| NR4A1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| EGR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ERCC6L | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KRT34 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| PSMC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| TNNC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| KCTD17 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 8，IntAct interactions: 15
- 调控相关比例: 2 / 8 = 25%

**评价**: STRING 8 个预测互作，IntAct 15 个实验互作。调控相关配体占比 25%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.0 + PDB: 9NKG, 9NKI | pLDDT=65.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus, nucleolus; Nucleus; Cytoplasm, cytosol / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 8 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. MIDN — Midnolin，非常新颖，仅有少数基础研究。
2. 蛋白大小468 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 25 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=65.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q504T8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000167470-MIDN/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MIDN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q504T8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
