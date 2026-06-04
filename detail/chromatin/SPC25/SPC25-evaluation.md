---
type: protein-evaluation
gene: "SPC25"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SPC25 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | SPC25 / MGC22228|AD024 |
| 蛋白全称 | Kinetochore protein Spc25 |
| 蛋白大小 | 224 aa |
| UniProt ID | Q9HBM1 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/chromatin/SPC25/IF_images/U2OS_1.jpg|U2OS]]
![[Projects/TEreg-finding/protein-interested/detail/chromatin/SPC25/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | **16** | Nuclear + cyto, no preference |
| 蛋白大小 | 10/10 | ×1 | **10** | 224 aa，处于理想范围 |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed 84 篇，中等研究热度 |
| 三维结构 | 8/10 | ×3 | **24** | 4 个 PDB 结构 + AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 3 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+0.5** | PDB + AlphaFold 结构互证 (+0.5) |
|  | **原始总分** |  | **80.5/183** | **80.0/183** |  |  |  |
|  | **归一化总分** |  | **44.0/100** | **43.7/100** |  |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| HPA IF | 暂无数据（待细胞分析），核定位基于 UniProt + GO 注释 | -- |
| UniProt | Nucleus, Chromosome, centromere, kinetochore | 实验证据/预测 |
| GO-CC | GO:0005634 | IBA|IEA |

**结论**: Nuclear + cyto, no preference

#### 3.2 蛋白大小评估

**评价**: 224 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 84 |

**评价**: PubMed 84 篇，中等研究热度

**关键文献**:
1. Jiang X et al. (2024). "Targeting the SPC25/RIOK1/MYH9 Axis to Overcome Tumor Stemness and Platinum Resistance in Epithelial Ovarian Cancer". *Adv Sci (Weinh)*. PMID: 39488790
2. Asai K et al. (2024). "Artificial kinetochore beads establish a biorientation-like state in the spindle". *Science*. PMID: 39298589
3. Wang Q et al. (2019). "Up-regulation of SPC25 promotes breast cancer". *Aging (Albany NY)*. PMID: 31400751
4. Luo M et al. (2025). "Mechanism Study of E2F8 Activation of SPC25-Mediated Glutamine Metabolism Promoting Immune Escape in Lung Adenocarcinoma". *Immunology*. PMID: 39829079
5. Jin Y et al. (2025). "The multifaceted functions of SPC25 in cancer: from molecular pathways to targeted therapy". *Front Med (Lausanne)*. PMID: 40400636
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 224 aa |
| PDB 条数 | 4 |
| 已注释结构域 | 3 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/chromatin/SPC25/SPC25-PAE.png]]

**评价**: 4 个 PDB 结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | Spc25 |
| InterPro | Spc25_C |
| Pfam | Spindle_Spc25 |

**染色质调控潜力分析**: 3 个已注释结构域，新颖蛋白基线水平

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

- C:Ndc80 complex (GO:0031262, IDA:UniProtKB)

**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 4 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 3 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | Partially consistent |

**互证加分明细**:
PDB + AlphaFold 结构互证 (+0.5)
**总计**: +0.5

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 84 篇，中等研究热度
2. 核定位: needs confirmation

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 4 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=SPC25
- Protein Atlas: https://www.proteinatlas.org/ENSG00000152253-SPC25
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SPC25%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q9HBM1
- STRING: https://string-db.org/network/9606.ENSG00000152253
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9HBM1


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[SPC25-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/chromatin/SPC25/SPC25-PAE.png]]




