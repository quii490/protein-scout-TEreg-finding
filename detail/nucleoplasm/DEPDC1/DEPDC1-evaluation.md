---
type: protein-evaluation
gene: "DEPDC1"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DEPDC1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DEPDC1 / DEPDC1 |
| 蛋白大小 | 811 aa |
| UniProt ID | Q5TB30 |
| 蛋白名称 | DEP domain-containing protein 1A |
| 评估日期 | 2026-05-29 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | UniProt Nucleus (唯一注释) |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 811 aa (800–1200 aa) |
| 🆕 研究新颖性 | 2/10 | ×5 | 30 | PubMed=99篇 (有一定研究) |
| 🏗️ 三维结构 | 9/10 | ×3 | 27 | PDB实验结构 (1条目) |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | PubMed≤100 — 无注释域基线 |
| 🔗 PPI 网络 | 6/10 | ×3 | 18 | IntAct实验物理互作 (21条co-IP/pull-down) |
| ➕ 互证加分 | — | max +3 | +2 | 核定位+转录因子功能一致 (+1.0); PDB实验结构确认 (+0.5); IntAct实验互作确认 (+0.5) |
|  | **原始总分** |  | **106/183** | **105.0/183** |  |  |  |
|  | **归一化总分** |  | **57.9/100** | **57.4/100** |  |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| UniProt | Nucleus | TrEMBL/Swiss-Prot |
| Protein Atlas (IF) | A-431, U-251MG | Supported (HPA)


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/DEPDC1/IF_images/DEPDC1_A_431_1.jpg|DEPDC1_A_431_1]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/DEPDC1/IF_images/DEPDC1_A_431_2.jpg|DEPDC1_A_431_2]]



**结论**: UniProt Nucleus (唯一注释)

#### 3.2 蛋白大小评估

811 aa 蛋白。**评价**: 811 aa (800–1200 aa)

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 99 |
| 新颖性分级 | 有一定研究 |

**评价**: PubMed 共 99 篇文献，属于**有一定研究**。研究空间充足，适合作为创新课题。


**关键文献**:
1. Di SC et al. (2024). "DEPDC1 as a metabolic target regulates glycolysis in renal cell carcinoma through AKT/mTOR/HIF1α pathway". *Cell Death Dis*. PMID: 39068164
2. Liu D et al. (2024). "Roles of DEPDC1 in various types of cancer (Review)". *Oncol Lett*. PMID: 39296974
3. Gao H et al. (2025). "Identification of glycolysis-related gene signatures for prognosis and therapeutic targeting in idiopathic pulmonary fibrosis". *Front Pharmacol*. PMID: 40093327
4. Li C & Zhu X (2024). "DEP domain containing 1 as a biomarker for poor prognosis in lung adenocarcinoma". *Heliyon*. PMID: 38765113
5. Laue K et al. (2026). "p53 inactivation drives breast cancer metastasis to the brain through SCD1 upregulation and increased fatty acid metabolism". *Nat Genet*. PMID: 41461910

#### 3.4 三维结构分析

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | None |
| 有序区域 (pLDDT>70) 占比 | None% |
| 高置信度 (pLDDT>90) 占比 | None% |
| 可用 PDB 条目 | 2YSR |

**评价**: PDB实验结构 (1条目)

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| UniProt | 无注释结构域 |
| GO Molecular Function | May be involved in transcriptional regulation as a transcriptional corepressor. The DEPDC1A-ZNF224 complex may play a critical role in bladder carcino |

**染色质调控潜力分析**: PubMed≤100 — 无注释域基线

#### 3.6 PPI 网络

**实验验证互作** (IntAct physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| Q5TB30 | anti tag coimmunoprecipitation | 28514442 | - | - |
| P32970 | anti tag coimmunoprecipitation | 28514442 | - | - |
| Q6UWB1 | anti tag coimmunoprecipitation | 28514442 | - | - |
| Q6PJG9 | anti tag coimmunoprecipitation | 28514442 | - | - |
| Q8WWB7 | anti tag coimmunoprecipitation | 28514442 | - | - |
| Q8N7X8 | anti tag coimmunoprecipitation | 28514442 | - | - |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| 无高置信度STRING互作 | - | - | - |

**已知复合体成员** (GO Cellular Component):
- 无已知复合体注释

**评价**: IntAct实验物理互作 (21条co-IP/pull-down)

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | pLDDT=None, PDB:1条目 | 一致 |
| 结构域 | UniProt | 0个注释域 | N/A |
| PPI | STRING + IntAct | IntAct:30, STRING:0 | 一致 |
| 定位 | UniProt | Nucleus | 是 |

**互证加分明细**:
- 核定位+转录因子功能一致 (+1.0)
- PDB实验结构确认 (+0.5)
- IntAct实验互作确认 (+0.5)
**总分**: +2 / max +3

**PAE 图**: 暂无PAE数据

### 4. 总体评价

**推荐等级**: ★★★ (69.4/100)

**核心优势**:
1. 有一定研究 (PubMed=99篇)
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
- UniProt: https://www.uniprot.org/uniprotkb/Q5TB30
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DEPDC1
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。




