---
type: protein-evaluation
gene: "KLHL8"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KLHL8 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KLHL8 / KIAA1378 |
| 蛋白名称 | Kelch-like protein 8 |
| 蛋白大小 | 620 aa / 68.8 kDa |
| UniProt ID | Q9P2G9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 620 aa / 68.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=15 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=90.7; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011705, IPR017096, IPR000210, IPR011043, IPR015 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.5/180** | |
| **归一化总分** | | | **76.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- Cul3-RING ubiquitin ligase complex (GO:0031463)
- cytoplasm (GO:0005737)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed broad count | 20 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1378 |

**关键文献**:
1. Defining E3 ligase-substrate relationships through multiplex CRISPR screening.. *Nature cell biology*. PMID: 37735597
2. The E3 ubiquitin ligase adaptor KLHL8 targets ZAR1 to regulate maternal mRNA degradation in oocytes.. *EMBO reports*. PMID: 40721554
3. Deciphering the alteration of MAP2 interactome caused by a schizophrenia-associated phosphorylation.. *Neurobiology of disease*. PMID: 39532265
4. A Million-Cow Genome-Wide Association Study of Three Fertility Traits in U.S. Holstein Cows.. *International journal of molecular sciences*. PMID: 37445674
5. Exome Sequencing Identified Susceptible Genes for High Residual Risks in Early-Onset Coronary Atherosclerotic Disease.. *Clinical cardiology*. PMID: 39673281

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.7 |
| 高置信度残基 (pLDDT>90) 占比 | 83.9% |
| 置信残基 (pLDDT 70-90) 占比 | 7.3% |
| 中等置信 (pLDDT 50-70) 占比 | 1.5% |
| 低置信 (pLDDT<50) 占比 | 7.4% |
| 有序区域 (pLDDT>70) 占比 | 91.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=90.7，有序区 91.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011705, IPR017096, IPR000210, IPR011043, IPR015915; Pfam: PF07707, PF00651, PF01344 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CUL3 | 0.989 | 0.735 | — |
| RBX1 | 0.924 | 0.098 | — |
| KLHL42 | 0.920 | 0.062 | — |
| KLHL13 | 0.914 | 0.048 | — |
| SPOP | 0.914 | 0.094 | — |
| SPOPL | 0.913 | 0.094 | — |
| KLHL9 | 0.913 | 0.048 | — |
| ENC1 | 0.912 | 0.000 | — |
| KLHL41 | 0.912 | 0.000 | — |
| KBTBD6 | 0.912 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ATXN1 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| COIL | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| USP7 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| COPS6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| CUL3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| COPS5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| DCUN1D1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| SIGLEC5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TAF15 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CCT3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.7 + PDB: 无 | pLDDT=90.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. KLHL8 — Kelch-like protein 8，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小620 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 15 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9P2G9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000145332-KLHL8/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KLHL8
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9P2G9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000145332-KLHL8/subcellular

![](https://images.proteinatlas.org/13856/105_G6_1_red_green.jpg)
![](https://images.proteinatlas.org/13856/105_G6_2_red_green.jpg)
![](https://images.proteinatlas.org/13856/160_G6_1_red_green.jpg)
![](https://images.proteinatlas.org/13856/160_G6_2_red_green.jpg)
![](https://images.proteinatlas.org/17762/112_F12_1_red_green.jpg)
![](https://images.proteinatlas.org/17762/112_F12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9P2G9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9P2G9 |
| SMART | SM00875;SM00225;SM00612; |
| UniProt Domain [FT] | DOMAIN 67..134; /note="BTB"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00037"; DOMAIN 169..270; /note="BACK" |
| InterPro | IPR011705;IPR017096;IPR000210;IPR011043;IPR015915;IPR006652;IPR011333; |
| Pfam | PF07707;PF00651;PF01344;PF24681; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000145332-KLHL8/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CUL3 | Intact, Biogrid | true |
| SNRPC | Biogrid, Opencell, Bioplex | true |
| SNRPF | Biogrid, Opencell, Bioplex | true |
| CCDC120 | Bioplex | false |
| CCT2 | Bioplex | false |
| CCT3 | Bioplex | false |
| CCT5 | Bioplex | false |
| CCT7 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
