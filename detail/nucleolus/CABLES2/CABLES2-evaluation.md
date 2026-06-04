---
type: protein-evaluation
gene: "CABLES2"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## CABLES2 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoli (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/CABLES2/IF_images/1832_B7_2_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/CABLES2/IF_images/1832_B7_7_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | CABLES2 |
| 蛋白名称 | CDK5 and ABL1 enzyme substrate 2 |
| 蛋白大小 | 478 aa |
| UniProt ID | [Q9BTV7](https://www.uniprot.org/uniprotkb/Q9BTV7) |
| HPA 核定位 (IF) | Nucleoli |
| HPA 可靠性 | Approved |
| PubMed 总数 | 22 |
| AlphaFold pLDDT | 59.8 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoli (Approved); UniProt: N/A |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 478 aa |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed 22篇 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15 | AlphaFold pLDDT: 59.8 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **113/183** |  |
| **归一化总分** |  |  | **61.7/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 CABLES2 定位：
- **亚细胞定位**: Nucleoli
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
1. Dinh TTH et al. (2021). "Disruption of entire Cables2 locus leads to embryonic lethality by diminished Rps21 gene expression and enhanced p53 pathway". *Elife*. PMID: 33949947
2. Fachin AL et al. (2009). "Gene expression profiles in radiation workers occupationally exposed to ionizing radiation". *J Radiat Res*. PMID: 19218781
3. Mesa-Eguiagaray I et al. (2025). "Association between methylation quantitative trait loci and colorectal cancer risk, survival and cancer recurrence". *Br J Cancer*. PMID: 40506516
4. Guo X et al. (2021). "Identifying Novel Susceptibility Genes for Colorectal Cancer Risk From a Transcriptome-Wide Association Study of 125,478 Subjects". *Gastroenterology*. PMID: 33058866
5. Hasan ASH et al. (2021). "Characterization of a bicistronic knock-in reporter mouse model for investigating the role of CABLES2 in vivo". *Exp Anim*. PMID: 32779618

**评价**: 基于 PubMed 检索结果。


#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| hsamir106b3p | clash | 23622248 | — | — |

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
1. **HPA IF 确认为核蛋白**: 原始"核定位≤3"淘汰为误判，HPA实验数据确认为Nucleoli
2. **研究新颖性**: PubMed仅22篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 59.8

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/CABLES2)
- [UniProt](https://www.uniprot.org/uniprotkb/Q9BTV7)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=CABLES2%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q9BTV7)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/CABLES2/CABLES2-PAE.png]]




