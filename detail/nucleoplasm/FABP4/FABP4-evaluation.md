---
type: protein-evaluation
gene: "FABP4"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FABP4 — REJECTED (研究热度过高 (PubMed strict=2230，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FABP4 |
| 蛋白名称 | Fatty acid-binding protein, adipocyte |
| 蛋白大小 | 132 aa / 14.7 kDa |
| UniProt ID | P15090 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 132 aa / 14.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=2230 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=95.8; PDB: 1TOU, 1TOW, 2HNX, 2NNQ, 3FR2, 3FR4, 3FR5 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR012674, IPR000463, IPR031259, IPR000566; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 12 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Approved |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- lipid droplet (GO:0005811)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2230 |
| PubMed broad count | 3234 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. FABP4 inhibition suppresses bone resorption and protects against postmenopausal osteoporosis in ovariectomized mice.. *Nature communications*. PMID: 40360512
2. Adipocyte-Induced FABP4 Expression in Ovarian Cancer Cells Promotes Metastasis and Mediates Carboplatin Resistance.. *Cancer research*. PMID: 32054768
3. Targeting FABP4 in elderly mice rejuvenates liver metabolism and ameliorates aging-associated metabolic disorders.. *Metabolism: clinical and experimental*. PMID: 36842611
4. FABP4 secreted by M1-polarized macrophages promotes synovitis and angiogenesis to exacerbate rheumatoid arthritis.. *Bone research*. PMID: 35729106
5. p21-activated kinase 4 counteracts PKA-dependent lipolysis by phosphorylating FABP4 and HSL.. *Nature metabolism*. PMID: 38216738

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 95.8 |
| 高置信度残基 (pLDDT>90) 占比 | 95.5% |
| 置信残基 (pLDDT 70-90) 占比 | 4.5% |
| 中等置信 (pLDDT 50-70) 占比 | 0.0% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 100.0% |
| 可用 PDB 条目 | 1TOU, 1TOW, 2HNX, 2NNQ, 3FR2, 3FR4, 3FR5, 3P6C, 3P6D, 3P6E |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1TOU, 1TOW, 2HNX, 2NNQ, 3FR2, 3FR4, 3FR5, 3P6C, 3P6D, 3P6E）+ AlphaFold极高置信度预测（pLDDT=95.8），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR012674, IPR000463, IPR031259, IPR000566; Pfam: PF00061 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LIPE | 0.999 | 0.575 | — |
| PPARG | 0.993 | 0.050 | — |
| CD36 | 0.969 | 0.000 | — |
| LPL | 0.965 | 0.000 | — |
| ADIPOQ | 0.942 | 0.000 | — |
| PLIN1 | 0.927 | 0.000 | — |
| CEBPA | 0.914 | 0.000 | — |
| FABP1 | 0.904 | 0.000 | — |
| GOT2 | 0.904 | 0.067 | — |
| SCARB2 | 0.866 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| VIM | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| SNCG | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| OSTF1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EXT2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| USP15 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| GDF5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| OAZ3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TFAP2C | psi-mi:"MI:0018"(two hybrid) | imex:IM-22985|pubmed:24835590 |
| FOXN3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| VIPR2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 12
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 12 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=95.8 + PDB: 1TOU, 1TOW, 2HNX, 2NNQ, 3FR2,  | pLDDT=95.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 12 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. FABP4 — Fatty acid-binding protein, adipocyte，研究基础较多，新颖性有限。
2. 蛋白大小132 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 2230 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 2230 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P15090
- Protein Atlas: https://www.proteinatlas.org/ENSG00000170323-FABP4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FABP4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P15090
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000170323-FABP4/subcellular

![](https://images.proteinatlas.org/2188/2164_D1_2_red_green.jpg)
![](https://images.proteinatlas.org/2188/2164_D1_3_red_green.jpg)
![](https://images.proteinatlas.org/2188/2174_A1_1_red_green.jpg)
![](https://images.proteinatlas.org/2188/2174_A1_2_red_green.jpg)
![](https://images.proteinatlas.org/2188/32_D4_1_red_green.jpg)
![](https://images.proteinatlas.org/2188/32_D4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P15090-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P15090 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR012674;IPR000463;IPR031259;IPR000566; |
| Pfam | PF00061; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000170323-FABP4/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| VIM | Intact, Biogrid | true |
| LIPE | Biogrid | false |
| SCG5 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
