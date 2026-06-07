---
type: protein-evaluation
gene: "CETN1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation, E-batch]
status: scored
---

## CETN1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CETN1 / CEN1 / CETN |
| 蛋白名称 | Centrin-1 |
| 蛋白大小 | 172 aa / 19.6 kDa |
| UniProt ID | Q12798 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 6/10 | ×4 | 24 | HPA: Nucleoplasm, Flagellar centriole; 额外: Mid piece, Principal piece; UniProt: Cytoplasm, cytoskele |
| 蛋白大小 | 8/10 | ×1 | 8 | 172 aa / 19.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=11 篇 |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=86.1; PDB: 暂无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR050145, IPR011992, IPR018247, IPR002048, IPR000629; Pfam: PF13499 |
| PPI 网络 | 10/10 | ×3 | 30 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.2 | AlphaFold 结构预测: +0.25 |
| **原始总分** | | | **154.2/180** | |
| **归一化总分 (÷1.83)** | | | **84.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Flagellar centriole | Supported |
| UniProt | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome | ECO:0000269
| UniProt | Cell projection, cilium | ECO:0000250

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- centriole (GO:0005814) [IDA:MGI]
- centrosome (GO:0005813) [IDA:UniProtKB]
- cytosol (GO:0005829) [TAS:Reactome]
- nucleus (GO:0005634) [IBA:GO_Central]
- photoreceptor connecting cilium (GO:0032391) [ISS:UniProtKB]
- spindle pole (GO:0000922) [IDA:UniProtKB]

**结论**: HPA: Nucleoplasm, Flagellar centriole; 额外: Mid piece, Principal piece; UniProt: Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Cell projection, cilium

#### 3.2 蛋白大小评估

**评价**: 172 aa / 19.6 kDa，大小适合大部分生化实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11 |
| PubMed 搜索链接 | [CETN1 PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=CETN1) |

**关键文献**:
暂无文献记录。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.1 |
| 高置信度残基 (pLDDT>90) 占比 | 68.0% |
| 置信残基 (pLDDT 70-90) 占比 | 17.4% |
| 中等置信 (pLDDT 50-70) 占比 | 6.4% |
| 低置信 (pLDDT<50) 占比 | 8.1% |
| 有序区域 (pLDDT>70) 占比 | 85.4% |
| 可用 PDB 条目 | 暂无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050145, IPR011992, IPR018247, IPR002048, IPR000629; Pfam: PF13499 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PCNT | 0.938 | 0.276 | — |
| POC5 | 0.935 | 0.786 | — |
| SFI1 | 0.924 | 0.763 | — |
| NIN | 0.867 | 0.189 | — |
| SGSM1 | 0.806 | 0.803 | — |
| ENY2 | 0.804 | 0.686 | — |
| PCM1 | 0.762 | 0.124 | — |
| CCP110 | 0.758 | 0.510 | — |
| CETN2 | 0.741 | 0.592 | — |
| CEP290 | 0.740 | 0.254 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| USP49 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| ZFAND5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| POC5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:29892012|doi:10.1038/s41588-018-0130-z|imex:IM-27553 |
| SGSM1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s41467-019-11959-3|pubmed:31515488 |
| SFI1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| BCKDK | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| CETN3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| SGSM2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| PPIP5K2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| MCM3AP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |

**PPI 互证分析**:
STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0/15。

**评价**: STRING + IntAct 双源 PPI 数据充分。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold | pLDDT=86.1, v6 | 预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Cell projection, cilium / Nucleoplasm, Flagellar centriole | 部分一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- AlphaFold 结构预测: +0.25
- 单库核定位证据: +0.25
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5

**总分**: +1.2 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐⭐

**归一化总分**: 84.3/100

**核心优势**:
1. CETN1 — Centrin-1，极度新颖，几乎未被系统研究（PubMed 11 篇）。
2. 蛋白大小172 aa，适合大部分生化实验。
3. AlphaFold pLDDT=86.1，结构预测质量高。

**风险/不确定性**:
1. 功能研究较少，具体调控机制待阐明

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q12798
- Protein Atlas: https://www.proteinatlas.org/search/CETN1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CETN1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q12798
- STRING: https://string-db.org/network/9606.CETN1
- Packet data timestamp: 2026-06-03 04:53:04

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000177143-CETN1/subcellular

![](https://images.proteinatlas.org/28956/2204_A11_44_blue_red_green.jpg)
![](https://images.proteinatlas.org/28956/2204_A11_9_blue_red_green.jpg)
![](https://images.proteinatlas.org/69157/2200_B10_40_blue_red_green.jpg)
![](https://images.proteinatlas.org/69157/2200_B10_8_blue_red_green.jpg)
![](https://images.proteinatlas.org/28956/329_E8_1_red_green.jpg)
![](https://images.proteinatlas.org/28956/329_E8_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q12798-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q12798 |
| SMART | SM00054; |
| UniProt Domain [FT] | DOMAIN 28..63; /note="EF-hand 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00448"; DOMAIN 64..99; /note="EF-hand 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00448"; DOMAIN 101..136; /note="EF-hand 3"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00448"; DOMAIN 137..172; /note="EF-hand 4"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00448" |
| InterPro | IPR050145;IPR011992;IPR018247;IPR002048;IPR000629; |
| Pfam | PF13499; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000177143-CETN1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| POC5 | Intact, Biogrid, Bioplex | true |
| SGSM1 | Intact, Biogrid | true |
| CCDC191 | Bioplex | false |
| CCP110 | Biogrid | false |
| CETN2 | Bioplex | false |
| CETN3 | Bioplex | false |
| EFCAB11 | Bioplex | false |
| ENY2 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
