---
type: protein-evaluation
gene: "DNTT"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DNTT 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DNTT / DNTT |
| 蛋白大小 | 509 aa |
| UniProt ID | P04053 |
| 蛋白名称 | DNA nucleotidylexotransferase |
| 评估日期 | 2026-05-29 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | UniProt Nucleus (唯一注释) |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 509 aa (200–800 aa, 适宜生化实验) |
| 🆕 研究新颖性 | 6/10 | ×5 | 30 | PubMed=53篇 (有一定研究) |
| 🏗️ 三维结构 | 9/10 | ×3 | 27 | PDB实验结构 (2条目) |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | PubMed≤100 — 无注释域基线 |
| 🔗 PPI 网络 | 6/10 | ×3 | 18 | IntAct实验物理互作 (5条co-IP/pull-down) |
| ➕ 互证加分 | — | max +3 | +1 | PDB实验结构确认 (+0.5); IntAct实验互作确认 (+0.5) |
| **原始总分** |  |  | **127.5/183** |  |
| **归一化总分** |  |  | **69.7/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| UniProt | Nucleus | TrEMBL/Swiss-Prot |
| Protein Atlas (IF) | REH, A-431 | Supported (HPA)


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/DNTT/IF_images/DNTT_REH_1.jpg|DNTT_REH_1]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/DNTT/IF_images/DNTT_REH_3.jpg|DNTT_REH_3]]



**结论**: UniProt Nucleus (唯一注释)

#### 3.2 蛋白大小评估

509 aa 蛋白。**评价**: 509 aa (200–800 aa, 适宜生化实验)

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 53 |
| 新颖性分级 | 有一定研究 |

**评价**: PubMed 共 53 篇文献，属于**有一定研究**。研究空间充足，适合作为创新课题。

**关键文献**:
1. Fedl AS et al. (2024). "Transcriptional function of E2A, Ebf1, Pax5, Ikaros and Aiolos analyzed by in vivo acute protein degradation in early B cell development". *Nat Immunol*. PMID: 39179932
2. Escherich CS et al. (2025). "DNTT-mediated DNA damage response drives inotuzumab ozogamicin resistance in B-cell acute lymphoblastic leukemia". *Blood*. PMID: 39791601
3. Chalabi S et al. (2022). "Temporal Gene Expression Profiles Reflect the Dynamics of Lymphoid Differentiation". *Int J Mol Sci*. PMID: 35163045
4. Lee Y et al. (2022). "Dual-channel P-type ternary DNTT-graphene barristor". *Sci Rep*. PMID: 36371420
5. Zhao Y et al. (2024). "Genomic determinants of response and resistance to inotuzumab ozogamicin in B-cell ALL". *Blood*. PMID: 38551807
#### 3.4 三维结构分析

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | None |
| 有序区域 (pLDDT>70) 占比 | None% |
| 高置信度 (pLDDT>90) 占比 | None% |
| 可用 PDB 条目 | 2COE; 5W4E |

**评价**: PDB实验结构 (2条目)

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| UniProt | 无注释结构域 |
| GO Molecular Function | Template-independent DNA polymerase which catalyzes the random addition of deoxynucleoside 5'-triphosphate to the 3'-end of a DNA initiator. One of th |

**染色质调控潜力分析**: PubMed≤100 — 无注释域基线

#### 3.6 PPI 网络

**实验验证互作** (IntAct physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| P02647 | anti bait coimmunoprecipitation | 15174051 | - | - |
| P04053 | cross-linking study | 30021884 | - | - |
| A8MW99 | validated two hybrid | 32296183 | - | - |
| Q04864 | two hybrid prey pooling approach | 25416956 | - | - |
| P69479 | anti tag coimmunoprecipitation | - | - | - |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| 无高置信度STRING互作 | - | - | - |

**已知复合体成员** (GO Cellular Component):
- 无已知复合体注释

**评价**: IntAct实验物理互作 (5条co-IP/pull-down)

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | pLDDT=None, PDB:2条目 | 一致 |
| 结构域 | UniProt | 0个注释域 | N/A |
| PPI | STRING + IntAct | IntAct:12, STRING:25 | 一致 |
| 定位 | UniProt | Nucleus | 是 |

**互证加分明细**:
- PDB实验结构确认 (+0.5)
- IntAct实验互作确认 (+0.5)
**总分**: +1 / max +3

**PAE 图**: 暂无PAE数据

### 4. 总体评价

**推荐等级**: ★★★ (69.9/100)

**核心优势**:
1. 有一定研究 (PubMed=53篇)
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
- UniProt: https://www.uniprot.org/uniprotkb/P04053
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DNTT
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。




