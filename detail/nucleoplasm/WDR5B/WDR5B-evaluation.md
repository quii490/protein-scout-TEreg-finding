---
type: protein-evaluation
gene: "WDR5B"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## WDR5B 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | WDR5B / FLJ11287 |
| 蛋白全称 | WD repeat-containing protein 5B |
| 蛋白大小 | 330 aa |
| UniProt ID | Q86VZ2 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 10/10 | ×1 | **10** | 330 aa，处于理想范围 |
| 研究新颖性 | 10/10 | ×5 | **50** | PubMed 2 篇，极度新颖 |
| 三维结构 | 6/10 | ×3 | **18** | 无 PDB 结构，仅 AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 11 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+1.5** | UniProt + GO 核定位互证 (+1); 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **131/183** |  |
| **归一化总分** |  |  | **71.6/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus | 实验证据/预测 |
| GO-CC | N/A | N/A |


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/WDR5B/IF_images/HaCaT_HPA076612_1.jpg|HaCaT]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/WDR5B/IF_images/MCF-7_HPA076612_2.jpg|MCF-7]]

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 330 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 2 |

**评价**: PubMed 2 篇，极度新颖

**关键文献**:
1. Bailey JK et al. (2024). "Initial Characterization of WDR5B Reveals a Role in the Proliferation of Retinal Pigment Epithelial Cells". *Cells*. PMID: 39056772
2. Wang X et al. (2021). "Association between structural brain features and gene expression by weighted gene co-expression network analysis in conversion from MCI to AD". *Behav Brain Res*. PMID: 33940051
3. Chang Z et al. (2019). "Identification of Prognostic Dosage-Sensitive Genes in Colorectal Cancer Based on Multi-Omics". *Front Genet*. PMID: 31998369
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 330 aa |
| PDB 条数 | 0 |
| 已注释结构域 | 11 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/WDR5B/WDR5B-PAE.png]]

**评价**: 无 PDB 结构，仅 AlphaFold 预测，新颖蛋白基线水平

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | Beta-prop_WDR5-like |
| InterPro | WD40/YVTN_repeat-like_dom_sf |
| InterPro | WD40_PAC1 |
| InterPro | WD40_repeat_CS |
| InterPro | WD40_repeat_dom_sf |
| InterPro | WD40_rpt |
| Pfam | Beta-prop_WDR5 |
| SMART | WD40 |
| PROSITE | WD_REPEATS_1 |
| PROSITE | WD_REPEATS_2 |
| PROSITE | WD_REPEATS_REGION |

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

- C:Set1C/COMPASS complex (GO:0048188, IBA:GO_Central)

**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 0 条 | 仅预测 |
| 结构域 | UniProt/InterPro/Pfam | 11 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
UniProt + GO 核定位互证 (+1)
多库结构域一致 (+0.5)
**总计**: +1.5

### 4. 总体评价

**推荐等级**: ****o (4/5)

**核心优势**:
1. 新颖性: PubMed 2 篇，极度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 无 PDB 结构，仅 AlphaFold 预测

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 AlphaFold 的突变设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=WDR5B
- Protein Atlas: https://www.proteinatlas.org/ENSG00000196981-WDR5B
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22WDR5B%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q86VZ2
- STRING: https://string-db.org/network/9606.ENSG00000196981
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86VZ2


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[WDR5B-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/WDR5B/WDR5B-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000196981-WDR5B/subcellular

![](https://images.proteinatlas.org/76612/1913_G17_1_red_green.jpg)
![](https://images.proteinatlas.org/76612/1913_G17_2_red_green.jpg)
![](https://images.proteinatlas.org/76612/2103_E5_2_red_green.jpg)
![](https://images.proteinatlas.org/76612/2103_E5_3_red_green.jpg)
![](https://images.proteinatlas.org/76612/2162_H2_1_red_green.jpg)
![](https://images.proteinatlas.org/76612/2162_H2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q86VZ2 |
| SMART | SM00320; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR059122;IPR015943;IPR020472;IPR019775;IPR036322;IPR001680; |
| Pfam | PF25175; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000196981-WDR5B/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CCT2 | Biogrid, Bioplex | true |
| WDR5 | Biogrid, Bioplex | true |
| HSPA8 | Bioplex | false |
| PI4K2B | Bioplex | false |
| RPIA | Bioplex | false |
| TMEM263 | Bioplex | false |
| TRIM65 | Bioplex | false |
| TUBA1A | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
