---
type: protein-evaluation
gene: "NUBP2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NUBP2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NUBP2 |
| 蛋白名称 | Cytosolic Fe-S cluster assembly factor NUBP2 |
| 蛋白大小 | 271 aa / 28.8 kDa |
| UniProt ID | Q9Y5Y2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Nucleus; Cytoplasm, cytoskeleton, microtubule organizing cen |
| 蛋白大小 | 10/10 | ×1 | 10 | 271 aa / 28.8 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=25 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=90.6; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000808, IPR019591, IPR028600, IPR027417, IPR033 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.5/180** | |
| **归一化总分** | | | **71.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Approved |
| UniProt | Nucleus; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Cytoplasm; Cytoplasm, c... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- axoneme (GO:0005930)
- centriole (GO:0005814)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- spindle pole centrosome (GO:0031616)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 25 |
| PubMed broad count | 29 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. RNA-Sequencing Analysis Identification of Potential Biomarkers for Diagnosis of Sarcopenia.. *The journals of gerontology. Series A, Biological sciences and medical sciences*. PMID: 37347997
2. Metformin inhibits oral squamous cell carcinoma progression through regulating RNA alternative splicing.. *Life sciences*. PMID: 36509195
3. Motor protein KIFC5A interacts with Nubp1 and Nubp2, and is implicated in the regulation of centrosome duplication.. *Journal of cell science*. PMID: 16638812
4. The nucleotide-binding proteins Nubp1 and Nubp2 are negative regulators of ciliogenesis.. *Cellular and molecular life sciences : CMLS*. PMID: 23807208
5. Isovalerylspiramycin I alleviates liver injury and liver fibrosis by targeting the nucleotide-binding protein 2 (NUBP2)-vascular non-inflammatory molecule-1 (VNN1) pathway.. *Journal of pharmaceutical analysis*. PMID: 40177065

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.6 |
| 高置信度残基 (pLDDT>90) 占比 | 70.5% |
| 置信残基 (pLDDT 70-90) 占比 | 24.4% |
| 中等置信 (pLDDT 50-70) 占比 | 3.3% |
| 低置信 (pLDDT<50) 占比 | 1.8% |
| 有序区域 (pLDDT>70) 占比 | 94.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=90.6，有序区 94.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000808, IPR019591, IPR028600, IPR027417, IPR033756; Pfam: PF10609 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NUBP1 | 0.922 | 0.456 | — |
| CIAO3 | 0.902 | 0.379 | — |
| CIAO1 | 0.885 | 0.150 | — |
| ABCB7 | 0.870 | 0.000 | — |
| NSFL1C | 0.830 | 0.000 | — |
| CIAPIN1 | 0.824 | 0.226 | — |
| FOXRED1 | 0.804 | 0.000 | — |
| NDOR1 | 0.795 | 0.091 | — |
| ACO1 | 0.794 | 0.000 | — |
| RHOA | 0.722 | 0.324 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Cdk5 | psi-mi:"MI:0018"(two hybrid) | pubmed:15575970|mint:MINT-7952 |
| Doa | psi-mi:"MI:0018"(two hybrid) | pubmed:15575970|mint:MINT-7952 |
| Nubp1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| CIAO1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| PHLDA3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| PTP4A3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| Dmel\CG14104 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| DISC1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| RAF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| RHOA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.6 + PDB: 无 | pLDDT=90.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, cytoskeleton, microtubule orga / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. NUBP2 — Cytosolic Fe-S cluster assembly factor NUBP2，非常新颖，仅有少数基础研究。
2. 蛋白大小271 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 25 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y5Y2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000095906-NUBP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NUBP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y5Y2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000095906-NUBP2/subcellular

![](https://images.proteinatlas.org/41704/2216_G3_10_blue_red_green.jpg)
![](https://images.proteinatlas.org/41704/2216_G3_24_blue_red_green.jpg)
![](https://images.proteinatlas.org/41704/504_F3_1_red_green.jpg)
![](https://images.proteinatlas.org/41704/504_F3_3_red_green.jpg)
![](https://images.proteinatlas.org/41704/506_F3_1_red_green.jpg)
![](https://images.proteinatlas.org/41704/506_F3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y5Y2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
