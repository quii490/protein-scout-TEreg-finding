---
type: protein-evaluation
gene: "POU6F1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## POU6F1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | POU6F1 / BRN5|MPOU|TCFB1 |
| 蛋白全称 | POU domain, class 6, transcription factor 1 |
| 蛋白大小 | 611 aa |
| UniProt ID | Q14863 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 10/10 | ×1 | **10** | 611 aa，处于理想范围 |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed 61 篇，中等研究热度 |
| 三维结构 | 8/10 | ×3 | **24** | 1 个 PDB 结构 + AlphaFold 预测 |
| 调控结构域 | 10/10 | ×2 | **20** | 染色质/DNA 结构域: homeobox_2, homeodomain, homeodomain-like_sf |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+2.0** | UniProt + GO 核定位互证 (+1); PDB + AlphaFold 结构互证 (+0.5); 多库结构域一致 (+0.5) |
|  | **原始总分** |  | **113/183** | **112.0/183** |  |  |  |
|  | **归一化总分** |  | **61.7/100** | **61.2/100** |  |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| HPA IF | 暂无数据（待细胞分析），核定位基于 UniProt + GO 注释 | -- |
| UniProt | Nucleus | 实验证据/预测 |
| GO-CC | N/A | N/A |


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/POU6F1/IF_images/HEK293_HPA050411_1.jpg|HEK293]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/POU6F1/IF_images/U-251MG_HPA050411_2.jpg|U-251MG]]

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 611 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 61 |

**评价**: PubMed 61 篇，中等研究热度

**关键文献**:
1. Wang S et al. (2025). "POU6F1 promote lumbar motor circuit reorganization following spinal cord injury". *Neurobiol Dis*. PMID: 40912411
2. Wang J et al. (2024). "POU6F1 promotes ferroptosis by increasing lncRNA-CASC2 transcription to regulate SOCS2/SLC7A11 signaling in gastric cancer". *Cell Biol Toxicol*. PMID: 38267746
3. Li WY et al. (2022). "Transgenic Schwann cells overexpressing POU6F1 promote sciatic nerve regeneration within acellular nerve allografts". *J Neural Eng*. PMID: 36317259
4. Wu D & Dean J (2023). "RNA exosome ribonuclease DIS3 degrades Pou6f1 to promote mouse pre-implantation cell differentiation". *Cell Rep*. PMID: 36724075
5. Liu M et al. (2026). "Downregulation of BST2 Rescues Cochlear Nerve Demyelination in Age-Related Hearing Loss via Enhancing Schwann Cell Migration". *Aging Cell*. PMID: 41391004
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 611 aa |
| PDB 条数 | 1 |
| 已注释结构域 | 14 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/POU6F1/POU6F1-PAE.png]]

**评价**: 1 个 PDB 结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | HD |
| InterPro | Homeodomain-like_sf |
| InterPro | Lambda_DNA-bd_dom_sf |
| InterPro | POU |
| InterPro | POU_dom |
| InterPro | POU_domain_TF |
| Pfam | Homeodomain |
| Pfam | Pou |
| SMART | HOX |
| SMART | POU |
| PROSITE | HOMEOBOX_2 |
| PROSITE | POU_1 |
| PROSITE | POU_2 |
| PROSITE | POU_3 |

**染色质调控潜力分析**: 染色质/DNA 结构域: homeobox_2, homeodomain, homeodomain-like_sf

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

- C:chromatin (GO:0000785, ISA:NTNU_SB)

**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 1 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 14 个 | 多库一致 |
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
1. 新颖性: PubMed 61 篇，中等研究热度
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 1 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=POU6F1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000184271-POU6F1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22POU6F1%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q14863
- STRING: https://string-db.org/network/9606.ENSG00000184271
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q14863


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[POU6F1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/POU6F1/POU6F1-PAE.png]]




