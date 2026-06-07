---
type: protein-evaluation
gene: "RPUSD2"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## RPUSD2 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/RPUSD2/IF_images/461_C12_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/RPUSD2/IF_images/461_C12_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | RPUSD2 |
| 蛋白名称 | Pseudouridylate synthase RPUSD2 |
| 蛋白大小 | 545 aa |
| UniProt ID | [Q8IZ73](https://www.uniprot.org/uniprotkb/Q8IZ73) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Approved |
| PubMed 总数 | 4 |
| AlphaFold pLDDT | 74.9 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Approved); UniProt: N/A |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 545 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed 4篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold pLDDT: 74.9 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **126/183** |  |
| **归一化总分** |  |  | **68.9/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 RPUSD2 定位：
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
1. Xu H et al. (2025). "A comprehensive tRNA pseudouridine map uncovers targets dependent on human stand-alone pseudouridine synthases". *Nat Cell Biol*. PMID: 41136621
2. Peula C et al. (2025). "Analysis of the mRNA modification machinery alterations in breast cancer through the SCAN-B cohort". *NAR Cancer*. PMID: 40918643
3. Liu W et al. (2026). "Quantitative analysis of small RNA pseudouridylation reveals interplay of PUS enzymes in tRNA anticodon stem-loop". *Nat Commun*. PMID: 41698914
4. Jin Z et al. (2022). "Integrative multiomics evaluation reveals the importance of pseudouridine synthases in hepatocellular carcinoma". *Front Genet*. PMID: 36437949
5. Zhang P et al. (2012). "Comprehensive gene and microRNA expression profiling reveals the crucial role of hsa-let-7i and its target genes in colorectal cancer metastasis". *Mol Biol Rep*. PMID: 21625861

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
2. **研究新颖性**: PubMed仅4篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 74.9

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/RPUSD2)
- [UniProt](https://www.uniprot.org/uniprotkb/Q8IZ73)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=RPUSD2%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q8IZ73)


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
| UniProt | Q8IZ73 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR020103;IPR006224;IPR006225;IPR006145;IPR050188; |
| Pfam | PF00849; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000166133-RPUSD2/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
