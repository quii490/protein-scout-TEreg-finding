---
type: protein-evaluation
gene: "PRR7"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PRR7 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | PRR7 / MGC10772 |
| 蛋白全称 | Proline-rich protein 7 |
| 蛋白大小 | 274 aa |
| UniProt ID | Q8TB68 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/chromatin/PRR7/IF_images/PC-3_1.jpg|PC-3]]
![[Projects/TEreg-finding/protein-interested/detail/chromatin/PRR7/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | **16** | Nuclear + cyto, no preference |
| 蛋白大小 | 10/10 | ×1 | **10** | 274 aa，处于理想范围 |
| 研究新颖性 | 10/10 | ×5 | **50** | PubMed 12 篇，极度新颖 |
| 三维结构 | 6/10 | ×3 | **18** | 无 PDB 结构，仅 AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 1 domain(s), 新颖蛋白基线水平 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+0.0** | None |
| **原始总分** |  |  | **114/183** |  |
| **归一化总分** |  |  | **62.3/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Cell membrane, Postsynaptic cell membrane, Postsynaptic density membrane, Cytoplasm, perinuclear region, Synapse, Cell p | 实验证据/预测 |
| GO-CC | N/A | N/A |

**结论**: Nuclear + cyto, no preference

#### 3.2 蛋白大小评估

**评价**: 274 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 12 |

**关键文献**:
1. Kim et al. (2024). "HOS15-mediated turnover of PRR7 enhances freezing tolerance.". *New Phytol*. PMID: 39155726
2. Kim et al. (2024). "HOS15-mediated turnover of PRR7 enhances freezing tolerance.". *bioRxiv*. PMID: 38979283
3. Wang et al. (2023). "Pan-cancer analysis of super enhancer-induced PRR7-AS1 as a potential prognostic and immunological biomarker.". *Front Genet*. PMID: 37091809
4. Yuan et al. (2024). "Complex epistatic interactions between ELF3, PRR9, and PRR7 regulate the circadian clock and plant physiology.". *Genetics*. PMID: 38142447
5. Chen-Xi et al. (2023). "Long non-coding RNA PRR7-AS1 promotes osteosarcoma progression via binding RNF2 to transcriptionally suppress MTUS1.". *Front Oncol*. PMID: 38033505
**评价**: PubMed 12 篇，极度新颖

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 274 aa |
| PDB 条数 | 0 |
| 已注释结构域 | 1 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/chromatin/PRR7/PRR7-PAE.png]]

**评价**: 无 PDB 结构，仅 AlphaFold 预测，新颖蛋白基线水平

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | WW_domain-binding |

**染色质调控潜力分析**: 1 domain(s), 新颖蛋白基线水平

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

- F:protein-containing complex binding (GO:0044877, IEA:Ensembl)


**PPI 互证分析**:
- （待补充：综合 STRING、IntAct 和 GO 数据库的互作信息，分析 PPI 网络的一致性）
**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 0 条 | 仅预测 |
| 结构域 | UniProt/InterPro/Pfam | 1 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | Partially consistent |

**互证加分明细**:
--
**总计**: +0.0

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 12 篇，极度新颖
2. 核定位: needs confirmation

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 无 PDB 结构，仅 AlphaFold 预测

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 AlphaFold 的突变设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=PRR7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000131188-PRR7
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22PRR7%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q8TB68
- STRING: https://string-db.org/network/9606.ENSG00000131188
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TB68


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[PRR7-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/chromatin/PRR7/PRR7-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000131188-PRR7/subcellular

![](https://images.proteinatlas.org/46636/1013_F2_2_red_green.jpg)
![](https://images.proteinatlas.org/46636/1013_F2_3_red_green.jpg)
![](https://images.proteinatlas.org/46636/1017_F2_3_red_green.jpg)
![](https://images.proteinatlas.org/46636/1017_F2_4_red_green.jpg)
![](https://images.proteinatlas.org/46636/1203_C2_2_red_green.jpg)
![](https://images.proteinatlas.org/46636/1203_C2_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8TB68 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR051994; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000131188-PRR7/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| NEDD4 | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
