---
type: protein-evaluation
gene: "IFT140"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## IFT140 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Supported)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/IFT140/IF_images/2176_H1_55_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/IFT140/IF_images/2176_H1_56_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | IFT140 |
| 蛋白名称 | Intraflagellar transport protein 140 homolog |
| 蛋白大小 | 1462 aa |
| UniProt ID | [Q96RY7](https://www.uniprot.org/uniprotkb/Q96RY7) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Supported |
| PubMed 总数 | 75 |
| AlphaFold pLDDT | 80.1 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Supported); UniProt: Cytoplasm, cytoskeleton, cilium basal body; Cytoplasm, cytoskeleton, microtubule organizing center, |
| 📏 蛋白大小 | 5/10 | ×1 | 5 | 1462 aa |
| 🆕 研究新颖性 | 4/10 | ×5 | 20 | PubMed 75篇 |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold pLDDT: 80.1 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **94/183** |  |
| **归一化总分** |  |  | **51.4/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 IFT140 定位：
- **亚细胞定位**: Nucleoplasm
- **抗体可靠性**: Supported
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Cytoplasm, cytoskeleton, cilium basal body; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Cell projection, cilium
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Adam MP et al. (1993). "Nonsyndromic Retinitis Pigmentosa Overview". **. PMID: 20301590
2. Adam MP et al. (1993). "Polycystic Kidney Disease, Autosomal Dominant". **. PMID: 20301424
3. Senum SR et al. (2022). "Monoallelic IFT140 pathogenic variants are an important cause of the autosomal dominant polycystic kidney-spectrum phenotype". *Am J Hum Genet*. PMID: 34890546
4. Adam MP et al. (1993). "Cranioectodermal Dysplasia". **. PMID: 24027799
5. Chang AR et al. (2022). "Exome Sequencing of a Clinical Population for Autosomal Dominant Polycystic Kidney Disease". *JAMA*. PMID: 36573973

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

**推荐等级**: ⭐

**核心发现**:
1. **HPA IF 确认为核蛋白**: 原始"核定位≤3"淘汰为误判，HPA实验数据确认为Nucleoplasm
2. **研究新颖性**: PubMed仅75篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 80.1

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/IFT140)
- [UniProt](https://www.uniprot.org/uniprotkb/Q96RY7)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=IFT140%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q96RY7)


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
| UniProt | Q96RY7 |
| SMART | SM00320; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR056154;IPR056155;IPR056168;IPR056156;IPR015943;IPR036322;IPR001680; |
| Pfam | PF23383;PF23385;PF24762;PF24760; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000187535-IFT140/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| IFT122 | Intact, Biogrid | true |
| IFT43 | Intact, Biogrid, Bioplex | true |
| TULP3 | Intact, Biogrid, Bioplex | true |
| ACSL3 | Intact | false |
| CIAO2A | Bioplex | false |
| CIB2 | Bioplex | false |
| D2HGDH | Bioplex | false |
| DHFR | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
