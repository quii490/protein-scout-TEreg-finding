---
type: protein-evaluation
gene: "DDIT3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DDIT3 — REJECTED (研究热度过高 (PubMed strict=730，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DDIT3 |
| 蛋白名称 | DDIT3 upstream open reading frame protein |
| 蛋白大小 | 34 aa / 4.3 kDa |
| UniProt ID | P0DPQ6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 2/10 | ×1 | 2 | 34 aa / 4.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=730 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=84.6; PDB: 无 |
| 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **73.5/180** | |
| **归一化总分** | | | **40.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- late endosome (GO:0005770)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 730 |
| PubMed broad count | 3114 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Ferroptosis-related biomarkers for Alzheimer's disease: Identification by bioinformatic analysis in hippocampus.. *Frontiers in cellular neuroscience*. PMID: 36467613
2. Identification of autophagy-related genes in osteoarthritis articular cartilage and their roles in immune infiltration.. *Frontiers in immunology*. PMID: 38090564
3. Gene of the month: DDIT3.. *Journal of clinical pathology*. PMID: 38053287
4. Lack of COL6/collagen VI causes megakaryocyte dysfunction by impairing autophagy and inducing apoptosis.. *Autophagy*. PMID: 35857791
5. Myxoid pleomorphic liposarcoma.. *Histology and histopathology*. PMID: 38450446

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.6 |
| 高置信度残基 (pLDDT>90) 占比 | 14.7% |
| 置信残基 (pLDDT 70-90) 占比 | 79.4% |
| 中等置信 (pLDDT 50-70) 占比 | 5.9% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 94.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=84.6，有序区 94.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ATF4 | 0.996 | 0.526 | — |
| CEBPB | 0.994 | 0.783 | — |
| ATF6 | 0.989 | 0.000 | — |
| ATF3 | 0.988 | 0.877 | — |
| XBP1 | 0.988 | 0.071 | — |
| BCL2 | 0.972 | 0.000 | — |
| NFE2L2 | 0.968 | 0.341 | — |
| BCL2L11 | 0.956 | 0.000 | — |
| EIF2S1 | 0.951 | 0.000 | — |
| MAPK14 | 0.950 | 0.320 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000494844.1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| SPOP | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MCMBP | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| BATF | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CEBPG | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| HSD17B14 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| DBP | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| KPNA2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| EP300 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| F2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.6 + PDB: 无 | pLDDT=84.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. DDIT3 — DDIT3 upstream open reading frame protein，研究基础较多，新颖性有限。
2. 蛋白大小34 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 730 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 730 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P0DPQ6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000175197-DDIT3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DDIT3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P0DPQ6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000175197-DDIT3/subcellular

![](https://images.proteinatlas.org/58416/1020_F8_1_red_green.jpg)
![](https://images.proteinatlas.org/58416/1020_F8_4_red_green.jpg)
![](https://images.proteinatlas.org/58416/993_F8_1_red_green.jpg)
![](https://images.proteinatlas.org/58416/993_F8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P0DPQ6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P0DPQ6 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | 未检出 |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000175197-DDIT3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ATF3 | Intact, Biogrid | true |
| ATF4 | Intact, Biogrid | true |
| BATF | Intact, Biogrid | true |
| BATF3 | Intact, Biogrid | true |
| CEBPA | Intact, Biogrid | true |
| CEBPB | Intact, Biogrid | true |
| CEBPE | Intact, Biogrid | true |
| CEBPG | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
