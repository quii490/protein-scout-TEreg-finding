---
type: protein-evaluation
gene: "APTX"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## APTX — REJECTED (研究热度过高 (PubMed strict=111，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | APTX / AXA1 |
| 蛋白名称 | Aprataxin |
| 蛋白大小 | 356 aa / 40.7 kDa |
| UniProt ID | Q7Z2E3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nucleoli; UniProt: Nucleus, nucleoplasm; Nucleus, nucleolus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 356 aa / 40.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=111 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=80.8; PDB: 3KT9, 4NDF, 4NDG, 4NDH, 4NDI, 6CVO, 6CVP |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR041388, IPR047289, IPR019808, IPR011146, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli | Supported |
| UniProt | Nucleus, nucleoplasm; Nucleus, nucleolus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 111 |
| PubMed broad count | 191 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: AXA1 |

**关键文献**:
1. Hereditary Ataxia Overview.. **. PMID: 20301317
2. Mechanism of APTX nicked DNA sensing and pleiotropic inactivation in neurodegenerative disease.. *The EMBO journal*. PMID: 29934293
3. XRCC1 phosphorylation affects aprataxin recruitment and DNA deadenylation activity.. *DNA repair*. PMID: 29477978
4. Replication-associated base excision repair/single-strand break repair regulates PARG inhibitor response via the PRMT1/PRMT5/ATR axis.. *NAR cancer*. PMID: 41480640
5. APTX acts in DNA double-strand break repair in a manner distinct from XRCC4.. *Journal of radiation research*. PMID: 36940705

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.8 |
| 高置信度残基 (pLDDT>90) 占比 | 62.4% |
| 置信残基 (pLDDT 70-90) 占比 | 12.6% |
| 中等置信 (pLDDT 50-70) 占比 | 2.8% |
| 低置信 (pLDDT<50) 占比 | 22.2% |
| 有序区域 (pLDDT>70) 占比 | 75.0% |
| 可用 PDB 条目 | 3KT9, 4NDF, 4NDG, 4NDH, 4NDI, 6CVO, 6CVP, 6CVQ, 6CVR, 6CVS |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（3KT9, 4NDF, 4NDG, 4NDH, 4NDI, 6CVO, 6CVP, 6CVQ, 6CVR, 6CVS）+ AlphaFold极高置信度预测（pLDDT=80.8），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR041388, IPR047289, IPR019808, IPR011146, IPR036265; Pfam: PF11969, PF17913, PF16278 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| XRCC1 | 0.999 | 0.784 | — |
| XRCC4 | 0.998 | 0.742 | — |
| APLF | 0.992 | 0.000 | — |
| LIG3 | 0.975 | 0.362 | — |
| TDP1 | 0.964 | 0.591 | — |
| SETX | 0.945 | 0.000 | — |
| PARP1 | 0.917 | 0.613 | — |
| POLB | 0.900 | 0.413 | — |
| COQ2 | 0.894 | 0.000 | — |
| COQ8A | 0.885 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TRIM37 | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| XRCC4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| CEP350 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| HIVEP1 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| CALCOCO1 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| CNTROB | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| SYT17 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| MAPKBP1 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| MBP | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| TSPYL2 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.8 + PDB: 3KT9, 4NDF, 4NDG, 4NDH, 4NDI,  | pLDDT=80.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus, nucleoplasm; Nucleus, nucleolus; Cytoplas / Nucleoplasm, Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. APTX — Aprataxin，研究基础较多，新颖性有限。
2. 蛋白大小356 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 111 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 111 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7Z2E3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000137074-APTX/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=APTX
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7Z2E3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/APTX/IF_images/1164_D7_5_red_green.jpg]]
![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/APTX/IF_images/1164_D7_3_red_green.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000137074-APTX/subcellular

![](https://images.proteinatlas.org/64930/1164_D7_3_red_green.jpg)
![](https://images.proteinatlas.org/64930/1164_D7_5_red_green.jpg)
![](https://images.proteinatlas.org/64930/1174_D7_2_red_green.jpg)
![](https://images.proteinatlas.org/64930/1174_D7_3_red_green.jpg)
![](https://images.proteinatlas.org/64930/1187_C6_1_red_green.jpg)
![](https://images.proteinatlas.org/64930/1187_C6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q7Z2E3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q7Z2E3 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 38..87; /note="FHA-like"; DOMAIN 182..287; /note="HIT"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00464" |
| InterPro | IPR041388;IPR047289;IPR019808;IPR011146;IPR036265;IPR008984;IPR032566;IPR013087; |
| Pfam | PF11969;PF17913;PF16278; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000137074-APTX/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PARP1 | Intact, Biogrid, Opencell | true |
| XRCC1 | Intact, Biogrid | true |
| XRCC4 | Intact, Biogrid | true |
| LIG3 | Biogrid | false |
| PNMA1 | Intact | false |
| SSRP1 | Opencell | false |
| TDP1 | Opencell | false |
| TP53 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
