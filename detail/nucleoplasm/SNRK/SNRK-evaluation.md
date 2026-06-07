---
type: protein-evaluation
gene: "SNRK"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SNRK 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | SNRK / FLJ20224|HSNFRK|KIAA0096 |
| 蛋白全称 | SNF-related serine/threonine-protein kinase |
| 蛋白大小 | 765 aa |
| UniProt ID | Q9NRH2 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 10/10 | ×1 | **10** | 765 aa，处于理想范围 |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed 44 篇，高度新颖 |
| 三维结构 | 8/10 | ×3 | **24** | 1 个 PDB 结构 + AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 11 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+2.0** | UniProt + GO 核定位互证 (+1); PDB + AlphaFold 结构互证 (+0.5); 多库结构域一致 (+0.5) |
|  | **原始总分** |  | **117/183** | **116.0/183** |  |  |  |
|  | **归一化总分** |  | **63.9/100** | **63.4/100** |  |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus | 实验证据/预测 |
| GO-CC | N/A | N/A |


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/SNRK/IF_images/A-431_HPA042163_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/SNRK/IF_images/U-251MG_HPA042163_2.jpg|U-251MG]]

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 765 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 44 |

**评价**: PubMed 44 篇，高度新颖

**关键文献**:
1. Stanczyk PJ et al. (2023). "DNA Damage and Nuclear Morphological Changes in Cardiac Hypertrophy Are Mediated by SNRK Through Actin Depolymerization". *Circulation*. PMID: 37721051
2. Lin S et al. (2025). "SNRK modulates mTOR-autophagy pathway for liver lipid homeostasis in MAFLD". *Mol Ther*. PMID: 39521960
3. Wang ZY et al. (2022). "Negative feedback of SNRK to circ-SNRK regulates cardiac function post-myocardial infarction". *Cell Death Differ*. PMID: 34621049
4. Thirugnanam K et al. (2024). "SNRK regulates TGFβ levels in atria to control cardiac fibrosis". *bioRxiv*. PMID: 39386731
5. Xu X et al. (2025). "Identification of m(6)A-related biomarkers in Kawasaki disease". *Biochim Biophys Acta Mol Basis Dis*. PMID: 39988181
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 765 aa |
| PDB 条数 | 1 |
| 已注释结构域 | 11 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/SNRK/SNRK-PAE.png]]

**评价**: 1 个 PDB 结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | Kinase-like_dom_sf |
| InterPro | Prot_kinase_dom |
| InterPro | Protein_kinase_ATP_BS |
| InterPro | Ser/Thr_kinase_AS |
| InterPro | UBA |
| Pfam | Pkinase |
| SMART | S_TKc |
| PROSITE | PROTEIN_KINASE_ATP |
| PROSITE | PROTEIN_KINASE_DOM |
| PROSITE | PROTEIN_KINASE_ST |
| PROSITE | UBA |

**染色质调控潜力分析**: 11 个已注释结构域，新颖蛋白基线水平

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

--

**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 1 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 11 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
UniProt + GO 核定位互证 (+1)
PDB + AlphaFold 结构互证 (+0.5)
多库结构域一致 (+0.5)
**总计**: +2.0

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 44 篇，高度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 1 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=SNRK
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163788-SNRK
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SNRK%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q9NRH2
- STRING: https://string-db.org/network/9606.ENSG00000163788
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NRH2


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[SNRK-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/SNRK/SNRK-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (approved)。来源: https://www.proteinatlas.org/ENSG00000163788-SNRK/subcellular

![](https://images.proteinatlas.org/42163/418_F3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/42163/418_F3_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/42163/424_F3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/42163/424_F3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/42163/429_F3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/42163/429_F3_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NRH2 |
| SMART | SM00220; |
| UniProt Domain [FT] | DOMAIN 16..269; /note="Protein kinase"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00159"; DOMAIN 291..334; /note="UBA"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00212" |
| InterPro | IPR011009;IPR000719;IPR017441;IPR008271;IPR015940; |
| Pfam | PF00069; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000163788-SNRK/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CAMK2A | Biogrid, Bioplex | true |
| HSP90AB1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
