---
type: protein-evaluation
gene: "REXO4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## REXO4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | REXO4 / PMC2, XPMC2H |
| 蛋白名称 | RNA exonuclease 4 |
| 蛋白大小 | 422 aa / 46.7 kDa |
| UniProt ID | Q9GZR2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm, Nucleoli; UniProt: Nucleus, nucleolus |
| 蛋白大小 | 10/10 | ×1 | 10 | 422 aa / 46.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=70.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR037431, IPR047021, IPR013520, IPR012337, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **141.5/180** | |
| **归一化总分** | | | **78.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli | Supported |
| UniProt | Nucleus, nucleolus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nuclear speck (GO:0016607)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 15 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PMC2, XPMC2H |

**关键文献**:
1. Revealing Stress Granule Compositional Heterogeneity through Antibody-Guided Proximity Labeling.. *Analytical chemistry*. PMID: 40198209
2. REXO4 acts as a biomarker and promotes hepatocellular carcinoma progression.. *Journal of gastrointestinal oncology*. PMID: 35070432
3. The expression and prognostic value of REXO4 in hepatocellular carcinoma.. *Journal of gastrointestinal oncology*. PMID: 34532121
4. Human REXO4 is Required for Cell Cycle Progression.. *bioRxiv : the preprint server for biology*. PMID: 39829749
5. DDX18 promotes growth and metastasis of hepatocellular carcinoma via activating EMT and MAPK signaling.. *Journal of gastrointestinal oncology*. PMID: 40950356

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.8 |
| 高置信度残基 (pLDDT>90) 占比 | 40.0% |
| 置信残基 (pLDDT 70-90) 占比 | 12.8% |
| 中等置信 (pLDDT 50-70) 占比 | 12.3% |
| 低置信 (pLDDT<50) 占比 | 34.8% |
| 有序区域 (pLDDT>70) 占比 | 52.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=70.8，有序区 52.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR037431, IPR047021, IPR013520, IPR012337, IPR036397; Pfam: PF00929 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| REXO2 | 0.845 | 0.095 | — |
| TRMT61A | 0.819 | 0.053 | — |
| DDX55 | 0.811 | 0.095 | — |
| RBM34 | 0.805 | 0.509 | — |
| PPAN | 0.793 | 0.674 | — |
| IMP4 | 0.784 | 0.235 | — |
| NIP7 | 0.772 | 0.230 | — |
| CALCOCO2 | 0.757 | 0.000 | — |
| ABT1 | 0.742 | 0.179 | — |
| UTP23 | 0.737 | 0.184 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Dmel\CG6833 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-9552|pubmed:19079254 |
| asnB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| RAB11A | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| RAB9A | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| CANX | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| FBL | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| RPS6 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| RRP8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PPAN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.8 + PDB: 无 | pLDDT=70.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus, nucleolus / Nucleoplasm, Nucleoli | 一致 |
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
1. REXO4 — RNA exonuclease 4，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小422 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9GZR2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000148300-REXO4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=REXO4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9GZR2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000148300-REXO4/subcellular

![](https://images.proteinatlas.org/47006/711_D5_1_red_green.jpg)
![](https://images.proteinatlas.org/47006/711_D5_2_red_green.jpg)
![](https://images.proteinatlas.org/47006/723_D5_1_red_green.jpg)
![](https://images.proteinatlas.org/47006/723_D5_2_red_green.jpg)
![](https://images.proteinatlas.org/47006/866_D5_1_red_green.jpg)
![](https://images.proteinatlas.org/47006/866_D5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9GZR2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9GZR2 |
| SMART | SM00479; |
| UniProt Domain [FT] | DOMAIN 243..394; /note="Exonuclease" |
| InterPro | IPR037431;IPR047021;IPR013520;IPR012337;IPR036397; |
| Pfam | PF00929; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000148300-REXO4/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DDX24 | Biogrid, Bioplex | true |
| NIFK | Biogrid, Bioplex | true |
| PUM3 | Biogrid, Bioplex | true |
| RBM28 | Biogrid, Bioplex | true |
| RPL7A | Biogrid, Bioplex | true |
| APEX1 | Biogrid | false |
| BAZ1B | Biogrid | false |
| C7orf50 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
