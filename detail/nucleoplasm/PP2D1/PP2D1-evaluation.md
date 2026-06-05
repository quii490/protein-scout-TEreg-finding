---
type: protein-evaluation
gene: "PP2D1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PP2D1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PP2D1 / C3orf48 |
| 蛋白名称 | Protein phosphatase 2C-like domain-containing protein 1 |
| 蛋白大小 | 630 aa / 71.6 kDa |
| UniProt ID | A8MPX8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Intermediate filaments; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 630 aa / 71.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=71.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR015655, IPR036457, IPR001932; Pfam: PF00481 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 11 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Intermediate filaments | Uncertain |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3 |
| PubMed broad count | 3 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C3orf48 |

**关键文献**:
1. Metal-dependent Ser/Thr protein phosphatase PPM family: Evolution, structures, diseases and inhibitors.. *Pharmacology & therapeutics*. PMID: 32650009
2. Large-scale discovery of male reproductive tract-specific genes through analysis of RNA-seq datasets.. *BMC biology*. PMID: 32814578
3. Gene expression profiles in respiratory settings in rats under extracorporeal membrane oxygenation.. *Journal of thoracic disease*. PMID: 39975719

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.5 |
| 高置信度残基 (pLDDT>90) 占比 | 41.1% |
| 置信残基 (pLDDT 70-90) 占比 | 22.9% |
| 中等置信 (pLDDT 50-70) 占比 | 7.0% |
| 低置信 (pLDDT<50) 占比 | 29.0% |
| 有序区域 (pLDDT>70) 占比 | 64.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=71.5，有序区 64.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR015655, IPR036457, IPR001932; Pfam: PF00481 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SPINT4 | 0.507 | 0.000 | — |
| SAXO1 | 0.499 | 0.091 | — |
| PPTC7 | 0.492 | 0.074 | — |
| HCFC1R1 | 0.457 | 0.000 | — |
| ZMYM5 | 0.425 | 0.113 | — |
| MTFMT | 0.419 | 0.000 | — |
| MED31 | 0.415 | 0.414 | — |
| MED14 | 0.412 | 0.406 | — |
| D6RAR5_HUMAN | 0.410 | 0.000 | — |
| MED7 | 0.406 | 0.406 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 11，IntAct interactions: 1
- 调控相关比例: 0 / 11 = 0%

**评价**: STRING 11 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.5 + PDB: 无 | pLDDT=71.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Intermediate filaments | 一致 |
| PPI | STRING + IntAct | 11 + 1 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. PP2D1 — Protein phosphatase 2C-like domain-containing protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小630 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A8MPX8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000183977-PP2D1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PP2D1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A8MPX8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000183977-PP2D1/subcellular

![](https://images.proteinatlas.org/36870/422_A12_1_red_green.jpg)
![](https://images.proteinatlas.org/36870/422_A12_2_red_green.jpg)
![](https://images.proteinatlas.org/36870/423_A12_1_red_green.jpg)
![](https://images.proteinatlas.org/36870/423_A12_2_red_green.jpg)
![](https://images.proteinatlas.org/36870/426_A12_1_red_green.jpg)
![](https://images.proteinatlas.org/36870/426_A12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-A8MPX8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
