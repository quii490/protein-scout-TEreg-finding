---
type: protein-evaluation
gene: "CDX4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CDX4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CDX4 |
| 蛋白名称 | Homeobox protein CDX-4 |
| 蛋白大小 | 284 aa / 30.5 kDa |
| UniProt ID | O14627 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm, Nuclear speckles; 额外: Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 284 aa / 30.5 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=82 篇 (≤100→2) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR006820, IPR047152, IPR001356, IPR020479, IPR017 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 13 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **98.0/180** | |
| **归一化总分** | | | **54.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear speckles; 额外: Cytosol | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 82 |
| PubMed broad count | 127 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. HoxA10 activates CDX4 transcription and Cdx4 activates HOXA10 transcription in myeloid cells.. *The Journal of biological chemistry*. PMID: 21471217
2. Cdx4 dysregulates Hox gene expression and generates acute myeloid leukemia alone and in cooperation with Meis1a in a murine model.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 17068127
3. Regulation of CDX4 gene transcription by HoxA9, HoxA10, the Mll-Ell oncogene and Shp2 during leukemogenesis.. *Oncogenesis*. PMID: 25531430
4. Cdx4 is a Cdx2 target gene.. *Mechanisms of development*. PMID: 20933081
5. Cdx4 and menin co-regulate Hoxa9 expression in hematopoietic cells.. *PloS one*. PMID: 17183676

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.8 |
| 高置信度残基 (pLDDT>90) 占比 | 20.1% |
| 置信残基 (pLDDT 70-90) 占比 | 5.3% |
| 中等置信 (pLDDT 50-70) 占比 | 39.4% |
| 低置信 (pLDDT<50) 占比 | 35.2% |
| 有序区域 (pLDDT>70) 占比 | 25.4% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=61.8），有序残基占 25.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR006820, IPR047152, IPR001356, IPR020479, IPR017970; Pfam: PF04731, PF00046 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TBPL2 | 0.911 | 0.000 | — |
| NAP1L2 | 0.868 | 0.000 | — |
| NAP1L1 | 0.762 | 0.000 | — |
| CHIC1 | 0.595 | 0.000 | — |
| ISL1 | 0.580 | 0.045 | — |
| SLC16A2 | 0.509 | 0.000 | — |
| FGF4 | 0.501 | 0.071 | — |
| TBX6 | 0.488 | 0.082 | — |
| LMO2 | 0.471 | 0.128 | — |
| FGF8 | 0.456 | 0.071 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PRKAB2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| PRKAA2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PITX1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-24135|pubmed:24722188| |
| ENSP00000362613.1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-23318|pubmed:25416956 |
| LMO2 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-23318|pubmed:25416956 |
| LMO1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-23318|pubmed:25416956 |
| PRKAA1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| CKS1B | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| - | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| BANP | psi-mi:"MI:1356"(validated two hybrid) | pubmed:26871637|imex:IM-25013| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 13
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 13 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.8 + PDB: 无 | pLDDT=61.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Nuclear speckles; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 13 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CDX4 — Homeobox protein CDX-4，研究基础较多，新颖性有限。
2. 蛋白大小284 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 82 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=61.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O14627
- Protein Atlas: https://www.proteinatlas.org/ENSG00000131264-CDX4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CDX4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O14627
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
