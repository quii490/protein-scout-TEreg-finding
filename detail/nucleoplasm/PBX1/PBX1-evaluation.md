---
type: protein-evaluation
gene: "PBX1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PBX1 — REJECTED (研究热度过高 (PubMed strict=761，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PBX1 / PRL |
| 蛋白名称 | Pre-B-cell leukemia transcription factor 1 |
| 蛋白大小 | 430 aa / 46.6 kDa |
| UniProt ID | P40424 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nuclear bodies, Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 430 aa / 46.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=761 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=69.2; PDB: 1B72, 1PUF |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001356, IPR017970, IPR009057, IPR008422, IPR005 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.5/180** | |
| **归一化总分** | | | **44.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear bodies, Cytosol | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- RNA polymerase II transcription regulator complex (GO:0090575)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 761 |
| PubMed broad count | 1238 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PRL |

**关键文献**:
1. Cicero Predicts cis-Regulatory DNA Interactions from Single-Cell Chromatin Accessibility Data.. *Molecular cell*. PMID: 30078726
2. Rheumatoid arthritis, systemic lupus erythematosus and primary Sjögren's syndrome shared megakaryocyte expansion in peripheral blood.. *Annals of the rheumatic diseases*. PMID: 34462261
3. Lactate programs PBX1 lactylation and mesangial proliferation in lupus nephritis.. *JCI insight*. PMID: 40299657
4. Integrated multi-omics approach revealed cellular senescence landscape.. *Nucleic acids research*. PMID: 36243980
5. TAT-PBX1 fusion protein alleviates LPS-induced acute lung injury via AMPK-TFAM signaling activation.. *Molecular therapy : the journal of the American Society of Gene Therapy*. PMID: 40926413

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.2 |
| 高置信度残基 (pLDDT>90) 占比 | 30.7% |
| 置信残基 (pLDDT 70-90) 占比 | 24.4% |
| 中等置信 (pLDDT 50-70) 占比 | 13.3% |
| 低置信 (pLDDT<50) 占比 | 31.6% |
| 有序区域 (pLDDT>70) 占比 | 55.1% |
| 可用 PDB 条目 | 1B72, 1PUF |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=69.2），有序残基占 55.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001356, IPR017970, IPR009057, IPR008422, IPR005542; Pfam: PF05920, PF03792 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PKNOX1 | 0.999 | 0.902 | — |
| MEIS1 | 0.999 | 0.898 | — |
| HOXB1 | 0.999 | 0.973 | — |
| HOXA9 | 0.998 | 0.945 | — |
| MEIS2 | 0.987 | 0.925 | — |
| TCF3 | 0.963 | 0.070 | — |
| D6RAR5_HUMAN | 0.931 | 0.926 | — |
| PDX1 | 0.928 | 0.458 | — |
| PKNOX2 | 0.917 | 0.785 | — |
| HOXB8 | 0.910 | 0.612 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HOXB1 | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:10052460 |
| Hoxa1 | psi-mi:"MI:0809"(bimolecular fluorescence compleme | imex:IM-15418|pubmed:23088713 |
| PKNOX1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-12050|pubmed:17623278 |
| MEIS1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-14346|pubmed:20541704 |
| MEIS2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| VWA5A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| C5orf24 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FAM222A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MAB21L2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MAB21L1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=69.2 + PDB: 1B72, 1PUF | pLDDT=69.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Nuclear bodies, Cytosol | 一致 |
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
1. PBX1 — Pre-B-cell leukemia transcription factor 1，研究基础较多，新颖性有限。
2. 蛋白大小430 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 761 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=69.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 761 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P40424
- Protein Atlas: https://www.proteinatlas.org/ENSG00000185630-PBX1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PBX1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P40424
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
