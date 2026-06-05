---
type: protein-evaluation
gene: "DLGAP5"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DLGAP5 — REJECTED (研究热度过高 (PubMed strict=204，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DLGAP5 / DLG7, KIAA0008 |
| 蛋白名称 | Disks large-associated protein 5 |
| 蛋白大小 | 846 aa / 95.1 kDa |
| UniProt ID | Q15398 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Mitotic spindle; UniProt: Nucleus; Cytoplasm; Cytoplasm, cytoskeleton, spindle |
| 蛋白大小 | 8/10 | ×1 | 8 | 846 aa / 95.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=204 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=55.6; PDB: 7ZX4, 8X9P, 9DHZ, 9DUQ |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR005026; Pfam: PF03359 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **79.5/180** | |
| **归一化总分** | | | **44.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Mitotic spindle | Supported |
| UniProt | Nucleus; Cytoplasm; Cytoplasm, cytoskeleton, spindle | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- mitotic spindle (GO:0072686)
- nucleus (GO:0005634)
- spindle pole centrosome (GO:0031616)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 204 |
| PubMed broad count | 271 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DLG7, KIAA0008 |

**关键文献**:
1. DLGAP5 promotes lung adenocarcinoma growth via upregulating PLK1 and serves as a therapeutic target.. *Journal of translational medicine*. PMID: 38414025
2. DLGAP5 enhances bladder cancer chemoresistance by regulating glycolysis through MYC stabilization.. *Theranostics*. PMID: 39990228
3. Differentially Expressed Genes Associated with the Development of Cervical Cancer.. *International journal of molecular sciences*. PMID: 41516135
4. DLGAP5 facilitates glioblastoma growth and tumor-associated macrophage M2 polarization.. *Journal of molecular histology*. PMID: 40944860
5. Biallelic variants in DLGAP5 cause spindle assembly defects and human early embryonic arrest.. *Human reproduction (Oxford, England)*. PMID: 40796344

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 55.6 |
| 高置信度残基 (pLDDT>90) 占比 | 16.4% |
| 置信残基 (pLDDT 70-90) 占比 | 11.0% |
| 中等置信 (pLDDT 50-70) 占比 | 11.8% |
| 低置信 (pLDDT<50) 占比 | 60.8% |
| 有序区域 (pLDDT>70) 占比 | 27.4% |
| 可用 PDB 条目 | 7ZX4, 8X9P, 9DHZ, 9DUQ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=55.6），有序残基占 27.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR005026; Pfam: PF03359 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HMMR | 0.999 | 0.072 | — |
| CEP55 | 0.999 | 0.000 | — |
| KIF11 | 0.997 | 0.000 | — |
| ASPM | 0.994 | 0.000 | — |
| BUB1 | 0.986 | 0.000 | — |
| MELK | 0.982 | 0.000 | — |
| CDC20 | 0.981 | 0.000 | — |
| BUB1B | 0.981 | 0.000 | — |
| PBK | 0.979 | 0.000 | — |
| TPX2 | 0.978 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TRAF2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TRIM37 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| FRMD8P1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H2BC9 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| RCN1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| GOLGA2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| B2M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KPNB1 | psi-mi:"MI:0096"(pull down) | pubmed:28330616|imex:IM-25671 |
| CORO1C | psi-mi:"MI:0096"(pull down) | pubmed:28330616|imex:IM-25671 |
| NEMP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=55.6 + PDB: 7ZX4, 8X9P, 9DHZ, 9DUQ | pLDDT=55.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Cytoplasm, cytoskeleton, spind / Cytosol; 额外: Mitotic spindle | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. DLGAP5 — Disks large-associated protein 5，研究基础较多，新颖性有限。
2. 蛋白大小846 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 204 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=55.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 204 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q15398
- Protein Atlas: https://www.proteinatlas.org/ENSG00000126787-DLGAP5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DLGAP5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q15398
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000126787-DLGAP5/subcellular

![](https://images.proteinatlas.org/71028/1840_B3_62_blue_red_green.jpg)
![](https://images.proteinatlas.org/71028/1840_B3_63_blue_red_green.jpg)
![](https://images.proteinatlas.org/71028/1973_F11_31_blue_red_green.jpg)
![](https://images.proteinatlas.org/71028/1973_F11_32_blue_red_green.jpg)
![](https://images.proteinatlas.org/71028/2087_G6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/71028/2087_G6_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q15398-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
