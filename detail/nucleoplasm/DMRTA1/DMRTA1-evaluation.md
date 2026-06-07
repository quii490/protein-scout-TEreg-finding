---
type: protein-evaluation
gene: "DMRTA1"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DMRTA1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DMRTA1 / DMRTA1 |
| 蛋白大小 | 504 aa |
| UniProt ID | Q5VZB9 |
| 蛋白名称 | Doublesex- and mab-3-related transcription factor A1 |
| 评估日期 | 2026-05-29 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 9/10 | ×4 | 36 | UniProt Nucleus (唯一注释) + 转录因子/同源盒/DNA结合蛋白 — 高可信度核定位 |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 504 aa (200–800 aa, 适宜生化实验) |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed=17篇 (极度新颖) |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | 新颖蛋白 (PubMed≤100) — 无结构基线, 不扣分 |
| 🧬 调控结构域 | 10/10 | ×2 | 20 | DM DNA结合结构域 (DMRT家族) — 转录因子 |
| 🔗 PPI 网络 | 4/10 | ×3 | 12 | 少量IntAct物理互作 (2条) |
| ➕ 互证加分 | — | max +3 | +1 | 核定位+转录因子功能一致 (+1.0) |
| **原始总分** |  |  | **147/183** |  |
| **归一化总分** |  |  | **80.3/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| UniProt | Nucleus | TrEMBL/Swiss-Prot |
| Protein Atlas (IF) | HeLa, PC-3 | Supported (HPA)


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/DMRTA1/IF_images/DMRTA1_HeLa_2.jpg|DMRTA1_HeLa_2]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/DMRTA1/IF_images/DMRTA1_HeLa_3.jpg|DMRTA1_HeLa_3]]



**结论**: UniProt Nucleus (唯一注释) + 转录因子/同源盒/DNA结合蛋白 — 高可信度核定位

#### 3.2 蛋白大小评估

504 aa 蛋白。**评价**: 504 aa (200–800 aa, 适宜生化实验)

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 17 |
| 新颖性分级 | 极度新颖 |

**评价**: PubMed 共 17 篇文献，属于**极度新颖**。研究空间充足，适合作为创新课题。

**关键文献**:
1. Bajpai P et al. (2025). "Defining molecular signatures of the solid/pseudopapillary and pseudoglandular patterns in so-called "solid-tubulocystic intrahepatic cholangiocarcinoma vs. NIPBL::NACC1 fusion hepatic carcinoma"". *Pathol Res Pract*. PMID: 40286787
2. Zhou Y et al. (2022). "Genome-wide Scan of Dental Fear and Anxiety Nominates Novel Genes". *J Dent Res*. PMID: 35771046
3. Zhang R et al. (2023). "The DMRTA1-SOX2 positive feedback loop promotes progression and chemotherapy resistance of esophageal squamous cell carcinoma". *Oncol Res*. PMID: 37744275
4. Kikkawa T et al. (2020). "Dmrt genes participate in the development of Cajal-Retzius cells derived from the cortical hem in the telencephalon". *Dev Dyn*. PMID: 32012381
5. Nickerson ML et al. (2017). "Molecular analysis of urothelial cancer cell lines for modeling tumor biology and drug response". *Oncogene*. PMID: 27270441
#### 3.4 三维结构分析

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | None |
| 有序区域 (pLDDT>70) 占比 | None% |
| 高置信度 (pLDDT>90) 占比 | None% |
| 可用 PDB 条目 | 无 |

**评价**: 新颖蛋白 (PubMed≤100) — 无结构基线, 不扣分

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| UniProt | 无注释结构域 |
| GO Molecular Function | 无 |

**染色质调控潜力分析**: DM DNA结合结构域 (DMRT家族) — 转录因子

#### 3.6 PPI 网络

**实验验证互作** (IntAct physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| Q5VZB9 | two hybrid | 21988832 | - | - |
| P51692 | two hybrid | 21988832 | - | - |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| 无高置信度STRING互作 | - | - | - |

**已知复合体成员** (GO Cellular Component):
- 无已知复合体注释

**评价**: 少量IntAct物理互作 (2条)

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | pLDDT=None, PDB:0条目 | 无实验结构 |
| 结构域 | UniProt | 0个注释域 | N/A |
| PPI | STRING + IntAct | IntAct:12, STRING:0 | 一致 |
| 定位 | UniProt | Nucleus | 是 |

**互证加分明细**:
- 核定位+转录因子功能一致 (+1.0)
**总分**: +1 / max +3

**PAE 图**: 暂无PAE数据

### 4. 总体评价

**推荐等级**: ★★★★ (80.3/100)

**核心优势**:
1. 极度新颖 (PubMed=17篇)
2. UniProt Nucleus (唯一注释) + 转录因子/同源盒/DNA结合蛋白 — 高可信度核定位
3. DM DNA结合结构域 (DMRT家族) — 转录因子

**风险/不确定性**:
1. 无 Protein Atlas IF 实验验证
2. 无 AlphaFold 高质量结构或结构待验证

**下一步建议**:
- [ ] Protein Atlas IF 实验验证核定位
- [ ] AlphaFold 结构预测分析
- [ ] Co-IP/MS 验证PPI网络

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5VZB9
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DMRTA1
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q5VZB9 |
| SMART | SM00301; |
| UniProt Domain [FT] | DOMAIN 327..362; /note="DMA"; /evidence="ECO:0000255" |
| InterPro | IPR001275;IPR036407;IPR005173;IPR026607;IPR046472;IPR009060; |
| Pfam | PF00751;PF03474;PF20624; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000176399-DMRTA1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| RNF11 | Intact | false |
| WFS1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
