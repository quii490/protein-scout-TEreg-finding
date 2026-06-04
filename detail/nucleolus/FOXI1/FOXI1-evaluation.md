---
type: protein-evaluation
gene: "FOXI1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## FOXI1 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoli (Reliability: Supported)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/FOXI1/IF_images/1576_G7_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/FOXI1/IF_images/1576_G7_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | FOXI1 |
| 蛋白名称 |  |
| 蛋白大小 | 378 aa |
| UniProt ID | [E0XEY9](https://www.uniprot.org/uniprotkb/E0XEY9) |
| HPA 核定位 (IF) | Nucleoli |
| HPA 可靠性 | Supported |
| PubMed 总数 | 87 |
| AlphaFold pLDDT | 54.4 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoli (Supported); UniProt: Nucleus |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 378 aa |
| 🆕 研究新颖性 | 2/10 | ×5 | 10 | PubMed 87篇 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15 | AlphaFold pLDDT: 54.4 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **83/183** |  |
| **归一化总分** |  |  | **45.4/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 FOXI1 定位：
- **亚细胞定位**: Nucleoli
- **抗体可靠性**: Supported
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Nucleus
- **结构域**: None identified
- **关键词**: ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Montoro DT et al. (2018). "A revised airway epithelial hierarchy includes CFTR-expressing ionocytes". *Nature*. PMID: 30069044
2. Wagner CA et al. (2023). "The pathophysiology of distal renal tubular acidosis". *Nat Rev Nephrol*. PMID: 37016093
3. Plasschaert LW et al. (2018). "A single-cell atlas of the airway epithelium reveals the CFTR-rich pulmonary ionocyte". *Nature*. PMID: 30069046
4. Shi M et al. (2023). "Human ureteric bud organoids recapitulate branching morphogenesis and differentiate into functional collecting duct cell types". *Nat Biotechnol*. PMID: 36038632
5. Yuan F et al. (2023). "Transgenic ferret models define pulmonary ionocyte diversity and function". *Nature*. PMID: 37730992

**评价**: 基于 PubMed 检索结果。


#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| DTX2 | two hybrid prey pooling approach | 32296183 | — | — |
| NFKBID | two hybrid prey pooling approach | 32296183 | — | — |
| USP54 | validated two hybrid | 32296183 | — | — |
| kr191_human | two hybrid array | 32296183 | — | — |
| RAMAC | two hybrid array | 32296183 | — | — |
| PIN1 | two hybrid array | 32296183 | — | — |
| FAM83A | two hybrid array | 32296183 | — | — |
| ATP23 | validated two hybrid | 32296183 | — | — |
| WWOX | validated two hybrid | 32296183 | — | — |
| VPS37C | two hybrid array | 32296183 | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| — | — | — | — |

**已知复合体成员** (GO Cellular Component):
- GO: Nucleus

**IntAct 查询记录**: IntAct: 15 实验验证互作

**评价**: 基于 IntAct + UniProt GO-CC 综合分析。


### 5. 总体评价

**推荐等级**: ⭐

**核心发现**:
1. **HPA IF 确认为核蛋白**: 原始"核定位≤3"淘汰为误判，HPA实验数据确认为Nucleoli
2. **研究新颖性**: PubMed仅87篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 54.4

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/FOXI1)
- [UniProt](https://www.uniprot.org/uniprotkb/E0XEY9)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=FOXI1%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/E0XEY9)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。




