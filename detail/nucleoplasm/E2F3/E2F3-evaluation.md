---
type: protein-evaluation
gene: "E2F3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## E2F3 — REJECTED (研究热度过高 (PubMed strict=560，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | E2F3 / KIAA0075 |
| 蛋白名称 | Transcription factor E2F3 |
| 蛋白大小 | 465 aa / 49.2 kDa |
| UniProt ID | O00716 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 465 aa / 49.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=560 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR015633, IPR037241, IPR032198, IPR003316, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.0/180** | |
| **归一化总分** | | | **44.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- RNA polymerase II transcription regulator complex (GO:0090575)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 560 |
| PubMed broad count | 874 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0075 |

**关键文献**:
1. Identifying the E2F3-MEX3A-KLF4 signaling axis that sustains cancer cells in undifferentiated and proliferative state.. *Theranostics*. PMID: 36276637
2. TACC3 enhances glycolysis in bladder cancer cells through inducing acetylation of c-Myc.. *Cell death & disease*. PMID: 40246827
3. Systematic identification of single transcription factor perturbations that drive cellular and tissue rejuvenation.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 41512022
4. ELF1-mediated transactivation of METTL3/YTHDF2 promotes nucleus pulposus cell senescence via m6A-dependent destabilization of E2F3 mRNA in intervertebral disc degeneration.. *Cell death discovery*. PMID: 40467575
5. Nanos genes and their role in development and beyond.. *Cellular and molecular life sciences : CMLS*. PMID: 29397397

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.5 |
| 高置信度残基 (pLDDT>90) 占比 | 22.8% |
| 置信残基 (pLDDT 70-90) 占比 | 13.5% |
| 中等置信 (pLDDT 50-70) 占比 | 13.5% |
| 低置信 (pLDDT<50) 占比 | 50.1% |
| 有序区域 (pLDDT>70) 占比 | 36.3% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=59.5），有序残基占 36.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR015633, IPR037241, IPR032198, IPR003316, IPR036388; Pfam: PF16421, PF02319 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RB1 | 0.998 | 0.900 | — |
| TFDP1 | 0.996 | 0.843 | — |
| RBL1 | 0.985 | 0.801 | — |
| RBL2 | 0.984 | 0.493 | — |
| E2F1 | 0.979 | 0.599 | — |
| TFDP2 | 0.976 | 0.687 | — |
| CDK2 | 0.973 | 0.091 | — |
| CCNA2 | 0.965 | 0.146 | — |
| E2F2 | 0.962 | 0.329 | — |
| CCNA1 | 0.957 | 0.146 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| BCL6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:16147992 |
| E7 | psi-mi:"MI:0096"(pull down) | imex:IM-14542|pubmed:16249186| |
| E2FA | psi-mi:"MI:0413"(electrophoretic mobility shift as | pubmed:11891240|imex:IM-20317 |
| DPB | psi-mi:"MI:0018"(two hybrid) | pubmed:11891240|imex:IM-20317 |
| Sp1 | psi-mi:"MI:0096"(pull down) | pubmed:8657141|imex:IM-19612 |
| DPA | psi-mi:"MI:0018"(two hybrid) | pubmed:11108847|imex:IM-19806 |
| RB1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-13586|pubmed:19249677 |
| MSH2 | psi-mi:"MI:0813"(proximity ligation assay) | pubmed:25241761|imex:IM-18707 |
| RBR1 | psi-mi:"MI:0809"(bimolecular fluorescence compleme | imex:IM-17903|pubmed:22921914 |
| EBI-5277760 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | imex:IM-26335|pubmed:20040599 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.5 + PDB: 无 | pLDDT=59.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. E2F3 — Transcription factor E2F3，研究基础较多，新颖性有限。
2. 蛋白大小465 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 560 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=59.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 560 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O00716
- Protein Atlas: https://www.proteinatlas.org/ENSG00000112242-E2F3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=E2F3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O00716
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
