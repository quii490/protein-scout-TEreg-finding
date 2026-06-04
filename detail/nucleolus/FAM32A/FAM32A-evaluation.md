---
type: protein-evaluation
gene: "FAM32A"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## FAM32A 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoli; Nucleoplasm (Reliability: Supported)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/FAM32A/IF_images/769_E12_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/FAM32A/IF_images/769_E12_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | FAM32A |
| 蛋白名称 | Protein FAM32A |
| 蛋白大小 | 112 aa |
| UniProt ID | [Q9Y421](https://www.uniprot.org/uniprotkb/Q9Y421) |
| HPA 核定位 (IF) | Nucleoli; Nucleoplasm |
| HPA 可靠性 | Supported |
| PubMed 总数 | 7 |
| AlphaFold pLDDT | 79.5 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA IF: Nucleoli; Nucleoplasm (Supported); UniProt: Nucleus; Nucleus |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 112 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed 7篇 |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold pLDDT: 79.5 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **131/183** |  |
| **归一化总分** |  |  | **71.6/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 FAM32A 定位：
- **亚细胞定位**: Nucleoli; Nucleoplasm
- **抗体可靠性**: Supported
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Nucleus; Nucleus
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Zhan X et al. (2022). "Mechanism of exon ligation by human spliceosome". *Mol Cell*. PMID: 35705093
2. Fica SM et al. (2019). "A human postcatalytic spliceosome structure reveals essential roles of metazoan factors for exon ligation". *Science*. PMID: 30705154
3. Wang W et al. (2021). "Genome-wide DNA methylation analysis of cognitive function in middle and old-aged Chinese monozygotic twins". *J Psychiatr Res*. PMID: 33131831
4. Li C et al. (2025). "Mettl14 Deficiency Promotes Fam32a Expression via m6A Modifications to Facilitate the Hepatocyte G1/S Transition". *J Cell Physiol*. PMID: 41099467
5. Ishizuka T et al. (2025). "Comprehensive identification and functional analysis of fully disordered proteins essential for cell survival". *RNA*. PMID: 41101973

**评价**: 基于 PubMed 检索结果。


#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| NSFL1C | two hybrid pooling approach | 16169070 | — | — |
| EBI-54261817 | clash | 23622248 | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| — | — | — | — |

**已知复合体成员** (GO Cellular Component):
- GO: Nucleus

**IntAct 查询记录**: IntAct: 2 实验验证互作

**评价**: 基于 IntAct + UniProt GO-CC 综合分析。


### 5. 总体评价

**推荐等级**: ⭐⭐⭐

**核心发现**:
1. **HPA IF 确认为核蛋白**: 原始"核定位≤3"淘汰为误判，HPA实验数据确认为Nucleoli; Nucleoplasm
2. **研究新颖性**: PubMed仅7篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 79.5

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/FAM32A)
- [UniProt](https://www.uniprot.org/uniprotkb/Q9Y421)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=FAM32A%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q9Y421)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。




