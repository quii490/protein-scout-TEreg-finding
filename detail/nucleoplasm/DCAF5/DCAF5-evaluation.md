---
type: protein-evaluation
gene: "DCAF5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DCAF5 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DCAF5 / BCRG2, KIAA1824, WDR22 |
| 蛋白名称 | DDB1- and CUL4-associated factor 5 |
| 蛋白大小 | 942 aa / 104.0 kDa |
| UniProt ID | Q96JK2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Mitochondria; UniProt: 无注释 |
| 蛋白大小 | 8/10 | x1 | 8 | 942 aa / 104.0 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=8 篇 (≤20→10) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold v6 pLDDT=60.1; PDB: 3I89, 8TL6 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR045151, IPR015943, IPR036322, IPR001680; Pfam:  |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.0/180** | |
| **归一化总分** | | | **64.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA检测到可靠IF图像信号。

**GO Cellular Component**:
- Cul4-RING E3 ubiquitin ligase complex (GO:0080008)
- cytoplasm (GO:0005737)
- nucleoplasm (GO:0005654)

**结论**: 核定位信号较弱，多个数据源显示混合定位。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8 |
| PubMed broad count | 15 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BCRG2, KIAA1824, WDR22 |

**关键文献**:
1. Targeting DCAF5 suppresses SMARCB1-mutant cancer by stabilizing SWI/SNF.. *Nature*. PMID: 38538798
2. Lysine Methylation-Dependent Proteolysis by the Malignant Brain Tumor (MBT) Domain Proteins.. *International journal of molecular sciences*. PMID: 38396925
3. Genetic Variants Associated with Neuropeptide Y Autoantibody Levels in Newly Diagnosed Individuals with Type 1 Diabetes.. *Genes*. PMID: 35627254
4. Genome-wide scan for runs of homozygosity in South American Camelids.. *BMC genomics*. PMID: 37605116
5. Identification of DCAF5 as a novel cancer prognostic and immunotherapy biomarker through pan-cancer analysis and renal clear cell carcinoma clinical data validation.. *Discover oncology*. PMID: 40522583

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.1 |
| 高置信度残基 (pLDDT>90) 占比 | 29.8% |
| 置信残基 (pLDDT 70-90) 占比 | 10.8% |
| 中等置信 (pLDDT 50-70) 占比 | 9.7% |
| 低置信 (pLDDT<50) 占比 | 49.7% |
| 有序区域 (pLDDT>70) 占比 | 40.6% |
| 可用 PDB 条目 | 3I89, 8TL6 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=60.1），有序残基占 40.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR045151, IPR015943, IPR036322, IPR001680; Pfam: PF00400 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DDB1 | 0.998 | 0.978 | — |
| CUL4A | 0.970 | 0.660 | — |
| DCAF4 | 0.958 | 0.103 | — |
| CUL4B | 0.955 | 0.364 | — |
| DCAF12 | 0.954 | 0.000 | — |
| DCAF10 | 0.952 | 0.000 | — |
| DDB2 | 0.945 | 0.000 | — |
| DCAF6 | 0.942 | 0.000 | — |
| DCAF16 | 0.937 | 0.000 | — |
| TRPC4AP | 0.936 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=60.1 + PDB: 3I89, 8TL6 | pLDDT=60.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Mitochondria | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DCAF5 -- DDB1- and CUL4-associated factor 5，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小942 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=60.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96JK2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000139990-DCAF5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DCAF5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96JK2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96JK2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
