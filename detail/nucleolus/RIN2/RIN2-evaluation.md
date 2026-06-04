---
type: protein-evaluation
gene: "RIN2"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## RIN2 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoli (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/RIN2/IF_images/440_E5_2_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/RIN2/IF_images/440_E5_3_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | RIN2 |
| 蛋白名称 | Ras and Rab interactor 2 |
| 蛋白大小 | 895 aa |
| UniProt ID | [Q8WYP3](https://www.uniprot.org/uniprotkb/Q8WYP3) |
| HPA 核定位 (IF) | Nucleoli |
| HPA 可靠性 | Approved |
| PubMed 总数 | 56 |
| AlphaFold pLDDT | 63.3 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoli (Approved); UniProt: Cytoplasm |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 895 aa |
| 🆕 研究新颖性 | 6/10 | ×5 | 30 | PubMed 56篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold pLDDT: 63.3 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **104/183** |  |
| **归一化总分** |  |  | **56.8/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 RIN2 定位：
- **亚细胞定位**: Nucleoli
- **抗体可靠性**: Approved
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Cytoplasm
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Rosato S et al. (2016). "RIN2 syndrome: Expanding the clinical phenotype". *Am J Med Genet A*. PMID: 27277385
2. Aslanger AD et al. (2014). "Newly described clinical features in two siblings with MACS syndrome and a novel mutation in RIN2". *Am J Med Genet A*. PMID: 24449201
3. Kawasaki T et al. (2005). "A duplicated pair of Arabidopsis RING-finger E3 ligases contribute to the RPM1- and RPS2-mediated hypersensitive response". *Plant J*. PMID: 16212605
4. Muraki N et al. (2022). "Resistance to mutant KRAS(V12)-induced senescence in an hTERT/Cdk4-immortalized normal human bronchial epithelial cell line". *Exp Cell Res*. PMID: 35149086
5. Kameli R et al. (2020). "Leukoencephalopathy in RIN2 syndrome: Novel mutation and expansion of clinical spectrum". *Eur J Med Genet*. PMID: 30769224

**评价**: 基于 PubMed 检索结果。


#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| GKAP1 | anti tag coimmunoprecipitation | 33961781 | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| — | — | — | — |

**已知复合体成员** (GO Cellular Component):
- GO: Cytoplasm

**IntAct 查询记录**: IntAct: 1 实验验证互作

**评价**: 基于 IntAct + UniProt GO-CC 综合分析。


### 5. 总体评价

**推荐等级**: ⭐⭐

**核心发现**:
1. **HPA IF 确认为核蛋白**: 原始"核定位≤3"淘汰为误判，HPA实验数据确认为Nucleoli
2. **研究新颖性**: PubMed仅56篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 63.3

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/RIN2)
- [UniProt](https://www.uniprot.org/uniprotkb/Q8WYP3)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=RIN2%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q8WYP3)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。




