---
type: protein-evaluation
gene: "APBA1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## APBA1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | APBA1 / MINT1, X11 |
| 蛋白名称 | Amyloid-beta A4 precursor protein-binding family A member 1 |
| 蛋白大小 | 837 aa / 92.9 kDa |
| UniProt ID | Q02410 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Golgi apparatus; UniProt: Cytoplasm; Cytoplasm, perinuclear region; Nucleus; Golgi app |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 837 aa / 92.9 kDa |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=21 篇 (≤40→8) |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.0; PDB: 1AQC, 1U37, 1U38, 1U39, 1U3B, 1X11, 1X45 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR051230, IPR001478, IPR036034, IPR011993, IPR006 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **119.5/180** | |
| **归一化总分 (÷1.83)** | | | **63.9/100******** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus | Supported |
| UniProt | Cytoplasm; Cytoplasm, perinuclear region; Nucleus; Golgi apparatus | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA IF 图像状态: if_display_images_available。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- dendritic spine (GO:0043197)
- glutamatergic synapse (GO:0098978)
- Golgi apparatus (GO:0005794)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 21 |
| PubMed broad count | 168 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MINT1, X11 |

**关键文献**:
1. Discovery of obesity genes through cross-ancestry analysis.. *Nature communications*. PMID: 41168175
2. CASK, APBA1, and STXBP1 collaborate during insulin secretion.. *Molecular and cellular endocrinology*. PMID: 33159991
3. Obesity and the Genome: Emerging Insights from Studies in 2024 and 2025.. *Genes*. PMID: 41009961
4. Protein-truncating variants in BSN are associated with severe adult-onset obesity, type 2 diabetes and fatty liver disease.. *Nature genetics*. PMID: 38575728
5. Genomic organization and promoter cloning of the human X11α gene APBA1.. *DNA and cell biology*. PMID: 22136355

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.0 |
| 高置信度残基 (pLDDT>90) 占比 | 12.1% |
| 置信残基 (pLDDT 70-90) 占比 | 28.2% |
| 中等置信 (pLDDT 50-70) 占比 | 9.7% |
| 低置信 (pLDDT<50) 占比 | 50.1% |
| 有序区域 (pLDDT>70) 占比 | 40.3% |
| 可用 PDB 条目 | 1AQC, 1U37, 1U38, 1U39, 1U3B, 1X11, 1X45, 1Y7N |

**PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。**

**评价**: AlphaFold 预测质量有限（pLDDT=59.0），有序残基占 40.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051230, IPR001478, IPR036034, IPR011993, IPR006020; Pfam: PF00595, PF00640 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CASK | 0.999 | 0.976 | — |
| APP | 0.998 | 0.980 | — |
| STXBP1 | 0.995 | 0.864 | — |
| LIN7A | 0.992 | 0.218 | — |
| LIN7C | 0.981 | 0.645 | — |
| KIF17 | 0.977 | 0.000 | — |
| LIN7B | 0.925 | 0.456 | — |
| NRXN1 | 0.913 | 0.076 | — |
| STX1A | 0.874 | 0.573 | — |
| GRIN2B | 0.860 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000265381.3 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| Kcnj12 | psi-mi:"MI:0096"(pull down) | pubmed:15024025 |
| APP | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:8887653 |
| secA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| Stxbp1 | psi-mi:"MI:0018"(two hybrid) | pubmed:9395480|imex:IM-20161 |
| Stx1a | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:9395480|imex:IM-20161 |
| grcA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| PSEN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:11083918|imex:IM-20841 |
| inaD | psi-mi:"MI:0053"(fluorescence polarization spectro | pubmed:21703451|imex:IM-16552 |
| LIN7C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.0 + PDB: 1AQC, 1U37, 1U38, 1U39, 1U3B,  | pLDDT=59.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm, perinuclear region; Nucleus; / Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ 

**核心优势**:
1. APBA1 — Amyloid-beta A4 precursor protein-binding family A member 1，非常新颖，仅有少数基础研究。
2. 蛋白大小837 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 21 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=59.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q02410
- Protein Atlas: https://www.proteinatlas.org/ENSG00000107282-APBA1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=APBA1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q02410
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 02:58:10

HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。
