---
type: protein-evaluation
gene: "NAMPT"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## NAMPT — REJECTED (研究热度过高 (PubMed strict=901，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NAMPT / PBEF, PBEF1 |
| 蛋白名称 | Nicotinamide phosphoribosyltransferase |
| 蛋白大小 | 491 aa / 55.5 kDa |
| UniProt ID | P43490 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles; 额外: Cell Junctions; UniProt: Nucleus; Cytoplasm; Secreted |
| 蛋白大小 | 10/10 | ×1 | 10 | 491 aa / 55.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=901 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=94.2; PDB: 2E5B, 2E5C, 2E5D, 2GVG, 2GVJ, 3DGR, 3DHD |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR013785, IPR041529, IPR041525, IPR016471, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles; 额外: Cell Junctions | Approved |
| UniProt | Nucleus; Cytoplasm; Secreted | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cell junction (GO:0030054)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- mitochondrial matrix (GO:0005759)
- nuclear speck (GO:0016607)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 901 |
| PubMed broad count | 1838 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PBEF, PBEF1 |

**关键文献**:
1. NAD(+) metabolism, stemness, the immune response, and cancer.. *Signal transduction and targeted therapy*. PMID: 33384409
2. NAMPT-Driven M2 Polarization of Tumor-Associated Macrophages Leads to an Immunosuppressive Microenvironment in Colorectal Cancer.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 38308188
3. NAMPT Impairs Vascular Permeability in Periodontitis by Influencing FASN-mediated Lipogenesis.. *International journal of biological sciences*. PMID: 40303304
4. miR-146a impedes the anti-aging effect of AMPK via NAMPT suppression and NAD(+)/SIRT inactivation.. *Signal transduction and targeted therapy*. PMID: 35241643
5. Nicotinamide mononucleotide, a key NAD(+) intermediate, treats the pathophysiology of diet- and age-induced diabetes in mice.. *Cell metabolism*. PMID: 21982712

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.2 |
| 高置信度残基 (pLDDT>90) 占比 | 89.8% |
| 置信残基 (pLDDT 70-90) 占比 | 5.5% |
| 中等置信 (pLDDT 50-70) 占比 | 2.0% |
| 低置信 (pLDDT<50) 占比 | 2.6% |
| 有序区域 (pLDDT>70) 占比 | 95.3% |
| 可用 PDB 条目 | 2E5B, 2E5C, 2E5D, 2GVG, 2GVJ, 3DGR, 3DHD, 3DHF, 3DKJ, 3DKL |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2E5B, 2E5C, 2E5D, 2GVG, 2GVJ, 3DGR, 3DHD, 3DHF, 3DKJ, 3DKL）+ AlphaFold极高置信度预测（pLDDT=94.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013785, IPR041529, IPR041525, IPR016471, IPR036068; Pfam: PF18127, PF04095 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SIRT1 | 0.993 | 0.000 | — |
| NMNAT1 | 0.992 | 0.000 | — |
| NMNAT2 | 0.976 | 0.000 | — |
| NMRK1 | 0.971 | 0.000 | — |
| SIRT3 | 0.970 | 0.000 | — |
| NNMT | 0.966 | 0.000 | — |
| SIRT6 | 0.964 | 0.000 | — |
| BST1 | 0.960 | 0.000 | — |
| SIRT4 | 0.959 | 0.000 | — |
| SIRT2 | 0.958 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| AKT2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| EBI-21359121 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| DDA1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| CUL5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| HSD17B10 | psi-mi:"MI:0030"(cross-linking study) | doi:10.1016/j.cels.2017.10.010 |
| SDHA | psi-mi:"MI:0030"(cross-linking study) | doi:10.1016/j.cels.2017.10.010 |
| LRRK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31046837|imex:IM-26684 |
| P2RY6 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| DISC1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| CFTR | psi-mi:"MI:0096"(pull down) | pubmed:29924966|imex:IM-27204 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.2 + PDB: 2E5B, 2E5C, 2E5D, 2GVG, 2GVJ,  | pLDDT=94.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Secreted / Nuclear speckles; 额外: Cell Junctions | 一致 |
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
1. NAMPT — Nicotinamide phosphoribosyltransferase，研究基础较多，新颖性有限。
2. 蛋白大小491 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 901 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 901 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P43490
- Protein Atlas: https://www.proteinatlas.org/ENSG00000105835-NAMPT/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NAMPT
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P43490
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (approved)。来源: https://www.proteinatlas.org/ENSG00000105835-NAMPT/subcellular

![](https://images.proteinatlas.org/57722/1043_H9_2_red_green.jpg)
![](https://images.proteinatlas.org/57722/1043_H9_3_red_green.jpg)
![](https://images.proteinatlas.org/57722/983_B4_1_red_green.jpg)
![](https://images.proteinatlas.org/57722/983_B4_2_red_green.jpg)
![](https://images.proteinatlas.org/57722/991_B4_1_red_green.jpg)
![](https://images.proteinatlas.org/57722/991_B4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P43490-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
