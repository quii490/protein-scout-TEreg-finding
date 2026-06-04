---
type: protein-evaluation
gene: "PUS1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PUS1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | PUS1 / MLASA1 |
| 蛋白全称 | Pseudouridylate synthase 1 homolog |
| 蛋白大小 | 427 aa |
| UniProt ID | Q9Y606 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/chromatin/PUS1/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/chromatin/PUS1/IF_images/U2OS_1.jpg|U2OS]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | **16** | Nuclear + cyto, no preference |
| 蛋白大小 | 10/10 | ×1 | **10** | 427 aa，处于理想范围 |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed 91 篇，中等研究热度 |
| 三维结构 | 10/10 | ×3 | **30** | 5 个 PDB 结构 |
| 调控结构域 | 7/10 | ×2 | **14** | 7 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+1.0** | PDB + AlphaFold 结构互证 (+0.5); 多库结构域一致 (+0.5) |
|  | **原始总分** |  | **86.5/183** | **86.0/183** |  |  |
|  | **归一化总分** |  | **47.3/100** | **47.0/100** |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| HPA IF | 暂无数据（待细胞分析），核定位基于 UniProt + GO 注释 | -- |
| UniProt | Mitochondrion, Nucleus, Cytoplasm | 实验证据/预测 |
| GO-CC | N/A | N/A |

**结论**: Nuclear + cyto, no preference

#### 3.2 蛋白大小评估

**评价**: 427 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 91 |

**关键文献**:
1. Zhang et al. (2023). "Quantitative profiling of pseudouridylation landscape in the human transcriptome.". *Nat Chem Biol*. PMID: 36997645
2. Wang et al. (2024). "Mitochondrial tRNA pseudouridylation governs erythropoiesis.". *Blood*. PMID: 38635773
3. Hu et al. (2024). "Pseudouridine synthase 1 promotes hepatocellular carcinoma through mRNA pseudouridylation to enhance the translation of oncogenic mRNAs.". *Hepatology*. PMID: 38015993
4. Martinez et al. (2022). "Pseudouridine synthases modify human pre-mRNA co-transcriptionally and affect pre-mRNA processing.". *Mol Cell*. PMID: 35051350
5. Zhang et al. (2023). "Identification and validation of key biomarkers based on RNA methylation genes in sepsis.". *Front Immunol*. PMID: 37701433
**评价**: PubMed 91 篇，中等研究热度

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 427 aa |
| PDB 条数 | 5 |
| 已注释结构域 | 7 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/chromatin/PUS1/PUS1-PAE.png]]

**评价**: 5 个 PDB 结构

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | PsdUridine_synth_cat_dom_sf |
| InterPro | PsdUridine_synth_TruA |
| InterPro | PsdUridine_synth_TruA_a/b_dom |
| InterPro | PsdUridine_synth_TruA_C |
| InterPro | PUS1/PUS2-like |
| InterPro | TruA/RsuA/RluB/E/F_N |
| Pfam | PseudoU_synth_1 |

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

- C:transcription regulator complex (GO:0005667, IEA:Ensembl)
- F:chromatin binding (GO:0003682, IEA:Ensembl)


**PPI 互证分析**:
- （待补充：综合 STRING、IntAct 和 GO 数据库的互作信息，分析 PPI 网络的一致性）
**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 5 条 | 一致 |
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
1. 新颖性: PubMed 91 篇，中等研究热度
2. 核定位: needs confirmation

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 5 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=PUS1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000177192-PUS1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22PUS1%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q9Y606
- STRING: https://string-db.org/network/9606.ENSG00000177192
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y606


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[PUS1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/chromatin/PUS1/PUS1-PAE.png]]




