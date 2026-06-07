---
type: protein-evaluation
gene: "GBP4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GBP4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GBP4 |
| 蛋白名称 | Guanylate-binding protein 4 |
| 蛋白大小 | 640 aa / 73.2 kDa |
| UniProt ID | Q96PP9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Golgi apparatus; 额外: Plasma membrane; UniProt: Golgi apparatus membrane; Cytoplasm; Nucleus; Cytoplasm, per |
| 蛋白大小 | 10/10 | ×1 | 10 | 640 aa / 73.2 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=60 篇 (≤60→6) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=85.8; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR030386, IPR037684, IPR003191, IPR036543, IPR015 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.5/180** | |
| **归一化总分** | | | **65.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Plasma membrane | Supported |
| UniProt | Golgi apparatus membrane; Cytoplasm; Nucleus; Cytoplasm, perinuclear region | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasmic vesicle (GO:0031410)
- cytosol (GO:0005829)
- Golgi apparatus (GO:0005794)
- Golgi membrane (GO:0000139)
- nucleus (GO:0005634)
- perinuclear region of cytoplasm (GO:0048471)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 60 |
| PubMed broad count | 81 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Whole-Genome DNA Methylation Profiling of Intrahepatic Cholangiocarcinoma Reveals Prognostic Subtypes with Distinct Biological Drivers.. *Cancer research*. PMID: 38471085
2. DNA hypo-methylation and expression of GBP4 induces T cell exhaustion in pancreatic cancer.. *Cancer immunology, immunotherapy : CII*. PMID: 39110249
3. Guanylate binding protein 4 shapes an inflamed tumor microenvironment and identifies immuno-hot tumors.. *Journal of cancer research and clinical oncology*. PMID: 38347243
4. Cross-assay RNA modeling reveals cancer biomarkers.. *bioRxiv : the preprint server for biology*. PMID: 42146664
5. Shigella IpaH9.8 limits GBP1-dependent LPS release from intracytosolic bacteria to suppress caspase-4 activation.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 37014865

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.8 |
| 高置信度残基 (pLDDT>90) 占比 | 54.4% |
| 置信残基 (pLDDT 70-90) 占比 | 34.2% |
| 中等置信 (pLDDT 50-70) 占比 | 5.2% |
| 低置信 (pLDDT<50) 占比 | 6.2% |
| 有序区域 (pLDDT>70) 占比 | 88.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=85.8，有序区 88.6%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR030386, IPR037684, IPR003191, IPR036543, IPR015894; Pfam: PF02263, PF02841 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GBP1 | 0.905 | 0.292 | — |
| GBP5 | 0.853 | 0.292 | — |
| STAT1 | 0.853 | 0.000 | — |
| GBP2 | 0.853 | 0.292 | — |
| CXCL10 | 0.776 | 0.000 | — |
| EPSTI1 | 0.767 | 0.000 | — |
| PARP14 | 0.751 | 0.000 | — |
| IRF1 | 0.740 | 0.000 | — |
| IFIT3 | 0.722 | 0.000 | — |
| IFIT2 | 0.712 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| stl | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| PNPT1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| ENST00000355754 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 3
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.8 + PDB: 无 | pLDDT=85.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus membrane; Cytoplasm; Nucleus; Cyto / Golgi apparatus; 额外: Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 3 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. GBP4 — Guanylate-binding protein 4，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小640 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 60 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96PP9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000162654-GBP4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GBP4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96PP9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/GBP4/IF_images/RT-4_1.jpg]]
![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/GBP4/IF_images/HEL_1.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (supported)。来源: https://www.proteinatlas.org/ENSG00000162654-GBP4/subcellular

![](https://images.proteinatlas.org/62039/1358_C6_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/62039/1358_C6_8_blue_red_green.jpg)
![](https://images.proteinatlas.org/62039/1396_F3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/62039/1396_F3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/62039/1848_D5_31_blue_red_green.jpg)
![](https://images.proteinatlas.org/62039/1848_D5_32_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96PP9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96PP9 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 50..292; /note="GB1/RHD3-type G"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01052" |
| InterPro | IPR030386;IPR037684;IPR003191;IPR036543;IPR015894;IPR027417; |
| Pfam | PF02263;PF02841; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000162654-GBP4/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| GBP1 | Intact | false |
| GBP2 | Intact | false |
| GBP5 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
