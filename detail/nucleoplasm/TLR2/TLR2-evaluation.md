---
type: protein-evaluation
gene: "TLR2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TLR2 — REJECTED (研究热度过高 (PubMed strict=7577，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TLR2 / TIL4 |
| 蛋白名称 | Toll-like receptor 2 |
| 蛋白大小 | 784 aa / 89.8 kDa |
| UniProt ID | O60603 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane; 额外: Nucleoplasm, Vesicles, Cytosol; UniProt: Membrane; Cytoplasmic vesicle, phagosome membrane; Membrane  |
| 蛋白大小 | 10/10 | ×1 | 10 | 784 aa / 89.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=7577 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=87.9; PDB: 1FYW, 1FYX, 1O77, 2Z7X, 2Z80, 6NIG, 8AR0 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000483, IPR001611, IPR003591, IPR032675, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane; 额外: Nucleoplasm, Vesicles, Cytosol | Supported |
| UniProt | Membrane; Cytoplasmic vesicle, phagosome membrane; Membrane raft | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cell surface (GO:0009986)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- Golgi apparatus (GO:0005794)
- membrane raft (GO:0045121)
- nucleoplasm (GO:0005654)
- phagocytic vesicle membrane (GO:0030670)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7577 |
| PubMed broad count | 16195 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TIL4 |

**关键文献**:
1. The PLAUR signaling promotes chronic pruritus.. *FASEB journal : official publication of the Federation of American Societies for Experimental Biology*. PMID: 35596683
2. Employing single-cell RNA sequencing coupled with an array of bioinformatics approaches to ascertain the shared genetic characteristics between osteoporosis and obesity.. *Bone & joint research*. PMID: 39412449
3. Protein Expression of TLR2, TLR4, and TLR9 on Monocytes in TB, HIV, and TB/HIV.. *Journal of immunology research*. PMID: 38660059
4. Myristoylated rhinovirus VP4 protein activates TLR2-dependent proinflammatory gene expression.. *American journal of physiology. Lung cellular and molecular physiology*. PMID: 30908938
5. The Spike protein of SARS-CoV-2 signals via Tlr2 in zebrafish.. *Developmental and comparative immunology*. PMID: 36587712

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.9 |
| 高置信度残基 (pLDDT>90) 占比 | 63.1% |
| 置信残基 (pLDDT 70-90) 占比 | 25.4% |
| 中等置信 (pLDDT 50-70) 占比 | 8.7% |
| 低置信 (pLDDT<50) 占比 | 2.8% |
| 有序区域 (pLDDT>70) 占比 | 88.5% |
| 可用 PDB 条目 | 1FYW, 1FYX, 1O77, 2Z7X, 2Z80, 6NIG, 8AR0 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1FYW, 1FYX, 1O77, 2Z7X, 2Z80, 6NIG, 8AR0）+ AlphaFold极高置信度预测（pLDDT=87.9），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000483, IPR001611, IPR003591, IPR032675, IPR000157; Pfam: PF00560, PF13855, PF01463 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TLR6 | 0.999 | 0.576 | — |
| TLR1 | 0.999 | 0.952 | — |
| TIRAP | 0.999 | 0.450 | — |
| MYD88 | 0.999 | 0.746 | — |
| TLR4 | 0.999 | 0.000 | — |
| HSPA1B | 0.998 | 0.102 | — |
| CLEC7A | 0.998 | 0.294 | — |
| HMGB1 | 0.998 | 0.297 | — |
| CD36 | 0.998 | 0.000 | — |
| TOLLIP | 0.997 | 0.292 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000519704.1 | psi-mi:"MI:0370"(tox-r dimerization assay) | imex:IM-26356|pubmed:23155421 |
| TLR6 | psi-mi:"MI:0370"(tox-r dimerization assay) | imex:IM-26356|pubmed:23155421 |
| TLR1 | psi-mi:"MI:0370"(tox-r dimerization assay) | imex:IM-26356|pubmed:23155421 |
| MYD88 | psi-mi:"MI:0663"(confocal microscopy) | imex:IM-14480|pubmed:16293622 |
| SIGLEC5 | psi-mi:"MI:0411"(enzyme linked immunosorbent assay | pubmed:25187624|imex:IM-26349 |
| SIGLEC9 | psi-mi:"MI:0411"(enzyme linked immunosorbent assay | pubmed:25187624|imex:IM-26349 |
| Cd22 | psi-mi:"MI:0411"(enzyme linked immunosorbent assay | pubmed:25187624|imex:IM-26349 |
| Cd33 | psi-mi:"MI:0411"(enzyme linked immunosorbent assay | pubmed:25187624|imex:IM-26349 |
| Siglech | psi-mi:"MI:0411"(enzyme linked immunosorbent assay | pubmed:25187624|imex:IM-26349 |
| Siglece | psi-mi:"MI:0411"(enzyme linked immunosorbent assay | pubmed:25187624|imex:IM-26349 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.9 + PDB: 1FYW, 1FYX, 1O77, 2Z7X, 2Z80,  | pLDDT=87.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Membrane; Cytoplasmic vesicle, phagosome membrane; / Plasma membrane; 额外: Nucleoplasm, Vesicles, Cytoso | 一致 |
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
1. TLR2 — Toll-like receptor 2，研究基础较多，新颖性有限。
2. 蛋白大小784 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 7577 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 7577 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O60603
- Protein Atlas: https://www.proteinatlas.org/ENSG00000137462-TLR2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TLR2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O60603
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (supported)。来源: https://www.proteinatlas.org/ENSG00000137462-TLR2/subcellular

![](https://images.proteinatlas.org/78321/2108_E4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/78321/2108_E4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/78321/2130_H10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/78321/2130_H10_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/78321/2214_A3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/78321/2214_A3_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O60603-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O60603 |
| SMART | SM00364;SM00369;SM00082;SM00255; |
| UniProt Domain [FT] | DOMAIN 525..579; /note="LRRCT"; DOMAIN 639..782; /note="TIR"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00204" |
| InterPro | IPR000483;IPR001611;IPR003591;IPR032675;IPR000157;IPR017241;IPR035897; |
| Pfam | PF00560;PF13855;PF01463;PF01582; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000137462-TLR2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| EGFR | Intact, Biogrid | true |
| ANXA2 | Biogrid | false |
| ATG16L1 | Biogrid | false |
| CXCR4 | Intact | false |
| MYD88 | Intact | false |
| TIRAP | Biogrid | false |
| TLR1 | Intact | false |
| TLR10 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
