---
type: protein-evaluation
gene: "MDFI"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MDFI 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MDFI |
| 蛋白名称 | MyoD family inhibitor |
| 蛋白大小 | 246 aa / 25.0 kDa |
| UniProt ID | Q99750 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 246 aa / 25.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=31 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=50.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026134; Pfam: PF15316 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.0/180** | |
| **归一化总分** | | | **66.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 31 |
| PubMed broad count | 86 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. MDFIC2 is a PIEZO channel modulator that can alleviate mechanical allodynia associated with neuropathic pain.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 41201821
2. The role of miR-128 and MDFI in cardiac hypertrophy and heart failure: Mechanistic.. *Journal of cellular and molecular medicine*. PMID: 39046458
3. Metabolic reprogramming in Helicobacter pylori infection: from mechanisms to therapeutics.. *Frontiers in cellular and infection microbiology*. PMID: 41158522
4. ACAN, MDFI, and CHST1 as Candidate Genes in Gastric Cancer: A Comprehensive Insilco Analysis.. *Asian Pacific journal of cancer prevention : APJCP*. PMID: 35225482
5. MDFI promotes the proliferation and tolerance to chemotherapy of colorectal cancer cells by binding ITGB4/LAMB3 to activate the AKT signaling pathway.. *Cancer biology & therapy*. PMID: 38375821

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 50.6 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 5.3% |
| 中等置信 (pLDDT 50-70) 占比 | 39.8% |
| 低置信 (pLDDT<50) 占比 | 54.9% |
| 有序区域 (pLDDT>70) 占比 | 5.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=50.6），有序残基占 5.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026134; Pfam: PF15316 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MYOD1 | 0.892 | 0.292 | — |
| OTX1 | 0.639 | 0.628 | — |
| SPRY1 | 0.636 | 0.601 | — |
| AQP1 | 0.632 | 0.624 | — |
| BEX2 | 0.619 | 0.591 | — |
| BBS2 | 0.606 | 0.606 | — |
| ZFYVE26 | 0.600 | 0.600 | — |
| SLC25A10 | 0.599 | 0.591 | — |
| LCE3D | 0.591 | 0.591 | — |
| NEU4 | 0.566 | 0.566 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000362142.2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| RABL6 | psi-mi:"MI:0096"(pull down) | pubmed:16189514|imex:IM-16520| |
| BAALC | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ZNF440 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| LMO3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TAP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| INTS11 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ZNF581 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CNNM3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| LASP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=50.6 + PDB: 无 | pLDDT=50.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm | 一致 |
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
1. MDFI — MyoD family inhibitor，非常新颖，仅有少数基础研究。
2. 蛋白大小246 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 31 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=50.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q99750
- Protein Atlas: https://www.proteinatlas.org/ENSG00000112559-MDFI/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MDFI
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q99750
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000112559-MDFI/subcellular

![](https://images.proteinatlas.org/49973/756_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/49973/756_A3_2_red_green.jpg)
![](https://images.proteinatlas.org/49973/760_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/49973/760_A3_3_red_green.jpg)
![](https://images.proteinatlas.org/49973/775_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/49973/775_A3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q99750-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q99750 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 99..246; /note="MDFI" |
| InterPro | IPR026134; |
| Pfam | PF15316; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000112559-MDFI/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| APLN | Intact, Biogrid | true |
| AQP1 | Intact, Biogrid | true |
| ATOSB | Intact, Biogrid | true |
| C10orf62 | Intact, Biogrid | true |
| CBFA2T2 | Intact, Biogrid | true |
| CCDC120 | Intact, Biogrid | true |
| DCAF6 | Intact, Biogrid | true |
| DCAF8 | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
