---
type: protein-evaluation
gene: "NHSL1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation, recovery, re-evaluation]
status: scored
---

## NHSL1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NHSL1 / C6orf63, KIAA1357 |
| 蛋白名称 | NHS-like protein 1 |
| 蛋白大小 | 1610 aa / 170.7 kDa |
| UniProt ID | Q5SYE7 |
| 数据采集时间 | 2026-06-03 23:44:11 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Nuclear membrane; 额外: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 5/10 | x1 | 5 | 1610 aa / 170.7 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=15 篇 (<= 20 -> 10) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold v6 pLDDT=41.5; PDB: 无 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR024845; Pfam: PF15273 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 10 partners; IntAct 15 interactions |
| 互证加分 | -- | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **112.5/180** | |
| **归一化总分** | | | **62.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear membrane; 额外: Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed broad count | 19 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C6orf63, KIAA1357 |

**关键文献**:
1. Proteogenomics Integrating Novel Junction Peptide Identification Strategy Discovers Three Novel Protein Isoforms of Human NHSL1 and EEF1B2.. *Journal of proteome research*. PMID: 34420305
2. Identification of the gene for Nance-Horan syndrome (NHS).. *Journal of medical genetics*. PMID: 15466011
3. Nance-Horan Syndrome-like 1 protein negatively regulates Scar/WAVE-Arp2/3 activity and inhibits lamellipodia stability and cell migration.. *Nature communications*. PMID: 34584076
4. PPP2R1A regulates migration persistence through the NHSL1-containing WAVE Shell Complex.. *Nature communications*. PMID: 37322026
5. Integrative genomic analysis of salivary duct carcinoma.. *Scientific reports*. PMID: 32929114

**评价**: 极度新颖，几乎未被系统研究（PubMed <= 20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 41.5 |
| 高置信度残基 (pLDDT>90) 占比 | 1.6% |
| 置信残基 (pLDDT 70-90) 占比 | 4.2% |
| 中等置信 (pLDDT 50-70) 占比 | 6.9% |
| 低置信 (pLDDT<50) 占比 | 87.3% |
| 有序区域 (pLDDT>70) 占比 | 5.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。**

**评价**: AlphaFold 预测质量有限（pLDDT=41.5），有序残基占 5.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR024845; Pfam: PF15273 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ABI2 | 0.736 | 0.687 | — |
| NCKAP1 | 0.699 | 0.678 | — |
| NCK2 | 0.649 | 0.608 | — |
| WASF1 | 0.622 | 0.562 | — |
| AMZ1 | 0.613 | 0.613 | — |
| KIAA1522 | 0.585 | 0.378 | — |
| WASF2 | 0.551 | 0.465 | — |
| BRK1 | 0.452 | 0.225 | — |
| PFN1 | 0.440 | 0.440 | — |
| NCK1 | 0.420 | 0.421 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| YWHAH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| AMZ1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ABI1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| NCK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ABI2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Gtf2e2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| SEC16A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| JUP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| SETX | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| STUB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 10，IntAct interactions: 15
- 调控相关比例: 0 / 10 = 0%

**评价**: STRING 10 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=41.5 + PDB: 无 | pLDDT=41.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nuclear membrane; 额外: Nucleoplasm | 待确认 |
| PPI | STRING + IntAct | 10 + 15 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0 (仅1源)
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ 

**核心优势**:
1. NHSL1 -- NHS-like protein 1，极度新颖，几乎未被系统研究（PubMed <= 20篇）。
2. 蛋白大小1610 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 15 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=41.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5SYE7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000135540-NHSL1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NHSL1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5SYE7
- STRING: https://string-db.org/network/9606.NHSL1
- Packet data timestamp: 2026-06-03 23:44:11

---
*本报告为全量重评估 (Full Re-evaluation) -- Recovery from false-rejection。所有评分基于最新harvest packet数据，使用标准/180评分体系计算。*
