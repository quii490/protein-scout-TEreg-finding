---
type: protein-evaluation
gene: "TRA2A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TRA2A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TRA2A |
| 蛋白名称 | Transformer-2 protein homolog alpha |
| 蛋白大小 | 282 aa / 32.7 kDa |
| UniProt ID | Q13595 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoli; 额外: Nucleoplasm, Vesicles; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 282 aa / 32.7 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=39 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=58.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR012677, IPR035979, IPR050441, IPR000504; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.0/180** | |
| **归一化总分** | | | **71.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; 额外: Nucleoplasm, Vesicles | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- spliceosomal complex (GO:0005681)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 39 |
| PubMed broad count | 56 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Differential Degradation of TRA2A and PYCR2 Mediated by Ubiquitin E3 Ligase E4B.. *Frontiers in cell and developmental biology*. PMID: 35669517
2. TRA2: The dominant power of alternative splicing in tumors.. *Heliyon*. PMID: 37151663
3. TRA2A Promoted Paclitaxel Resistance and Tumor Progression in Triple-Negative Breast Cancers via Regulating Alternative Splicing.. *Molecular cancer therapeutics*. PMID: 28416606
4. H3K18la Facilitates TRA2A-Mediated Alternative Splicing of STIL, Suppressing Ferroptosis and Cisplatin Treatment Sensitivity in Ovarian Cancer.. *Cancer research and treatment*. PMID: 40907573
5. TRA2A Binds With LncRNA MALAT1 To Promote Esophageal Cancer Progression By Regulating EZH2/β-catenin Pathway.. *Journal of Cancer*. PMID: 34234858

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 58.9 |
| 高置信度残基 (pLDDT>90) 占比 | 20.9% |
| 置信残基 (pLDDT 70-90) 占比 | 8.2% |
| 中等置信 (pLDDT 50-70) 占比 | 21.6% |
| 低置信 (pLDDT<50) 占比 | 49.3% |
| 有序区域 (pLDDT>70) 占比 | 29.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=58.9），有序残基占 29.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR012677, IPR035979, IPR050441, IPR000504; Pfam: PF00076 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SRSF10 | 0.953 | 0.798 | — |
| SRSF6 | 0.937 | 0.756 | — |
| SRSF1 | 0.934 | 0.426 | — |
| SRSF7 | 0.897 | 0.502 | — |
| SRSF3 | 0.896 | 0.532 | — |
| TRA2B | 0.876 | 0.818 | — |
| U2SURP | 0.837 | 0.778 | — |
| CLK3 | 0.837 | 0.787 | — |
| DHX15 | 0.836 | 0.798 | — |
| SRSF8 | 0.818 | 0.731 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-913075 | psi-mi:"MI:0018"(two hybrid) | pubmed:16249178|imex:IM-19255 |
| E9PD75 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-30059|pubmed:39251607 |
| Nol3 | psi-mi:"MI:0018"(two hybrid) | pubmed:16249178|imex:IM-19255 |
| Srsf7 | psi-mi:"MI:0018"(two hybrid) | pubmed:16249178|imex:IM-19255 |
| Gnrh1 | psi-mi:"MI:0416"(fluorescence microscopy) | pubmed:16249178|imex:IM-19255 |
| YWHAG | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| YTHDC1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| NXF1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| TAF9 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=58.9 + PDB: 无 | pLDDT=58.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoli; 额外: Nucleoplasm, Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TRA2A — Transformer-2 protein homolog alpha，非常新颖，仅有少数基础研究。
2. 蛋白大小282 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 39 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=58.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13595
- Protein Atlas: https://www.proteinatlas.org/ENSG00000164548-TRA2A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TRA2A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13595
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (supported)。来源: https://www.proteinatlas.org/ENSG00000164548-TRA2A/subcellular

![](https://images.proteinatlas.org/54018/849_C4_1_red_green.jpg)
![](https://images.proteinatlas.org/54018/849_C4_2_red_green.jpg)
![](https://images.proteinatlas.org/54018/869_C4_5_red_green.jpg)
![](https://images.proteinatlas.org/54018/869_C4_6_red_green.jpg)
![](https://images.proteinatlas.org/54018/885_C4_1_red_green.jpg)
![](https://images.proteinatlas.org/54018/885_C4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q13595-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
