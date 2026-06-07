---
type: protein-evaluation
gene: "Csnk1e"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## Csnk1e — REJECTED (研究热度过高 (PubMed strict=110，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | Csnk1e |
| 蛋白名称 | Casein kinase I isoform epsilon |
| 蛋白大小 | 416 aa / 47.3 kDa |
| UniProt ID | P49674 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 416 aa / 47.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=110 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=79.2; PDB: 4HNI, 4HOK |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR050235, IPR011009, IPR000719, IPR017441, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **90.0/180** | |
| **归一化总分** | | | **50.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- growth cone (GO:0030426)
- neuronal cell body (GO:0043025)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- ribonucleoprotein complex (GO:1990904)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 110 |
| PubMed broad count | 135 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Casein kinase 1 family member CSNK1E can regulate proliferation and migration in hepatocellular carcinoma.. *Journal of cancer research and clinical oncology*. PMID: 41014359
2. CK1δ/ε-mediated TDP-43 phosphorylation contributes to early motor neuron disease toxicity in amyotrophic lateral sclerosis.. *Acta neuropathologica communications*. PMID: 39633494
3. Genetic association study of CSNK1E gene in bipolar disorder and circadian characteristics.. *Nordic journal of psychiatry*. PMID: 30445897
4. Exome sequencing identifies genes for socioeconomic status in 350,770 individuals.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 39772748
5. Altered CSNK1E, FABP4 and NEFH protein levels in the dorsolateral prefrontal cortex in schizophrenia.. *Schizophrenia research*. PMID: 27236410

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.2 |
| 高置信度残基 (pLDDT>90) 占比 | 63.9% |
| 置信残基 (pLDDT 70-90) 占比 | 5.8% |
| 中等置信 (pLDDT 50-70) 占比 | 5.5% |
| 低置信 (pLDDT<50) 占比 | 24.8% |
| 有序区域 (pLDDT>70) 占比 | 69.7% |
| 可用 PDB 条目 | 4HNI, 4HOK |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（4HNI, 4HOK）+ AlphaFold高质量预测（pLDDT=79.2），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050235, IPR011009, IPR000719, IPR017441, IPR008271; Pfam: PF00069 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PER2 | 0.999 | 0.890 | — |
| CRY1 | 0.999 | 0.968 | — |
| ARNTL | 0.997 | 0.696 | — |
| CRY2 | 0.997 | 0.757 | — |
| PER1 | 0.996 | 0.897 | — |
| PER3 | 0.994 | 0.551 | — |
| CLOCK | 0.994 | 0.558 | — |
| AXIN1 | 0.993 | 0.617 | — |
| GSK3B | 0.989 | 0.086 | — |
| CSNK1D | 0.989 | 0.831 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSMUSP00000113975.2 | psi-mi:"MI:0018"(two hybrid) | pubmed:23555304|imex:IM-20564 |
| DVL2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| RAD54B | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CCNA1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MCC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| AXIN1 | psi-mi:"MI:0663"(confocal microscopy) | imex:IM-15364|pubmed:21988832 |
| FAM110C | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| ENTR1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| TNS2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| FAM110A | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.2 + PDB: 4HNI, 4HOK | pLDDT=79.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. Csnk1e — Casein kinase I isoform epsilon，研究基础较多，新颖性有限。
2. 蛋白大小416 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 110 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 110 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P49674
- Protein Atlas: https://www.proteinatlas.org/search/Csnk1e
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=Csnk1e
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P49674
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000213923-CSNK1E/subcellular

![](https://images.proteinatlas.org/9626/921_G6_1_red_green.jpg)
![](https://images.proteinatlas.org/9626/921_G6_3_red_green.jpg)
![](https://images.proteinatlas.org/9626/923_G6_2_red_green.jpg)
![](https://images.proteinatlas.org/9626/923_G6_3_red_green.jpg)
![](https://images.proteinatlas.org/9626/931_G6_1_red_green.jpg)
![](https://images.proteinatlas.org/9626/931_G6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P49674-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P49674 |
| SMART | SM00220; |
| UniProt Domain [FT] | DOMAIN 9..277; /note="Protein kinase"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00159" |
| InterPro | IPR050235;IPR011009;IPR000719;IPR017441;IPR008271; |
| Pfam | PF00069; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000213923-CSNK1E/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| APC | Intact, Biogrid | true |
| AXIN1 | Intact, Biogrid | true |
| CRY1 | Biogrid, Opencell, Bioplex | true |
| CSNK1D | Biogrid, Opencell | true |
| DVL2 | Intact, Biogrid | true |
| FAM110A | Intact, Biogrid | true |
| FAM110C | Intact, Biogrid, Bioplex | true |
| FAM83D | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
