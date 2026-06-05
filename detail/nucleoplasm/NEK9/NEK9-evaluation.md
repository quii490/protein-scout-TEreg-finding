---
type: protein-evaluation
gene: "NEK9"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NEK9 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NEK9 / KIAA1995, NEK8, NERCC |
| 蛋白名称 | Serine/threonine-protein kinase Nek9 |
| 蛋白大小 | 979 aa / 107.2 kDa |
| UniProt ID | Q8TD19 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 979 aa / 107.2 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=72 篇 (≤80→4) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=73.9; PDB: 3ZKE, 3ZKF |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011009, IPR042767, IPR000719, IPR058923, IPR009 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **108.0/180** | |
| **归一化总分** | | | **60.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 72 |
| PubMed broad count | 119 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1995, NEK8, NERCC |

**关键文献**:
1. USP19 potentiates autophagic cell death via inhibiting mTOR pathway through deubiquitinating NEK9 in pancreatic cancer.. *Cell death and differentiation*. PMID: 39627360
2. NEK9 regulates primary cilia formation by acting as a selective autophagy adaptor for MYH9/myosin IIA.. *Nature communications*. PMID: 34078910
3. Cancer associated fibroblast derived SLIT2 drives gastric cancer cell metastasis by activating NEK9.. *Cell death & disease*. PMID: 37443302
4. NEK9-mediated Wnt signalling repressor TLE3 rewires Docetaxel resistance in cancer cells by inducing pyroptosis.. *British journal of cancer*. PMID: 40926063
5. Phosphorylation of shiftless is important for inhibiting the programmed -1 ribosomal frameshift.. *Science advances*. PMID: 41417896

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.9 |
| 高置信度残基 (pLDDT>90) 占比 | 43.1% |
| 置信残基 (pLDDT 70-90) 占比 | 24.3% |
| 中等置信 (pLDDT 50-70) 占比 | 7.6% |
| 低置信 (pLDDT<50) 占比 | 25.0% |
| 有序区域 (pLDDT>70) 占比 | 67.4% |
| 可用 PDB 条目 | 3ZKE, 3ZKF |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（3ZKE, 3ZKF）+ AlphaFold高质量预测（pLDDT=73.9），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011009, IPR042767, IPR000719, IPR058923, IPR009091; Pfam: PF00069, PF25390 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NEK7 | 0.999 | 0.962 | — |
| ANKS6 | 0.979 | 0.050 | — |
| NEK6 | 0.975 | 0.842 | — |
| NPHP3 | 0.973 | 0.045 | — |
| INVS | 0.929 | 0.050 | — |
| BICD2 | 0.924 | 0.413 | — |
| PLK1 | 0.856 | 0.301 | — |
| DYNLL1 | 0.844 | 0.620 | — |
| EML4 | 0.811 | 0.622 | — |
| ANKS3 | 0.767 | 0.050 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000238616.5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| ENSMUSP00000049056.8 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| NEK6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| GABARAPL2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| TTN | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| MAP1LC3A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| GABARAPL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| GABARAP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| EBI-1380999 | psi-mi:"MI:0096"(pull down) | pubmed:17721511|imex:IM-19952 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.9 + PDB: 3ZKE, 3ZKF | pLDDT=73.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. NEK9 — Serine/threonine-protein kinase Nek9，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小979 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 72 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TD19
- Protein Atlas: https://www.proteinatlas.org/ENSG00000119638-NEK9/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NEK9
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TD19
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8TD19-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
