---
type: protein-evaluation
gene: "DAGLA"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DAGLA — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DAGLA / C11orf11, KIAA0659, NSDDR |
| 蛋白名称 | Diacylglycerol lipase-alpha |
| 蛋白大小 | 1042 aa / 115.0 kDa |
| UniProt ID | Q9Y4D2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cell membrane; Postsynaptic density membrane; Early endosome |
| 蛋白大小 | 8/10 | x1 | 8 | 1042 aa / 115.0 kDa |
| 研究新颖性 | 6/10 | x5 | 30 | PubMed strict=44 篇 (≤60→6) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold v6 pLDDT=63.0; PDB: 无 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR029058, IPR052214, IPR002921; Pfam: PF01764 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **87.5/180** | |
| **归一化总分** | | | **48.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cell membrane; Postsynaptic density membrane; Early endosome membrane; Cell projection, dendritic sp... | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- dendrite membrane (GO:0032590)
- dendritic spine membrane (GO:0032591)
- early endosome membrane (GO:0031901)
- plasma membrane (GO:0005886)
- postsynaptic density membrane (GO:0098839)
- postsynaptic membrane (GO:0045211)
- varicosity (GO:0043196)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 44 |
| PubMed broad count | 178 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C11orf11, KIAA0659, NSDDR |

**关键文献**:
1. Diacylglycerol lipase alpha promotes tumorigenesis in oral cancer by cell-cycle progression.. *Experimental cell research*. PMID: 29614312
2. Identification of DAGLA as an autoantibody target in cerebellar ataxia.. *Journal of neurology, neurosurgery, and psychiatry*. PMID: 38663995
3. Endocannabinoid dysfunction in neurological disease: neuro-ocular DAGLA-related syndrome.. *Brain : a journal of neurology*. PMID: 35737950
4. Lipolytic gene DAGLA is targeted by miR-223 in chicken hepatocytes.. *Gene*. PMID: 32998047
5. Deciphering the interaction between N-palmitoyl-D-glucosamine and the endocannabinoidome.. *Scientific reports*. PMID: 40596256

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.0 |
| 高置信度残基 (pLDDT>90) 占比 | 25.2% |
| 置信残基 (pLDDT 70-90) 占比 | 25.2% |
| 中等置信 (pLDDT 50-70) 占比 | 11.0% |
| 低置信 (pLDDT<50) 占比 | 38.5% |
| 有序区域 (pLDDT>70) 占比 | 50.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=63.0），有序残基占 50.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029058, IPR052214, IPR002921; Pfam: PF01764 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DAGLB | 0.915 | 0.000 | — |
| FAAH | 0.898 | 0.000 | — |
| NAPEPLD | 0.894 | 0.000 | — |
| MGLL | 0.887 | 0.000 | — |
| ABHD6 | 0.831 | 0.000 | — |
| CNR1 | 0.817 | 0.000 | — |
| GRM5 | 0.811 | 0.000 | — |
| ABHD12 | 0.791 | 0.000 | — |
| ABHD4 | 0.714 | 0.000 | — |
| GPR55 | 0.700 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.0 + PDB: 无 | pLDDT=63.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane; Postsynaptic density membrane; Earl / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. DAGLA -- Diacylglycerol lipase-alpha，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小1042 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 44 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=63.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y4D2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000134780-DAGLA/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DAGLA
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y4D2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y4D2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
