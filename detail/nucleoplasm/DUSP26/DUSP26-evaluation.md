---
type: protein-evaluation
gene: "DUSP26"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DUSP26 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DUSP26 / DUSP24, LDP4, MKP8, NATA1, SKRP3 |
| 蛋白名称 | Dual specificity protein phosphatase 26 |
| 蛋白大小 | 211 aa / 23.9 kDa |
| UniProt ID | Q9BV47 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Cytoplasm; Nucleus; Golgi apparatus |
| 蛋白大小 | 10/10 | ×1 | 10 | 211 aa / 23.9 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=39 篇 (≤40→8) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=84.3; PDB: 2E0T, 4B04, 4HRF, 5GTJ |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR020405, IPR000340, IPR029021, IPR016130, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 14 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **132.5/180** | |
| **归一化总分** | | | **73.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Cytoplasm; Nucleus; Golgi apparatus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- extracellular exosome (GO:0070062)
- Golgi apparatus (GO:0005794)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 39 |
| PubMed broad count | 58 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DUSP24, LDP4, MKP8, NATA1, SKRP3 |

**关键文献**:
1. A Review of DUSP26: Structure, Regulation and Relevance in Human Disease.. *International journal of molecular sciences*. PMID: 33466673
2. Dual-Specificity Phosphatase 26 Protects Against Cardiac Hypertrophy Through TAK1.. *Journal of the American Heart Association*. PMID: 33522247
3. Overexpression of DUSP26 gene suppressed the proliferation, migration, and invasion of human prostate cancer cells.. *Experimental cell research*. PMID: 39222869
4. Protein phosphatase Dusp26 associates with KIF3 motor and promotes N-cadherin-mediated cell-cell adhesion.. *Oncogene*. PMID: 19043453
5. Dusp26 phosphatase regulates mitochondrial respiration and oxidative stress and protects neuronal cell death.. *Cellular and molecular life sciences : CMLS*. PMID: 35313355

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.3 |
| 高置信度残基 (pLDDT>90) 占比 | 67.8% |
| 置信残基 (pLDDT 70-90) 占比 | 11.4% |
| 中等置信 (pLDDT 50-70) 占比 | 2.8% |
| 低置信 (pLDDT<50) 占比 | 18.0% |
| 有序区域 (pLDDT>70) 占比 | 79.2% |
| 可用 PDB 条目 | 2E0T, 4B04, 4HRF, 5GTJ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2E0T, 4B04, 4HRF, 5GTJ）+ AlphaFold高质量预测（pLDDT=84.3），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR020405, IPR000340, IPR029021, IPR016130, IPR000387; Pfam: PF00782 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| AK2 | 0.698 | 0.000 | — |
| HSF4 | 0.631 | 0.292 | — |
| RNF122 | 0.497 | 0.000 | — |
| PMPCA | 0.464 | 0.072 | — |
| TP53 | 0.462 | 0.297 | — |
| AFG3L2 | 0.438 | 0.072 | — |
| PTPN3 | 0.429 | 0.071 | — |
| PTS | 0.420 | 0.000 | — |
| NPAS4 | 0.420 | 0.000 | — |
| DUSP23 | 0.413 | 0.083 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 14，IntAct interactions: 0
- 调控相关比例: 0 / 14 = 0%

**评价**: STRING 14 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.3 + PDB: 2E0T, 4B04, 4HRF, 5GTJ | pLDDT=84.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Golgi apparatus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 14 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DUSP26 — Dual specificity protein phosphatase 26，非常新颖，仅有少数基础研究。
2. 蛋白大小211 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 39 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BV47
- Protein Atlas: https://www.proteinatlas.org/ENSG00000133878-DUSP26/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DUSP26
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BV47
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000133878-DUSP26/subcellular

![](https://images.proteinatlas.org/18221/112_G12_1_red_green.jpg)
![](https://images.proteinatlas.org/18221/112_G12_2_red_green.jpg)
![](https://images.proteinatlas.org/18221/1430_E8_2_red_green.jpg)
![](https://images.proteinatlas.org/18221/1430_E8_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BV47-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
