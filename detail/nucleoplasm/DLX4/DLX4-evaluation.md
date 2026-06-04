---
type: protein-evaluation
gene: "DLX4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DLX4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DLX4 / BP1, DLX7, DLX8, DLX9 |
| 蛋白名称 | Homeobox protein DLX-4 |
| 蛋白大小 | 240 aa / 26.3 kDa |
| UniProt ID | Q92988 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 240 aa / 26.3 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=86 篇 (≤100→2) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR050460, IPR001356, IPR020479, IPR017970, IPR009 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 8 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **98.0/180** | |
| **归一化总分** | | | **54.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 86 |
| PubMed broad count | 145 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BP1, DLX7, DLX8, DLX9 |

**关键文献**:
1. DLX4 upregulates TWIST and enhances tumor migration, invasion and metastasis.. *International journal of biological sciences*. PMID: 23091415
2. Homeodomain protein DLX4 facilitates nasopharyngeal carcinoma progression via up-regulation of YB-1.. *Genes to cells : devoted to molecular & cellular mechanisms*. PMID: 32281175
3. Knockdown of DLK4 inhibits non-small cell lung cancer tumor growth by downregulating CKS2.. *Open life sciences*. PMID: 37744456
4. The homeobox gene DLX4 regulates erythro-megakaryocytic differentiation by stimulating IL-1β and NF-κB signaling.. *Journal of cell science*. PMID: 26208636
5. Identification and validation of DLX4 as a prognostic and diagnostic biomarker for clear cell renal cell carcinoma.. *Oncology letters*. PMID: 36936018

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.6 |
| 高置信度残基 (pLDDT>90) 占比 | 24.2% |
| 置信残基 (pLDDT 70-90) 占比 | 5.4% |
| 中等置信 (pLDDT 50-70) 占比 | 45.8% |
| 低置信 (pLDDT<50) 占比 | 24.6% |
| 有序区域 (pLDDT>70) 占比 | 29.6% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=65.6），有序残基占 29.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050460, IPR001356, IPR020479, IPR017970, IPR009057; Pfam: PF00046 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BARX1 | 0.498 | 0.076 | — |
| XRCC5 | 0.459 | 0.000 | — |
| XRCC6 | 0.444 | 0.000 | — |
| HOPX | 0.427 | 0.045 | — |
| PAX8 | 0.427 | 0.000 | — |
| POU1F1 | 0.408 | 0.059 | — |
| PAX2 | 0.407 | 0.000 | — |
| PAX4 | 0.406 | 0.071 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NCK1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| LSM3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| CRK | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| SRC | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| FYN | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| GRB2 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| Maged1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:11084035|imex:IM-20068 |
| ABL1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| PIK3R1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| PLCG1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 8，IntAct interactions: 15
- 调控相关比例: 0 / 8 = 0%

**评价**: STRING 8 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.6 + PDB: 无 | pLDDT=65.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 8 + 15 interactions | 数据充分 |

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
1. DLX4 — Homeobox protein DLX-4，研究基础较多，新颖性有限。
2. 蛋白大小240 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 86 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=65.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q92988
- Protein Atlas: https://www.proteinatlas.org/ENSG00000108813-DLX4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DLX4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q92988
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
