---
type: protein-evaluation
gene: "CENPA"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CENPA — REJECTED (研究热度过高 (PubMed strict=768，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CENPA |
| 蛋白名称 | Histone H3-like centromeric protein A |
| 蛋白大小 | 140 aa / 16.0 kDa |
| UniProt ID | P49450 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Chromosome, centromere |
| 蛋白大小 | 8/10 | ×1 | 8 | 140 aa / 16.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=768 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=81.5; PDB: 3AN2, 3NQJ, 3NQU, 3R45, 3WTP, 5CVD, 5Z23 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR007125, IPR009072, IPR000164; Pfam: PF00125 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus; Chromosome, centromere | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- CENP-A containing nucleosome (GO:0043505)
- chromosome, centromeric region (GO:0000775)
- condensed chromosome, centromeric region (GO:0000779)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleosome (GO:0000786)
- nucleus (GO:0005634)
- pericentric heterochromatin (GO:0005721)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 768 |
| PubMed broad count | 1371 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. CENPA functions as a transcriptional regulator to promote hepatocellular carcinoma progression via cooperating with YY1.. *International journal of biological sciences*. PMID: 37928273
2. CENPA and BRCA1 are potential biomarkers associated with immune infiltration in heart failure and pan-cancer.. *Heliyon*. PMID: 38576566
3. EWSR1 maintains centromere identity.. *Cell reports*. PMID: 37243594
4. CENPA promotes glutamine metabolism and tumor progression by up-regulating SLC38A1 in endometrial cancer.. *Cellular signalling*. PMID: 38382691
5. Post-translational Modifications of Centromeric Chromatin.. *Progress in molecular and subcellular biology*. PMID: 28840239

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.5 |
| 高置信度残基 (pLDDT>90) 占比 | 60.0% |
| 置信残基 (pLDDT 70-90) 占比 | 5.7% |
| 中等置信 (pLDDT 50-70) 占比 | 30.0% |
| 低置信 (pLDDT<50) 占比 | 4.3% |
| 有序区域 (pLDDT>70) 占比 | 65.7% |
| 可用 PDB 条目 | 3AN2, 3NQJ, 3NQU, 3R45, 3WTP, 5CVD, 5Z23, 6BUZ, 6C0W, 6E0C |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（3AN2, 3NQJ, 3NQU, 3R45, 3WTP, 5CVD, 5Z23, 6BUZ, 6C0W, 6E0C）+ AlphaFold极高置信度预测（pLDDT=81.5），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007125, IPR009072, IPR000164; Pfam: PF00125 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CENPN | 0.999 | 0.955 | — |
| CENPI | 0.999 | 0.881 | — |
| CENPC | 0.999 | 0.952 | — |
| HJURP | 0.999 | 0.990 | — |
| CENPM | 0.999 | 0.897 | — |
| CENPH | 0.999 | 0.903 | — |
| H4C6 | 0.999 | 0.988 | — |
| H2AC18 | 0.998 | 0.917 | — |
| CENPU | 0.998 | 0.915 | — |
| CENPT | 0.997 | 0.931 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| STH1 | psi-mi:"MI:0018"(two hybrid) | pubmed:12697820|imex:IM-19866 |
| UBC7 | psi-mi:"MI:0397"(two hybrid array) | pubmed:14690591 |
| CSE4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21884933|imex:IM-16572 |
| FYN | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| cnp1 | psi-mi:"MI:0416"(fluorescence microscopy) | pubmed:11909965|imex:IM-18892 |
| ABL1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| CENPT | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12152|pubmed:19070575 |
| centoromere protein C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12152|pubmed:19070575 |
| NPM1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12180|pubmed:19410545 |
| HJURP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12180|pubmed:19410545 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.5 + PDB: 3AN2, 3NQJ, 3NQU, 3R45, 3WTP,  | pLDDT=81.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome, centromere / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CENPA — Histone H3-like centromeric protein A，研究基础较多，新颖性有限。
2. 蛋白大小140 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 768 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 768 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P49450
- Protein Atlas: https://www.proteinatlas.org/ENSG00000115163-CENPA/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CENPA
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P49450
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
