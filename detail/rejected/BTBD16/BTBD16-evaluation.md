---
type: protein-evaluation
gene: "BTBD16"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## BTBD16 — REJECTED (核定位证据不足 (核定位得分 3/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BTBD16 / C10orf87 |
| 蛋白名称 | BTB/POZ domain-containing protein 16 |
| 蛋白大小 | 506 aa / 58.5 kDa |
| UniProt ID | Q32M84 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 3/10 | ×4 | 12 | HPA: 暂无HPA定位数据; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 506 aa / 58.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=8 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=78.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR056426, IPR042833, IPR048859, IPR011333; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 7 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **117.0/180** | |
| **归一化总分** | | | **65.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无数据 |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据不足，HPA与UniProt存在矛盾或缺乏核注释。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8 |
| PubMed broad count | 10 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C10orf87 |

**关键文献**:
1. Shared genetics and causal relationships between migraine and thyroid function traits.. *Cephalalgia : an international journal of headache*. PMID: 36739509
2. Exploring the shared genetic architecture of type 2 diabetes mellitus and bone mineral density.. *Archives of osteoporosis*. PMID: 40549202
3. Brain-wide genome-wide colocalization study for integrating genetics, transcriptomics and brain morphometry in Alzheimer's disease.. *NeuroImage*. PMID: 37634885
4. Identification of Prognosis-Related Genes in Bladder Cancer Microenvironment across TCGA Database.. *BioMed research international*. PMID: 33204728
5. Chronic high-salt diet induces cognitive impairment and anxiety through gut microbiota alterations.. *European journal of pharmacology*. PMID: 41207351

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.8 |
| 高置信度残基 (pLDDT>90) 占比 | 41.3% |
| 置信残基 (pLDDT 70-90) 占比 | 34.8% |
| 中等置信 (pLDDT 50-70) 占比 | 9.1% |
| 低置信 (pLDDT<50) 占比 | 14.8% |
| 有序区域 (pLDDT>70) 占比 | 76.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=78.8，有序区 76.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR056426, IPR042833, IPR048859, IPR011333; Pfam: PF23998, PF21059 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PLEKHA1 | 0.576 | 0.000 | — |
| CCDC191 | 0.480 | 0.000 | — |
| DPY19L3 | 0.452 | 0.000 | — |
| ZBTB16 | 0.429 | 0.000 | — |
| ARMS2 | 0.407 | 0.000 | — |
| TACC2 | 0.403 | 0.000 | — |
| NDUFAF6 | 0.400 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ROPN1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 7，IntAct interactions: 1
- 调控相关比例: 0 / 7 = 0%

**评价**: STRING 7 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.8 + PDB: 无 | pLDDT=78.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 7 + 1 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. BTBD16 — BTB/POZ domain-containing protein 16，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小506 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q32M84
- Protein Atlas: https://www.proteinatlas.org/search/BTBD16
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BTBD16
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q32M84
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (uncertain)。来源: https://www.proteinatlas.org/ENSG00000138152-BTBD16/subcellular

![](https://images.proteinatlas.org/57638/1101_G4_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/57638/1101_G4_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/57638/1135_G4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/57638/1135_G4_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/57638/1393_H1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/57638/1393_H1_4_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q32M84-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
