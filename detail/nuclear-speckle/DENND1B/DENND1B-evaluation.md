---
type: protein-evaluation
gene: "DENND1B"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

## DENND1B 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nuclear speckles (Reliability: Supported)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/DENND1B/IF_images/487_H2_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/DENND1B/IF_images/487_H2_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | DENND1B |
| 蛋白名称 | DENN domain-containing protein 1B |
| 蛋白大小 | 775 aa |
| UniProt ID | [Q6P3S1](https://www.uniprot.org/uniprotkb/Q6P3S1) |
| HPA 核定位 (IF) | Nuclear speckles |
| HPA 可靠性 | Supported |
| PubMed 总数 | 30 |
| AlphaFold pLDDT | 66.7 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nuclear speckles (Supported); UniProt: Cytoplasm, cytosol; Cytoplasmic vesicle, clathrin-coated vesicle |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 775 aa |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed 30篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold pLDDT: 66.7 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **116/183** |  |
| **归一化总分** |  |  | **63.4/100** |  |

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 DENND1B 定位：
- **亚细胞定位**: Nuclear speckles
- **抗体可靠性**: Supported
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Cytoplasm, cytosol; Cytoplasmic vesicle, clathrin-coated vesicle
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Wallis NJ et al. (2025). "Canine genome-wide association study identifies DENND1B as an obesity gene in dogs and humans". *Science*. PMID: 40048553
2. Ollila HM et al. (2023). "Narcolepsy risk loci outline role of T cell autoimmunity and infectious triggers in narcolepsy". *Nat Commun*. PMID: 37188663
3. Chen D et al. (2022). "circRNA DENND1B inhibits tumorigenicity of clear cell renal cell carcinoma via miR-122-5p/TIMP2 axis". *Open Med (Wars)*. PMID: 36578555
4. Kuhns S et al. (2019). "Rab35 controls cilium length, function and membrane composition". *EMBO Rep*. PMID: 31432619
5. Fiuza BSD et al. (2017). "Polymorphisms in DENND1B gene are associated with asthma and atopy phenotypes in Brazilian children". *Mol Immunol*. PMID: 28668455

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

**推荐等级**: ⭐⭐

**核心发现**:
1. **HPA IF 确认为核蛋白**: 原始"核定位≤3"淘汰为误判，HPA实验数据确认为Nuclear speckles
2. **研究新颖性**: PubMed仅30篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 66.7

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/DENND1B)
- [UniProt](https://www.uniprot.org/uniprotkb/Q6P3S1)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=DENND1B%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q6P3S1)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。




