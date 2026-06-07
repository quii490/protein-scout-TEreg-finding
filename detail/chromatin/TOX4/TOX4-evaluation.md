---
type: protein-evaluation
gene: "TOX4"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TOX4 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | TOX4 / LCP1 |
| 蛋白全称 | TOX high mobility group box family member 4 |
| 蛋白大小 | 621 aa |
| UniProt ID | O94842 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/chromatin/TOX4/IF_images/PC-3_1.jpg|PC-3]]
![[Projects/TEreg-finding/protein-interested/detail/chromatin/TOX4/IF_images/U2OS_1.jpg|U2OS]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 10/10 | ×1 | **10** | 621 aa，处于理想范围 |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed 27 篇，高度新颖 |
| 三维结构 | 8/10 | ×3 | **24** | 1 个 PDB 结构 + AlphaFold 预测 |
| 调控结构域 | 10/10 | ×2 | **20** | 染色质/DNA 结构域: hmg, hmg_box, hmg_box_2, hmg_box_dom, hmg_box_dom_sf |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+2.0** | UniProt + GO 核定位互证 (+1); PDB + AlphaFold 结构互证 (+0.5); 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **133/183** |  |
| **归一化总分** |  |  | **72.7/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus, Chromosome | 实验证据/预测 |
| GO-CC | N/A | N/A |

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 621 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 27 |

**评价**: PubMed 27 篇，高度新颖

**关键文献**:
1. Wang F et al. (2025). "TOX High-Mobility Group Box Family Member 4 promotes DNA double-strand break repair via nonhomologous end joining". *J Biol Chem*. PMID: 40328361
2. Vanheer L et al. (2019). "Tox4 modulates cell fate reprogramming". *J Cell Sci*. PMID: 31519808
3. Duncalf L et al. (2025). "PNUTS:PP1 recruitment to Tox4 regulates chromosomal dispersal in Drosophila germline development". *Cell Rep*. PMID: 40347473
4. Wang T et al. (2023). "Tox4 regulates transcriptional elongation and reinitiation during murine T cell development". *Commun Biol*. PMID: 37286708
5. Wang L et al. (2022). "TOX4, an insulin receptor-independent regulator of hepatic glucose production, is activated in diabetic liver". *Cell Metab*. PMID: 34914893
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 621 aa |
| PDB 条数 | 1 |
| 已注释结构域 | 6 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/chromatin/TOX4/TOX4-PAE.png]]

**评价**: 1 个 PDB 结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | HMG_box_dom |
| InterPro | HMG_box_dom_sf |
| InterPro | TOX_HMG-box_domain |
| Pfam | HMG_box |
| SMART | HMG |
| PROSITE | HMG_BOX_2 |

**染色质调控潜力分析**: 染色质/DNA 结构域: hmg, hmg_box, hmg_box_2, hmg_box_dom, hmg_box_dom_sf

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

- C:chromatin (GO:0000785, IDA:UniProtKB)
- C:PTW/PP1 phosphatase complex (GO:0072357, IDA:UniProtKB)
- F:chromatin DNA binding (GO:0031490, IBA:GO_Central)

**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 1 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 6 个 | 多库一致 |
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
1. 新颖性: PubMed 27 篇，高度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 1 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=TOX4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000092203-TOX4
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22TOX4%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/O94842
- STRING: https://string-db.org/network/9606.ENSG00000092203
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O94842


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[TOX4-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/chromatin/TOX4/TOX4-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000092203-TOX4/subcellular

![](https://images.proteinatlas.org/17880/115_A1_1_red_green.jpg)
![](https://images.proteinatlas.org/17880/115_A1_2_red_green.jpg)
![](https://images.proteinatlas.org/17880/116_A1_1_red_green.jpg)
![](https://images.proteinatlas.org/17880/116_A1_2_red_green.jpg)
![](https://images.proteinatlas.org/17880/117_A1_1_red_green.jpg)
![](https://images.proteinatlas.org/17880/117_A1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O94842 |
| SMART | SM00398; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR009071;IPR036910;IPR051365; |
| Pfam | PF00505; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000092203-TOX4/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| TBX6 | Intact, Biogrid | true |
| ATXN1 | Intact | false |
| BANP | Intact | false |
| CPSF6 | Opencell | false |
| FUS | Biogrid | false |
| GEMIN6 | Intact | false |
| HSPA4 | Biogrid | false |
| MYL7 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
