---
type: protein-evaluation
gene: "NAA20"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NAA20 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | NAA20 / dJ1002M8.1|NAT3 |
| 蛋白名称 | N-alpha-acetyltransferase 20 |
| 蛋白大小 | 178 aa |
| UniProt ID | P61599 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 加权 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 4/10 | ×4 | **16** | 核+胞质均分，无偏好 |
| 📏 蛋白大小 | 8/10 | ×1 | **8** | 178 aa，可接受范围 |
| 🆕 研究新颖性 | 10/10 | ×5 | **50** | PubMed 17篇，极度新颖 |
| 🏗️ 三维结构 | 8/10 | ×3 | **24** | 3 个 PDB 实验结构 + AlphaFold 预测 |
| 🧬 调控结构域 | 7/10 | ×2 | **14** | 5 个结构域注释，新颖蛋白基线（存在新域发现潜力） |
| 🔗 PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极少 |
| ➕ 互证加分 | — | — | **+1.0** | 三维结构: AlphaFold + PDB 双源 (+0.5); 结构域: 多库注释一致 (+0.5) |
| **原始总分** |  |  | **118.5/183** |  |
| **归一化总分** |  |  | **64.8/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_conserved_high_confidence | 高置信度保守 |
| Protein Atlas (IF) | IF image available (embedded below) | See IF_images/ |
| UniProt | N/A | 实验/预测 |
| GO Cellular Component | GO:0005634 | N/A |


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NAA20/IF_images/PC-3_HPA063344_1.jpg|PC-3]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NAA20/IF_images/Rh30_HPA063344_2.jpg|Rh30]]

**结论**: 核+胞质均分，无偏好

#### 3.2 蛋白大小评估

**评价**: 178 aa，178 aa，可接受范围。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 17 |
| 核定位分数 (weighted max) | 4 |
| Research hotness | 4.5308 |

**评价**: PubMed 17篇，极度新颖

**关键文献**:
1. Huber M et al. (2020). "NatB-Mediated N-Terminal Acetylation Affects Growth and Biotic Stress Responses". *Plant Physiol*. PMID: 31744933
2. D'Onofrio G et al. (2023). "Novel biallelic variants expand the phenotype of NAA20-related syndrome". *Clin Genet*. PMID: 37191084
3. Lasa M et al. (2020). "Maturation of NAA20 Aminoterminal End Is Essential to Assemble NatB N-Terminal Acetyltransferase Complex". *J Mol Biol*. PMID: 32976911
4. Hong H et al. (2017). "Molecular Basis of Substrate Specific Acetylation by N-Terminal Acetyltransferase NatB". *Structure*. PMID: 28380339
5. Sengodan K & Palli SR (2025). "Histone and N-terminal acetyltransferases play important roles in female reproduction and embryogenesis of the red flour beetle Tribolium castaneum". *Insect Mol Biol*. PMID: 40437965
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 178 aa |
| PDB 条目数 | 3 |
| UniProt 注释结构域数 | 5 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NAA20/NAA20-PAE.png]]

**评价**: 3 个 PDB 实验结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | Acyl_CoA_acyltransferase |
| InterPro | GNAT_dom |
| InterPro | NatB_acetyltransferase_subunit |
| Pfam | Acetyltransf_1 |
| PROSITE | GNAT |

**染色质调控潜力分析**: 5 个结构域注释，新颖蛋白基线（存在新域发现潜力）

#### 3.6 PPI 网络

**实验验证互作** (IntAct):

IntAct 实验互作: 17 条

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| — | — | — | — |

**已知复合体成员** (GO Cellular Component):

- C:NatB complex (GO:0031416, IPI:ComplexPortal)

**PPI 互证分析**: PPI 数据极少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 3 entries | 一致 |
| 结构域 | UniProt / InterPro / Pfam | 5 domains | 多库一致 |
| PPI | STRING + IntAct | 0 STRING + 17 IntAct | 单源 |
| 定位 | Protein Atlas / UniProt / GO | Nucleus | 部分一致 |

**互证加分明细**:
三维结构: AlphaFold + PDB 双源 (+0.5)
结构域: 多库注释一致 (+0.5)
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ★★★☆☆ (3/5)

**核心优势**:
1. 新颖性: PubMed 17 篇，极度新颖
2. 核定位: 核定位证据需进一步确认

**风险/不确定性**:
1. HPA IF 数据可进一步验证
2. 3 PDB 结构可用

**下一步建议**:
- [ ] 验证核定位: IF 实验确认亚核定位
- [ ] 功能研究: 基于 PPI 网络设计功能实验
- [ ] 结构分析: 基于 PDB 结构设计功能实验

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=NAA20
- Protein Atlas: https://www.proteinatlas.org/ENSG00000173418-NAA20
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22NAA20%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/P61599
- STRING: https://string-db.org/network/9606.ENSG00000173418
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P61599


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[NAA20-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NAA20/NAA20-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P61599 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 2..157; /note="N-acetyltransferase"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00532" |
| InterPro | IPR016181;IPR000182;IPR051646; |
| Pfam | PF00583; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000173418-NAA20/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| NAA25 | Intact, Biogrid | true |
| HNRNPA2B1 | Biogrid | false |
| IKBKB | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
