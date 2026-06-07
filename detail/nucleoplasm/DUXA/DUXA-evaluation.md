---
type: protein-evaluation
gene: "DUXA"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DUXA 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DUXA |
| 蛋白名称 | Double homeobox protein A |
| 蛋白大小 | 204 aa / 23.8 kDa |
| UniProt ID | A6NLW8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 204 aa / 23.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=17 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=75.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001356, IPR051306, IPR009057, IPR000047; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **137.0/180** | |
| **归一化总分** | | | **76.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 17 |
| PubMed broad count | 25 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Single-nucleus RNA-seq identifies divergent populations of FSHD2 myotube nuclei.. *PLoS genetics*. PMID: 32365093
2. Relationship of DUX4 and target gene expression in FSHD myocytes.. *Human mutation*. PMID: 33502067
3. Antagonism among DUX family members evolved from an ancestral toxic single homeodomain protein.. *iScience*. PMID: 37744032
4. Antagonism among DUX family members evolved from an ancestral toxic single homeodomain protein.. *bioRxiv : the preprint server for biology*. PMID: 36711898
5. DUXA regulates the early development of porcine cloned embryos.. *Theriogenology*. PMID: 40652737

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.2 |
| 高置信度残基 (pLDDT>90) 占比 | 51.0% |
| 置信残基 (pLDDT 70-90) 占比 | 6.9% |
| 中等置信 (pLDDT 50-70) 占比 | 17.2% |
| 低置信 (pLDDT<50) 占比 | 25.0% |
| 有序区域 (pLDDT>70) 占比 | 57.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=75.2，有序区 57.9%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001356, IPR051306, IPR009057, IPR000047; Pfam: PF00046 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LEUTX | 0.746 | 0.091 | — |
| TPRX1 | 0.730 | 0.000 | — |
| ARGFX | 0.724 | 0.091 | — |
| NANOGNB | 0.628 | 0.000 | — |
| ZSCAN4 | 0.612 | 0.071 | — |
| MBD3L3 | 0.533 | 0.068 | — |
| ADAT1 | 0.481 | 0.000 | — |
| PRAMEF5 | 0.455 | 0.000 | — |
| RHOXF2B | 0.448 | 0.000 | — |
| PLAC9 | 0.448 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.2 + PDB: 无 | pLDDT=75.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DUXA — Double homeobox protein A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小204 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 17 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A6NLW8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000258873-DUXA/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DUXA
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A6NLW8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03



<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-A6NLW8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | A6NLW8 |
| SMART | SM00389; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR001356;IPR051306;IPR009057;IPR000047; |
| Pfam | PF00046; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000258873-DUXA/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
