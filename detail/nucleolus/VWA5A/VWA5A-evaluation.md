---
type: protein-evaluation
gene: "VWA5A"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## VWA5A 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoli; Nucleoplasm (Reliability: Enhanced)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/VWA5A/IF_images/1046_F12_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/VWA5A/IF_images/1046_F12_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | VWA5A |
| 蛋白名称 | von Willebrand factor A domain-containing protein 5A |
| 蛋白大小 | 786 aa |
| UniProt ID | [O00534](https://www.uniprot.org/uniprotkb/O00534) |
| HPA 核定位 (IF) | Nucleoli; Nucleoplasm |
| HPA 可靠性 | Enhanced |
| PubMed 总数 | 15 |
| AlphaFold pLDDT | 84.6 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 9/10 | ×4 | 36 | HPA IF: Nucleoli; Nucleoplasm (Enhanced); UniProt: N/A |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 786 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed 15篇 |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold pLDDT: 84.6 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **141/183** |  |
| **归一化总分** |  |  | **77.0/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 VWA5A 定位：
- **亚细胞定位**: Nucleoli; Nucleoplasm
- **抗体可靠性**: Enhanced
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: N/A
- **结构域**: None identified
- **关键词**: ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Szabo A et al. (2021). "A human iPSC-astroglia neurodevelopmental model reveals divergent transcriptomic patterns in schizophrenia". *Transl Psychiatry*. PMID: 34716291
2. Lian C et al. (2025). "Identification of a Treg-related gene signature for predicting prognosis and immunosuppression in skin cutaneous melanoma". *Clin Exp Med*. PMID: 41286029
3. Liu X et al. (2023). "Chromosome-Level Analysis of the Pelochelys cantorii Genome Provides Insights to Its Immunity, Growth and Longevity". *Biology (Basel)*. PMID: 37508370
4. Ma Y et al. (2025). "Mapping the BCSC-1 interactome in breast cancer". *Sci Rep*. PMID: 41120661
5. Koh J et al. (2024). "Identification of VWA5A as a novel biomarker for inhibiting metastasis in breast cancer by machine-learning based protein prioritization". *Sci Rep*. PMID: 38291227

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

**推荐等级**: ⭐⭐⭐⭐

**核心发现**:
1. **HPA IF 确认为核蛋白**: 原始"核定位≤3"淘汰为误判，HPA实验数据确认为Nucleoli; Nucleoplasm
2. **研究新颖性**: PubMed仅15篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 84.6

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/VWA5A)
- [UniProt](https://www.uniprot.org/uniprotkb/O00534)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=VWA5A%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/O00534)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。




