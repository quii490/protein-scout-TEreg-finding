---
type: protein-evaluation
gene: "SCMH1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SCMH1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | SCMH1 / Scml3 |
| 蛋白全称 | Polycomb protein SCMH1 |
| 蛋白大小 | 660 aa |
| UniProt ID | Q96GD3 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 10/10 | ×1 | **10** | 660 aa，处于理想范围 |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed 35 篇，高度新颖 |
| 三维结构 | 8/10 | ×3 | **24** | 1 个 PDB 结构 + AlphaFold 预测 |
| 调控结构域 | 10/10 | ×2 | **20** | 染色质/DNA 结构域: mbt, mbt_scmh1_rpt1, mbt_scmh1_rpt2, pcg_chromatin_remod_ |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+2.0** | UniProt + GO 核定位互证 (+1); PDB + AlphaFold 结构互证 (+0.5); 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **133/183** |  |
| **归一化总分** |  |  | **72.7/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

> **IF 图像**: 暂无数据。

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus | 实验证据/预测 |
| GO-CC | GO:0005634 | IDA|IEA |


> **Protein Atlas IF**: 暂无HPA数据，核定位基于UniProt+GO


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/SCMH1/IF_images/Hep-G2_HPA048898_1.jpg|Hep-G2]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/SCMH1/IF_images/U-251MG_HPA048898_2.jpg|U-251MG]]

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 660 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 35 |

**评价**: PubMed 35 篇，高度新颖


**关键文献**:
1. Li B et al. (2023). "FTO-dependent m(6)A modification of Plpp3 in circSCMH1-regulated vascular repair and functional recovery following stroke". *Nat Commun*. PMID: 36717587
2. Jia Y et al. (2025). "Nose-to-Brain Delivery of Circular RNA SCMH1-Loaded Lipid Nanoparticles for Ischemic Stroke Therapy". *Adv Mater*. PMID: 40143778
3. Wang Y et al. (2024). "Circular RNA SCMH1 suppresses KMO expression to inhibit mitophagy and promote functional recovery following stroke". *Theranostics*. PMID: 39659575
4. Yang L et al. (2020). "Extracellular Vesicle-Mediated Delivery of Circular RNA SCMH1 Promotes Functional Recovery in Rodent and Nonhuman Primate Ischemic Stroke Models". *Circulation*. PMID: 32441115
5. Zhang X et al. (2023). "Circular RNA as biomarkers for acute ischemic stroke: A systematic review and meta-analysis". *CNS Neurosci Ther*. PMID: 37186176

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 660 aa |
| PDB 条数 | 1 |
| 已注释结构域 | 18 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/SCMH1/SCMH1-PAE.png]]

**评价**: 1 个 PDB 结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | Mbt |
| InterPro | MBT_SCMH1_rpt1 |
| InterPro | MBT_SCMH1_rpt2 |
| InterPro | PcG_chromatin_remod_factors |
| InterPro | SAM |
| InterPro | SAM/pointed_sf |
| InterPro | SAM_Scm-like |
| InterPro | SCML2_RBR |
| InterPro | SLED |
| InterPro | SLED_sf |
| Pfam | MBT |
| Pfam | RBR |
| Pfam | SAM_1 |
| Pfam | SLED |
| SMART | MBT |

**染色质调控潜力分析**: 染色质/DNA 结构域: mbt, mbt_scmh1_rpt1, mbt_scmh1_rpt2, pcg_chromatin_remod_factors

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

- F:chromatin binding (GO:0003682, IBA:GO_Central)
- P:heterochromatin formation (GO:0031507, ISS:UniProtKB)

**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 1 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 18 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
UniProt + GO 核定位互证 (+1)
PDB + AlphaFold 结构互证 (+0.5)
多库结构域一致 (+0.5)
**总计**: +2.0

### 4. 总体评价

**推荐等级**: ****o (4/5)

**核心优势**:
1. 新颖性: PubMed 35 篇，高度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 1 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=SCMH1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000010803-SCMH1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SCMH1%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q96GD3
- STRING: https://string-db.org/network/9606.ENSG00000010803
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96GD3


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[SCMH1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/SCMH1/SCMH1-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000010803-SCMH1/subcellular

![](https://images.proteinatlas.org/48898/739_H10_1_red_green.jpg)
![](https://images.proteinatlas.org/48898/739_H10_2_red_green.jpg)
![](https://images.proteinatlas.org/48898/751_D6_1_red_green.jpg)
![](https://images.proteinatlas.org/48898/751_D6_2_red_green.jpg)
![](https://images.proteinatlas.org/48898/753_H10_1_red_green.jpg)
![](https://images.proteinatlas.org/48898/753_H10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96GD3 |
| SMART | SM00561;SM00454; |
| UniProt Domain [FT] | DOMAIN 593..658; /note="SAM"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00184" |
| InterPro | IPR004092;IPR047279;IPR047280;IPR050548;IPR001660;IPR013761;IPR047531;IPR033763;IPR021987;IPR038348; |
| Pfam | PF02820;PF17208;PF00536;PF12140; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000010803-SCMH1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PHC2 | Intact, Biogrid | true |
| BMI1 | Biogrid | false |
| CBX4 | Biogrid | false |
| CBX6 | Biogrid | false |
| HPCAL4 | Intact | false |
| MAGEA12 | Intact | false |
| PCGF2 | Biogrid | false |
| PHC1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
