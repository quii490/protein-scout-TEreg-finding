---
type: protein-evaluation
gene: "CCDC12"
date: 2026-06-02
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CCDC12 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CCDC12 / CCDC12 |
| 蛋白全名 | Coiled-coil domain-containing protein 12 |
| 蛋白大小 | 166 aa / 19.2 kDa |
| UniProt ID | Q8WUD4 |
| 子定位分类 | nucleoplasm |
| HPA IF 主定位 | Nucleoplasm |
| HPA IF 附加定位 | 无 |
| HPA Reliability | Supported |
| 评估日期 | 2026-06-02 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | x4 | 28 | HPA主定位核 |
| 蛋白大小 | 8/10 | x1 | 8 | 166 aa (acceptable range) |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed=12 (Extremely novel) |
| 三维结构 | 9/10 | x3 | 27 | PDB实验结构(2条目) + AlphaFold质量(pLDDT=75.7) |
| 调控结构域 | 7/10 | x2 | 14 | 新颖蛋白基线，无注释结构域 |
| PPI网络 | 6/10 | x3 | 18 | STRING实验分>0.5 (9条) |
| 互证加分 | — | max+3 | +2.0 | PDB实验结构(2条目) (+1.0); IntAct实验互作丰富(15条) (+0.5); STRING实验分>0.7 (+0.5) |
| **加权总分** | | | **147.0/180** | |
| **归一化总分 (÷1.83)** | | | **80.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | Nucleoplasm | Supported |
| UniProt | 无UniProt注释 | Swiss-Prot/TrEMBL |
| GO-CC | nucleoplasm (TAS:Reactome); post-mRNA release spliceosomal complex (IBA:GO_Central); U2-type spliceosomal complex (IBA:GO_Central) | |

暂无PAE图

暂无HPA IF图像数据。

**结论**: HPA主定位核

#### 3.2 蛋白大小评估

166 aa (acceptable range)

**评价**: 166 aa / 19.2 kDa，适宜大小的蛋白，适合常规生化实验和结构生物学分析。

**评分: 8/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 12 |
| PubMed symbol_only | 17 |
| PubMed broad | 17 |
| 别名 | CCDC12 |
| 新颖性分级 | Extremely novel |

**评价**: 仅 PubMed 12 篇 (strict)，极度新颖。该蛋白几乎未被系统研究，是探索新型核蛋白功能的绝佳候选。

**评分: 10/10**。

**关键文献**:
1. **CCDC12 gene methylation in peripheral blood as a potential biomarker for breast cancer detection.** *Biomarkers : biochemical indicators of exposure, response, and susceptibility to chemicals* (2024 Jul) PMID:38776382 -- Liu J et al.
2. **Genetic analysis in African ancestry populations reveals genetic contributors to lung cancer susceptibility.** *American journal of human genetics* (2025 Sep 4) PMID:40829600 -- Betti MJ et al.
3. **HBV Integration-mediated Cell Apoptosis in HepG2.2.15.** *Journal of Cancer* (2019) PMID:31417659 -- Hu X et al.
4. **Integrated analysis of transcriptome and genome variations in pediatric T cell acute lymphoblastic leukemia: data from north Indian tertiary care center.** *BMC cancer* (2024 Mar 8) PMID:38459434 -- Singh M et al.
5. **Genome-Wide Association Meta-Analysis Reveals Novel Juvenile Idiopathic Arthritis Susceptibility Loci.** *Arthritis & rheumatology (Hoboken, N.J.)* (2017 Nov) PMID:28719732 -- McIntosh LA et al.


#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 75.7 |
| pLDDT > 90 (Very High) | 26.5% |
| pLDDT 70-90 (High) | 42.8% |
| pLDDT 50-70 (Medium) | 18.1% |
| pLDDT < 50 (Low) | 12.7% |
| 有序区域 (pLDDT>70) 占比 | 69.3% |
| AlphaFold 版本 | v6 |
| 实验结构 (PDB) | 8RO2 (EM, 3.50 A, Z=1-166); 9FMD (EM, 3.30 A, Z=1-166) |

暂无PAE图

**评价**: 优异的实验结构覆盖 + AlphaFold 补充（pLDDT=75.7，有序区域 69%）。

**评分: 9/10**。

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
| CDC40 | 0.997 | 0.987 | — |
| CRNKL1 | 0.997 | 0.994 | — |
| PRPF19 | 0.989 | 0.988 | — |
| CDC5L | 0.981 | 0.981 | — |
| EFTUD2 | 0.973 | 0.972 | — |
| SYF2 | 0.940 | 0.699 | — |
| PPIL1 | 0.903 | 0.475 | — |
| TCERG1 | 0.900 | 0.840 | — |
| SRRM1 | 0.852 | 0.000 | — |
| RNF113A | 0.848 | 0.000 | — |


**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 调控相关? |
|---------|------|------|----------|
| ATG5 | 0007(anti tag coimmunoprecipitation) | pubmed:20562859|imex | — |
| ARHGEF19 | 0007(anti tag coimmunoprecipitation) | pubmed:32203420|imex | — |
| WDR83 | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| SNRPE | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| SNRPN | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| ELAVL2 | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| SNRNP40 | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| PRPF19 | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| DHX8 | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| KIAA1143 | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |


**已知复合体成员** (GO Cellular Component):
- nucleoplasm (TAS:Reactome)
- post-mRNA release spliceosomal complex (IBA:GO_Central)
- U2-type spliceosomal complex (IBA:GO_Central)

**PPI 互证分析**:
- STRING partners (score>0.4): 15
- IntAct 物理互作: 13
- 调控相关比例: 0/15 (0%)

**评价**: STRING实验分>0.5 (9条)

**评分: 6/10**。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 定位 | UniProt + HPA | Non-nuclear + Nucleoplasm/Nucleoli | 待确认 |
| 结构域 | InterPro + Pfam | 0个域 | 无注释 |
| PPI | STRING + IntAct | 15 + 13 | 数据充分 |

**互证加分明细**:
- PDB实验结构(2条目) (+1.0)
- IntAct实验互作丰富(15条) (+0.5)
- STRING实验分>0.7 (+0.5)
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐⭐ (80.3/100)

**核心优势**:
1. Extremely novel -- PubMed=12篇
2. HPA主定位核

**风险/不确定性**:
1. HPA IF图像可进一步分析
2. 结构数据可接受

**下一步建议**:
- [ ] 获取 HPA IF 图像确认核定位
- [ ] 查阅最新关键文献补充功能细节
- [ ] 设计体外 DNA/染色质结合实验

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WUD4
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CCDC12
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WUD4
- STRING: https://string-db.org/cgi/network?identifiers=CCDC12&species=9606
