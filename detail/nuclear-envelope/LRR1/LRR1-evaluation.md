---
type: protein-evaluation
gene: "LRR1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LRR1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LRR1 / PPIL5 |
| 蛋白名称 | Leucine-rich repeat protein 1 |
| 蛋白大小 | 414 aa / 46.7 kDa |
| UniProt ID | Q96L50 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nuclear membrane; 额外: Vesicles; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 414 aa / 46.7 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=45 篇 (≤60→6) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=88.2; PDB: 7PLO |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001611, IPR025875, IPR003591, IPR032675, IPR050 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **119.0/180** | |
| **归一化总分** | | | **66.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear membrane; 额外: Vesicles | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 45 |
| PubMed broad count | 73 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PPIL5 |

**关键文献**:
1. A novel oncogene, leucine-rich repeat protein 1, mediates hypoxia-induced hepatocellular carcinoma progression.. *Functional & integrative genomics*. PMID: 40459634
2. Whole-Genome Sequencing Reveals Individual and Cohort Level Insights into Chromosome 9p Syndromes.. *medRxiv : the preprint server for health sciences*. PMID: 40196253
3. Structural basis for LAR-RPTP/Slitrk complex-mediated synaptic adhesion.. *Nature communications*. PMID: 25394468
4. Arabidopsis U-box E3 ubiquitin ligase PUB11 negatively regulates drought tolerance by degrading the receptor-like protein kinases LRR1 and KIN7.. *Journal of integrative plant biology*. PMID: 33347703
5. Distribution and Evolution of Yersinia Leucine-Rich Repeat Proteins.. *Infection and immunity*. PMID: 27217422

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.2 |
| 高置信度残基 (pLDDT>90) 占比 | 63.3% |
| 置信残基 (pLDDT 70-90) 占比 | 27.3% |
| 中等置信 (pLDDT 50-70) 占比 | 7.0% |
| 低置信 (pLDDT<50) 占比 | 2.4% |
| 有序区域 (pLDDT>70) 占比 | 90.6% |
| 可用 PDB 条目 | 7PLO |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=88.2，有序区 90.6%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001611, IPR025875, IPR003591, IPR032675, IPR050216; Pfam: PF00560, PF12799, PF25344 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CUL2 | 0.996 | 0.971 | — |
| RBX1 | 0.990 | 0.931 | — |
| ELOC | 0.989 | 0.928 | — |
| ELOB | 0.984 | 0.914 | — |
| MCM7 | 0.947 | 0.852 | — |
| WDHD1 | 0.935 | 0.800 | — |
| MCM3 | 0.932 | 0.800 | — |
| MCM5 | 0.916 | 0.800 | — |
| CDC45 | 0.905 | 0.801 | — |
| GINS4 | 0.895 | 0.800 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| COPS5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| COPS6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| CUL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15601820|imex:IM-19076 |
| ELOB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15601820|imex:IM-19076 |
| RBX1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15601820|imex:IM-19076 |
| ELOC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15601820|imex:IM-19076 |
| CUL5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| COPS2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZBTB38 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| COPS8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.2 + PDB: 7PLO | pLDDT=88.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Nuclear membrane; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. LRR1 — Leucine-rich repeat protein 1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小414 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 45 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96L50
- Protein Atlas: https://www.proteinatlas.org/ENSG00000165501-LRR1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LRR1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96L50
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000165501-LRR1/subcellular

![](https://images.proteinatlas.org/69364/1434_D5_1_red_green.jpg)
![](https://images.proteinatlas.org/69364/1434_D5_2_red_green.jpg)
![](https://images.proteinatlas.org/69364/1436_D5_3_red_green.jpg)
![](https://images.proteinatlas.org/69364/1436_D5_4_red_green.jpg)
![](https://images.proteinatlas.org/69364/1547_H6_1_red_green.jpg)
![](https://images.proteinatlas.org/69364/1547_H6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96L50-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96L50 |
| SMART | SM00369; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR001611;IPR025875;IPR003591;IPR032675;IPR050216;IPR057437; |
| Pfam | PF00560;PF12799;PF25344; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000165501-LRR1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CDKN1A | Biogrid | false |
| COPS2 | Biogrid | false |
| COPS3 | Biogrid | false |
| COPS5 | Biogrid | false |
| COPS6 | Biogrid | false |
| COPS7A | Biogrid | false |
| COPS8 | Biogrid | false |
| CUL2 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
