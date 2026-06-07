---
type: protein-evaluation
gene: "CCDC148"
date: 2026-06-02
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CCDC148 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CCDC148 / CCDC148 |
| 蛋白全名 | Coiled-coil domain-containing protein 148 |
| 蛋白大小 | 591 aa / 71.1 kDa |
| UniProt ID | Q8NFR7 |
| 子定位分类 | nucleolus |
| HPA IF 主定位 | Nucleoplasm, Nucleoli, Nucleoli rim |
| HPA IF 附加定位 | 无 |
| HPA Reliability | Uncertain |
| 评估日期 | 2026-06-02 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | x4 | 28 | HPA主定位核 |
| 蛋白大小 | 10/10 | x1 | 10 | 591 aa (200-800 aa ideal range) |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed=4 (Extremely novel) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold中等(pLDDT=78.9, >70%=75.6%) |
| 调控结构域 | 7/10 | x2 | 14 | 新颖蛋白基线，无注释结构域 |
| PPI网络 | 6/10 | x3 | 18 | STRING实验分>0.5 (1条) |
| 互证加分 | — | max+3 | +0.5 | IntAct实验互作丰富(10条) (+0.5) |
| **加权总分** | | | **141.5/180** | |
| **归一化总分 (÷1.83)** | | | **77.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | Nucleoplasm, Nucleoli, Nucleoli rim | Uncertain |
| UniProt | 无UniProt注释 | Swiss-Prot/TrEMBL |
| GO-CC | 无 | |

暂无PAE图

暂无HPA IF图像数据。

**结论**: HPA主定位核

#### 3.2 蛋白大小评估

591 aa (200-800 aa ideal range)

**评价**: 591 aa / 71.1 kDa，适宜大小的蛋白，适合常规生化实验和结构生物学分析。

**评分: 10/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 4 |
| PubMed symbol_only | 8 |
| PubMed broad | 8 |
| 别名 | CCDC148 |
| 新颖性分级 | Extremely novel |

**评价**: 仅 PubMed 4 篇 (strict)，极度新颖。该蛋白几乎未被系统研究，是探索新型核蛋白功能的绝佳候选。

**评分: 10/10**。

**关键文献**:
1. **A non-small cell lung carcinoma patient responded to crizotinib therapy after alectinib-induced interstitial lung disease.** *Zhejiang da xue xue bao. Yi xue ban = Journal of Zhejiang University. Medical sciences* (2023 Oct 8) PMID:37899398 -- Sun W et al.
2. **Haplotype association mapping of acute lung injury in mice implicates activin a receptor, type 1.** *American journal of respiratory and critical care medicine* (2011 Jun 1) PMID:21297076 -- Leikauf GD et al.
3. **The plasma peptides of ovarian cancer.** *Clinical proteomics* (2018) PMID:30598658 -- Dufresne J et al.
4. **Identification of Specific Tumor Markers in Vulvar Carcinoma Through Extensive Human Papillomavirus DNA Characterization Using Next Generation Sequencing Method.** *Journal of lower genital tract disease* (2020 Jan) PMID:31860576 -- Thomas J et al.


#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 78.9 |
| pLDDT > 90 (Very High) | 35.2% |
| pLDDT 70-90 (High) | 40.4% |
| pLDDT 50-70 (Medium) | 16.6% |
| pLDDT < 50 (Low) | 7.8% |
| 有序区域 (pLDDT>70) 占比 | 75.6% |
| AlphaFold 版本 | v6 |
| 实验结构 (PDB) | 无 |

暂无PAE图

**评价**: AlphaFold 中等质量（pLDDT=78.9，有序区域 76%）。作为新颖蛋白，此水平可接受。

**评分: 7/10**。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | 无注释 |
| Pfam | 无注释 |

**染色质调控潜力分析**: 存在注释结构域（0个），但未发现明确染色质/DNA结合域。新颖蛋白基线不扣分。

**评分: 7/10**。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4, top 10):

| Partner | Score | 实验分 | 调控相关? |
|---------|-------|--------|----------|
| TEX9 | 0.631 | 0.545 | — |
| LRRC49 | 0.537 | 0.000 | — |
| MORN3 | 0.472 | 0.000 | — |
| CCNI2 | 0.451 | 0.000 | — |
| LTF | 0.428 | 0.428 | — |
| SCGB1D1 | 0.428 | 0.428 | — |
| UPP2 | 0.427 | 0.000 | — |
| C11orf65 | 0.425 | 0.000 | — |
| SAT1 | 0.424 | 0.424 | — |
| SCGB2A1 | 0.422 | 0.421 | — |


**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 调控相关? |
|---------|------|------|----------|
| SAT1 | 0397(two hybrid array) | pubmed:19060904|imex | — |
| STXBP1 | 0399(two hybrid fragment pooling approac | pubmed:31413325|imex | — |
| USHBP1 | 0397(two hybrid array) | imex:IM-23318|pubmed | — |
| SCGB2A1 | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| SCGB1D1 | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| IGHA1 | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| LTF | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| TEX9 | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| LACRT | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |


**已知复合体成员** (GO Cellular Component):
- 无GO-CC注释

**PPI 互证分析**:
- STRING partners (score>0.4): 12
- IntAct 物理互作: 9
- 调控相关比例: 0/12 (0%)

**评价**: STRING实验分>0.5 (1条)

**评分: 6/10**。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 定位 | UniProt + HPA | Non-nuclear + Nucleoplasm/Nucleoli | 待确认 |
| 结构域 | InterPro + Pfam | 0个域 | 无注释 |
| PPI | STRING + IntAct | 12 + 9 | 数据充分 |

**互证加分明细**:
- IntAct实验互作丰富(10条) (+0.5)
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐⭐ (77.3/100)

**核心优势**:
1. Extremely novel -- PubMed=4篇
2. HPA主定位核

**风险/不确定性**:
1. HPA IF图像可进一步分析
2. 结构数据可接受

**下一步建议**:
- [ ] 获取 HPA IF 图像确认核定位
- [ ] 查阅最新关键文献补充功能细节
- [ ] 设计体外 DNA/染色质结合实验

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NFR7
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CCDC148
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NFR7
- STRING: https://string-db.org/cgi/network?identifiers=CCDC148&species=9606

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8NFR7 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR039902; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000153237-CCDC148/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| SAT1 | Intact, Biogrid | true |
| GOLGB1 | Biogrid | false |
| USHBP1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
