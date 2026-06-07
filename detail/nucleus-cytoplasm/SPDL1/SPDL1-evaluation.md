---
type: protein-evaluation
gene: "SPDL1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SPDL1 — REJECTED (研究热度过高 (PubMed strict=190，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SPDL1 / CCDC99 |
| 蛋白名称 | Protein Spindly |
| 蛋白大小 | 605 aa / 70.2 kDa |
| UniProt ID | Q96EA4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Cytoplasm, cytoskeleton, microtubule organizing center, cent |
| 蛋白大小 | 10/10 | ×1 | 10 | 605 aa / 70.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=190 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=74.3; PDB: 8ARF |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR028593, IPR051149 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **87.0/180** | |
| **归一化总分** | | | **48.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Approved |
| UniProt | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Chromosome, centromere, kinetoch... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- centrosome (GO:0005813)
- cytosol (GO:0005829)
- nucleus (GO:0005634)
- outer kinetochore (GO:0000940)
- spindle pole (GO:0000922)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 190 |
| PubMed broad count | 519 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CCDC99 |

**关键文献**:
1. Accelerating novel candidate gene discovery in neurogenetic disorders via whole-exome sequencing of prescreened multiplex consanguineous families.. *Cell reports*. PMID: 25558065
2. Emerging role and function of SPDL1 in human health and diseases.. *Open medicine (Warsaw, Poland)*. PMID: 38623460
3. Soluble immune checkpoint factors reflect exhaustion of antitumor immunity and response to PD-1 blockade.. *The Journal of clinical investigation*. PMID: 38557498
4. Lipid Droplet-Localized Spindle Apparatus Coiled-Coil Protein 1 Regulates Lipid Droplet Distribution.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 41487061
5. Soluble PD-L1 reprograms blood monocytes to prevent cerebral edema and facilitate recovery after ischemic stroke.. *Brain, behavior, and immunity*. PMID: 38070624

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.3 |
| 高置信度残基 (pLDDT>90) 占比 | 41.0% |
| 置信残基 (pLDDT 70-90) 占比 | 24.3% |
| 中等置信 (pLDDT 50-70) 占比 | 8.9% |
| 低置信 (pLDDT<50) 占比 | 25.8% |
| 有序区域 (pLDDT>70) 占比 | 65.3% |
| 可用 PDB 条目 | 8ARF |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=74.3，有序区 65.3%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR028593, IPR051149 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BUB1B | 0.958 | 0.000 | — |
| CENPF | 0.950 | 0.000 | — |
| SKA3 | 0.947 | 0.099 | — |
| SKA1 | 0.946 | 0.000 | — |
| SKA2 | 0.927 | 0.000 | — |
| BOD1 | 0.917 | 0.000 | — |
| PLK1 | 0.889 | 0.000 | — |
| CDC20 | 0.888 | 0.000 | — |
| NDC80 | 0.878 | 0.000 | — |
| HOXD13 | 0.868 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| B4E393 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| GPS2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| CEP126 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| GSTT2B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| THUMPD2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ASB16 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FADS2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H3C1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| PPP1R18 | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-23318|pubmed:25416956 |
| CA8 | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-25511|pubmed:25910212 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.3 + PDB: 8ARF | pLDDT=74.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, microtubule organizing ce / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. SPDL1 — Protein Spindly，研究基础较多，新颖性有限。
2. 蛋白大小605 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 190 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 190 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96EA4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000040275-SPDL1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SPDL1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96EA4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96EA4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96EA4 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR028593;IPR051149; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000040275-SPDL1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| USP15 | Intact, Biogrid | true |
| CA8 | Intact | false |
| DNAAF4 | Intact | false |
| MAPRE1 | Opencell | false |
| MYC | Biogrid | false |
| PPP1R18 | Intact | false |
| RPS5 | Biogrid | false |
| RTP5 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
