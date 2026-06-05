---
type: protein-evaluation
gene: "DCAF1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DCAF1 — REJECTED (研究热度过高 (PubMed strict=146，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DCAF1 / KIAA0800, RIP, VPRBP |
| 蛋白名称 | DDB1- and CUL4-associated factor 1 |
| 蛋白大小 | 1507 aa / 169.0 kDa |
| UniProt ID | Q9Y4B6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nucleoli fibrillar center; UniProt: Cytoplasm; Nucleus; Cytoplasm, cytoskeleton, microtubule org |
| 蛋白大小 | 5/10 | ×1 | 5 | 1507 aa / 169.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=146 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=74.9; PDB: 3WA0, 4CC9, 4P7I, 4PXW, 4Z8L, 5AJA, 5JK7 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011989, IPR016024, IPR006594, IPR033270, IPR015 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **89.0/180** | |
| **归一化总分** | | | **49.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli fibrillar center | Supported |
| UniProt | Cytoplasm; Nucleus; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centrosome (GO:0005813)
- Cul4-RING E3 ubiquitin ligase complex (GO:0080008)
- cytoplasm (GO:0005737)
- fibrillar center (GO:0001650)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 146 |
| PubMed broad count | 218 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0800, RIP, VPRBP |

**关键文献**:
1. DCAF1-based PROTACs with activity against clinically validated targets overcoming intrinsic- and acquired-degrader resistance.. *Nature communications*. PMID: 38177131
2. STK39 inhibits antiviral immune response by inhibiting DCAF1-mediated PP2A degradation.. *Acta pharmaceutica Sinica. B*. PMID: 40370558
3. CRL4-DCAF1 Ubiquitin Ligase Dependent Functions of HIV Viral Protein R and Viral Protein X.. *Viruses*. PMID: 39205287
4. Discovery of Nanomolar DCAF1 Small Molecule Ligands.. *Journal of medicinal chemistry*. PMID: 36948210
5. CRL4(DCAF1) ubiquitin ligase regulates PLK4 protein levels to prevent premature centriole duplication.. *Life science alliance*. PMID: 38490717

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.9 |
| 高置信度残基 (pLDDT>90) 占比 | 44.6% |
| 置信残基 (pLDDT 70-90) 占比 | 25.7% |
| 中等置信 (pLDDT 50-70) 占比 | 5.0% |
| 低置信 (pLDDT<50) 占比 | 24.7% |
| 有序区域 (pLDDT>70) 占比 | 70.3% |
| 可用 PDB 条目 | 3WA0, 4CC9, 4P7I, 4PXW, 4Z8L, 5AJA, 5JK7, 6N45, 6ZUE, 6ZX9 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（3WA0, 4CC9, 4P7I, 4PXW, 4Z8L, 5AJA, 5JK7, 6N45, 6ZUE, 6ZX9）+ AlphaFold极高置信度预测（pLDDT=74.9），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011989, IPR016024, IPR006594, IPR033270, IPR015943 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CUL4A | 0.999 | 0.989 | — |
| CUL4B | 0.999 | 0.828 | — |
| RBX1 | 0.999 | 0.966 | — |
| DDB1 | 0.999 | 0.992 | — |
| DTL | 0.996 | 0.000 | — |
| SAMHD1 | 0.995 | 0.971 | — |
| DDA1 | 0.995 | 0.834 | — |
| UNG | 0.979 | 0.960 | — |
| DDB2 | 0.967 | 0.000 | — |
| NF2 | 0.956 | 0.827 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Rpgrip1l | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| COPS5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:18850735|imex:IM-20477 |
| SLX4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12200|pubmed:19596235 |
| vpr | psi-mi:"MI:0096"(pull down) | imex:IM-17346|pubmed:22190034| |
| UBXN7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |
| DDB1A | psi-mi:"MI:0018"(two hybrid) | pubmed:18552200|imex:IM-20346 |
| CUL4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:18552200|imex:IM-20346 |
| COPS6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| DDA1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| Cep78 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.9 + PDB: 3WA0, 4CC9, 4P7I, 4PXW, 4Z8L,  | pLDDT=74.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Cytoplasm, cytoskeleton, micro / Nucleoplasm; 额外: Nucleoli fibrillar center | 一致 |
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
1. DCAF1 — DDB1- and CUL4-associated factor 1，研究基础较多，新颖性有限。
2. 蛋白大小1507 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 146 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 146 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y4B6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000145041-DCAF1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DCAF1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y4B6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000145041-DCAF1/subcellular

![](https://images.proteinatlas.org/52445/782_H8_2_red_green.jpg)
![](https://images.proteinatlas.org/52445/782_H8_3_red_green.jpg)
![](https://images.proteinatlas.org/52445/787_H8_1_red_green.jpg)
![](https://images.proteinatlas.org/52445/787_H8_3_red_green.jpg)
![](https://images.proteinatlas.org/52445/915_H4_2_red_green.jpg)
![](https://images.proteinatlas.org/52445/915_H4_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y4B6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
