---
type: protein-evaluation
gene: "FOXS1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## FOXS1 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FOXS1/IF_images/555_F10_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FOXS1/IF_images/555_F10_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | FOXS1 |
| 蛋白名称 | Forkhead box protein S1 |
| 蛋白大小 | 330 aa |
| UniProt ID | [O43638](https://www.uniprot.org/uniprotkb/O43638) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Approved |
| PubMed 总数 | 25 |
| AlphaFold pLDDT | 63.0 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Approved); UniProt: Nucleus |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 330 aa |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed 25篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold pLDDT: 63.0 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **118/183** |  |
| **归一化总分** |  |  | **64.5/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 FOXS1 定位：
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
1. Jiang C et al. (2025). "Oxidized LDL-induced FOXS1 mediates cholesterol transport dysfunction and inflammasome activation to drive aortic valve calcification". *Cardiovasc Res*. PMID: 40990096
2. Zhang L et al. (2022). "Forkhead Box S1 mediates epithelial-mesenchymal transition through the Wnt/β-catenin signaling pathway to regulate colorectal cancer progression". *J Transl Med*. PMID: 35864528
3. Lei D et al. (2020). "Forkhead Box S1 Inhibits the Progression of Hepatocellular Carcinoma". *Onco Targets Ther*. PMID: 33235470
4. Wang F & Li S (2022). "Forkhead Box S1 inhibits the progression of lung squamous cell carcinoma cells by mediating Wnt/β-catenin pathway". *Chin J Physiol*. PMID: 36308082
5. Tavares AH et al. (2025). "TGF-β1-dependent expression of FOXS1 attenuates adipogenic potential and enhances a myofibroblast cellular phenotype". *J Biol Chem*. PMID: 40774386

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
1. **HPA IF 确认为核蛋白**: 原始"核定位≤3"淘汰为误判，HPA实验数据确认为Nucleoplasm
2. **研究新颖性**: PubMed仅25篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 63.0

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/FOXS1)
- [UniProt](https://www.uniprot.org/uniprotkb/O43638)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=FOXS1%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/O43638)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。




