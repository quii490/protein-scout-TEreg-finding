---
type: protein-evaluation
gene: "PRRC2B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PRRC2B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PRRC2B / BAT2L, BAT2L1, KIAA0515 |
| 蛋白名称 | Protein PRRC2B |
| 蛋白大小 | 2229 aa / 243.0 kDa |
| UniProt ID | Q5JSZ5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Cytosol; 额外: Nuclear bodies; UniProt: 无注释 |
| 蛋白大小 | 2/10 | ×1 | 2 | 2229 aa / 243.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v6 pLDDT=38.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR009738, IPR033184; Pfam: PF07001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **103.5/180** | |
| **归一化总分** | | | **57.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nuclear bodies | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 22 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BAT2L, BAT2L1, KIAA0515 |

**关键文献**:
1. The Role of PRRC2B in Cerebral Vascular Remodeling Under Acute Hypoxia in Mice.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 37395402
2. RNA binding protein PRRC2B mediates translation of specific mRNAs and regulates cell cycle progression.. *Nucleic acids research*. PMID: 37125639
3. Loss-of-function of RNA-binding protein PRRC2B causes translational defects and congenital cardiovascular malformation.. *medRxiv : the preprint server for health sciences*. PMID: 39398999
4. Identification of key carcinogenic genes in Wilms' tumor.. *Genes & genetic systems*. PMID: 34334530
5. Identification and Characterization of a ceRNA Regulatory Network Involving LINC00482 and PRRC2B in Peripheral Blood Mononuclear Cells: Implications for COPD Pathogenesis and Diagnosis.. *International journal of chronic obstructive pulmonary disease*. PMID: 38348310

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 38.0 |
| 高置信度残基 (pLDDT>90) 占比 | 1.5% |
| 置信残基 (pLDDT 70-90) 占比 | 0.7% |
| 中等置信 (pLDDT 50-70) 占比 | 6.3% |
| 低置信 (pLDDT<50) 占比 | 91.6% |
| 有序区域 (pLDDT>70) 占比 | 2.2% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=38.0），有序残基占 2.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009738, IPR033184; Pfam: PF07001 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EIF3H | 0.825 | 0.825 | — |
| EIF3F | 0.815 | 0.813 | — |
| EIF3I | 0.786 | 0.786 | — |
| G3BP2 | 0.785 | 0.440 | — |
| EIF3L | 0.780 | 0.779 | — |
| EIF3E | 0.777 | 0.777 | — |
| EIF3G | 0.674 | 0.672 | — |
| G3BP1 | 0.618 | 0.463 | — |
| EIF3C | 0.598 | 0.592 | — |
| UBAP2L | 0.561 | 0.166 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EHMT2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ATN1 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| ATXN1 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| RERE | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| Hoxa1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15418|pubmed:23088713 |
| EIF3H | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| USP11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| USP3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| Eif3a | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| PLOD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=38.0 + PDB: 无 | pLDDT=38.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Cytosol; 额外: Nuclear bodies | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PRRC2B — Protein PRRC2B，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小2229 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=38.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5JSZ5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000288701-PRRC2B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PRRC2B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5JSZ5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
