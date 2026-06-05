---
type: protein-evaluation
gene: "CDKL3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CDKL3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CDKL3 |
| 蛋白名称 | Cyclin-dependent kinase-like 3 |
| 蛋白大小 | 592 aa / 67.5 kDa |
| UniProt ID | Q8IVW4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Vesicles; UniProt: Cytoplasm |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 592 aa / 67.5 kDa |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=34 篇 (≤40→8) |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.4; PDB: 无 |
| 🧬 调控结构域 | 5/10 | ×2 | 10 | 无注释结构域 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 3 partners; IntAct 30 interactions |
| ➕ 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **104.0/180** | |
| **归一化总分** | | | **57.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Vesicles | Uncertain |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 34 |
| PubMed broad count | 36 |
| 别名(未计入scoring) |  |

**关键文献**:
1. CDKL3 Targets ATG5 to Exacerbate the Progression of Malignant Melanoma.. *Mol Carcinog*. PMID: 40569051
2. HNF4α-CDKL3 axis restricts MASLD progression by targeting FoxO1 via noncanonical phosphorylation.. *Hepatology*. PMID: 39658857
3. CDKL3, a versatile kinase with increasing recognition.. *Biochem Biophys Res Commun*. PMID: 40466365
4. Therapeutic Outcomes and Biomarker Potential of CDKL3 of Neoadjuvant Chemotherapy in Patients With Stage IIIC Versus Stage IV Epithelial Ovarian Cancer.. *JCO Precis Oncol*. PMID: 40865031
5. 5-Methylcytosine-modified circRNA-CCNL2 regulates vascular remdeling in hypoxic pulmonary hypertension through binding to FXR2.. *Int J Biol Macromol*. PMID: 39800017

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.4 |
| 高置信度残基 (pLDDT>90) 占比 | 41.6% |
| 置信残基 (pLDDT 70-90) 占比 | 6.9% |
| 中等置信 (pLDDT 50-70) 占比 | 3.5% |
| 低置信 (pLDDT<50) 占比 | 48.0% |
| 有序区域 (pLDDT>70) 占比 | 48.5% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CDKL3/CDKL3-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=64.4），有序残基占 48.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| STAMBP | 0.000 | 0.000 | — |
| MBD3L2 | 0.000 | 0.000 | — |
| ANKRD10 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q8IVW4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q5JR59-3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:P51116 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:A8MQ03 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q96BR9 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q9NRI5-2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q9P2M1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:O95630 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P11142 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q8WWB5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 3，IntAct interactions: 30
- 调控相关比例: 0 / 3 = 0%

**评价**: STRING 3 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.4 + PDB: 无 | pLDDT=64.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoplasm, Vesicles | 一致 |
| PPI | STRING + IntAct | 3 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CDKL3 — Cyclin-dependent kinase-like 3，非常新颖，仅有少数基础研究。
2. 蛋白大小592 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 34 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=64.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IVW4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000006837-CDKL3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CDKL3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IVW4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CDKL3/CDKL3-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000006837-CDKL3/subcellular

![](https://images.proteinatlas.org/27751/218_G10_1_red_green.jpg)
![](https://images.proteinatlas.org/27751/218_G10_2_red_green.jpg)
![](https://images.proteinatlas.org/27751/219_G10_1_red_green.jpg)
![](https://images.proteinatlas.org/27751/219_G10_2_red_green.jpg)
![](https://images.proteinatlas.org/27751/220_G10_1_red_green.jpg)
![](https://images.proteinatlas.org/27751/220_G10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
