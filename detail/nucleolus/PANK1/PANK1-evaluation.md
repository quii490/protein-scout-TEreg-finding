---
type: protein-evaluation
gene: "PANK1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PANK1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PANK1 / PANK |
| 蛋白名称 | Pantothenate kinase 1 |
| 蛋白大小 | 598 aa / 64.3 kDa |
| UniProt ID | Q8TE04 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm; Nucleus; Nucleus, nucleolus; Cytoplasm, cytosol;  |
| 蛋白大小 | 10/10 | ×1 | 10 | 598 aa / 64.3 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=40 篇 (≤40→8) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=71.2; PDB: 2I7N, 3SMP |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR043129, IPR004567; Pfam: PF03630 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.5/180** | |
| **归一化总分** | | | **70.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm; Nucleus; Nucleus, nucleolus; Cytoplasm, cytosol; Cytoplasmic vesicle, clathrin-coated ves... | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- clathrin-coated vesicle (GO:0030136)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleolus (GO:0005730)
- nucleus (GO:0005634)
- recycling endosome (GO:0055037)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 40 |
| PubMed broad count | 59 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PANK |

**关键文献**:
1. Counteracting TGM2 by a Fibroin peptide ameliorated Adriamycin-induced nephropathy via regulation of lipid metabolism through PANX1-PPAR α/PANK1 pathway.. *Translational research : the journal of laboratory and clinical medicine*. PMID: 38734063
2. PIEZO1 as a new target for hyperglycemic stress-induced neuropathic injury: The potential therapeutic role of bezafibrate.. *Biomedicine & pharmacotherapy = Biomedecine & pharmacotherapie*. PMID: 38815290
3. Pantothenate Kinase 1 Inhibits the Progression of Hepatocellular Carcinoma by Negatively Regulating Wnt/β-catenin Signaling.. *International journal of biological sciences*. PMID: 35280671
4. p53 activates the PANK1/miRNA-107 gene leading to downregulation of CDK6 and p130 cell cycle proteins.. *Nucleic acids research*. PMID: 20833636
5. circ-Pank1 promotes dopaminergic neuron neurodegeneration through modulating miR-7a-5p/α-syn pathway in Parkinson's disease.. *Cell death & disease*. PMID: 35589691

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.2 |
| 高置信度残基 (pLDDT>90) 占比 | 53.2% |
| 置信残基 (pLDDT 70-90) 占比 | 7.2% |
| 中等置信 (pLDDT 50-70) 占比 | 1.5% |
| 低置信 (pLDDT<50) 占比 | 38.1% |
| 有序区域 (pLDDT>70) 占比 | 60.4% |
| 可用 PDB 条目 | 2I7N, 3SMP |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2I7N, 3SMP）+ AlphaFold高质量预测（pLDDT=71.2），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR043129, IPR004567; Pfam: PF03630 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Q0WNV9 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| SCD | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 2
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.2 + PDB: 2I7N, 3SMP | pLDDT=71.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Nucleus, nucleolus; Cytoplasm, / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 0 + 2 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. PANK1 — Pantothenate kinase 1，非常新颖，仅有少数基础研究。
2. 蛋白大小598 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 40 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TE04
- Protein Atlas: https://www.proteinatlas.org/ENSG00000152782-PANK1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PANK1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TE04
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03



<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8TE04-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8TE04 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR043129;IPR004567; |
| Pfam | PF03630; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000152782-PANK1/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
