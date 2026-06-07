---
type: protein-evaluation
gene: "CCDC7"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CCDC7 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CCDC7 / BIOT2, C10orf68 |
| 蛋白名称 | Coiled-coil domain-containing protein 7 |
| 蛋白大小 | 1385 aa / 157.4 kDa |
| UniProt ID | Q96M83 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli; 额外: Mitotic spindle, Cytosol; UniProt: 无注释 |
| 蛋白大小 | 5/10 | ×1 | 5 | 1385 aa / 157.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=43.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR029272; Pfam: PF15368 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 12 partners; IntAct 10 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **124.5/180** | |
| **归一化总分** | | | **69.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; 额外: Mitotic spindle, Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 14 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BIOT2, C10orf68 |

**关键文献**:
1. Induction of ferroptosis in prostate cancer by CCDC7(19-13) via TRIM21-mediated ubiquitination of SLC7A11.. *Cell death and differentiation*. PMID: 40983631
2. A protein-encoding CCDC7 circular RNA inhibits the progression of prostate cancer by up-regulating FLRT3.. *NPJ precision oncology*. PMID: 38225404
3. CCDC7 Activates Interleukin-6 and Vascular Endothelial Growth Factor to Promote Proliferation via the JAK-STAT3 Pathway in Cervical Cancer Cells.. *OncoTargets and therapy*. PMID: 32669853
4. Rare Mutations in CCDC7 Contribute to Early-Onset Preeclampsia by Inhibiting Trophoblast Migration and Invasion.. *Journal of personalized medicine*. PMID: 38540995
5. Bioinformatics analysis and identification of potential genes related to pathogenesis of cervical intraepithelial neoplasia.. *Journal of Cancer*. PMID: 32127942

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 43.3 |
| 高置信度残基 (pLDDT>90) 占比 | 2.2% |
| 置信残基 (pLDDT 70-90) 占比 | 11.2% |
| 中等置信 (pLDDT 50-70) 占比 | 9.2% |
| 低置信 (pLDDT<50) 占比 | 77.4% |
| 有序区域 (pLDDT>70) 占比 | 13.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=43.3），有序残基占 13.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029272; Pfam: PF15368 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ERVFRD-1 | 0.516 | 0.000 | — |
| ERVV-2 | 0.511 | 0.000 | — |
| ERVV-1 | 0.496 | 0.000 | — |
| TEX13C | 0.475 | 0.000 | — |
| ENSP00000498408 | 0.442 | 0.000 | — |
| APOBEC3G | 0.432 | 0.000 | — |
| ZSCAN1 | 0.423 | 0.000 | — |
| LRRC69 | 0.418 | 0.000 | — |
| KIAA0586 | 0.415 | 0.000 | — |
| CCDC136 | 0.415 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EWSR1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CIAO1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| KLHL20 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| ITGA6 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| PLXNA1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| NXF1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ZDHHC17 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-21827|pubmed:24705354 |
| HTT | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| EBI-18211613 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| ATG16L1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31015422|imex:IM-29997 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 12，IntAct interactions: 10
- 调控相关比例: 0 / 12 = 0%

**评价**: STRING 12 个预测互作，IntAct 10 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=43.3 + PDB: 无 | pLDDT=43.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoli; 额外: Mitotic spindle, Cytosol | 待确认 |
| PPI | STRING + IntAct | 12 + 10 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CCDC7 — Coiled-coil domain-containing protein 7，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1385 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=43.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96M83
- Protein Atlas: https://www.proteinatlas.org/ENSG00000216937-CCDC7/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CCDC7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96M83
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96M83-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (approved)。来源: https://www.proteinatlas.org/ENSG00000216937-CCDC7/subcellular

![](https://images.proteinatlas.org/75536/1623_F3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/75536/1623_F3_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/75536/1756_C9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/75536/1756_C9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/75536/1758_C9_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/75536/1758_C9_5_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96M83 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR029272; |
| Pfam | PF15368; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000216937-CCDC7/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PLXNA1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
