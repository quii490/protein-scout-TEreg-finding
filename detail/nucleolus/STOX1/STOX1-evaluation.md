---
type: protein-evaluation
gene: "STOX1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## STOX1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | STOX1 / C10orf24 |
| 蛋白名称 | Storkhead-box protein 1 |
| 蛋白大小 | 989 aa / 111.0 kDa |
| UniProt ID | Q6ZVD7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nucleoli fibrillar center, Cytosol; UniProt: Cytoplasm; Nucleus; Cytoplasm, cytoskeleton, microtubule org |
| 蛋白大小 | 8/10 | ×1 | 8 | 989 aa / 111.0 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=53 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=48.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR019391, IPR040126; Pfam: PF10264 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 10 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **108.0/180** | |
| **归一化总分** | | | **60.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli fibrillar center, Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Nucleus; Nuc... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cell cortex (GO:0005938)
- centrosome (GO:0005813)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- fibrillar center (GO:0001650)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 53 |
| PubMed broad count | 79 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C10orf24 |

**关键文献**:
1. Identification of metabolism related biomarkers in obesity based on adipose bioinformatics and machine learning.. *Journal of translational medicine*. PMID: 39482740
2. Preeclampsia and STOX1 (storkhead-box protein 1): Molecular evaluation of STOX1 in preeclampsia.. *Gene*. PMID: 38969244
3. Antagonisation of Prokineticin Receptor-2 Attenuates Preeclampsia Symptoms.. *Journal of cellular and molecular medicine*. PMID: 39817714
4. Targeting STOX1 in the therapy of preeclampsia.. *Expert opinion on therapeutic targets*. PMID: 27782763
5. Genetic Approaches in Preeclampsia.. *Methods in molecular biology (Clifton, N.J.)*. PMID: 29196994

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 48.7 |
| 高置信度残基 (pLDDT>90) 占比 | 11.0% |
| 置信残基 (pLDDT 70-90) 占比 | 10.0% |
| 中等置信 (pLDDT 50-70) 占比 | 8.2% |
| 低置信 (pLDDT<50) 占比 | 70.8% |
| 有序区域 (pLDDT>70) 占比 | 21.0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=48.7），有序残基占 21.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019391, IPR040126; Pfam: PF10264 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| F5 | 0.672 | 0.000 | — |
| AGTR2 | 0.599 | 0.000 | — |
| EPHX1 | 0.594 | 0.000 | — |
| CCAR1 | 0.561 | 0.000 | — |
| GSTP1 | 0.555 | 0.000 | — |
| ACVR2A | 0.544 | 0.000 | — |
| MTHFR | 0.516 | 0.000 | — |
| DDX50 | 0.501 | 0.000 | — |
| AADACL2 | 0.491 | 0.000 | — |
| AGTR1 | 0.489 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GCLM | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| GORASP2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| ADARB1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| NFYC | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| BANP | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ROR2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| POU2F1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TPM2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DPP9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DNAL4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 10
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 10 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=48.7 + PDB: 无 | pLDDT=48.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Cytoplasm, cytoskeleton, micro / Nucleoplasm; 额外: Nucleoli fibrillar center, Cytoso | 一致 |
| PPI | STRING + IntAct | 15 + 10 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. STOX1 — Storkhead-box protein 1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小989 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 53 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=48.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6ZVD7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000165730-STOX1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=STOX1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6ZVD7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
