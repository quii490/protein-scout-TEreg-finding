---
type: protein-evaluation
gene: "DFFB"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DFFB 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DFFB / CAD, DFF2, DFF40 |
| 蛋白名称 | DNA fragmentation factor subunit beta |
| 蛋白大小 | 338 aa / 39.1 kDa |
| UniProt ID | O76075 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli; 额外: Nucleoplasm; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 338 aa / 39.1 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=31 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=92.7; PDB: 1IBX |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR003508, IPR039729, IPR015311, IPR044925; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **129.0/180** | |
| **归一化总分** | | | **71.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; 额外: Nucleoplasm | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytosol (GO:0005829)
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
| PubMed strict count | 31 |
| PubMed broad count | 133 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CAD, DFF2, DFF40 |

**关键文献**:
1. Jagged Ends on Multinucleosomal Cell-Free DNA Serve as a Biomarker for Nuclease Activity and Systemic Lupus Erythematosus.. *Clinical chemistry*. PMID: 35587043
2. HNRNPCL1, PRAMEF1, CFAP74, and DFFB: Common Potential Biomarkers for Sporadic and Suspected Lynch Syndrome Endometrial Cancer.. *Cancer management and research*. PMID: 33177874
3. Attenuated expression of DFFB is a hallmark of oligodendrogliomas with 1p-allelic loss.. *Molecular cancer*. PMID: 16156899
4. Early gene expression profile in mouse brain after exposure to ionizing radiation.. *Radiation research*. PMID: 16435913
5. MEG3 Regulates CSE-Induced Apoptosis by Regulating miR-421/DFFB Signal Axis.. *International journal of chronic obstructive pulmonary disease*. PMID: 37215747

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.7 |
| 高置信度残基 (pLDDT>90) 占比 | 82.8% |
| 置信残基 (pLDDT 70-90) 占比 | 13.0% |
| 中等置信 (pLDDT 50-70) 占比 | 3.0% |
| 低置信 (pLDDT<50) 占比 | 1.2% |
| 有序区域 (pLDDT>70) 占比 | 95.8% |
| 可用 PDB 条目 | 1IBX |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=92.7，有序区 95.8%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003508, IPR039729, IPR015311, IPR044925; Pfam: PF02017, PF09230 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DFFA | 0.999 | 0.987 | — |
| CASP3 | 0.978 | 0.095 | — |
| CIDEB | 0.929 | 0.292 | — |
| H1-0 | 0.928 | 0.292 | — |
| ACIN1 | 0.875 | 0.000 | — |
| CIDEA | 0.875 | 0.244 | — |
| DNASE2 | 0.839 | 0.000 | — |
| H1-1 | 0.785 | 0.292 | — |
| H1-3 | 0.781 | 0.292 | — |
| H1-5 | 0.781 | 0.292 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DFFA | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| H1-3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:19882353|imex:IM-17244 |
| H1-5 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:19882353|imex:IM-17244 |
| H1-0 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:19882353|imex:IM-17244 |
| H1-1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:19882353|imex:IM-17244 |
| Vps28 | psi-mi:"MI:0096"(pull down) | imex:IM-26697|pubmed:14557248 |
| VIM | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| UBB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NEFH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PRKACB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.7 + PDB: 1IBX | pLDDT=92.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoli; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DFFB — DNA fragmentation factor subunit beta，非常新颖，仅有少数基础研究。
2. 蛋白大小338 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 31 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O76075
- Protein Atlas: https://www.proteinatlas.org/ENSG00000169598-DFFB/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DFFB
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O76075
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
