---
type: protein-evaluation
gene: "FANK1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FANK1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FANK1 |
| 蛋白名称 | Fibronectin type 3 and ankyrin repeat domains protein 1 |
| 蛋白大小 | 345 aa / 38.3 kDa |
| UniProt ID | Q8TC84 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Cytoplasm, cytosol; Cytoplasm, cytoskeleton, cilium |
| 蛋白大小 | 10/10 | ×1 | 10 | 345 aa / 38.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=92.7; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR002110, IPR036770, IPR003961, IPR036116, IPR013 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 14 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.5/180** | |
| **归一化总分** | | | **76.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus; Cytoplasm, cytosol; Cytoplasm, cytoskeleton, cilium basal body; Cell projection, cilium | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- ciliary basal body (GO:0036064)
- ciliary base (GO:0097546)
- cilium (GO:0005929)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 22 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Single-cell RNA-seq reveals dynamic change in tumor microenvironment during pancreatic ductal adenocarcinoma malignant progression.. *EBioMedicine*. PMID: 33819739
2. Proapoptotic RYBP interacts with FANK1 and induces tumor cell apoptosis through the AP-1 signaling pathway.. *Cellular signalling*. PMID: 27060496
3. Fank1 is a testis-specific gene encoding a nuclear protein exclusively expressed during the transition from the meiotic to the haploid phase of spermatogenesis.. *Gene expression patterns : GEP*. PMID: 17604233
4. Normal spermatogenesis in Fank1 (fibronectin type 3 and ankyrin repeat domains 1) mutant mice.. *PeerJ*. PMID: 31086747
5. Testis-specific Fank1 gene in knockdown mice produces oligospermia via apoptosis.. *Asian journal of andrology*. PMID: 24369145

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.7 |
| 高置信度残基 (pLDDT>90) 占比 | 82.3% |
| 置信残基 (pLDDT 70-90) 占比 | 11.9% |
| 中等置信 (pLDDT 50-70) 占比 | 2.9% |
| 低置信 (pLDDT<50) 占比 | 2.9% |
| 有序区域 (pLDDT>70) 占比 | 94.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=92.7，有序区 94.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002110, IPR036770, IPR003961, IPR036116, IPR013783; Pfam: PF12796 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DHX32 | 0.710 | 0.116 | — |
| COPS5 | 0.648 | 0.334 | — |
| FAM199X | 0.591 | 0.000 | — |
| ATG4B | 0.566 | 0.560 | — |
| SPATA4 | 0.559 | 0.111 | — |
| RYBP | 0.543 | 0.300 | — |
| UBXN2B | 0.540 | 0.540 | — |
| ZNF717 | 0.518 | 0.091 | — |
| MALRD1 | 0.504 | 0.093 | — |
| CCDC113 | 0.490 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| UBXN2B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| A4GNT | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ATG4B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| VCAM1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MAGEA4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TRIM63 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:31391242|imex:IM-25805| |
| TRIM55 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:31391242|imex:IM-25805| |
| WFS1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| KIF1B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| HTT | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 14
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 14 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.7 + PDB: 无 | pLDDT=92.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, cytosol; Cytoplasm, cytoskelet / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 14 interactions | 数据充分 |

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
1. FANK1 — Fibronectin type 3 and ankyrin repeat domains protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小345 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TC84
- Protein Atlas: https://www.proteinatlas.org/ENSG00000203780-FANK1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FANK1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TC84
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000203780-FANK1/subcellular

![](https://images.proteinatlas.org/38413/2145_B8_15_blue_red_green.jpg)
![](https://images.proteinatlas.org/38413/2145_B8_55_blue_red_green.jpg)
![](https://images.proteinatlas.org/38413/2153_H8_11_blue_red_green.jpg)
![](https://images.proteinatlas.org/38413/2153_H8_47_blue_red_green.jpg)
![](https://images.proteinatlas.org/38413/2209_E2_18_blue_red_green.jpg)
![](https://images.proteinatlas.org/38413/2209_E2_23_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8TC84-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8TC84 |
| SMART | SM00248;SM00060; |
| UniProt Domain [FT] | DOMAIN 8..108; /note="Fibronectin type-III"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00316" |
| InterPro | IPR002110;IPR036770;IPR003961;IPR036116;IPR013783; |
| Pfam | PF12796; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000203780-FANK1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| FGFR3 | Intact | false |
| HSPB1 | Intact | false |
| HTT | Intact | false |
| MAGEA4 | Bioplex | false |
| NEFL | Intact | false |
| RYBP | Biogrid | false |
| WFS1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
