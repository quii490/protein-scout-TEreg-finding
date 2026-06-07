---
type: protein-evaluation
gene: "DMRTA2"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DMRTA2 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DMRTA2 / DMRTA2 |
| 蛋白大小 | 542 aa |
| UniProt ID | Q96SC8 |
| 蛋白名称 | Doublesex- and mab-3-related transcription factor A2 |
| 评估日期 | 2026-05-29 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 9/10 | ×4 | 36 | UniProt Nucleus (唯一注释) + 转录因子/同源盒/DNA结合蛋白 — 高可信度核定位 |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 542 aa (200–800 aa, 适宜生化实验) |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed=33篇 (非常新颖) |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | 新颖蛋白 (PubMed≤100) — 无结构基线, 不扣分 |
| 🧬 调控结构域 | 10/10 | ×2 | 20 | DM DNA结合结构域 (DMRT家族) — 转录因子 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | 低置信度STRING关联 (11条) |
| ➕ 互证加分 | — | max +3 | +1 | 核定位+转录因子功能一致 (+1.0) |
| **原始总分** |  |  | **134/183** |  |
| **归一化总分** |  |  | **73.2/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| UniProt | Nucleus | TrEMBL/Swiss-Prot |
| Protein Atlas (IF) | Rh30, SH-SY5Y | Supported (HPA)


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/DMRTA2/IF_images/DMRTA2_Rh30_1.jpg|DMRTA2_Rh30_1]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/DMRTA2/IF_images/DMRTA2_Rh30_14.jpg|DMRTA2_Rh30_14]]

**结论**: UniProt Nucleus (唯一注释) + 转录因子/同源盒/DNA结合蛋白 — 高可信度核定位

#### 3.2 蛋白大小评估

542 aa 蛋白。**评价**: 542 aa (200–800 aa, 适宜生化实验)

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 33 |
| 新颖性分级 | 非常新颖 |

**评价**: PubMed 共 33 篇文献，属于**非常新颖**。研究空间充足，适合作为创新课题。

**关键文献**:
1. Maleszewska M et al. (2024). "DMRTA2 supports glioma stem-cell mediated neovascularization in glioblastoma". *Cell Death Dis*. PMID: 38509074
2. Shen X et al. (2025). "Evidence That Dmrta2 Acts through Repression of Pax6 in Cortical Patterning and Identification of a Mutation Impairing DNA Recognition Associated with Microcephaly in Human". *eNeuro*. PMID: 40541527
3. Anirudhan J et al. (2025). "Novel Insights into Emx2 and Dmrta2 Cooperation during Cortex Development and Evidence for Dmrta2 Function in the Choroid Plexus". *J Neurosci*. PMID: 40456611
4. Young FI et al. (2017). "The doublesex-related Dmrta2 safeguards neural progenitor maintenance involving transcriptional regulation of Hes1". *Proc Natl Acad Sci U S A*. PMID: 28655839
5. Xu S et al. (2013). "Zebrafish dmrta2 regulates the expression of cdkn2c in spermatogenesis in the adult testis". *Biol Reprod*. PMID: 23175770
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
| GO Molecular Function | May be involved in sexual development |

**染色质调控潜力分析**: DM DNA结合结构域 (DMRT家族) — 转录因子

#### 3.6 PPI 网络

**实验验证互作** (IntAct physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| 无实验验证物理互作 | - | - | - | - |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| 无高置信度STRING互作 | - | - | - |

**已知复合体成员** (GO Cellular Component):
- 无已知复合体注释

**评价**: 低置信度STRING关联 (11条)

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | pLDDT=None, PDB:0条目 | 无实验结构 |
| 结构域 | UniProt | 0个注释域 | N/A |
| PPI | STRING + IntAct | IntAct:0, STRING:11 | 一致 |
| 定位 | UniProt | Nucleus | 是 |

**互证加分明细**:
- 核定位+转录因子功能一致 (+1.0)
**总分**: +1 / max +3

**PAE 图**: 暂无PAE数据

### 4. 总体评价

**推荐等级**: ★★★★ (73.2/100)

**核心优势**:
1. 非常新颖 (PubMed=33篇)
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
- UniProt: https://www.uniprot.org/uniprotkb/Q96SC8
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DMRTA2
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
| UniProt | Q96SC8 |
| SMART | SM00301; |
| UniProt Domain [FT] | DOMAIN 314..349; /note="DMA"; /evidence="ECO:0000255" |
| InterPro | IPR001275;IPR036407;IPR005173;IPR026607;IPR046472;IPR009060; |
| Pfam | PF00751;PF03474;PF20624; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000142700-DMRTA2/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
