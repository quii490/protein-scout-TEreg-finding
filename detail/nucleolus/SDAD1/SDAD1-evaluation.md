---
type: protein-evaluation
gene: "SDAD1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SDAD1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | SDAD1 / FLJ10498|Sda1|hSDA |
| 蛋白全称 | Protein SDA1 homolog |
| 蛋白大小 | 687 aa |
| UniProt ID | Q9NVU7 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/SDAD1/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/SDAD1/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 6/10 | ×4 | **24** | 细胞核+细胞质，UniProt 支持核定位 |
| 蛋白大小 | 10/10 | ×1 | **10** | 687 aa，处于理想范围 |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed 37 篇，高度新颖 |
| 三维结构 | 10/10 | ×3 | **30** | 7 个 PDB 结构 |
| 调控结构域 | 7/10 | ×2 | **14** | 8 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+1.0** | PDB + AlphaFold 结构互证 (+0.5); 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **124.5/183** |  |
| **归一化总分** |  |  | **68.0/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| HPA IF | 暂无数据（待细胞分析），核定位基于 UniProt + GO 注释 | -- |
| UniProt | Nucleus, nucleolus | 实验证据/预测 |
| GO-CC | GO:0005634 | IBA|IDA|IEA |

**结论**: 细胞核+细胞质，UniProt 支持核定位

#### 3.2 蛋白大小评估

**评价**: 687 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 37 |

**关键文献**:
1. Chen et al. (2024). "Regulation of microglia inflammation and oligodendrocyte demyelination by Engeletin via the TLR4/RRP9/NF-κB pathway after spinal cord injury.". *Pharmacol Res*. PMID: 39395773
2. Meng et al. (2024). "Higher expression of TSR2 aggravating hypertension via the PPAR signaling pathway.". *Aging (Albany NY)*. PMID: 38814181
3. Xiao et al. (2024). "Roles of NOC3L and DDX17 in acquired immunodeficiency complicated with viral myocarditis and osteoporosis.". *Medicine (Baltimore)*. PMID: 39809148
4. Yuan et al. (2023). "LncRNA LINC01232 Enhances Proliferation, Angiogenesis, Migration and Invasion of Colon Adenocarcinoma Cells by Downregulating miR-181a-5p.". *J Microbiol Biotechnol*. PMID: 36655275
5. Jing et al. (2019). "Long non-coding RNA small nucleolar RNA host gene 7 facilitates cardiac hypertrophy via stabilization of SDA1 domain containing 1 mRNA.". *J Cell Biochem*. PMID: 31026094
**评价**: PubMed 37 篇，高度新颖

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 687 aa |
| PDB 条数 | 7 |
| 已注释结构域 | 8 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleolus/SDAD1/SDAD1-PAE.png]]

**评价**: 7 个 PDB 结构

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | ARM-type_fold |
| InterPro | Sda1 |
| InterPro | SDA1_C |
| InterPro | SDA1_MD |
| InterPro | SDA1_N |
| Pfam | SDA1_C |
| Pfam | SDA1_dom |
| Pfam | SDA1_HEAT |

**染色质调控潜力分析**: 8 个已注释结构域，新颖蛋白基线水平

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
| 三维结构 | AlphaFold + PDB | 7 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 8 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
PDB + AlphaFold 结构互证 (+0.5)
多库结构域一致 (+0.5)
**总计**: +1.0

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 37 篇，高度新颖
2. 核定位: 部分核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 7 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=SDAD1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000198301-SDAD1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SDAD1%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q9NVU7
- STRING: https://string-db.org/network/9606.ENSG00000198301
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NVU7


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[SDAD1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/SDAD1/SDAD1-PAE.png]]




