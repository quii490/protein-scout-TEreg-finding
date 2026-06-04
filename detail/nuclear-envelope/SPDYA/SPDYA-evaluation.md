---
type: protein-evaluation
gene: "SPDYA"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SPDYA 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SPDYA / SPDY1, SPY1 |
| 蛋白名称 | Speedy protein A |
| 蛋白大小 | 313 aa / 36.5 kDa |
| UniProt ID | Q5MJ70 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 313 aa / 36.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.3; PDB: 5UQ1, 5UQ2, 5UQ3, 7E34 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR020984, IPR052316; Pfam: PF11357 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **139.5/180** | |
| **归一化总分** | | | **77.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromosome, telomeric region (GO:0000781)
- nuclear envelope (GO:0005635)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- XY body (GO:0001741)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 60 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SPDY1, SPY1 |

**关键文献**:
1. Genomic variations associated with risk and protection against vincristine-induced peripheral neuropathy in pediatric cancer patients.. *NPJ genomic medicine*. PMID: 39500896
2. Analysis of differentially expressed microRNAs in bovine mammary epithelial cells treated with lipoteichoic acid.. *Journal of animal physiology and animal nutrition*. PMID: 35997417
3. Analysis and gonadal localization of Speedy A mRNA transcript, a novel gene associated with early germline cells in the scallop, Argopecten purpuratus.. *Animal reproduction science*. PMID: 34954527
4. Genomic heterogeneity of ALK fusion breakpoints in non-small-cell lung cancer.. *Modern pathology : an official journal of the United States and Canadian Academy of Pathology, Inc*. PMID: 29327716
5. Epigenetic basis of hepatocellular carcinoma: A network-based integrative meta-analysis.. *World journal of hepatology*. PMID: 29399289

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.3 |
| 高置信度残基 (pLDDT>90) 占比 | 39.6% |
| 置信残基 (pLDDT 70-90) 占比 | 11.8% |
| 中等置信 (pLDDT 50-70) 占比 | 10.5% |
| 低置信 (pLDDT<50) 占比 | 38.0% |
| 有序区域 (pLDDT>70) 占比 | 51.4% |
| 可用 PDB 条目 | 5UQ1, 5UQ2, 5UQ3, 7E34 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=68.3），有序残基占 51.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR020984, IPR052316; Pfam: PF11357 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CDK2 | 0.999 | 0.981 | — |
| CDKN1B | 0.983 | 0.961 | — |
| SUN1 | 0.958 | 0.900 | — |
| CDK1 | 0.949 | 0.000 | — |
| CDC25C | 0.900 | 0.000 | — |
| NFYB | 0.815 | 0.745 | — |
| NFYA | 0.808 | 0.745 | — |
| POLE3 | 0.805 | 0.743 | — |
| TERB2 | 0.760 | 0.000 | — |
| TERB1 | 0.733 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| AQP1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CDKN1B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CDK5 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CDK16 | psi-mi:"MI:0018"(two hybrid) | imex:IM-25032|pubmed:22184064 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 4
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 4 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.3 + PDB: 5UQ1, 5UQ2, 5UQ3, 7E34 | pLDDT=68.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 4 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. SPDYA — Speedy protein A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小313 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=68.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5MJ70
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163806-SPDYA/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SPDYA
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5MJ70
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
