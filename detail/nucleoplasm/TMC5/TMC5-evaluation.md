---
type: protein-evaluation
gene: "TMC5"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## TMC5 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TMC5/IF_images/486_F6_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TMC5/IF_images/486_F6_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TMC5 |
| 蛋白名称 | Transmembrane channel-like protein 5 |
| 蛋白大小 | 1006 aa |
| UniProt ID | [Q6UXY8](https://www.uniprot.org/uniprotkb/Q6UXY8) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Approved |
| PubMed 总数 | 19 |
| AlphaFold pLDDT | 62.9 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Approved); UniProt: Membrane |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 1006 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed 19篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold pLDDT: 62.9 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **124/183** |  |
| **归一化总分** |  |  | **67.8/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 TMC5 定位：
- **亚细胞定位**: Nucleoplasm
- **抗体可靠性**: Approved
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Membrane
- **结构域**: None identified
- **关键词**: ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Gan XY et al. (2023). "Role of Up-Regulated Transmembrane Channel-Like Protein 5 in Pancreatic Adenocarcinoma". *Dig Dis Sci*. PMID: 36459296
2. Braz JM et al. (2026). "Contribution of transmembrane channel-like (TMC) proteins 3, 5 and 7 to pain and itch processing". *J Pain*. PMID: 41207409
3. Li J et al. (2025). "Transmembrane channel-like 5 drives hepatocellular carcinoma progression by regulating epithelial-mesenchymal transition". *World J Clin Oncol*. PMID: 40130046
4. Wei Y et al. (2025). "The expression of transmembrane channel-like 5 in gastric cancer and its impact on tumor progression". *Sci Rep*. PMID: 40851023
5. Tian E et al. (2025). "RBM15 promotes COAD progression by regulating the m6A modification of TMC5". *Hereditas*. PMID: 40883807

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
2. **研究新颖性**: PubMed仅19篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 62.9

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/TMC5)
- [UniProt](https://www.uniprot.org/uniprotkb/Q6UXY8)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=TMC5%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q6UXY8)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6UXY8 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR038900;IPR012496; |
| Pfam | PF07810; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000103534-TMC5/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
