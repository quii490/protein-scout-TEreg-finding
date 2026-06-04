---
type: protein-evaluation
gene: "DNTTIP1"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DNTTIP1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DNTTIP1 / DNTTIP1 |
| 蛋白大小 | 329 aa |
| UniProt ID | Q9H147 |
| 蛋白名称 | Deoxynucleotidyltransferase terminal-interacting protein 1 |
| 评估日期 | 2026-05-29 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | UniProt Nucleus (唯一注释) |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 329 aa (200–800 aa, 适宜生化实验) |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed=23篇 (非常新颖) |
| 🏗️ 三维结构 | 10/10 | ×3 | 30 | PDB实验结构 (4条目) — 实验验证 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | 新颖蛋白 (PubMed≤50) — 无注释域基线, 可能存在新域 |
| 🔗 PPI 网络 | 6/10 | ×3 | 18 | IntAct实验物理互作 (12条co-IP/pull-down) |
| ➕ 互证加分 | — | max +3 | +2.5 | 核定位+转录因子功能一致 (+1.0); PDB多条目实验结构确认 (+1.0); IntAct实验互作确认 (+0.5) |
| **原始总分** |  |  | **141/183** |  |
| **归一化总分** |  |  | **77.0/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| UniProt | Nucleus | TrEMBL/Swiss-Prot |
| Protein Atlas (IF) | A-431, CACO-2 | Supported (HPA)


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/DNTTIP1/IF_images/DNTTIP1_A_431_2.jpg|DNTTIP1_A_431_2]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/DNTTIP1/IF_images/DNTTIP1_A_431_4.jpg|DNTTIP1_A_431_4]]



**结论**: UniProt Nucleus (唯一注释)

#### 3.2 蛋白大小评估

329 aa 蛋白。**评价**: 329 aa (200–800 aa, 适宜生化实验)

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 23 |
| 新颖性分级 | 非常新颖 |

**评价**: PubMed 共 23 篇文献，属于**非常新颖**。研究空间充足，适合作为创新课题。

**关键文献**:
1. Sawai Y et al. (2018). "Critical role of deoxynucleotidyl transferase terminal interacting protein 1 in oral cancer". *Lab Invest*. PMID: 29855544
2. Wilhelm E et al. (2024). "Mitotic deacetylase complex (MiDAC) recognizes the HIV-1 core promoter to control activated viral gene expression". *PLoS Pathog*. PMID: 38781120
3. Itoh T et al. (2015). "Structural and functional characterization of a cell cycle associated HDAC1/2 complex reveals the structural basis for complex assembly and nucleosome targeting". *Nucleic Acids Res*. PMID: 25653165
4. Wang X et al. (2023). "High Expression of DNTTIP1 Predicts Poor Prognosis in Clear Cell Renal Cell Carcinoma". *Pharmgenomics Pers Med*. PMID: 36636625
5. Liu YJ et al. (2022). "DNTTIP2 Expression is Associated with Macrophage Infiltration and Malignant Characteristics in Low-Grade Glioma". *Pharmgenomics Pers Med*. PMID: 35370417
#### 3.4 三维结构分析

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | None |
| 有序区域 (pLDDT>70) 占比 | None% |
| 高置信度 (pLDDT>90) 占比 | None% |
| 可用 PDB 条目 | 2MWI; 4D6K; 6Z2J; 6Z2K |

**评价**: PDB实验结构 (4条目) — 实验验证

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| UniProt | 无注释结构域 |
| GO Molecular Function | Increases DNTT terminal deoxynucleotidyltransferase activity (in vitro) (PubMed:11473582). Also acts as a transcriptional regulator, binding to the co |

**染色质调控潜力分析**: 新颖蛋白 (PubMed≤50) — 无注释域基线, 可能存在新域

#### 3.6 PPI 网络

**实验验证互作** (IntAct physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| intact:EBI | pull down | 19505873 | - | - |
| Q9H147 | anti bait coimmunoprecipitation | 21258344 | - | - |
| Q13547 | anti bait coimmunoprecipitation | 21258344 | - | - |
| Q92769 | anti bait coimmunoprecipitation | 21258344 | - | - |
| Q96PN7 | anti bait coimmunoprecipitation | 21258344 | - | - |
| Q6NT76 | two hybrid array | 32296183 | - | - |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| 无高置信度STRING互作 | - | - | - |

**已知复合体成员** (GO Cellular Component):
- 无已知复合体注释

**评价**: IntAct实验物理互作 (12条co-IP/pull-down)

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | pLDDT=None, PDB:4条目 | 一致 |
| 结构域 | UniProt | 0个注释域 | N/A |
| PPI | STRING + IntAct | IntAct:30, STRING:25 | 一致 |
| 定位 | UniProt | Nucleus | 是 |

**互证加分明细**:
- 核定位+转录因子功能一致 (+1.0)
- PDB多条目实验结构确认 (+1.0)
- IntAct实验互作确认 (+0.5)
**总分**: +2.5 / max +3

**PAE 图**: 暂无PAE数据

### 4. 总体评价

**推荐等级**: ★★★★ (77.9/100)

**核心优势**:
1. 非常新颖 (PubMed=23篇)
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
- UniProt: https://www.uniprot.org/uniprotkb/Q9H147
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DNTTIP1
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。




