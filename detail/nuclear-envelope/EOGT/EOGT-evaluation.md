---
type: protein-evaluation
gene: "EOGT"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

## EOGT 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nuclear membrane; Nucleoplasm (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/EOGT/IF_images/222_H3_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/EOGT/IF_images/222_H3_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | EOGT |
| 蛋白名称 | EGF domain-specific O-linked N-acetylglucosamine transferase |
| 蛋白大小 | 527 aa |
| UniProt ID | [Q5NDL2](https://www.uniprot.org/uniprotkb/Q5NDL2) |
| HPA 核定位 (IF) | Nuclear membrane; Nucleoplasm |
| HPA 可靠性 | Approved |
| PubMed 总数 | 42 |
| AlphaFold pLDDT | 91.5 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA IF: Nuclear membrane; Nucleoplasm (Approved); UniProt: Endoplasmic reticulum lumen |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 527 aa |
| 🆕 研究新颖性 | 6/10 | ×5 | 30 | PubMed 42篇 |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | AlphaFold pLDDT: 91.5 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **116/183** |  |
| **归一化总分** |  |  | **63.4/100** |  |

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 EOGT 定位：
- **亚细胞定位**: Nuclear membrane; Nucleoplasm
- **抗体可靠性**: Approved
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Endoplasmic reticulum lumen
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Ogawa M & Okajima T (2019). "Structure and function of extracellular O-GlcNAc". *Curr Opin Struct Biol*. PMID: 30669087
2. Varshney S & Stanley P (2017). "EOGT and O-GlcNAc on secreted and membrane proteins". *Biochem Soc Trans*. PMID: 28408480
3. Deng S et al. (2024). "Novel insights into the roles of migrasome in cancer". *Discov Oncol*. PMID: 38748047
4. Matsumoto K et al. (2021). "Diseases related to Notch glycosylation". *Mol Aspects Med*. PMID: 33341260
5. Tsukamoto Y et al. (2024). "Characterization of galactosyltransferase and sialyltransferase genes mediating the elongation of the extracellular O-GlcNAc glycans". *Biochem Biophys Res Commun*. PMID: 38359610

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
1. **HPA IF 确认为核蛋白**: 原始"核定位≤3"淘汰为误判，HPA实验数据确认为Nuclear membrane; Nucleoplasm
2. **研究新颖性**: PubMed仅42篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 91.5

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/EOGT)
- [UniProt](https://www.uniprot.org/uniprotkb/Q5NDL2)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=EOGT%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q5NDL2)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。




