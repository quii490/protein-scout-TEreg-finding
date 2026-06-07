---
type: protein-evaluation
gene: "TBL1Y"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TBL1Y 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TBL1Y / TBL1 |
| 蛋白名称 | F-box-like/WD repeat-containing protein TBL1Y |
| 蛋白大小 | 522 aa / 56.7 kDa |
| UniProt ID | Q9BQ87 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 522 aa / 56.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=86.8; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR045183, IPR006594, IPR015943, IPR020472, IPR019 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **146.5/180** | |
| **归一化总分** | | | **81.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- histone deacetylase complex (GO:0000118)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 21 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TBL1 |

**关键文献**:
1. Y Chromosome Missing Protein, TBL1Y, May Play an Important Role in Cardiac Differentiation.. *Journal of proteome research*. PMID: 28853286
2. Comparing the roles of sex chromosome-encoded protein homologs in gene regulation.. *Genes & development*. PMID: 39048311
3. Embryonic expression patterns of TBL1 family in zebrafish.. *Gene expression patterns : GEP*. PMID: 38272246
4. Footprints of X-to-Y gene conversion in recent human evolution.. *Molecular biology and evolution*. PMID: 19812029
5. TBL1Y: a new gene involved in syndromic hearing loss.. *European journal of human genetics : EJHG*. PMID: 30341416

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.8 |
| 高置信度残基 (pLDDT>90) 占比 | 71.3% |
| 置信残基 (pLDDT 70-90) 占比 | 14.6% |
| 中等置信 (pLDDT 50-70) 占比 | 5.7% |
| 低置信 (pLDDT<50) 占比 | 8.4% |
| 有序区域 (pLDDT>70) 占比 | 85.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=86.8，有序区 85.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR045183, IPR006594, IPR015943, IPR020472, IPR019775; Pfam: PF08513, PF00400 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TBL1XR1 | 0.999 | 0.421 | — |
| GPS2 | 0.999 | 0.702 | — |
| HDAC3 | 0.998 | 0.758 | — |
| NCOR1 | 0.998 | 0.592 | — |
| CTNNB1 | 0.992 | 0.051 | — |
| NCOR2 | 0.991 | 0.645 | — |
| PRKY | 0.983 | 0.055 | — |
| TBL1X | 0.950 | 0.338 | — |
| AMELY | 0.943 | 0.000 | — |
| SKP1 | 0.928 | 0.091 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| HDAC3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MAP3K7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TBL1X | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NCOR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CAPN15 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TCP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DNAJB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CCT6A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CCT5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.8 + PDB: 无 | pLDDT=86.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
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
1. TBL1Y — F-box-like/WD repeat-containing protein TBL1Y，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小522 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BQ87
- Protein Atlas: https://www.proteinatlas.org/ENSG00000092377-TBL1Y/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TBL1Y
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BQ87
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000092377-TBL1Y/subcellular

![](https://images.proteinatlas.org/50857/1943_F10_1_red_green.jpg)
![](https://images.proteinatlas.org/50857/1943_F10_2_red_green.jpg)
![](https://images.proteinatlas.org/50857/1954_H11_37_cr5dfb7a40880b5_red_green.jpg)
![](https://images.proteinatlas.org/50857/1954_H11_50_cr5dfb7a408862d_red_green.jpg)
![](https://images.proteinatlas.org/50857/1981_G9_5_red_green.jpg)
![](https://images.proteinatlas.org/50857/1981_G9_6_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BQ87-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BQ87 |
| SMART | SM00667;SM00320; |
| UniProt Domain [FT] | DOMAIN 4..36; /note="LisH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00126"; DOMAIN 41..86; /note="F-box-like" |
| InterPro | IPR045183;IPR006594;IPR015943;IPR020472;IPR019775;IPR036322;IPR001680; |
| Pfam | PF08513;PF00400; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000092377-TBL1Y/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| HDAC3 | Biogrid, Opencell | true |
| CCT2 | Bioplex | false |
| CCT6B | Bioplex | false |
| DNAJB4 | Bioplex | false |
| ERF | Bioplex | false |
| ETV3 | Bioplex | false |
| GPS2 | Bioplex | false |
| NDUFS6 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
