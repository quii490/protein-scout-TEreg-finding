---
type: protein-evaluation
gene: "MKNK2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MKNK2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MKNK2 / GPRK7, MNK2 |
| 蛋白名称 | MAP kinase-interacting serine/threonine-protein kinase 2 |
| 蛋白大小 | 465 aa / 51.9 kDa |
| UniProt ID | Q9HBH9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear bodies; 额外: Nucleoplasm, Cytosol; UniProt: Nucleus, PML body; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 465 aa / 51.9 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=60 篇 (≤60→6) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=71.0; PDB: 2AC3, 2AC5, 2HW7, 6CJ5, 6CJE, 6CJH, 6CJW |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR050205, IPR011009, IPR000719, IPR017441, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **124.0/180** | |
| **归一化总分** | | | **68.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies; 额外: Nucleoplasm, Cytosol | Supported |
| UniProt | Nucleus, PML body; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- PML body (GO:0016605)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 60 |
| PubMed broad count | 193 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GPRK7, MNK2 |

**关键文献**:
1. Human umbilical cord-derived mesenchymal stem cells not only ameliorate blood glucose but also protect vascular endothelium from diabetic damage through a paracrine mechanism mediated by MAPK/ERK signaling.. *Stem cell research & therapy*. PMID: 35715841
2. Study on MKNK2 as a potential prognostic and immunological biomarker in pan-cancer.. *European review for medical and pharmacological sciences*. PMID: 39624012
3. MiR-125b targeted regulation of MKNK2 inhibits multiple myeloma proliferation and invasion.. *American journal of translational research*. PMID: 39114709
4. The role and mechanisms of the microRNA-1180-3p/MKNK2/CREB3 signaling axis in tumor progression following insufficient radiofrequency ablation of colorectal cancer liver metastasis.. *Biochemical pharmacology*. PMID: 40784570
5. Identification of the human Mnk2 gene (MKNK2) through protein interaction with estrogen receptor beta.. *Genomics*. PMID: 11013076

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.0 |
| 高置信度残基 (pLDDT>90) 占比 | 38.7% |
| 置信残基 (pLDDT 70-90) 占比 | 24.1% |
| 中等置信 (pLDDT 50-70) 占比 | 6.5% |
| 低置信 (pLDDT<50) 占比 | 30.8% |
| 有序区域 (pLDDT>70) 占比 | 62.8% |
| 可用 PDB 条目 | 2AC3, 2AC5, 2HW7, 6CJ5, 6CJE, 6CJH, 6CJW, 6CJY, 6CK3, 6CK6 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2AC3, 2AC5, 2HW7, 6CJ5, 6CJE, 6CJH, 6CJW, 6CJY, 6CK3, 6CK6）+ AlphaFold极高置信度预测（pLDDT=71.0），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050205, IPR011009, IPR000719, IPR017441, IPR008271; Pfam: PF00069 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MAPK1 | 0.983 | 0.790 | — |
| MKNK1 | 0.945 | 0.443 | — |
| MAPK3 | 0.937 | 0.210 | — |
| EIF4E1B | 0.912 | 0.130 | — |
| ATF4 | 0.910 | 0.000 | — |
| EIF4E2 | 0.906 | 0.000 | — |
| MAPK14 | 0.862 | 0.833 | — |
| EIF4G1 | 0.855 | 0.292 | — |
| EIF4E | 0.803 | 0.130 | — |
| ATP7A | 0.796 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000250896.3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| Traf2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Mapk1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| MAPK8 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| Csf1 | psi-mi:"MI:0096"(pull down) | pubmed:16267818|imex:IM-16654 |
| MAPK14 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| RPL7A | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| syd | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| SRPK1 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:23602568|imex:IM-17935 |
| MESD | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 3 / 15 = 20%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 20%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.0 + PDB: 2AC3, 2AC5, 2HW7, 6CJ5, 6CJE,  | pLDDT=71.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus, PML body; Cytoplasm / Nuclear bodies; 额外: Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. MKNK2 — MAP kinase-interacting serine/threonine-protein kinase 2，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小465 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 60 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9HBH9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000099875-MKNK2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MKNK2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9HBH9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (supported)。来源: https://www.proteinatlas.org/ENSG00000099875-MKNK2/subcellular

![](https://images.proteinatlas.org/70499/1647_B4_31_red_green.jpg)
![](https://images.proteinatlas.org/70499/1647_B4_33_red_green.jpg)
![](https://images.proteinatlas.org/70499/1653_B2_5_red_green.jpg)
![](https://images.proteinatlas.org/70499/1653_B2_6_red_green.jpg)
![](https://images.proteinatlas.org/70499/1684_H6_1_red_green.jpg)
![](https://images.proteinatlas.org/70499/1684_H6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9HBH9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9HBH9 |
| SMART | SM00220; |
| UniProt Domain [FT] | DOMAIN 84..388; /note="Protein kinase"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00159" |
| InterPro | IPR050205;IPR011009;IPR000719;IPR017441;IPR008271; |
| Pfam | PF00069; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000099875-MKNK2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| MAPK14 | Intact, Biogrid | true |
| EIF4G1 | Biogrid | false |
| GAPDH | Opencell | false |
| MAPK1 | Biogrid | false |
| VHL | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
