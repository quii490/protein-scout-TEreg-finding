---
type: protein-evaluation
gene: "CPNE4"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## CPNE4 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CPNE4/IF_images/378_F4_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CPNE4/IF_images/378_F4_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | CPNE4 |
| 蛋白名称 | Copine-4 |
| 蛋白大小 | 557 aa |
| UniProt ID | [Q96A23](https://www.uniprot.org/uniprotkb/Q96A23) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Approved |
| PubMed 总数 | 22 |
| AlphaFold pLDDT | 87.1 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Approved); UniProt: N/A |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 557 aa |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed 22篇 |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | AlphaFold pLDDT: 87.1 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **122/183** |  |
| **归一化总分** |  |  | **66.7/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 CPNE4 定位：
- **亚细胞定位**: Nucleoplasm
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
1. Goel M et al. (2021). "Molecular studies into cell biological role of Copine-4 in Retinal Ganglion Cells". *PLoS One*. PMID: 34847148
2. Liu X et al. (2020). "Genome-Wide Association Study of Muscle Glycogen in Jingxing Yellow Chicken". *Genes (Basel)*. PMID: 32366026
3. Goel M et al. (2019). "Differential expression and subcellular localization of Copines in mouse retina". *J Comp Neurol*. PMID: 30866042
4. George L et al. (2023). "Genetic improvement of economic traits in Murrah buffalo using significant SNPs from genome-wide association study". *Trop Anim Health Prod*. PMID: 37184817
5. Bossu CM et al. (2022). "Clock-linked genes underlie seasonal migratory timing in a diurnal raptor". *Proc Biol Sci*. PMID: 35506230

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
2. **研究新颖性**: PubMed仅22篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 87.1

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/CPNE4)
- [UniProt](https://www.uniprot.org/uniprotkb/Q96A23)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=CPNE4%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q96A23)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CPNE4/CPNE4-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96A23 |
| SMART | SM00239;SM00327; |
| UniProt Domain [FT] | DOMAIN 3..131; /note="C2 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00041"; DOMAIN 137..264; /note="C2 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00041"; DOMAIN 305..507; /note="VWFA"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00219" |
| InterPro | IPR000008;IPR035892;IPR037768;IPR045052;IPR010734;IPR002035;IPR036465; |
| Pfam | PF00168;PF07002; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000196353-CPNE4/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
