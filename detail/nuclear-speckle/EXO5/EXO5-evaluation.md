---
type: protein-evaluation
gene: "EXO5"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## EXO5 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nuclear speckles; Nucleoplasm (Reliability: Supported)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/EXO5/IF_images/256_C6_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/EXO5/IF_images/256_C6_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | EXO5 |
| 蛋白名称 | Exonuclease V |
| 蛋白大小 | 373 aa |
| UniProt ID | [Q9H790](https://www.uniprot.org/uniprotkb/Q9H790) |
| HPA 核定位 (IF) | Nuclear speckles; Nucleoplasm |
| HPA 可靠性 | Supported |
| PubMed 总数 | 29 |
| AlphaFold pLDDT | 80.0 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA IF: Nuclear speckles; Nucleoplasm (Supported); UniProt: Nucleus; Cytoplasm, cytosol |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 373 aa |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed 29篇 |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold pLDDT: 80.0 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **123/183** |  |
| **归一化总分** |  |  | **67.2/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 EXO5 定位：
- **亚细胞定位**: Nuclear speckles; Nucleoplasm
- **抗体可靠性**: Supported
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Nucleus; Cytoplasm, cytosol
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Knijnenburg TA et al. (2018). "Genomic and Molecular Landscape of DNA Damage Repair Deficiency across The Cancer Genome Atlas". *Cell Rep*. PMID: 29617664
2. Zaman Q et al. (2021). "Exonuclease 5 is dispensable for meiotic progression and male fertility in mouse". *Gene*. PMID: 33164760
3. Sparks JL et al. (2019). "The roles of fission yeast exonuclease 5 in nuclear and mitochondrial genome stability". *DNA Repair (Amst)*. PMID: 31563844
4. Burgers PM et al. (2010). "Yeast exonuclease 5 is essential for mitochondrial genome maintenance". *Mol Cell Biol*. PMID: 20086101
5. Hambarde S et al. (2021). "EXO5-DNA structure and BLM interactions direct DNA resection critical for ATR-dependent replication restart". *Mol Cell*. PMID: 34197737

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
1. **HPA IF 确认为核蛋白**: 原始"核定位≤3"淘汰为误判，HPA实验数据确认为Nuclear speckles; Nucleoplasm
2. **研究新颖性**: PubMed仅29篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 80.0

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/EXO5)
- [UniProt](https://www.uniprot.org/uniprotkb/Q9H790)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=EXO5%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q9H790)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。




