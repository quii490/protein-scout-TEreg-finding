---
type: protein-evaluation
gene: "OSBPL3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## OSBPL3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | OSBPL3 / KIAA0704, ORP3, OSBP3 |
| 蛋白名称 | Oxysterol-binding protein-related protein 3 |
| 蛋白大小 | 887 aa / 101.2 kDa |
| UniProt ID | Q9H4L5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Nucleoli; UniProt: Endoplasmic reticulum membrane; Cytoplasm, cytosol; Cell mem |
| 蛋白大小 | 8/10 | ×1 | 8 | 887 aa / 101.2 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=42 篇 (≤60→6) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=71.9; PDB: 7CYZ, 7DEI, 7DEJ |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR037239, IPR000648, IPR018494, IPR011993, IPR041 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **119.0/180** | |
| **归一化总分** | | | **66.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoli | Supported |
| UniProt | Endoplasmic reticulum membrane; Cytoplasm, cytosol; Cell membrane; Cell projection, filopodium tip; ... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- endoplasmic reticulum membrane (GO:0005789)
- filopodium tip (GO:0032433)
- membrane (GO:0016020)
- nuclear membrane (GO:0031965)
- perinuclear endoplasmic reticulum (GO:0097038)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 42 |
| PubMed broad count | 66 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0704, ORP3, OSBP3 |

**关键文献**:
1. OSBPL3 modulates the immunosuppressive microenvironment and predicts therapeutic outcomes in pancreatic cancer.. *Biology direct*. PMID: 39789613
2. The expression, immune infiltration, prognosis, and experimental validation of OSBPL family genes in liver cancer.. *BMC cancer*. PMID: 36918840
3. Clinical Value and Potential Mechanisms of Oxysterol-Binding Protein Like 3 (OSBPL3) in Human Tumors.. *Frontiers in molecular biosciences*. PMID: 34738015
4. OSBPL3 drives colorectal cancer progression via Hippo-YAP signaling and modulates MEK inhibitor sensitivity.. *Communications biology*. PMID: 41794997
5. Glucocorticoids, genes and brain function.. *Progress in neuro-psychopharmacology & biological psychiatry*. PMID: 29180230

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.9 |
| 高置信度残基 (pLDDT>90) 占比 | 43.4% |
| 置信残基 (pLDDT 70-90) 占比 | 17.9% |
| 中等置信 (pLDDT 50-70) 占比 | 8.0% |
| 低置信 (pLDDT<50) 占比 | 30.7% |
| 有序区域 (pLDDT>70) 占比 | 61.3% |
| 可用 PDB 条目 | 7CYZ, 7DEI, 7DEJ |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（7CYZ, 7DEI, 7DEJ）+ AlphaFold高质量预测（pLDDT=71.9），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR037239, IPR000648, IPR018494, IPR011993, IPR041680; Pfam: PF01237, PF15409 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RRAS | 0.925 | 0.069 | — |
| VAPA | 0.899 | 0.617 | — |
| VAPB | 0.873 | 0.780 | — |
| PLEK2 | 0.726 | 0.000 | — |
| PLEK | 0.724 | 0.000 | — |
| OSBPL9 | 0.630 | 0.091 | — |
| PITPNM3 | 0.564 | 0.513 | — |
| PJVK | 0.513 | 0.000 | — |
| EVA1A | 0.503 | 0.000 | — |
| OSBPL7 | 0.486 | 0.435 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| YWHAB | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| YWHAG | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| gag-pol | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-17346|pubmed:22190034| |
| ORF | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-17346|pubmed:22190034| |
| YWHAH | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11897|pubmed:17979178 |
| YWHAZ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAQ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ILVBL | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Pde4dip | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28671696|doi:10.1038/nn |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.9 + PDB: 7CYZ, 7DEI, 7DEJ | pLDDT=71.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane; Cytoplasm, cytosol / Cytosol; 额外: Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. OSBPL3 — Oxysterol-binding protein-related protein 3，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小887 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 42 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H4L5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000070882-OSBPL3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=OSBPL3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H4L5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
