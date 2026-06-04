---
type: protein-evaluation
gene: "SREK1IP1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## SREK1IP1 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoli; Nucleoplasm (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/SREK1IP1/IF_images/1261_C12_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/SREK1IP1/IF_images/1261_C12_5_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SREK1IP1 |
| 蛋白名称 | Protein SREK1IP1 |
| 蛋白大小 | 155 aa |
| UniProt ID | [Q8N9Q2](https://www.uniprot.org/uniprotkb/Q8N9Q2) |
| HPA 核定位 (IF) | Nucleoli; Nucleoplasm |
| HPA 可靠性 | Approved |
| PubMed 总数 | 5 |
| AlphaFold pLDDT | 63.7 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA IF: Nucleoli; Nucleoplasm (Approved); UniProt: N/A |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 155 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed 5篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold pLDDT: 63.7 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **128/183** |  |
| **归一化总分** |  |  | **69.9/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 SREK1IP1 定位：
- **亚细胞定位**: Nucleoli; Nucleoplasm
- **抗体可靠性**: Approved
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: N/A
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Kamarck ML et al. (2024). "Identifying candidate genes underlying isolated congenital anosmia". *Clin Genet*. PMID: 38148624
2. Aceituno-Valenzuela UI et al. (2024). "CXIP4 depletion causes early lethality and pre-mRNA missplicing in Arabidopsis". *bioRxiv*. PMID: 38915646
3. Nehring P & Przybyłkowski A (2025). "Genetic Determinants of Colonic Diverticulosis-A Systematic Review". *Genes (Basel)*. PMID: 40428403
4. Aceituno-Valenzuela U et al. (2024). "CAX-INTERACTING PROTEIN4 depletion causes early lethality and pre-mRNA missplicing in Arabidopsis". *Plant Physiol*. PMID: 39657023
5. Akiyama Y et al. (2016). "Reduced expression of SET7/9, a histone mono-methyltransferase, is associated with gastric cancer progression". *Oncotarget*. PMID: 26701885

**评价**: 基于 PubMed 检索结果。


#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| HSD17B14 | two hybrid array | 31515488 | — | — |
| NKAPD1 | two hybrid prey pooling approach | 32296183 | — | — |
| RNF151 | validated two hybrid | 32296183 | — | — |
| ELOA2 | two hybrid array | 32296183 | — | — |
| NKAPL | validated two hybrid | 32296183 | — | — |
| MACROH2A1 | validated two hybrid | 32296183 | — | — |
| H2BC15 | two hybrid array | 32296183 | — | — |
| GTF2H4 | two hybrid array | 32296183 | — | — |
| DDIT4L | validated two hybrid | 32296183 | — | — |
| CCNL1 | two hybrid prey pooling approach | 32296183 | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| — | — | — | — |

**已知复合体成员** (GO Cellular Component):
- 暂无 GO-CC 数据

**IntAct 查询记录**: IntAct: 31 实验验证互作

**评价**: —


### 5. 总体评价

**推荐等级**: ⭐⭐⭐

**核心发现**:
1. **HPA IF 确认为核蛋白**: 原始"核定位≤3"淘汰为误判，HPA实验数据确认为Nucleoli; Nucleoplasm
2. **研究新颖性**: PubMed仅5篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 63.7

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/SREK1IP1)
- [UniProt](https://www.uniprot.org/uniprotkb/Q8N9Q2)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=SREK1IP1%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q8N9Q2)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。




