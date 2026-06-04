---
type: protein-evaluation
gene: "CRABP2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CRABP2 — REJECTED (研究热度过高 (PubMed strict=243，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CRABP2 |
| 蛋白名称 | Cellular retinoic acid-binding protein 2 |
| 蛋白大小 | 138 aa / 15.7 kDa |
| UniProt ID | P29373 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Cytoplasm; Endoplasmic reticulum; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 138 aa / 15.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=243 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=96.7; PDB: 1BLR, 1BM5, 1CBQ, 1CBS, 1XCA, 2CBS, 2FR3 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR012674, IPR000463, IPR031259, IPR000566; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Supported |
| UniProt | Cytoplasm; Endoplasmic reticulum; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- endoplasmic reticulum (GO:0005783)
- extracellular exosome (GO:0070062)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 243 |
| PubMed broad count | 293 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Dual Role of CRABP2 in Colorectal Cancer: Oncogenesis via Nuclear RB1 and Cytoplasmic AFG3L2/SLC25A39 Axis, While Limiting Liver Metastasis through Cytoplasmic AFG3L2/PINK1/Parkin-Mediated Mitophagy.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 40305785
2. GRPR Drives Metastasis via CRABP2 and FNDC4 Pathways in Lung Adenocarcinoma.. *Cells*. PMID: 39768218
3. Prognostic role of CRABP2 in lung cancer: a meta-analysis.. *Journal of cardiothoracic surgery*. PMID: 38915108
4. CRABP2 promotes metastasis and lipid droplet accumulation in non-small cell lung cancer by downregulating PLAAT4.. *Journal of Cancer*. PMID: 40657374
5. CRABP2 promotes peritoneal metastasis in CRC through TGF-β/Smad-mediated EMT signaling and invadopodia formation.. *Cellular signalling*. PMID: 40505846

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 96.7 |
| 高置信度残基 (pLDDT>90) 占比 | 97.8% |
| 置信残基 (pLDDT 70-90) 占比 | 2.2% |
| 中等置信 (pLDDT 50-70) 占比 | 0.0% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 100.0% |
| 可用 PDB 条目 | 1BLR, 1BM5, 1CBQ, 1CBS, 1XCA, 2CBS, 2FR3, 2FRS, 2FS6, 2FS7 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1BLR, 1BM5, 1CBQ, 1CBS, 1XCA, 2CBS, 2FR3, 2FRS, 2FS6, 2FS7）+ AlphaFold极高置信度预测（pLDDT=96.7），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR012674, IPR000463, IPR031259, IPR000566; Pfam: PF00061 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RARB | 0.967 | 0.050 | — |
| RARG | 0.941 | 0.050 | — |
| RARA | 0.902 | 0.050 | — |
| RXRA | 0.821 | 0.050 | — |
| S100A13 | 0.754 | 0.000 | — |
| PLAAT4 | 0.753 | 0.000 | — |
| PLAAT3 | 0.748 | 0.000 | — |
| PBRM1 | 0.744 | 0.000 | — |
| CCND3 | 0.742 | 0.425 | — |
| RARS1 | 0.742 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| LRRK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31046837|imex:IM-26684 |
| RAB5A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| FLAD1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CCND3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ACTN2 | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-25511|pubmed:25910212 |
| CDK15 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| UGT1A10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GDF5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FCF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DDX19B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=96.7 + PDB: 1BLR, 1BM5, 1CBQ, 1CBS, 1XCA,  | pLDDT=96.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Endoplasmic reticulum; Nucleus / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CRABP2 — Cellular retinoic acid-binding protein 2，研究基础较多，新颖性有限。
2. 蛋白大小138 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 243 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 243 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P29373
- Protein Atlas: https://www.proteinatlas.org/ENSG00000143320-CRABP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CRABP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P29373
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
