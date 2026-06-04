---
type: protein-evaluation
gene: "PELI1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PELI1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PELI1 / PRISM |
| 蛋白名称 | E3 ubiquitin-protein ligase pellino homolog 1 |
| 蛋白大小 | 418 aa / 46.3 kDa |
| UniProt ID | Q96FA3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nucleoli, Basal body; 额外: Intermediate filament; UniProt: Chromosome |
| 蛋白大小 | 10/10 | ×1 | 10 | 418 aa / 46.3 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=89 篇 (≤100→2) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=89.5; PDB: 9IF9 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR006800, IPR048334, IPR048335; Pfam: PF04710, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **99.0/180** | |
| **归一化总分** | | | **55.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli, Basal body; 额外: Intermediate filaments, Centriolar satellite, Centrosome, Cytosol | Supported |
| UniProt | Chromosome | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleus (GO:0005634)
- site of double-strand break (GO:0035861)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 89 |
| PubMed broad count | 196 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PRISM |

**关键文献**:
1. Microglial exosomes facilitate α-synuclein transmission in Parkinson's disease.. *Brain : a journal of neurology*. PMID: 32355963
2. Pellino-1 promotes intrinsic activation of skin-resident IL-17A-producing T cells in psoriasis.. *The Journal of allergy and clinical immunology*. PMID: 36646143
3. HNF4α ubiquitination mediated by Peli1 impairs FAO and accelerates pressure overload-induced myocardial hypertrophy.. *Cell death & disease*. PMID: 38346961
4. Peli1 Deficiency in Macrophages Attenuates Pulmonary Hypertension by Enhancing Foxp1-Mediated Transcriptional Inhibition of IL-6.. *Hypertension (Dallas, Tex. : 1979)*. PMID: 39618410
5. Role of the Peli1-RIPK1 Signaling Axis in Methamphetamine-Induced Neuroinflammation.. *ACS chemical neuroscience*. PMID: 36763609

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.5 |
| 高置信度残基 (pLDDT>90) 占比 | 74.6% |
| 置信残基 (pLDDT 70-90) 占比 | 15.1% |
| 中等置信 (pLDDT 50-70) 占比 | 6.2% |
| 低置信 (pLDDT<50) 占比 | 4.1% |
| 有序区域 (pLDDT>70) 占比 | 89.7% |
| 可用 PDB 条目 | 9IF9 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=89.5，有序区 89.7%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR006800, IPR048334, IPR048335; Pfam: PF04710, PF20723 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| IRAK1 | 0.998 | 0.885 | — |
| IRAK4 | 0.995 | 0.838 | — |
| TRAF6 | 0.987 | 0.735 | — |
| RIPK1 | 0.976 | 0.535 | — |
| TRADD | 0.955 | 0.000 | — |
| RIPK3 | 0.907 | 0.328 | — |
| UBE2V1 | 0.855 | 0.516 | — |
| SMAD6 | 0.827 | 0.292 | — |
| UBE2N | 0.821 | 0.302 | — |
| TBK1 | 0.821 | 0.535 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| IRAK1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:12496252 |
| TRAF6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:12496252 |
| IRAK4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:12496252 |
| SRPK2 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:23602568|imex:IM-17935 |
| SRPK1 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:23602568|imex:IM-17935 |
| TANK | psi-mi:"MI:2289"(virotrap) | pubmed:30561431|imex:IM-26500 |
| DISC1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| LCN2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| RIMS4 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| LMNA | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.5 + PDB: 9IF9 | pLDDT=89.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Chromosome / Nucleoplasm, Nucleoli, Basal body; 额外: Intermediat | 一致 |
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
1. PELI1 — E3 ubiquitin-protein ligase pellino homolog 1，研究基础较多，新颖性有限。
2. 蛋白大小418 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 89 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96FA3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000197329-PELI1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PELI1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96FA3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
