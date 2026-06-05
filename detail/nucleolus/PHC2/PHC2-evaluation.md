---
type: protein-evaluation
gene: "PHC2"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PHC2 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | PHC2 / HPH2 |
| 蛋白全称 | Polyhomeotic-like protein 2 |
| 蛋白大小 | 858 aa |
| UniProt ID | Q8IXK0 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/PHC2/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/PHC2/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 8/10 | ×1 | **8** | 858 aa，尚可接受 |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed 36 篇，高度新颖 |
| 三维结构 | 6/10 | ×3 | **18** | 无 PDB 结构，仅 AlphaFold 预测 |
| 调控结构域 | 10/10 | ×2 | **20** | 染色质/DNA 结构域: pcg_chromatin_remod_factors |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+1.5** | UniProt + GO 核定位互证 (+1); 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **125/183** |  |
| **归一化总分** |  |  | **68.3/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus | 实验证据/预测 |
| GO-CC | N/A | N/A |

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 858 aa，尚可接受

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 36 |

**关键文献**:
1. Niekamp et al. (2024). "Modularity of PRC1 composition and chromatin interaction define condensate properties.". *Mol Cell*. PMID: 38521066
2. Kornya et al. (2023). "Investigation of Platelet Function Analyzer 200 platelet function measurements in healthy cats and cats receiving clopidogrel.". *J Vet Diagn Invest*. PMID: 37646490
3. Song et al. (2025). "Nucleoporins cooperate with Polycomb silencers to promote transcriptional repression and repair at DNA double-strand breaks.". *Proc Natl Acad Sci U S A*. PMID: 40440073
4. Bae et al. (2019). "Phc2 controls hematopoietic stem and progenitor cell mobilization from bone marrow by repressing Vcam1 expression.". *Nat Commun*. PMID: 31375680
5. Gray et al. (2016). "BMI1 regulates PRC1 architecture and activity through homo- and hetero-oligomerization.". *Nat Commun*. PMID: 27827373
**评价**: PubMed 36 篇，高度新颖

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 858 aa |
| PDB 条数 | 0 |
| 已注释结构域 | 11 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleolus/PHC2/PHC2-PAE.png]]

**评价**: 无 PDB 结构，仅 AlphaFold 预测，新颖蛋白基线水平

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | PcG_chromatin_remod_factors |
| InterPro | SAM |
| InterPro | SAM/pointed_sf |
| InterPro | Znf_FCS |
| InterPro | Znf_FCS_sf |
| Pfam | PHC2_SAM_assoc |
| Pfam | SAM_1 |
| Pfam | zf-FCS_1 |
| SMART | SAM |
| PROSITE | SAM_DOMAIN |
| PROSITE | ZF_FCS |

**染色质调控潜力分析**: 染色质/DNA 结构域: pcg_chromatin_remod_factors

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| Plcg2 | two hybrid | 15102471 | — | — |
| MCRS1 | pull down | 16189514 | — | — |
| LMO3 | two hybrid pooling approach | 16189514 | — | — |
| SFMBT1 | two hybrid pooling approach | 16189514 | — | — |
| PHC1 | two hybrid pooling approach | 16189514 | — | — |
| FHL3 | two hybrid pooling approach | 16189514 | — | — |
| SCMH1 | two hybrid pooling approach | 16169070 | — | — |
| TMEM70 | two hybrid pooling approach | 16169070 | — | — |
| AFG3L2 | two hybrid pooling approach | 16169070 | — | — |
| BSDC1 | two hybrid pooling approach | 16169070 | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

- C:heterochromatin (GO:0000792, IEA:Ensembl)
- C:PcG protein complex (GO:0031519, IDA:UniProtKB)
- C:PRC1 complex (GO:0035102, IDA:UniProtKB)
- F:chromatin binding (GO:0003682, IBA:GO_Central)


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
1. 新颖性: PubMed 36 篇，高度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 无 PDB 结构，仅 AlphaFold 预测

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 AlphaFold 的突变设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=PHC2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000134686-PHC2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22PHC2%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q8IXK0
- STRING: https://string-db.org/network/9606.ENSG00000134686
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IXK0


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[PHC2-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/PHC2/PHC2-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000134686-PHC2/subcellular

![](https://images.proteinatlas.org/47403/616_G8_1_red_green.jpg)
![](https://images.proteinatlas.org/47403/616_G8_2_red_green.jpg)
![](https://images.proteinatlas.org/47403/619_G8_1_red_green.jpg)
![](https://images.proteinatlas.org/47403/619_G8_2_red_green.jpg)
![](https://images.proteinatlas.org/47403/622_G8_1_red_green.jpg)
![](https://images.proteinatlas.org/47403/622_G8_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
