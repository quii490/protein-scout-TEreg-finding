---
type: protein-evaluation
gene: "MAP9"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MAP9 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MAP9 / ASAP |
| 蛋白名称 | Microtubule-associated protein 9 |
| 蛋白大小 | 647 aa / 74.2 kDa |
| UniProt ID | Q49MG5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Primary cilium, Primary cilium transition zone; 额外: Nuclear ; UniProt: Cytoplasm; Cytoplasm, cytoskeleton; Cytoplasm, cytoskeleton, |
| 蛋白大小 | 10/10 | ×1 | 10 | 647 aa / 74.2 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=23 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026106 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 9 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **108.0/180** | |
| **归一化总分** | | | **60.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Primary cilium, Primary cilium transition zone; 额外: Nuclear speckles, Centrosome | Approved |
| UniProt | Cytoplasm; Cytoplasm, cytoskeleton; Cytoplasm, cytoskeleton, spindle | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- astral microtubule (GO:0000235)
- axon (GO:0030424)
- cytoplasm (GO:0005737)
- mitotic spindle (GO:0072686)
- mitotic spindle midzone (GO:1990023)
- spindle midzone (GO:0051233)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 23 |
| PubMed broad count | 41 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ASAP |

**关键文献**:
1. Sex-specific genetic architecture of blood pressure.. *Nature medicine*. PMID: 38459180
2. Microtubule associated protein 9 inhibits liver tumorigenesis by suppressing ERCC3.. *EBioMedicine*. PMID: 32151798
3. MAP9/MAPH-9 supports axonemal microtubule doublets and modulates motor movement.. *Developmental cell*. PMID: 38159567
4. Gene organization, evolution and expression of the microtubule-associated protein ASAP (MAP9).. *BMC genomics*. PMID: 18782428
5. MAP9/MAPH-9 supports axonemal microtubule doublets and modulates motor movement.. *bioRxiv : the preprint server for biology*. PMID: 36865107

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.2 |
| 高置信度残基 (pLDDT>90) 占比 | 27.0% |
| 置信残基 (pLDDT 70-90) 占比 | 7.3% |
| 中等置信 (pLDDT 50-70) 占比 | 14.5% |
| 低置信 (pLDDT<50) 占比 | 51.2% |
| 有序区域 (pLDDT>70) 占比 | 34.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=61.2），有序残基占 34.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026106 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TUBA4A | 0.722 | 0.000 | — |
| AURKA | 0.579 | 0.047 | — |
| KIF2A | 0.497 | 0.497 | — |
| MAP10 | 0.479 | 0.000 | — |
| NXPE3 | 0.454 | 0.000 | — |
| SGO1 | 0.433 | 0.000 | — |
| MAP7D3 | 0.416 | 0.000 | — |
| SPICE1 | 0.408 | 0.069 | — |
| MAP7 | 0.400 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NEURL4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:29426014|imex:IM-26302| |
| TPR | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| AK2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| RPL10A | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| DCTN1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |
| SPICE1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |
| LCA5 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |
| OASL | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| TRAF3IP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| MVP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 9，IntAct interactions: 15
- 调控相关比例: 1 / 9 = 11%

**评价**: STRING 9 个预测互作，IntAct 15 个实验互作。调控相关配体占比 11%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.2 + PDB: 无 | pLDDT=61.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm, cytoskeleton; Cytoplasm, cyt / Primary cilium, Primary cilium transition zone; 额外 | 一致 |
| PPI | STRING + IntAct | 9 + 15 interactions | 数据充分 |

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
1. MAP9 — Microtubule-associated protein 9，非常新颖，仅有少数基础研究。
2. 蛋白大小647 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 23 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=61.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q49MG5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000164114-MAP9/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MAP9
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q49MG5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Primary cilium (approved)。来源: https://www.proteinatlas.org/ENSG00000164114-MAP9/subcellular

![](https://images.proteinatlas.org/37864/2121_E2_43_red_green.jpg)
![](https://images.proteinatlas.org/37864/2121_E2_8_red_green.jpg)
![](https://images.proteinatlas.org/37864/2132_D10_13_red_green.jpg)
![](https://images.proteinatlas.org/37864/2132_D10_55_red_green.jpg)
![](https://images.proteinatlas.org/37864/2167_G2_12_red_green.jpg)
![](https://images.proteinatlas.org/37864/2167_G2_80_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q49MG5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
