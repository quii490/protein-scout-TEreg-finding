---
type: protein-evaluation
gene: "PLD3"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## PLD3 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PLD3/IF_images/621_B9_2_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PLD3/IF_images/621_B9_3_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PLD3 |
| 蛋白名称 | 5'-3' exonuclease PLD3 |
| 蛋白大小 | 490 aa |
| UniProt ID | [Q8IV08](https://www.uniprot.org/uniprotkb/Q8IV08) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Approved |
| PubMed 总数 | 77 |
| AlphaFold pLDDT | 91.2 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Approved); UniProt: Endoplasmic reticulum membrane; Lysosome lumen; Early endosome membrane; Late endosome membrane; Gol |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 490 aa |
| 🆕 研究新颖性 | 4/10 | ×5 | 20 | PubMed 77篇 |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | AlphaFold pLDDT: 91.2 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **102/183** |  |
| **归一化总分** |  |  | **55.7/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 PLD3 定位：
- **亚细胞定位**: Nucleoplasm
- **抗体可靠性**: Approved
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Endoplasmic reticulum membrane; Lysosome lumen; Early endosome membrane; Late endosome membrane; Golgi apparatus membrane
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Karch CM & Goate AM (2015). "Alzheimer's disease risk genes and mechanisms of disease pathogenesis". *Biol Psychiatry*. PMID: 24951455
2. Singh S et al. (2024). "PLD3 and PLD4 synthesize S,S-BMP, a key phospholipid enabling lipid degradation in lysosomes". *Cell*. PMID: 39423811
3. Si S et al. (2024). "Identification of novel therapeutic targets for chronic kidney disease and kidney function by integrating multi-omics proteome with transcriptome". *Genome Med*. PMID: 38898508
4. Coarelli G et al. (2023). "Autosomal dominant cerebellar ataxias: new genes and progress towards treatments". *Lancet Neurol*. PMID: 37479376
5. Van Acker ZP et al. (2023). "Phospholipase D3 degrades mitochondrial DNA to regulate nucleotide signaling and APP metabolism". *Nat Commun*. PMID: 37225734

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
2. **研究新颖性**: PubMed仅77篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 91.2

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/PLD3)
- [UniProt](https://www.uniprot.org/uniprotkb/Q8IV08)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=PLD3%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q8IV08)


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
| UniProt | Q8IV08 |
| SMART | SM00155; |
| UniProt Domain [FT] | DOMAIN 196..223; /note="PLD phosphodiesterase 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00153"; DOMAIN 411..437; /note="PLD phosphodiesterase 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00153" |
| InterPro | IPR050874;IPR032803;IPR001736; |
| Pfam | PF13918; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000105223-PLD3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BCAP31 | Biogrid | false |
| CFTR | Biogrid | false |
| CLEC4D | Biogrid | false |
| CLEC4E | Biogrid | false |
| CNIH3 | Intact | false |
| CTSS | Biogrid | false |
| DPP4 | Biogrid | false |
| FBXO6 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
