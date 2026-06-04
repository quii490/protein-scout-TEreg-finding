---
type: protein-evaluation
gene: "CCDC117"
date: 2026-06-02
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CCDC117 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CCDC117 / CCDC117 |
| 蛋白全名 | Coiled-coil domain-containing protein 117 |
| 蛋白大小 | 279 aa / 30.5 kDa |
| UniProt ID | Q8IWD4 |
| 子定位分类 | nucleus-cytoplasm |
| HPA IF 主定位 | Nucleoplasm |
| HPA IF 附加定位 | Microtubules, Cytosol |
| HPA Reliability | Approved |
| 评估日期 | 2026-06-02 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 6/10 | x4 | 24 | HPA主定位核，附加Cytosol/Vesicles |
| 蛋白大小 | 10/10 | x1 | 10 | 279 aa (200-800 aa ideal range) |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed=6 (Extremely novel) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold低置信(pLDDT=59.9)，新颖蛋白基线 |
| 调控结构域 | 7/10 | x2 | 14 | 新颖蛋白基线，无注释结构域 |
| PPI网络 | 6/10 | x3 | 18 | STRING实验分>0.5 (2条) |
| 互证加分 | — | max+3 | +2.0 | UniProt核定位 + HPA IF核验证一致 (+1.0); IntAct实验互作丰富(15条) (+0.5); STRING实验分>0.7 (+0.5) |
| **加权总分** | | | **136.0/180** | |
| **归一化总分 (÷1.83)** | | | **74.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | Nucleoplasm, Microtubules, Cytosol | Approved |
| UniProt | Cytoplasm, cytoskeleton, spindle (ECO:0000269); Nucleus (ECO:0000269) | Swiss-Prot/TrEMBL |
| GO-CC | mitotic spindle (IDA:UniProtKB); nucleus (IEA:UniProtKB-SubCell) | |

暂无PAE图

暂无HPA IF图像数据。

**结论**: HPA主定位核，附加Cytosol/Vesicles

#### 3.2 蛋白大小评估

279 aa (200-800 aa ideal range)

**评价**: 279 aa / 30.5 kDa，适宜大小的蛋白，适合常规生化实验和结构生物学分析。

**评分: 10/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 6 |
| PubMed symbol_only | 9 |
| PubMed broad | 9 |
| 别名 | CCDC117 |
| 新颖性分级 | Extremely novel |

**评价**: 仅 PubMed 6 篇 (strict)，极度新颖。该蛋白几乎未被系统研究，是探索新型核蛋白功能的绝佳候选。

**评分: 10/10**。

**关键文献**:
1. **Acute transcriptomic changes in murine RAW 264.7 cells following pseudorabies virus infection.** *Archives of virology* (2022 Dec) PMID:36269412 -- Tong C et al.
2. **Circulating MicroRNAs as potential biomarkers for alcoholic steatohepatitis.** *Liver international : official journal of the International Association for the Study of the Liver* (2013 Sep) PMID:23682678 -- Chen YP et al.
3. **Placental Nkx2-5 and target gene expression in early-onset and severe preeclampsia.** *Hypertension in pregnancy* (2014 Nov) PMID:24987805 -- Rivers ER et al.
4. **Nkx2-5 Second Heart Field Target Gene Ccdc117 Regulates DNA Metabolism and Proliferation.** *Scientific reports* (2019 Feb 11) PMID:30742009 -- Horton AJ et al.
5. **Ccdc117 deficiency triggers hyperandrogenemia, maintaining normal sperm production despite reduced testis size.** *Reproduction (Cambridge, England)* (2026 Apr 5) PMID:41866304 -- Zang M et al.


#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 59.9 |
| pLDDT > 90 (Very High) | 6.1% |
| pLDDT 70-90 (High) | 20.1% |
| pLDDT 50-70 (Medium) | 40.5% |
| pLDDT < 50 (Low) | 33.3% |
| 有序区域 (pLDDT>70) 占比 | 26.2% |
| AlphaFold 版本 | v6 |
| 实验结构 (PDB) | 无 |

暂无PAE图

**评价**: AlphaFold 预测置信度偏低（pLDDT=59.9，有序区域 26%）。作为新颖蛋白，属正常现象。

**评分: 6/10**。

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
| STIP1 | 0.839 | 0.834 | — |
| HSP90AA1 | 0.607 | 0.602 | — |
| VEPH1 | 0.606 | 0.000 | — |
| MEGF11 | 0.596 | 0.000 | — |
| MSANTD4 | 0.536 | 0.000 | — |
| PTAFR | 0.492 | 0.000 | — |
| HSPA4 | 0.488 | 0.454 | — |
| SLC35B2 | 0.481 | 0.477 | — |
| TCEANC2 | 0.462 | 0.000 | — |
| AP4E1 | 0.448 | 0.000 | — |


**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 调控相关? |
|---------|------|------|----------|
| HSPA8 | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| STIP1 | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| HSP90AA4P | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| BAG1 | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| HSPBP1 | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| RAB6B | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| HSP90AB1 | 0007(anti tag coimmunoprecipitation) | pubmed:25036637|imex | — |
| HSPA4 | 0007(anti tag coimmunoprecipitation) | pubmed:33961781|imex | — |
| HSPA2 | 0007(anti tag coimmunoprecipitation) | pubmed:33961781|imex | — |
| hspa1a_hspa1b_human-1 | 0007(anti tag coimmunoprecipitation) | pubmed:33961781|imex | — |


**已知复合体成员** (GO Cellular Component):
- mitotic spindle (IDA:UniProtKB)
- nucleus (IEA:UniProtKB-SubCell)

**PPI 互证分析**:
- STRING partners (score>0.4): 15
- IntAct 物理互作: 11
- 调控相关比例: 0/15 (0%)

**评价**: STRING实验分>0.5 (2条)

**评分: 6/10**。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 定位 | UniProt + HPA | Nucleus + Nucleoplasm/Nucleoli | 一致 |
| 结构域 | InterPro + Pfam | 0个域 | 无注释 |
| PPI | STRING + IntAct | 15 + 11 | 数据充分 |

**互证加分明细**:
- UniProt核定位 + HPA IF核验证一致 (+1.0)
- IntAct实验互作丰富(15条) (+0.5)
- STRING实验分>0.7 (+0.5)
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐⭐ (74.3/100)

**核心优势**:
1. Extremely novel -- PubMed=6篇
2. HPA主定位核，附加Cytosol/Vesicles

**风险/不确定性**:
1. HPA IF图像可进一步分析
2. AlphaFold预测质量待提升

**下一步建议**:
- [ ] 获取 HPA IF 图像确认核定位
- [ ] 查阅最新关键文献补充功能细节
- [ ] 设计体外 DNA/染色质结合实验

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IWD4
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CCDC117
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IWD4
- STRING: https://string-db.org/cgi/network?identifiers=CCDC117&species=9606
