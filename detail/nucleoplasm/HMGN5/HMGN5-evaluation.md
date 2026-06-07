---
type: protein-evaluation
gene: "HMGN5"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## HMGN5 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Supported)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/HMGN5/IF_images/55_D5_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/HMGN5/IF_images/55_D5_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | HMGN5 |
| 蛋白名称 | High mobility group nucleosome-binding domain-containing protein 5 |
| 蛋白大小 | 282 aa |
| UniProt ID | [P82970](https://www.uniprot.org/uniprotkb/P82970) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Supported |
| PubMed 总数 | 51 |
| AlphaFold pLDDT | 52.8 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Supported); UniProt: Nucleus |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 282 aa |
| 🆕 研究新颖性 | 6/10 | ×5 | 30 | PubMed 51篇 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15 | AlphaFold pLDDT: 52.8 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **103/183** |  |
| **归一化总分** |  |  | **56.3/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 HMGN5 定位：
- **亚细胞定位**: Nucleoplasm
- **抗体可靠性**: Supported
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Nucleus
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Shi Z et al. (2016). "Research advances in HMGN5 and cancer". *Tumour Biol*. PMID: 26700674
2. Rochman M et al. (2010). "HMGN5/NSBP1: a new member of the HMGN protein family that affects chromatin structure and function". *Biochim Biophys Acta*. PMID: 20123071
3. Weng M et al. (2015). "The high-mobility group nucleosome-binding domain 5 is highly expressed in breast cancer and promotes the proliferation and invasion of breast cancer cells". *Tumour Biol*. PMID: 25315189
4. Yao K et al. (2020). "HMGN5 promotes IL-6-induced epithelial-mesenchymal transition of bladder cancer by interacting with Hsp27". *Aging (Albany NY)*. PMID: 32315283
5. Mou J et al. (2022). "HMGN5 Escorts Oncogenic STAT3 Signaling by Regulating the Chromatin Landscape in Breast Cancer Tumorigenesis". *Mol Cancer Res*. PMID: 36066963

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
2. **研究新颖性**: PubMed仅51篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 52.8

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/HMGN5)
- [UniProt](https://www.uniprot.org/uniprotkb/P82970)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=HMGN5%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/P82970)


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
| UniProt | P82970 |
| SMART | SM00527; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR040164;IPR000079; |
| Pfam | PF01101; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000198157-HMGN5/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CBX8 | Biogrid, Opencell | true |
| ACLY | Opencell | false |
| APOBEC3C | Opencell | false |
| ATAD2 | Opencell | false |
| ATAD2B | Opencell | false |
| ATG13 | Opencell | false |
| BANF1 | Opencell | false |
| BARD1 | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
