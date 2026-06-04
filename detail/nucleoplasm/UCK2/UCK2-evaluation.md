---
type: protein-evaluation
gene: "UCK2"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## UCK2 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/UCK2/IF_images/990_G5_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/UCK2/IF_images/990_G5_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | UCK2 |
| 蛋白名称 | Uridine-cytidine kinase 2 |
| 蛋白大小 | 261 aa |
| UniProt ID | [Q9BZX2](https://www.uniprot.org/uniprotkb/Q9BZX2) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Approved |
| PubMed 总数 | 79 |
| AlphaFold pLDDT | 86.1 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Approved); UniProt: N/A |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 261 aa |
| 🆕 研究新颖性 | 4/10 | ×5 | 20 | PubMed 79篇 |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | AlphaFold pLDDT: 86.1 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **102/183** |  |
| **归一化总分** |  |  | **55.7/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 UCK2 定位：
- **亚细胞定位**: Nucleoplasm
- **抗体可靠性**: Approved
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: N/A
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Gao J et al. (2025). "Integrating machine learning and molecular docking to decipher the molecular network of aflatoxin B1-induced hepatocellular carcinoma". *Int J Surg*. PMID: 40392001
2. Leung K (2004). "3'-(E)-(2-[(123/131)I]Iodovinyl)uridine". **. PMID: 20641989
3. Pham BQ et al. (2025). "mTORC1 regulates the pyrimidine salvage pathway by controlling UCK2 turnover via the CTLH-WDR26 E3 ligase". *Cell Rep*. PMID: 39808525
4. Fu Y et al. (2022). "The Metabolic and Non-Metabolic Roles of UCK2 in Tumor Progression". *Front Oncol*. PMID: 35669416
5. Zhou Q et al. (2018). "Uridine-cytidine kinase 2 promotes metastasis of hepatocellular carcinoma cells via the Stat3 pathway". *Cancer Manag Res*. PMID: 30568496

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
2. **研究新颖性**: PubMed仅79篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 86.1

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/UCK2)
- [UniProt](https://www.uniprot.org/uniprotkb/Q9BZX2)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=UCK2%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q9BZX2)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。




