---
type: protein-evaluation
gene: "CDPF1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation, E-batch]
status: scored
---

## CDPF1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CDPF1 / C22orf40 |
| 蛋白名称 | Cysteine-rich DPF motif domain-containing protein 1 |
| 蛋白大小 | 123 aa / 13.9 kDa |
| UniProt ID | Q6NVV7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Cytosol; 额外: Nucleoplasm; UniProt: — |
| 蛋白大小 | 8/10 | ×1 | 8 | 123 aa / 13.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=1 篇 |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=87.1; PDB: 暂无 |
| 调控结构域 | 6/10 | ×2 | 12 | InterPro: IPR042426, IPR018785; Pfam: PF10170 |
| PPI 网络 | 7/10 | ×3 | 21 | STRING 5 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.2 | AlphaFold 结构预测: +0.25 |
| **原始总分** | | | **135.2/180** | |
| **归一化总分 (÷1.83)** | | | **73.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Approved |
| UniProt | — | — |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- 无 GO-CC 数据

**结论**: HPA: Cytosol; 额外: Nucleoplasm; UniProt: —

#### 3.2 蛋白大小评估

**评价**: 123 aa / 13.9 kDa，大小适合大部分生化实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1 |
| PubMed 搜索链接 | [CDPF1 PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=CDPF1) |

**关键文献**:
暂无文献记录。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.1 |
| 高置信度残基 (pLDDT>90) 占比 | 66.7% |
| 置信残基 (pLDDT 70-90) 占比 | 16.3% |
| 中等置信 (pLDDT 50-70) 占比 | 13.0% |
| 低置信 (pLDDT<50) 占比 | 4.1% |
| 有序区域 (pLDDT>70) 占比 | 83.0% |
| 可用 PDB 条目 | 暂无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR042426, IPR018785; Pfam: PF10170 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PKDREJ | 0.614 | 0.000 | — |
| ATXN10 | 0.536 | 0.000 | — |
| ZNF691 | 0.485 | 0.000 | — |
| OXLD1 | 0.485 | 0.000 | — |
| WNT7B | 0.457 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| hflK | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| HDAC4 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| ENKD1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| FAM221A | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| VGLL3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| KCTD9 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TFAP2D | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CATSPER1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| FRS3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| DDIT4L | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
STRING 5 个预测互作，IntAct 15 个实验互作。调控相关配体占比 1/5。

**评价**: PPI 数据中等。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold | pLDDT=87.1, v6 | 预测 |
| 定位 | UniProt + HPA | — / Cytosol | 部分一致 |
| PPI | STRING + IntAct | 5 + 15 interactions | 数据有限 |

**互证加分明细**:
- AlphaFold 结构预测: +0.25
- 单库核定位证据: +0.25
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5

**总分**: +1.2 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐⭐

**归一化总分**: 73.9/100

**核心优势**:
1. CDPF1 — Cysteine-rich DPF motif domain-containing protein 1，极度新颖，几乎未被系统研究（PubMed 1 篇）。
2. 蛋白大小123 aa，适合大部分生化实验。
3. AlphaFold pLDDT=87.1，结构预测质量高。

**风险/不确定性**:
1. 核定位信号较弱，多源数据支持有限。
2. PubMed 1 篇，研究基础极有限，功能注释不完整

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] Co-IP/MS 实验鉴定互作伙伴

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6NVV7
- Protein Atlas: https://www.proteinatlas.org/search/CDPF1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CDPF1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6NVV7
- STRING: https://string-db.org/network/9606.CDPF1
- Packet data timestamp: 2026-06-03 04:45:27

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000205643-CDPF1/subcellular

![](https://images.proteinatlas.org/18823/149_E6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/18823/149_E6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/18823/150_E6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/18823/150_E6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/18823/151_E6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/18823/151_E6_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6NVV7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6NVV7 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR042426;IPR018785; |
| Pfam | PF10170; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000205643-CDPF1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BHLHE40 | Intact | false |
| CATSPER1 | Intact | false |
| DDIT4L | Intact | false |
| DHX34 | Intact, Bioplex | false |
| EFEMP2 | Intact | false |
| ENKD1 | Intact | false |
| FAM221A | Intact | false |
| FRS3 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
