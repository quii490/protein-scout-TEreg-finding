---
type: protein-evaluation
gene: "TESC"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TESC 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | TESC / TSC|FLJ20607|CHP3 |
| 蛋白全称 | Calcineurin B homologous protein 3 |
| 蛋白大小 | 214 aa |
| UniProt ID | Q96BS2 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/TESC/IF_images/HEK293_1.jpg|HEK293]]
![[Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/TESC/IF_images/A-549_1.jpg|A-549]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | **16** | Nuclear + cyto, no preference |
| 蛋白大小 | 10/10 | ×1 | **10** | 214 aa，处于理想范围 |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed 64 篇，中等研究热度 |
| 三维结构 | 6/10 | ×3 | **18** | 无 PDB 结构，仅 AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 7 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+0.5** | 多库结构域一致 (+0.5) |
|  | **原始总分** |  | **84.5/183** | **84.0/183** |  |  |
|  | **归一化总分** |  | **46.2/100** | **45.9/100** |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus, Cytoplasm, Membrane, Cell membrane, Cell projection, lamellipodium, Cell projection, ruffle membrane | 实验证据/预测 |
| GO-CC | GO:0005634 | IEA |

**结论**: Nuclear + cyto, no preference

#### 3.2 蛋白大小评估

**评价**: 214 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 64 |

**关键文献**:
1. Shichkin et al. (2020). "Thymus Regeneration and Future Challenges.". *Stem Cell Rev Rep*. PMID: 31997162
2. Lee et al. (2018). "Tescalcin/c-Src/IGF1Rβ-mediated STAT3 activation enhances cancer stemness and radioresistant properties through ALDH1.". *Sci Rep*. PMID: 30013043
3. Wu et al. (2024). "Tescalcin modulates bone marrow-derived mesenchymal stem cells osteogenic differentiation via the Wnt/β-catenin signaling pathway.". *Environ Toxicol*. PMID: 38124301
4. Zou et al. (2022). "Tescalcin promotes highly invasive papillary thyroid microcarcinoma by regulating FOS/ERK signaling pathway.". *BMC Cancer*. PMID: 35641944
5. Bao et al. (2009). "Expression and evolutionary conservation of the tescalcin gene during development.". *Gene Expr Patterns*. PMID: 19345287
**评价**: PubMed 64 篇，中等研究热度

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 214 aa |
| PDB 条数 | 0 |
| 已注释结构域 | 7 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/TESC/TESC-PAE.png]]

**评价**: 无 PDB 结构，仅 AlphaFold 预测，新颖蛋白基线水平

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | CHP3 |
| InterPro | EF-hand-dom_pair |
| InterPro | EF_Hand_1_Ca_BS |
| InterPro | EF_hand_dom |
| SMART | EFh |
| PROSITE | EF_HAND_1 |
| PROSITE | EF_HAND_2 |

**染色质调控潜力分析**: 7 个已注释结构域，新颖蛋白基线水平

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


**PPI 互证分析**:
- （待补充：综合 STRING、IntAct 和 GO 数据库的互作信息，分析 PPI 网络的一致性）
**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 0 条 | 仅预测 |
| 结构域 | UniProt/InterPro/Pfam | 7 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | Partially consistent |

**互证加分明细**:
多库结构域一致 (+0.5)
**总计**: +0.5

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 64 篇，中等研究热度
2. 核定位: needs confirmation

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 无 PDB 结构，仅 AlphaFold 预测

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 AlphaFold 的突变设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=TESC
- Protein Atlas: https://www.proteinatlas.org/ENSG00000088992-TESC
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22TESC%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q96BS2
- STRING: https://string-db.org/network/9606.ENSG00000088992
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96BS2


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[TESC-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/TESC/TESC-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000088992-TESC/subcellular

![](https://images.proteinatlas.org/53200/806_D1_1_red_green.jpg)
![](https://images.proteinatlas.org/53200/806_D1_2_red_green.jpg)
![](https://images.proteinatlas.org/53200/810_D1_1_red_green.jpg)
![](https://images.proteinatlas.org/53200/810_D1_2_red_green.jpg)
![](https://images.proteinatlas.org/53200/864_E12_1_red_green.jpg)
![](https://images.proteinatlas.org/53200/864_E12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96BS2 |
| SMART | SM00054; |
| UniProt Domain [FT] | DOMAIN 110..145; /note="EF-hand"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00448" |
| InterPro | IPR052490;IPR011992;IPR018247;IPR002048; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000088992-TESC/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| HMG20A | Intact, Biogrid | true |
| SLC9A1 | Intact, Biogrid | true |
| INSL4 | Bioplex | false |
| WBP11 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
