---
type: protein-evaluation
gene: "KLHL18"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KLHL18 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KLHL18 / KIAA0795 |
| 蛋白名称 | Kelch-like protein 18 |
| 蛋白大小 | 574 aa / 63.6 kDa |
| UniProt ID | O94889 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Nuclear bodies; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 574 aa / 63.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=93.4; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011705, IPR017096, IPR000210, IPR015915, IPR006 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.5/180** | |
| **归一化总分** | | | **70.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear bodies | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- Cul3-RING ubiquitin ligase complex (GO:0031463)
- cytoplasm (GO:0005737)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 12 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0795 |

**关键文献**:
1. Identification of potential therapeutic targeting in ovarian aging from genetic screening with clinical validation.. *Journal of assisted reproduction and genetics*. PMID: 40343599
2. Cul3-Klhl18 ubiquitin ligase modulates rod transducin translocation during light-dark adaptation.. *The EMBO journal*. PMID: 31696965
3. The CUL3-KLHL18 ligase regulates mitotic entry and ubiquitylates Aurora-A.. *Biology open*. PMID: 23213400
4. KLHL18 inhibits the proliferation, migration, and invasion of non-small cell lung cancer by inhibiting PI3K/PD-L1 axis activity.. *Cell & bioscience*. PMID: 33292627
5. Familial Multiple Myeloma: Insights From Epidemiology and Underlying Germline Genetic Predisposition to the Clinic.. *Clinical lymphoma, myeloma & leukemia*. PMID: 39947961

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.4 |
| 高置信度残基 (pLDDT>90) 占比 | 84.1% |
| 置信残基 (pLDDT 70-90) 占比 | 13.6% |
| 中等置信 (pLDDT 50-70) 占比 | 0.9% |
| 低置信 (pLDDT<50) 占比 | 1.4% |
| 有序区域 (pLDDT>70) 占比 | 97.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=93.4，有序区 97.7%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011705, IPR017096, IPR000210, IPR015915, IPR006652; Pfam: PF07707, PF00651, PF01344 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CUL3 | 0.910 | 0.829 | — |
| UBE2M | 0.640 | 0.623 | — |
| KCTD2 | 0.615 | 0.071 | — |
| EEF1G | 0.593 | 0.590 | — |
| KIF9 | 0.583 | 0.000 | — |
| TBRG4 | 0.581 | 0.000 | — |
| NUDCD3 | 0.548 | 0.528 | — |
| ESPNL | 0.541 | 0.045 | — |
| CCDC12 | 0.517 | 0.000 | — |
| COPS6 | 0.508 | 0.508 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| COPS5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| COPS6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| Neto | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| CUL3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| CUL5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| DCUN1D1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| PCMT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| UBE2M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ATP6V1G1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CFH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.4 + PDB: 无 | pLDDT=93.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. KLHL18 — Kelch-like protein 18，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小574 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O94889
- Protein Atlas: https://www.proteinatlas.org/ENSG00000114648-KLHL18/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KLHL18
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O94889
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000114648-KLHL18/subcellular

![](https://images.proteinatlas.org/35028/1216_D3_1_red_green.jpg)
![](https://images.proteinatlas.org/35028/1216_D3_4_red_green.jpg)
![](https://images.proteinatlas.org/35028/563_F11_1_red_green.jpg)
![](https://images.proteinatlas.org/35028/563_F11_2_red_green.jpg)
![](https://images.proteinatlas.org/35028/566_F11_1_red_green.jpg)
![](https://images.proteinatlas.org/35028/566_F11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O94889-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O94889 |
| SMART | SM00875;SM00225;SM00612; |
| UniProt Domain [FT] | DOMAIN 66..105; /note="BTB"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00037"; DOMAIN 140..242; /note="BACK" |
| InterPro | IPR011705;IPR017096;IPR000210;IPR015915;IPR006652;IPR030603;IPR011333; |
| Pfam | PF07707;PF00651;PF01344;PF24681; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000114648-KLHL18/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AURKA | Biogrid | false |
| COPS3 | Biogrid | false |
| COPS5 | Biogrid | false |
| COPS6 | Biogrid | false |
| CUL3 | Biogrid | false |
| RBX1 | Biogrid | false |
| UBE2M | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
