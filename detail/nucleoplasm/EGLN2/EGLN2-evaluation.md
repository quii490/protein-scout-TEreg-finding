---
type: protein-evaluation
gene: "EGLN2"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## EGLN2 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Supported)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/EGLN2/IF_images/985_C10_3_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/EGLN2/IF_images/985_C10_4_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | EGLN2 |
| 蛋白名称 |  |
| 蛋白大小 | 139 aa |
| UniProt ID | [M0R0Z6](https://www.uniprot.org/uniprotkb/M0R0Z6) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Supported |
| PubMed 总数 | 98 |
| AlphaFold pLDDT | 60.0 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Supported); UniProt: N/A |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 139 aa |
| 🆕 研究新颖性 | 2/10 | ×5 | 10 | PubMed 98篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold pLDDT: 60.0 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **84/183** |  |
| **归一化总分** |  |  | **45.9/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 EGLN2 定位：
- **亚细胞定位**: Nucleoplasm
- **抗体可靠性**: Supported
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: N/A
- **结构域**: None identified
- **关键词**: ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Germeys C et al. (2024). "Targeting EGLN2/PHD1 protects motor neurons and normalizes the astrocytic interferon response". *Cell Rep*. PMID: 39255062
2. Lin Q et al. (2021). "Inhibiting NLRP3 inflammasome attenuates apoptosis in contrast-induced acute kidney injury through the upregulation of HIF1A and BNIP3-mediated mitophagy". *Autophagy*. PMID: 33345685
3. Wang S et al. (2025). "Joint Analysis of Multiple Omics to Describe the Biological Characteristics of Resistant Hypertension". *J Clin Hypertens (Greenwich)*. PMID: 39716980
4. Zhang D et al. (2025). "Comprehensive Pan-cancer Analysis and Experimental Verification of EGLN Family: Potential Biomarkers in Cervical Cancer". *Curr Cancer Drug Targets*. PMID: 40464184
5. Zhang L et al. (2017). "Tumor suppressor SPOP ubiquitinates and degrades EglN2 to compromise growth of prostate cancer cells". *Cancer Lett*. PMID: 28089830

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

**推荐等级**: ⭐

**核心发现**:
1. **HPA IF 确认为核蛋白**: 原始"核定位≤3"淘汰为误判，HPA实验数据确认为Nucleoplasm
2. **研究新颖性**: PubMed仅98篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 60.0

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/EGLN2)
- [UniProt](https://www.uniprot.org/uniprotkb/M0R0Z6)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=EGLN2%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/M0R0Z6)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。




