---
type: protein-evaluation
gene: "PHF8"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PHF8 — REJECTED (研究热度过高 (PubMed strict=130，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PHF8 / KDM7B, KIAA1111, ZNF422 |
| 蛋白名称 | Histone lysine demethylase PHF8 |
| 蛋白大小 | 1060 aa / 117.9 kDa |
| UniProt ID | Q9UPP1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Nucleus, nucleolus |
| 蛋白大小 | 8/10 | ×1 | 8 | 1060 aa / 117.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=130 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.4; PDB: 2WWU, 3K3N, 3K3O, 3KV4, 4DO0, 7CMZ |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR041070, IPR050690, IPR003347, IPR019786, IPR011 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **79.5/180** | |
| **归一化总分** | | | **44.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus; Nucleus, nucleolus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nuclear membrane (GO:0031965)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 130 |
| PubMed broad count | 186 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KDM7B, KIAA1111, ZNF422 |

**关键文献**:
1. Homocysteine Metabolites, Endothelial Dysfunction, and Cardiovascular Disease.. *International journal of molecular sciences*. PMID: 39859460
2. PHF8-GLUL axis in lipid deposition and tumor growth of clear cell renal cell carcinoma.. *Science advances*. PMID: 37531433
3. Loss of PHF8 induces a viral mimicry response by activating endogenous retrotransposons.. *Nature communications*. PMID: 37454216
4. PHF8/KDM7B: A Versatile Histone Demethylase and Epigenetic Modifier in Nervous System Disease and Cancers.. *Epigenomes*. PMID: 39311138
5. PHF8 facilitates transcription recovery following DNA double-strand break repair.. *Nucleic acids research*. PMID: 39087553

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.4 |
| 高置信度残基 (pLDDT>90) 占比 | 34.2% |
| 置信残基 (pLDDT 70-90) 占比 | 9.0% |
| 中等置信 (pLDDT 50-70) 占比 | 4.0% |
| 低置信 (pLDDT<50) 占比 | 52.9% |
| 有序区域 (pLDDT>70) 占比 | 43.2% |
| 可用 PDB 条目 | 2WWU, 3K3N, 3K3O, 3KV4, 4DO0, 7CMZ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=62.4），有序残基占 43.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR041070, IPR050690, IPR003347, IPR019786, IPR011011; Pfam: PF17811, PF02373, PF00628 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| H3C12 | 0.987 | 0.924 | — |
| H3-3B | 0.985 | 0.914 | — |
| H3C13 | 0.985 | 0.914 | — |
| H3C1 | 0.984 | 0.983 | — |
| H3-2 | 0.971 | 0.914 | — |
| H3-5 | 0.971 | 0.914 | — |
| HCFC1 | 0.970 | 0.292 | — |
| H4C6 | 0.954 | 0.537 | — |
| TOPBP1 | 0.951 | 0.939 | — |
| H3-4 | 0.927 | 0.580 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| - | psi-mi:"MI:0096"(pull down) | imex:IM-11882|pubmed:17884155 |
| PML-RAR | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:23518351|imex:IM-18737 |
| RARA | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:23518351|imex:IM-18737 |
| EBI-6602397 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:23518351|imex:IM-18737 |
| ENSP00000338868.6 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:23518351|imex:IM-18737 |
| EBI-1265562 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:23518351|imex:IM-18737 |
| EBI-6602616 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:23518351|imex:IM-18737 |
| ENSP00000350676.5 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:23518351|imex:IM-18737 |
| HMGN2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H1-5 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.4 + PDB: 2WWU, 3K3N, 3K3O, 3KV4, 4DO0,  | pLDDT=62.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus, nucleolus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. PHF8 — Histone lysine demethylase PHF8，研究基础较多，新颖性有限。
2. 蛋白大小1060 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 130 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=62.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 130 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UPP1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000172943-PHF8/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PHF8
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UPP1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000172943-PHF8/subcellular

![](https://images.proteinatlas.org/62015/1104_C2_1_red_green.jpg)
![](https://images.proteinatlas.org/62015/1104_C2_2_red_green.jpg)
![](https://images.proteinatlas.org/62015/1127_C2_2_red_green.jpg)
![](https://images.proteinatlas.org/62015/1127_C2_6_red_green.jpg)
![](https://images.proteinatlas.org/62015/1169_G3_1_red_green.jpg)
![](https://images.proteinatlas.org/62015/1169_G3_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UPP1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
