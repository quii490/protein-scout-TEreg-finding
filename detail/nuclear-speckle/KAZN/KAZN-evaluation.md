---
type: protein-evaluation
gene: "KAZN"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KAZN 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KAZN / C1orf196, KAZ, KIAA1026 |
| 蛋白名称 | Kazrin |
| 蛋白大小 | 775 aa / 86.4 kDa |
| UniProt ID | Q674X7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nuclear speckles, Cytosol; UniProt: Cytoplasm, cytoskeleton; Cytoplasm; Cell junction, desmosome |
| 蛋白大小 | 10/10 | ×1 | 10 | 775 aa / 86.4 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=21 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=70.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR037614, IPR059089, IPR037613, IPR037615, IPR037 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.5/180** | |
| **归一化总分** | | | **68.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear speckles, Cytosol | Supported |
| UniProt | Cytoplasm, cytoskeleton; Cytoplasm; Cell junction, desmosome; Nucleus; Cytoplasm; Cell junction, des... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cornified envelope (GO:0001533)
- cytoskeleton (GO:0005856)
- cytosol (GO:0005829)
- desmosome (GO:0030057)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 21 |
| PubMed broad count | 49 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C1orf196, KAZ, KIAA1026 |

**关键文献**:
1. Distinct subtypes of polycystic ovary syndrome with novel genetic associations: An unsupervised, phenotypic clustering analysis.. *PLoS medicine*. PMID: 32574161
2. Investigation of biomarkers in Endometriosis-associated infertility: Systematic Review.. *Anais da Academia Brasileira de Ciencias*. PMID: 36477241
3. Epigenome-wide DNA methylation regulates cardinal pathological features of psoriasis.. *Clinical epigenetics*. PMID: 30092825
4. A Data-Driven Review of the Genetic Factors of Pregnancy Complications.. *International journal of molecular sciences*. PMID: 32403311
5. Silencing of LINC00284 inhibits cell proliferation and migration in oral squamous cell carcinoma by the miR-211-3p/MAFG axis and FUS/KAZN axis.. *Cancer biology & therapy*. PMID: 33618612

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.1 |
| 高置信度残基 (pLDDT>90) 占比 | 44.5% |
| 置信残基 (pLDDT 70-90) 占比 | 13.4% |
| 中等置信 (pLDDT 50-70) 占比 | 4.9% |
| 低置信 (pLDDT<50) 占比 | 37.2% |
| 有序区域 (pLDDT>70) 占比 | 57.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=70.1，有序区 57.9%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR037614, IPR059089, IPR037613, IPR037615, IPR037616; Pfam: PF25986, PF00536, PF07647 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PPL | 0.980 | 0.292 | — |
| ARHGAP5 | 0.740 | 0.422 | — |
| PPFIBP1 | 0.558 | 0.412 | — |
| PPFIBP2 | 0.547 | 0.412 | — |
| ZNF813 | 0.477 | 0.000 | — |
| ATG5 | 0.475 | 0.475 | — |
| FAM110D | 0.470 | 0.000 | — |
| ZDHHC14 | 0.429 | 0.000 | — |
| SYT4 | 0.427 | 0.000 | — |
| ANKRD61 | 0.426 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| COIL | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| PLEC | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| ARHGAP5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| PSMA1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TXN2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TNS4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| LMO2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| USP2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CLVS2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ARID5A | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.1 + PDB: 无 | pLDDT=70.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton; Cytoplasm; Cell junction, / Nucleoplasm; 额外: Nuclear speckles, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. KAZN — Kazrin，非常新颖，仅有少数基础研究。
2. 蛋白大小775 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 21 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q674X7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000189337-KAZN/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KAZN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q674X7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000189337-KAZN/subcellular

![](https://images.proteinatlas.org/32095/640_A11_6_red_green.jpg)
![](https://images.proteinatlas.org/32095/640_A11_7_red_green.jpg)
![](https://images.proteinatlas.org/32095/641_A11_1_red_green.jpg)
![](https://images.proteinatlas.org/32095/641_A11_2_red_green.jpg)
![](https://images.proteinatlas.org/32095/642_A11_1_red_green.jpg)
![](https://images.proteinatlas.org/32095/642_A11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q674X7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
