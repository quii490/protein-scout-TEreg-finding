---
type: protein-evaluation
gene: "ACACA"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ACACA — REJECTED (研究热度过高 (PubMed strict=568，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ACACA / ACAC, ACC1, ACCA |
| 蛋白名称 | Acetyl-CoA carboxylase 1 |
| 蛋白大小 | 2346 aa / 265.6 kDa |
| UniProt ID | Q13085 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Cytosol; 额外: Nucleoli fibrillar center, Actin filaments; UniProt: Cytoplasm, cytosol |
| 蛋白大小 | 2/10 | ×1 | 2 | 2346 aa / 265.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=568 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=82.8; PDB: 2YL2, 3COJ, 4ASI, 6G2D, 6G2H, 6G2I, 8XKZ |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR049076, IPR049074, IPR034733, IPR013537, IPR011 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **76.0/180** | |
| **归一化总分** | | | **42.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoli fibrillar center, Actin filaments | Supported |
| UniProt | Cytoplasm, cytosol | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- actin cytoskeleton (GO:0015629)
- cytosol (GO:0005829)
- fibrillar center (GO:0001650)
- mitochondrion (GO:0005739)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 568 |
| PubMed broad count | 841 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ACAC, ACC1, ACCA |

**关键文献**:
1. Periplocin suppresses the growth of colorectal cancer cells by triggering LGALS3 (galectin 3)-mediated lysophagy.. *Autophagy*. PMID: 37471054
2. ACACA reduces lipid accumulation through dual regulation of lipid metabolism and mitochondrial function via AMPK- PPARα- CPT1A axis.. *Journal of translational medicine*. PMID: 38395901
3. SQSTM1/p62 activates NFE2L2/NRF2 via ULK1-mediated autophagic KEAP1 degradation and protects mouse liver from lipotoxicity.. *Autophagy*. PMID: 31913745
4. NFIA regulates articular chondrocyte fatty acid metabolism and joint homeostasis.. *Science translational medicine*. PMID: 40737429
5. Muscle-generated BDNF (brain derived neurotrophic factor) maintains mitochondrial quality control in female mice.. *Autophagy*. PMID: 34689722

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.8 |
| 高置信度残基 (pLDDT>90) 占比 | 40.5% |
| 置信残基 (pLDDT 70-90) 占比 | 46.6% |
| 中等置信 (pLDDT 50-70) 占比 | 5.4% |
| 低置信 (pLDDT<50) 占比 | 7.5% |
| 有序区域 (pLDDT>70) 占比 | 87.1% |
| 可用 PDB 条目 | 2YL2, 3COJ, 4ASI, 6G2D, 6G2H, 6G2I, 8XKZ, 8XL0, 8XL1, 8XL2 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2YL2, 3COJ, 4ASI, 6G2D, 6G2H, 6G2I, 8XKZ, 8XL0, 8XL1, 8XL2）+ AlphaFold极高置信度预测（pLDDT=82.8），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR049076, IPR049074, IPR034733, IPR013537, IPR011761; Pfam: PF08326, PF21385, PF02785 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FASN | 0.998 | 0.073 | — |
| BRCA1 | 0.995 | 0.986 | — |
| ACLY | 0.986 | 0.000 | — |
| PRKAA1 | 0.981 | 0.473 | — |
| SREBF1 | 0.981 | 0.000 | — |
| MCAT | 0.975 | 0.000 | — |
| ACSS2 | 0.970 | 0.069 | — |
| MLYCD | 0.966 | 0.000 | — |
| ACACB | 0.966 | 0.459 | — |
| ACAT1 | 0.962 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CHGB | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| ATXN1 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| MCC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ILK | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MYC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| BRCA1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-14410|pubmed:16326698 |
| CIAO1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| Rpgrip1l | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| GABARAP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| OPG044 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:22810585|imex:IM-17331 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.8 + PDB: 2YL2, 3COJ, 4ASI, 6G2D, 6G2H,  | pLDDT=82.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol / Cytosol; 额外: Nucleoli fibrillar center, Actin fila | 一致 |
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
1. ACACA — Acetyl-CoA carboxylase 1，研究基础较多，新颖性有限。
2. 蛋白大小2346 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 568 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 568 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13085
- Protein Atlas: https://www.proteinatlas.org/ENSG00000278540-ACACA/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ACACA
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13085
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000278540-ACACA/subcellular

![](https://images.proteinatlas.org/36650/752_C2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/36650/752_C2_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/36650/847_E2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/36650/847_E2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/36650/857_E2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/36650/857_E2_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q13085-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q13085 |
| SMART | SM00878; |
| UniProt Domain [FT] | DOMAIN 117..618; /note="Biotin carboxylation"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00969"; DOMAIN 275..466; /note="ATP-grasp"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00409"; DOMAIN 745..819; /note="Biotinyl-binding"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01066"; DOMAIN 1576..1914; /note="CoA carboxyltransferase N-terminal"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01136"; DOMAIN 1918..2234; /note="CoA carboxyltransferase C-terminal"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01137" |
| InterPro | IPR049076;IPR049074;IPR034733;IPR013537;IPR011761;IPR013815;IPR005481;IPR001882;IPR011764;IPR005482;IPR000089;IPR029045;IPR011763;IPR011762;IPR005479;IPR016185;IPR011054;IPR011053; |
| Pfam | PF08326;PF21385;PF02785;PF00289;PF00364;PF01039;PF02786; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000278540-ACACA/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AKR1B10 | Intact, Biogrid | true |
| BRCA1 | Intact, Biogrid | true |
| MYC | Intact, Biogrid | true |
| SIRT1 | Intact, Biogrid | true |
| ACACB | Biogrid | false |
| CCNF | Biogrid | false |
| CD274 | Biogrid | false |
| COP1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
