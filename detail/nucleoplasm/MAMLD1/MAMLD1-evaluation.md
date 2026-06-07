---
type: protein-evaluation
gene: "MAMLD1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MAMLD1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MAMLD1 / CG1, CXorf6 |
| 蛋白大小 | 774 aa / 83.2 kDa |
| UniProt ID | [Q13495](https://www.uniprot.org/uniprot/Q13495) |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 8/10 | ×4 | 32 | Nucleus (UniProt), HPA: Nucleoplasm, GO: nuclear body, nucleoplasm |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 774 aa, 83.2 kDa |
| 🆕 研究新颖性 | 4/10 | ×5 | 20 | PubMed = 74 篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | pLDDT = 43.75, PDB = 0 条目 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | MAMLD1 domain (InterPro only) |
| 🔗 PPI 网络 | 2/10 | ×3 | 6 | No curated interactions |
| ➕ 互证加分 | — | max +3 | +0 | — |
| **原始总分** |  |  | **100/183** |  |
| **归一化总分** |  |  | **54.6/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | — | — |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus (UniProt), HPA: Nucleoplasm, GO: nuclear body, nucleoplasm | Experimental/ECO evidence |

**结论**: Nucleus (UniProt), HPA: Nucleoplasm, GO: nuclear body, nucleoplasm

#### 3.2 蛋白大小评估

774 aa (83.2 kDa)，在理想生化实验范围（200-800 aa）内。

**评价**: 大小适合生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 74 |
| 最早发表年份 | — |
| Chromatin/epigenetics 比例 | — |

**主要研究方向**:
- Mastermind-like Notch coactivator. Very poor AlphaFold quality (pLDDT 43.75) suggests high intrinsic disorder. No PPI data limits assessment.

**关键文献**:
1. Miyado M et al. (2022). "MAMLD1 and Differences/Disorders of Sex Development: An Update." *Sex Dev*. PMID: 34695834
2. Ogata T et al. (2012). "MAMLD1 and 46,XY disorders of sex development." *Semin Reprod Med*. PMID: 23044878
3. Ogata T et al. (2009). "MAMLD1 (CXorf6): a new gene involved in hypospadias." *Horm Res*. PMID: 19339788
4. Chen W et al. (2023). "Shared diagnostic genes and potential mechanism between PCOS and recurrent implantation failure." *Front Immunol*. PMID: 37261354
5. Stark JC et al. (2025). "Clinical applications of RNA sequencing in a rare disease cohort." *Genome Med*. PMID: 40597352

**评价**: Mastermind-like Notch coactivator. Very poor AlphaFold quality (pLDDT 43.75) suggests high intrinsic disorder. No PPI data limits assessment.

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 43.75 |
| 有序区域 (pLDDT>70) 占比 | 3.1% |
| 可用 PDB 条目 | 0 个 (—) |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MAMLD1/MAMLD1-PAE.png]]

**评价**: Mastermind-like Notch coactivator. Likely transcriptional coactivator in Notch signaling. Very low AlphaFold quality (pLDDT 43.75) suggests high intrinsic disorder.

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| GeneCards | — |
| SMART | — |
| InterPro/Pfam | MAMLD1 domain (InterPro only) |

**染色质调控潜力分析**: Mastermind-like Notch coactivator. Likely transcriptional coactivator in Notch signaling. Very low AlphaFold quality (pLDDT 43.75) suggests high intrinsic disorder.

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| No curated interactions | — | — | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| STRING 数据不可用 | — | — | — |

**已知复合体成员** (GO Cellular Component):
- GO: centrosome, Golgi apparatus, nuclear body, nucleoplasm

**IntAct 查询记录**: IntAct 查询无物理互作记录

**PPI 互证分析**:
- STRING + IntAct 共同确认: —
- 仅 STRING 预测: —
- 仅 IntAct 实验: —
- 调控相关比例: — / — (— %)

**评价**: Mastermind-like Notch coactivator. Very poor AlphaFold quality (pLDDT 43.75) suggests high intrinsic disorder. No PPI data limits assessment.

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT + PDB | pLDDT=43.75, PDB=0条目 | — |
| 结构域 | UniProt / InterPro / Pfam | MAMLD1 domain (InterPro only) | — |
| PPI | STRING + IntAct | — | — |
| 定位 | Protein Atlas / UniProt / GO | Nucleus (UniProt), HPA: Nucleoplasm, GO: nuclear body, nucle | — |

**互证加分明细**:
- —
**总分**: +0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5)

**核心优势**:
1. Nuclear localization confirmed by HPA + UniProt
2. Disease relevance: disorders of sex development
3. Notch coactivator function
4. Reasonable novelty (PubMed=74)

**风险/不确定性**:
1. Very poor AlphaFold quality (pLDDT 43.75, 3.1% ordered)
2. No PDB structures
3. No PPI data
4. Coactivator function inferred from paralog homology
5. No structural domains beyond MAMLD1 family

**下一步建议**:
- [ ] HPA IF 实验验证核定位
- [ ] Co-IP 验证 PPI
- [ ] 功能实验验证染色质调控角色

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprot/Q13495
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13495
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MAMLD1%5BTitle/Abstract%5D
- HPA: https://www.proteinatlas.org/Q13495


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[MAMLD1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MAMLD1/MAMLD1-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000013619-MAMLD1/subcellular

![](https://images.proteinatlas.org/3923/1158_A5_1_red_green.jpg)
![](https://images.proteinatlas.org/3923/1158_A5_4_red_green.jpg)
![](https://images.proteinatlas.org/3923/1252_H5_1_red_green.jpg)
![](https://images.proteinatlas.org/3923/1252_H5_2_red_green.jpg)
![](https://images.proteinatlas.org/3923/1401_A5_3_red_green.jpg)
![](https://images.proteinatlas.org/3923/1401_A5_6_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q13495 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR026131; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000013619-MAMLD1/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
