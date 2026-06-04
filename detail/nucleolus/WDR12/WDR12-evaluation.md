---
type: protein-evaluation
gene: "WDR12"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## WDR12 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | WDR12 |
| 蛋白名称 | Ribosome biogenesis protein WDR12 |
| 蛋白大小 | 423 aa / 47.7 kDa |
| UniProt ID | Q9GZL7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane, Cytosol; 额外: Nucleoli; UniProt: Nucleus, nucleolus; Nucleus, nucleoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 423 aa / 47.7 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=47 篇 (≤60→6) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=89.1; PDB: 6N31, 6P0Q, 8FKY |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR012972, IPR015943, IPR020472, IPR019775, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.0/180** | |
| **归一化总分** | | | **68.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cytosol; 额外: Nucleoli | Approved |
| UniProt | Nucleus, nucleolus; Nucleus, nucleoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- PeBoW complex (GO:0070545)
- preribosome, large subunit precursor (GO:0030687)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 47 |
| PubMed broad count | 60 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Genetic etiological spectrum of sperm morphological abnormalities.. *Journal of assisted reproduction and genetics*. PMID: 39417902
2. circMIRIAF aggravates myocardial ischemia-reperfusion injury via targeting miR-544/WDR12 axis.. *Redox biology*. PMID: 38795544
3. Roles of WDR12 and MRTO4 genes in colorectal cancer.. *Medicine*. PMID: 39969382
4. Wdr12, a mouse gene encoding a novel WD-Repeat Protein with a notchless-like amino-terminal domain.. *Genomics*. PMID: 11827460
5. WDR12/RAC1 axis promoted proliferation and anti-apoptosis in colorectal cancer cells.. *Molecular and cellular biochemistry*. PMID: 38341833

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.1 |
| 高置信度残基 (pLDDT>90) 占比 | 69.7% |
| 置信残基 (pLDDT 70-90) 占比 | 22.7% |
| 中等置信 (pLDDT 50-70) 占比 | 1.9% |
| 低置信 (pLDDT<50) 占比 | 5.7% |
| 有序区域 (pLDDT>70) 占比 | 92.4% |
| 可用 PDB 条目 | 6N31, 6P0Q, 8FKY |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（6N31, 6P0Q, 8FKY）+ AlphaFold高质量预测（pLDDT=89.1），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR012972, IPR015943, IPR020472, IPR019775, IPR036322; Pfam: PF08154, PF00400 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NIP7 | 0.999 | 0.942 | — |
| PES1 | 0.999 | 0.992 | — |
| BOP1 | 0.999 | 0.992 | — |
| RSL24D1 | 0.998 | 0.933 | — |
| WDR74 | 0.998 | 0.941 | — |
| BRIX1 | 0.998 | 0.952 | — |
| NIFK | 0.998 | 0.960 | — |
| EBNA1BP2 | 0.998 | 0.949 | — |
| MAK16 | 0.998 | 0.935 | — |
| RSL1D1 | 0.998 | 0.951 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| BOP1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:16043514|imex:IM-20399 |
| PES1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:16043514|imex:IM-20399 |
| RPS6 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| RRP1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-26310|pubmed:20926688 |
| LRRK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31046837|imex:IM-26684 |
| TMCO5A | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| IGHMBP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NIFK | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| WDR55 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.1 + PDB: 6N31, 6P0Q, 8FKY | pLDDT=89.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus, nucleolus; Nucleus, nucleoplasm / Plasma membrane, Cytosol; 额外: Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. WDR12 — Ribosome biogenesis protein WDR12，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小423 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 47 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9GZL7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000138442-WDR12/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=WDR12
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9GZL7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
