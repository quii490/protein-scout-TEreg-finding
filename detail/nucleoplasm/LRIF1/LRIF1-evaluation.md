---
type: protein-evaluation
gene: "LRIF1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LRIF1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LRIF1 / C1orf103, RIF1 |
| 蛋白名称 | Ligand-dependent nuclear receptor-interacting factor 1 |
| 蛋白大小 | 769 aa / 84.6 kDa |
| UniProt ID | Q5T3J3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Centriolar satellite; UniProt: Chromosome; Nucleus matrix |
| 蛋白大小 | 10/10 | ×1 | 10 | 769 aa / 84.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=14 篇 (≤20→10) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v6 pLDDT=0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026191; Pfam: PF15741 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **132.0/180** | |
| **归一化总分** | | | **73.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Centriolar satellite | Supported |
| UniProt | Chromosome; Nucleus matrix | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- Barr body (GO:0001740)
- centriolar satellite (GO:0034451)
- nuclear matrix (GO:0016363)
- nucleoplasm (GO:0005654)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 14 |
| PubMed broad count | 22 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C1orf103, RIF1 |

**关键文献**:
1. Facioscapulohumeral Muscular Dystrophy.. **. PMID: 20301616
2. A discrete region of the D4Z4 is sufficient to initiate epigenetic silencing.. *Human molecular genetics*. PMID: 40627547
3. SMCHD1 and LRIF1 converge at the FSHD-associated D4Z4 repeat and LRIF1 promoter yet display different modes of action.. *Communications biology*. PMID: 37380887
4. LRIF1 interacts with HP1α to coordinate accurate chromosome segregation during mitosis.. *Journal of molecular cell biology*. PMID: 30016453
5. Homozygous nonsense variant in LRIF1 associated with facioscapulohumeral muscular dystrophy.. *Neurology*. PMID: 32467133

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026191; Pfam: PF15741 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SMCHD1 | 0.966 | 0.434 | — |
| CBX3 | 0.807 | 0.702 | — |
| CBX5 | 0.739 | 0.678 | — |
| DUX4 | 0.622 | 0.000 | — |
| CBX1 | 0.613 | 0.555 | — |
| TRAK2 | 0.530 | 0.000 | — |
| SDAD1 | 0.510 | 0.000 | — |
| LZIC | 0.489 | 0.000 | — |
| RRP15 | 0.481 | 0.000 | — |
| C17orf80 | 0.480 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NOC2L | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| GPRASP2 | psi-mi:"MI:0096"(pull down) | pubmed:15383276|mint:MINT-5217 |
| GIT1 | psi-mi:"MI:0096"(pull down) | pubmed:15383276|mint:MINT-5217 |
| CEP126 | psi-mi:"MI:0018"(two hybrid) | pubmed:15383276|mint:MINT-5217 |
| BARD1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15383276|mint:MINT-5217 |
| FEZ1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15383276|mint:MINT-5217 |
| GADD45G | psi-mi:"MI:0018"(two hybrid) | pubmed:15383276|mint:MINT-5217 |
| Hap1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15383276|mint:MINT-5217 |
| KAT7 | psi-mi:"MI:0018"(two hybrid) | pubmed:15383276|mint:MINT-5217 |
| IMMT | psi-mi:"MI:0018"(two hybrid) | pubmed:15383276|mint:MINT-5217 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Chromosome; Nucleus matrix / Nucleoplasm; 额外: Centriolar satellite | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. LRIF1 — Ligand-dependent nuclear receptor-interacting factor 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小769 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 14 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5T3J3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000121931-LRIF1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LRIF1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5T3J3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000121931-LRIF1/subcellular

![](https://images.proteinatlas.org/44515/1177_H1_2_red_green.jpg)
![](https://images.proteinatlas.org/44515/1177_H1_3_red_green.jpg)
![](https://images.proteinatlas.org/44515/2269_G12_138_red_green.jpg)
![](https://images.proteinatlas.org/44515/2269_G12_63_red_green.jpg)
![](https://images.proteinatlas.org/44515/498_G7_1_red_green.jpg)
![](https://images.proteinatlas.org/44515/498_G7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5T3J3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
