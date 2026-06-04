---
type: protein-evaluation
gene: "NRSN2"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

## NRSN2 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NRSN2/IF_images/128_E12_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NRSN2/IF_images/128_E12_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | NRSN2 |
| 蛋白名称 | Neurensin-2 |
| 蛋白大小 | 204 aa |
| UniProt ID | [Q9GZP1](https://www.uniprot.org/uniprotkb/Q9GZP1) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Approved |
| PubMed 总数 | 22 |
| AlphaFold pLDDT | 64.6 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Approved); UniProt: Membrane |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 204 aa |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed 22篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold pLDDT: 64.6 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **116/183** |  |
| **归一化总分** |  |  | **63.4/100** |  |

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 NRSN2 定位：
- **亚细胞定位**: Nucleoplasm
- **抗体可靠性**: Approved
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Membrane
- **结构域**: None identified
- **关键词**: ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Wang G & Yang K (2020). "Neurensin-2 promotes proliferation, invasion and migration of colorectal cancer cells via interaction with SOX12". *Oncol Lett*. PMID: 33193849
2. Yun C et al. (2024). "miR-488-3p Represses Malignant Behaviors and Facilitates Autophagy of Osteosarcoma Cells by Targeting Neurensin-2". *Curr Pharm Biotechnol*. PMID: 37365792
3. Ma HQ et al. (2009). "Decreased expression of Neurensin-2 correlates with poor prognosis in hepatocellular carcinoma". *World J Gastroenterol*. PMID: 19824122
4. Wu YB et al. (2023). "Long non-coding RNA NRSN2-AS1 promotes ovarian cancer progression through targeting PTK2/β-catenin pathway". *Cell Death Dis*. PMID: 37875515
5. Zhang XY et al. (2015). "NRSN2 promotes non-small cell lung cancer cell growth through PI3K/Akt/mTOR pathway". *Int J Clin Exp Pathol*. PMID: 26045763

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

**推荐等级**: ⭐⭐

**核心发现**:
1. **HPA IF 确认为核蛋白**: 原始"核定位≤3"淘汰为误判，HPA实验数据确认为Nucleoplasm
2. **研究新颖性**: PubMed仅22篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 64.6

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/NRSN2)
- [UniProt](https://www.uniprot.org/uniprotkb/Q9GZP1)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=NRSN2%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q9GZP1)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。




