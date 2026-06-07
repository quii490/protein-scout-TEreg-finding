---
type: protein-evaluation
gene: "DSN1"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DSN1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DSN1 / DSN1 |
| 蛋白大小 | 356 aa |
| UniProt ID | Q9H410 |
| 蛋白名称 | Kinetochore-associated protein DSN1 homolog |
| 评估日期 | 2026-05-29 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | UniProt Nucleus (唯一注释) |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 356 aa (200–800 aa, 适宜生化实验) |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed=33篇 (非常新颖) |
| 🏗️ 三维结构 | 10/10 | ×3 | 30 | PDB实验结构 (5条目) — 实验验证 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | 新颖蛋白 (PubMed≤50) — 无注释域基线, 可能存在新域 |
| 🔗 PPI 网络 | 4/10 | ×3 | 12 | 少量IntAct物理互作 (2条) |
| ➕ 互证加分 | — | max +3 | +1 | PDB多条目实验结构确认 (+1.0) |
| **原始总分** |  |  | **135/183** |  |
| **归一化总分** |  |  | **73.8/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| UniProt | Nucleus; Chromosome, centromere, kinetochore | TrEMBL/Swiss-Prot |
| Protein Atlas (IF) | HEL, Rh30 | Supported (HPA)


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/chromatin/DSN1/IF_images/DSN1_HEL_61.jpg|DSN1_HEL_61]]
![[Projects/TEreg-finding/protein-interested/detail/chromatin/DSN1/IF_images/DSN1_HEL_62.jpg|DSN1_HEL_62]]



**结论**: UniProt Nucleus (唯一注释)

#### 3.2 蛋白大小评估

356 aa 蛋白。**评价**: 356 aa (200–800 aa, 适宜生化实验)

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 33 |
| 新颖性分级 | 非常新颖 |

**关键文献**:
1. Yatskevich et al. (2024). "Structure of the human outer kinetochore KMN network complex.". *Nat Struct Mol Biol*. PMID: 38459127
2. Xue et al. (2026). "TRMT6-directed m(1)A modification initiates lung squamous cell carcinoma via YTHDF3-stabilized cell cycle genes.". *NPJ Precis Oncol*. PMID: 41803297
3. Xu et al. (2025). "A Comprehensive Analysis of the Role of DSN1 in Pan-Cancer Prognosis and Immunotherapy.". *J Cancer*. PMID: 40535813
4. Przewloka et al. (2009). "Searching for Drosophila Dsn1 kinetochore protein.". *Cell Cycle*. PMID: 19270503
5. Bonner et al. (2019). "Enrichment of Aurora B kinase at the inner kinetochore controls outer kinetochore assembly.". *J Cell Biol*. PMID: 31527147
**评价**: PubMed 共 33 篇文献，属于**非常新颖**。研究空间充足，适合作为创新课题。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | None |
| 有序区域 (pLDDT>70) 占比 | None% |
| 高置信度 (pLDDT>90) 占比 | None% |
| 可用 PDB 条目 | 5LSI; 5LSJ; 5LSK; 8PPR; 8Q5H |

**评价**: PDB实验结构 (5条目) — 实验验证


**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/chromatin/DSN1/DSN1-PAE.png]]

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| UniProt | 无注释结构域 |
| GO Molecular Function | Part of the MIS12 complex which is required for normal chromosome alignment and segregation and kinetochore formation during mitosis |

**染色质调控潜力分析**: 新颖蛋白 (PubMed≤50) — 无注释域基线, 可能存在新域

#### 3.6 PPI 网络

**实验验证互作** (IntAct physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| P40568 | two hybrid array | 14690591 | - | - |
| Q12143 | pull down | 14690591 | - | - |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| 无高置信度STRING互作 | - | - | - |

**已知复合体成员** (GO Cellular Component):
- 无已知复合体注释


**PPI 互证分析**:
- （待补充：综合 STRING、IntAct 和 GO 数据库的互作信息，分析 PPI 网络的一致性）
**评价**: 少量IntAct物理互作 (2条)

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | pLDDT=None, PDB:5条目 | 一致 |
| 结构域 | UniProt | 0个注释域 | N/A |
| PPI | STRING + IntAct | IntAct:30, STRING:25 | 一致 |
| 定位 | UniProt | Nucleus | 是 |

**互证加分明细**:
- PDB多条目实验结构确认 (+1.0)
**总分**: +1 / max +3

### 4. 总体评价

**推荐等级**: ★★★★ (73.8/100)

**核心优势**:
1. 非常新颖 (PubMed=33篇)
2. UniProt Nucleus (唯一注释)
3. 新颖蛋白 (PubMed≤50) — 无注释域基线, 可能存在新域

**风险/不确定性**:
1. 无 Protein Atlas IF 实验验证
2. 无 AlphaFold 高质量结构或结构待验证

**下一步建议**:
- [ ] Protein Atlas IF 实验验证核定位
- [ ] AlphaFold 结构预测分析
- [ ] Co-IP/MS 验证PPI网络

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H410
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DSN1
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[DSN1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/chromatin/DSN1/DSN1-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H410 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR013218; |
| Pfam | PF08202; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000149636-DSN1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CBX1 | Biogrid, Opencell | true |
| CBX5 | Biogrid, Bioplex | true |
| MIS12 | Intact, Biogrid, Opencell, Bioplex | true |
| NDC80 | Biogrid, Bioplex | true |
| NSL1 | Intact, Biogrid, Bioplex | true |
| NUF2 | Biogrid, Opencell, Bioplex | true |
| SPC24 | Biogrid, Bioplex | true |
| SPC25 | Biogrid, Bioplex | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
