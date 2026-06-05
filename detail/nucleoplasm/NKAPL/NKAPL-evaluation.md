---
type: protein-evaluation
gene: "NKAPL"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NKAPL 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NKAPL / C6orf194 |
| 蛋白名称 | NKAP-like protein |
| 蛋白大小 | 402 aa / 46.3 kDa |
| UniProt ID | Q5M9Q1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Golgi apparatus; 额外: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 402 aa / 46.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=15 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR040466, IPR009269; Pfam: PF15692, PF06047 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 12 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Nucleoplasm | Uncertain |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed broad count | 24 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C6orf194 |

**关键文献**:
1. NKAPL facilitates transcription pause-release and bridges elongation to initiation during meiosis exit.. *Nature communications*. PMID: 39824811
2. NKAPL suppresses NSCLC progression by enhancing the protein stability of TRIM21 and further inhibiting the NF-κB signaling pathway.. *Genes & diseases*. PMID: 40605974
3. Resequencing and association study of the NFKB activating protein-like gene (NKAPL) in schizophrenia.. *Schizophrenia research*. PMID: 24972756
4. Transcriptional landscape of human cancers.. *Oncotarget*. PMID: 28427185
5. Association of NKAPL, TSPAN18, and MPC2 gene variants with schizophrenia based on new data and a meta-analysis in Han Chinese.. *Acta neuropsychiatrica*. PMID: 27460766

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.1 |
| 高置信度残基 (pLDDT>90) 占比 | 8.7% |
| 置信残基 (pLDDT 70-90) 占比 | 26.9% |
| 中等置信 (pLDDT 50-70) 占比 | 16.9% |
| 低置信 (pLDDT<50) 占比 | 47.5% |
| 有序区域 (pLDDT>70) 占比 | 35.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=60.1），有序残基占 35.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR040466, IPR009269; Pfam: PF15692, PF06047 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ZKSCAN4 | 0.722 | 0.000 | — |
| ZKSCAN8 | 0.645 | 0.000 | — |
| NKAP | 0.619 | 0.598 | — |
| ZSCAN9 | 0.614 | 0.000 | — |
| ZSCAN16 | 0.608 | 0.000 | — |
| PRPF38A | 0.597 | 0.000 | — |
| PGBD1 | 0.596 | 0.000 | — |
| ZSCAN26 | 0.574 | 0.000 | — |
| CIR1 | 0.529 | 0.224 | — |
| ZSCAN31 | 0.515 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CUL2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| MAPK1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| NKAPD1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| ZNF417 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SREK1IP1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ARL6IP4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| DDX41 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| NKAP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CLK3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ZNF587 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 12
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 12 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.1 + PDB: 无 | pLDDT=60.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Golgi apparatus; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 12 interactions | 数据充分 |

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
1. NKAPL — NKAP-like protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小402 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 15 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=60.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5M9Q1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000189134-NKAPL/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NKAPL
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5M9Q1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (uncertain)。来源: https://www.proteinatlas.org/ENSG00000189134-NKAPL/subcellular

![](https://images.proteinatlas.org/71697/2095_C3_1_red_green.jpg)
![](https://images.proteinatlas.org/71697/2095_C3_3_red_green.jpg)
![](https://images.proteinatlas.org/71697/2100_G5_1_red_green.jpg)
![](https://images.proteinatlas.org/71697/2100_G5_2_red_green.jpg)
![](https://images.proteinatlas.org/71697/2104_D2_1_red_green.jpg)
![](https://images.proteinatlas.org/71697/2104_D2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5M9Q1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
