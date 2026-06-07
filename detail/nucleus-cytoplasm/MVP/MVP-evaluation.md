---
type: protein-evaluation
gene: "MVP"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## MVP — REJECTED (研究热度过高 (PubMed strict=540，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MVP / LRP |
| 蛋白名称 | Major vault protein |
| 蛋白大小 | 893 aa / 99.3 kDa |
| UniProt ID | Q14764 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Cytoplasm; Nucleus, nuclear pore complex; Cytoplasm, perinuc |
| 蛋白大小 | 8/10 | ×1 | 8 | 893 aa / 99.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=540 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=81.3; PDB: 1Y7X, 9BW5, 9BW6, 9BW7, 9MXH, 9MXJ, 9MXV |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR036013, IPR039059, IPR041139, IPR043023, IPR021 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **93.5/180** | |
| **归一化总分** | | | **51.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Enhanced |
| UniProt | Cytoplasm; Nucleus, nuclear pore complex; Cytoplasm, perinuclear region | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytoskeleton (GO:0005856)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- extracellular region (GO:0005576)
- ficolin-1-rich granule lumen (GO:1904813)
- membrane (GO:0016020)
- nuclear pore (GO:0005643)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 540 |
| PubMed broad count | 3746 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: LRP |

**关键文献**:
1. Endothelial IGFBP6 suppresses vascular inflammation and atherosclerosis.. *Nature cardiovascular research*. PMID: 39794479
2. Endothelial major vault protein alleviates vascular remodeling via promoting Parkin-mediated mitophagy.. *Nature communications*. PMID: 40348769
3. Discovery of 318 new risk loci for type 2 diabetes and related vascular outcomes among 1.4 million participants in a multi-ancestry meta-analysis.. *Nature genetics*. PMID: 32541925
4. MVP-LCN2 axis triggers evasion of ferroptosis to drive hepatocarcinogenesis and sorafenib resistance.. *Drug resistance updates : reviews and commentaries in antimicrobial and anticancer chemotherapy*. PMID: 40262414
5. Lactylation-driven MVP upregulation boosts immunotherapy resistance by inhibiting PD-L1 degradation in hepatocellular carcinoma.. *Journal for immunotherapy of cancer*. PMID: 40983342

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.3 |
| 高置信度残基 (pLDDT>90) 占比 | 31.8% |
| 置信残基 (pLDDT 70-90) 占比 | 51.7% |
| 中等置信 (pLDDT 50-70) 占比 | 8.3% |
| 低置信 (pLDDT<50) 占比 | 8.2% |
| 有序区域 (pLDDT>70) 占比 | 83.5% |
| 可用 PDB 条目 | 1Y7X, 9BW5, 9BW6, 9BW7, 9MXH, 9MXJ, 9MXV, 9R86, 9R87 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1Y7X, 9BW5, 9BW6, 9BW7, 9MXH, 9MXJ, 9MXV, 9R86, 9R87）+ AlphaFold极高置信度预测（pLDDT=81.3），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036013, IPR039059, IPR041139, IPR043023, IPR021870; Pfam: PF11978, PF01505, PF17794 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PARP4 | 0.999 | 0.786 | — |
| TEP1 | 0.998 | 0.292 | — |
| PTEN | 0.786 | 0.292 | — |
| PARP1 | 0.770 | 0.000 | — |
| ABCB1 | 0.760 | 0.078 | — |
| MYD88 | 0.724 | 0.000 | — |
| ABCC1 | 0.702 | 0.069 | — |
| ESR1 | 0.667 | 0.294 | — |
| COP1 | 0.603 | 0.603 | — |
| C19orf48 | 0.572 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.3 + PDB: 1Y7X, 9BW5, 9BW6, 9BW7, 9MXH,  | pLDDT=81.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus, nuclear pore complex; Cytoplas / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. MVP — Major vault protein，研究基础较多，新颖性有限。
2. 蛋白大小893 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 540 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 540 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q14764
- Protein Atlas: https://www.proteinatlas.org/ENSG00000013364-MVP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MVP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q14764
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (enhanced)。来源: https://www.proteinatlas.org/ENSG00000013364-MVP/subcellular

![](https://images.proteinatlas.org/22717/663_A2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/22717/663_A2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/22717/672_A2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/22717/672_A2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/2321/32_B8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/2321/33_B8_1_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q14764-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q14764 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR036013;IPR039059;IPR041139;IPR043023;IPR021870;IPR041134;IPR043179;IPR040989;IPR041136;IPR002499; |
| Pfam | PF11978;PF01505;PF17794;PF17795;PF17796; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000013364-MVP/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ANLN | Biogrid | false |
| CHMP4B | Biogrid | false |
| COP1 | Biogrid | false |
| DTX2 | Intact | false |
| ESR1 | Biogrid | false |
| HSPA1A | Biogrid | false |
| MAP7 | Bioplex | false |
| NTAQ1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
