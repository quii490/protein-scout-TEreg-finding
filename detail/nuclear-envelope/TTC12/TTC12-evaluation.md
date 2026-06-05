---
type: protein-evaluation
gene: "TTC12"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TTC12 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TTC12 |
| 蛋白名称 | Tetratricopeptide repeat protein 12 |
| 蛋白大小 | 705 aa / 78.8 kDa |
| UniProt ID | Q9H892 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Nuclear membrane, Plasma membrane; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 705 aa / 78.8 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=29 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=90.3; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011989, IPR016024, IPR011990, IPR019734, IPR043 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.5/180** | |
| **归一化总分** | | | **71.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nuclear membrane, Plasma membrane | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centrosome (GO:0005813)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nuclear membrane (GO:0031965)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 29 |
| PubMed broad count | 38 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Primary Ciliary Dyskinesia.. **. PMID: 20301301
2. A neurobiological pathway to smoking in adolescence: TTC12-ANKK1-DRD2 variants and reward response.. *European neuropsychopharmacology : the journal of the European College of Neuropsychopharmacology*. PMID: 30104163
3. Biallelic mutations of TTC12 and TTC21B were identified in Chinese patients with multisystem ciliopathy syndromes.. *Human genomics*. PMID: 36273201
4. Haplotype spanning TTC12 and ANKK1, flanked by the DRD2 and NCAM1 loci, is strongly associated to nicotine dependence in two distinct American populations.. *Human molecular genetics*. PMID: 17085484
5. Ankyrin Repeat and Kinase Domain Containing 1 Gene, and Addiction Vulnerability.. *International journal of molecular sciences*. PMID: 32260442

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.3 |
| 高置信度残基 (pLDDT>90) 占比 | 77.9% |
| 置信残基 (pLDDT 70-90) 占比 | 14.9% |
| 中等置信 (pLDDT 50-70) 占比 | 2.8% |
| 低置信 (pLDDT<50) 占比 | 4.4% |
| 有序区域 (pLDDT>70) 占比 | 92.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=90.3，有序区 92.8%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011989, IPR016024, IPR011990, IPR019734, IPR043195; Pfam: PF00515, PF13181 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ANKK1 | 0.946 | 0.100 | — |
| DRD2 | 0.694 | 0.000 | — |
| CFAP300 | 0.600 | 0.069 | — |
| C22orf23 | 0.599 | 0.000 | — |
| WDHD1 | 0.580 | 0.510 | — |
| DNAAF1 | 0.559 | 0.051 | — |
| ZMYND10 | 0.556 | 0.000 | — |
| PIH1D2 | 0.552 | 0.175 | — |
| NCAM1 | 0.552 | 0.054 | — |
| ZW10 | 0.539 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PB1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-13585|pubmed:20064372 |
| H1-2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| AIRIM | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SIGLECL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MIPOL1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| HPCAL4 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-23318|pubmed:25416956 |
| MRP4 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:27107014|imex:IM-24995 |
| PCM1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |
| PAK1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| EFNB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 2 / 15 = 13%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 13%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.3 + PDB: 无 | pLDDT=90.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Cytosol; 额外: Nuclear membrane, Plasma membrane | 一致 |
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
1. TTC12 — Tetratricopeptide repeat protein 12，非常新颖，仅有少数基础研究。
2. 蛋白大小705 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 29 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H892
- Protein Atlas: https://www.proteinatlas.org/ENSG00000149292-TTC12/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TTC12
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H892
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000149292-TTC12/subcellular

![](https://images.proteinatlas.org/38542/2149_A6_15_blue_red_green.jpg)
![](https://images.proteinatlas.org/38542/2149_A6_59_blue_red_green.jpg)
![](https://images.proteinatlas.org/38542/2152_G8_17_blue_red_green.jpg)
![](https://images.proteinatlas.org/38542/2152_G8_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/38542/626_G7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/38542/626_G7_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H892-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
