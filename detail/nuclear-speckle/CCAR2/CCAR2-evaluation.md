---
type: protein-evaluation
gene: "CCAR2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CCAR2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CCAR2 / DBC1, KIAA1967 |
| 蛋白名称 | Cell cycle and apoptosis regulator protein 2 |
| 蛋白大小 | 923 aa / 102.9 kDa |
| UniProt ID | Q8N163 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nuclear bodies; UniProt: Nucleus; Cytoplasm; Cytoplasm, cytoskeleton, spindle |
| 蛋白大小 | 8/10 | ×1 | 8 | 923 aa / 102.9 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=46 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.8; PDB: 8EZ6 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR025224, IPR025954, IPR011992, IPR045353, IPR025 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **108.5/180** | |
| **归一化总分** | | | **60.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear bodies | Enhanced |
| UniProt | Nucleus; Cytoplasm; Cytoplasm, cytoskeleton, spindle | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- DBIRD complex (GO:0044609)
- mitochondrial matrix (GO:0005759)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- spindle (GO:0005819)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 46 |
| PubMed broad count | 141 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DBC1, KIAA1967 |

**关键文献**:
1. Acetylation in the regulation of autophagy.. *Autophagy*. PMID: 35435793
2. The gut microbiota reprograms intestinal lipid metabolism through long noncoding RNA Snhg9.. *Science (New York, N.Y.)*. PMID: 37616368
3. Diagnostic Yield and Novel Candidate Genes by Exome Sequencing in 152 Consanguineous Families With Neurodevelopmental Disorders.. *JAMA psychiatry*. PMID: 28097321
4. CCAR1 and CCAR2 as gene chameleons with antagonistic duality: Preclinical, human translational, and mechanistic basis.. *Cancer science*. PMID: 33403784
5. CCAR2 controls mitotic progression through spatiotemporal regulation of Aurora B.. *Cell death & disease*. PMID: 35672287

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.8 |
| 高置信度残基 (pLDDT>90) 占比 | 35.9% |
| 置信残基 (pLDDT 70-90) 占比 | 19.1% |
| 中等置信 (pLDDT 50-70) 占比 | 7.4% |
| 低置信 (pLDDT<50) 占比 | 37.7% |
| 有序区域 (pLDDT>70) 占比 | 55.0% |
| 可用 PDB 条目 | 8EZ6 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=68.8），有序残基占 55.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR025224, IPR025954, IPR011992, IPR045353, IPR025223; Pfam: PF14443, PF19256, PF14444 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SIRT1 | 0.999 | 0.830 | — |
| HSPA8 | 0.996 | 0.994 | — |
| ZNF326 | 0.980 | 0.000 | — |
| RANBP3 | 0.925 | 0.000 | — |
| EDC4 | 0.851 | 0.000 | — |
| HAO1 | 0.835 | 0.835 | — |
| ATM | 0.823 | 0.000 | — |
| ATR | 0.789 | 0.000 | — |
| RNF40 | 0.784 | 0.000 | — |
| RPS19BP1 | 0.784 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MAP3K3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| NFKB2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| IKBKB | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| RELA | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| RELB | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| TAB2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| NFKBIB | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| TRADD | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| PNMA1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:14676191 |
| WRAP73 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.8 + PDB: 8EZ6 | pLDDT=68.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Cytoplasm, cytoskeleton, spind / Nucleoplasm, Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CCAR2 — Cell cycle and apoptosis regulator protein 2，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小923 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 46 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=68.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N163
- Protein Atlas: https://www.proteinatlas.org/ENSG00000158941-CCAR2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CCAR2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N163
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
