---
type: protein-evaluation
gene: "C1D"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## C1D 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | C1D / 核核酸结合蛋白C1D |
| 蛋白大小 | 141 aa / 16.0 kDa |
| UniProt ID | Q13901 |
| 评估日期 | 2026-05-29 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | Nucleus; Cytoplasm; Nucleus, nucleolus |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 141 aa / 16.0 kDa |
| 🆕 研究新颖性 | 4/10 | ×5 | 30 | PubMed 70 篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | No PDB. Small protein (141aa), AlphaFold available but no experimental structure |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | No annotated domains. RNA exosome recruitment factor. Novel protein, baseline 7. |
| 🔗 PPI 网络 | 6/10 | ×3 | 18 | RNA exosome: EXOSC10(0.999), EXOSC9(0.999), EXOSC1-8(all 0.999), MTREX(0.999), D |
| ➕ 互证加分 | — | max +3 | 1 | Nucleolar localization + exosome complex PPI consistent. |
|  | **原始总分** |  | **109/183** | **106.0/183** |  |  |
|  | **归一化总分** |  | **59.6/100** | **57.9/100** |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| UniProt | Nucleus; Cytoplasm; Nucleus, nucleolus | Swiss-Prot |
| Protein Atlas (IF) | nucleoplasm+nucleoli (Approved, A-431) | Approved |

![[Projects/TEreg-finding/protein-interested/detail/nucleolus/C1D/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/C1D/IF_images/A-431_2.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/C1D/IF_images/U-251MG_1.jpg|U-251MG]]

**结论**: Nucleus; Cytoplasm; Nucleus, nucleolus。C1D定位于Nucleus，在多个数据库中确认核定位。

#### 3.2 蛋白大小评估

**评价**: 141 aa (16.0 kDa)，大小合适。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 70 |
| 主要研究方向 | RNA exosome recruitment to pre-rRNA |

**评价**: PubMed 70 篇，有一定研究基础但仍有niche空间。

**关键文献**:
1. Spira AI et al. (2025). "Preventing Infusion-Related Reactions With Intravenous Amivantamab-Results From SKIPPirr, a Phase 2 Study: A Brief Report". *J Thorac Oncol*. PMID: 39864547
2. Wohlgemuth K et al. (2024). "Pathogenic variants in CFAP46, CFAP54, CFAP74 and CFAP221 cause primary ciliary dyskinesia with a defective C1d projection of the central apparatus". *Eur Respir J*. PMID: 39362668
3. Mitchell P (2010). "Rrp47 and the function of the Sas10/C1D domain". *Biochem Soc Trans*. PMID: 20659009
4. Ortiz-Fernández L & Sawalha AH (2019). "Genetics of Antiphospholipid Syndrome". *Curr Rheumatol Rep*. PMID: 31807905
5. Jackson RA et al. (2016). "C1D family proteins in coordinating RNA processing, chromosome condensation and DNA damage response". *Cell Div*. PMID: 27030795
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| 可用 PDB 条目 | 无 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/C1D/C1D-PAE.png]]

**评价**: No PDB. Small protein (141aa), AlphaFold available but no experimental structure.

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| UniProt | No annotated domains. RNA exosome recruitment factor. Novel protein, baseline 7. |

**染色质调控潜力分析**: No annotated domains. RNA exosome recruitment factor. Novel protein, baseline 7.

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.7):

RNA exosome: EXOSC10(0.999), EXOSC9(0.999), EXOSC1-8(all 0.999), MTREX(0.999), DIS3(0.997). RNA processing, nucleolar.

**实验验证互作** (IntAct):

RNA exosome: EXOSC10(0.999), EXOSC9(0.999), EXOSC1-8(all 0.999), MTREX(0.999), DIS3(0.997). RNA processing, nucleolar.

**已知复合体成员** (GO Cellular Component):
- UniProt GO-CC 核相关注释根据实际查询结果获取。

**PPI 互证分析**:
RNA exosome: EXOSC10(0.999), EXOSC9(0.999), EXOSC1-8(all 0.999), MTREX(0.999), DIS3(0.997). RNA processing, nucleolar.

**评价**: PPI网络部分涉及转录/染色质调控

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 无PDB结构 | 预测为主 |
| 定位 | UniProt / GO | Nucleus; Cytoplasm; Nucleus, nucleolus | 一致 |
| PPI | STRING + IntAct | 见3.6节 | 部分一致 |

**互证加分明细**:
Nucleolar localization + exosome complex PPI consistent.

**总分**: +1 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. RNA exosome recruitment to pre-rRNA
2. 蛋白功能独特

**风险/不确定性**:
1. IF图像数据待补充
2. 研究已有一定基础

**下一步建议**:
- [ ] 获取 Protein Atlas IF 图像确认核定位
- [ ] 查阅最新5篇关键文献
- [ ] 设计体外DNA/染色质结合实验

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13901
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=C1D


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[C1D-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/C1D/C1D-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q13901 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR011082;IPR007146; |
| Pfam | PF04000; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000197223-C1D/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| EXOSC1 | Biogrid, Bioplex | true |
| EXOSC10 | Intact, Biogrid | true |
| EXOSC5 | Biogrid, Bioplex | true |
| RBM7 | Biogrid, Bioplex | true |
| CASP6 | Intact | false |
| DIS3 | Bioplex | false |
| EXOSC2 | Bioplex | false |
| EXOSC3 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
