---
type: protein-evaluation
gene: "PLRG1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PLRG1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | PLRG1 / PRL1|Prp46|PRPF46|Cwc1|TANGO4 |
| 蛋白全称 | Pleiotropic regulator 1 |
| 蛋白大小 | 514 aa |
| UniProt ID | O43660 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/chromatin/PLRG1/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/chromatin/PLRG1/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 10/10 | ×1 | **10** | 514 aa，处于理想范围 |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed 28 篇，高度新颖 |
| 三维结构 | 10/10 | ×3 | **30** | 35 个 PDB 结构 |
| 调控结构域 | 7/10 | ×2 | **14** | 11 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+2.0** | UniProt + GO 核定位互证 (+1); PDB + AlphaFold 结构互证 (+0.5); 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **133/183** |  |
| **归一化总分** |  |  | **72.7/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| HPA IF | 暂无数据（待细胞分析），核定位基于 UniProt + GO 注释 | -- |
| UniProt | Nucleus, Nucleus speckle | 实验证据/预测 |
| GO-CC | GO:0005634 | IBA|IDA|IEA |

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 514 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 28 |

**关键文献**:
1. Liu et al. (2021). "USP42 drives nuclear speckle mRNA splicing via directing dynamic phase separation to promote tumorigenesis.". *Cell Death Differ*. PMID: 33731873
2. Hasan et al. (2025). "Discovering periodontitis biomarkers and therapeutic targets through bioinformatics and ensemble learning analysis.". *Sci Rep*. PMID: 41044121
3. de et al. (2018). "Prp19/Pso4 Is an Autoinhibited Ubiquitin Ligase Activated by Stepwise Assembly of Three Splicing Factors.". *Mol Cell*. PMID: 29547724
4. Kwon et al. (2024). "YBX1 promotes epithelial-mesenchymal transition in hepatocellular carcinoma via transcriptional regulation of PLRG1.". *Med Oncol*. PMID: 39400789
5. Choi et al. (2023). "Elevated level of PLRG1 is critical for the proliferation and maintenance of genome stability of tumor cells.". *BMB Rep*. PMID: 37817442
**评价**: PubMed 28 篇，高度新颖

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 514 aa |
| PDB 条数 | 35 |
| 已注释结构域 | 11 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/chromatin/PLRG1/PLRG1-PAE.png]]

**评价**: 35 个 PDB 结构

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | Prp46/PLRG1-like |
| InterPro | WD40/YVTN_repeat-like_dom_sf |
| InterPro | WD40_PAC1 |
| InterPro | WD40_repeat_CS |
| InterPro | WD40_repeat_dom_sf |
| InterPro | WD40_rpt |
| Pfam | WD40 |
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

- C:Prp19 complex (GO:0000974, IPI:ComplexPortal)


**PPI 互证分析**:
- （待补充：综合 STRING、IntAct 和 GO 数据库的互作信息，分析 PPI 网络的一致性）
**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 35 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 11 个 | 多库一致 |
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
1. 新颖性: PubMed 28 篇，高度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 35 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=PLRG1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000171566-PLRG1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22PLRG1%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/O43660
- STRING: https://string-db.org/network/9606.ENSG00000171566
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O43660


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[PLRG1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/chromatin/PLRG1/PLRG1-PAE.png]]




