---
type: protein-evaluation
gene: "DGKA"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DGKA 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DGKA / DAGK, DAGK1 |
| 蛋白名称 | Diacylglycerol kinase alpha |
| 蛋白大小 | 735 aa / 82.6 kDa |
| UniProt ID | P23743 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Vesicles; 额外: Nucleoplasm, Mitochondria; UniProt: Cytoplasm, cytosol |
| 蛋白大小 | 10/10 | x1 | 10 | 735 aa / 82.6 kDa |
| 研究新颖性 | 4/10 | x5 | 20 | PubMed strict=75 篇 (≤80→4) |
| 三维结构 | 9/10 | x3 | 27 | AlphaFold v6 pLDDT=82.5; PDB: 1TUZ, 6IIE |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR017438, IPR046349, IPR047469, IPR029477, IPR037 |
| PPI 网络 | 2/10 | x3 | 6 | STRING 0 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.5/180** | |
| **归一化总分** | | | **53.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Nucleoplasm, Mitochondria | Approved |
| UniProt | Cytoplasm, cytosol | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA检测到可靠IF图像信号。

**GO Cellular Component**:
- cytosol (GO:0005829)
- membrane (GO:0016020)
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 75 |
| PubMed broad count | 112 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DAGK, DAGK1 |

**关键文献**:
1. Multiomics analysis reveals metabolic subtypes and identifies diacylglycerol kinase α (DGKA) as a potential therapeutic target for intrahepatic cholangiocarcinoma.. *Cancer communications (London, England)*. PMID: 38143235
2. DGKA interacts with SRC/FAK to promote the metastasis of non-small cell lung cancer.. *Cancer letters*. PMID: 35131384
3. ILDR2 has a negligible role in hepatic steatosis.. *PloS one*. PMID: 29847571
4. BET-bromodomain inhibitors modulate epigenetic patterns at the diacylglycerol kinase alpha enhancer associated with radiation-induced fibrosis.. *Radiotherapy and oncology : journal of the European Society for Therapeutic Radiology and Oncology*. PMID: 28916223
5. Decreased LIPF expression is correlated with DGKA and predicts poor outcome of gastric cancer.. *Oncology reports*. PMID: 27498782

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.5 |
| 高置信度残基 (pLDDT>90) 占比 | 45.0% |
| 置信残基 (pLDDT 70-90) 占比 | 37.1% |
| 中等置信 (pLDDT 50-70) 占比 | 10.1% |
| 低置信 (pLDDT<50) 占比 | 7.8% |
| 有序区域 (pLDDT>70) 占比 | 82.1% |
| 可用 PDB 条目 | 1TUZ, 6IIE |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构 + AlphaFold高质量（pLDDT=82.5），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR017438, IPR046349, IPR047469, IPR029477, IPR037607; Pfam: PF00130, PF14513, PF00609 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 无PPI数据
- STRING partners: 0，IntAct interactions: 0
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.5 + PDB: 1TUZ, 6IIE | pLDDT=82.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol / Vesicles; 额外: Nucleoplasm, Mitochondria | 一致 |
| PPI | STRING + IntAct | 0 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DGKA -- Diacylglycerol kinase alpha，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小735 aa，大小适中（200-800 aa），适合常规生化实验。

**风险/不确定性**:
1. PubMed 75 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P23743
- Protein Atlas: https://www.proteinatlas.org/ENSG00000065357-DGKA/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DGKA
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P23743
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P23743-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
