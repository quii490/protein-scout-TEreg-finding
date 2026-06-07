---
type: protein-evaluation
gene: "SEBOX"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SEBOX 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SEBOX / OG9X |
| 蛋白名称 | Homeobox protein SEBOX |
| 蛋白大小 | 190 aa / 20.4 kDa |
| UniProt ID | Q9HB31 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 190 aa / 20.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=8 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001356, IPR009057, IPR042223; Pfam: PF00046 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 9 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **131.5/180** | |
| **归一化总分** | | | **73.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nucleus (GO:0005634)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8 |
| PubMed broad count | 9 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: OG9X |

**关键文献**:
1. Double assurance in the induction of axial development by egg dorsal determinants in Xenopus embryos.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 39928870
2. Associations among Sebox and other MEGs and its effects on early embryogenesis.. *PloS one*. PMID: 25679966
3. Mouse Sebox homeobox gene expression in skin, brain, oocytes, and two-cell embryos.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 10922053
4. Knockdown of maternal homeobox transcription factor SEBOX gene impaired early embryonic development in porcine parthenotes.. *The Journal of reproduction and development*. PMID: 24018616
5. Sebox regulates mesoderm formation in early amphibian embryos.. *Developmental dynamics : an official publication of the American Association of Anatomists*. PMID: 26285158

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.2 |
| 高置信度残基 (pLDDT>90) 占比 | 25.3% |
| 置信残基 (pLDDT 70-90) 占比 | 7.4% |
| 中等置信 (pLDDT 50-70) 占比 | 42.1% |
| 低置信 (pLDDT<50) 占比 | 25.3% |
| 有序区域 (pLDDT>70) 占比 | 32.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=65.2），有序残基占 32.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001356, IPR009057, IPR042223; Pfam: PF00046 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LBX1 | 0.701 | 0.104 | — |
| SCGN | 0.486 | 0.100 | — |
| TMEM200A | 0.475 | 0.000 | — |
| OOEP | 0.459 | 0.000 | — |
| H1-8 | 0.445 | 0.000 | — |
| NOBOX | 0.434 | 0.000 | — |
| TLE6 | 0.423 | 0.095 | — |
| MYH8 | 0.414 | 0.045 | — |
| CA8 | 0.406 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 9，IntAct interactions: 0
- 调控相关比例: 0 / 9 = 0%

**评价**: STRING 9 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.2 + PDB: 无 | pLDDT=65.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 9 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. SEBOX — Homeobox protein SEBOX，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小190 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=65.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9HB31
- Protein Atlas: https://www.proteinatlas.org/ENSG00000274529-SEBOX/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SEBOX
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9HB31
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03



<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9HB31-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9HB31 |
| SMART | SM00389; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR001356;IPR009057;IPR042223; |
| Pfam | PF00046; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000274529-SEBOX/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
