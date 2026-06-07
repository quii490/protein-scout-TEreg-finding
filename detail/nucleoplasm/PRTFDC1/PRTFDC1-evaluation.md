---
type: protein-evaluation
gene: "PRTFDC1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PRTFDC1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PRTFDC1 / HHGP |
| 蛋白名称 | Phosphoribosyltransferase domain-containing protein 1 |
| 蛋白大小 | 225 aa / 25.7 kDa |
| UniProt ID | Q9NRG1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Golgi apparatus, Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 225 aa / 25.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=18 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=90.7; PDB: 2JBH |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR050408, IPR005904, IPR029057, IPR000836; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **127.0/180** | |
| **归一化总分** | | | **70.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Golgi apparatus, Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 18 |
| PubMed broad count | 22 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HHGP |

**关键文献**:
1. Phosphoribosyl transferase domain containing 1: A prognostic biomarker in testicular germ cell tumors.. *Molecular therapy. Oncology*. PMID: 40241724
2. Epigenetic modifications and transgenerational inheritance in women victims of violence (EWVV).. *Environmental epigenetics*. PMID: 41070359
3. Gene duplication and inactivation in the HPRT gene family.. *Genomics*. PMID: 16928426
4. Histone acetyltransferase inhibition reverses opacity in rat galactose-induced cataract.. *PloS one*. PMID: 36417410
5. Structural and functional studies of the human phosphoribosyltransferase domain containing protein 1.. *The FEBS journal*. PMID: 21054786

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.7 |
| 高置信度残基 (pLDDT>90) 占比 | 77.8% |
| 置信残基 (pLDDT 70-90) 占比 | 13.8% |
| 中等置信 (pLDDT 50-70) 占比 | 4.0% |
| 低置信 (pLDDT<50) 占比 | 4.4% |
| 有序区域 (pLDDT>70) 占比 | 91.6% |
| 可用 PDB 条目 | 2JBH |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=90.7，有序区 91.6%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050408, IPR005904, IPR029057, IPR000836; Pfam: PF00156 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ADSL | 0.870 | 0.000 | — |
| RRM1 | 0.860 | 0.000 | — |
| HPRT1 | 0.837 | 0.830 | — |
| ATP5F1C | 0.837 | 0.000 | — |
| ATP5F1A | 0.825 | 0.000 | — |
| MT-ATP6 | 0.816 | 0.000 | — |
| EEF2KMT | 0.792 | 0.792 | — |
| MTAP | 0.731 | 0.071 | — |
| PNP | 0.730 | 0.069 | — |
| WDR90 | 0.708 | 0.708 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EEF2KMT | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| DTNB | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| STAT5A | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| HPRT1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| EWSR1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| NIF3L1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| FLAD1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| LRRK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31046837|imex:IM-26684 |
| SIK1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TCL1A | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.7 + PDB: 2JBH | pLDDT=90.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Golgi apparatus, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. PRTFDC1 — Phosphoribosyltransferase domain-containing protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小225 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 18 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NRG1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000099256-PRTFDC1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PRTFDC1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NRG1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000099256-PRTFDC1/subcellular

![](https://images.proteinatlas.org/21458/263_A4_1_red_green.jpg)
![](https://images.proteinatlas.org/21458/263_A4_2_red_green.jpg)
![](https://images.proteinatlas.org/21458/264_A4_1_red_green.jpg)
![](https://images.proteinatlas.org/21458/264_A4_2_red_green.jpg)
![](https://images.proteinatlas.org/21458/277_A4_1_red_green.jpg)
![](https://images.proteinatlas.org/21458/277_A4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NRG1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NRG1 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR050408;IPR005904;IPR029057;IPR000836; |
| Pfam | PF00156; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000099256-PRTFDC1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| HPRT1 | Intact, Biogrid | true |
| CNRIP1 | Intact | false |
| EEF2KMT | Intact | false |
| EPM2AIP1 | Intact | false |
| FLAD1 | Intact | false |
| GNPDA1 | Intact | false |
| LGALS9B | Intact | false |
| LNX1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
