---
type: protein-evaluation
gene: "ASCC3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ASCC3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ASCC3 / HELIC1, RQT2 |
| 蛋白名称 | Activating signal cointegrator 1 complex subunit 3 |
| 蛋白大小 | 2202 aa / 251.5 kDa |
| UniProt ID | Q8N3C0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Golgi apparatus; UniProt: Nucleus; Nucleus speckle; Cytoplasm, cytosol |
| 蛋白大小 | 2/10 | ×1 | 2 | 2202 aa / 251.5 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=25 篇 (≤40→8) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=79.7; PDB: 6YXQ, 8ALZ |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR003593, IPR058856, IPR035892, IPR011545, IPR050 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **122.0/180** | |
| **归一化总分** | | | **67.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Golgi apparatus | Supported |
| UniProt | Nucleus; Nucleus speckle; Cytoplasm, cytosol | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- cytosolic ribosome (GO:0022626)
- DNA repair complex (GO:1990391)
- membrane (GO:0016020)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- RQC-trigger complex (GO:0180022)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 25 |
| PubMed broad count | 51 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HELIC1, RQT2 |

**关键文献**:
1. ASCC3 promotes the immunosuppression and progression of non-small cell lung cancer by impairing the type I interferon response via CAND1-mediated ubiquitination inhibition of STAT3.. *Journal for immunotherapy of cancer*. PMID: 38148115
2. The ASC-1 Complex Disassembles Collided Ribosomes.. *Molecular cell*. PMID: 32579943
3. Ribosomal collision is not a prerequisite for ZNF598-mediated ribosome ubiquitination and disassembly of ribosomal complexes by ASCC.. *Nucleic acids research*. PMID: 38366554
4. Extended DNA threading through a dual-engine motor module of the activating signal co-integrator 1 complex.. *Nature communications*. PMID: 37019967
5. Identification of biomarker associated with Trop2 in breast cancer: implication for targeted therapy.. *Discover oncology*. PMID: 39240479

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.7 |
| 高置信度残基 (pLDDT>90) 占比 | 27.2% |
| 置信残基 (pLDDT 70-90) 占比 | 53.8% |
| 中等置信 (pLDDT 50-70) 占比 | 10.1% |
| 低置信 (pLDDT<50) 占比 | 8.9% |
| 有序区域 (pLDDT>70) 占比 | 81.0% |
| 可用 PDB 条目 | 6YXQ, 8ALZ |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（6YXQ, 8ALZ）+ AlphaFold高质量预测（pLDDT=79.7），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003593, IPR058856, IPR035892, IPR011545, IPR050474; Pfam: PF26582, PF00270, PF00271 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TRIP4 | 0.999 | 0.844 | — |
| ASCC2 | 0.999 | 0.987 | — |
| ASCC1 | 0.999 | 0.834 | — |
| ALKBH3 | 0.978 | 0.840 | — |
| PRPF8 | 0.894 | 0.777 | — |
| ZNF598 | 0.878 | 0.374 | — |
| PRPF6 | 0.844 | 0.777 | — |
| SNW1 | 0.843 | 0.782 | — |
| CDC5L | 0.833 | 0.781 | — |
| XAB2 | 0.831 | 0.782 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| EIF3H | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| OTUD6B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| G3BP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| G3BP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| SUMO3 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:17000644|imex:IM-19940 |
| Q81LD1 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| CAND1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| ASCC2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LRRK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31046837|imex:IM-26684 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.7 + PDB: 6YXQ, 8ALZ | pLDDT=79.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus speckle; Cytoplasm, cytosol / Cytosol; 额外: Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. ASCC3 — Activating signal cointegrator 1 complex subunit 3，非常新颖，仅有少数基础研究。
2. 蛋白大小2202 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 25 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N3C0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000112249-ASCC3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ASCC3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N3C0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
