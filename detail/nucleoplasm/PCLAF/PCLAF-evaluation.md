---
type: protein-evaluation
gene: "PCLAF"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PCLAF 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PCLAF / KIAA0101, NS5ATP9, PAF |
| 蛋白名称 | PCNA-associated factor |
| 蛋白大小 | 111 aa / 12.0 kDa |
| UniProt ID | Q15004 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Centrosome; UniProt: Nucleus; Cytoplasm, perinuclear region |
| 蛋白大小 | 8/10 | ×1 | 8 | 111 aa / 12.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=31 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.1; PDB: 4D2G, 6EHT, 6GWS, 6IIW |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR040444, IPR031444; Pfam: PF15715 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 7 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **119.5/180** | |
| **归一化总分** | | | **66.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Centrosome | Supported |
| UniProt | Nucleus; Cytoplasm, perinuclear region | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- centrosome (GO:0005813)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- perinuclear region of cytoplasm (GO:0048471)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 31 |
| PubMed broad count | 132 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0101, NS5ATP9, PAF |

**关键文献**:
1. Dysregulated NF-κB signal promotes the hub gene PCLAF expression to facilitate nasopharyngeal carcinoma proliferation and metastasis.. *Biomedicine & pharmacotherapy = Biomedecine & pharmacotherapie*. PMID: 32070873
2. PCNA-associated factor (KIAA0101/PCLAF) overexpression and gene copy number alterations in hepatocellular carcinoma tissues.. *BMC cancer*. PMID: 33743635
3. NUSAP1 and PCLAF (KIA0101) Downregulation by Neoadjuvant Therapy is Associated with Better Therapeutic Outcomes and Survival in Breast Cancer.. *Journal of oncology*. PMID: 36478748
4. Cancer-Associated Fibroblast-Derived GDF15 Induces Oxidative Stress and Neutrophil Infiltration in Head and Neck Squamous Cell Carcinoma through the PI3K/AKT/STAT3 Axis Cascade.. *Research (Washington, D.C.)*. PMID: 41035818
5. Clathrin Light Chain B Drives Hepatocellular Carcinoma Progression Through Dual Mechanisms: Small Extracellular Vesicle-Mediated Angiogenesis and the NF-κB-PCLAF Signaling Axis.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 40820941

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.1 |
| 高置信度残基 (pLDDT>90) 占比 | 9.9% |
| 置信残基 (pLDDT 70-90) 占比 | 17.1% |
| 中等置信 (pLDDT 50-70) 占比 | 58.6% |
| 低置信 (pLDDT<50) 占比 | 14.4% |
| 有序区域 (pLDDT>70) 占比 | 27.0% |
| 可用 PDB 条目 | 4D2G, 6EHT, 6GWS, 6IIW |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=65.1），有序残基占 27.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR040444, IPR031444; Pfam: PF15715 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PCNA | 0.997 | 0.988 | — |
| UBE2C | 0.938 | 0.292 | — |
| BIRC5 | 0.930 | 0.000 | — |
| TOP2A | 0.920 | 0.000 | — |
| ING1 | 0.915 | 0.292 | — |
| NUSAP1 | 0.914 | 0.000 | — |
| ZWINT | 0.913 | 0.000 | — |
| ASPM | 0.909 | 0.000 | — |
| RRM2 | 0.907 | 0.000 | — |
| CENPF | 0.898 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CDKN1A | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| PCNA | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TERF1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| FANCM | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| EPB41L4B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| IL1R2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 7
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 7 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.1 + PDB: 4D2G, 6EHT, 6GWS, 6IIW | pLDDT=65.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, perinuclear region / Centrosome | 一致 |
| PPI | STRING + IntAct | 15 + 7 interactions | 数据充分 |

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
1. PCLAF — PCNA-associated factor，非常新颖，仅有少数基础研究。
2. 蛋白大小111 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 31 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=65.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q15004
- Protein Atlas: https://www.proteinatlas.org/ENSG00000166803-PCLAF/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PCLAF
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q15004
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
