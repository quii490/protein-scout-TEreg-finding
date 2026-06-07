---
type: protein-evaluation
gene: "AKNA"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

## AKNA 核蛋白评估报告（HPA复核救回）

**IF 图像

![[Projects/TEreg-finding/protein-interested/detail/nucleolus/AKNA/IF_images/SK-MEL-30_1.jpg]]**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/AKNA/IF_images/HaCaT_1.jpg]]

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoli fibrillar center; Nucleoplasm (Reliability: Supported)，确认为核蛋白。

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | AKNA |
| 蛋白名称 | Microtubule organization protein AKNA |
| 蛋白大小 | 1439 aa |
| UniProt ID | [Q7Z591](https://www.uniprot.org/uniprotkb/Q7Z591) |
| HPA 核定位 (IF) | Nucleoli fibrillar center; Nucleoplasm |
| HPA 可靠性 | Supported |
| PubMed 总数 | 51 |
| AlphaFold pLDDT | 46.8 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA IF: Nucleoli fibrillar center; Nucleoplasm (Supported); UniProt: Cytoplasm, cytoskeleton, microtubule organizing center, centrosome, centriole; Nucleus |
| 📏 蛋白大小 | 5/10 | ×1 | 5 | 1439 aa |
| 🆕 研究新颖性 | 6/10 | ×5 | 30 | PubMed 51篇 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15 | AlphaFold pLDDT: 46.8 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **102/183** |  |
| **归一化总分** |  |  | **55.7/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 AKNA 定位：
- **亚细胞定位**: Nucleoli fibrillar center; Nucleoplasm
- **抗体可靠性**: Supported
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Cytoplasm, cytoskeleton, microtubule organizing center, centrosome, centriole; Nucleus
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ; ; ; 

![[Projects/TEreg-finding/protein-interested/detail/nucleolus/AKNA/AKNA-PAE.png]]

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Camargo Ortega G et al. (2019). "The centrosome protein AKNA regulates neurogenesis via microtubule organization". *Nature*. PMID: 30787442
2. Ramírez-González A et al. (2021). "Functional Role of AKNA: A Scoping Review". *Biomolecules*. PMID: 34827707
3. Ramírez-González A et al. (2023). "Critical Role of the Transcription Factor AKNA in T-Cell Activation: An Integrative Bioinformatics Approach". *Int J Mol Sci*. PMID: 36835622
4. Martínez-Nava GA et al. (2015). "Cervical cancer-associated promoter polymorphism affects akna expression levels". *Genes Immun*. PMID: 25373726
5. Waseem SS et al. (2021). "A Homozygous AKNA Frameshift Variant Is Associated with Microcephaly in a Pakistani Family". *Genes (Basel)*. PMID: 34680889

**评价**: 基于 PubMed 检索结果。


#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| GIGYF2 | classical fluorescence spectroscopy | 16120600 | — | — |
| ligA | two hybrid pooling approach | 20711500 | — | — |
| purL | two hybrid pooling approach | 20711500 | — | — |
| LMO1 | validated two hybrid | 32296183 | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| — | — | — | — |

**已知复合体成员** (GO Cellular Component):
- 暂无 GO-CC 数据

**IntAct 查询记录**: IntAct: 4 实验验证互作

**评价**: —


### 5. 总体评价

**推荐等级**: ⭐⭐

**核心发现**:
1. **HPA IF 确认为核蛋白**: 原始"核定位≤3"淘汰为误判，HPA实验数据确认为Nucleoli fibrillar center; Nucleoplasm
2. **研究新颖性**: PubMed仅51篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 46.8

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/AKNA)
- [UniProt](https://www.uniprot.org/uniprotkb/Q7Z591)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=AKNA%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q7Z591)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[AKNA-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/AKNA/AKNA-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q7Z591 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR052655;IPR022150; |
| Pfam | PF12443; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000106948-AKNA/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CD2BP2 | Intact | false |
| LMO1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
