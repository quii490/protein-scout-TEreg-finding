---
type: protein-evaluation
gene: "SPSB4"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## SPSB4 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/SPSB4/IF_images/1687_E2_2_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/SPSB4/IF_images/1687_E2_3_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SPSB4 |
| 蛋白名称 | SPRY domain-containing SOCS box protein 4 |
| 蛋白大小 | 273 aa |
| UniProt ID | [Q96A44](https://www.uniprot.org/uniprotkb/Q96A44) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Approved |
| PubMed 总数 | 18 |
| AlphaFold pLDDT | 89.1 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Approved); UniProt: Cytoplasm; Cytoplasm, cytosol |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 273 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed 18篇 |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | AlphaFold pLDDT: 89.1 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **132/183** |  |
| **归一化总分** |  |  | **72.1/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 SPSB4 定位：
- **亚细胞定位**: Nucleoplasm
- **抗体可靠性**: Approved
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Cytoplasm; Cytoplasm, cytosol
- **结构域**: None identified
- **关键词**: ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Selinger M et al. (2022). "Integrative RNA profiling of TBEV-infected neurons and astrocytes reveals potential pathogenic effectors". *Comput Struct Biotechnol J*. PMID: 35685361
2. Li K et al. (2024). "Subtle Structural Differences Affect the Inhibitory Potency of RGD-Containing Cyclic Peptide Inhibitors Targeting SPSB Proteins". *Int J Mol Sci*. PMID: 38928469
3. Pragasam AK et al. (2025). "Invasive Salmonella Typhimurium colonizes gallbladder and contributes to gallbladder carcinogenesis through activation of host epigenetic modulator KDM6B". *Cancer Lett*. PMID: 40074067
4. Suen TC & DeBruyne JP (2023). "Lysine-independent ubiquitination and degradation of REV-ERBα involves a bi-functional degradation control sequence at its N-terminus". *bioRxiv*. PMID: 37205588
5. Sadek MM et al. (2018). "A Cyclic Peptide Inhibitor of the iNOS-SPSB Protein-Protein Interaction as a Potential Anti-Infective Agent". *ACS Chem Biol*. PMID: 30226743

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
2. **研究新颖性**: PubMed仅18篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 89.1

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/SPSB4)
- [UniProt](https://www.uniprot.org/uniprotkb/Q96A44)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=SPSB4%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q96A44)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。




