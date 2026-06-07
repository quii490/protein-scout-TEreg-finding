---
type: protein-evaluation
gene: "SPTBN4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SPTBN4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SPTBN4 / KIAA1642, SPTBN3 |
| 蛋白名称 | Spectrin beta chain, non-erythrocytic 4 |
| 蛋白大小 | 2564 aa / 289.0 kDa |
| UniProt ID | Q9H254 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli; 额外: Nucleoplasm; UniProt: Cytoplasm, cytoskeleton; Cytoplasm, cell cortex |
| 蛋白大小 | 2/10 | ×1 | 2 | 2564 aa / 289.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=20 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=71.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001589, IPR001715, IPR036872, IPR011993, IPR041 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **125.5/180** | |
| **归一化总分** | | | **69.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; 额外: Nucleoplasm | Approved |
| UniProt | Cytoplasm, cytoskeleton; Cytoplasm, cell cortex | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- actin filament (GO:0005884)
- axon hillock (GO:0043203)
- axon initial segment (GO:0043194)
- cell body fiber (GO:0070852)
- cell junction (GO:0030054)
- cell projection (GO:0042995)
- cortical actin cytoskeleton (GO:0030864)
- cytoplasm (GO:0005737)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 20 |
| PubMed broad count | 37 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1642, SPTBN3 |

**关键文献**:
1. Expanding the genetic heterogeneity of intellectual disability.. *Human genetics*. PMID: 28940097
2. Postsynaptic β1 spectrin maintains Na(+) channels at the neuromuscular junction.. *The Journal of physiology*. PMID: 38441922
3. Heterozygous loss-of-function variants in SPTAN1 cause a novel early childhood onset distal myopathy with chronic neurogenic features.. *medRxiv : the preprint server for health sciences*. PMID: 39371122
4. Multiomics Approach Distinguishes SPTBN4 as a Key Molecule in Diagnosis, Prognosis, and Immune Suppression of Testicular Seminomas.. *International journal of genomics*. PMID: 40321316
5. SPTBN5, Encoding the βV-Spectrin Protein, Leads to a Syndrome of Intellectual Disability, Developmental Delay, and Seizures.. *Frontiers in molecular neuroscience*. PMID: 35782384

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.8 |
| 高置信度残基 (pLDDT>90) 占比 | 7.7% |
| 置信残基 (pLDDT 70-90) 占比 | 63.1% |
| 中等置信 (pLDDT 50-70) 占比 | 11.7% |
| 低置信 (pLDDT<50) 占比 | 17.5% |
| 有序区域 (pLDDT>70) 占比 | 70.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=71.8，有序区 70.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001589, IPR001715, IPR036872, IPR011993, IPR041681; Pfam: PF00307, PF15410, PF00435 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ANK3 | 0.999 | 0.822 | — |
| ANK2 | 0.986 | 0.797 | — |
| ANK1 | 0.972 | 0.423 | — |
| NRCAM | 0.972 | 0.000 | — |
| SPTAN1 | 0.967 | 0.447 | — |
| NFASC | 0.956 | 0.000 | — |
| SPTA1 | 0.955 | 0.293 | — |
| SPTBN5 | 0.919 | 0.000 | — |
| SPTBN2 | 0.914 | 0.000 | — |
| KCNQ2 | 0.884 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CELSR3 | psi-mi:"MI:0018"(two hybrid) | pubmed:unassigned5 |
| DISC1 | psi-mi:"MI:0018"(two hybrid) | pubmed:12812986|imex:IM-19614 |
| RAD51D | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| BRAF | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| Shank3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28671696|doi:10.1038/nn |
| HOMER1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PCDHGC3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RSBN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ERBB2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:24189400|imex:IM-21413 |
| ANTXR2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.8 + PDB: 无 | pLDDT=71.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton; Cytoplasm, cell cortex / Nucleoli; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. SPTBN4 — Spectrin beta chain, non-erythrocytic 4，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小2564 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 20 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H254
- Protein Atlas: https://www.proteinatlas.org/ENSG00000160460-SPTBN4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SPTBN4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H254
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (approved)。来源: https://www.proteinatlas.org/ENSG00000160460-SPTBN4/subcellular

![](https://images.proteinatlas.org/54481/1370_D5_1_red_green.jpg)
![](https://images.proteinatlas.org/54481/1370_D5_3_red_green.jpg)
![](https://images.proteinatlas.org/54481/1372_D5_2_red_green.jpg)
![](https://images.proteinatlas.org/54481/1372_D5_4_red_green.jpg)
![](https://images.proteinatlas.org/54481/1511_D3_1_red_green.jpg)
![](https://images.proteinatlas.org/54481/1511_D3_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H254-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H254 |
| SMART | SM00033;SM00233;SM00150; |
| UniProt Domain [FT] | DOMAIN 61..165; /note="Calponin-homology (CH) 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00044"; DOMAIN 180..285; /note="Calponin-homology (CH) 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00044"; DOMAIN 2418..2527; /note="PH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00145" |
| InterPro | IPR001589;IPR001715;IPR036872;IPR011993;IPR041681;IPR001605;IPR001849;IPR018159;IPR016343;IPR002017; |
| Pfam | PF00307;PF15410;PF00435; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000160460-SPTBN4/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DISC1 | Intact, Biogrid | true |
| PTPRN | Intact, Biogrid | true |
| MAPRE1 | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
