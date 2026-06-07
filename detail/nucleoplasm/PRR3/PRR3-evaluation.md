---
type: protein-evaluation
gene: "PRR3"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## PRR3 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PRR3/IF_images/1272_H9_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PRR3/IF_images/1272_H9_3_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PRR3 |
| 蛋白名称 | Proline-rich protein 3 |
| 蛋白大小 | 188 aa |
| UniProt ID | [P79522](https://www.uniprot.org/uniprotkb/P79522) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Approved |
| PubMed 总数 | 18 |
| AlphaFold pLDDT | 60.7 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Approved); UniProt: N/A |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 188 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed 18篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold pLDDT: 60.7 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **124/183** |  |
| **归一化总分** |  |  | **67.8/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 PRR3 定位：
- **亚细胞定位**: Nucleoplasm
- **抗体可靠性**: Approved
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: N/A
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Małecki JM et al. (2025). "Identification of substrates and sequence requirements for CARNMT1-mediated histidine methylation of C3H zinc fingers". *J Biol Chem*. PMID: 40473212
2. Buś S et al. (2023). "A New Approach to Detecting Atrial Fibrillation Using Count Statistics of Relative Changes between Consecutive RR Intervals". *J Clin Med*. PMID: 36675616
3. Biczuk B et al. (2024). "pRR30, pRR3.25% and Asymmetrical Entropy Descriptors in Atrial Fibrillation Detection". *Entropy (Basel)*. PMID: 38667850
4. Para A et al. (2007). "PRR3 Is a vascular regulator of TOC1 stability in the Arabidopsis circadian clock". *Plant Cell*. PMID: 18055606
5. Fujiwara S et al. (2008). "Post-translational regulation of the Arabidopsis circadian clock through selective proteolysis and phosphorylation of pseudo-response regulator proteins". *J Biol Chem*. PMID: 18562312

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
2. **研究新颖性**: PubMed仅18篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 60.7

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/PRR3)
- [UniProt](https://www.uniprot.org/uniprotkb/P79522)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=PRR3%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/P79522)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NQS3 |
| SMART | SM00409; |
| UniProt Domain [FT] | DOMAIN 59..165; /note="Ig-like V-type"; DOMAIN 170..258; /note="Ig-like C2-type 1"; DOMAIN 269..354; /note="Ig-like C2-type 2" |
| InterPro | IPR013162;IPR007110;IPR036179;IPR013783;IPR003599;IPR013106;IPR033320;IPR033319;IPR051427; |
| Pfam | PF08205;PF07686; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000204576-PRR3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| APOBEC3C | Intact, Biogrid | true |
| HNRNPK | Intact, Biogrid | true |
| RBMX | Intact, Biogrid | true |
| APOBEC3F | Bioplex | false |
| ASF1A | Intact | false |
| CCDC57 | Intact | false |
| CDKN2AIP | Bioplex | false |
| CLP1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
