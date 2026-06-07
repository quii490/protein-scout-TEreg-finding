---
type: protein-evaluation
gene: "OTX2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## OTX2 — REJECTED (研究热度过高 (PubMed strict=769，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | OTX2 |
| 蛋白名称 | Homeobox protein OTX2 |
| 蛋白大小 | 289 aa / 31.6 kDa |
| UniProt ID | P32243 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Vesicles; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 289 aa / 31.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=769 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001356, IPR017970, IPR009057, IPR003022, IPR003 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.0/180** | |
| **归一化总分** | | | **48.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- growth cone (GO:0030426)
- nucleus (GO:0005634)
- protein-containing complex (GO:0032991)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 769 |
| PubMed broad count | 1239 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Persistent Wnt signaling affects IVF embryo implantation and offspring metabolism.. *Science bulletin*. PMID: 40441968
2. The Otx family.. *Current opinion in genetics & development*. PMID: 12100885
3. IGF2BP1 restricts the induction of human primordial germ cell fate in an m(6)A-dependent manner.. *Cell stem cell*. PMID: 40436019
4. O-GlcNAcylation regulates OTX2's proteostasis.. *iScience*. PMID: 38026167
5. Re-focusing on Agnathia-Otocephaly complex.. *Clinical oral investigations*. PMID: 32643087

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.7 |
| 高置信度残基 (pLDDT>90) 占比 | 19.4% |
| 置信残基 (pLDDT 70-90) 占比 | 2.8% |
| 中等置信 (pLDDT 50-70) 占比 | 33.2% |
| 低置信 (pLDDT<50) 占比 | 44.6% |
| 有序区域 (pLDDT>70) 占比 | 22.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=59.7），有序残基占 22.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001356, IPR017970, IPR009057, IPR003022, IPR003025; Pfam: PF00046, PF03529 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FOXA2 | 0.918 | 0.510 | — |
| SOX2 | 0.914 | 0.091 | — |
| POU5F1 | 0.912 | 0.312 | — |
| SIX6 | 0.894 | 0.095 | — |
| SIX3 | 0.878 | 0.091 | — |
| PAX2 | 0.823 | 0.000 | — |
| RCVRN | 0.811 | 0.000 | — |
| FGF8 | 0.808 | 0.058 | — |
| SOX1 | 0.807 | 0.091 | — |
| SOX3 | 0.796 | 0.091 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ATXN1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| CDK4 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:22094256|imex:IM-16628 |
| Mixl1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| Tlx3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| Alx4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| Hoxb13 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| Emx1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| Dmrtc2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| Zbtb3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| GTF2F2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.7 + PDB: 无 | pLDDT=59.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Vesicles | 一致 |
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
1. OTX2 — Homeobox protein OTX2，研究基础较多，新颖性有限。
2. 蛋白大小289 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 769 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=59.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 769 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P32243
- Protein Atlas: https://www.proteinatlas.org/ENSG00000165588-OTX2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=OTX2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P32243
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000165588-OTX2/subcellular

![](https://images.proteinatlas.org/1123/1606_F1_5_red_green.jpg)
![](https://images.proteinatlas.org/1123/1606_F1_6_red_green.jpg)
![](https://images.proteinatlas.org/1123/1614_F1_1_red_green.jpg)
![](https://images.proteinatlas.org/1123/1614_F1_2_red_green.jpg)
![](https://images.proteinatlas.org/1123/1852_E4_16_cr5afd4342eb471_red_green.jpg)
![](https://images.proteinatlas.org/1123/1852_E4_22_cr5afd4342eb132_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P32243-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P32243 |
| SMART | SM00389; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR001356;IPR017970;IPR009057;IPR003022;IPR003025;IPR013851; |
| Pfam | PF00046;PF03529; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000165588-OTX2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ATXN1 | Intact, Biogrid | true |
| FOXA2 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
