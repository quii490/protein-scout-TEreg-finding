---
type: protein-evaluation
gene: "CRACR2A"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CRACR2A — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CRACR2A / EFCAB4B, RAB46 |
| 蛋白名称 | EF-hand calcium-binding domain-containing protein 4B |
| 蛋白大小 | 731 aa / 83.2 kDa |
| UniProt ID | Q9BSW2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm; Cytoplasm; Cytoplasm, cytoskeleton, microtubule o |
| 蛋白大小 | 10/10 | ×1 | 10 | 731 aa / 83.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=69.3; PDB: 6PSD |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011992, IPR018247, IPR002048, IPR027417, IPR050 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **110.5/180** | |
| **归一化总分** | | | **61.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm; Cytoplasm; Cytoplasm, cytoskeleton, microtubule organizing center; Cell membrane; Golgi a... | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- extracellular region (GO:0005576)
- Golgi membrane (GO:0000139)
- immunological synapse (GO:0001772)
- membrane (GO:0016020)
- microtubule organizing center (GO:0005815)
- plasma membrane (GO:0005886)
- specific granule lumen (GO:0035580)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 35 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: EFCAB4B, RAB46 |

**关键文献**:
1. Cracking CRAC.. *Nature cell biology*. PMID: 20442700
2. A large Rab GTPase family in a small GTPase world.. *Small GTPases*. PMID: 27221160
3. Molecular modulators of store-operated calcium entry.. *Biochimica et biophysica acta*. PMID: 27130253
4. CRACR2a is a calcium-activated dynein adaptor protein that regulates endocytic traffic.. *The Journal of cell biology*. PMID: 30814157
5. Gene mapping, gene-set analysis, and genomic prediction of postpartum blood calcium in Holstein cows.. *Journal of dairy science*. PMID: 34756434

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.3 |
| 高置信度残基 (pLDDT>90) 占比 | 35.0% |
| 置信残基 (pLDDT 70-90) 占比 | 25.0% |
| 中等置信 (pLDDT 50-70) 占比 | 7.8% |
| 低置信 (pLDDT<50) 占比 | 32.1% |
| 有序区域 (pLDDT>70) 占比 | 60.0% |
| 可用 PDB 条目 | 6PSD |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=69.3），有序残基占 60.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011992, IPR018247, IPR002048, IPR027417, IPR050227; Pfam: PF13499, PF00071 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| STIM1 | 0.944 | 0.292 | — |
| ORAI1 | 0.828 | 0.292 | — |
| DYNC1LI1 | 0.822 | 0.797 | — |
| SARAF | 0.755 | 0.054 | — |
| STIMATE | 0.701 | 0.055 | — |
| ORAI2 | 0.620 | 0.292 | — |
| EFHB | 0.618 | 0.000 | — |
| MCPH1 | 0.605 | 0.605 | — |
| ORAI3 | 0.598 | 0.292 | — |
| C11orf97 | 0.583 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TRIM29 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ATN1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| Hoxa1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15418|pubmed:23088713 |
| PLS1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MCPH1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CLUAP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ARMC3 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| TLE5 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| KRT75 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MID2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=69.3 + PDB: 6PSD | pLDDT=69.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm; Cytoplasm, cytoskeleton, mic / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CRACR2A — EF-hand calcium-binding domain-containing protein 4B，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小731 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=69.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BSW2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000130038-CRACR2A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CRACR2A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BSW2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
