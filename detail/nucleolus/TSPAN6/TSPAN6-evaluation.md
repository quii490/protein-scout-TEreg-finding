---
type: protein-evaluation
gene: "TSPAN6"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## TSPAN6 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoli fibrillar center (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/TSPAN6/IF_images/1832_C1_2_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/TSPAN6/IF_images/1832_C1_4_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TSPAN6 |
| 蛋白名称 | Tetraspanin-6 |
| 蛋白大小 | 245 aa |
| UniProt ID | [O43657](https://www.uniprot.org/uniprotkb/O43657) |
| HPA 核定位 (IF) | Nucleoli fibrillar center |
| HPA 可靠性 | Approved |
| PubMed 总数 | 25 |
| AlphaFold pLDDT | 88.3 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoli fibrillar center (Approved); UniProt: Membrane |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 245 aa |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed 25篇 |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | AlphaFold pLDDT: 88.3 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **122/183** |  |
| **归一化总分** |  |  | **66.7/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 TSPAN6 定位：
- **亚细胞定位**: Nucleoli fibrillar center
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
1. Monies D et al. (2017). "The landscape of genetic diseases in Saudi Arabia based on the first 1000 diagnostic panels and exomes". *Hum Genet*. PMID: 28600779
2. Huang R et al. (2022). "The role of tetraspanins pan-cancer". *iScience*. PMID: 35992081
3. Wang Z et al. (2025). "Comprehensive molecular characterization of high-stemness gastric cancer cells using single-cell transcriptomics, spatial mapping, and machine learning". *NPJ Precis Oncol*. PMID: 41408440
4. Andrijes R et al. (2021). "Tetraspanin 6 is a regulator of carcinogenesis in colorectal cancer". *Proc Natl Acad Sci U S A*. PMID: 34521767
5. Chen L et al. (2025). "Single-cell and multi-omics analysis identifies TRIM9 as a key ubiquitination regulator in pancreatic cancer". *Front Immunol*. PMID: 41050689

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
1. **HPA IF 确认为核蛋白**: 原始"核定位≤3"淘汰为误判，HPA实验数据确认为Nucleoli fibrillar center
2. **研究新颖性**: PubMed仅25篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 88.3

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/TSPAN6)
- [UniProt](https://www.uniprot.org/uniprotkb/O43657)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=TSPAN6%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/O43657)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。




