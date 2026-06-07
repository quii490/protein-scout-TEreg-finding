---
type: protein-evaluation
gene: "DET1"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DET1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DET1 / DET1 |
| 蛋白大小 | 550 aa |
| UniProt ID | Q7L5Y6 |
| 蛋白名称 | DET1 homolog |
| 评估日期 | 2026-05-29 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | UniProt Nucleus (唯一注释) |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 550 aa (200–800 aa, 适宜生化实验) |
| 🆕 研究新颖性 | 6/10 | ×5 | 40 | PubMed=42篇 (非常新颖) |
| 🏗️ 三维结构 | 9/10 | ×3 | 27 | PDB实验结构 (2条目) |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | 新颖蛋白 (PubMed≤50) — 无注释域基线, 可能存在新域 |
| 🔗 PPI 网络 | 6/10 | ×3 | 18 | IntAct实验物理互作 (14条co-IP/pull-down) |
| ➕ 互证加分 | — | max +3 | +1 | PDB实验结构确认 (+0.5); IntAct实验互作确认 (+0.5) |
|  | **原始总分** |  | **127.5/183** | **127.0/183** |  |  |  |
|  | **归一化总分** |  | **69.7/100** | **69.4/100** |  |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| UniProt | Nucleus | TrEMBL/Swiss-Prot |
| Protein Atlas (IF) | A-549, SK-MEL-30 | Supported (HPA)


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/DET1/IF_images/DET1_A_549_2.jpg|DET1_A_549_2]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/DET1/IF_images/DET1_A_549_3.jpg|DET1_A_549_3]]



**结论**: UniProt Nucleus (唯一注释)

#### 3.2 蛋白大小评估

550 aa 蛋白。**评价**: 550 aa (200–800 aa, 适宜生化实验)

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 42 |
| 新颖性分级 | 非常新颖 |

**评价**: PubMed 共 42 篇文献，属于**非常新颖**。研究空间充足，适合作为创新课题。

**关键文献**:
1. Karayel O et al. (2025). "Impairment of DET1 causes neurological defects and lethality in mice and humans". *Proc Natl Acad Sci U S A*. PMID: 39937864
2. Kaur N et al. (2013). "Peroxisomes and photomorphogenesis". *Subcell Biochem*. PMID: 23821150
3. Ndoja A et al. (2025). "COP1 Deficiency in BRAF(V600E) Melanomas Confers Resistance to Inhibitors of the MAPK Pathway". *Cells*. PMID: 40643496
4. Burgess AE et al. (2025). "DET1 dynamics underlie cooperative ubiquitination by CRL4(DET1-COP1) complexes". *Sci Adv*. PMID: 40009677
5. Kang MY et al. (2015). "Negative regulatory roles of DE-ETIOLATED1 in flowering time in Arabidopsis". *Sci Rep*. PMID: 25962685
#### 3.4 三维结构分析

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | None |
| 有序区域 (pLDDT>70) 占比 | None% |
| 高置信度 (pLDDT>90) 占比 | None% |
| 可用 PDB 条目 | 9BJZ; 9DHD |

**评价**: PDB实验结构 (2条目)

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| UniProt | 无注释结构域 |
| GO Molecular Function | Component of the E3 ubiquitin ligase DCX DET1-COP1 complex, which is required for ubiquitination and subsequent degradation of target proteins. The co |

**染色质调控潜力分析**: 新颖蛋白 (PubMed≤50) — 无注释域基线, 可能存在新域

#### 3.6 PPI 网络

**实验验证互作** (IntAct physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| Q99288 | two hybrid | 18719252 | - | - |
| Q9LJD7 | pull down | 16844902 | - | - |
| intact:EBI | anti tag coimmunoprecipitation | 12225661 | - | - |
| P32502 | two hybrid | 18719252 | - | - |
| Q9M0V3 | two hybrid | 16792691 | - | - |
| Q9ZNU6 | pull down | 16792691 | - | - |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| 无高置信度STRING互作 | - | - | - |

**已知复合体成员** (GO Cellular Component):
- 无已知复合体注释

**评价**: IntAct实验物理互作 (14条co-IP/pull-down)

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | pLDDT=None, PDB:2条目 | 一致 |
| 结构域 | UniProt | 0个注释域 | N/A |
| PPI | STRING + IntAct | IntAct:30, STRING:25 | 一致 |
| 定位 | UniProt | Nucleus | 是 |

**互证加分明细**:
- PDB实验结构确认 (+0.5)
- IntAct实验互作确认 (+0.5)
**总分**: +1 / max +3

**PAE 图**: 暂无PAE数据

### 4. 总体评价

**推荐等级**: ★★★★ (75.4/100)

**核心优势**:
1. 非常新颖 (PubMed=42篇)
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
- UniProt: https://www.uniprot.org/uniprotkb/Q7L5Y6
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DET1
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q7L5Y6 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR019138; |
| Pfam | PF09737; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000140543-DET1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| COPS5 | Biogrid, Bioplex | true |
| COPS7A | Biogrid, Bioplex | true |
| COPS7B | Biogrid, Bioplex | true |
| DDA1 | Biogrid, Bioplex | true |
| DDB1 | Biogrid, Bioplex | true |
| TRIB1 | Biogrid, Bioplex | true |
| TRIB2 | Biogrid, Bioplex | true |
| UBE2E1 | Biogrid, Bioplex | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
