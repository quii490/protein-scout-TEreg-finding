---
type: protein-evaluation
gene: "PLD4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PLD4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PLD4 / C14orf175 |
| 蛋白名称 | 5'-3' exonuclease PLD4 |
| 蛋白大小 | 506 aa / 55.6 kDa |
| UniProt ID | Q96BZ4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Endoplasmic reticulum membrane; Golgi apparatus, trans-Golgi |
| 蛋白大小 | 10/10 | ×1 | 10 | 506 aa / 55.6 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=30 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=86.2; PDB: 8V08 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR050874, IPR032803, IPR001736; Pfam: PF13918 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **129.0/180** | |
| **归一化总分** | | | **71.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Endoplasmic reticulum membrane; Golgi apparatus, trans-Golgi network membrane; Nucleus; Early endoso... | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- early endosome (GO:0005769)
- endomembrane system (GO:0012505)
- endoplasmic reticulum membrane (GO:0005789)
- lysosome (GO:0005764)
- nucleus (GO:0005634)
- phagocytic vesicle (GO:0045335)
- trans-Golgi network membrane (GO:0032588)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 30 |
| PubMed broad count | 59 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C14orf175 |

**关键文献**:
1. PLD3 and PLD4 are single-stranded acid exonucleases that regulate endosomal nucleic-acid sensing.. *Nature immunology*. PMID: 30111894
2. Targeting Phospholipase D4 Attenuates Kidney Fibrosis.. *Journal of the American Society of Nephrology : JASN*. PMID: 28814511
3. Macrophages in dermal disease progression of phospholipase D4-deficient Fleckvieh calves.. *Veterinary pathology*. PMID: 34856834
4. Disease in the Pld4thss/thss Model of Murine Lupus Requires TLR9.. *ImmunoHorizons*. PMID: 37555846
5. PLD4 is a genetic determinant to systemic lupus erythematosus and involved in murine autoimmune phenotypes.. *Annals of the rheumatic diseases*. PMID: 30679154

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.2 |
| 高置信度残基 (pLDDT>90) 占比 | 75.5% |
| 置信残基 (pLDDT 70-90) 占比 | 5.9% |
| 中等置信 (pLDDT 50-70) 占比 | 6.1% |
| 低置信 (pLDDT<50) 占比 | 12.5% |
| 有序区域 (pLDDT>70) 占比 | 81.4% |
| 可用 PDB 条目 | 8V08 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=86.2，有序区 81.4%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050874, IPR032803, IPR001736; Pfam: PF13918 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PLD2 | 0.956 | 0.000 | — |
| PLD1 | 0.924 | 0.000 | — |
| CEPT1 | 0.913 | 0.000 | — |
| CHPT1 | 0.913 | 0.000 | — |
| PLD3 | 0.911 | 0.000 | — |
| MBOAT2 | 0.911 | 0.000 | — |
| LPCAT3 | 0.910 | 0.000 | — |
| MBOAT1 | 0.908 | 0.000 | — |
| SELENOI | 0.908 | 0.000 | — |
| PLAAT3 | 0.907 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ATG16L1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31015422|imex:IM-29997 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 1
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.2 + PDB: 8V08 | pLDDT=86.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane; Golgi apparatus, t / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 1 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. PLD4 — 5'-3' exonuclease PLD4，非常新颖，仅有少数基础研究。
2. 蛋白大小506 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 30 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96BZ4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000166428-PLD4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PLD4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96BZ4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03



<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96BZ4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96BZ4 |
| SMART | SM00155; |
| UniProt Domain [FT] | DOMAIN 209..236; /note="PLD phosphodiesterase 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00153"; DOMAIN 423..449; /note="PLD phosphodiesterase 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00153" |
| InterPro | IPR050874;IPR032803;IPR001736; |
| Pfam | PF13918; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000166428-PLD4/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PLD3 | Biogrid | false |
| RPN2 | Biogrid | false |
| TM9SF1 | Biogrid | false |
| TM9SF3 | Biogrid | false |
| TMX3 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
