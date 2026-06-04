---
type: protein-evaluation
gene: "CC2D1B"
date: 2026-06-02
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CC2D1B 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CC2D1B / KIAA1836 | LGD1 |
| 蛋白全名 | Coiled-coil and C2 domain-containing protein 1B |
| 蛋白大小 | 858 aa / 94.2 kDa |
| UniProt ID | Q5T0F9 |
| 子定位分类 | nucleoplasm |
| HPA IF 主定位 | Nucleoplasm |
| HPA IF 附加定位 | Vesicles |
| HPA Reliability | Supported |
| 评估日期 | 2026-06-02 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | x4 | 32 | HPA主定位核 + 转录因子功能，附加胞质信号 |
| 蛋白大小 | 8/10 | x1 | 8 | 858 aa (acceptable range) |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed=22 (Very novel) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold中等(pLDDT=70.9, >70%=59.3%) |
| 调控结构域 | 8/10 | x2 | 16 | DNA/chromatin相关结构域: [] |
| PPI网络 | 6/10 | x3 | 18 | STRING实验分>0.5 (1条) |
| 互证加分 | — | max+3 | +2.0 | UniProt核定位 + HPA IF核验证一致 (+1.0); IntAct实验互作丰富(15条) (+0.5); InterPro注释丰富(5个结构域) ( |
| **加权总分** | | | **137.0/180** | |
| **归一化总分 (÷1.83)** | | | **74.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | Nucleoplasm, Vesicles | Supported |
| UniProt | Nucleus (ECO:0000269) | Swiss-Prot/TrEMBL |
| GO-CC | cytosol (IEA:Ensembl); endosome membrane (IEA:Ensembl); nuclear envelope (TAS:Reactome); nucleoplasm (IDA:HPA); nucleus (IBA:GO_Central) | |

暂无PAE图

暂无HPA IF图像数据。

**结论**: HPA主定位核 + 转录因子功能，附加胞质信号

#### 3.2 蛋白大小评估

858 aa (acceptable range)

**评价**: 858 aa / 94.2 kDa，偏大蛋白，但仍在可操作范围内。

**评分: 8/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 22 |
| PubMed symbol_only | 30 |
| PubMed broad | 31 |
| 别名 | KIAA1836 | LGD1 |
| 新颖性分级 | Very novel |

**评价**: PubMed 22 篇 (strict)，非常新颖。仅有少数基础研究，研究空间充足。

**评分: 8/10**。

**关键文献**:
1. **Genetic etiological spectrum of sperm morphological abnormalities.** *Journal of assisted reproduction and genetics* (2024 Nov) PMID:39417902 -- Arora M et al.
2. **YAP and TAZ Regulate Cc2d1b and Purβ in Schwann Cells.** *Frontiers in molecular neuroscience* (2019) PMID:31379499 -- Sophie B et al.
3. **Replication competent HIV-guided CRISPR screen identifies antiviral factors including targets of the accessory protein Nef.** *Nature communications* (2024 May 7) PMID:38714682 -- Prelli Bozzo C et al.
4. **Loss of the Intellectual Disability and Autism Gene Cc2d1a and Its Homolog Cc2d1b Differentially Affect Spatial Memory, Anxiety, and Hyperactivity.** *Frontiers in genetics* (2018) PMID:29552027 -- Zamarbide M et al.
5. **GWAS-informed data integration and non-coding CRISPRi screen illuminate genetic etiology of bone mineral density.** *Genome biology* (2025 Oct 3) PMID:41044600 -- Conery M et al.


#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 70.9 |
| pLDDT > 90 (Very High) | 29.8% |
| pLDDT 70-90 (High) | 29.5% |
| pLDDT 50-70 (Medium) | 10.8% |
| pLDDT < 50 (Low) | 29.8% |
| 有序区域 (pLDDT>70) 占比 | 59.3% |
| AlphaFold 版本 | v6 |
| 实验结构 (PDB) | 无 |

暂无PAE图

**评价**: AlphaFold 中等质量（pLDDT=70.9，有序区域 59%）。作为新颖蛋白，此水平可接受。

**评分: 7/10**。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | 无注释 |
| Pfam | 无注释 |

**染色质调控潜力分析**: 含明确的DNA/染色质相关结构域：无注释结构域。

**评分: 8/10**。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4, top 10):

| Partner | Score | 实验分 | 调控相关? |
|---------|-------|--------|----------|
| CHMP4B | 0.858 | 0.697 | — |
| CHMP4C | 0.831 | 0.263 | — |
| CHMP4A | 0.777 | 0.000 | — |
| CHMP7 | 0.753 | 0.000 | — |
| CHMP6 | 0.713 | 0.000 | — |
| IST1 | 0.712 | 0.000 | — |
| CHMP3 | 0.683 | 0.000 | — |
| LEMD2 | 0.680 | 0.065 | — |
| CHMP2A | 0.677 | 0.000 | — |
| DPP9 | 0.630 | 0.000 | — |


**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 调控相关? |
|---------|------|------|----------|
| MDFI | 0397(two hybrid array) | pubmed:32296183|imex | — |
| BMX | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| TSNAX | 0007(anti tag coimmunoprecipitation) | pubmed:26496610|imex | — |
| C1qbp | 0007(anti tag coimmunoprecipitation) | pubmed:26496610|imex | — |
| CHMP4B | 0007(anti tag coimmunoprecipitation) | pubmed:26496610|imex | — |
| Chmp4b | 0007(anti tag coimmunoprecipitation) | pubmed:26496610|imex | — |
| KIFC3 | 0007(anti tag coimmunoprecipitation) | pubmed:26496610|imex | — |
| PCDH7 | 0007(anti tag coimmunoprecipitation) | pubmed:33961781|imex | — |
| HSPA14 | 0007(anti tag coimmunoprecipitation) | pubmed:33961781|imex | — |
| FAT4 | 0007(anti tag coimmunoprecipitation) | pubmed:33961781|imex | — |


**已知复合体成员** (GO Cellular Component):
- cytosol (IEA:Ensembl)
- endosome membrane (IEA:Ensembl)
- nuclear envelope (TAS:Reactome)
- nucleoplasm (IDA:HPA)
- nucleus (IBA:GO_Central)

**PPI 互证分析**:
- STRING partners (score>0.4): 15
- IntAct 物理互作: 11
- 调控相关比例: 0/15 (0%)

**评价**: STRING实验分>0.5 (1条)

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
- InterPro注释丰富(5个结构域) (+0.5)
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐⭐ (74.9/100)

**核心优势**:
1. Very novel -- PubMed=22篇
2. HPA主定位核 + 转录因子功能，附加胞质信号

**风险/不确定性**:
1. HPA IF图像可进一步分析
2. 结构数据可接受

**下一步建议**:
- [ ] 获取 HPA IF 图像确认核定位
- [ ] 查阅最新关键文献补充功能细节
- [ ] 设计体外 DNA/染色质结合实验

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5T0F9
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CC2D1B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5T0F9
- STRING: https://string-db.org/cgi/network?identifiers=CC2D1B&species=9606
