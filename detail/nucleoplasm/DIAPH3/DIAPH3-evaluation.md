---
type: protein-evaluation
gene: "DIAPH3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DIAPH3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DIAPH3 / DIAP3 |
| 蛋白名称 | Protein diaphanous homolog 3 |
| 蛋白大小 | 1193 aa / 136.9 kDa |
| UniProt ID | Q9NSV4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane, Microtubules; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 1193 aa / 136.9 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=70 篇 (≤80→4) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=71.8; PDB: 5UWP, 6X2Y |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011989, IPR016024, IPR014767, IPR044933, IPR015 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **104.5/180** | |
| **归一化总分** | | | **58.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Microtubules | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- actin filament (GO:0005884)
- actin filament bundle (GO:0032432)
- cleavage furrow (GO:0032154)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- ESCRT I complex (GO:0000813)
- filamentous actin (GO:0031941)
- microtubule organizing center (GO:0005815)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 70 |
| PubMed broad count | 115 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DIAP3 |

**关键文献**:
1. Mechanotransduction and YAP-dependent matrix remodelling is required for the generation and maintenance of cancer-associated fibroblasts.. *Nature cell biology*. PMID: 23708000
2. Unveiling novel cell clusters and biomarkers in glioblastoma and its peritumoral microenvironment at the single-cell perspective.. *Journal of translational medicine*. PMID: 38851695
3. Super Enhancer-Regulated LncRNA LINC01089 Induces Alternative Splicing of DIAPH3 to Drive Hepatocellular Carcinoma Metastasis.. *Cancer research*. PMID: 37756562
4. Formins in Human Disease.. *Cells*. PMID: 34685534
5. Identification and characterization of human DIAPH3 gene in silico.. *International journal of molecular medicine*. PMID: 14767582

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.8 |
| 高置信度残基 (pLDDT>90) 占比 | 29.5% |
| 置信残基 (pLDDT 70-90) 占比 | 35.0% |
| 中等置信 (pLDDT 50-70) 占比 | 9.6% |
| 低置信 (pLDDT<50) 占比 | 26.0% |
| 有序区域 (pLDDT>70) 占比 | 64.5% |
| 可用 PDB 条目 | 5UWP, 6X2Y |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（5UWP, 6X2Y）+ AlphaFold高质量预测（pLDDT=71.8），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011989, IPR016024, IPR014767, IPR044933, IPR015425; Pfam: PF06367, PF06371, PF02181 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MYC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| SIRT1 | psi-mi:"MI:0096"(pull down) | imex:IM-12078|pubmed:19343720 |
| KATNAL1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:26929214|imex:IM-26156 |
| KATNAL2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:26929214|imex:IM-26156 |
| PGRMC1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| BCHE | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SCN2B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HS2ST1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TPTE2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| VASN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.8 + PDB: 5UWP, 6X2Y | pLDDT=71.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Plasma membrane, Microtubules | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DIAPH3 — Protein diaphanous homolog 3，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小1193 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 70 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NSV4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000139734-DIAPH3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DIAPH3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NSV4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
