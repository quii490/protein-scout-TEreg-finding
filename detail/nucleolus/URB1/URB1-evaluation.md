---
type: protein-evaluation
gene: "URB1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## URB1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | URB1 / KIAA0539|NPA1 |
| 蛋白全称 | Nucleolar pre-ribosomal-associated protein 1 |
| 蛋白大小 | 2271 aa |
| UniProt ID | O60287 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/URB1/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/URB1/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 6/10 | ×4 | **24** | 细胞核+细胞质，UniProt 支持核定位 |
| 蛋白大小 | 2/10 | ×1 | **2** | 2271 aa, too extreme |
| 研究新颖性 | 10/10 | ×5 | **50** | PubMed 13 篇，极度新颖 |
| 三维结构 | 6/10 | ×3 | **18** | 无 PDB 结构，仅 AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 8 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+0.5** | 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **114.5/183** |  |
| **归一化总分** |  |  | **62.6/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| HPA IF | 暂无数据（待细胞分析），核定位基于 UniProt + GO 注释 | -- |
| UniProt | Nucleus, nucleolus | 实验证据/预测 |
| GO-CC | N/A | N/A |

**结论**: 细胞核+细胞质，UniProt 支持核定位

#### 3.2 蛋白大小评估

**评价**: 2271 aa， too extreme

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 13 |

**评价**: PubMed 13 篇，极度新颖

**关键文献**:
1. Shan L et al. (2023). "Nucleolar URB1 ensures 3' ETS rRNA removal to prevent exosome surveillance". *Nature*. PMID: 36890225
2. Taheri M et al. (2023). "Upregulation of MAPKAPK5-AS1, PXN-AS1 and URB1-AS1 lncRNAs in non-functioning pituitary adenoma". *J Cell Mol Med*. PMID: 37154079
3. Bui APN et al. (2025). "PCR-RFLP assays to detect recessive lethal alleles in Landrace and Duroc pigs in Vietnam". *J Vet Diagn Invest*. PMID: 40772539
4. Wang T et al. (2021). "Ribosome assembly factor URB1 contributes to colorectal cancer proliferation through transcriptional activation of ATF4". *Cancer Sci*. PMID: 32888357
5. He J et al. (2017). "Ribosome biogenesis protein Urb1 acts downstream of mTOR complex 1 to modulate digestive organ development in zebrafish". *J Genet Genomics*. PMID: 29246861
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 2271 aa |
| PDB 条数 | 0 |
| 已注释结构域 | 8 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleolus/URB1/URB1-PAE.png]]

**评价**: 无 PDB 结构，仅 AlphaFold 预测，新颖蛋白基线水平

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | ARM-type_fold |
| InterPro | HEAT_URB1 |
| InterPro | URB1 |
| InterPro | URB1_C |
| InterPro | URB1_N |
| Pfam | HEAT_URB1 |
| Pfam | NopRA1 |
| Pfam | Npa1 |

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

**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 0 条 | 仅预测 |
| 结构域 | UniProt/InterPro/Pfam | 8 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
多库结构域一致 (+0.5)
**总计**: +0.5

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 13 篇，极度新颖
2. 核定位: 部分核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 无 PDB 结构，仅 AlphaFold 预测

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 AlphaFold 的突变设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=URB1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000142207-URB1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22URB1%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/O60287
- STRING: https://string-db.org/network/9606.ENSG00000142207
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O60287


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[URB1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/URB1/URB1-PAE.png]]




