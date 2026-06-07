---
type: protein-evaluation
gene: "NTAQ1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NTAQ1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NTAQ1 / C8orf32, WDYHV1 |
| 蛋白名称 | Protein N-terminal glutamine amidohydrolase |
| 蛋白大小 | 205 aa / 23.7 kDa |
| UniProt ID | Q96HA8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Vesicles; UniProt: Cytoplasm, cytosol; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 205 aa / 23.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=94.3; PDB: 3C9Q, 4W79, 6KGJ, 8JJF, 8JJG, 8JJH, 8JJI |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR037132, IPR039733, IPR023128; Pfam: PF09764 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **146.0/180** | |
| **归一化总分** | | | **81.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles | Supported |
| UniProt | Cytoplasm, cytosol; Nucleus | Swiss-Prot/TrEMBL |

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
| PubMed strict count | 10 |
| PubMed broad count | 13 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C8orf32, WDYHV1 |

**关键文献**:
1. Glutamine-specific N-terminal amidase, a component of the N-end rule pathway.. *Molecular cell*. PMID: 19560421
2. Cereblon covalent modulation through structure-based design of histidine targeting chemical probes.. *RSC chemical biology*. PMID: 36128501
3. Structural basis for dual specificity of yeast N-terminal amidase in the N-end rule pathway.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 27791147
4. Crystal structure of human protein N-terminal glutamine amidohydrolase, an initial component of the N-end rule pathway.. *PloS one*. PMID: 25356641
5. Structural study for substrate recognition of human N-terminal glutamine amidohydrolase 1 in the arginine N-degron pathway.. *Protein science : a publication of the Protein Society*. PMID: 38864716

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.3 |
| 高置信度残基 (pLDDT>90) 占比 | 90.2% |
| 置信残基 (pLDDT 70-90) 占比 | 3.9% |
| 中等置信 (pLDDT 50-70) 占比 | 2.0% |
| 低置信 (pLDDT<50) 占比 | 3.9% |
| 有序区域 (pLDDT>70) 占比 | 94.1% |
| 可用 PDB 条目 | 3C9Q, 4W79, 6KGJ, 8JJF, 8JJG, 8JJH, 8JJI, 8JJU, 8JJW, 8JJX |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（3C9Q, 4W79, 6KGJ, 8JJF, 8JJG, 8JJH, 8JJI, 8JJU, 8JJW, 8JJX）+ AlphaFold极高置信度预测（pLDDT=94.3），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR037132, IPR039733, IPR023128; Pfam: PF09764 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| UBR2 | 0.790 | 0.292 | — |
| NTAN1 | 0.776 | 0.230 | — |
| UBR1 | 0.756 | 0.230 | — |
| ATE1 | 0.728 | 0.000 | — |
| ATAD2 | 0.614 | 0.000 | — |
| UBE2A | 0.612 | 0.000 | — |
| C1orf50 | 0.574 | 0.329 | — |
| COPZ2 | 0.573 | 0.000 | — |
| TRABD | 0.530 | 0.000 | — |
| HSD17B14 | 0.530 | 0.530 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TRIP13 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| RABAC1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| RPIA | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| SFN | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MDFI | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| HPRT1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| JUP | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CBFA2T2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| BLOC1S6 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| PCBD1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.3 + PDB: 3C9Q, 4W79, 6KGJ, 8JJF, 8JJG,  | pLDDT=94.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol; Nucleus / Nucleoplasm; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. NTAQ1 — Protein N-terminal glutamine amidohydrolase，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小205 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96HA8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000156795-NTAQ1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NTAQ1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96HA8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000156795-NTAQ1/subcellular

![](https://images.proteinatlas.org/24823/230_F7_1_red_green.jpg)
![](https://images.proteinatlas.org/24823/230_F7_2_red_green.jpg)
![](https://images.proteinatlas.org/24823/231_F7_1_red_green.jpg)
![](https://images.proteinatlas.org/24823/231_F7_2_red_green.jpg)
![](https://images.proteinatlas.org/24823/232_F7_1_red_green.jpg)
![](https://images.proteinatlas.org/24823/232_F7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96HA8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96HA8 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR037132;IPR039733;IPR023128; |
| Pfam | PF09764; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000156795-NTAQ1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ACTB | Intact, Biogrid | true |
| BIRC2 | Intact, Biogrid, Bioplex | true |
| BTBD1 | Intact, Biogrid, Bioplex | true |
| COIL | Intact, Biogrid | true |
| PLA2G10 | Intact, Biogrid | true |
| RAD54L | Intact, Biogrid, Bioplex | true |
| VAC14 | Intact, Biogrid | true |
| XIAP | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
