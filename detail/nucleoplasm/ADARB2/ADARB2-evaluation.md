---
type: protein-evaluation
gene: "ADARB2"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## ADARB2 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ADARB2/IF_images/2062_G3_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ADARB2/IF_images/2062_G3_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | ADARB2 |
| 蛋白名称 | Inactive double-stranded RNA-specific editase B2 |
| 蛋白大小 | 739 aa |
| UniProt ID | [Q9NS39](https://www.uniprot.org/uniprotkb/Q9NS39) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Approved |
| PubMed 总数 | 76 |
| AlphaFold pLDDT | 71.2 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Approved); UniProt: Nucleus |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 739 aa |
| 🆕 研究新颖性 | 4/10 | ×5 | 20 | PubMed 76篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold pLDDT: 71.2 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **96/183** |  |
| **归一化总分** |  |  | **52.5/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 ADARB2 定位：
- **亚细胞定位**: Nucleoplasm
- **抗体可靠性**: Approved
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Nucleus
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Berkhout JB et al. (2024). "An integrated single-cell RNA-seq atlas of the mouse hypothalamic paraventricular nucleus links transcriptomic and functional types". *J Neuroendocrinol*. PMID: 38281730
2. Li W et al. (2023). "The allelic regulation of tumor suppressor ADARB2 in papillary thyroid carcinoma". *Endocr Relat Cancer*. PMID: 36305508
3. Kolenda T et al. (2025). "Expression Profile and Clinical Relevance of ADAR Family Genes in Head and Neck Squamous Cell Carcinoma". *Genes (Basel)*. PMID: 41300768
4. Hirose T et al. (2014). "NEAT1 long noncoding RNA regulates transcription via protein sequestration within subnuclear bodies". *Mol Biol Cell*. PMID: 24173718
5. Yu S et al. (2024). "Integrated analysis of circRNA regulation with ADARB2 enrichment in inhibitory neurons". *Comput Biol Med*. PMID: 39341111

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
2. **研究新颖性**: PubMed仅76篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 71.2

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/ADARB2)
- [UniProt](https://www.uniprot.org/uniprotkb/Q9NS39)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=ADARB2%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q9NS39)


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
| UniProt | Q9NS39 |
| SMART | SM00552;SM00358; |
| UniProt Domain [FT] | DOMAIN 125..191; /note="DRBM 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00266"; DOMAIN 274..341; /note="DRBM 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00266"; DOMAIN 408..735; /note="A to I editase"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00240" |
| InterPro | IPR002466;IPR044460;IPR014720; |
| Pfam | PF02137;PF00035; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000185736-ADARB2/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
