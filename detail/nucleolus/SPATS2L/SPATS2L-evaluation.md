---
type: protein-evaluation
gene: "SPATS2L"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SPATS2L 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SPATS2L / DNAPTP6 |
| 蛋白名称 | SPATS2-like protein |
| 蛋白大小 | 558 aa / 61.7 kDa |
| UniProt ID | Q9NUQ6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli, Cytosol; UniProt: Cytoplasm; Nucleus, nucleolus |
| 蛋白大小 | 10/10 | ×1 | 10 | 558 aa / 61.7 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=30 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR009816, IPR009060; Pfam: PF07139 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.0/180** | |
| **归一化总分** | | | **66.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli, Cytosol | Enhanced |
| UniProt | Cytoplasm; Nucleus, nucleolus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- protein-containing complex (GO:0032991)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 30 |
| PubMed broad count | 42 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DNAPTP6 |

**关键文献**:
1. IGJ and SPATS2L immunohistochemistry sensitively and specifically identify BCR::ABL1+ and BCR::ABL1-like B-acute lymphoblastic leukaemia.. *British journal of haematology*. PMID: 37871900
2. A cross-tissue transcriptome-wide association study identifies novel susceptibility genes for atrial fibrillation.. *Journal of arrhythmia*. PMID: 40416952
3. SPATS2L is a positive feedback regulator of the type I interferon signaling pathway and plays a vital role in lupus.. *Acta biochimica et biophysica Sinica*. PMID: 39099414
4. Characteristic DNA methylation profiles of chorionic villi in recurrent miscarriage.. *Scientific reports*. PMID: 35896560
5. Identification of Molecular Subtypes of B-Cell Acute Lymphoblastic Leukemia in Mexican Children by Whole-Transcriptome Analysis.. *International journal of molecular sciences*. PMID: 40725249

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.1 |
| 高置信度残基 (pLDDT>90) 占比 | 33.0% |
| 置信残基 (pLDDT 70-90) 占比 | 2.7% |
| 中等置信 (pLDDT 50-70) 占比 | 14.3% |
| 低置信 (pLDDT<50) 占比 | 50.0% |
| 有序区域 (pLDDT>70) 占比 | 35.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=63.1），有序残基占 35.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009816, IPR009060; Pfam: PF07139 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RTP4 | 0.613 | 0.000 | — |
| EPSTI1 | 0.584 | 0.000 | — |
| OAS3 | 0.578 | 0.000 | — |
| IFI44L | 0.554 | 0.000 | — |
| IFI44 | 0.554 | 0.000 | — |
| KCTD18 | 0.553 | 0.000 | — |
| IFI16 | 0.547 | 0.510 | — |
| DDX60 | 0.540 | 0.000 | — |
| RSAD2 | 0.512 | 0.000 | — |
| IFI27 | 0.511 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| CSNK2A1 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:22113938|imex:IM-16640 |
| CANX | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| FBL | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| AP2A1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H3C1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| FMR1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| FGFR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| TRIM44 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.1 + PDB: 无 | pLDDT=63.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus, nucleolus / Nucleoli, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. SPATS2L — SPATS2-like protein，非常新颖，仅有少数基础研究。
2. 蛋白大小558 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 30 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=63.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NUQ6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000196141-SPATS2L/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SPATS2L
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NUQ6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (enhanced)。来源: https://www.proteinatlas.org/ENSG00000196141-SPATS2L/subcellular

![](https://images.proteinatlas.org/55427/1027_H2_2_red_green.jpg)
![](https://images.proteinatlas.org/55427/1027_H2_7_red_green.jpg)
![](https://images.proteinatlas.org/55427/875_D7_2_red_green.jpg)
![](https://images.proteinatlas.org/55427/875_D7_3_red_green.jpg)
![](https://images.proteinatlas.org/55427/883_D7_1_red_green.jpg)
![](https://images.proteinatlas.org/55427/883_D7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NUQ6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
