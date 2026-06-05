---
type: protein-evaluation
gene: "NSRP1"
date: 2026-06-04
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NSRP1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NSRP1 / CCDC55, NSRP70 |
| 蛋白名称 | Nuclear speckle splicing regulatory protein 1 |
| 蛋白大小 | 558 aa / 66.4 kDa |
| UniProt ID | Q9H0G5 |
| 评估日期 | 2026-06-04 |

**功能简介** (UniProt): RNA-binding protein that mediates pre-mRNA alternative splicing regulation (PubMed:21296756). Through CCDC118 regulation, may promote pre-adipocyte differentiation (By similarity)

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus; Nucleus speckle |
| 蛋白大小 | 10/10 | ×1 | 10 | 558 aa / 66.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=8 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR046850, IPR042816, IPR018612; Pfam: PF20427, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.0/180** | |
| **归一化总分** | | | **76.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus; Nucleus speckle | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- ribonucleoprotein complex (GO:1990904)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8 |
| PubMed broad count | 15 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CCDC55, NSRP70 |

**关键文献**:
1. The CCDC55 couples cannabinoid receptor CNR1 to a putative DISC1 schizophrenia pathway.. *Neuroscience*. PMID: 26475744
2. A milder form of NSRP1-associated neurodevelopmental disorder, caused by a missense variant in the nuclear localization signal.. *American journal of medical genetics. Part A*. PMID: 38808951
3. Downregulation of the splicing regulator NSRP1 confers resistance to CDK4/6 inhibitors via activation of interferon signaling in breast cancer.. *The Journal of biological chemistry*. PMID: 39667501
4. Comprehensive Atlas of Alternative Splicing Reveals NSRP1 Promoting Adipogenesis through CCDC18.. *International journal of molecular sciences*. PMID: 38474122
5. SNPs associated with body weight and backfat thickness in two pig breeds identified by a genome-wide association study.. *Genomics*. PMID: 30439481

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.8 |
| 高置信度残基 (pLDDT>90) 占比 | 8.6% |
| 置信残基 (pLDDT 70-90) 占比 | 31.0% |
| 中等置信 (pLDDT 50-70) 占比 | 22.9% |
| 低置信 (pLDDT<50) 占比 | 37.5% |
| 有序区域 (pLDDT>70) 占比 | 39.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=62.8），有序残基占 39.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR046850, IPR042816, IPR018612; Pfam: PF20427, PF09745 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CDC5L | 0.961 | 0.954 | — |
| CTNNBL1 | 0.766 | 0.762 | — |
| EFCAB5 | 0.725 | 0.000 | — |
| SLU7 | 0.695 | 0.000 | — |
| PPIL4 | 0.654 | 0.490 | — |
| DHX40 | 0.634 | 0.140 | — |
| NKAP | 0.620 | 0.000 | — |
| DHX8 | 0.603 | 0.214 | — |
| MFAP1 | 0.597 | 0.197 | — |
| SF3A1 | 0.585 | 0.184 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%，尚无实验验证互作。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.8 + PDB: 无 | pLDDT=62.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Nucleus speckle / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. NSRP1 — Nuclear speckle splicing regulatory protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小558 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=62.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H0G5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000126653-NSRP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NSRP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H0G5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live via harvest pipeline; evaluated 2026-06-04

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000126653-NSRP1/subcellular

![](https://images.proteinatlas.org/15593/138_G5_1_red_green.jpg)
![](https://images.proteinatlas.org/15593/138_G5_2_red_green.jpg)
![](https://images.proteinatlas.org/15593/139_G5_1_red_green.jpg)
![](https://images.proteinatlas.org/15593/139_G5_2_red_green.jpg)
![](https://images.proteinatlas.org/15593/166_G5_1_red_green.jpg)
![](https://images.proteinatlas.org/15593/166_G5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H0G5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
