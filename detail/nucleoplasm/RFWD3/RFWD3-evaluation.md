---
type: protein-evaluation
gene: "RFWD3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## RFWD3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RFWD3 / RNF201 |
| 蛋白名称 | E3 ubiquitin-protein ligase RFWD3 |
| 蛋白大小 | 774 aa / 85.1 kDa |
| UniProt ID | Q6PCD5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus; Nucleus, PML body; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 774 aa / 85.1 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=37 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=70.1; PDB: 6CVZ |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR037381, IPR015943, IPR036322, IPR056527, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **127.0/180** | |
| **归一化总分** | | | **70.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Enhanced |
| UniProt | Nucleus; Nucleus, PML body; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- PML body (GO:0016605)
- site of DNA damage (GO:0090734)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 37 |
| PubMed broad count | 60 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RNF201 |

**关键文献**:
1. Fanconi Anemia.. **. PMID: 20301575
2. Heterozygous RPA2 variant as a novel genetic cause of telomere biology disorders.. *Genes & development*. PMID: 39231615
3. CK2-dependent degradation of CBX3 dictates replication fork stalling and PARP inhibitor sensitivity.. *Science advances*. PMID: 38781342
4. RFWD3 acts as a tumor promotor in the development and progression of bladder cancer.. *Histology and histopathology*. PMID: 36458571
5. E3 ligases: a ubiquitous link between DNA repair, DNA replication and human disease.. *The Biochemical journal*. PMID: 38985307

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.1 |
| 高置信度残基 (pLDDT>90) 占比 | 46.3% |
| 置信残基 (pLDDT 70-90) 占比 | 13.2% |
| 中等置信 (pLDDT 50-70) 占比 | 4.0% |
| 低置信 (pLDDT<50) 占比 | 36.6% |
| 有序区域 (pLDDT>70) 占比 | 59.5% |
| 可用 PDB 条目 | 6CVZ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=70.1，有序区 59.5%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR037381, IPR015943, IPR036322, IPR056527, IPR001680; Pfam: PF23419, PF13639 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RPA1 | 0.997 | 0.994 | — |
| RPA3 | 0.997 | 0.994 | — |
| RPA2 | 0.996 | 0.994 | — |
| PRIMPOL | 0.994 | 0.994 | — |
| MDM2 | 0.792 | 0.292 | — |
| FANCI | 0.775 | 0.000 | — |
| RAD51 | 0.749 | 0.292 | — |
| MLKL | 0.726 | 0.000 | — |
| FANCD2 | 0.702 | 0.000 | — |
| FANCA | 0.701 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000460049.1 | psi-mi:"MI:0096"(pull down) | pubmed:28691929|imex:IM-27281 |
| Q81YX2 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| UBE2D1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-9597|pubmed:19690564 |
| UBE2D2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-9597|pubmed:19690564 |
| UBE2D3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-9597|pubmed:19690564 |
| UBE2D4 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-9597|pubmed:19690564 |
| UBE2E3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-11696|pubmed:19549727 |
| UBE2W | psi-mi:"MI:0397"(two hybrid array) | imex:IM-11696|pubmed:19549727 |
| UBE2E1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-11696|pubmed:19549727 |
| UBE2N | psi-mi:"MI:0397"(two hybrid array) | imex:IM-11696|pubmed:19549727 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.1 + PDB: 6CVZ | pLDDT=70.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus, PML body; Cytoplasm / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. RFWD3 — E3 ubiquitin-protein ligase RFWD3，非常新颖，仅有少数基础研究。
2. 蛋白大小774 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 37 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6PCD5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000168411-RFWD3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RFWD3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6PCD5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000168411-RFWD3/subcellular

![](https://images.proteinatlas.org/48258/712_A9_1_red_green.jpg)
![](https://images.proteinatlas.org/48258/712_A9_2_red_green.jpg)
![](https://images.proteinatlas.org/48258/804_A9_1_red_green.jpg)
![](https://images.proteinatlas.org/48258/804_A9_2_red_green.jpg)
![](https://images.proteinatlas.org/48258/964_A9_1_red_green.jpg)
![](https://images.proteinatlas.org/48258/964_A9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6PCD5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6PCD5 |
| SMART | SM00184;SM00320; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR037381;IPR015943;IPR036322;IPR056527;IPR001680;IPR001841;IPR013083; |
| Pfam | PF23419;PF13639; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000168411-RFWD3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CCT2 | Biogrid, Bioplex | true |
| CCT5 | Biogrid, Bioplex | true |
| CCT7 | Biogrid, Bioplex | true |
| MDM2 | Intact, Biogrid | true |
| RPA2 | Intact, Biogrid | true |
| TP53 | Intact, Biogrid | true |
| UBE2D1 | Intact, Biogrid | true |
| UBE2D2 | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
