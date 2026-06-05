---
type: protein-evaluation
gene: "N4BP2L2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## N4BP2L2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | N4BP2L2 / CG005, PFAAP5 |
| 蛋白名称 | NEDD4-binding protein 2-like 2 |
| 蛋白大小 | 583 aa / 67.5 kDa |
| UniProt ID | Q92802 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 583 aa / 67.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=54.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026302, IPR027417; Pfam: PF13671 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- extracellular exosome (GO:0070062)
- nucleus (GO:0005634)
- transcription repressor complex (GO:0017053)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 15 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CG005, PFAAP5 |

**关键文献**:
1. Biomarker Identification in Membranous Nephropathy Using a Long Non-coding RNA-Mediated Competitive Endogenous RNA Network.. *Interdisciplinary sciences, computational life sciences*. PMID: 34472046
2. Comprehensive analysis of ammonia-induced cell death and GLS1 in gastric adenocarcinoma: implications for prognosis and therapeutic strategies.. *Cancer cell international*. PMID: 41063160
3. Circ-N4BP2L2 enhances mitochondrial function in non-small cell lung cancer cells through regulating the miR-135a-5p/ARL5B axis.. *Environmental toxicology*. PMID: 36637163
4. Expression profile of circular RNAs in epicardial adipose tissue in heart failure.. *Chinese medical journal*. PMID: 32852391
5. Multiomics Screening Identifies Molecular Biomarkers Causally Associated With the Risk of Coronary Artery Disease.. *Circulation. Genomic and precision medicine*. PMID: 32969717

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 54.8 |
| 高置信度残基 (pLDDT>90) 占比 | 24.5% |
| 置信残基 (pLDDT 70-90) 占比 | 4.3% |
| 中等置信 (pLDDT 50-70) 占比 | 6.0% |
| 低置信 (pLDDT<50) 占比 | 65.2% |
| 有序区域 (pLDDT>70) 占比 | 28.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=54.8），有序残基占 28.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026302, IPR027417; Pfam: PF13671 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NDUFB7 | 0.703 | 0.483 | — |
| NDUFA5 | 0.538 | 0.471 | — |
| SCAF11 | 0.538 | 0.000 | — |
| PPIH | 0.537 | 0.537 | — |
| NDUFA6 | 0.536 | 0.483 | — |
| NDUFS6 | 0.532 | 0.483 | — |
| NDUFS2 | 0.527 | 0.471 | — |
| PNISR | 0.522 | 0.000 | — |
| NDUFA2 | 0.521 | 0.483 | — |
| NDUFA12 | 0.520 | 0.483 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Hoxa1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15418|pubmed:23088713 |
| PRPF4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| Q0WD93 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| yscR | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| hmsT | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| A0A384L0S4 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| A0A380PMW6 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ENSP00000501537.1 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| rlmF | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| cutF | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=54.8 + PDB: 无 | pLDDT=54.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. N4BP2L2 — NEDD4-binding protein 2-like 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小583 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=54.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q92802
- Protein Atlas: https://www.proteinatlas.org/ENSG00000244754-N4BP2L2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=N4BP2L2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q92802
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000244754-N4BP2L2/subcellular

![](https://images.proteinatlas.org/59327/1016_G10_2_red_green.jpg)
![](https://images.proteinatlas.org/59327/1016_G10_3_red_green.jpg)
![](https://images.proteinatlas.org/59327/1061_E6_2_red_green.jpg)
![](https://images.proteinatlas.org/59327/1061_E6_3_red_green.jpg)
![](https://images.proteinatlas.org/59327/1239_G10_1_red_green.jpg)
![](https://images.proteinatlas.org/59327/1239_G10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q92802-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
