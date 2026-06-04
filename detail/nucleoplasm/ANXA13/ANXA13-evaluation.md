---
type: protein-evaluation
gene: "ANXA13"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ANXA13 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ANXA13 / ANX13 |
| 蛋白名称 | Annexin A13 |
| 蛋白大小 | 316 aa / 35.4 kDa |
| UniProt ID | P27216 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane; 额外: Nucleoplasm; UniProt: Apical cell membrane; Cell membrane; Cytoplasmic vesicle |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 316 aa / 35.4 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=19 篇 (≤20→10) |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=94.8; PDB: 6B3I |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001464, IPR018502, IPR018252, IPR037104, IPR009 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 13 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **139.0/180** | |
| **归一化总分 (÷1.83)** | | | **74.9/100******** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane; 额外: Nucleoplasm | Supported |
| UniProt | Apical cell membrane; Cell membrane; Cytoplasmic vesicle | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA IF 图像状态: if_display_images_available。

**GO Cellular Component**:
- apical plasma membrane (GO:0016324)
- basolateral plasma membrane (GO:0016323)
- cytoplasm (GO:0005737)
- cytoplasmic vesicle (GO:0031410)
- exocytic vesicle (GO:0070382)
- extracellular exosome (GO:0070062)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 19 |
| PubMed broad count | 28 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ANX13 |

**关键文献**:
1. ANXA13 promotes cell proliferation and invasion and attenuates apoptosis in renal cell carcinoma.. *Heliyon*. PMID: 37520951
2. Intracellular Transport of Ribosome-Inactivating Proteins Depends on Annexin 13.. *Doklady. Biochemistry and biophysics*. PMID: 33119820
3. Annexins induce curvature on free-edge membranes displaying distinct morphologies.. *Scientific reports*. PMID: 29985397
4. ANXA13 expression patterns in hepatocellular carcinoma and impact on tumor behavior.. *World journal of gastrointestinal surgery*. PMID: 41178894
5. Annexin A13 predicts poor prognosis for lung adenocarcinoma patients and accelerates the proliferation and migration of lung adenocarcinoma cells by modulating epithelial-mesenchymal transition.. *Fundamental & clinical pharmacology*. PMID: 32145097

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.8 |
| 高置信度残基 (pLDDT>90) 占比 | 91.1% |
| 置信残基 (pLDDT 70-90) 占比 | 5.1% |
| 中等置信 (pLDDT 50-70) 占比 | 0.9% |
| 低置信 (pLDDT<50) 占比 | 2.8% |
| 有序区域 (pLDDT>70) 占比 | 96.2% |
| 可用 PDB 条目 | 6B3I |

**PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。**

**评价**: AlphaFold 极高置信度预测（pLDDT=94.8，有序区 96.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001464, IPR018502, IPR018252, IPR037104, IPR009166; Pfam: PF00191 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CSMD3 | 0.837 | 0.059 | — |
| EXT1 | 0.747 | 0.000 | — |
| TRPS1 | 0.727 | 0.000 | — |
| ANXA2 | 0.643 | 0.554 | — |
| APBB1IP | 0.566 | 0.566 | — |
| MSI2 | 0.485 | 0.471 | — |
| CDH17 | 0.446 | 0.000 | — |
| DEUP1 | 0.418 | 0.418 | — |
| DYSF | 0.416 | 0.061 | — |
| ANXA5 | 0.413 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Chuk | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Actg1 | psi-mi:"MI:0276"(blue native page) | imex:IM-11844|pubmed:17205597 |
| Acta1 | psi-mi:"MI:0276"(blue native page) | imex:IM-11844|pubmed:17205597 |
| Abcg3 | psi-mi:"MI:0276"(blue native page) | imex:IM-11844|pubmed:17205597 |
| DEUP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ANXA2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| APBB1IP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SRPRA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TUBGCP3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MSI2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 13，IntAct interactions: 15
- 调控相关比例: 0 / 13 = 0%

**评价**: STRING 13 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.8 + PDB: 6B3I | pLDDT=94.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Apical cell membrane; Cell membrane; Cytoplasmic v / Plasma membrane; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 13 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐ 

**核心优势**:
1. ANXA13 — Annexin A13，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小316 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 19 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P27216
- Protein Atlas: https://www.proteinatlas.org/ENSG00000104537-ANXA13/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ANXA13
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P27216
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 02:53:56

HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。
