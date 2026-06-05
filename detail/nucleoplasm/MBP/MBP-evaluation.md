---
type: protein-evaluation
gene: "MBP"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## MBP — REJECTED (研究热度过高 (PubMed strict=11589，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MBP |
| 蛋白名称 | Myelin basic protein |
| 蛋白大小 | 304 aa / 33.1 kDa |
| UniProt ID | P02686 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane; UniProt: Myelin membrane; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 304 aa / 33.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=11589 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=54.1; PDB: 1BX2, 1FV1, 1HQR, 1K2D, 1YMM, 1ZGL |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000548; Pfam: PF01669 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane | Approved |
| UniProt | Myelin membrane; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cell periphery (GO:0071944)
- cell surface (GO:0009986)
- compact myelin (GO:0043218)
- cytosol (GO:0005829)
- internode region of axon (GO:0033269)
- myelin sheath (GO:0043209)
- neuronal cell body (GO:0043025)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11589 |
| PubMed broad count | 18106 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Physiology, Major Basic Protein.. **. PMID: 33085271
2. Molecular Identification and Sequencing of Mannose Binding Protein (MBP) Gene of Acanthamoeba palestinensis.. *Iranian journal of parasitology*. PMID: 22347229
3. The Biological Significance and Regulatory Mechanism of c-Myc Binding Protein 1 (MBP-1).. *International journal of molecular sciences*. PMID: 30518090
4. Posttranscriptional regulation of myelin protein gene expression.. *Annals of the New York Academy of Sciences*. PMID: 1724125
5. The evolution of Olig genes and their roles in myelination.. *Neuron glia biology*. PMID: 19737433

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 54.1 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 7.9% |
| 中等置信 (pLDDT 50-70) 占比 | 51.3% |
| 低置信 (pLDDT<50) 占比 | 40.8% |
| 有序区域 (pLDDT>70) 占比 | 7.9% |
| 可用 PDB 条目 | 1BX2, 1FV1, 1HQR, 1K2D, 1YMM, 1ZGL |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=54.1），有序残基占 7.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000548; Pfam: PF01669 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MAG | 0.989 | 0.000 | — |
| PLP1 | 0.988 | 0.512 | — |
| CALM3 | 0.988 | 0.453 | — |
| CALML4 | 0.987 | 0.070 | — |
| CALML3 | 0.987 | 0.091 | — |
| CALML6 | 0.987 | 0.070 | — |
| CALML5 | 0.987 | 0.091 | — |
| MOG | 0.955 | 0.000 | — |
| MAPK1 | 0.953 | 0.920 | — |
| SOX10 | 0.933 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PRG2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| Hpca | psi-mi:"MI:0096"(pull down) | pubmed:16470652|imex:IM-11839 |
| APP | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:16049941|imex:IM-20090 |
| APTX | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| ATN1 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| ATXN1 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| SOST | psi-mi:"MI:0096"(pull down) | pubmed:22206666|imex:IM-17213 |
| Ywhaz | psi-mi:"MI:0028"(cosedimentation in solution) | imex:IM-11648|pubmed:19562802 |
| PID | psi-mi:"MI:0423"(in-gel kinase assay) | pubmed:12857841 |
| Kcnma1 | psi-mi:"MI:0096"(pull down) | imex:IM-11875|pubmed:17610306 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=54.1 + PDB: 1BX2, 1FV1, 1HQR, 1K2D, 1YMM,  | pLDDT=54.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Myelin membrane; Nucleus / Plasma membrane | 一致 |
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
1. MBP — Myelin basic protein，研究基础较多，新颖性有限。
2. 蛋白大小304 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 11589 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=54.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 11589 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P02686
- Protein Atlas: https://www.proteinatlas.org/ENSG00000197971-MBP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MBP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P02686
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P02686-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
