---
type: protein-evaluation
gene: "STOX2"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## STOX2 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | STOX2 / DKFZp762K222 |
| 蛋白全称 | Storkhead-box protein 2 |
| 蛋白大小 | 926 aa |
| UniProt ID | Q9P2F5 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleus-cytoplasm/STOX2/IF_images/HeLa_1.jpg|HeLa]]
![[Projects/TEreg-finding/protein-interested/detail/nucleus-cytoplasm/STOX2/IF_images/SH-SY5Y_1.jpg|SH-SY5Y]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | **16** | Nuclear + cyto, no preference |
| 蛋白大小 | 8/10 | ×1 | **8** | 926 aa，尚可接受 |
| 研究新颖性 | 10/10 | ×5 | **50** | PubMed 5 篇，极度新颖 |
| 三维结构 | 6/10 | ×3 | **18** | 无 PDB 结构，仅 AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 3 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+0.0** | None |
| **原始总分** |  |  | **112/183** |  |
| **归一化总分** |  |  | **61.2/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

> 
| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| HPA IF | 暂无数据（待细胞分析），核定位基于 UniProt + GO 注释 | -- |
| UniProt |  | 实验证据/预测 |
| GO-CC | N/A | N/A |

**结论**: Nuclear + cyto, no preference

#### 3.2 蛋白大小评估

**评价**: 926 aa，尚可接受

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 5 |

**评价**: PubMed 5 篇，极度新颖

**关键文献**:
1. Sasahira T et al. (2016). "Storkhead box 2 and melanoma inhibitory activity promote oral squamous cell carcinoma progression". *Oncotarget*. PMID: 27050375
2. Li H et al. (2025). "Revealing the key modules and potential prognostic markers of gastric cancer transformation based on weighted gene co-expression networks". *Front Genet*. PMID: 41367615
3. Zhang R et al. (2024). "Whole-Genome Sequencing for Identifying Candidate Genes Related to the Special Phenotypes of the Taihu Dianzi Pigeon". *Animals (Basel)*. PMID: 38612286
4. Liburkin-Dan T et al. (2022). "Knock-Out of the Five Lysyl-Oxidase Family Genes Enables Identification of Lysyl-Oxidase Pro-Enzyme Regulated Genes". *Int J Mol Sci*. PMID: 36232621
5. Oudejans CB et al. (2016). "Noncoding RNA-regulated gain-of-function of STOX2 in Finnish pre-eclamptic families". *Sci Rep*. PMID: 27555360
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 926 aa |
| PDB 条数 | 0 |
| 已注释结构域 | 3 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleus-cytoplasm/STOX2/STOX2-PAE.png]]

**评价**: 无 PDB 结构，仅 AlphaFold 预测，新颖蛋白基线水平

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | Storkhead-box_WHD |
| InterPro | STOX1/2 |
| Pfam | WHD_Storkhead |

**染色质调控潜力分析**: 3 个已注释结构域，新颖蛋白基线水平

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| Csnk1e | tandem affinity purification | 20360068 | — | — |
| EBI-54261957 | clash | 23622248 | — | — |
| EBI-22266552 | clash | 23622248 | — | — |


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
| 结构域 | UniProt/InterPro/Pfam | 3 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | Partially consistent |

**互证加分明细**:
--
**总计**: +0.0

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 5 篇，极度新颖
2. 核定位: needs confirmation

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 无 PDB 结构，仅 AlphaFold 预测

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 AlphaFold 的突变设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=STOX2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000173320-STOX2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22STOX2%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q9P2F5
- STRING: https://string-db.org/network/9606.ENSG00000173320
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9P2F5


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[STOX2-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleus-cytoplasm/STOX2/STOX2-PAE.png]]




