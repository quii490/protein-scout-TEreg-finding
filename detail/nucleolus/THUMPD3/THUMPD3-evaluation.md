---
type: protein-evaluation
gene: "THUMPD3"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## THUMPD3 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoli (Reliability: Enhanced)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/THUMPD3/IF_images/393_G1_2_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/THUMPD3/IF_images/393_G1_3_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | THUMPD3 |
| 蛋白名称 | tRNA (guanine(6)-N(2))-methyltransferase THUMP3 |
| 蛋白大小 | 507 aa |
| UniProt ID | [Q9BV44](https://www.uniprot.org/uniprotkb/Q9BV44) |
| HPA 核定位 (IF) | Nucleoli |
| HPA 可靠性 | Enhanced |
| PubMed 总数 | 23 |
| AlphaFold pLDDT | 78.6 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA IF: Nucleoli (Enhanced); UniProt: Cytoplasm |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 507 aa |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed 23篇 |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold pLDDT: 78.6 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **125/183** |  |
| **归一化总分** |  |  | **68.3/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 THUMPD3 定位：
- **亚细胞定位**: Nucleoli
- **抗体可靠性**: Enhanced
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Cytoplasm
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Wang C et al. (2023). "N 2-methylguanosine modifications on human tRNAs and snRNA U6 are important for cell proliferation, protein translation and pre-mRNA splicing". *Nucleic Acids Res*. PMID: 37283053
2. Yuan W et al. (2026). "tRNA m(2)G methyltransferase complex THUMPD3-TRMT112 promotes pancreatic cancer progression and autophagy via modulating TFEB translation". *Mol Cancer*. PMID: 41530782
3. Klimontova M et al. (2024). "PhOxi-seq Detects Enzyme-Dependent m(2)G in Multiple RNA Types". *ACS Chem Biol*. PMID: 39611406
4. Tan Y et al. (2022). "THUMPD3-AS1 Is Correlated with Gastric Cancer and Regulates Cell Function through miR-1252-3p and CXCL17". *Crit Rev Eukaryot Gene Expr*. PMID: 36017917
5. Zhang Z et al. (2023). "LncRNA THUMPD3-AS1 promotes invasion and EMT in gastric cancer by regulating the miR-1297/BCAT1 pathway". *iScience*. PMID: 37705956

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
1. **HPA IF 确认为核蛋白**: 原始"核定位≤3"淘汰为误判，HPA实验数据确认为Nucleoli
2. **研究新颖性**: PubMed仅23篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 78.6

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/THUMPD3)
- [UniProt](https://www.uniprot.org/uniprotkb/Q9BV44)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=THUMPD3%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q9BV44)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。




