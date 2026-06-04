---
type: protein-evaluation
gene: "CCDC97"
date: 2026-06-02
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CCDC97 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CCDC97 / CCDC97 |
| 蛋白全名 | Coiled-coil domain-containing protein 97 |
| 蛋白大小 | 343 aa / 38.9 kDa |
| UniProt ID | Q96F63 |
| 子定位分类 | nucleus-cytoplasm |
| HPA IF 主定位 | Nucleoplasm |
| HPA IF 附加定位 | Plasma membrane, Cytosol |
| HPA Reliability | Supported |
| 评估日期 | 2026-06-02 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 6/10 | x4 | 24 | HPA主定位核，附加Cytosol/Vesicles |
| 蛋白大小 | 10/10 | x1 | 10 | 343 aa (200-800 aa ideal range) |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed=2 (Extremely novel) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold中等(pLDDT=77.0, >70%=69.1%) |
| 调控结构域 | 7/10 | x2 | 14 | 新颖蛋白基线，无注释结构域 |
| PPI网络 | 6/10 | x3 | 18 | STRING实验分>0.5 (11条) |
| 互证加分 | — | max+3 | +2.0 | UniProt核定位 + HPA IF核验证一致 (+1.0); IntAct实验互作丰富(15条) (+0.5); STRING实验分>0.7 (+0.5) |
| **加权总分** | | | **139.0/180** | |
| **归一化总分 (÷1.83)** | | | **76.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | Nucleoplasm, Plasma membrane, Cytosol | Supported |
| UniProt | Nucleus (ECO:0000305) | Swiss-Prot/TrEMBL |
| GO-CC | nucleus (IEA:UniProtKB-SubCell) | |

暂无PAE图

暂无HPA IF图像数据。

**结论**: HPA主定位核，附加Cytosol/Vesicles

#### 3.2 蛋白大小评估

343 aa (200-800 aa ideal range)

**评价**: 343 aa / 38.9 kDa，适宜大小的蛋白，适合常规生化实验和结构生物学分析。

**评分: 10/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 2 |
| PubMed symbol_only | 6 |
| PubMed broad | 6 |
| 别名 | CCDC97 |
| 新颖性分级 | Extremely novel |

**评价**: 仅 PubMed 2 篇 (strict)，极度新颖。该蛋白几乎未被系统研究，是探索新型核蛋白功能的绝佳候选。

**评分: 10/10**。

**关键文献**:
1. **Kinome-Wide siRNA Screening Identifies DYRK1B as a Potential Therapeutic Target for Triple-Negative Breast Cancer Cells.** *Cancers* (2021 Nov 18) PMID:34830933 -- Chang CC et al.
2. **Selection and Validation of Reference Genes for Gene Expression Studies in an Equine Adipose-Derived Mesenchymal Stem Cell Differentiation Model by Proteome Analysis and Reverse-Transcriptase Quantitative Real-Time PCR.** *Genes* (2023 Mar 8) PMID:36980946 -- Riveroll AL et al.


#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 77.0 |
| pLDDT > 90 (Very High) | 39.7% |
| pLDDT 70-90 (High) | 29.4% |
| pLDDT 50-70 (Medium) | 12.0% |
| pLDDT < 50 (Low) | 19.0% |
| 有序区域 (pLDDT>70) 占比 | 69.1% |
| AlphaFold 版本 | v6 |
| 实验结构 (PDB) | 无 |

暂无PAE图

**评价**: AlphaFold 中等质量（pLDDT=77.0，有序区域 69%）。作为新颖蛋白，此水平可接受。

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
| SF3B6 | 0.907 | 0.887 | — |
| SF3B5 | 0.896 | 0.881 | — |
| SF3B1 | 0.843 | 0.822 | — |
| SF3B3 | 0.806 | 0.785 | — |
| SF3A2 | 0.799 | 0.511 | — |
| SF3A1 | 0.799 | 0.629 | — |
| SF3B4 | 0.788 | 0.592 | — |
| SF3A3 | 0.765 | 0.626 | — |
| TTC33 | 0.728 | 0.728 | — |
| ZRSR2 | 0.713 | 0.703 | — |


**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 调控相关? |
|---------|------|------|----------|
| MAPK14 | 0398(two hybrid pooling approach) | pubmed:20936779|imex | — |
| SF3B1 | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| JUN | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| ATF1 | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| SF3A3 | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| SF3B2 | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| SF3B3 | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| SF3B4 | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| SF3A2 | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| SF3A1 | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |


**已知复合体成员** (GO Cellular Component):
- nucleus (IEA:UniProtKB-SubCell)

**PPI 互证分析**:
- STRING partners (score>0.4): 15
- IntAct 物理互作: 13
- 调控相关比例: 0/15 (0%)

**评价**: STRING实验分>0.5 (11条)

**评分: 6/10**。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 定位 | UniProt + HPA | Nucleus + Nucleoplasm/Nucleoli | 一致 |
| 结构域 | InterPro + Pfam | 0个域 | 无注释 |
| PPI | STRING + IntAct | 15 + 13 | 数据充分 |

**互证加分明细**:
- UniProt核定位 + HPA IF核验证一致 (+1.0)
- IntAct实验互作丰富(15条) (+0.5)
- STRING实验分>0.7 (+0.5)
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐⭐ (76.0/100)

**核心优势**:
1. Extremely novel -- PubMed=2篇
2. HPA主定位核，附加Cytosol/Vesicles

**风险/不确定性**:
1. HPA IF图像可进一步分析
2. 结构数据可接受

**下一步建议**:
- [ ] 获取 HPA IF 图像确认核定位
- [ ] 查阅最新关键文献补充功能细节
- [ ] 设计体外 DNA/染色质结合实验

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96F63
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CCDC97
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96F63
- STRING: https://string-db.org/cgi/network?identifiers=CCDC97&species=9606
