---
type: protein-evaluation
gene: "SIX1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SIX1 — REJECTED (研究热度过高 (PubMed strict=538，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SIX1 |
| 蛋白名称 | Homeobox protein SIX1 |
| 蛋白大小 | 284 aa / 32.2 kDa |
| UniProt ID | Q15475 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nucleoli; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 284 aa / 32.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=538 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=75.6; PDB: 4EGC |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001356, IPR017970, IPR009057, IPR008422, IPR031 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **87.0/180** | |
| **归一化总分** | | | **48.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- transcription regulator complex (GO:0005667)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 538 |
| PubMed broad count | 844 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Genetic Hearing Loss Overview.. **. PMID: 20301607
2. Branchio-oto-renal syndrome.. *American journal of medical genetics. Part A*. PMID: 17238186
3. Branchiootorenal Spectrum Disorder.. **. PMID: 20301554
4. Phosphorylation determines the glucose metabolism reprogramming and tumor-promoting activity of sine oculis homeobox 1.. *Signal transduction and targeted therapy*. PMID: 39617783
5. AAV-mediated Gene Cocktails Enhance Supporting Cell Reprogramming and Hair Cell Regeneration.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 38810137

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.6 |
| 高置信度残基 (pLDDT>90) 占比 | 52.1% |
| 置信残基 (pLDDT 70-90) 占比 | 11.3% |
| 中等置信 (pLDDT 50-70) 占比 | 8.1% |
| 低置信 (pLDDT<50) 占比 | 28.5% |
| 有序区域 (pLDDT>70) 占比 | 63.4% |
| 可用 PDB 条目 | 4EGC |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=75.6，有序区 63.4%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001356, IPR017970, IPR009057, IPR008422, IPR031701; Pfam: PF05920, PF16878 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EYA1 | 0.997 | 0.835 | — |
| EYA2 | 0.996 | 0.893 | — |
| DACH1 | 0.939 | 0.077 | — |
| PAX3 | 0.925 | 0.000 | — |
| EYA3 | 0.906 | 0.394 | — |
| EYA4 | 0.895 | 0.723 | — |
| MYOG | 0.859 | 0.000 | — |
| MYOD1 | 0.856 | 0.000 | — |
| PAX2 | 0.832 | 0.000 | — |
| SALL1 | 0.810 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CCDC85B | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MDFI | psi-mi:"MI:0096"(pull down) | pubmed:16189514|imex:IM-16520| |
| VTN | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| POU6F2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| EYA2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| H2AP | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| TLE5 | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-25511|pubmed:25910212 |
| P4HA3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| EYA4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MYH3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.6 + PDB: 4EGC | pLDDT=75.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm; 额外: Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. SIX1 — Homeobox protein SIX1，研究基础较多，新颖性有限。
2. 蛋白大小284 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 538 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 538 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q15475
- Protein Atlas: https://www.proteinatlas.org/ENSG00000126778-SIX1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SIX1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q15475
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000126778-SIX1/subcellular

![](https://images.proteinatlas.org/1893/17_E2_1_red_green.jpg)
![](https://images.proteinatlas.org/1893/17_E2_2_red_green.jpg)
![](https://images.proteinatlas.org/1893/18_E2_1_red_green.jpg)
![](https://images.proteinatlas.org/1893/18_E2_2_red_green.jpg)
![](https://images.proteinatlas.org/1893/19_E2_1_red_green.jpg)
![](https://images.proteinatlas.org/1893/19_E2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q15475-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q15475 |
| SMART | SM00389; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR001356;IPR017970;IPR009057;IPR008422;IPR031701; |
| Pfam | PF05920;PF16878; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000126778-SIX1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| EYA1 | Intact, Biogrid | true |
| EYA2 | Intact, Biogrid | true |
| H2AP | Intact, Biogrid | true |
| MDFI | Intact, Biogrid | true |
| DDOST | Opencell | false |
| EYA4 | Biogrid | false |
| HSPA9 | Biogrid | false |
| OST4 | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
