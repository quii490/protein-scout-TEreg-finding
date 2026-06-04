---
type: protein-evaluation
gene: "BLCAP"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BLCAP 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BLCAP / BC10 |
| 蛋白名称 | Apoptosis inducing factor BLCAP |
| 蛋白大小 | 87 aa / 9.9 kDa |
| UniProt ID | P62952 |
| 评估日期 | 2026-06-03 |
| 数据采集时间 | 2026-06-03 03:38:24 |

**IF 图像**:
![](https://images.proteinatlas.org/47390/1582_H7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/47390/1582_H7_2_blue_red_green.jpg)

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | x4 | 36 | HPA: Nucleoli; UniProt: Cytoplasm, Nu... |
| 蛋白大小 | 4/10 | x1 | 4 | 87 aa / 9.9 kDa |
| 研究新颖性 | 6/10 | x5 | 30 | PubMed strict=44 篇 (41-60->6) |
| 三维结构 | 5/10 | x3 | 15 | AlphaFold v6 pLDDT=62.7 |
| 调控结构域 | 5/10 | x2 | 10 | InterPro: 1; Pfam: 1; IPR009598 |
| PPI 网络 | 10/10 | x3 | 30 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | -- | max +3 | 1.5 | 多库定位一致 (3源): +0.5; STRING + IntAct 双源验证: +0.5; 结构域 + AlphaFold 质量: +0.5 |
| **原始总分** | | | **126.5/180** | |
| **归一化总分 (/1.83)** | | | **69.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; 额外: Nucleoli | Approved |
| UniProt | Cytoplasm, Nucleus, Membrane | Swiss-Prot/TrEMBL |

**IF 图像说明**: 原图已通过HPA检索获取，见上方嵌入图像。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- membrane (GO:0016020)
- nucleus (GO:0005634)

**结论**: 核定位证据充分，多个数据源一致支持核定位，定位特异性高。

#### 3.2 蛋白大小评估

**评价**: 87 aa，蛋白较小，但仍在可操作范围。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 44 |
| PubMed broad count | 66 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BC10 |

**关键文献**:
1. Identification and characterization of ADAR1 mutations and changes in gene expression in human cancers.. *Cancer genetics*. PMID: 39488870
2. BLCAP arrests G₁/S checkpoint and induces apoptosis through downregulation of pRb1 in HeLa cells.. *Oncology reports*. PMID: 26986503
3. A-to-I RNA editing of BLCAP promotes cell proliferation by losing the inhibitory of Rb1 in colorectal cancer.. *Experimental cell research*. PMID: 35605649
4. Bladder cancer-associated protein is suppressed in human cervical tumors.. *Experimental and therapeutic medicine*. PMID: 22969892
5. Human BLCAP transcript: new editing events in normal and cancerous tissues.. *International journal of cancer*. PMID: 19908260

**评价**: 中等新颖性，有一定研究基础但仍有探索空间（PubMed 41-60篇）。新颖性评分 6/10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.7 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 34.5% |
| 中等置信 (pLDDT 50-70) 占比 | 46.0% |
| 低置信 (pLDDT<50) 占比 | 19.5% |
| 有序区域 (pLDDT>70) 占比 | 34.5% |

**PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。**

**评价**: AlphaFold中等质量预测（pLDDT=62.7），存在部分低置信区域。三维结构评分 5/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009598; Pfam: PF06726 |

**染色质调控潜力分析**: 存在 2 个已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score > 0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NNAT | 0.968 | 0.000 | -- |
| CYFIP2 | 0.684 | 0.000 | -- |
| COG3 | 0.638 | 0.000 | -- |
| AZIN1 | 0.630 | 0.000 | -- |
| ADAR | 0.583 | 0.000 | -- |
| GRB10 | 0.578 | 0.000 | -- |
| CSNK2A1 | 0.550 | 0.000 | -- |
| RBBP9 | 0.532 | 0.000 | -- |
| HERC3 | 0.520 | 0.000 | -- |
| HERC3-2 | 0.520 | 0.000 | -- |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NOTCH2NLA | two hybrid array | imex:IM-27438|doi:10.1038/s41467-019-11959-3|pubmed:31515488 |
| CYSRT1 | two hybrid array | pubmed:32296183|imex:IM-25472 |
| MFSD5 | two hybrid prey pooling approach | pubmed:32296183|imex:IM-25472 |
| GOSR2 | two hybrid prey pooling approach | pubmed:32296183|imex:IM-25472 |
| CLDND2 | validated two hybrid | pubmed:32296183|imex:IM-25472 |
| FAM241B | two hybrid array | pubmed:32296183|imex:IM-25472 |
| SSMEM1 | two hybrid array | pubmed:32296183|imex:IM-25472 |
| HOXA1 | validated two hybrid | pubmed:32296183|imex:IM-25472 |
| - | validated two hybrid | pubmed:32296183|imex:IM-25472 |
| SKAP1 | validated two hybrid | imex:IM-23318|pubmed:25416956 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15

**评价**: 互作网络丰富：STRING 15 预测 + IntAct 15 实验互作。PPI 评分 10/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold v6 | pLDDT=62.7 | 单一来源 |
| 定位 | UniProt + HPA | Nucleoli / Nucleus | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
**总分**: +1.5 / max +3

### 4. 总体评价

**归一化总分**: 69.1/100

**核心优势**:
1. 存在 2 个已知结构域，有明确的结构-功能切入点。
2. 核定位信号明确，多个数据源一致支持。

**风险/不确定性**:
1. 暂无PDB实验结构，结构证据完全依赖AlphaFold预测
2. 蛋白过小（87 aa），实验操作受限

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] 考虑通过AlphaFold预测 + MD模拟获取结构信息

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/P62952
- Protein Atlas: https://www.proteinatlas.org/search/BLCAP
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BLCAP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P62952
- STRING: https://string-db.org/network/9606.BLCAP
- Packet data timestamp: 2026-06-03 03:38:24
