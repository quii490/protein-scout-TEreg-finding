---
type: protein-evaluation
gene: "CYFIP2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CYFIP2 — REJECTED (研究热度过高 (PubMed strict=120，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CYFIP2 / KIAA1168, PIR121 |
| 蛋白名称 | Cytoplasmic FMR1-interacting protein 2 |
| 蛋白大小 | 1278 aa / 148.4 kDa |
| UniProt ID | Q96F07 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Endoplasmic reticulum; 额外: Plasma membrane, Cytosol; UniProt: Cytoplasm; Nucleus; Cytoplasm, perinuclear region; Synapse,  |
| 蛋白大小 | 5/10 | ×1 | 5 | 1278 aa / 148.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=120 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=86.8; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR009828, IPR008081; Pfam: PF07159, PF05994 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **83.5/180** | |
| **归一化总分** | | | **46.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Endoplasmic reticulum; 额外: Plasma membrane, Cytosol | Approved |
| UniProt | Cytoplasm; Nucleus; Cytoplasm, perinuclear region; Synapse, synaptosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- membrane (GO:0016020)
- neuron projection (GO:0043005)
- nucleus (GO:0005634)
- perinuclear region of cytoplasm (GO:0048471)
- SCAR complex (GO:0031209)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 120 |
| PubMed broad count | 154 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1168, PIR121 |

**关键文献**:
1. Analysis and Experimental Validation of Rheumatoid Arthritis Innate Immunity Gene CYFIP2 and Pan-Cancer.. *Frontiers in immunology*. PMID: 35898498
2. CYFIP2 p.Arg87Cys Causes Neurological Defects and Degradation of CYFIP2.. *Annals of neurology*. PMID: 36251395
3. Haploinsufficiency of Cyfip2 Causes Lithium-Responsive Prefrontal Dysfunction.. *Annals of neurology*. PMID: 32562430
4. CYFIP2: potential pancreatic cancer biomarker and immunotherapeutic target.. *Discover oncology*. PMID: 39739214
5. Neurodevelopmental disorder-associated CYFIP2 regulates membraneless organelles and eIF2α phosphorylation via protein interactors and actin cytoskeleton.. *Human molecular genetics*. PMID: 38981622

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.8 |
| 高置信度残基 (pLDDT>90) 占比 | 62.1% |
| 置信残基 (pLDDT 70-90) 占比 | 28.0% |
| 中等置信 (pLDDT 50-70) 占比 | 4.5% |
| 低置信 (pLDDT<50) 占比 | 5.4% |
| 有序区域 (pLDDT>70) 占比 | 90.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=86.8，有序区 90.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009828, IPR008081; Pfam: PF07159, PF05994 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BRK1 | 0.999 | 0.590 | — |
| FMR1 | 0.999 | 0.568 | — |
| NCKAP1 | 0.999 | 0.968 | — |
| WASF2 | 0.999 | 0.880 | — |
| NCKAP1L | 0.999 | 0.895 | — |
| ABI1 | 0.999 | 0.861 | — |
| FXR1 | 0.999 | 0.368 | — |
| ABI2 | 0.999 | 0.741 | — |
| FXR2 | 0.999 | 0.368 | — |
| WASF1 | 0.999 | 0.885 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| YWHAH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:14676191 |
| YWHAZ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:14676191 |
| GRB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15417|pubmed:21706016 |
| ZC3H12A | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| BIRC3 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| SMAD4 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| aspA1 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| Dlg4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-11694|pubmed:19455133 |
| Abi1 | psi-mi:"MI:0096"(pull down) | imex:IM-8314|pubmed:20697350|m |
| PLG | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.8 + PDB: 无 | pLDDT=86.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Cytoplasm, perinuclear region; / Endoplasmic reticulum; 额外: Plasma membrane, Cytoso | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CYFIP2 — Cytoplasmic FMR1-interacting protein 2，研究基础较多，新颖性有限。
2. 蛋白大小1278 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 120 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 120 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96F07
- Protein Atlas: https://www.proteinatlas.org/ENSG00000055163-CYFIP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CYFIP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96F07
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Endoplasmic reticulum (approved)。来源: https://www.proteinatlas.org/ENSG00000055163-CYFIP2/subcellular

![](https://images.proteinatlas.org/71459/1469_E11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/71459/1469_E11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/71459/1478_E11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/71459/1478_E11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/71459/1523_H9_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/71459/1523_H9_5_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96F07-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
