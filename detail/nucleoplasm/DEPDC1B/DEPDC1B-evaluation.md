---
type: protein-evaluation
gene: "DEPDC1B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DEPDC1B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DEPDC1B / XTP8 |
| 蛋白名称 | DEP domain-containing protein 1B |
| 蛋白大小 | 529 aa / 61.8 kDa |
| UniProt ID | Q8WUY9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Golgi apparatus; 额外: Nucleoplasm, Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | x1 | 10 | 529 aa / 61.8 kDa |
| 研究新颖性 | 6/10 | x5 | 30 | PubMed strict=49 篇 (<=60->6) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=77.7; PDB: 无 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR000591, IPR008936, IPR000198, IPR036388, IPR036 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **101.0/180** | |
| **归一化总分** | | | **56.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Nucleoplasm, Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TremBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 49 |
| PubMed broad count | 69 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: XTP8 |

**关键文献**:
1. DEPDC1B promotes colorectal cancer via facilitating cell proliferation and migration while inhibiting apoptosis.. *Cell cycle (Georgetown, Tex.)*. PMID: 36016512
2. Illuminating DEPDC1B in Multi-pronged Regulation of Tumor Progression.. *Methods in molecular biology (Clifton, N.J.)*. PMID: 37191806
3. Role of DEP domain-containing protein 1B (DEPDC1B) in epithelial ovarian cancer.. *Journal of Cancer*. PMID: 37056386
4. DEPDC1B-mediated USP5 deubiquitination of β-catenin promotes breast cancer metastasis by activating the wnt/β-catenin pathway.. *American journal of physiology. Cell physiology*. PMID: 37642235
5. DEPDC1B: A novel tumor suppressor gene associated with immune infiltration in colon adenocarcinoma.. *Cancer medicine*. PMID: 39087856

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.7 |
| 高置信度残基 (pLDDT>90) 占比 | 37.6% |
| 置信残基 (pLDDT 70-90) 占比 | 35.2% |
| 中等置信 (pLDDT 50-70) 占比 | 9.5% |
| 低置信 (pLDDT<50) 占比 | 17.8% |
| 有序区域 (pLDDT>70) 占比 | 72.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=77.7，有序区 72.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000591, IPR008936, IPR000198, IPR036388, IPR036390; Pfam: PF00610, PF00620 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DLGAP5 | 0.878 | 0.000 | — |
| CCNB1 | 0.845 | 0.000 | — |
| KIF11 | 0.842 | 0.000 | — |
| CEP55 | 0.834 | 0.000 | — |
| KIF14 | 0.822 | 0.000 | — |
| KIF15 | 0.817 | 0.000 | — |
| HMMR | 0.812 | 0.049 | — |
| NUF2 | 0.810 | 0.000 | — |
| DEPDC1 | 0.798 | 0.000 | — |
| BUB1B | 0.797 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBPL | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| LAMP1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| RAB9A | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| TGOLN2 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| COQ8A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| ARHGEF12 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| ERLIN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| GSN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| HUWE1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| MRPS18B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.7 + PDB: 无 | pLDDT=77.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Golgi apparatus; 额外: Nucleoplasm, Cytosol | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ***

**核心优势**:
1. DEPDC1B -- DEP domain-containing protein 1B，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小529 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 49 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WUY9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000035499-DEPDC1B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DEPDC1B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WUY9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (approved)。来源: https://www.proteinatlas.org/ENSG00000035499-DEPDC1B/subcellular

![](https://images.proteinatlas.org/38255/411_D4_1_red_green.jpg)
![](https://images.proteinatlas.org/38255/411_D4_2_red_green.jpg)
![](https://images.proteinatlas.org/38255/415_D4_1_red_green.jpg)
![](https://images.proteinatlas.org/38255/415_D4_4_red_green.jpg)
![](https://images.proteinatlas.org/38255/416_D4_1_red_green.jpg)
![](https://images.proteinatlas.org/38255/416_D4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8WUY9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8WUY9 |
| SMART | SM00049; |
| UniProt Domain [FT] | DOMAIN 24..108; /note="DEP"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00066"; DOMAIN 201..393; /note="Rho-GAP"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00172" |
| InterPro | IPR000591;IPR008936;IPR000198;IPR036388;IPR036390; |
| Pfam | PF00610;PF00620; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000035499-DEPDC1B/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CDC23 | Biogrid, Opencell | true |
| ANAPC1 | Opencell | false |
| ANAPC4 | Opencell | false |
| CDC16 | Opencell | false |
| KRAS | Biogrid | false |
| LAMP1 | Biogrid | false |
| NRAS | Biogrid | false |
| PTPRF | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
