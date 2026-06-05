---
type: protein-evaluation
gene: "SUZ12"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SUZ12 — REJECTED (研究热度过高 (PubMed strict=598，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SUZ12 / CHET9, JJAZ1, KIAA0160 |
| 蛋白名称 | Polycomb protein SUZ12 |
| 蛋白大小 | 739 aa / 83.1 kDa |
| UniProt ID | Q15022 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm, Nucleoli, Nuclear bodies; 额外: Nucleoli rim; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 739 aa / 83.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=598 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=71.0; PDB: 4W2R, 5HYN, 5IJ7, 5IJ8, 5LS6, 5WAI, 5WAK |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR019135, IPR057540; Pfam: PF09733, PF23320 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **102.0/180** | |
| **归一化总分** | | | **56.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli, Nuclear bodies; 额外: Nucleoli rim | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin silencing complex (GO:0005677)
- ESC/E(Z) complex (GO:0035098)
- nuclear body (GO:0016604)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- protein-DNA complex (GO:0032993)
- ribonucleoprotein complex (GO:1990904)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 598 |
| PubMed broad count | 904 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CHET9, JJAZ1, KIAA0160 |

**关键文献**:
1. Imagawa-Matsumoto syndrome: SUZ12-related overgrowth disorder.. *Clinical genetics*. PMID: 36645289
2. Identification and prioritization of myeloid malignancy germline variants in a large cohort of adult patients with AML.. *Blood*. PMID: 34482403
3. LncRNA-MEG3 Regulates Muscle Mass and Metabolic Homeostasis by Facilitating SUZ12 Liquid-Liquid Phase Separation.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 40285575
4. Lactylation-boosted polycomb repression of KLF4 elicits glycolysis in retinoblastoma: A positive feedback circuit between histone modifications.. *Cancer letters*. PMID: 40383410
5. Mono-methylation of lysine 27 at histone 3 confers lifelong susceptibility to stress.. *Neuron*. PMID: 38959894

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.0 |
| 高置信度残基 (pLDDT>90) 占比 | 37.6% |
| 置信残基 (pLDDT 70-90) 占比 | 23.7% |
| 中等置信 (pLDDT 50-70) 占比 | 7.8% |
| 低置信 (pLDDT<50) 占比 | 30.9% |
| 有序区域 (pLDDT>70) 占比 | 61.3% |
| 可用 PDB 条目 | 4W2R, 5HYN, 5IJ7, 5IJ8, 5LS6, 5WAI, 5WAK, 5WG6, 6B3W, 6C23 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（4W2R, 5HYN, 5IJ7, 5IJ8, 5LS6, 5WAI, 5WAK, 5WG6, 6B3W, 6C23）+ AlphaFold极高置信度预测（pLDDT=71.0），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019135, IPR057540; Pfam: PF09733, PF23320 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EED | 0.999 | 0.997 | — |
| RNF2 | 0.999 | 0.292 | — |
| RBBP7 | 0.999 | 0.970 | — |
| RBBP4 | 0.999 | 0.996 | — |
| EZH2 | 0.999 | 0.999 | — |
| MTF2 | 0.999 | 0.877 | — |
| AEBP2 | 0.999 | 0.991 | — |
| EZH1 | 0.999 | 0.997 | — |
| JARID2 | 0.999 | 0.986 | — |
| PHF19 | 0.998 | 0.985 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Pcl | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:12697833 |
| esc | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:12697833 |
| "E | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:12697833 |
| Caf1-55 | psi-mi:"MI:0071"(molecular sieving) | pubmed:12697833 |
| DNMT3B | psi-mi:"MI:0029"(cosedimentation through density g | pubmed:22094255|imex:IM-16629 |
| SIRT1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:22094255|imex:IM-16629 |
| PML-RAR | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-11934|pubmed:17560333 |
| PML | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-11934|pubmed:17560333 |
| Eed | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12117|pubmed:20064375 |
| Jarid2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12117|pubmed:20064375 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.0 + PDB: 4W2R, 5HYN, 5IJ7, 5IJ8, 5LS6,  | pLDDT=71.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Nucleoli, Nuclear bodies; 额外: Nucleol | 一致 |
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
1. SUZ12 — Polycomb protein SUZ12，研究基础较多，新颖性有限。
2. 蛋白大小739 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 598 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 598 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q15022
- Protein Atlas: https://www.proteinatlas.org/ENSG00000178691-SUZ12/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SUZ12
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q15022
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000178691-SUZ12/subcellular

![](https://images.proteinatlas.org/57436/1005_A7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/57436/1005_A7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/57436/1015_A7_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/57436/1015_A7_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/57436/1043_A4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/57436/1043_A4_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q15022-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
