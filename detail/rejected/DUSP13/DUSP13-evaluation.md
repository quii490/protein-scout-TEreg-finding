---
type: protein-evaluation
gene: "DUSP13"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DUSP13 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DUSP13 / DUSP13, SKRP4, TMDP |
| 蛋白名称 | Dual specificity protein phosphatase 13B |
| 蛋白大小 | 198 aa / 22.1 kDa |
| UniProt ID | Q9UII6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: 无注释 |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 198 aa / 22.1 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=20 篇 (≤20→10) |
| 🏗️ 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=90.7; PDB: 2GWO, 2PQ5 |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR020405, IPR000340, IPR029021, IPR016130, IPR000 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 11 partners; IntAct 0 interactions |
| ➕ 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **119.0/180** | |
| **归一化总分** | | | **66.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 20 |
| PubMed broad count | 27 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DUSP13, SKRP4, TMDP |

**关键文献**:
1. Therapeutic Targets for Sepsis: Multicenter Proteome-Wide Analyses and Experimental Validation.. *Journal of proteome research*. PMID: 40459852
2. Predicted plasma proteomics from genetic scores and treatment outcomes in major depression: a meta-analysis.. *European neuropsychopharmacology : the journal of the European College of Neuropsychopharmacology*. PMID: 40408832
3. Dual-specificity phosphatases 13 and 27 as key switches in muscle stem cell transition from proliferation to differentiation.. *Stem cells (Dayton, Ohio)*. PMID: 38975693
4. Myogenin Regulates DUSP13 to Inhibit Apoptosis Induced by Reactive Oxygen Species.. *Frontiers in bioscience (Landmark edition)*. PMID: 38420814
5. A phenome-wide bidirectional Mendelian randomization analysis of atrial fibrillation.. *International journal of epidemiology*. PMID: 35292824

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.7 |
| 高置信度残基 (pLDDT>90) 占比 | 78.8% |
| 置信残基 (pLDDT 70-90) 占比 | 10.1% |
| 中等置信 (pLDDT 50-70) 占比 | 5.1% |
| 低置信 (pLDDT<50) 占比 | 6.1% |
| 有序区域 (pLDDT>70) 占比 | 88.9% |
| 可用 PDB 条目 | 2GWO, 2PQ5 |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（2GWO, 2PQ5）+ AlphaFold高质量预测（pLDDT=90.7），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR020405, IPR000340, IPR029021, IPR016130, IPR000387; Pfam: PF00782 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LMNA | 0.658 | 0.645 | — |
| ATXN1 | 0.503 | 0.292 | — |
| UTP15 | 0.488 | 0.000 | — |
| AP3M1 | 0.486 | 0.049 | — |
| KAT6B | 0.471 | 0.084 | — |
| CACNG1 | 0.457 | 0.000 | — |
| SAMD8 | 0.452 | 0.000 | — |
| SMIM12 | 0.410 | 0.047 | — |
| DUSP11 | 0.407 | 0.048 | — |
| LYZL4 | 0.404 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 11，IntAct interactions: 0
- 调控相关比例: 0 / 11 = 0%

**评价**: STRING 11 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.7 + PDB: 2GWO, 2PQ5 | pLDDT=90.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 11 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. DUSP13 — Dual specificity protein phosphatase 13B，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小198 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 20 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UII6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000079393-DUSP13/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DUSP13
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UII6
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 12:20:58
