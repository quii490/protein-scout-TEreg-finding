---
type: protein-evaluation
gene: "MYOZ2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MYOZ2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MYOZ2 / C4orf5 |
| 蛋白名称 | Myozenin-2 |
| 蛋白大小 | 264 aa / 29.9 kDa |
| UniProt ID | Q9NPC6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Cytosol; UniProt: Cytoplasm, myofibril, sarcomere, Z line |
| 蛋白大小 | 10/10 | ×1 | 10 | 264 aa / 29.9 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=39 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR008438; Pfam: PF05556 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **108.0/180** | |
| **归一化总分** | | | **60.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Approved |
| UniProt | Cytoplasm, myofibril, sarcomere, Z line | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- actin cytoskeleton (GO:0015629)
- sarcomere (GO:0030017)
- Z disc (GO:0030018)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 39 |
| PubMed broad count | 62 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C4orf5 |

**关键文献**:
1. Nonsyndromic Hypertrophic Cardiomyopathy Overview.. **. PMID: 20301725
2. Potential Biomarkers in Myocardial Fibrosis: A Bioinformatic Analysis.. *Arquivos brasileiros de cardiologia*. PMID: 39699450
3. Interaction of MyoD and MyoG with Myoz2 gene in bovine myoblast differentiation.. *Research in veterinary science*. PMID: 36191510
4. Expression and prognosis of MYOZ2 in gastric cancer.. *European review for medical and pharmacological sciences*. PMID: 30280773
5. Molecular cloning and characterization of different expression of MYOZ2 and MYOZ3 in Tianfu goat.. *PloS one*. PMID: 24367523

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.7 |
| 高置信度残基 (pLDDT>90) 占比 | 6.1% |
| 置信残基 (pLDDT 70-90) 占比 | 25.8% |
| 中等置信 (pLDDT 50-70) 占比 | 54.9% |
| 低置信 (pLDDT<50) 占比 | 13.3% |
| 有序区域 (pLDDT>70) 占比 | 31.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=64.7），有序残基占 31.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008438; Pfam: PF05556 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TCAP | 0.992 | 0.510 | — |
| ACTN2 | 0.987 | 0.330 | — |
| CSRP3 | 0.952 | 0.000 | — |
| MYOT | 0.927 | 0.000 | — |
| LDB3 | 0.925 | 0.000 | — |
| MYL2 | 0.905 | 0.000 | — |
| LMOD2 | 0.897 | 0.000 | — |
| FLNC | 0.889 | 0.292 | — |
| MYL3 | 0.829 | 0.000 | — |
| MYH7 | 0.820 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EWSR1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| Prkce | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:12169683 |
| PDLIM3 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| MYB | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| pnp | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| katG | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ACTN4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| araB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ACTN2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| AMEL | psi-mi:"MI:0096"(pull down) | pubmed:31621902|imex:IM-26981 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.7 + PDB: 无 | pLDDT=64.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, myofibril, sarcomere, Z line / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. MYOZ2 — Myozenin-2，非常新颖，仅有少数基础研究。
2. 蛋白大小264 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 39 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=64.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NPC6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000172399-MYOZ2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MYOZ2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NPC6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000172399-MYOZ2/subcellular

![](https://images.proteinatlas.org/35764/1364_B10_1_red_green.jpg)
![](https://images.proteinatlas.org/35764/1364_B10_2_red_green.jpg)
![](https://images.proteinatlas.org/35764/392_H1_1_red_green.jpg)
![](https://images.proteinatlas.org/35764/392_H1_2_red_green.jpg)
![](https://images.proteinatlas.org/35764/393_H1_2_red_green.jpg)
![](https://images.proteinatlas.org/35764/393_H1_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NPC6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NPC6 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR008438; |
| Pfam | PF05556; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000172399-MYOZ2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ACTN4 | Intact, Biogrid | true |
| ACTN1 | Intact | false |
| ACTN2 | Intact | false |
| DRICH1 | Intact | false |
| FGFR3 | Intact | false |
| GRIN2C | Intact | false |
| GSN | Intact | false |
| MKRN3 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
