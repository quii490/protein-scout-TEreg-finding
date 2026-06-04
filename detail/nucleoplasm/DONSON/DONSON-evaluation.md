---
type: protein-evaluation
gene: "DONSON"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DONSON 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DONSON / DONSON |
| 蛋白大小 | 566 aa |
| UniProt ID | Q9NYP3 |
| 蛋白名称 | Protein downstream neighbor of Son |
| 评估日期 | 2026-05-29 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | UniProt Nucleus (唯一注释) |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 566 aa (200–800 aa, 适宜生化实验) |
| 🆕 研究新颖性 | 6/10 | ×5 | 40 | PubMed=46篇 (非常新颖) |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | 新颖蛋白 (PubMed≤100) — 无结构基线, 不扣分 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | 新颖蛋白 (PubMed≤50) — 无注释域基线, 可能存在新域 |
| 🔗 PPI 网络 | 4/10 | ×3 | 12 | 少量IntAct物理互作 (2条) |
| ➕ 互证加分 | — | max +3 | +0 | 无额外互证 |
|  | **原始总分** |  | **112/183** | **112.0/183** |  |  |  |
|  | **归一化总分** |  | **61.2/100** | **61.2/100** |  |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| UniProt | Nucleus | TrEMBL/Swiss-Prot |
| Protein Atlas (IF) | A-431, U-251MG | Supported (HPA)


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/DONSON/IF_images/DONSON_A_431_1.jpg|DONSON_A_431_1]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/DONSON/IF_images/DONSON_A_431_2.jpg|DONSON_A_431_2]]



**结论**: UniProt Nucleus (唯一注释)

#### 3.2 蛋白大小评估

566 aa 蛋白。**评价**: 566 aa (200–800 aa, 适宜生化实验)

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 46 |
| 新颖性分级 | 非常新颖 |

**评价**: PubMed 共 46 篇文献，属于**非常新颖**。研究空间充足，适合作为创新课题。

**关键文献**:
1. Terui R et al. (2024). "Single-molecule imaging reveals the mechanism of bidirectional replication initiation in metazoa". *Cell*. PMID: 38866019
2. Lim Y et al. (2023). "In silico protein interaction screening uncovers DONSON's role in replication initiation". *Science*. PMID: 37590370
3. Xia Y et al. (2023). "DNSN-1 recruits GINS for CMG helicase assembly during DNA replication initiation in Caenorhabditis elegans". *Science*. PMID: 37590372
4. Qi Y et al. (2022). "Downstream Neighbor of Son Overexpression is Associated With Breast Cancer Progression and a Poor Prognosis". *J Breast Cancer*. PMID: 35914745
5. Stewart GS (2024). "DONSON: Slding in 2 the limelight". *DNA Repair (Amst)*. PMID: 38159447
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
| GO Molecular Function | Replisome component that maintains genome stability by protecting stalled or damaged replication forks. After the induction of replication stress, req |

**染色质调控潜力分析**: 新颖蛋白 (PubMed≤50) — 无注释域基线, 可能存在新域

#### 3.6 PPI 网络

**实验验证互作** (IntAct physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| P49321 | anti tag coimmunoprecipitation | 26496610 | - | - |
| Q9NYP3 | anti tag coimmunoprecipitation | 33961781 | - | - |

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
| PPI | STRING + IntAct | IntAct:6, STRING:25 | 一致 |
| 定位 | UniProt | Nucleus | 是 |

**互证加分明细**:
- 无额外互证加分
**总分**: +0 / max +3

**PAE 图**: 暂无PAE数据

### 4. 总体评价

**推荐等级**: ★★★ (66.7/100)

**核心优势**:
1. 非常新颖 (PubMed=46篇)
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
- UniProt: https://www.uniprot.org/uniprotkb/Q9NYP3
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DONSON
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。




