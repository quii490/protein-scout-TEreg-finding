---
type: protein-evaluation
gene: "TPRG1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TPRG1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TPRG1 / FAM79B |
| 蛋白名称 | Tumor protein p63-regulated gene 1 protein |
| 蛋白大小 | 275 aa / 31.2 kDa |
| UniProt ID | Q6ZUI0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 275 aa / 31.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=18 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=73.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR034753, IPR022158, IPR040242; Pfam: PF12456 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 5 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.5/180** | |
| **归一化总分** | | | **67.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 18 |
| PubMed broad count | 26 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FAM79B |

**关键文献**:
1. TPRG1-AS1 induces RBM24 expression and inhibits liver cancer progression by sponging miR-4691-5p and miR-3659.. *Liver international : official journal of the International Association for the Study of the Liver*. PMID: 34328265
2. Tumor protein P63 Regulated 1 contributes to inflammation and cell proliferation of cystitis glandularis through regulating the NF-кB/cyclooxygenase-2/prostaglandin E2 axis.. *Bosnian journal of basic medical sciences*. PMID: 34998360
3. Long Noncoding RNA TPRG1-AS1 Suppresses Migration of Vascular Smooth Muscle Cells and Attenuates Atherogenesis via Interacting With MYH9 Protein.. *Arteriosclerosis, thrombosis, and vascular biology*. PMID: 36172865
4. Novel loci for triglyceride/HDL-C ratio longitudinal change among subjects without T2D.. *Journal of lipid research*. PMID: 39557295
5. CCND1-associated ceRNA network reveal the critical pathway of TPRG1-AS1-hsa-miR-363-3p-MYO1B as a prognostic marker for head and neck squamous cell carcinoma.. *Scientific reports*. PMID: 37481637

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.7 |
| 高置信度残基 (pLDDT>90) 占比 | 34.2% |
| 置信残基 (pLDDT 70-90) 占比 | 26.5% |
| 中等置信 (pLDDT 50-70) 占比 | 20.4% |
| 低置信 (pLDDT<50) 占比 | 18.9% |
| 有序区域 (pLDDT>70) 占比 | 60.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=73.7，有序区 60.7%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR034753, IPR022158, IPR040242; Pfam: PF12456 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SRSF8 | 0.542 | 0.414 | — |
| TMEM120A | 0.535 | 0.535 | — |
| TP63 | 0.520 | 0.000 | — |
| SRSF2 | 0.520 | 0.414 | — |
| C9orf135 | 0.403 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TMX2 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| HSD17B13 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CGRRF1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TMEM120A | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CIDEB | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SLC10A6 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| RHBDD2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SCN3B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| HSD17B11 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| EBAG9 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 5，IntAct interactions: 15
- 调控相关比例: 0 / 5 = 0%

**评价**: STRING 5 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.7 + PDB: 无 | pLDDT=73.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 5 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TPRG1 — Tumor protein p63-regulated gene 1 protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小275 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 18 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6ZUI0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000188001-TPRG1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TPRG1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6ZUI0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000188001-TPRG1/subcellular

![](https://images.proteinatlas.org/44751/1396_B10_2_red_green.jpg)
![](https://images.proteinatlas.org/44751/1396_B10_3_red_green.jpg)
![](https://images.proteinatlas.org/44751/526_F5_1_red_green.jpg)
![](https://images.proteinatlas.org/44751/526_F5_2_red_green.jpg)
![](https://images.proteinatlas.org/44751/528_F5_1_red_green.jpg)
![](https://images.proteinatlas.org/44751/528_F5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6ZUI0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6ZUI0 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 68..240; /note="hSac2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01127" |
| InterPro | IPR034753;IPR022158;IPR040242; |
| Pfam | PF12456; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000188001-TPRG1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| APOC1 | Intact | false |
| APOC4 | Intact | false |
| AQP6 | Intact | false |
| CCR1 | Bioplex | false |
| CGRRF1 | Intact | false |
| CIDEB | Intact | false |
| EBAG9 | Intact | false |
| HSD17B11 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
