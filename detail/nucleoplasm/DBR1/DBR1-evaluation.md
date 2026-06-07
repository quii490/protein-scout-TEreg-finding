---
type: protein-evaluation
gene: "DBR1"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DBR1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DBR1 / DBR1 |
| 蛋白大小 | 544 aa |
| UniProt ID | Q9UK59 |
| 蛋白名称 | Lariat debranching enzyme |
| 评估日期 | 2026-05-29 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | UniProt Nucleus (唯一注释) |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 544 aa (200–800 aa, 适宜生化实验) |
| 🆕 研究新颖性 | 6/10 | ×5 | 30 | PubMed=59篇 (有一定研究) |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | 新颖蛋白 (PubMed≤100) — 无结构基线, 不扣分 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | PubMed≤100 — 无注释域基线 |
| 🔗 PPI 网络 | 6/10 | ×3 | 18 | IntAct实验物理互作 (9条co-IP/pull-down) |
| ➕ 互证加分 | — | max +3 | +0.5 | IntAct实验互作确认 (+0.5) |
| **原始总分** |  |  | **118.5/183** |  |
| **归一化总分** |  |  | **64.8/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| UniProt | Nucleus | TrEMBL/Swiss-Prot |
| Protein Atlas (IF) | A-431, U-251MG | Supported (HPA)


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/DBR1/IF_images/DBR1_A_431_1.jpg|DBR1_A_431_1]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/DBR1/IF_images/DBR1_A_431_2.jpg|DBR1_A_431_2]]



**结论**: UniProt Nucleus (唯一注释)

#### 3.2 蛋白大小评估

544 aa 蛋白。**评价**: 544 aa (200–800 aa, 适宜生化实验)

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 59 |
| 新颖性分级 | 有一定研究 |

**评价**: PubMed 共 59 篇文献，属于**有一定研究**。研究空间充足，适合作为创新课题。

**关键文献**:
1. Karch CM & Goate AM (2015). "Alzheimer's disease risk genes and mechanisms of disease pathogenesis". *Biol Psychiatry*. PMID: 24951455
2. Chan YH et al. (2024). "SARS-CoV-2 brainstem encephalitis in human inherited DBR1 deficiency". *J Exp Med*. PMID: 39023559
3. Buerer L et al. (2024). "The debranching enzyme Dbr1 regulates lariat turnover and intron splicing". *Nat Commun*. PMID: 38816363
4. Wu C et al. (2024). "Sequestration of DBR1 to stress granules promotes lariat intronic RNAs accumulation for heat-stress tolerance". *Nat Commun*. PMID: 39227617
5. Duan C et al. (2024). "Elevated levels of intracellular RNA lariats suppress the antiviral response". *bioRxiv*. PMID: 39677789
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
| GO Molecular Function | Cleaves the 2'-5' phosphodiester linkage at the branch point of excised lariat intron RNA and converts them into linear molecules that can be subseque |

**染色质调控潜力分析**: PubMed≤100 — 无注释域基线

#### 3.6 PPI 网络

**实验验证互作** (IntAct physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| Q9VSD7 | two hybrid | 14605208 | - | - |
| intact:EBI | pull down | 23902751 | - | - |
| Q8D008 | two hybrid pooling approach | 20711500 | - | - |
| Q96QZ7 | anti tag coimmunoprecipitation | 28514442 | - | - |
| Q9UK59 | anti tag coimmunoprecipitation | 28514442 | - | - |
| Q5S007 | anti tag coimmunoprecipitation | 31046837 | - | - |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| 无高置信度STRING互作 | - | - | - |

**已知复合体成员** (GO Cellular Component):
- 无已知复合体注释

**评价**: IntAct实验物理互作 (9条co-IP/pull-down)

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | pLDDT=None, PDB:0条目 | 无实验结构 |
| 结构域 | UniProt | 0个注释域 | N/A |
| PPI | STRING + IntAct | IntAct:30, STRING:25 | 一致 |
| 定位 | UniProt | Nucleus | 是 |

**互证加分明细**:
- IntAct实验互作确认 (+0.5)
**总分**: +0.5 / max +3

**PAE 图**: 暂无PAE数据

### 4. 总体评价

**推荐等级**: ★★★ (64.8/100)

**核心优势**:
1. 有一定研究 (PubMed=59篇)
2. UniProt Nucleus (唯一注释)
3. PubMed≤100 — 无注释域基线

**风险/不确定性**:
1. 无 Protein Atlas IF 实验验证
2. 无 AlphaFold 高质量结构或结构待验证

**下一步建议**:
- [ ] Protein Atlas IF 实验验证核定位
- [ ] AlphaFold 结构预测分析
- [ ] Co-IP/MS 验证PPI网络

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UK59
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DBR1
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
| UniProt | Q9UK59 |
| SMART | SM01124; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR004843;IPR007708;IPR041816;IPR029052; |
| Pfam | PF05011;PF00149; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000138231-DBR1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CSNK1A1 | Biogrid, Opencell | true |
| MPLKIP | Bioplex | false |
| PLK1 | Biogrid | false |
| PRKN | Biogrid | false |
| TBP | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
