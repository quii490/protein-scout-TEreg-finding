---
type: protein-evaluation
gene: "SEPTIN12"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SEPTIN12 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SEPTIN12 / SEPT12 |
| 蛋白名称 | Septin-12 |
| 蛋白大小 | 358 aa / 40.7 kDa |
| UniProt ID | Q8IYM1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Microtubules; 额外: Annulus; UniProt: Cytoplasm; Cytoplasm, cytoskeleton; Cytoplasm, cytoskeleton, |
| 蛋白大小 | 10/10 | ×1 | 10 | 358 aa / 40.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=15 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=81.4; PDB: 6MQ9, 6MQB, 6MQK, 6MQL |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR030379, IPR027417, IPR016491; Pfam: PF00735 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **143.0/180** | |
| **归一化总分** | | | **79.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Microtubules; 额外: Annulus | Supported |
| UniProt | Cytoplasm; Cytoplasm, cytoskeleton; Cytoplasm, cytoskeleton, spindle; Nucleus; Cell projection, cili... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cell division site (GO:0032153)
- cleavage furrow (GO:0032154)
- microtubule cytoskeleton (GO:0015630)
- midbody (GO:0030496)
- nucleus (GO:0005634)
- perinuclear region of cytoplasm (GO:0048471)
- septin complex (GO:0031105)
- septin ring (GO:0005940)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed broad count | 34 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SEPT12 |

**关键文献**:
1. SUN5 interacts with nuclear membrane LaminB1 and cytoskeletal GTPase Septin12 mediating the sperm head-and-tail junction.. *Molecular human reproduction*. PMID: 38870534
2. Evaluation of an Updated Gene Panel as a Diagnostic Tool for Both Male and Female Infertility.. *Reproductive sciences (Thousand Oaks, Calif.)*. PMID: 38664359
3. Regulation of septin phosphorylation: SEPT12 phosphorylation in sperm septin assembly.. *Cytoskeleton (Hoboken, N.J.)*. PMID: 30160375
4. SEPT12-microtubule complexes are required for sperm head and tail formation.. *International journal of molecular sciences*. PMID: 24213608
5. SEPTIN12 genetic variants confer susceptibility to teratozoospermia.. *PloS one*. PMID: 22479503

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.4 |
| 高置信度残基 (pLDDT>90) 占比 | 57.0% |
| 置信残基 (pLDDT 70-90) 占比 | 19.8% |
| 中等置信 (pLDDT 50-70) 占比 | 6.7% |
| 低置信 (pLDDT<50) 占比 | 16.5% |
| 有序区域 (pLDDT>70) 占比 | 76.8% |
| 可用 PDB 条目 | 6MQ9, 6MQB, 6MQK, 6MQL |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（6MQ9, 6MQB, 6MQK, 6MQL）+ AlphaFold高质量预测（pLDDT=81.4），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR030379, IPR027417, IPR016491; Pfam: PF00735 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SEPTIN4 | 0.997 | 0.905 | — |
| SEPTIN7 | 0.992 | 0.913 | — |
| SEPTIN2 | 0.991 | 0.899 | — |
| SEPTIN6 | 0.989 | 0.871 | — |
| SEPTIN5 | 0.988 | 0.921 | — |
| SEPTIN11 | 0.986 | 0.835 | — |
| SEPTIN1 | 0.957 | 0.883 | — |
| SEPTIN3 | 0.953 | 0.832 | — |
| SEPTIN9 | 0.939 | 0.000 | — |
| SEPTIN10 | 0.937 | 0.833 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SEPTIN14 | psi-mi:"MI:0018"(two hybrid) | pubmed:17922164|imex:IM-20117 |
| SEPTIN6 | psi-mi:"MI:0096"(pull down) | pubmed:18047794|imex:IM-19278 |
| SEPTIN5 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| SEPTIN1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| SEPTIN7 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| RSPH14 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SEPTIN4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SEPTIN2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CCT6B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SEPTIN8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.4 + PDB: 6MQ9, 6MQB, 6MQK, 6MQL | pLDDT=81.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm, cytoskeleton; Cytoplasm, cyt / Microtubules; 额外: Annulus | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. SEPTIN12 — Septin-12，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小358 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 15 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IYM1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000140623-SEPTIN12/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SEPTIN12
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IYM1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
