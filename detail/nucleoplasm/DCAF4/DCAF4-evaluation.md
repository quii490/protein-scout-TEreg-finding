---
type: protein-evaluation
gene: "DCAF4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DCAF4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DCAF4 / WDR21, WDR21A |
| 蛋白名称 | DDB1- and CUL4-associated factor 4 |
| 蛋白大小 | 495 aa / 55.7 kDa |
| UniProt ID | Q8WV16 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | x4 | 32 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | x1 | 10 | 495 aa / 55.7 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=77.2; PDB: 3I8C |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR052254, IPR015943, IPR036322, IPR001680; Pfam:  |
| PPI 网络 | 2/10 | x3 | 6 | STRING 0 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **137.5/180** | |
| **归一化总分** | | | **76.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- Cul4-RING E3 ubiquitin ligase complex (GO:0080008)
- nucleoplasm (GO:0005654)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 14 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: WDR21, WDR21A |

**关键文献**:
1. DCAF4, a novel gene associated with leucocyte telomere length.. *Journal of medical genetics*. PMID: 25624462
2. Integrated Bioinformatics Analysis of the Hub Genes Involved in Irinotecan Resistance in Colorectal Cancer.. *Biomedicines*. PMID: 35885025
3. Small molecule NSC1892 targets the CUL4A/4B-DDB1 interactions and causes impairment of CRL4(DCAF4) E3 ligases to inhibit colorectal cancer cell growth.. *International journal of biological sciences*. PMID: 32140073
4. Inflammation-dependent overexpression of c-Myc enhances CRL4(DCAF4) E3 ligase activity and promotes ubiquitination of ST7 in colitis-associated cancer.. *The Journal of pathology*. PMID: 30945288
5. Gene-based evaluation of low-frequency variation and genetically-predicted gene expression impacting risk of keloid formation.. *Annals of human genetics*. PMID: 29484647

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.2 |
| 高置信度残基 (pLDDT>90) 占比 | 34.1% |
| 置信残基 (pLDDT 70-90) 占比 | 42.0% |
| 中等置信 (pLDDT 50-70) 占比 | 9.1% |
| 低置信 (pLDDT<50) 占比 | 14.7% |
| 有序区域 (pLDDT>70) 占比 | 76.1% |
| 可用 PDB 条目 | 3I8C |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 高质量预测（pLDDT=77.2，有序区 76.1%）。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052254, IPR015943, IPR036322, IPR001680; Pfam: PF23761 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究基础。

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
| 三维结构 | AlphaFold pLDDT=77.2 + PDB: 3I8C | pLDDT=77.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 0 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DCAF4 -- DDB1- and CUL4-associated factor 4，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小495 aa，大小适中（200-800 aa），适合常规生化实验。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WV16
- Protein Atlas: https://www.proteinatlas.org/ENSG00000119599-DCAF4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DCAF4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WV16
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
