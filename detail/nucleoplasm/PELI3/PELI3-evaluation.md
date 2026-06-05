---
type: protein-evaluation
gene: "PELI3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PELI3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PELI3 |
| 蛋白名称 | E3 ubiquitin-protein ligase pellino homolog 3 |
| 蛋白大小 | 469 aa / 50.8 kDa |
| UniProt ID | Q8N2H9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Vesicles; 额外: Nucleoli; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 469 aa / 50.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=18 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=81.0; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR006800, IPR048334, IPR048335; Pfam: PF04710, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.5/180** | |
| **归一化总分** | | | **68.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Vesicles; 额外: Nucleoli | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 18 |
| PubMed broad count | 38 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Protective coding variants in CFH and PELI3 and a variant near CTRB1 are associated with age-related macular degeneration†.. *Human molecular genetics*. PMID: 28011711
2. Juanbi Qianggu Formula inhibits fibroblast-like synovicytes activation via repressing LncRNA ITSN1-2 to promote RIP2 K48 ubiquitination.. *Chinese medicine*. PMID: 40629453
3. FTO promotes gefitinib-resistance by enhancing PELI3 expression and autophagy in non-small cell lung cancer.. *Pulmonary pharmacology & therapeutics*. PMID: 39154901
4. Pellino 3 promotes the colitis-associated colorectal cancer through suppression of IRF4-mediated negative regulation of TLR4 signalling.. *Molecular oncology*. PMID: 37341064
5. Peli3 ablation ameliorates acetaminophen-induced liver injury through inhibition of GSK3β phosphorylation and mitochondrial translocation.. *Experimental & molecular medicine*. PMID: 37258579

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.0 |
| 高置信度残基 (pLDDT>90) 占比 | 56.9% |
| 置信残基 (pLDDT 70-90) 占比 | 19.2% |
| 中等置信 (pLDDT 50-70) 占比 | 8.7% |
| 低置信 (pLDDT<50) 占比 | 15.1% |
| 有序区域 (pLDDT>70) 占比 | 76.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=81.0，有序区 76.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR006800, IPR048334, IPR048335; Pfam: PF04710, PF20723 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| IRAK1 | 0.997 | 0.854 | — |
| TRAF6 | 0.980 | 0.785 | — |
| IRAK4 | 0.908 | 0.328 | — |
| MAP3K7 | 0.849 | 0.644 | — |
| UBE2N | 0.803 | 0.292 | — |
| UBE2V1 | 0.769 | 0.292 | — |
| RIPK2 | 0.718 | 0.328 | — |
| TAB1 | 0.706 | 0.000 | — |
| MAP3K14 | 0.664 | 0.292 | — |
| IKBKG | 0.650 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| IRAK1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:12874243 |
| TRAF6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:12874243 |
| MAP3K7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:12874243 |
| MAP3K14 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:12874243 |
| PIK3R3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:25814554|imex:IM-22632 |
| TRIM55 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:31391242|imex:IM-25805| |
| SARS1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| FKBP1A | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| EIF2S3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| ERN1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.0 + PDB: 无 | pLDDT=81.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Vesicles; 额外: Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PELI3 — E3 ubiquitin-protein ligase pellino homolog 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小469 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 18 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N2H9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000174516-PELI3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PELI3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N2H9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000174516-PELI3/subcellular

![](https://images.proteinatlas.org/62281/1106_E11_1_red_green.jpg)
![](https://images.proteinatlas.org/62281/1106_E11_3_red_green.jpg)
![](https://images.proteinatlas.org/62281/1148_E11_1_red_green.jpg)
![](https://images.proteinatlas.org/62281/1148_E11_2_red_green.jpg)
![](https://images.proteinatlas.org/62281/1246_H9_1_red_green.jpg)
![](https://images.proteinatlas.org/62281/1246_H9_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8N2H9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
