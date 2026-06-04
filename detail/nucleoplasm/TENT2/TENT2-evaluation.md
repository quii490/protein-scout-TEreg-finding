---
type: protein-evaluation
gene: "TENT2"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TENT2 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | TENT2 / FLJ38499|GLD2|TUT2 |
| 蛋白全称 | terminal nucleotidyltransferase 2 |
| 蛋白大小 | 484 aa |
| UniProt ID | Q6PIY7 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | **16** | Nuclear + cyto, no preference |
| 蛋白大小 | 10/10 | ×1 | **10** | 484 aa，处于理想范围 |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed 28 篇，高度新颖 |
| 三维结构 | 6/10 | ×3 | **18** | 无 PDB 结构，仅 AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | No annotated domains, 新颖蛋白基线水平 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+0.0** | None |
| **原始总分** |  |  | **104/183** |  |
| **归一化总分** |  |  | **56.8/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| HPA IF | 暂无数据（待细胞分析），核定位基于 UniProt + GO 注释 | -- |
| UniProt | N/A | 实验证据/预测 |
| GO-CC | N/A | N/A |


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TENT2/IF_images/U-251MG_HPA054468_1.jpg|U-251MG]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TENT2/IF_images/U2OS_HPA054468_2.jpg|U2OS]]

**结论**: Nuclear + cyto, no preference

#### 3.2 蛋白大小评估

**评价**: 484 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 28 |

**评价**: PubMed 28 篇，高度新颖

**关键文献**:
1. Wu G et al. (2024). "RNA 3'end tailing safeguards cells against products of pervasive transcription termination". *Nat Commun*. PMID: 39617768
2. Wardaszka-Pianka P et al. (2025). "Terminal nucleotidyltransferase Tent2 microRNA A-tailing enzyme regulates excitatory/inhibitory balance in the hippocampus". *RNA*. PMID: 40101932
3. Steinberg JI et al. (2025). "HENMT1 restricts endogenous retrovirus activity by methylation of 3'-tRNA fragments". *bioRxiv*. PMID: 40463248
4. Snoek BC et al. (2019). "Altered microRNA processing proteins in HPV-induced cancers". *Curr Opin Virol*. PMID: 31408800
5. Yang A et al. (2022). "TENT2, TUT4, and TUT7 selectively regulate miRNA sequence and abundance". *Nat Commun*. PMID: 36071058
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | N/A aa |
| PDB 条数 | 0 |
| 已注释结构域 | 0 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TENT2/TENT2-PAE.png]]

**评价**: 无 PDB 结构，仅 AlphaFold 预测，新颖蛋白基线水平

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|

**染色质调控潜力分析**: No annotated domains, 新颖蛋白基线水平

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
| 三维结构 | AlphaFold + PDB | 0 条 | 仅预测 |
| 结构域 | UniProt/InterPro/Pfam | 0 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | Partially consistent |

**互证加分明细**:
--
**总计**: +0.0

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 28 篇，高度新颖
2. 核定位: needs confirmation

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 无 PDB 结构，仅 AlphaFold 预测

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 AlphaFold 的突变设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=TENT2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000164329-TENT2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22TENT2%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q6PIY7
- STRING: https://string-db.org/network/9606.ENSG00000164329
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6PIY7


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[TENT2-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TENT2/TENT2-PAE.png]]




