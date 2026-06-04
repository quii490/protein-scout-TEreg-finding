---
type: protein-evaluation
gene: "SEPHS1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SEPHS1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | SEPHS1 / SPS|SPS1 |
| 蛋白全称 | Zincore component SEPHS1 |
| 蛋白大小 | 392 aa |
| UniProt ID | P49903 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/chromatin/SEPHS1/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/chromatin/SEPHS1/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | **16** | Nuclear + cyto, no preference |
| 蛋白大小 | 10/10 | ×1 | **10** | 392 aa，处于理想范围 |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed 39 篇，高度新颖 |
| 三维结构 | 8/10 | ×3 | **24** | 4 个 PDB 结构 + AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 7 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+1.0** | PDB + AlphaFold 结构互证 (+0.5); 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **110.5/183** |  |
| **归一化总分** |  |  | **60.4/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| HPA IF | 暂无数据（待细胞分析），核定位基于 UniProt + GO 注释 | -- |
| UniProt | Nucleus, Chromosome, Cytoplasm, Cell membrane, Nucleus membrane, Cytoplasm, Cytoplasm, Cytoplasm | 实验证据/预测 |
| GO-CC | N/A | N/A |

**结论**: Nuclear + cyto, no preference

#### 3.2 蛋白大小评估

**评价**: 392 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 39 |

**关键文献**:
1. Bianchi et al. (2025). "Zincore, an atypical coregulator, binds zinc finger transcription factors to control gene expression.". *Science*. PMID: 40608935
2. Hu et al. (2024). "SEPHS1 attenuates intervertebral disc degeneration by delaying nucleus pulposus cell senescence through the Hippo-Yap/Taz pathway.". *Am J Physiol Cell Physiol*. PMID: 38105759
3. Ahmed et al. (2024). "SEPHS1 Gene: A new master key for neurodevelopmental disorders.". *Clin Chim Acta*. PMID: 38960024
4. Na et al. (2018). "Selenophosphate synthetase 1 and its role in redox homeostasis, defense and proliferation.". *Free Radic Biol Med*. PMID: 29715549
5. Hao et al. (2023). "Pan-Cancer Study of the Prognosistic Value of Selenium Phosphate Synthase 1.". *Cancer Control*. PMID: 37072373
**评价**: PubMed 39 篇，高度新颖

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 392 aa |
| PDB 条数 | 4 |
| 已注释结构域 | 7 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/chromatin/SEPHS1/SEPHS1-PAE.png]]

**评价**: 4 个 PDB 结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | PurM-like_C_dom |
| InterPro | PurM-like_C_sf |
| InterPro | PurM-like_N |
| InterPro | PurM-like_N_sf |
| InterPro | SPS/SelD |
| Pfam | AIRS |
| Pfam | AIRS_C |

**染色质调控潜力分析**: 7 个已注释结构域，新颖蛋白基线水平

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
| 三维结构 | AlphaFold + PDB | 4 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 7 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | Partially consistent |

**互证加分明细**:
PDB + AlphaFold 结构互证 (+0.5)
多库结构域一致 (+0.5)
**总计**: +1.0

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 39 篇，高度新颖
2. 核定位: needs confirmation

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 4 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=SEPHS1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000086475-SEPHS1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SEPHS1%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/P49903
- STRING: https://string-db.org/network/9606.ENSG00000086475
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P49903


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[SEPHS1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/chromatin/SEPHS1/SEPHS1-PAE.png]]




