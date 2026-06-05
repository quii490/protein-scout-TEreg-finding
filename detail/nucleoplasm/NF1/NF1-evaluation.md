---
type: protein-evaluation
gene: "NF1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## NF1 — REJECTED (研究热度过高 (PubMed strict=4516，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NF1 |
| 蛋白名称 | Neurofibromin |
| 蛋白大小 | 2839 aa / 319.4 kDa |
| UniProt ID | P21359 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane; 额外: Nucleoplasm, Microtubules; UniProt: Nucleus; Nucleus, nucleolus; Cell membrane |
| 蛋白大小 | 2/10 | ×1 | 2 | 2839 aa / 319.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=4516 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=87.2; PDB: 1NF1, 2D4Q, 2E2X, 3P7Z, 3PEG, 3PG7, 6OB2 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR016024, IPR001251, IPR036865, IPR011993, IPR054 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.0/180** | |
| **归一化总分** | | | **48.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane; 额外: Nucleoplasm, Microtubules | Supported |
| UniProt | Nucleus; Nucleus, nucleolus; Cell membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- axon (GO:0030424)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- dendrite (GO:0030425)
- glutamatergic synapse (GO:0098978)
- membrane (GO:0016020)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4516 |
| PubMed broad count | 10349 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Segmental neurofibromatosis.. *Dermatology (Basel, Switzerland)*. PMID: 12077526
2. Neurofibromatosis type 1.. *American journal of medical genetics*. PMID: 11180219
3. NF1 gene and neurofibromatosis 1.. *American journal of epidemiology*. PMID: 10625171
4. MEK-SHP2 inhibition prevents tibial pseudarthrosis caused by NF1 loss in Schwann cells and skeletal stem/progenitor cells.. *Science translational medicine*. PMID: 38924432
5. The NF1 gene in tumor syndromes and melanoma.. *Laboratory investigation; a journal of technical methods and pathology*. PMID: 28067895

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.2 |
| 高置信度残基 (pLDDT>90) 占比 | 67.5% |
| 置信残基 (pLDDT 70-90) 占比 | 21.1% |
| 中等置信 (pLDDT 50-70) 占比 | 4.6% |
| 低置信 (pLDDT<50) 占比 | 6.9% |
| 有序区域 (pLDDT>70) 占比 | 88.6% |
| 可用 PDB 条目 | 1NF1, 2D4Q, 2E2X, 3P7Z, 3PEG, 3PG7, 6OB2, 6OB3, 6V65, 6V6F |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1NF1, 2D4Q, 2E2X, 3P7Z, 3PEG, 3PG7, 6OB2, 6OB3, 6V65, 6V6F）+ AlphaFold极高置信度预测（pLDDT=87.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016024, IPR001251, IPR036865, IPR011993, IPR054071; Pfam: PF13716, PF21877, PF00616 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KRAS | 0.996 | 0.543 | — |
| NRAS | 0.994 | 0.568 | — |
| HRAS | 0.994 | 0.789 | — |
| SPRED1 | 0.992 | 0.792 | — |
| NF2 | 0.970 | 0.000 | — |
| RRAS | 0.960 | 0.320 | — |
| RRAS2 | 0.958 | 0.320 | — |
| MRAS | 0.955 | 0.320 | — |
| BRAF | 0.903 | 0.092 | — |
| SPRED2 | 0.884 | 0.493 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| sgg | psi-mi:"MI:0963"(interactome parallel affinity cap | pubmed:21447707|imex:IM-17304 |
| NetB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-16527|pubmed:25294943 |
| BNIP3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-16527|pubmed:25294943 |
| Spn | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-16527|pubmed:25294943 |
| CALM1 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:16512683|imex:IM-19867 |
| SDC2 | psi-mi:"MI:0018"(two hybrid) | pubmed:11356864|imex:IM-19039| |
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| Sdc1 | psi-mi:"MI:0018"(two hybrid) | pubmed:11356864|imex:IM-19039| |
| Sdc3 | psi-mi:"MI:0018"(two hybrid) | pubmed:11356864|imex:IM-19039| |
| Sdc4 | psi-mi:"MI:0018"(two hybrid) | pubmed:11356864|imex:IM-19039| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.2 + PDB: 1NF1, 2D4Q, 2E2X, 3P7Z, 3PEG,  | pLDDT=87.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus, nucleolus; Cell membrane / Plasma membrane; 额外: Nucleoplasm, Microtubules | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. NF1 — Neurofibromin，研究基础较多，新颖性有限。
2. 蛋白大小2839 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 4516 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 4516 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P21359
- Protein Atlas: https://www.proteinatlas.org/ENSG00000196712-NF1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NF1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P21359
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (supported)。来源: https://www.proteinatlas.org/ENSG00000196712-NF1/subcellular

![](https://images.proteinatlas.org/75627/2056_A11_2_red_green.jpg)
![](https://images.proteinatlas.org/75627/2056_A11_6_red_green.jpg)
![](https://images.proteinatlas.org/75627/2088_D7_3_red_green.jpg)
![](https://images.proteinatlas.org/75627/2088_D7_4_red_green.jpg)
![](https://images.proteinatlas.org/75627/2154_E2_1_red_green.jpg)
![](https://images.proteinatlas.org/75627/2154_E2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
