---
type: protein-evaluation
gene: "TFEB"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TFEB — REJECTED (研究热度过高 (PubMed strict=1529，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TFEB / BHLHE35 |
| 蛋白名称 | Transcription factor EB |
| 蛋白大小 | 476 aa / 52.9 kDa |
| UniProt ID | P19484 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Nucleus; Cytoplasm, cytosol; Lysosome membrane; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 476 aa / 52.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1529 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.2; PDB: 7UX2, 7UXC, 7UXH, 7Y62 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011598, IPR024098, IPR036638, IPR021802, IPR031 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm, cytosol; Lysosome membrane; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- lysosomal membrane (GO:0005765)
- nucleus (GO:0005634)
- transcription regulator complex (GO:0005667)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1529 |
| PubMed broad count | 2783 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BHLHE35 |

**关键文献**:
1. TFEB links autophagy to lysosomal biogenesis.. *Science (New York, N.Y.)*. PMID: 21617040
2. The cGAS-STING pathway activates transcription factor TFEB to stimulate lysosome biogenesis and pathogen clearance.. *Immunity*. PMID: 39689715
3. A gene network regulating lysosomal biogenesis and function.. *Science (New York, N.Y.)*. PMID: 19556463
4. Induction of lysosomal and mitochondrial biogenesis by AMPK phosphorylation of FNIP1.. *Science (New York, N.Y.)*. PMID: 37079666
5. Sustained alternate-day fasting potentiates doxorubicin cardiotoxicity.. *Cell metabolism*. PMID: 36868222

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.2 |
| 高置信度残基 (pLDDT>90) 占比 | 22.9% |
| 置信残基 (pLDDT 70-90) 占比 | 13.4% |
| 中等置信 (pLDDT 50-70) 占比 | 22.1% |
| 低置信 (pLDDT<50) 占比 | 41.6% |
| 有序区域 (pLDDT>70) 占比 | 36.3% |
| 可用 PDB 条目 | 7UX2, 7UXC, 7UXH, 7Y62 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=63.2），有序残基占 36.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011598, IPR024098, IPR036638, IPR021802, IPR031867; Pfam: PF11851, PF00010, PF15951 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MTOR | 0.983 | 0.901 | — |
| TFE3 | 0.979 | 0.831 | — |
| MITF | 0.976 | 0.808 | — |
| RRAGC | 0.972 | 0.902 | — |
| RRAGA | 0.970 | 0.900 | — |
| RPTOR | 0.959 | 0.901 | — |
| YWHAG | 0.940 | 0.933 | — |
| MLST8 | 0.897 | 0.811 | — |
| LAMTOR1 | 0.881 | 0.800 | — |
| LAMTOR2 | 0.868 | 0.800 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| A0A2P0HFX1 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| Pou5f1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:20362542|imex:IM-16970 |
| SRPK1 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:23602568|imex:IM-17935 |
| YWHAH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAZ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TFEC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TFE3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAG | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAE | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.2 + PDB: 7UX2, 7UXC, 7UXH, 7Y62 | pLDDT=63.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, cytosol; Lysosome membrane; Nu / Cytosol | 一致 |
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
1. TFEB — Transcription factor EB，研究基础较多，新颖性有限。
2. 蛋白大小476 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1529 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=63.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1529 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P19484
- Protein Atlas: https://www.proteinatlas.org/ENSG00000112561-TFEB/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TFEB
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P19484
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
