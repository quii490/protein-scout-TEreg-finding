---
type: protein-evaluation
gene: "TSR2"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TSR2 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | TSR2 / DT1P1A10|RP1-112K5.2|WGG1 |
| 蛋白全称 | Pre-rRNA-processing protein TSR2 homolog |
| 蛋白大小 | 191 aa |
| UniProt ID | Q969E8 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | **16** | Nuclear + cyto, no preference |
| 蛋白大小 | 8/10 | ×1 | **8** | 191 aa，尚可接受 |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed 42 篇，高度新颖 |
| 三维结构 | 6/10 | ×3 | **18** | 无 PDB 结构，仅 AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 2 domain(s), 新颖蛋白基线水平 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+0.0** | None |
|  | **原始总分** |  | **92/183** | **92.0/183** |  |  |  |
|  | **归一化总分** |  | **50.3/100** | **50.3/100** |  |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt |  | 实验证据/预测 |
| GO-CC | GO:0005634 | IEA |


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TSR2/IF_images/A-431_HPA030514_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TSR2/IF_images/U-251MG_HPA030514_2.jpg|U-251MG]]

**结论**: Nuclear + cyto, no preference

#### 3.2 蛋白大小评估

**评价**: 191 aa，尚可接受

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 42 |

**评价**: PubMed 42 篇，高度新颖

**关键文献**:
1. Liu Y & Karlsson S (2024). "Perspectives of current understanding and therapeutics of Diamond-Blackfan anemia". *Leukemia*. PMID: 37973818
2. Adam MP et al. (1993). "DBA Syndrome". **. PMID: 20301769
3. Yang YM et al. (2023). "Chaperone-directed ribosome repair after oxidative damage". *Mol Cell*. PMID: 37086725
4. Yang YM & Karbstein K (2024). "The ubiquitin-proteasome system regulates the formation of specialized ribosomes during high salt stress in yeast". *bioRxiv*. PMID: 39185221
5. Klenotic PA et al. (2013). "Molecular basis of antiangiogenic thrombospondin-1 type 1 repeat domain interactions with CD36". *Arterioscler Thromb Vasc Biol*. PMID: 23640500
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 191 aa |
| PDB 条数 | 0 |
| 已注释结构域 | 2 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TSR2/TSR2-PAE.png]]

**评价**: 无 PDB 结构，仅 AlphaFold 预测，新颖蛋白基线水平

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | Pre-rRNA_process_TSR2 |
| Pfam | WGG |

**染色质调控潜力分析**: 2 domain(s), 新颖蛋白基线水平

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
| 三维结构 | AlphaFold + PDB | 0 条 | 仅预测 |
| 结构域 | UniProt/InterPro/Pfam | 2 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | Partially consistent |

**互证加分明细**:
--
**总计**: +0.0

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 42 篇，高度新颖
2. 核定位: needs confirmation

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 无 PDB 结构，仅 AlphaFold 预测

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 AlphaFold 的突变设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=TSR2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000158526-TSR2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22TSR2%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q969E8
- STRING: https://string-db.org/network/9606.ENSG00000158526
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q969E8


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[TSR2-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TSR2/TSR2-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000158526-TSR2/subcellular

![](https://images.proteinatlas.org/30514/364_B5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/30514/364_B5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/30514/365_B5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/30514/365_B5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/30514/369_B5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/30514/369_B5_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q969E8 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR019398; |
| Pfam | PF10273; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000158526-TSR2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| RPS26 | Intact, Biogrid, Opencell | true |
| CAMK2A | Intact | false |
| DAPL1 | Intact | false |
| DYNC1H1 | Opencell | false |
| EXOSC3 | Intact | false |
| GABARAP | Intact | false |
| GABARAPL2 | Intact | false |
| GAS2L3 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
