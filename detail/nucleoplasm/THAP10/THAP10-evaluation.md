---
type: protein-evaluation
gene: "THAP10"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## THAP10 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/THAP10/IF_images/557_F10_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/THAP10/IF_images/557_F10_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | THAP10 |
| 蛋白名称 | THAP domain-containing protein 10 |
| 蛋白大小 | 257 aa |
| UniProt ID | [Q9P2Z0](https://www.uniprot.org/uniprotkb/Q9P2Z0) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Approved |
| PubMed 总数 | 4 |
| AlphaFold pLDDT | 62.9 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Approved); UniProt: N/A |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 257 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed 4篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold pLDDT: 62.9 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **126/183** |  |
| **归一化总分** |  |  | **68.9/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 THAP10 定位：
- **亚细胞定位**: Nucleoplasm
- **抗体可靠性**: Approved
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: N/A
- **结构域**: None identified
- **关键词**: ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Sanghavi HM & Majumdar S (2021). "Oligomerization of THAP9 Transposase via Amino-Terminal Domains". *Biochemistry*. PMID: 34033475
2. Li Y et al. (2017). "A novel epigenetic AML1-ETO/THAP10/miR-383 mini-circuitry contributes to t(8;21) leukaemogenesis". *EMBO Mol Med*. PMID: 28539478
3. Sanghavi HM et al. (2019). "Classification of the human THAP protein family identifies an evolutionarily conserved coiled coil region". *BMC Struct Biol*. PMID: 30836974
4. Zhang L et al. (2024). "CRISPR-Cas9 screening develops an epigenetic and transcriptional gene signature for risk stratification and target prediction in neuroblastoma". *Front Cell Dev Biol*. PMID: 39175876
5. De Souza Santos E et al. (2008). "Silencing of LRRC49 and THAP10 genes by bidirectional promoter hypermethylation is a frequent event in breast cancer". *Int J Oncol*. PMID: 18575747

**评价**: 基于 PubMed 检索结果。


#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| — | — | — | — |

**已知复合体成员** (GO Cellular Component):
- 暂无 GO-CC 数据

**IntAct 查询记录**: IntAct: 未检索到实验验证互作

**评价**: 待补充 IntAct/STRING/GO-CC 数据。


### 5. 总体评价

**推荐等级**: ⭐⭐⭐

**核心发现**:
1. **HPA IF 确认为核蛋白**: 原始"核定位≤3"淘汰为误判，HPA实验数据确认为Nucleoplasm
2. **研究新颖性**: PubMed仅4篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 62.9

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/THAP10)
- [UniProt](https://www.uniprot.org/uniprotkb/Q9P2Z0)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=THAP10%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q9P2Z0)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。




