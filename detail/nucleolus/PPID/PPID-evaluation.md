---
type: protein-evaluation
gene: "PPID"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PPID 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | PPID / CYP-40|CypD |
| 蛋白全称 | Peptidyl-prolyl cis-trans isomerase D |
| 蛋白大小 | 370 aa |
| UniProt ID | Q08752 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/PPID/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/PPID/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | **28** | UniProt 核定位，部分细胞质 |
| 蛋白大小 | 10/10 | ×1 | **10** | 370 aa，处于理想范围 |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed 92 篇，中等研究热度 |
| 三维结构 | 6/10 | ×3 | **18** | 无 PDB 结构，仅 AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 11 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+1.5** | UniProt + GO 核定位互证 (+1); 多库结构域一致 (+0.5) |
|  | **原始总分** |  | **87/183** | **86.0/183** |  |  |
|  | **归一化总分** |  | **47.5/100** | **47.0/100** |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| HPA IF | 暂无数据（待细胞分析），核定位基于 UniProt + GO 注释 | -- |
| UniProt | Cytoplasm, Nucleus, nucleolus, Nucleus, nucleoplasm | 实验证据/预测 |
| GO-CC | N/A | N/A |

**结论**: UniProt Nucleus + partial cyto

#### 3.2 蛋白大小评估

**评价**: 370 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 92 |

**关键文献**:
1. Lucas et al. (2022). "Editorial.". *J Pers Soc Psychol*. PMID: 35049327
2. Jiang et al. (2024). "Activation of BK channels prevents diabetes-induced osteopenia by regulating mitochondrial Ca(2+) and SLC25A5/ANT2-PINK1-PRKN-mediated mitophagy.". *Autophagy*. PMID: 38873928
3. Biczo et al. (2018). "Mitochondrial Dysfunction, Through Impaired Autophagy, Leads to Endoplasmic Reticulum Stress, Deregulated Lipid Metabolism, and Pancreatitis in Animal Models.". *Gastroenterology*. PMID: 29074451
4. Gunduz-Cinar et al. (2019). "Identification of a novel gene regulating amygdala-mediated fear extinction.". *Mol Psychiatry*. PMID: 29311651
5. Kirkwood et al. (2022). "Pituitary Pars Intermedia Dysfunction (PPID) in Horses.". *Vet Sci*. PMID: 36288169
**评价**: PubMed 92 篇，中等研究热度

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 370 aa |
| PDB 条数 | 0 |
| 已注释结构域 | 11 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleolus/PPID/PPID-PAE.png]]

**评价**: 无 PDB 结构，仅 AlphaFold 预测，新颖蛋白基线水平

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | Cyclophilin-like_dom_sf |
| InterPro | Cyclophilin-type_PPIase_CS |
| InterPro | Cyclophilin-type_PPIase_dom |
| InterPro | TPR-like_helical_dom_sf |
| InterPro | TPR_rpt |
| Pfam | Pro_isomerase |
| SMART | TPR |
| PROSITE | CSA_PPIASE_1 |
| PROSITE | CSA_PPIASE_2 |
| PROSITE | TPR |
| PROSITE | TPR_REGION |

**染色质调控潜力分析**: 11 个已注释结构域，新颖蛋白基线水平

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| HAP1 | two hybrid pooling approach | 16169070 | — | — |
| KAT7 | two hybrid pooling approach | 16169070 | — | — |
| IMMT | cross-linking study | 30021884 | — | — |
| IQCB1 | inference by socio-affinity scoring | unassigned1312 | — | — |
| UROD | anti tag coimmunoprecipitation | 28514442 | — | — |
| RPL29 | anti tag coimmunoprecipitation | 33961781 | — | — |
| ADAM29 | anti tag coimmunoprecipitation | 33961781 | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

- P:protein-containing complex assembly (GO:0065003, IDA:UniProtKB)


**PPI 互证分析**:
- （待补充：综合 STRING、IntAct 和 GO 数据库的互作信息，分析 PPI 网络的一致性）
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

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 92 篇，中等研究热度
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 无 PDB 结构，仅 AlphaFold 预测

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 AlphaFold 的突变设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=PPID
- Protein Atlas: https://www.proteinatlas.org/ENSG00000171497-PPID
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22PPID%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q08752
- STRING: https://string-db.org/network/9606.ENSG00000171497
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q08752


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[PPID-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/PPID/PPID-PAE.png]]




