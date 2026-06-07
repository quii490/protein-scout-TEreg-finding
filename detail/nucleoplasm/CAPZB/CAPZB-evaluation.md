---
type: protein-evaluation
gene: "CAPZB"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## CAPZB 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CAPZB/IF_images/333_G3_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CAPZB/IF_images/333_G3_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | CAPZB |
| 蛋白名称 | F-actin-capping protein subunit beta |
| 蛋白大小 | 272 aa |
| UniProt ID | [P47756](https://www.uniprot.org/uniprotkb/P47756) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Approved |
| PubMed 总数 | 65 |
| AlphaFold pLDDT | 91.0 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Approved); UniProt: Cytoplasm, cytoskeleton; Cytoplasm, myofibril, sarcomere |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 272 aa |
| 🆕 研究新颖性 | 4/10 | ×5 | 20 | PubMed 65篇 |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | AlphaFold pLDDT: 91.0 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **102/183** |  |
| **归一化总分** |  |  | **55.7/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 CAPZB 定位：
- **亚细胞定位**: Nucleoplasm
- **抗体可靠性**: Approved
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Cytoplasm, cytoskeleton; Cytoplasm, myofibril, sarcomere
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Fan H et al. (2024). "Identification and validation of differentially expressed disulfidptosis-related genes in hypertrophic cardiomyopathy". *Mol Med*. PMID: 39701955
2. Yeat NY et al. (2025). "Bro1 proteins determine tumor immune evasion and metastasis by controlling secretion or degradation of multivesicular bodies". *Dev Cell*. PMID: 40185104
3. Cai X et al. (2024). "CAPZB mRNA is a novel biomarker for cervical high-grade squamous lesions". *Sci Rep*. PMID: 39209986
4. Zhao H et al. (2024). "Novel insights of disulfidptosis-mediated immune microenvironment regulation in atherosclerosis based on bioinformatics analyses". *Sci Rep*. PMID: 39521794
5. Zhang K et al. (2024). "Disulfidptosis-related gene expression reflects the prognosis of drug-resistant cancer patients and inhibition of MYH9 reverses sorafenib resistance". *Transl Oncol*. PMID: 39146597

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
2. **研究新颖性**: PubMed仅65篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 91.0

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/CAPZB)
- [UniProt](https://www.uniprot.org/uniprotkb/P47756)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=CAPZB%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/P47756)


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
| UniProt | P47756 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR037282;IPR042276;IPR001698;IPR043175;IPR019771; |
| Pfam | PF01115; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000077549-CAPZB/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ACTB | Biogrid, Opencell | true |
| ACTC1 | Biogrid, Opencell | true |
| ACTG1 | Biogrid, Opencell | true |
| ACTR10 | Biogrid, Opencell | true |
| ACTR1A | Biogrid, Opencell | true |
| ACTR1B | Biogrid, Opencell | true |
| ARAP1 | Biogrid, Opencell | true |
| ARHGAP17 | Biogrid, Opencell | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
