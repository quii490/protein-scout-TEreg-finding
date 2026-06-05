---
type: protein-evaluation
gene: "SMAD4"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SMAD4 — REJECTED (研究热度过高 (PubMed strict=3884，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SMAD4 / DPC4, MADH4 |
| 蛋白名称 | SMAD family member 4 |
| 蛋白大小 | 552 aa / 60.4 kDa |
| UniProt ID | Q13485 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Centrosome, Basal body; 额外: Vesicles, Primary c; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 552 aa / 60.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=3884 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=73.4; PDB: 1DD1, 1G88, 1MR1, 1U7F, 1U7V, 1YGS, 5C4V |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR013790, IPR003619, IPR013019, IPR017855, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Centrosome, Basal body; 额外: Vesicles, Primary cilium tip, Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- activin responsive factor complex (GO:0032444)
- centrosome (GO:0005813)
- chromatin (GO:0000785)
- ciliary basal body (GO:0036064)
- ciliary tip (GO:0097542)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- heteromeric SMAD protein complex (GO:0071144)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3884 |
| PubMed broad count | 6699 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DPC4, MADH4 |

**关键文献**:
1. Smad4/DPC4.. *Journal of clinical pathology*. PMID: 29720405
2. PRMT5 methylating SMAD4 activates TGF-β signaling and promotes colorectal cancer metastasis.. *Oncogene*. PMID: 36991117
3. SMAD4 Deficiency Promotes Pancreatic Cancer Progression and Confers Susceptibility to TGFβ Inhibition.. *Cancer research*. PMID: 40440097
4. Juvenile polyposis syndrome.. *Archives of medical science : AMS*. PMID: 25097590
5. SMAD4 induces opposite effects on metastatic growth from pancreatic tumors depending on the organ of residence.. *Nature cancer*. PMID: 40999053

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.4 |
| 高置信度残基 (pLDDT>90) 占比 | 50.0% |
| 置信残基 (pLDDT 70-90) 占比 | 12.5% |
| 中等置信 (pLDDT 50-70) 占比 | 4.7% |
| 低置信 (pLDDT<50) 占比 | 32.8% |
| 有序区域 (pLDDT>70) 占比 | 62.5% |
| 可用 PDB 条目 | 1DD1, 1G88, 1MR1, 1U7F, 1U7V, 1YGS, 5C4V, 5MEY, 5MEZ, 5MF0 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1DD1, 1G88, 1MR1, 1U7F, 1U7V, 1YGS, 5C4V, 5MEY, 5MEZ, 5MF0）+ AlphaFold极高置信度预测（pLDDT=73.4），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013790, IPR003619, IPR013019, IPR017855, IPR001132; Pfam: PF03165, PF03166 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SMAD3 | 0.999 | 0.999 | — |
| SMAD2 | 0.999 | 0.999 | — |
| SKIL | 0.999 | 0.899 | — |
| SMAD9 | 0.999 | 0.877 | — |
| LEF1 | 0.999 | 0.335 | — |
| SMAD5 | 0.999 | 0.612 | — |
| TGFBR1 | 0.998 | 0.535 | — |
| CTNNB1 | 0.998 | 0.308 | — |
| SKI | 0.998 | 0.994 | — |
| E2F4 | 0.997 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SKI | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CG12604 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Spx | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| ND-24 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Sld5 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG14634 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Med | psi-mi:"MI:0397"(two hybrid array) | doi:10.1016/j.celrep.2019.03.0 |
| daf-3 | psi-mi:"MI:0096"(pull down) | pubmed:14992718 |
| Skor1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15528197 |
| Ctbp1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15528197 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.4 + PDB: 1DD1, 1G88, 1MR1, 1U7F, 1U7V,  | pLDDT=73.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm, Centrosome, Basal body; 额外: Vesicles, | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. SMAD4 — SMAD family member 4，研究基础较多，新颖性有限。
2. 蛋白大小552 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 3884 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 3884 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13485
- Protein Atlas: https://www.proteinatlas.org/ENSG00000141646-SMAD4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SMAD4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13485
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000141646-SMAD4/subcellular

![](https://images.proteinatlas.org/19154/155_B7_1_red_green.jpg)
![](https://images.proteinatlas.org/19154/155_B7_2_red_green.jpg)
![](https://images.proteinatlas.org/19154/157_B7_1_red_green.jpg)
![](https://images.proteinatlas.org/19154/157_B7_2_red_green.jpg)
![](https://images.proteinatlas.org/19154/199_B7_1_red_green.jpg)
![](https://images.proteinatlas.org/19154/199_B7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q13485-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
