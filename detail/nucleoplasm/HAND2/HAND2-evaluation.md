---
type: protein-evaluation
gene: "HAND2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## HAND2 — REJECTED (研究热度过高 (PubMed strict=437，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HAND2 |
| 蛋白名称 | HAND2 (UniProt未获取) |
| 蛋白大小 | 未知 aa / 未知 kDa |
| UniProt ID | HAND2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Vesicles; UniProt: 暂无数据（UniProt获取失败） |
| 蛋白大小 | 5/10 | ×1 | 5 | 未知 aa / 未知 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=437 篇 (>100→REJECTED) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | 暂无数据 (UniProt未获取) |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **65/180** | |
| **归一化总分** | | | **36.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles | Approved |
| UniProt | 暂无数据（UniProt获取失败） | 获取失败 |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释 (UniProt未获取)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 437 |
| PubMed broad count | 765 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Cardiac Reprogramming and Gata4 Overexpression Reduce Fibrosis and Improve Diastolic Dysfunction in Heart Failure With Preserved Ejection Fraction.. *Circulation*. PMID: 39673349
2. Direct Reprogramming Improves Cardiac Function and Reverses Fibrosis in Chronic Myocardial Infarction.. *Circulation*. PMID: 36503256
3. Heterogeneity of neuroblastoma cell identity defined by transcriptional circuitries.. *Nature genetics*. PMID: 28740262
4. Super-enhancer-driven IRF2BP2 enhances ALK activity and promotes neuroblastoma cell proliferation.. *Neuro-oncology*. PMID: 38864832
5. Targeting SWI/SNF ATPases reduces neuroblastoma cell plasticity.. *The EMBO journal*. PMID: 39174852

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v? |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 暂无数据 (UniProt未获取) |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSMUSP00000044983.4 | psi-mi:"MI:0096"(pull down) | pubmed:10924525 |
| Mcf2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Hand1 | psi-mi:"MI:0018"(two hybrid) | pubmed:10924525 |
| Tcf3 | psi-mi:"MI:0018"(two hybrid) | pubmed:10924525 |
| Hey2 | psi-mi:"MI:0096"(pull down) | pubmed:10924525 |
| Hey1 | psi-mi:"MI:0096"(pull down) | pubmed:10924525 |
| Heyl | psi-mi:"MI:0096"(pull down) | pubmed:10924525 |
| RAD21 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| SPANXN3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| RIPPLY1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v? | 仅预测 |
| 定位 | UniProt + HPA | 暂无数据（UniProt获取失败） / Nucleoplasm; 额外: Vesicles | 待确认 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. HAND2 — HAND2 (UniProt未获取)，研究基础较多，新颖性有限。
2. 蛋白大小未知 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 437 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 437 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/HAND2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000164107-HAND2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HAND2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/HAND2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000164107-HAND2/subcellular

![](https://images.proteinatlas.org/19591/1223_C3_1_red_green.jpg)
![](https://images.proteinatlas.org/19591/1223_C3_2_red_green.jpg)
![](https://images.proteinatlas.org/19591/1446_G10_2_red_green.jpg)
![](https://images.proteinatlas.org/19591/1446_G10_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P61296 |
| SMART | SM00353; |
| UniProt Domain [FT] | DOMAIN 99..151; /note="bHLH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00981" |
| InterPro | IPR011598;IPR050283;IPR036638; |
| Pfam | PF00010; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000164107-HAND2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| TCF4 | Intact, Biogrid | true |
| GATA4 | Biogrid | false |
| PHOX2A | Biogrid | false |
| PPP2R5D | Biogrid | false |
| RAD21 | Biogrid | false |
| TCF12 | Biogrid | false |
| TCF3 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
