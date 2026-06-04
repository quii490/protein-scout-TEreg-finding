---
type: protein-evaluation
gene: "EVX1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## EVX1 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/EVX1/IF_images/1526_A4_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/EVX1/IF_images/1526_A4_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | EVX1 |
| 蛋白名称 | Homeobox even-skipped homolog protein 1 |
| 蛋白大小 | 407 aa |
| UniProt ID | [P49640](https://www.uniprot.org/uniprotkb/P49640) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Approved |
| PubMed 总数 | 74 |
| AlphaFold pLDDT | 56.2 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Approved); UniProt: Nucleus |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 407 aa |
| 🆕 研究新颖性 | 4/10 | ×5 | 20 | PubMed 74篇 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15 | AlphaFold pLDDT: 56.2 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **95/183** |  |
| **归一化总分** |  |  | **51.9/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 EVX1 定位：
- **亚细胞定位**: Nucleoplasm
- **抗体可靠性**: Approved
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Nucleus
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Ebinger JE et al. (2026). "GWAS and Replication Analysis of Apparent Treatment-Resistant Hypertension". *Hypertension*. PMID: 41404655
2. Moran-Rivard L et al. (2001). "Evx1 is a postmitotic determinant of v0 interneuron identity in the spinal cord". *Neuron*. PMID: 11239430
3. Briata P et al. (1995). "Transcriptional repression by the human homeobox protein EVX1 in transfected mammalian cells". *J Biol Chem*. PMID: 7499236
4. Avaron F et al. (2003). "Comparison of even-skipped related gene expression pattern in vertebrates shows an association between expression domain loss and modification of selective constraints on sequences". *Evol Dev*. PMID: 12622731
5. Schulte CJ et al. (2011). "Evx1 is required for joint formation in zebrafish fin dermoskeleton". *Dev Dyn*. PMID: 21509898

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
2. **研究新颖性**: PubMed仅74篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 56.2

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/EVX1)
- [UniProt](https://www.uniprot.org/uniprotkb/P49640)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=EVX1%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/P49640)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。




