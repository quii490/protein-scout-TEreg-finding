---
type: protein-evaluation
gene: "SLF1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SLF1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SLF1 / ANKRD32, BRCTD1 |
| 蛋白名称 | SMC5-SMC6 complex localization factor protein 1 |
| 蛋白大小 | 1058 aa / 121.0 kDa |
| UniProt ID | Q9BQI6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Cytoplasm; Cytoplasm, cytoskeleton, microtubule org |
| 蛋白大小 | 8/10 | ×1 | 8 | 1058 aa / 121.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=31 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=69.2; PDB: 8IR2, 8IR4, 8PEF |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR002110, IPR036770, IPR001357, IPR036420, IPR049 |
| PPI 网络 | 8/10 | ×3 | 24 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **134.5/180** | |
| **归一化总分** | | | **74.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus; Cytoplasm; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centrosome (GO:0005813)
- chromosome, telomeric region (GO:0000781)
- cytoplasm (GO:0005737)
- nuclear inclusion body (GO:0042405)
- nucleoplasm (GO:0005654)
- nucleosome (GO:0000786)
- nucleus (GO:0005634)
- site of double-strand break (GO:0035861)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 31 |
| PubMed broad count | 47 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ANKRD32, BRCTD1 |

**关键文献**:
1. Structural insights into Rad18 targeting by the SLF1 BRCT domains.. *The Journal of biological chemistry*. PMID: 37748650
2. Repression of mitochondrial translation, respiration and a metabolic cycle-regulated gene, SLF1, by the yeast Pumilio-family protein Puf3p.. *PloS one*. PMID: 21655263
3. Interaction of the La-related protein Slf1 with colliding ribosomes maintains translation of oxidative-stress responsive mRNAs.. *Nucleic acids research*. PMID: 37070186
4. RNA Binding by the Yeast Slf1 and Sro9 La-motif Domains.. *Journal of molecular biology*. PMID: 41223936
5. Two yeast La motif-containing proteins are RNA-binding proteins that associate with polyribosomes.. *Molecular biology of the cell*. PMID: 10564276

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.2 |
| 高置信度残基 (pLDDT>90) 占比 | 24.9% |
| 置信残基 (pLDDT 70-90) 占比 | 38.9% |
| 中等置信 (pLDDT 50-70) 占比 | 9.1% |
| 低置信 (pLDDT<50) 占比 | 27.1% |
| 有序区域 (pLDDT>70) 占比 | 63.8% |
| 可用 PDB 条目 | 8IR2, 8IR4, 8PEF |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=69.2），有序残基占 63.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002110, IPR036770, IPR001357, IPR036420, IPR049935; Pfam: PF12796, PF23294, PF16770 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SLF2 | 0.999 | 0.826 | — |
| SMC5 | 0.959 | 0.609 | — |
| RAD18 | 0.956 | 0.786 | — |
| CDC45 | 0.947 | 0.900 | — |
| PSMD12 | 0.922 | 0.882 | — |
| TP53BP1 | 0.921 | 0.838 | — |
| MCM3 | 0.916 | 0.896 | — |
| MCM5 | 0.894 | 0.844 | — |
| SMC6 | 0.867 | 0.420 | — |
| NSMCE4A | 0.835 | 0.451 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| E9P8Z6 | psi-mi:"MI:0111"(dihydrofolate reductase reconstru | pubmed:31454312|imex:IM-26944 |
| PAB1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| SSB1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| UBC7 | psi-mi:"MI:0397"(two hybrid array) | pubmed:14690591 |
| SSA2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SCJ1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| HSP82 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| PAC10 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| CCT8 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| CCT3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 6 / 15 = 40%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 40%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=69.2 + PDB: 8IR2, 8IR4, 8PEF | pLDDT=69.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Cytoplasm, cytoskeleton, micro / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. SLF1 — SMC5-SMC6 complex localization factor protein 1，非常新颖，仅有少数基础研究。
2. 蛋白大小1058 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 31 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=69.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BQI6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000133302-SLF1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SLF1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BQI6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000133302-SLF1/subcellular

![](https://images.proteinatlas.org/54213/1050_A12_5_red_green.jpg)
![](https://images.proteinatlas.org/54213/1050_A12_6_red_green.jpg)
![](https://images.proteinatlas.org/54213/859_G9_1_red_green.jpg)
![](https://images.proteinatlas.org/54213/859_G9_3_red_green.jpg)
![](https://images.proteinatlas.org/54213/862_G9_1_red_green.jpg)
![](https://images.proteinatlas.org/54213/862_G9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BQI6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BQI6 |
| SMART | SM00248;SM00292; |
| UniProt Domain [FT] | DOMAIN 12..77; /note="BRCT 1"; DOMAIN 119..196; /note="BRCT 2" |
| InterPro | IPR002110;IPR036770;IPR001357;IPR036420;IPR049935;IPR042479;IPR057595; |
| Pfam | PF12796;PF23294;PF16770; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000133302-SLF1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| RAD18 | Biogrid, Bioplex | true |
| SLF2 | Intact, Biogrid, Bioplex | true |
| UBE2A | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
