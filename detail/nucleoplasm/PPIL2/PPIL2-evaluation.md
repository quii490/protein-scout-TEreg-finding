---
type: protein-evaluation
gene: "PPIL2"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PPIL2 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | PPIL2 / UBOX7|CYC4|Cyp-60 |
| 蛋白全称 | RING-type E3 ubiquitin-protein ligase PPIL2 |
| 蛋白大小 | 520 aa |
| UniProt ID | Q13356 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | **16** | Nuclear + cyto, no preference |
| 蛋白大小 | 10/10 | ×1 | **10** | 520 aa，处于理想范围 |
| 研究新颖性 | 10/10 | ×5 | **50** | PubMed 16 篇，极度新颖 |
| 三维结构 | 10/10 | ×3 | **30** | 9 个 PDB 结构 |
| 调控结构域 | 10/10 | ×2 | **20** | 染色质/DNA 结构域: znf_ring/fyve/phd |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+1.0** | PDB + AlphaFold 结构互证 (+0.5); 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **132.5/183** |  |
| **归一化总分** |  |  | **72.4/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| HPA IF | 暂无数据（待细胞分析），核定位基于 UniProt + GO 注释 | -- |
| UniProt | Nucleus | 实验证据/预测 |
| GO-CC | GO:0005634 | IBA|IEA |


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PPIL2/IF_images/A-431_HPA035344_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PPIL2/IF_images/U-251MG_HPA035344_2.jpg|U-251MG]]

**结论**: Nuclear + cyto, no preference

#### 3.2 蛋白大小评估

**评价**: 520 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 16 |

**评价**: PubMed 16 篇，极度新颖

**关键文献**:
1. Bai R et al. (2021). "Structure of the activated human minor spliceosome". *Science*. PMID: 33509932
2. Wang P et al. (2025). "PPIL2 is a target of the JAK2/STAT5 pathway and promotes myeloproliferation via degradation of p53". *J Clin Invest*. PMID: 40338661
3. Rajiv C & Davis TL (2018). "Structural and Functional Insights into Human Nuclear Cyclophilins". *Biomolecules*. PMID: 30518120
4. Müller D et al. (2018). "Novel minor HLA DR associated antigens in type 1 diabetes". *Clin Immunol*. PMID: 29990590
5. Espeseth AS et al. (2006). "A genome wide analysis of ubiquitin ligases in APP processing identifies a novel regulator of BACE1 mRNA levels". *Mol Cell Neurosci*. PMID: 16978875
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 520 aa |
| PDB 条数 | 9 |
| 已注释结构域 | 12 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PPIL2/PPIL2-PAE.png]]

**评价**: 9 个 PDB 结构

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | Cyclophilin-like_dom_sf |
| InterPro | Cyclophilin-type_PPIase_CS |
| InterPro | Cyclophilin-type_PPIase_dom |
| InterPro | Cyclophilin_A-like |
| InterPro | PPIL2_U-box_dom |
| InterPro | Ubox_domain |
| InterPro | Znf_RING/FYVE/PHD |
| Pfam | Pro_isomerase |
| SMART | Ubox |
| PROSITE | CSA_PPIASE_1 |
| PROSITE | CSA_PPIASE_2 |
| PROSITE | U_BOX |

**染色质调控潜力分析**: 染色质/DNA 结构域: znf_ring/fyve/phd

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
| 三维结构 | AlphaFold + PDB | 9 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 12 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | Partially consistent |

**互证加分明细**:
PDB + AlphaFold 结构互证 (+0.5)
多库结构域一致 (+0.5)
**总计**: +1.0

### 4. 总体评价

**推荐等级**: ****o (4/5)

**核心优势**:
1. 新颖性: PubMed 16 篇，极度新颖
2. 核定位: needs confirmation

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 9 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=PPIL2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100023-PPIL2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22PPIL2%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q13356
- STRING: https://string-db.org/network/9606.ENSG00000100023
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13356


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[PPIL2-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PPIL2/PPIL2-PAE.png]]




