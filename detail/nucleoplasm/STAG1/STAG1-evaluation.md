---
type: protein-evaluation
gene: "STAG1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## STAG1 — REJECTED (研究热度过高 (PubMed strict=102，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | STAG1 / STAG1, TMEPAI |
| 蛋白名称 | Protein TMEPAI |
| 蛋白大小 | 287 aa / 31.6 kDa |
| UniProt ID | Q969W9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Nuclear bodies, Primary cilium; UniProt: Early endosome membrane; Golgi apparatus membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 287 aa / 31.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=102 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=56.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR043445 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **68.0/180** | |
| **归一化总分** | | | **37.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear bodies, Primary cilium | Supported |
| UniProt | Early endosome membrane; Golgi apparatus membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- early endosome membrane (GO:0031901)
- endosome membrane (GO:0010008)
- Golgi membrane (GO:0000139)
- membrane (GO:0016020)
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 102 |
| PubMed broad count | 154 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: STAG1, TMEPAI |

**关键文献**:
1. STAG1 mutations cause a novel cohesinopathy characterised by unspecific syndromic intellectual disability.. *Journal of medical genetics*. PMID: 28119487
2. STAG2 mutations reshape the cohesin-structured spatial chromatin architecture to drive gene regulation in acute myeloid leukemia.. *Cell reports*. PMID: 39084219
3. Whole-exome sequencing analysis identifies risk genes for schizophrenia.. *Nature communications*. PMID: 40753099
4. STAG2 regulates interferon signaling in melanoma via enhancer loop reprogramming.. *Nature communications*. PMID: 35388001
5. A Novel Variant of STAG1 Gene and Literature Review.. *Annals of human genetics*. PMID: 40899458

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 56.7 |
| 高置信度残基 (pLDDT>90) 占比 | 7.0% |
| 置信残基 (pLDDT 70-90) 占比 | 12.2% |
| 中等置信 (pLDDT 50-70) 占比 | 36.2% |
| 低置信 (pLDDT<50) 占比 | 44.6% |
| 有序区域 (pLDDT>70) 占比 | 19.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=56.7），有序残基占 19.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR043445 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| WAPL | 0.999 | 0.869 | — |
| SMC1A | 0.999 | 0.993 | — |
| RAD21 | 0.999 | 0.999 | — |
| SMC3 | 0.999 | 0.999 | — |
| PDS5A | 0.999 | 0.731 | — |
| SMC1B | 0.998 | 0.895 | — |
| NIPBL | 0.997 | 0.956 | — |
| STAG2 | 0.996 | 0.792 | — |
| REC8 | 0.994 | 0.505 | — |
| PDS5B | 0.990 | 0.916 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| smc1a | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:10931856 |
| smc3 | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:10931856 |
| rad21 | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:10931856 |
| WAPL | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12007|pubmed:17113138 |
| PDS5B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12007|pubmed:17113138 |
| PDS5A | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12007|pubmed:17113138 |
| PMEPA1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| alaS | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| HDAC11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-18733|pubmed:23752268 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 3 / 15 = 20%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 20%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=56.7 + PDB: 无 | pLDDT=56.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Early endosome membrane; Golgi apparatus membrane / Nucleoplasm; 额外: Nuclear bodies, Primary cilium | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. STAG1 — Protein TMEPAI，研究基础较多，新颖性有限。
2. 蛋白大小287 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 102 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=56.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 102 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q969W9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000118007-STAG1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=STAG1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q969W9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000118007-STAG1/subcellular

![](https://images.proteinatlas.org/35015/2183_F9_25_red_green.jpg)
![](https://images.proteinatlas.org/35015/2183_F9_51_red_green.jpg)
![](https://images.proteinatlas.org/35015/2206_F11_13_red_green.jpg)
![](https://images.proteinatlas.org/35015/2206_F11_53_red_green.jpg)
![](https://images.proteinatlas.org/35015/2232_A7_19_red_green.jpg)
![](https://images.proteinatlas.org/35015/2232_A7_42_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q969W9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
