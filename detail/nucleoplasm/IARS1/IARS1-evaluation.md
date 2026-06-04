---
type: protein-evaluation
gene: "IARS1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## IARS1 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/IARS1/IF_images/299_G2_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/IARS1/IF_images/299_G2_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | IARS1 |
| 蛋白名称 | Isoleucine--tRNA ligase, cytoplasmic |
| 蛋白大小 | 1262 aa |
| UniProt ID | [P41252](https://www.uniprot.org/uniprotkb/P41252) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Approved |
| PubMed 总数 | 22 |
| AlphaFold pLDDT | 88.8 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Approved); UniProt: Cytoplasm; Cytoplasm, cytosol |
| 📏 蛋白大小 | 5/10 | ×1 | 5 | 1262 aa |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed 22篇 |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | AlphaFold pLDDT: 88.8 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **117/183** |  |
| **归一化总分** |  |  | **63.9/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 IARS1 定位：
- **亚细胞定位**: Nucleoplasm
- **抗体可靠性**: Approved
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Cytoplasm; Cytoplasm, cytosol
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Watanabe M & Sasaki N (2024). "Mechanisms and Future Research Perspectives on Mitochondrial Diseases Associated with Isoleucyl-tRNA Synthetase Gene Mutations". *Genes (Basel)*. PMID: 39062673
2. Chung S et al. (2022). "Regulation of BRCA1 stability through the tandem UBX domains of isoleucyl-tRNA synthetase 1". *Nat Commun*. PMID: 36347866
3. Watanabe Y et al. (2026). "Isoleucyl-tRNA synthetase 1 is essential for embryogenesis in mice". *J Vet Med Sci*. PMID: 41192854
4. Kok G et al. (2025). "Isoleucine-to-valine substitutions support cellular physiology during isoleucine deprivation". *Nucleic Acids Res*. PMID: 39657787
5. Wongkittichote P et al. (2025). "Atypical Presentation of IARS1-Related Disorder: Expanding the Phenotype and Genotype". *JIMD Rep*. PMID: 40365325

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
2. **研究新颖性**: PubMed仅22篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 88.8

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/IARS1)
- [UniProt](https://www.uniprot.org/uniprotkb/P41252)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=IARS1%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/P41252)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。




