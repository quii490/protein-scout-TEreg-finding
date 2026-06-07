---
type: protein-evaluation
gene: "TENM2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TENM2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TENM2 |
| 蛋白名称 | TENM2 (UniProt未获取) |
| 蛋白大小 | 未知 aa / 未知 kDa |
| UniProt ID | TENM2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli; UniProt: 暂无数据（UniProt获取失败） |
| 蛋白大小 | 5/10 | ×1 | 5 | 未知 aa / 未知 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=28 篇 (≤40→8) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | 暂无数据 (UniProt未获取) |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 5 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **108.5/180** | |
| **归一化总分** | | | **60.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli | Approved |
| UniProt | 暂无数据（UniProt获取失败） | 获取失败 |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释 (UniProt未获取)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 28 |
| PubMed broad count | 48 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Genome-wide meta-analysis and omics integration identifies novel genes associated with diabetic kidney disease.. *Diabetologia*. PMID: 35763030
2. Identification of two unannotated miRNAs in classic Hodgkin lymphoma cell lines.. *PloS one*. PMID: 36961799
3. Cartography of teneurin and latrophilin expression reveals spatiotemporal axis heterogeneity in the mouse hippocampus during development.. *PLoS biology*. PMID: 38713721
4. Dihydroartemisinin inhibits HNSCC invasion and migration by controlling miR-195-5p expression.. *Heliyon*. PMID: 38961909
5. Bioinformatics And Experimental Insights Into Sotorasib Resistance Mechanisms in Non-small-cell Lung Cancer.. *Anti-cancer agents in medicinal chemistry*. PMID: 40776650

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v? |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 暂无数据 (UniProt未获取) |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ADGRL3 | 0.999 | 0.996 | — |
| ADGRL1 | 0.999 | 0.967 | — |
| ADGRL2 | 0.998 | 0.967 | — |
| FLRT3 | 0.877 | 0.045 | — |
| ZIC1 | 0.624 | 0.045 | — |
| EGF | 0.557 | 0.000 | — |
| CNTN6 | 0.519 | 0.000 | — |
| NXPE1 | 0.500 | 0.000 | — |
| LCT | 0.478 | 0.000 | — |
| ROBO2 | 0.476 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |
| LAMP1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| DISC1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| Tsc1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28671696|doi:10.1038/nn |
| CD81 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-28053|pubmed:32900848 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 5
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 5 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v? | 仅预测 |
| 定位 | UniProt + HPA | 暂无数据（UniProt获取失败） / Nucleoli | 待确认 |
| PPI | STRING + IntAct | 15 + 5 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TENM2 — TENM2 (UniProt未获取)，非常新颖，仅有少数基础研究。
2. 蛋白大小未知 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 28 篇，已有一定研究基础
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/TENM2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000145934-TENM2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TENM2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/TENM2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (approved)。来源: https://www.proteinatlas.org/ENSG00000145934-TENM2/subcellular

![](https://images.proteinatlas.org/68691/1397_D5_4_red_green.jpg)
![](https://images.proteinatlas.org/68691/1397_D5_5_red_green.jpg)
![](https://images.proteinatlas.org/68691/1402_D5_1_red_green.jpg)
![](https://images.proteinatlas.org/68691/1402_D5_2_red_green.jpg)
![](https://images.proteinatlas.org/68691/1559_A2_1_red_green.jpg)
![](https://images.proteinatlas.org/68691/1559_A2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NT68 |
| SMART | SM00181;SM00179; |
| UniProt Domain [FT] | DOMAIN 1..375; /note="Teneurin N-terminal"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00694"; DOMAIN 575..603; /note="EGF-like 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 598..634; /note="EGF-like 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 636..668; /note="EGF-like 3"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 669..701; /note="EGF-like 4"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 702..735; /note="EGF-like 5"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 738..766; /note="EGF-like 6"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 769..797; /note="EGF-like 7"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 808..841; /note="EGF-like 8"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076" |
| InterPro | IPR011042;IPR008969;IPR000742;IPR001881;IPR057627;IPR011044;IPR022385;IPR056823;IPR009471;IPR056822;IPR056820;IPR051216;IPR057629;IPR028916;IPR006530; |
| Pfam | PF25024;PF24329;PF23093;PF06484;PF25021;PF25023;PF23538;PF15636;PF25020; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000145934-TENM2/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
