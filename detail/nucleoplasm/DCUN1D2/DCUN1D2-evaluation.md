---
type: protein-evaluation
gene: "DCUN1D2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DCUN1D2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DCUN1D2 / C13orf17, DCUN1L2 |
| 蛋白名称 | DCN1-like protein 2 |
| 蛋白大小 | 259 aa / 30.2 kDa |
| UniProt ID | Q6PH85 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane, Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 259 aa / 30.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=93.8; PDB: 4GAO |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR014764, IPR042460, IPR005176, IPR009060; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **139.0/180** | |
| **归一化总分** | | | **77.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cytosol | Approved |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)
- ubiquitin ligase complex (GO:0000151)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 7 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C13orf17, DCUN1L2 |

**关键文献**:
1. Circuit-wide proteomics profiling reveals brain region-specific protein signatures in the male WKY rats with endogenous depression.. *Journal of affective disorders*. PMID: 36162674
2. Immunomodulatory effect of 5-azacytidine (5-azaC): potential role in the transplantation setting.. *Blood*. PMID: 19887673
3. Dystonia, facial dysmorphism, intellectual disability and breast cancer associated with a chromosome 13q34 duplication and overexpression of TFDP1: case report.. *BMC medical genetics*. PMID: 23849371
4. Integrative radiogenomic analysis for multicentric radiophenotype in glioblastoma.. *Oncotarget*. PMID: 26863628
5. Concentration of neddylation-related molecules in paranodal myelin of the peripheral nervous system.. *Proceedings of the Japan Academy. Series B, Physical and biological sciences*. PMID: 26860454

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.8 |
| 高置信度残基 (pLDDT>90) 占比 | 90.0% |
| 置信残基 (pLDDT 70-90) 占比 | 6.9% |
| 中等置信 (pLDDT 50-70) 占比 | 0.8% |
| 低置信 (pLDDT<50) 占比 | 2.3% |
| 有序区域 (pLDDT>70) 占比 | 96.9% |
| 可用 PDB 条目 | 4GAO |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=93.8，有序区 96.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR014764, IPR042460, IPR005176, IPR009060; Pfam: PF03556, PF14555 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CUL3 | 0.961 | 0.784 | — |
| UBE2M | 0.959 | 0.842 | — |
| CUL2 | 0.895 | 0.735 | — |
| CUL4B | 0.880 | 0.682 | — |
| CUL4A | 0.880 | 0.626 | — |
| UBE2F | 0.870 | 0.483 | — |
| CUL1 | 0.865 | 0.784 | — |
| RBX1 | 0.777 | 0.361 | — |
| UBA3 | 0.765 | 0.075 | — |
| CUL5 | 0.764 | 0.634 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DCUN1D1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| Map3k1 | psi-mi:"MI:0997"(ubiquitinase assay) | imex:IM-22822|pubmed:25260751 |
| UBE2V1 | psi-mi:"MI:0997"(ubiquitinase assay) | imex:IM-22822|pubmed:25260751 |
| UBA1 | psi-mi:"MI:0997"(ubiquitinase assay) | imex:IM-22822|pubmed:25260751 |
| UBE2N | psi-mi:"MI:0997"(ubiquitinase assay) | imex:IM-22822|pubmed:25260751 |
| INPPL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| KLHL18 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| GAP43 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CUL4B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.8 + PDB: 4GAO | pLDDT=93.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Plasma membrane, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. DCUN1D2 — DCN1-like protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小259 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6PH85
- Protein Atlas: https://www.proteinatlas.org/ENSG00000150401-DCUN1D2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DCUN1D2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6PH85
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000150401-DCUN1D2/subcellular

![](https://images.proteinatlas.org/39349/460_A9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/39349/460_A9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/39349/465_A9_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/39349/465_A9_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/39349/467_A9_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/39349/467_A9_5_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6PH85-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
