---
type: protein-evaluation
gene: "RAC1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## RAC1 — REJECTED (研究热度过高 (PubMed strict=6186，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RAC1 / TC25 |
| 蛋白名称 | Ras-related C3 botulinum toxin substrate 1 |
| 蛋白大小 | 192 aa / 21.4 kDa |
| UniProt ID | P63000 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; 额外: Nucleoli; UniProt: Cell membrane; Melanosome; Cytoplasm; Cell projection, lamel |
| 蛋白大小 | 8/10 | ×1 | 8 | 192 aa / 21.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=6186 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=93.8; PDB: 1E96, 1FOE, 1G4U, 1HE1, 1HH4, 1I4D, 1I4L |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR027417, IPR005225, IPR001806, IPR003578; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Nucleoli | Supported |
| UniProt | Cell membrane; Melanosome; Cytoplasm; Cell projection, lamellipodium; Cell projection, dendrite; Syn... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cell cortex (GO:0005938)
- cell projection (GO:0042995)
- cytoplasm (GO:0005737)
- cytoplasmic ribonucleoprotein granule (GO:0036464)
- cytoplasmic vesicle (GO:0031410)
- cytoskeleton (GO:0005856)
- cytosol (GO:0005829)
- dendrite (GO:0030425)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6186 |
| PubMed broad count | 11526 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TC25 |

**关键文献**:
1. Identification of RAC1 in promoting brain metastasis of lung adenocarcinoma using single-cell transcriptome sequencing.. *Cell death & disease*. PMID: 37202394
2. Rac1 Suppression by the Focal Adhesion Protein GIT ArfGAP2 and Podocyte Protection.. *Journal of the American Society of Nephrology : JASN*. PMID: 40019803
3. Implication of Rac1 GTPase in molecular and cellular mitochondrial functions.. *Life sciences*. PMID: 38387701
4. Destabilization of fear memory by Rac1-driven engram-microglia communication in hippocampus.. *Brain, behavior, and immunity*. PMID: 38670239
5. Stress-Sensitive Protein Rac1 and Its Involvement in Neurodevelopmental Disorders.. *Neural plasticity*. PMID: 33299404

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.8 |
| 高置信度残基 (pLDDT>90) 占比 | 86.5% |
| 置信残基 (pLDDT 70-90) 占比 | 7.3% |
| 中等置信 (pLDDT 50-70) 占比 | 6.2% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 93.8% |
| 可用 PDB 条目 | 1E96, 1FOE, 1G4U, 1HE1, 1HH4, 1I4D, 1I4L, 1I4T, 1MH1, 1RYF |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1E96, 1FOE, 1G4U, 1HE1, 1HH4, 1I4D, 1I4L, 1I4T, 1MH1, 1RYF）+ AlphaFold极高置信度预测（pLDDT=93.8），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027417, IPR005225, IPR001806, IPR003578; Pfam: PF00071 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PAK1 | 0.999 | 0.995 | — |
| NCF2 | 0.999 | 0.982 | — |
| TRIO | 0.994 | 0.980 | — |
| ARHGDIA | 0.994 | 0.926 | — |
| ARFIP2 | 0.993 | 0.987 | — |
| PREX1 | 0.993 | 0.971 | — |
| CYFIP1 | 0.993 | 0.957 | — |
| NCKAP1 | 0.990 | 0.935 | — |
| IQGAP1 | 0.988 | 0.901 | — |
| PAK2 | 0.983 | 0.840 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ARFIP2 | psi-mi:"MI:0018"(two hybrid) | pubmed:8670882|mint:MINT-52210 |
| ARF6 | psi-mi:"MI:0018"(two hybrid) | pubmed:9312003 |
| ARF3 | psi-mi:"MI:0018"(two hybrid) | pubmed:9312003 |
| ITGB3BP | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| LY6D | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| hrpA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| SNX1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| DISC1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| CEP63 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.8 + PDB: 1E96, 1FOE, 1G4U, 1HE1, 1HH4,  | pLDDT=93.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane; Melanosome; Cytoplasm; Cell project / Nucleoplasm, Cytosol; 额外: Nucleoli | 一致 |
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
1. RAC1 — Ras-related C3 botulinum toxin substrate 1，研究基础较多，新颖性有限。
2. 蛋白大小192 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 6186 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 6186 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P63000
- Protein Atlas: https://www.proteinatlas.org/ENSG00000136238-RAC1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RAC1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P63000
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000136238-RAC1/subcellular

![](https://images.proteinatlas.org/35994/265_F2_1_red_green.jpg)
![](https://images.proteinatlas.org/35994/265_F2_2_red_green.jpg)
![](https://images.proteinatlas.org/35994/266_F2_1_red_green.jpg)
![](https://images.proteinatlas.org/35994/266_F2_2_red_green.jpg)
![](https://images.proteinatlas.org/35994/267_F2_1_red_green.jpg)
![](https://images.proteinatlas.org/35994/267_F2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P63000-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
