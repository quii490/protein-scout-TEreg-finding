---
type: protein-evaluation
gene: "TFE3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TFE3 — REJECTED (研究热度过高 (PubMed strict=1022，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TFE3 / BHLHE33 |
| 蛋白名称 | Transcription factor E3 |
| 蛋白大小 | 575 aa / 61.5 kDa |
| UniProt ID | P19532 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Cytoplasm, cytosol; Nucleus; Lysosome membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 575 aa / 61.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1022 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=58.6; PDB: 7F09 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011598, IPR024100, IPR036638, IPR021802, IPR031 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.5/180** | |
| **归一化总分** | | | **44.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Approved |
| UniProt | Cytoplasm, cytosol; Nucleus; Lysosome membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- lysosomal membrane (GO:0005765)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1022 |
| PubMed broad count | 1700 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BHLHE33 |

**关键文献**:
1. AMPK-dependent phosphorylation is required for transcriptional activation of TFEB and TFE3.. *Autophagy*. PMID: 33734022
2. Reprogramming tumour-associated macrophages to outcompete cancer cells.. *Nature*. PMID: 37380769
3. PEComa-its clinical features, histopathology, and current therapy.. *Japanese journal of clinical oncology*. PMID: 40336169
4. Inhibition of nonalcoholic fatty liver disease in mice by selective inhibition of mTORC1.. *Science (New York, N.Y.)*. PMID: 35420934
5. NUPR1 promotes the proliferation and metastasis of oral squamous cell carcinoma cells by activating TFE3-dependent autophagy.. *Signal transduction and targeted therapy*. PMID: 35462576

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 58.6 |
| 高置信度残基 (pLDDT>90) 占比 | 18.6% |
| 置信残基 (pLDDT 70-90) 占比 | 11.0% |
| 中等置信 (pLDDT 50-70) 占比 | 15.8% |
| 低置信 (pLDDT<50) 占比 | 54.6% |
| 有序区域 (pLDDT>70) 占比 | 29.6% |
| 可用 PDB 条目 | 7F09 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=58.6），有序残基占 29.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011598, IPR024100, IPR036638, IPR021802, IPR031867; Pfam: PF11851, PF00010, PF15951 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MITF | 0.996 | 0.832 | — |
| ASPSCR1 | 0.985 | 0.000 | — |
| TFEB | 0.979 | 0.831 | — |
| PRCC | 0.968 | 0.000 | — |
| E2F3 | 0.881 | 0.292 | — |
| SFPQ | 0.873 | 0.000 | — |
| TBC1D25 | 0.831 | 0.000 | — |
| CTSK | 0.813 | 0.000 | — |
| CLTC | 0.774 | 0.098 | — |
| SMAD3 | 0.760 | 0.510 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PHB2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| CUL2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| PFAS | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| GSTM3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| CACYBP | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ENSP00000518054.1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EIF3I | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| NAP1L1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| SMS | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| PSMA1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=58.6 + PDB: 7F09 | pLDDT=58.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol; Nucleus; Lysosome membrane / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. TFE3 — Transcription factor E3，研究基础较多，新颖性有限。
2. 蛋白大小575 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1022 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=58.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1022 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P19532
- Protein Atlas: https://www.proteinatlas.org/ENSG00000068323-TFE3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TFE3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P19532
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
