---
type: protein-evaluation
gene: "SAMD14"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## SAMD14 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoli fibrillar center; Nucleoplasm (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/SAMD14/IF_images/1331_C3_5_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/SAMD14/IF_images/1331_C3_8_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SAMD14 |
| 蛋白名称 | Sterile alpha motif domain-containing protein 14 |
| 蛋白大小 | 417 aa |
| UniProt ID | [Q8IZD0](https://www.uniprot.org/uniprotkb/Q8IZD0) |
| HPA 核定位 (IF) | Nucleoli fibrillar center; Nucleoplasm |
| HPA 可靠性 | Approved |
| PubMed 总数 | 9 |
| AlphaFold pLDDT | 59.9 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA IF: Nucleoli fibrillar center; Nucleoplasm (Approved); UniProt: N/A |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 417 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed 9篇 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15 | AlphaFold pLDDT: 59.9 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **127/183** |  |
| **归一化总分** |  |  | **69.4/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 SAMD14 定位：
- **亚细胞定位**: Nucleoli fibrillar center; Nucleoplasm
- **抗体可靠性**: Approved
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: N/A
- **结构域**: None identified
- **关键词**: ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Schaefer MA et al. (2023). "Physiological and regenerative functions of sterile-α motif protein-14 in hematopoiesis". *Exp Hematol*. PMID: 37722652
2. Ray S et al. (2020). "Sterile α-motif domain requirement for cellular signaling and survival". *J Biol Chem*. PMID: 32241909
3. Roy P et al. (2025). "A Phosphoinositide Interacting Protein Coordinates Stress Precursor Activities". *bioRxiv*. PMID: 40894755
4. Ray S et al. (2022). "Functional requirements for a Samd14-capping protein complex in stress erythropoiesis". *Elife*. PMID: 35713400
5. Hewitt KJ et al. (2025). "Signaling mechanisms and cis -regulatory control of Samd14 in erythroid regeneration". *Curr Opin Hematol*. PMID: 40293138

**评价**: 基于 PubMed 检索结果。


#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| H3C13 | cross-linking study | 30021884 | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| — | — | — | — |

**已知复合体成员** (GO Cellular Component):
- 暂无 GO-CC 数据

**IntAct 查询记录**: IntAct: 1 实验验证互作

**评价**: 基于 IntAct + UniProt GO-CC 综合分析。


### 5. 总体评价

**推荐等级**: ⭐⭐⭐

**核心发现**:
1. **HPA IF 确认为核蛋白**: 原始"核定位≤3"淘汰为误判，HPA实验数据确认为Nucleoli fibrillar center; Nucleoplasm
2. **研究新颖性**: PubMed仅9篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 59.9

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/SAMD14)
- [UniProt](https://www.uniprot.org/uniprotkb/Q8IZD0)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=SAMD14%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q8IZD0)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。




