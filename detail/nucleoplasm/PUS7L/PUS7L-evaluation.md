---
type: protein-evaluation
gene: "PUS7L"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PUS7L 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | PUS7L / DKFZP434G1415 |
| 蛋白全称 | Pseudouridylate synthase PUS7L |
| 蛋白大小 | 701 aa |
| UniProt ID | Q9H0K6 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | **16** | Nuclear + cyto, no preference |
| 蛋白大小 | 10/10 | ×1 | **10** | 701 aa，处于理想范围 |
| 研究新颖性 | 10/10 | ×5 | **50** | PubMed 4 篇，极度新颖 |
| 三维结构 | 6/10 | ×3 | **18** | 无 PDB 结构，仅 AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 10 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+0.5** | 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **114.5/183** |  |
| **归一化总分** |  |  | **62.6/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| HPA IF | 暂无数据（待细胞分析），核定位基于 UniProt + GO 注释 | -- |
| UniProt |  | 实验证据/预测 |
| GO-CC | N/A | N/A |


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PUS7L/IF_images/CACO-2_HPA056203_1.jpg|CACO-2]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PUS7L/IF_images/U-251MG_HPA056203_2.jpg|U-251MG]]

**结论**: Nuclear + cyto, no preference

#### 3.2 蛋白大小评估

**评价**: 701 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 4 |

**评价**: PubMed 4 篇，极度新颖

**关键文献**:
1. Xu H et al. (2025). "A comprehensive tRNA pseudouridine map uncovers targets dependent on human stand-alone pseudouridine synthases". *Nat Cell Biol*. PMID: 41136621
2. Thavarajah T et al. (2020). "The plasma peptides of sepsis". *Clin Proteomics*. PMID: 32636717
3. Li J et al. (2025). "Unveiling the clinical significance of RNA pseudouridine in colorectal cancer". *Sci China Life Sci*. PMID: 40189490
4. Jin Z et al. (2022). "Integrative multiomics evaluation reveals the importance of pseudouridine synthases in hepatocellular carcinoma". *Front Genet*. PMID: 36437949
5. Cornejo-Sanchez DM et al. (2023). "Rare-variant association analysis reveals known and new age-related hearing loss genes". *Eur J Hum Genet*. PMID: 36788145
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 701 aa |
| PDB 条数 | 0 |
| 已注释结构域 | 10 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PUS7L/PUS7L-PAE.png]]

**评价**: 无 PDB 结构，仅 AlphaFold 预测，新颖蛋白基线水平

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | PsdUridine_synth_cat_dom_sf |
| InterPro | PsdUridine_synth_TruD |
| InterPro | PsdUridine_synth_TruD_insert |
| InterPro | PUS7L_N |
| InterPro | R3H_PUS7L |
| InterPro | TruD_catalytic |
| Pfam | PUS7L_N |
| Pfam | R3H_PUS7L |
| Pfam | TruD |
| PROSITE | TRUD |

**染色质调控潜力分析**: 10 个已注释结构域，新颖蛋白基线水平

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
| 结构域 | UniProt/InterPro/Pfam | 10 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | Partially consistent |

**互证加分明细**:
多库结构域一致 (+0.5)
**总计**: +0.5

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 4 篇，极度新颖
2. 核定位: needs confirmation

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 无 PDB 结构，仅 AlphaFold 预测

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 AlphaFold 的突变设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=PUS7L
- Protein Atlas: https://www.proteinatlas.org/ENSG00000129317-PUS7L
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22PUS7L%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q9H0K6
- STRING: https://string-db.org/network/9606.ENSG00000129317
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H0K6


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[PUS7L-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PUS7L/PUS7L-PAE.png]]




