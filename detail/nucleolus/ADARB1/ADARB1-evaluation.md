---
type: protein-evaluation
gene: "ADARB1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ADARB1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ADARB1 / ADAR2, DRADA2, RED1 |
| 蛋白名称 | Double-stranded RNA-specific editase 1 |
| 蛋白大小 | 741 aa / 80.8 kDa |
| UniProt ID | P78563 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus; Nucleus, nucleolus; Nucleus; Nucleus, nucleolus; Nu |
| 蛋白大小 | 10/10 | ×1 | 10 | 741 aa / 80.8 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=64 篇 (≤80→4) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=76.5; PDB: 1ZY7, 5ED1, 5ED2, 5HP2, 5HP3, 6D06, 6VFF |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR002466, IPR044458, IPR044459, IPR014720, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **114.0/180** | |
| **归一化总分** | | | **63.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Nucleus; Nucleus, nucleolus; Nucleus; Nucleus, nucleolus; Nucleus; Nucleus, nucleolus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- synapse (GO:0045202)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 64 |
| PubMed broad count | 700 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ADAR2, DRADA2, RED1 |

**关键文献**:
1. Identification of the shared gene signatures and pathways between sarcopenia and type 2 diabetes mellitus.. *PloS one*. PMID: 35271662
2. Nanocarriers Targeting Circular RNA ADARB1 Boost Radiosensitivity of Nasopharyngeal Carcinoma through Synergically Promoting Ferroptosis.. *ACS nano*. PMID: 39467079
3. Case-control study of ADARB1 and ADARB2 gene variants in migraine.. *The journal of headache and pain*. PMID: 25916332
4. Systematic analysis of A-to-I RNA editing upon release of ADAR from the nucleolus.. *RNA biology*. PMID: 40464638
5. Joint effect of ADARB1 gene, HTR2C gene and stressful life events on suicide attempt risk in patients with major psychiatric disorders.. *The world journal of biological psychiatry : the official journal of the World Federation of Societies of Biological Psychiatry*. PMID: 25732952

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.5 |
| 高置信度残基 (pLDDT>90) 占比 | 52.6% |
| 置信残基 (pLDDT 70-90) 占比 | 15.5% |
| 中等置信 (pLDDT 50-70) 占比 | 4.9% |
| 低置信 (pLDDT<50) 占比 | 27.0% |
| 有序区域 (pLDDT>70) 占比 | 68.1% |
| 可用 PDB 条目 | 1ZY7, 5ED1, 5ED2, 5HP2, 5HP3, 6D06, 6VFF, 7KFN, 8E0F, 8E4X |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1ZY7, 5ED1, 5ED2, 5HP2, 5HP3, 6D06, 6VFF, 7KFN, 8E0F, 8E4X）+ AlphaFold极高置信度预测（pLDDT=76.5），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002466, IPR044458, IPR044459, IPR014720, IPR008996; Pfam: PF02137, PF00035 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BMP7 | 0.871 | 0.000 | — |
| SYCP2 | 0.862 | 0.000 | — |
| ADA | 0.833 | 0.000 | — |
| GRIA2 | 0.822 | 0.000 | — |
| POFUT2 | 0.808 | 0.000 | — |
| SYCP3 | 0.788 | 0.000 | — |
| REC8 | 0.779 | 0.000 | — |
| SLC39A1 | 0.777 | 0.000 | — |
| MEI4 | 0.745 | 0.000 | — |
| PRKRA | 0.702 | 0.610 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-12002366 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| MAP1LC3A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| NCBP3 | psi-mi:"MI:0096"(pull down) | pubmed:26382858|imex:IM-26480 |
| PNPT1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| STOX1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| EHHADH | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| STAU1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| UBE2I | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ADGRE5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| EIF2AK2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.5 + PDB: 1ZY7, 5ED1, 5ED2, 5HP2, 5HP3,  | pLDDT=76.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus, nucleolus; Nucleus; Nucleus, nuc / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. ADARB1 — Double-stranded RNA-specific editase 1，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小741 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 64 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P78563
- Protein Atlas: https://www.proteinatlas.org/ENSG00000197381-ADARB1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ADARB1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P78563
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000197381-ADARB1/subcellular

![](https://images.proteinatlas.org/29645/505_D5_1_red_green.jpg)
![](https://images.proteinatlas.org/29645/508_D5_1_red_green.jpg)
![](https://images.proteinatlas.org/29645/508_D5_2_red_green.jpg)
![](https://images.proteinatlas.org/29645/548_D5_1_red_green.jpg)
![](https://images.proteinatlas.org/29645/548_D5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P78563-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P78563 |
| SMART | SM00552;SM00358; |
| UniProt Domain [FT] | DOMAIN 78..144; /note="DRBM 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00266"; DOMAIN 231..298; /note="DRBM 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00266"; DOMAIN 370..737; /note="A to I editase"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00240" |
| InterPro | IPR002466;IPR044458;IPR044459;IPR014720;IPR008996; |
| Pfam | PF02137;PF00035; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000197381-ADARB1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PIN1 | Intact, Biogrid | true |
| PRKRA | Intact, Biogrid | true |
| RSL1D1 | Intact, Biogrid | true |
| SURF6 | Intact, Biogrid | true |
| BRIX1 | Biogrid | false |
| C7orf50 | Biogrid | false |
| CCDC124 | Biogrid | false |
| CEBPZ | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
