---
type: protein-evaluation
gene: "PHF7"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PHF7 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PHF7 |
| 蛋白名称 | E3 ubiquitin-protein ligase PHF7 |
| 蛋白大小 | 381 aa / 43.8 kDa |
| UniProt ID | Q9BWX1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nuclear speckles; 额外: Golgi apparatus; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 381 aa / 43.8 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=24 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=76.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR034732, IPR051188, IPR059102, IPR042013, IPR011 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.5/180** | |
| **归一化总分** | | | **68.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear speckles; 额外: Golgi apparatus | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- Golgi apparatus (GO:0005794)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 24 |
| PubMed broad count | 35 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Cellular Reprogramming by PHF7 Enhances Cardiac Function Following Myocardial Infarction.. *Circulation*. PMID: 40631661
2. PHF7 Modulates BRDT Stability and Histone-to-Protamine Exchange during Spermiogenesis.. *Cell reports*. PMID: 32726616
3. Expanding duplication of the testis PHD Finger Protein 7 (PHF7) gene in the chicken genome.. *Genomics*. PMID: 35716824
4. Phf7 has impacts on the body growth and bone remodeling by regulating testicular hormones in male mice.. *Biochemical and biophysical research communications*. PMID: 38430697
5. PHF7, a novel male gene influences female fecundity and population growth in Nilaparvata lugens Stål (Hemiptera: Delphacidae).. *Scientific reports*. PMID: 28912601

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.3 |
| 高置信度残基 (pLDDT>90) 占比 | 59.8% |
| 置信残基 (pLDDT 70-90) 占比 | 10.2% |
| 中等置信 (pLDDT 50-70) 占比 | 2.4% |
| 低置信 (pLDDT<50) 占比 | 27.6% |
| 有序区域 (pLDDT>70) 占比 | 70.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=76.3，有序区 70.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR034732, IPR051188, IPR059102, IPR042013, IPR011011; Pfam: PF26054, PF13771 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TCEAL1 | 0.700 | 0.700 | — |
| USP7 | 0.679 | 0.658 | — |
| H3-4 | 0.675 | 0.151 | — |
| H3-5 | 0.673 | 0.151 | — |
| H3C13 | 0.673 | 0.151 | — |
| H3C12 | 0.673 | 0.151 | — |
| H3-2 | 0.673 | 0.151 | — |
| H3-3B | 0.673 | 0.151 | — |
| USP11 | 0.634 | 0.482 | — |
| MAGEF1 | 0.604 | 0.230 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Moe | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| CT24026 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| "l | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Pih1D1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| prod | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG6280 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:37061542|imex:IM-28761 |
| Dmel\CG13733 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:37061542|imex:IM-28761 |
| NC2alpha-RA | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:37061542|imex:IM-28761 |
| Syn2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:37061542|imex:IM-28761 |
| IKBKG | psi-mi:"MI:0089"(protein array) | pubmed:20098747|imex:IM-17256 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.3 + PDB: 无 | pLDDT=76.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Nuclear speckles; 额外: Golgi apparatus | 一致 |
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
1. PHF7 — E3 ubiquitin-protein ligase PHF7，非常新颖，仅有少数基础研究。
2. 蛋白大小381 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 24 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BWX1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000010318-PHF7/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PHF7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BWX1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000010318-PHF7/subcellular

![](https://images.proteinatlas.org/36283/413_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/36283/413_A3_2_red_green.jpg)
![](https://images.proteinatlas.org/36283/417_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/36283/417_A3_2_red_green.jpg)
![](https://images.proteinatlas.org/36283/420_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/36283/420_A3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BWX1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BWX1 |
| SMART | SM00249; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR034732;IPR051188;IPR059102;IPR042013;IPR011011;IPR001965;IPR001841;IPR013083; |
| Pfam | PF26054;PF13771; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000010318-PHF7/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| GRN | Intact | false |
| HARS2 | Bioplex | false |
| SPRED1 | Intact | false |
| UBE2D2 | Intact | false |
| UBE2D4 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
