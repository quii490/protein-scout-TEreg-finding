---
type: protein-evaluation
gene: "POU5F1B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## POU5F1B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | POU5F1B / OCT4PG1, OTF3C, OTF3P1, POU5F1P1, POU5FLC20 |
| 蛋白名称 | POU domain, class 5, transcription factor 1B |
| 蛋白大小 | 359 aa / 38.6 kDa |
| UniProt ID | Q06416 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Mitochondria, Cytosol; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 359 aa / 38.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=20 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001356, IPR017970, IPR009057, IPR010982, IPR013 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 13 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **129.5/180** | |
| **归一化总分** | | | **71.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Mitochondria, Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytosol (GO:0005829)
- mitochondrion (GO:0005739)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 20 |
| PubMed broad count | 40 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: OCT4PG1, OTF3C, OTF3P1, POU5F1P1, POU5FLC20, POU5FLC8 |

**关键文献**:
1. Genome-wide profiling of HPV integration in cervical cancer identifies clustered genomic hot spots and a potential microhomology-mediated integration mechanism.. *Nature genetics*. PMID: 25581428
2. Transposon-activated POU5F1B promotes colorectal cancer growth and metastasis.. *Nature communications*. PMID: 35987910
3. The landscape of 8q24 cytoband in gastric cancer (Review).. *Oncology letters*. PMID: 38464340
4. The Octamer-Binding Transcription Factor 4 (OCT4) Pseudogene, POU Domain Class 5 Transcription Factor 1B (POU5F1B), is Upregulated in Cervical Cancer and Down-Regulation Inhibits Cell Proliferation and Migration and Induces Apoptosis in Cervical Cancer Cell Lines.. *Medical science monitor : international medical journal of experimental and clinical research*. PMID: 30762028
5. Expression Profiling of Circulating Tumor Cells in Pancreatic Ductal Adenocarcinoma Patients: Biomarkers Predicting Overall Survival.. *Frontiers in oncology*. PMID: 31552188

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.4 |
| 高置信度残基 (pLDDT>90) 占比 | 29.2% |
| 置信残基 (pLDDT 70-90) 占比 | 8.4% |
| 中等置信 (pLDDT 50-70) 占比 | 18.1% |
| 低置信 (pLDDT<50) 占比 | 44.3% |
| 有序区域 (pLDDT>70) 占比 | 37.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=64.4），有序残基占 37.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001356, IPR017970, IPR009057, IPR010982, IPR013847; Pfam: PF00046, PF00157 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| POU5F1 | 0.970 | 0.000 | — |
| NANOG | 0.716 | 0.307 | — |
| LRATD2 | 0.642 | 0.000 | — |
| MYC | 0.635 | 0.000 | — |
| NANOGP8 | 0.630 | 0.000 | — |
| TCF7L2 | 0.582 | 0.065 | — |
| PRDM14 | 0.572 | 0.053 | — |
| PGA5 | 0.478 | 0.000 | — |
| CCHCR1 | 0.477 | 0.130 | — |
| HLA-C | 0.424 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 13，IntAct interactions: 0
- 调控相关比例: 0 / 13 = 0%

**评价**: STRING 13 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.4 + PDB: 无 | pLDDT=64.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm; 额外: Mitochondria, Cytosol | 一致 |
| PPI | STRING + IntAct | 13 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. POU5F1B — POU domain, class 5, transcription factor 1B，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小359 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 20 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=64.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q06416
- Protein Atlas: https://www.proteinatlas.org/ENSG00000212993-POU5F1B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=POU5F1B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q06416
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000212993-POU5F1B/subcellular

![](https://images.proteinatlas.org/58267/1343_G6_1_red_green.jpg)
![](https://images.proteinatlas.org/58267/1343_G6_2_red_green.jpg)
![](https://images.proteinatlas.org/58267/1347_G6_2_red_green.jpg)
![](https://images.proteinatlas.org/58267/1347_G6_3_red_green.jpg)
![](https://images.proteinatlas.org/58267/1518_H6_1_red_green.jpg)
![](https://images.proteinatlas.org/58267/1518_H6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q06416-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
