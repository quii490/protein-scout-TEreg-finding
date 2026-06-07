---
type: protein-evaluation
gene: "TASOR"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TASOR 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TASOR / C3orf63, FAM208A, KIAA1105 |
| 蛋白名称 | Protein TASOR |
| 蛋白大小 | 1670 aa / 189.0 kDa |
| UniProt ID | Q9UK61 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus; Chromosome |
| 蛋白大小 | 5/10 | ×1 | 5 | 1670 aa / 189.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=17 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=56.3; PDB: 6SWG, 6TL1 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR056242, IPR046432, IPR056243, IPR022188; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus; Chromosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- heterochromatin (GO:0000792)
- HUSH complex (GO:0140283)
- nucleoplasm (GO:0005654)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 17 |
| PubMed broad count | 30 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C3orf63, FAM208A, KIAA1105 |

**关键文献**:
1. Selective silencing of euchromatic L1s revealed by genome-wide screens for L1 regulators.. *Nature*. PMID: 29211708
2. LINE-1 repression in Epstein-Barr virus-associated gastric cancer through viral-host genome interaction.. *Nucleic acids research*. PMID: 36942479
3. Interplay between Two Paralogous Human Silencing Hub (HuSH) Complexes in Regulating LINE-1 Element Silencing.. *Nature communications*. PMID: 39489739
4. TASOR expression in naive embryonic stem cells safeguards their developmental potential.. *Cell reports*. PMID: 39453814
5. GENE SILENCING. Epigenetic silencing by the HUSH complex mediates position-effect variegation in human cells.. *Science (New York, N.Y.)*. PMID: 26022416

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 56.3 |
| 高置信度残基 (pLDDT>90) 占比 | 17.7% |
| 置信残基 (pLDDT 70-90) 占比 | 20.1% |
| 中等置信 (pLDDT 50-70) 占比 | 9.6% |
| 低置信 (pLDDT<50) 占比 | 52.6% |
| 有序区域 (pLDDT>70) 占比 | 37.8% |
| 可用 PDB 条目 | 6SWG, 6TL1 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=56.3），有序残基占 37.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR056242, IPR046432, IPR056243, IPR022188; Pfam: PF12509, PF24630, PF23314 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PPHLN1 | 0.999 | 0.926 | — |
| MPHOSPH8 | 0.998 | 0.608 | — |
| SETDB1 | 0.822 | 0.304 | — |
| MORC2 | 0.718 | 0.000 | — |
| ZNF638 | 0.673 | 0.046 | — |
| YTHDC1 | 0.580 | 0.292 | — |
| DCAF1 | 0.503 | 0.000 | — |
| ATF7IP | 0.486 | 0.045 | — |
| USP17L19 | 0.473 | 0.000 | — |
| ATRX | 0.464 | 0.071 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TOM1L1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| TBC1D4 | psi-mi:"MI:0018"(two hybrid) | pubmed:unassigned5 |
| AP2M1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| GTF2F2 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| ypeB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| lysS | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| asd | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| REEP5 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| PB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28169297|imex:IM-25584 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=56.3 + PDB: 6SWG, 6TL1 | pLDDT=56.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TASOR — Protein TASOR，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1670 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 17 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=56.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UK61
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163946-TASOR/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TASOR
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UK61
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000163946-TASOR/subcellular

![](https://images.proteinatlas.org/17142/138_F2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17142/138_F2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/17142/139_F2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17142/139_F2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/17142/166_F2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17142/166_F2_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UK61-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9UK61 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 166..319; /note="TASOR pseudo-PARP"; /evidence="ECO:0000269\|PubMed:33009411" |
| InterPro | IPR056242;IPR046432;IPR056243;IPR022188; |
| Pfam | PF12509;PF24630;PF23314; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000163946-TASOR/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| MPHOSPH8 | Intact, Biogrid | true |
| CPSF6 | Opencell | false |
| EZH2 | Biogrid | false |
| MATR3 | Biogrid | false |
| SNRPA | Opencell | false |
| SNRPC | Opencell | false |
| SSRP1 | Opencell | false |
| TOP1 | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
