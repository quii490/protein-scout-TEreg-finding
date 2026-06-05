---
type: protein-evaluation
gene: "BET1L"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BET1L 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BET1L / GS15 |
| 蛋白名称 | BET1-like protein |
| 蛋白大小 | 111 aa / 12.4 kDa |
| UniProt ID | Q9NYM9 |
| 评估日期 | 2026-06-03 |
| 数据采集时间 | 2026-06-03 03:35:12 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Golgi apparatus; UniProt: Golgi ... |
| 蛋白大小 | 7/10 | x1 | 7 | 111 aa / 12.4 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=14 篇 (<=20->10) |
| 三维结构 | 10/10 | x3 | 30 | AlphaFold v6 pLDDT=89.0 |
| 调控结构域 | 5/10 | x2 | 10 | InterPro: 2; Pfam: 0; IPR039899, IPR000727 |
| PPI 网络 | 10/10 | x3 | 30 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | -- | max +3 | 1.5 | 多库定位一致 (3源): +0.5; STRING + IntAct 双源验证: +0.5; 结构域 + AlphaFold 质量: +0.5 |
| **原始总分** | | | **144.5/180** | |
| **归一化总分 (/1.83)** | | | **79.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Nucleoplasm, Golgi apparatus | Supported |
| UniProt | Golgi apparatus membrane, Golgi apparatus, trans-Golgi network membrane | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- cytosol (GO:0005829)
- endosome (GO:0005768)
- Golgi apparatus (GO:0005794)
- Golgi membrane (GO:0000139)
- Golgi stack (GO:0005795)
- membrane (GO:0016020)
- SNARE complex (GO:0031201)

**结论**: 核定位证据一般，存在混合定位或不一致信号，需进一步实验验证。

#### 3.2 蛋白大小评估

**评价**: 111 aa，蛋白较小，但仍在可操作范围。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 14 |
| PubMed broad count | 36 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GS15 |

**关键文献**:
1. Syntaxin-5's flexibility in SNARE pairing supports Golgi functions.. *Traffic (Copenhagen, Denmark)*. PMID: 37340984
2. Risk of uterine leiomyoma based on BET1L rs2280543 single nucleotide polymorphism and vegetarian diet.. *BMC women's health*. PMID: 35477381
3. A Trans-Ethnic Genome-Wide Association Study of Uterine Fibroids.. *Frontiers in genetics*. PMID: 31249589
4. Genetic Modulation of BET1L Confers Colorectal Cancer Susceptibility by Reducing miRNA Binding and m6A Modification.. *Cancer research*. PMID: 37115853
5. Genome-wide association study reveals BET1L associated with survival time in the 137,693 Japanese individuals.. *Communications biology*. PMID: 36737517

**评价**: 极度新颖，几乎未被系统研究（PubMed <= 20篇）。新颖性评分 10/10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.0 |
| 高置信度残基 (pLDDT>90) 占比 | 70.3% |
| 置信残基 (pLDDT 70-90) 占比 | 21.6% |
| 中等置信 (pLDDT 50-70) 占比 | 7.2% |
| 低置信 (pLDDT<50) 占比 | 0.9% |
| 有序区域 (pLDDT>70) 占比 | 91.9% |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold高质量预测（pLDDT=89.0），预测结构可信。三维结构评分 10/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039899, IPR000727; Pfam: 无 |

**染色质调控潜力分析**: 存在 2 个已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score > 0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GOLGA2 | 0.847 | 0.000 | -- |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GORAB | two hybrid array | imex:IM-15364|pubmed:21988832 |
| TGOLN2 | proximity-dependent biotin identificatio | pubmed:29568061|imex:IM-26301 |
| VAMP5 | pull down | pubmed:30833792|imex:IM-26691 |
| NAPA | pull down | pubmed:30833792|imex:IM-26691 |
| STX18 | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| Uso1 | anti tag coimmunoprecipitation | pubmed:11927603|imex:IM-23550 |
| Gosr1 | anti bait coimmunoprecipitation | pubmed:11927603|imex:IM-23550 |
| Stx5 | anti bait coimmunoprecipitation | pubmed:11927603|imex:IM-23550 |
| Ykt6 | anti bait coimmunoprecipitation | pubmed:11927603|imex:IM-23550 |
| TMEM216 | proximity-dependent biotin identificatio | imex:IM-24512|pubmed:26638075 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15

**评价**: 互作网络丰富：STRING 15 预测 + IntAct 15 实验互作。PPI 评分 10/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold v6 | pLDDT=89.0 | 单一来源 |
| 定位 | HPA | Nucleoplasm | 单一来源 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
**总分**: +1.5 / max +3

### 4. 总体评价

**归一化总分**: 79.0/100

**核心优势**:
1. BET1L -- BET1-like protein，极度新颖，几乎未被系统研究（PubMed <= 20篇）。
2. AlphaFold高质量预测（pLDDT=89.0），结构可信度高。
3. 存在 2 个已知结构域，有明确的结构-功能切入点。

**风险/不确定性**:
1. 核定位信号较弱或存在矛盾（评分 4/10），需IF实验验证
2. 暂无PDB实验结构，结构证据完全依赖AlphaFold预测

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] 考虑通过AlphaFold预测 + MD模拟获取结构信息

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q9NYM9
- Protein Atlas: https://www.proteinatlas.org/search/BET1L
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BET1L
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NYM9
- STRING: https://string-db.org/network/9606.BET1L
- Packet data timestamp: 2026-06-03 03:35:12

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (supported)。来源: https://www.proteinatlas.org/ENSG00000177951-BET1L/subcellular

![](https://images.proteinatlas.org/39819/460_B12_1_red_green.jpg)
![](https://images.proteinatlas.org/39819/460_B12_2_red_green.jpg)
![](https://images.proteinatlas.org/39819/465_B12_1_red_green.jpg)
![](https://images.proteinatlas.org/39819/465_B12_2_red_green.jpg)
![](https://images.proteinatlas.org/39819/467_B12_1_red_green.jpg)
![](https://images.proteinatlas.org/39819/467_B12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NYM9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
