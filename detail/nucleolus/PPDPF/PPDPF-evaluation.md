---
type: protein-evaluation
gene: "PPDPF"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## PPDPF 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoli; Nucleoplasm (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/PPDPF/IF_images/424_C5_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/PPDPF/IF_images/424_C5_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PPDPF |
| 蛋白名称 | Pancreatic progenitor cell differentiation and proliferation factor |
| 蛋白大小 | 114 aa |
| UniProt ID | [Q9H3Y8](https://www.uniprot.org/uniprotkb/Q9H3Y8) |
| HPA 核定位 (IF) | Nucleoli; Nucleoplasm |
| HPA 可靠性 | Approved |
| PubMed 总数 | 25 |
| AlphaFold pLDDT | 59.8 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA IF: Nucleoli; Nucleoplasm (Approved); UniProt: N/A |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 114 aa |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed 25篇 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15 | AlphaFold pLDDT: 59.8 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **115/183** |  |
| **归一化总分** |  |  | **62.8/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 PPDPF 定位：
- **亚细胞定位**: Nucleoli; Nucleoplasm
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
1. Fang X et al. (2025). "PPDPF preserves integrity of proximal tubule by modulating NMNAT activity in chronic kidney diseases". *Sci Adv*. PMID: 40106551
2. Zi Y et al. (2023). "Phosphorylation of PPDPF via IL6-JAK2 activates the Wnt/β-catenin pathway in colorectal cancer". *EMBO Rep*. PMID: 37477088
3. Zhu B et al. (2025). "PPDPF promotes the progression of esophageal squamous cell carcinoma via c-Myc/CD24 axis". *J Immunother Cancer*. PMID: 40774693
4. Li Z et al. (2025). "PPDPF-mediated regulation of BCAA metabolism enhances mTORC1 activity and drives cholangiocarcinoma progression". *Oncogene*. PMID: 40025229
5. Li M et al. (2024). "PPDPF promotes esophageal squamous cell carcinoma progression by blocking PCCA binding to PCCB and inhibiting methionine catabolism". *Cancer Lett*. PMID: 39694223

**评价**: 基于 PubMed 检索结果。


#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| hsamir7445p | clash | 23622248 | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| — | — | — | — |

**已知复合体成员** (GO Cellular Component):
- 暂无 GO-CC 数据

**IntAct 查询记录**: IntAct: 1 实验验证互作

**评价**: 基于 IntAct + UniProt GO-CC 综合分析。


### 5. 总体评价

**推荐等级**: ⭐⭐

**核心发现**:
1. **HPA IF 确认为核蛋白**: 原始"核定位≤3"淘汰为误判，HPA实验数据确认为Nucleoli; Nucleoplasm
2. **研究新颖性**: PubMed仅25篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 59.8

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/PPDPF)
- [UniProt](https://www.uniprot.org/uniprotkb/Q9H3Y8)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=PPDPF%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q9H3Y8)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。




