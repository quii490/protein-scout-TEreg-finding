---
type: protein-evaluation
gene: "CPSF3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CPSF3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CPSF3 / CPSF73 |
| 蛋白名称 | Cleavage and polyadenylation specificity factor subunit 3 |
| 蛋白大小 | 684 aa / 77.5 kDa |
| UniProt ID | Q9UKF6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | x4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 10/10 | x1 | 10 | 684 aa / 77.5 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=31 篇 (≤40→8) |
| 三维结构 | 10/10 | x3 | 30 | AlphaFold v6 pLDDT=90.2; PDB: 2I7T, 2I7V, 6M8Q, 6V4X, 8T1Q, 8T1R |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR022712, IPR021718, IPR050698, IPR001279, IPR036 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **139.5/180** | |
| **归一化总分** | | | **77.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- mRNA cleavage and polyadenylation specificity factor complex (GO:0005847)
- nucleoplasm (GO:0005654)
- ribonucleoprotein complex (GO:1990904)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 31 |
| PubMed broad count | 60 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CPSF73 |

**关键文献**:
1. CPSF3 regulates alternative polyadenylation of CNIH2 to promote esophageal squamous cell carcinoma progression.. *Cancer letters*. PMID: 38718887
2. Heat shock induces premature transcript termination and reconfigures the human transcriptome.. *Molecular cell*. PMID: 35114099
3. Small molecule inhibition of CPSF3 impacts R-loop distribution and abundance.. *bioRxiv : the preprint server for biology*. PMID: 40654756
4. CSR1 induces cell death through inactivation of CPSF3.. *Oncogene*. PMID: 18806823
5. Comprehensive investigation identifies CPSF3 as a novel prognostic and oncogenic biomarker in bladder cancer.. *Discover oncology*. PMID: 41071397

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.2 |
| 高置信度残基 (pLDDT>90) 占比 | 64.0% |
| 置信残基 (pLDDT 70-90) 占比 | 30.6% |
| 中等置信 (pLDDT 50-70) 占比 | 3.9% |
| 低置信 (pLDDT<50) 占比 | 1.5% |
| 有序区域 (pLDDT>70) 占比 | 94.6% |
| 可用 PDB 条目 | 2I7T, 2I7V, 6M8Q, 6V4X, 8T1Q, 8T1R |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构 + AlphaFold极高置信度（pLDDT=90.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR022712, IPR021718, IPR050698, IPR001279, IPR036866; Pfam: PF10996, PF11718, PF00753 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CPSF2 | 0.999 | 0.997 | — |
| WDR33 | 0.999 | 0.992 | — |
| CPSF4 | 0.999 | 0.961 | — |
| CPSF1 | 0.999 | 0.991 | — |
| CSTF2 | 0.999 | 0.929 | — |
| FIP1L1 | 0.999 | 0.969 | — |
| SYMPK | 0.999 | 0.997 | — |
| PCF11 | 0.998 | 0.954 | — |
| WDR82 | 0.995 | 0.964 | — |
| RBBP6 | 0.994 | 0.974 | — |

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
| 三维结构 | AlphaFold pLDDT=90.2 + PDB: 2I7T, 2I7V, 6M8Q, 6V4X, 8T1Q,  | pLDDT=90.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (>=3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. CPSF3 -- Cleavage and polyadenylation specificity factor subunit 3，非常新颖，仅有少数基础研究。
2. 蛋白大小684 aa，大小适中（200-800 aa），适合常规生化实验。

**风险/不确定性**:
1. PubMed 31 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UKF6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000119203-CPSF3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CPSF3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UKF6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UKF6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
