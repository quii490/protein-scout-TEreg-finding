---
type: protein-evaluation
gene: "MN1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## MN1 — REJECTED (研究热度过高 (PubMed strict=297，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MN1 |
| 蛋白名称 | Transcriptional activator MN1 |
| 蛋白大小 | 1320 aa / 136.0 kDa |
| UniProt ID | Q10571 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 5/10 | ×1 | 5 | 1320 aa / 136.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=297 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=42.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR037644 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **83.0/180** | |
| **归一化总分** | | | **46.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 297 |
| PubMed broad count | 940 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Oncogenic fusions converge on shared mechanisms in initiating astroblastoma.. *Nature*. PMID: 40369078
2. Penetrance, variable expressivity and monogenic neurodevelopmental disorders.. *European journal of medical genetics*. PMID: 38453051
3. PATZ1 fusions define a novel molecularly distinct neuroepithelial tumor entity with a broad histological spectrum.. *Acta neuropathologica*. PMID: 34417833
4. Primitive Neuroectodermal Tumor.. **. PMID: 32965836
5. Distinctive Craniofacial and Oral Anomalies in MN1 C-terminal Truncation Syndrome.. *The Chinese journal of dental research*. PMID: 38546519

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 42.0 |
| 高置信度残基 (pLDDT>90) 占比 | 2.0% |
| 置信残基 (pLDDT 70-90) 占比 | 4.2% |
| 中等置信 (pLDDT 50-70) 占比 | 5.7% |
| 低置信 (pLDDT<50) 占比 | 88.1% |
| 有序区域 (pLDDT>70) 占比 | 6.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=42.0），有序残基占 6.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR037644 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BAALC | 0.781 | 0.000 | — |
| HSPB8 | 0.767 | 0.000 | — |
| BEND2 | 0.686 | 0.000 | — |
| GARS1 | 0.685 | 0.000 | — |
| IGHMBP2 | 0.649 | 0.000 | — |
| ETV6 | 0.615 | 0.000 | — |
| AP1B1 | 0.614 | 0.000 | — |
| ACSL6 | 0.571 | 0.000 | — |
| ACSL5 | 0.558 | 0.000 | — |
| HSPB3 | 0.554 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| LMO3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| LMO1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PADI6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| LMO2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 4
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 4 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=42.0 + PDB: 无 | pLDDT=42.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 4 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. MN1 — Transcriptional activator MN1，研究基础较多，新颖性有限。
2. 蛋白大小1320 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 297 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=42.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 297 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q10571
- Protein Atlas: https://www.proteinatlas.org/ENSG00000169184-MN1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MN1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q10571
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000169184-MN1/subcellular

![](https://images.proteinatlas.org/3072/1645_A2_19_cr57b568c04df55_red_green.jpg)
![](https://images.proteinatlas.org/3072/1645_A2_2_cr57b568ba4ce65_red_green.jpg)
![](https://images.proteinatlas.org/3072/1786_A2_1_red_green.jpg)
![](https://images.proteinatlas.org/3072/1786_A2_2_red_green.jpg)
![](https://images.proteinatlas.org/3072/53_E1_1_red_green.jpg)
![](https://images.proteinatlas.org/3072/53_E1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q10571-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
