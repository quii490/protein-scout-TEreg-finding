---
type: protein-evaluation
gene: "LRP10"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LRP10 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LRP10 / KIAA0816, LRP10, MEGF7 |
| 蛋白名称 | Low-density lipoprotein receptor-related protein 4 |
| 蛋白大小 | 1905 aa / 212.0 kDa |
| UniProt ID | O75096 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Nucleoli; UniProt: Cell membrane |
| 蛋白大小 | 5/10 | ×1 | 5 | 1905 aa / 212.0 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=58 篇 (≤60→6) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=77.1; PDB: 8S9P |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011042, IPR026823, IPR000742, IPR001881, IPR018 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.5/180** | |
| **归一化总分** | | | **53.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli | Approved |
| UniProt | Cell membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cell surface (GO:0009986)
- dendrite (GO:0030425)
- neuromuscular junction (GO:0031594)
- neuronal cell body (GO:0043025)
- plasma membrane (GO:0005886)
- plasma membrane raft (GO:0044853)
- postsynaptic density (GO:0014069)
- synaptic membrane (GO:0097060)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 58 |
| PubMed broad count | 79 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0816, LRP10, MEGF7 |

**关键文献**:
1. Monogenic Parkinson's Disease: Genotype, Phenotype, Pathophysiology, and Genetic Testing.. *Genes*. PMID: 35328025
2. Parkinson's disease - genetic cause.. *Current opinion in neurology*. PMID: 37366140
3. Sex specific molecular networks and key drivers of Alzheimer's disease.. *Molecular neurodegeneration*. PMID: 37340466
4. The role of genetics in Parkinson's disease: a large cohort study in Chinese mainland population.. *Brain : a journal of neurology*. PMID: 32613234
5. LRP10 and α-synuclein transmission in Lewy body diseases.. *Cellular and molecular life sciences : CMLS*. PMID: 38315424

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.1 |
| 高置信度残基 (pLDDT>90) 占比 | 32.9% |
| 置信残基 (pLDDT 70-90) 占比 | 42.6% |
| 中等置信 (pLDDT 50-70) 占比 | 10.9% |
| 低置信 (pLDDT<50) 占比 | 13.6% |
| 有序区域 (pLDDT>70) 占比 | 75.5% |
| 可用 PDB 条目 | 8S9P |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=77.1，有序区 75.5%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011042, IPR026823, IPR000742, IPR001881, IPR018097; Pfam: PF12662, PF14670, PF00057 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| LRP4 | psi-mi:"MI:0018"(two hybrid) | pubmed:12421765 |
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| rpoB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| Q81R13 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ARRB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:17620599 |
| MX1 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| SOST | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZFP41 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TGFBR2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MGST3 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.1 + PDB: 8S9P | pLDDT=77.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane / Nucleoplasm; 额外: Nucleoli | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. LRP10 — Low-density lipoprotein receptor-related protein 4，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小1905 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 58 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75096
- Protein Atlas: https://www.proteinatlas.org/ENSG00000197324-LRP10/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LRP10
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75096
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000197324-LRP10/subcellular

![](https://images.proteinatlas.org/932/1034_H5_2_red_green.jpg)
![](https://images.proteinatlas.org/932/1034_H5_3_red_green.jpg)
![](https://images.proteinatlas.org/932/1386_C6_1_red_green.jpg)
![](https://images.proteinatlas.org/932/1386_C6_2_red_green.jpg)
![](https://images.proteinatlas.org/932/91_F8_1_red_green.jpg)
![](https://images.proteinatlas.org/932/91_F8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O75096-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O75096 |
| SMART | SM00181;SM00179;SM00192;SM00135; |
| UniProt Domain [FT] | DOMAIN 26..67; /note="LDL-receptor class A 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00124"; DOMAIN 70..106; /note="LDL-receptor class A 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00124"; DOMAIN 109..144; /note="LDL-receptor class A 3"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00124"; DOMAIN 147..183; /note="LDL-receptor class A 4"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00124"; DOMAIN 190..226; /note="LDL-receptor class A 5"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00124"; DOMAIN 230..266; /note="LDL-receptor class A 6"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00124"; DOMAIN 269..305; /note="LDL-receptor class A 7"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00124"; DOMAIN 311..350; /note="LDL-receptor class A 8"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00124"; DOMAIN 354..394; /note="EGF-like 1; calcium-binding"; /evidence="ECO:0000255"; DOMAIN 395..434; /note="EGF-like 2; calcium-binding"; /evidence="ECO:0000255"; DOMAIN 698..737; /note="EGF-like 3" |
| InterPro | IPR011042;IPR026823;IPR000742;IPR001881;IPR018097;IPR009030;IPR036055;IPR051221;IPR023415;IPR000033;IPR002172; |
| Pfam | PF12662;PF14670;PF00057;PF00058; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000197324-LRP10/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ABHD14A | Bioplex | false |
| ADORA2B | Bioplex | false |
| BCL2L2 | Intact | false |
| BCL2L2-PABPN1 | Intact | false |
| C16orf92 | Intact | false |
| CALHM5 | Bioplex | false |
| CISD2 | Intact | false |
| CSNK1G2 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
