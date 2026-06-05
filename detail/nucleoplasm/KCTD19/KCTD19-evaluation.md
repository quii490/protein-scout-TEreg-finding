---
type: protein-evaluation
gene: "KCTD19"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KCTD19 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KCTD19 |
| 蛋白名称 | BTB/POZ domain-containing protein KCTD19 |
| 蛋白大小 | 926 aa / 104.9 kDa |
| UniProt ID | Q17RG1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 926 aa / 104.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011333, IPR003131; Pfam: PF02214 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 5 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **132.0/180** | |
| **归一化总分** | | | **73.3/100** | |

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
| PubMed strict count | 13 |
| PubMed broad count | 18 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. KCTD19 and its associated protein ZFP541 are independently essential for meiosis in male mice.. *PLoS genetics*. PMID: 33961623
2. Biallelic variants in KCTD19 associated with male factor infertility and oligoasthenoteratozoospermia.. *Human reproduction (Oxford, England)*. PMID: 37192818
3. Loss-of-function variants in KCTD19 cause non-obstructive azoospermia in humans.. *iScience*. PMID: 37485353
4. The ZFP541-KCTD19 complex is essential for pachytene progression by activating meiotic genes during mouse spermatogenesis.. *Journal of genetics and genomics = Yi chuan xue bao*. PMID: 35341968
5. Molecular quantitative trait loci in reproductive tissues impact male fertility in cattle.. *Nature communications*. PMID: 38253538

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.7 |
| 高置信度残基 (pLDDT>90) 占比 | 29.8% |
| 置信残基 (pLDDT 70-90) 占比 | 25.9% |
| 中等置信 (pLDDT 50-70) 占比 | 8.3% |
| 低置信 (pLDDT<50) 占比 | 36.0% |
| 有序区域 (pLDDT>70) 占比 | 55.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=65.7），有序残基占 55.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011333, IPR003131; Pfam: PF02214 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BOP1 | 0.978 | 0.834 | — |
| WDR12 | 0.963 | 0.806 | — |
| FTSJ3 | 0.959 | 0.805 | — |
| PES1 | 0.958 | 0.814 | — |
| NOC2L | 0.945 | 0.809 | — |
| MRTO4 | 0.941 | 0.802 | — |
| GTPBP4 | 0.938 | 0.823 | — |
| NIP7 | 0.932 | 0.811 | — |
| RPF1 | 0.929 | 0.812 | — |
| NIFK | 0.926 | 0.821 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ZSCAN22 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| - | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| B4DZ49 | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-23318|pubmed:25416956 |
| ECT2L | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| KCTD15 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 5
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 5 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.7 + PDB: 无 | pLDDT=65.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 5 interactions | 数据充分 |

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
1. KCTD19 — BTB/POZ domain-containing protein KCTD19，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小926 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=65.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q17RG1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000168676-KCTD19/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KCTD19
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q17RG1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q17RG1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
