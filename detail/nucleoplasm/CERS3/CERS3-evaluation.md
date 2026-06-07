---
type: protein-evaluation
gene: "CERS3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation, E-batch]
status: scored
---

## CERS3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CERS3 / LASS3 |
| 蛋白名称 | Ceramide synthase 3 |
| 蛋白大小 | 383 aa / 46.3 kDa |
| UniProt ID | Q8IU89 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Endoplasmic reticulum membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 383 aa / 46.3 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=45 篇 |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=87.3; PDB: 暂无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001356, IPR009057, IPR016439, IPR006634; Pfam: PF00046, PF03798 |
| PPI 网络 | 10/10 | ×3 | 30 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.2 | AlphaFold 结构预测: +0.25 |
| **原始总分** | | | **158.2/180** | |
| **归一化总分 (÷1.83)** | | | **86.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Endoplasmic reticulum membrane | ECO:0000250

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- endoplasmic reticulum (GO:0005783) [ISS:UniProtKB]
- endoplasmic reticulum membrane (GO:0005789) [TAS:Reactome]

**结论**: HPA: Nucleoplasm; UniProt: Endoplasmic reticulum membrane

#### 3.2 蛋白大小评估

**评价**: 383 aa / 46.3 kDa，大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 45 |
| PubMed 搜索链接 | [CERS3 PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=CERS3) |

**关键文献**:
暂无文献记录。

**评价**: 较新颖，研究关注度低。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.3 |
| 高置信度残基 (pLDDT>90) 占比 | 67.1% |
| 置信残基 (pLDDT 70-90) 占比 | 19.1% |
| 中等置信 (pLDDT 50-70) 占比 | 10.2% |
| 低置信 (pLDDT<50) 占比 | 3.7% |
| 有序区域 (pLDDT>70) 占比 | 86.19999999999999% |
| 可用 PDB 条目 | 暂无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001356, IPR009057, IPR016439, IPR006634; Pfam: PF00046, PF03798 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SGMS1 | 0.975 | 0.000 | — |
| KDSR | 0.969 | 0.000 | — |
| ACER1 | 0.965 | 0.115 | — |
| DEGS1 | 0.965 | 0.071 | — |
| UGCG | 0.964 | 0.000 | — |
| DEGS2 | 0.963 | 0.071 | — |
| ASAH1 | 0.960 | 0.068 | — |
| SMPD1 | 0.959 | 0.000 | — |
| ACER2 | 0.958 | 0.115 | — |
| CERK | 0.957 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PCBD2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ORMDL3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| EBI-2857623 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| SLC39A9 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| NEU1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| Q8NEN6 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SSUH2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278|doi:10.1016/j.cell.2021.04.011 |
| AKR1B10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278|doi:10.1016/j.cell.2021.04.011 |
| C3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278|doi:10.1016/j.cell.2021.04.011 |
| IGKC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278|doi:10.1016/j.cell.2021.04.011 |

**PPI 互证分析**:
STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0/15。

**评价**: STRING + IntAct 双源 PPI 数据充分。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold | pLDDT=87.3, v6 | 预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane / Nucleoplasm | 部分一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- AlphaFold 结构预测: +0.25
- 单库核定位证据: +0.25
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5

**总分**: +1.2 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐⭐

**归一化总分**: 86.5/100

**核心优势**:
1. CERS3 — Ceramide synthase 3，较新颖，PubMed 45 篇。
2. 蛋白大小383 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。
3. AlphaFold pLDDT=87.3，结构预测质量高。

**风险/不确定性**:
1. 功能研究较少，具体调控机制待阐明

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IU89
- Protein Atlas: https://www.proteinatlas.org/search/CERS3
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CERS3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IU89
- STRING: https://string-db.org/network/9606.CERS3
- Packet data timestamp: 2026-06-03 04:51:23

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000154227-CERS3/subcellular

![](https://images.proteinatlas.org/24356/1791_E2_3_red_green.jpg)
![](https://images.proteinatlas.org/24356/1791_E2_4_red_green.jpg)
![](https://images.proteinatlas.org/24356/195_C12_1_red_green.jpg)
![](https://images.proteinatlas.org/24356/195_C12_2_red_green.jpg)
![](https://images.proteinatlas.org/24356/196_C12_1_red_green.jpg)
![](https://images.proteinatlas.org/24356/196_C12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IU89-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8IU89 |
| SMART | SM00389;SM00724; |
| UniProt Domain [FT] | DOMAIN 130..331; /note="TLC"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00205" |
| InterPro | IPR001356;IPR009057;IPR016439;IPR006634; |
| Pfam | PF00046;PF03798; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000154227-CERS3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| A2ML1 | Bioplex | false |
| AKR1B10 | Bioplex | false |
| ANXA8 | Bioplex | false |
| C3 | Bioplex | false |
| CALML5 | Bioplex | false |
| CBR1 | Bioplex | false |
| DSG3 | Bioplex | false |
| EVPL | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
