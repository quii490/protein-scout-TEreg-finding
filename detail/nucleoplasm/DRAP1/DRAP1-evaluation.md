---
type: protein-evaluation
gene: "DRAP1"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DRAP1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DRAP1 / DRAP1 |
| 蛋白大小 | 212 aa |
| UniProt ID | C9JCC6 |
| 蛋白名称 | Dr1-associated corepressor |
| 评估日期 | 2026-05-29 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | UniProt Nucleus (唯一注释) |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 212 aa (200–800 aa, 适宜生化实验) |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed=37篇 (非常新颖) |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | 新颖蛋白 (PubMed≤100) — 无结构基线, 不扣分 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | 新颖蛋白 (PubMed≤50) — 无注释域基线, 可能存在新域 |
| 🔗 PPI 网络 | 6/10 | ×3 | 18 | IntAct实验物理互作 (11条co-IP/pull-down) |
| ➕ 互证加分 | — | max +3 | +0.5 | IntAct实验互作确认 (+0.5) |
| **原始总分** |  |  | **128.5/183** |  |
| **归一化总分** |  |  | **70.2/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| UniProt | Nucleus | TrEMBL/Swiss-Prot |
| Protein Atlas (IF) | A-431, U-251MG | Supported (HPA)


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/DRAP1/IF_images/DRAP1_A_431_1.jpg|DRAP1_A_431_1]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/DRAP1/IF_images/DRAP1_A_431_2.jpg|DRAP1_A_431_2]]



**结论**: UniProt Nucleus (唯一注释)

#### 3.2 蛋白大小评估

212 aa 蛋白。**评价**: 212 aa (200–800 aa, 适宜生化实验)

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 37 |
| 新颖性分级 | 非常新颖 |

**评价**: PubMed 共 37 篇文献，属于**非常新颖**。研究空间充足，适合作为创新课题。

**关键文献**:
1. Huang MY et al. (2024). "The DRAP1/DR1 Repressor Complex Increases mTOR Activity to Promote Progression and Confer Everolimus Sensitivity in Triple-Negative Breast Cancer". *Cancer Res*. PMID: 38748783
2. Mermelstein F et al. (1996). "Requirement of a corepressor for Dr1-mediated repression of transcription". *Genes Dev*. PMID: 8608938
3. Wang J et al. (2022). "Tumor-Infiltrated CD8+ T Cell 10-Gene Signature Related to Clear Cell Renal Cell Carcinoma Prognosis". *Front Immunol*. PMID: 35812454
4. Schier AF (2003). "Nodal signaling in vertebrate development". *Annu Rev Cell Dev Biol*. PMID: 14570583
5. Wang Y et al. (2015). "Evaluation of housekeeping genes for normalizing real-time quantitative PCR assays in pig skeletal muscle at multiple developmental stages". *Gene*. PMID: 25865298
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

**染色质调控潜力分析**: 新颖蛋白 (PubMed≤50) — 无注释域基线, 可能存在新域

#### 3.6 PPI 网络

**实验验证互作** (IntAct physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| Q14919 | two hybrid array | 25416956 | - | - |
| Q9W2E3 | two hybrid | 14605208 | - | - |
| Q9V9Y9 | two hybrid | 14605208 | - | - |
| A1ZBT3 | two hybrid | 14605208 | - | - |
| Q9VCR9 | two hybrid | 14605208 | - | - |
| Q9VCT2 | two hybrid | 14605208 | - | - |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| 无高置信度STRING互作 | - | - | - |

**已知复合体成员** (GO Cellular Component):
- 无已知复合体注释

**评价**: IntAct实验物理互作 (11条co-IP/pull-down)

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

**推荐等级**: ★★★★ (70.2/100)

**核心优势**:
1. 非常新颖 (PubMed=37篇)
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
- UniProt: https://www.uniprot.org/uniprotkb/C9JCC6
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DRAP1
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。




