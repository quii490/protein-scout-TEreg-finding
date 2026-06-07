---
type: protein-evaluation
gene: "BEND5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BEND5 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BEND5 / C1orf165 |
| 蛋白名称 | BEN domain-containing protein 5 |
| 蛋白大小 | 421 aa / 48.2 kDa |
| UniProt ID | Q7L4P6 |
| 评估日期 | 2026-06-03 |
| 数据采集时间 | 2026-06-03 03:34:48 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 10/10 | x4 | 40 | HPA: Nuclear speckles |
| 蛋白大小 | 10/10 | x1 | 10 | 421 aa / 48.2 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=17 篇 (<=20->10) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=73.4 |
| 调控结构域 | 5/10 | x2 | 10 | InterPro: 2; Pfam: 1; IPR018379, IPR040391 |
| PPI 网络 | 8/10 | x3 | 24 | STRING 9 partners; IntAct 15 interactions |
| 互证加分 | -- | max +3 | 1.0 | STRING + IntAct 双源验证: +0.5; 结构域 + AlphaFold 质量: +0.5 |
| **原始总分** | | | **156.0/180** | |
| **归一化总分 (/1.83)** | | | **85.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles; 额外: Nuclear speckles, Cytosol | Approved |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- Golgi apparatus (GO:0005794)

**结论**: 核定位证据充分，多个数据源一致支持核定位，定位特异性高。

#### 3.2 蛋白大小评估

**评价**: 421 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 17 |
| PubMed broad count | 41 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C1orf165 |

**关键文献**:
1. Interaction between BEND5 and RBPJ suppresses breast cancer growth and metastasis via inhibiting Notch signaling.. *International journal of biological sciences*. PMID: 35844785
2. Hypermethylation of BEND5 contributes to cell proliferation and is a prognostic marker of colorectal cancer.. *Oncotarget*. PMID: 29371920
3. NLRP3 Inhibition Reduces rt-PA Induced Endothelial Dysfunction under Ischemic Conditions.. *Biomedicines*. PMID: 35453512
4. Bend family proteins mark chromatin boundaries and synergistically promote early germ cell differentiation.. *Protein & cell*. PMID: 34731408
5. Evaluation of bEnd5 cell line as an in vitro model for the blood-brain barrier under normal and hypoxic/aglycemic conditions.. *Journal of pharmaceutical sciences*. PMID: 17828743

**评价**: 极度新颖，几乎未被系统研究（PubMed <= 20篇）。新颖性评分 10/10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.4 |
| 高置信度残基 (pLDDT>90) 占比 | 38.2% |
| 置信残基 (pLDDT 70-90) 占比 | 26.8% |
| 中等置信 (pLDDT 50-70) 占比 | 8.3% |
| 低置信 (pLDDT<50) 占比 | 26.6% |
| 有序区域 (pLDDT>70) 占比 | 65.0% |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold中等质量预测（pLDDT=73.4），存在部分低置信区域。三维结构评分 7/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR018379, IPR040391; Pfam: PF10523 |

**染色质调控潜力分析**: 存在 3 个已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score > 0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BEND3 | 0.423 | 0.045 | -- |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CTNNBIP1 | two hybrid pooling approach | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 |
| USP2 | two hybrid pooling approach | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 |
| GRAP2 | two hybrid pooling approach | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 |
| DDR1 | two hybrid pooling approach | pubmed:16169070|imex:IM-16517|mint:MINT-5217955 |
| GFI1B | two hybrid | pubmed:16713569|imex:IM-11827|mint:MINT-5218676 |
| USP7 | two hybrid | pubmed:16713569|imex:IM-11827|mint:MINT-5218676 |
| MAP1LC3A | anti tag coimmunoprecipitation | pubmed:20562859|imex:IM-15184 |
| ERBB3 | ubiquitin reconstruction | pubmed:31980649|imex:IM-26434 |
| GORASP2 | two hybrid array | pubmed:29892012|doi:10.1038/s41588-018-0130-z|imex:IM-27553 |
| PTGR2 | two hybrid array | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 9，IntAct interactions: 15

**评价**: 互作网络中等：STRING 9 预测 + IntAct 15 实验互作。PPI 评分 8/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold v6 | pLDDT=73.4 | 单一来源 |
| 定位 | HPA | Nuclear speckles | 单一来源 |
| PPI | STRING + IntAct | 9 + 15 interactions | 数据充分 |

**互证加分明细**:
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
**总分**: +1.0 / max +3

### 4. 总体评价

**归一化总分**: 85.2/100

**核心优势**:
1. BEND5 -- BEN domain-containing protein 5，极度新颖，几乎未被系统研究（PubMed <= 20篇）。
2. 蛋白大小421 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。
3. 存在 3 个已知结构域，有明确的结构-功能切入点。
4. 核定位信号明确，多个数据源一致支持。

**风险/不确定性**:
1. 暂无PDB实验结构，结构证据完全依赖AlphaFold预测

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] 考虑通过AlphaFold预测 + MD模拟获取结构信息

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q7L4P6
- Protein Atlas: https://www.proteinatlas.org/search/BEND5
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BEND5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7L4P6
- STRING: https://string-db.org/network/9606.BEND5
- Packet data timestamp: 2026-06-03 03:34:48

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (approved)。来源: https://www.proteinatlas.org/ENSG00000162373-BEND5/subcellular

![](https://images.proteinatlas.org/54347/1057_G11_3_red_green.jpg)
![](https://images.proteinatlas.org/54347/1057_G11_4_red_green.jpg)
![](https://images.proteinatlas.org/54347/1391_C5_2_red_green.jpg)
![](https://images.proteinatlas.org/54347/1391_C5_3_red_green.jpg)
![](https://images.proteinatlas.org/54347/1817_G1_1_red_green.jpg)
![](https://images.proteinatlas.org/54347/1817_G1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q7L4P6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q7L4P6 |
| SMART | SM01025; |
| UniProt Domain [FT] | DOMAIN 302..408; /note="BEN"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00784" |
| InterPro | IPR018379;IPR040391; |
| Pfam | PF10523; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000162373-BEND5/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| GORASP2 | Intact, Biogrid | true |
| PRKAB2 | Intact, Biogrid | true |
| BUD31 | Intact | false |
| EIF3D | Intact | false |
| FAM161A | Intact | false |
| LCE1B | Intact | false |
| NTAQ1 | Intact | false |
| PIMREG | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
