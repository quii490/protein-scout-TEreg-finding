---
type: protein-evaluation
gene: "PCTP"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## PCTP 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoli; Nucleoplasm (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/PCTP/IF_images/1294_B8_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/PCTP/IF_images/1294_B8_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PCTP |
| 蛋白名称 | Phosphatidylcholine transfer protein |
| 蛋白大小 | 214 aa |
| UniProt ID | [Q9UKL6](https://www.uniprot.org/uniprotkb/Q9UKL6) |
| HPA 核定位 (IF) | Nucleoli; Nucleoplasm |
| HPA 可靠性 | Approved |
| PubMed 总数 | 91 |
| AlphaFold pLDDT | 93.1 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA IF: Nucleoli; Nucleoplasm (Approved); UniProt: Cytoplasm |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 214 aa |
| 🆕 研究新颖性 | 2/10 | ×5 | 10 | PubMed 91篇 |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | AlphaFold pLDDT: 93.1 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **96/183** |  |
| **归一化总分** |  |  | **52.5/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 PCTP 定位：
- **亚细胞定位**: Nucleoli; Nucleoplasm
- **抗体可靠性**: Approved
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Cytoplasm
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Luo S et al. (2025). "Insulinoma detection on low-dose pancreatic CT perfusion: comparing with conventional contrast-enhanced CT and MRI". *Insights Imaging*. PMID: 40120059
2. Abraham S et al. (2021). "PCTP contributes to human platelet activation by enhancing dense granule secretion". *Thromb Res*. PMID: 33770537
3. Kang HW et al. (2009). "Mice lacking Pctp /StarD2 exhibit increased adaptive thermogenesis and enlarged mitochondria in brown adipose tissue". *J Lipid Res*. PMID: 19502644
4. Kang HW et al. (2010). "PC-TP/StARD2: Of membranes and metabolism". *Trends Endocrinol Metab*. PMID: 20338778
5. Balasubramanian P et al. (2019). "Speed and energy optimized quasi-delay-insensitive block carry lookahead adder". *PLoS One*. PMID: 31226125

**评价**: 基于 PubMed 检索结果。


#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| VAPA | anti tag coimmunoprecipitation | 28514442 | — | — |
| squalene | affinity chromatography technology | 25159688 | — | — |
| lanosterol | affinity chromatography technology | 25159688 | — | — |
| Taurocholic acid | affinity chromatography technology | 25159688 | — | — |
| AGTRAP | validated two hybrid | 25416956 | — | — |
| RANGRF | anti tag coimmunoprecipitation | 33961781 | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| — | — | — | — |

**已知复合体成员** (GO Cellular Component):
- GO: Cytoplasm

**IntAct 查询记录**: IntAct: 6 实验验证互作

**评价**: 基于 IntAct + UniProt GO-CC 综合分析。


### 5. 总体评价

**推荐等级**: ⭐

**核心发现**:
1. **HPA IF 确认为核蛋白**: 原始"核定位≤3"淘汰为误判，HPA实验数据确认为Nucleoli; Nucleoplasm
2. **研究新颖性**: PubMed仅91篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 93.1

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/PCTP)
- [UniProt](https://www.uniprot.org/uniprotkb/Q9UKL6)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=PCTP%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q9UKL6)


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
| UniProt | Q9UKL6 |
| SMART | SM00234; |
| UniProt Domain [FT] | DOMAIN 1..212; /note="START"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00197" |
| InterPro | IPR041950;IPR023393;IPR002913;IPR051213; |
| Pfam | PF01852; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000141179-PCTP/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ACOT13 | Biogrid | false |
| AGTRAP | Intact | false |
| PAX3 | Biogrid | false |
| RAD23B | Bioplex | false |
| TPPP | Bioplex | false |
| UBB | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
