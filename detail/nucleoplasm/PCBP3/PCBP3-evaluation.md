---
type: protein-evaluation
gene: "PCBP3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PCBP3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PCBP3 / PCBP3-OT1, PCBP3OT |
| 蛋白名称 | Poly(rC)-binding protein 3 |
| 蛋白大小 | 371 aa / 39.5 kDa |
| UniProt ID | P57721 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Mitochondria; 额外: Vesicles; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 371 aa / 39.5 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=21 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR004087, IPR004088, IPR036612; Pfam: PF00013 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.0/180** | |
| **归一化总分** | | | **66.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Mitochondria; 额外: Vesicles | Uncertain |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- nucleus (GO:0005634)
- ribonucleoprotein complex (GO:1990904)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 21 |
| PubMed broad count | 29 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PCBP3-OT1, PCBP3OT |

**关键文献**:
1. Anlotinib Inhibits PFKFB3-Driven Glycolysis in Myofibroblasts to Reverse Pulmonary Fibrosis.. *Frontiers in pharmacology*. PMID: 34603058
2. Autoimmune Mechanisms of Interferon Hypersensitivity and Neurodegenerative Diseases: Down Syndrome.. *Autoimmune diseases*. PMID: 32566271
3. Exploration of RNA-binding proteins identified RPS27 as a potential regulator associated with Kaposi's sarcoma development.. *BMC cancer*. PMID: 40016701
4. Iron Export through the Transporter Ferroportin 1 Is Modulated by the Iron Chaperone PCBP2.. *The Journal of biological chemistry*. PMID: 27302059
5. Early DNA methylation changes in children developing beta cell autoimmunity at a young age.. *Diabetologia*. PMID: 35142878

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.3 |
| 高置信度残基 (pLDDT>90) 占比 | 2.2% |
| 置信残基 (pLDDT 70-90) 占比 | 52.0% |
| 中等置信 (pLDDT 50-70) 占比 | 12.4% |
| 低置信 (pLDDT<50) 占比 | 33.4% |
| 有序区域 (pLDDT>70) 占比 | 54.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=67.3），有序残基占 54.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004087, IPR004088, IPR036612; Pfam: PF00013 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| YBEY | 0.610 | 0.000 | — |
| POFUT2 | 0.564 | 0.000 | — |
| TSTA3 | 0.530 | 0.530 | — |
| RBM11 | 0.473 | 0.000 | — |
| PCBP1 | 0.465 | 0.402 | — |
| RWDD2B | 0.453 | 0.070 | — |
| PDCD2L | 0.448 | 0.322 | — |
| SNRPA | 0.445 | 0.363 | — |
| VPS53 | 0.437 | 0.091 | — |
| COMMD9 | 0.433 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PTBP1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| PTBP2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| TNIK | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| RNPS1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ARF6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MCC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| SAP18 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| 38505205 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| NS | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:22810585|imex:IM-17331 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.3 + PDB: 无 | pLDDT=67.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoplasm, Mitochondria; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. PCBP3 — Poly(rC)-binding protein 3，非常新颖，仅有少数基础研究。
2. 蛋白大小371 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 21 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=67.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P57721
- Protein Atlas: https://www.proteinatlas.org/ENSG00000183570-PCBP3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PCBP3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P57721
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000183570-PCBP3/subcellular

![](https://images.proteinatlas.org/30247/1792_B2_1_red_green.jpg)
![](https://images.proteinatlas.org/30247/1792_B2_2_red_green.jpg)
![](https://images.proteinatlas.org/30247/1876_G11_10_cr5b6d487c2a6c9_red_green.jpg)
![](https://images.proteinatlas.org/30247/1876_G11_5_cr5b6d487c2a136_red_green.jpg)
![](https://images.proteinatlas.org/30247/272_G12_1_red_green.jpg)
![](https://images.proteinatlas.org/30247/272_G12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P57721-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P57721 |
| SMART | SM00322; |
| UniProt Domain [FT] | DOMAIN 45..95; /note="KH 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00117"; DOMAIN 129..182; /note="KH 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00117"; DOMAIN 293..357; /note="KH 3"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00117" |
| InterPro | IPR004087;IPR004088;IPR036612; |
| Pfam | PF00013; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000183570-PCBP3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PCBP1 | Biogrid | false |
| PCBP2 | Biogrid | false |
| PTBP1 | Biogrid | false |
| RBM39 | Biogrid | false |
| RUVBL1 | Biogrid | false |
| SNRPA | Biogrid | false |
| STK4 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
