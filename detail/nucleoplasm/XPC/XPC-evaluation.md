---
type: protein-evaluation
gene: "XPC"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## XPC — REJECTED (研究热度过高 (PubMed strict=1010，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | XPC / XPCC |
| 蛋白名称 | DNA repair protein complementing XP-C cells |
| 蛋白大小 | 940 aa / 106.0 kDa |
| UniProt ID | Q01831 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Plasma membrane; UniProt: Nucleus; Chromosome; Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 940 aa / 106.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1010 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.6; PDB: 2A4J, 2GGM, 2OBH, 2RVB, 8EBS, 8EBT, 8EBU |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR018327, IPR004583, IPR018026, IPR038765, IPR018 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **79.5/180** | |
| **归一化总分** | | | **44.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Plasma membrane | Enhanced |
| UniProt | Nucleus; Chromosome; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- mitochondrion (GO:0005739)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleotide-excision repair complex (GO:0000109)
- nucleotide-excision repair factor 2 complex (GO:0000111)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1010 |
| PubMed broad count | 1671 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: XPCC |

**关键文献**:
1. Generation and characterization of CRISPR-Cas9-mediated XPC gene knockout in human skin cells.. *Scientific reports*. PMID: 39730601
2. The moonlighting of RAD23 in DNA repair and protein degradation.. *Biochimica et biophysica acta. Gene regulatory mechanisms*. PMID: 36863450
3. BTG3-dependent VCP/p97 nuclear translocation is required for efficient repair of UV-induced DNA lesions.. *Nucleic acids research*. PMID: 40626560
4. Polymorphisms in XPC gene and risk for prostate cancer.. *Molecular biology reports*. PMID: 30552616
5. XPC as breast cancer susceptibility gene: evidence from genetic profiling, statistical inferences and protein structural analysis.. *Breast cancer (Tokyo, Japan)*. PMID: 32562189

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.6 |
| 高置信度残基 (pLDDT>90) 占比 | 39.1% |
| 置信残基 (pLDDT 70-90) 占比 | 15.2% |
| 中等置信 (pLDDT 50-70) 占比 | 4.0% |
| 低置信 (pLDDT<50) 占比 | 41.6% |
| 有序区域 (pLDDT>70) 占比 | 54.3% |
| 可用 PDB 条目 | 2A4J, 2GGM, 2OBH, 2RVB, 8EBS, 8EBT, 8EBU, 8EBV, 8EBW, 8EBX |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=66.6），有序残基占 54.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR018327, IPR004583, IPR018026, IPR038765, IPR018325; Pfam: PF10403, PF10404, PF10405 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CETN2 | 0.999 | 0.988 | — |
| RAD23B | 0.999 | 0.984 | — |
| RAD23A | 0.998 | 0.954 | — |
| ERCC1 | 0.994 | 0.000 | — |
| GTF2H1 | 0.992 | 0.948 | — |
| ERCC4 | 0.983 | 0.228 | — |
| DDB2 | 0.982 | 0.824 | — |
| XPA | 0.981 | 0.535 | — |
| XRCC6 | 0.979 | 0.729 | — |
| ERCC3 | 0.972 | 0.747 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CETN2 | psi-mi:"MI:0091"(chromatography technology) | pubmed:21962512|imex:IM-16583 |
| RAD23B | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:21962512|imex:IM-16583 |
| TSG101 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| Pou5f1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:21962512|imex:IM-16583 |
| katG | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| lysU | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| A0A0G2RM98 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ENSP00000285021.8 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| Q777D1 | psi-mi:"MI:0018"(two hybrid) | pubmed:18024891 |
| Sema1a | psi-mi:"MI:0963"(interactome parallel affinity cap | pubmed:21447707|imex:IM-17304 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.6 + PDB: 2A4J, 2GGM, 2OBH, 2RVB, 8EBS,  | pLDDT=66.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome; Cytoplasm / Nucleoplasm; 额外: Plasma membrane | 一致 |
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
1. XPC — DNA repair protein complementing XP-C cells，研究基础较多，新颖性有限。
2. 蛋白大小940 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 1010 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=66.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1010 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q01831
- Protein Atlas: https://www.proteinatlas.org/ENSG00000154767-XPC/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=XPC
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q01831
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
