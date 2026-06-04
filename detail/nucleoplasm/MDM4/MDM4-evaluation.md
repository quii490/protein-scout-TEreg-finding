---
type: protein-evaluation
gene: "MDM4"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## MDM4 — REJECTED (研究热度过高 (PubMed strict=477，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MDM4 / MDMX |
| 蛋白名称 | Protein Mdm4 |
| 蛋白大小 | 490 aa / 54.9 kDa |
| UniProt ID | O15151 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 490 aa / 54.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=477 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.1; PDB: 2CR8, 2MWY, 2N06, 2N0U, 2N0W, 2N14, 2VJE |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR051652, IPR015458, IPR016495, IPR036885, IPR003 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- transcription repressor complex (GO:0017053)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 477 |
| PubMed broad count | 971 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MDMX |

**关键文献**:
1. Comprehensive and Integrative Genomic Characterization of Hepatocellular Carcinoma.. *Cell*. PMID: 28622513
2. MDM4 inhibits ferroptosis in p53 mutant colon cancer via regulating TRIM21/GPX4 expression.. *Cell death & disease*. PMID: 39543140
3. Genomic and Transcriptomic Analyses of Breast Cancer Primaries and Matched Metastases in AURORA, the Breast International Group (BIG) Molecular Screening Initiative.. *Cancer discovery*. PMID: 34183353
4. MDM4 alternative splicing and implication in MDM4 targeted cancer therapies.. *American journal of cancer research*. PMID: 35018230
5. Uncovering immune cell-associated genes in breast cancer: based on summary data-based Mendelian randomized analysis and colocalization study.. *Breast cancer research : BCR*. PMID: 39614330

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.1 |
| 高置信度残基 (pLDDT>90) 占比 | 26.9% |
| 置信残基 (pLDDT 70-90) 占比 | 7.6% |
| 中等置信 (pLDDT 50-70) 占比 | 11.6% |
| 低置信 (pLDDT<50) 占比 | 53.9% |
| 有序区域 (pLDDT>70) 占比 | 34.5% |
| 可用 PDB 条目 | 2CR8, 2MWY, 2N06, 2N0U, 2N0W, 2N14, 2VJE, 2VJF, 2VYR, 3DAB |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=60.1），有序残基占 34.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051652, IPR015458, IPR016495, IPR036885, IPR003121; Pfam: PF13920, PF00641 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MDM2 | 0.999 | 0.999 | — |
| TP53 | 0.999 | 0.999 | — |
| SFN | 0.977 | 0.948 | — |
| USP7 | 0.973 | 0.790 | — |
| CSNK1A1 | 0.971 | 0.883 | — |
| RPS27A | 0.970 | 0.929 | — |
| UBC | 0.967 | 0.929 | — |
| CDKN2A | 0.963 | 0.441 | — |
| UBB | 0.959 | 0.905 | — |
| ATM | 0.954 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MDM2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| sigA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| - | psi-mi:"MI:0084"(phage display) | pubmed:17875722 |
| EBI-28988565 | psi-mi:"MI:0084"(phage display) | pubmed:17875722 |
| TP53 | psi-mi:"MI:0411"(enzyme linked immunosorbent assay | pubmed:17875722 |
| UBE2D2 | psi-mi:"MI:0071"(molecular sieving) | pubmed:20705607|imex:IM-17029 |
| UBA1 | psi-mi:"MI:0997"(ubiquitinase assay) | pubmed:20705607|imex:IM-17029 |
| RPS27A | psi-mi:"MI:0997"(ubiquitinase assay) | pubmed:20705607|imex:IM-17029 |
| Ywhae | psi-mi:"MI:0096"(pull down) | imex:IM-13598|pubmed:19573810 |
| MKRN3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15696|pubmed:22493164 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.1 + PDB: 2CR8, 2MWY, 2N06, 2N0U, 2N0W,  | pLDDT=60.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. MDM4 — Protein Mdm4，研究基础较多，新颖性有限。
2. 蛋白大小490 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 477 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=60.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 477 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O15151
- Protein Atlas: https://www.proteinatlas.org/ENSG00000198625-MDM4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MDM4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O15151
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
