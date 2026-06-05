---
type: protein-evaluation
gene: "HRAS"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## HRAS — REJECTED (研究热度过高 (PubMed strict=3563，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HRAS / HRAS1 |
| 蛋白名称 | GTPase HRas |
| 蛋白大小 | 189 aa / 21.3 kDa |
| UniProt ID | P01112 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Nucleoplasm, Basal body; UniProt: Cell membrane; Golgi apparatus; Golgi apparatus membrane; Nu |
| 蛋白大小 | 8/10 | ×1 | 8 | 189 aa / 21.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=3563 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=91.9; PDB: 121P, 1AA9, 1AGP, 1BKD, 1CLU, 1CRP, 1CRQ |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR027417, IPR005225, IPR001806, IPR020849; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm, Basal body | Supported |
| UniProt | Cell membrane; Golgi apparatus; Golgi apparatus membrane; Nucleus; Cytoplasm; Cytoplasm, perinuclear... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- ciliary basal body (GO:0036064)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- endoplasmic reticulum membrane (GO:0005789)
- glutamatergic synapse (GO:0098978)
- Golgi apparatus (GO:0005794)
- Golgi membrane (GO:0000139)
- GTPase complex (GO:1905360)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3563 |
| PubMed broad count | 8610 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HRAS1 |

**关键文献**:
1. ZDHHC18 promotes renal fibrosis development by regulating HRAS palmitoylation.. *The Journal of clinical investigation*. PMID: 39913299
2. The Spectrum of Spitz Melanocytic Lesions: From Morphologic Diagnosis to Molecular Classification.. *Frontiers in oncology*. PMID: 35747831
3. Comprehensive Molecular Characterization of Pheochromocytoma and Paraganglioma.. *Cancer cell*. PMID: 28162975
4. Costello syndrome: Clinical phenotype, genotype, and management guidelines.. *American journal of medical genetics. Part A*. PMID: 31222966
5. Overexpression of wild-type HRAS drives non-alcoholic steatohepatitis to hepatocellular carcinoma in mice.. *Zoological research*. PMID: 38757223

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.9 |
| 高置信度残基 (pLDDT>90) 占比 | 78.3% |
| 置信残基 (pLDDT 70-90) 占比 | 13.8% |
| 中等置信 (pLDDT 50-70) 占比 | 3.2% |
| 低置信 (pLDDT<50) 占比 | 4.8% |
| 有序区域 (pLDDT>70) 占比 | 92.1% |
| 可用 PDB 条目 | 121P, 1AA9, 1AGP, 1BKD, 1CLU, 1CRP, 1CRQ, 1CRR, 1CTQ, 1GNP |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（121P, 1AA9, 1AGP, 1BKD, 1CLU, 1CRP, 1CRQ, 1CRR, 1CTQ, 1GNP）+ AlphaFold极高置信度预测（pLDDT=91.9），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027417, IPR005225, IPR001806, IPR020849; Pfam: PF00071 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RALGDS | 0.999 | 0.989 | — |
| SOS1 | 0.999 | 0.991 | — |
| RAF1 | 0.999 | 0.999 | — |
| RASSF5 | 0.999 | 0.971 | — |
| BRAF | 0.999 | 0.921 | — |
| RASA1 | 0.999 | 0.982 | — |
| AFDN | 0.998 | 0.966 | — |
| PIK3CG | 0.998 | 0.950 | — |
| PIK3CA | 0.995 | 0.758 | — |
| RASGRF1 | 0.995 | 0.323 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000488757.1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:35839996|imex:IM-30494 |
| RAF1 | psi-mi:"MI:0018"(two hybrid) | pubmed:8670882|mint:MINT-52210 |
| Rabac1 | psi-mi:"MI:0018"(two hybrid) | pubmed:11335720|imex:IM-26228 |
| BRAP | psi-mi:"MI:0096"(pull down) | pubmed:14724641 |
| Fnta | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:15451670 |
| SHOC2 | psi-mi:"MI:0096"(pull down) | imex:IM-14435|pubmed:16301319 |
| Rapgef4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-14526|pubmed:16316996 |
| RASA1 | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:9219684|mint:MINT-52215 |
| Ralgds | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:9628477 |
| SOS1 | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:9690470|mint:MINT-65480 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.9 + PDB: 121P, 1AA9, 1AGP, 1BKD, 1CLU,  | pLDDT=91.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane; Golgi apparatus; Golgi apparatus me / Cytosol; 额外: Nucleoplasm, Basal body | 一致 |
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
1. HRAS — GTPase HRas，研究基础较多，新颖性有限。
2. 蛋白大小189 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 3563 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 3563 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P01112
- Protein Atlas: https://www.proteinatlas.org/ENSG00000174775-HRAS/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HRAS
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P01112
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000174775-HRAS/subcellular

![](https://images.proteinatlas.org/70222/2244_B12_19_blue_red_green.jpg)
![](https://images.proteinatlas.org/70222/2244_B12_7_blue_red_green.jpg)
![](https://images.proteinatlas.org/72761/2266_D12_185_blue_red_green.jpg)
![](https://images.proteinatlas.org/72761/2266_D12_61_blue_red_green.jpg)
![](https://images.proteinatlas.org/70222/1357_B12_1_red_green.jpg)
![](https://images.proteinatlas.org/70222/1357_B12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P01112-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
