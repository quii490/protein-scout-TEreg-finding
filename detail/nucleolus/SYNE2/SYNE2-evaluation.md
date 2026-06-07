---
type: protein-evaluation
gene: "SYNE2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SYNE2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SYNE2 / KIAA1011, NUA |
| 蛋白名称 | Nesprin-2 |
| 蛋白大小 | 6885 aa / 796.4 kDa |
| UniProt ID | Q8WXH0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear membrane, Intermediate filaments; 额外: Primary cilium; UniProt: Nucleus outer membrane; Sarcoplasmic reticulum membrane; Cel |
| 蛋白大小 | 0/10 | ×1 | 0 | 6885 aa / 796.4 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=71 篇 (≤80→4) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=83.3; PDB: 4DXS, 4FI9, 6XF1 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001589, IPR001715, IPR036872, IPR012315, IPR018 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **103.0/180** | |
| **归一化总分** | | | **57.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear membrane, Intermediate filaments; 额外: Primary cilium | Approved |
| UniProt | Nucleus outer membrane; Sarcoplasmic reticulum membrane; Cell membrane; Cytoplasm, cytoskeleton; Mit... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cilium (GO:0005929)
- cytoplasm (GO:0005737)
- extracellular exosome (GO:0070062)
- fibrillar center (GO:0001650)
- filopodium membrane (GO:0031527)
- focal adhesion (GO:0005925)
- intermediate filament cytoskeleton (GO:0045111)
- lamellipodium membrane (GO:0031258)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 71 |
| PubMed broad count | 190 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1011, NUA |

**关键文献**:
1. Emery-Dreifuss Muscular Dystrophy.. **. PMID: 20301609
2. Emery-Dreifuss muscular dystrophy.. *Handbook of clinical neurology*. PMID: 21496632
3. EGFR and SYNE2 are associated with p21 expression and SYNE2 variants predict post-operative clinical outcomes in HBV-related hepatocellular carcinoma.. *Scientific reports*. PMID: 27502069
4. Profibrotic Molecules Are Reduced in CRISPR-Edited Emery-Dreifuss Muscular Dystrophy Fibroblasts.. *Cells*. PMID: 40940734
5. ENO1-related gene signature predicts prognosis and therapeutic response in diffuse large B-cell lymphoma.. *Frontiers in immunology*. PMID: 41208958

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.3 |
| 高置信度残基 (pLDDT>90) 占比 | 59.2% |
| 置信残基 (pLDDT 70-90) 占比 | 18.7% |
| 中等置信 (pLDDT 50-70) 占比 | 11.2% |
| 低置信 (pLDDT<50) 占比 | 10.9% |
| 有序区域 (pLDDT>70) 占比 | 77.9% |
| 可用 PDB 条目 | 4DXS, 4FI9, 6XF1 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（4DXS, 4FI9, 6XF1）+ AlphaFold高质量预测（pLDDT=83.3），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001589, IPR001715, IPR036872, IPR012315, IPR018159; Pfam: PF00307, PF10541, PF00435 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SUN2 | 0.999 | 0.976 | — |
| SUN1 | 0.999 | 0.452 | — |
| EMD | 0.995 | 0.330 | — |
| LMNA | 0.994 | 0.313 | — |
| FHOD1 | 0.994 | 0.926 | — |
| SYNE1 | 0.966 | 0.000 | — |
| LMNB1 | 0.963 | 0.070 | — |
| SYNE3 | 0.945 | 0.101 | — |
| TMEM67 | 0.933 | 0.292 | — |
| SUN3 | 0.835 | 0.091 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| APPL1 | psi-mi:"MI:0813"(proximity ligation assay) | pubmed:23414517|imex:IM-16425 |
| ABI1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| SLX4IP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12200|pubmed:19596235 |
| HDAC11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-18733|pubmed:23752268 |
| SUN2 | psi-mi:"MI:0096"(pull down) | pubmed:22632968|imex:IM-17371 |
| SUN1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:22632968|imex:IM-17371 |
| Mycbp2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28671696|doi:10.1038/nn |
| COL23A1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| STXBP3 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.3 + PDB: 4DXS, 4FI9, 6XF1 | pLDDT=83.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus outer membrane; Sarcoplasmic reticulum mem / Nuclear membrane, Intermediate filaments; 额外: Prim | 一致 |
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
1. SYNE2 — Nesprin-2，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小6885 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 71 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WXH0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000054654-SYNE2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SYNE2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WXH0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear membrane (uncertain)。来源: https://www.proteinatlas.org/ENSG00000054654-SYNE2/subcellular

![](https://images.proteinatlas.org/50204/2149_B2_38_blue_red_green.jpg)
![](https://images.proteinatlas.org/50204/2149_B2_58_blue_red_green.jpg)
![](https://images.proteinatlas.org/50204/2161_D6_20_blue_red_green.jpg)
![](https://images.proteinatlas.org/50204/2161_D6_25_blue_red_green.jpg)
![](https://images.proteinatlas.org/50204/2176_H6_14_blue_red_green.jpg)
![](https://images.proteinatlas.org/50204/2176_H6_56_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8WXH0 |
| SMART | SM00033;SM01249;SM00150; |
| UniProt Domain [FT] | DOMAIN 31..136; /note="Calponin-homology (CH) 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00044"; DOMAIN 181..286; /note="Calponin-homology (CH) 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00044"; DOMAIN 6826..6885; /note="KASH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00385" |
| InterPro | IPR001589;IPR001715;IPR036872;IPR012315;IPR018159;IPR002017;IPR057057;IPR056887; |
| Pfam | PF00307;PF10541;PF00435;PF25034;PF25035; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000054654-SYNE2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| APPL1 | Intact, Biogrid | true |
| SUN2 | Intact, Biogrid | true |
| BCAP31 | Biogrid | false |
| BIN1 | Biogrid | false |
| BRAP | Biogrid | false |
| CDC37 | Biogrid | false |
| CTNNB1 | Biogrid | false |
| EFTUD2 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
