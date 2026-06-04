---
type: protein-evaluation
gene: "CCDC141"
date: 2026-06-02
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CCDC141 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CCDC141 / CAMDI |
| 蛋白全名 | Coiled-coil domain-containing protein 141 |
| 蛋白大小 | 1530 aa / 175.1 kDa |
| UniProt ID | Q6ZP82 |
| 子定位分类 | nucleus-cytoplasm |
| HPA IF 主定位 | Nucleoplasm |
| HPA IF 附加定位 | 无 |
| HPA Reliability | Approved |
| 评估日期 | 2026-06-02 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | x4 | 28 | HPA主定位核 |
| 蛋白大小 | 5/10 | x1 | 5 | 1530 aa (small or large) |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed=24 (Very novel) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold中等(pLDDT=71.8, >70%=69.9%) |
| 调控结构域 | 8/10 | x2 | 16 | DNA/chromatin相关结构域: [] |
| PPI网络 | 6/10 | x3 | 18 | 有物理互作(14条)，调控邻居占比低 |
| 互证加分 | — | max+3 | +1.0 | IntAct实验互作丰富(15条) (+0.5); InterPro注释丰富(8个结构域) (+0.5) |
| **加权总分** | | | **129.0/180** | |
| **归一化总分 (÷1.83)** | | | **70.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | Nucleoplasm | Approved |
| UniProt | Cytoplasm (ECO:0000250); Cytoplasm, cytoskeleton, microtubule organizing center, centrosome (ECO:0000250) | Swiss-Prot/TrEMBL |
| GO-CC | centrosome (IEA:UniProtKB-SubCell); cytoplasm (IEA:UniProtKB-SubCell) | |

暂无PAE图

暂无HPA IF图像数据。

**结论**: HPA主定位核

#### 3.2 蛋白大小评估

1530 aa (small or large)

**评价**: 1530 aa / 175.1 kDa，大蛋白，实验操作有一定挑战。

**评分: 5/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 24 |
| PubMed symbol_only | 34 |
| PubMed broad | 39 |
| 别名 | CAMDI |
| 新颖性分级 | Very novel |

**评价**: PubMed 24 篇 (strict)，非常新颖。仅有少数基础研究，研究空间充足。

**评分: 8/10**。

**关键文献**:
1. **Epistasis regulates genetic control of cardiac hypertrophy.** *Nature cardiovascular research* (2025 Jun) PMID:40473955 -- Wang Q et al.
2. **Meta-Analysis of Genome-Wide Association Studies Reveals Genetic Mechanisms of Supraventricular Arrhythmias.** *Circulation. Genomic and precision medicine* (2024 Jun) PMID:38804128 -- Weng LC et al.
3. **CCDC141 is a Connectin/Titin and Nesprin-1 binding protein that adapts cardiomyocytes to mechanical stress.** *Communications biology* (2025 Nov 26) PMID:41298937 -- Hanashima A et al.
4. **Isolated Gonadotropin-Releasing Hormone (GnRH) Deficiency.** (1993) PMID:20301509 -- Adam MP et al.
5. **Genome-wide analysis identified novel susceptible genes of restless legs syndrome in migraineurs.** *The journal of headache and pain* (2022 Mar 29) PMID:35350973 -- Jiang YJ et al.


#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 71.8 |
| pLDDT > 90 (Very High) | 16.4% |
| pLDDT 70-90 (High) | 53.5% |
| pLDDT 50-70 (Medium) | 9.7% |
| pLDDT < 50 (Low) | 20.4% |
| 有序区域 (pLDDT>70) 占比 | 69.9% |
| AlphaFold 版本 | v6 |
| 实验结构 (PDB) | 无 |

暂无PAE图

**评价**: AlphaFold 中等质量（pLDDT=71.8，有序区域 70%）。作为新颖蛋白，此水平可接受。

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
| DISC1 | 0.897 | 0.505 | — |
| TTN | 0.795 | 0.000 | — |
| SLC35F1 | 0.579 | 0.046 | — |
| PROKR2 | 0.514 | 0.000 | — |
| KLHL38 | 0.504 | 0.091 | — |
| SYT10 | 0.476 | 0.069 | — |
| CCSER2 | 0.460 | 0.000 | — |
| KIAA1755 | 0.450 | 0.000 | — |
| IGSF10 | 0.450 | 0.045 | — |
| FEZF1 | 0.447 | 0.071 | — |


**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 调控相关? |
|---------|------|------|----------|
| DISC1 | 0018(two hybrid) | pubmed:12812986|imex | — |
| RRAD | 0399(two hybrid fragment pooling approac | pubmed:23414517|imex | — |
| Disc1 | 0006(anti bait coimmunoprecipitation) | pubmed:20956536|imex | — |
| Myl9 | 0006(anti bait coimmunoprecipitation) | pubmed:20956536|imex | — |
| HOMER3 | 0397(two hybrid array) | pubmed:32296183|imex | — |
| C7 | 0007(anti tag coimmunoprecipitation) | pubmed:33961781|imex | — |
| EFHD1 | 0007(anti tag coimmunoprecipitation) | pubmed:33961781|imex | — |
| Hdac6 | 0018(two hybrid) | pubmed:27737934|imex | — |
| Cav3 | 0006(anti bait coimmunoprecipitation) | pubmed:24952909|imex | — |
| WFS1 | 0397(two hybrid array) | pubmed:32814053|imex | — |


**已知复合体成员** (GO Cellular Component):
- centrosome (IEA:UniProtKB-SubCell)
- cytoplasm (IEA:UniProtKB-SubCell)

**PPI 互证分析**:
- STRING partners (score>0.4): 13
- IntAct 物理互作: 13
- 调控相关比例: 0/13 (0%)

**评价**: 有物理互作(14条)，调控邻居占比低

**评分: 6/10**。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 定位 | UniProt + HPA | Non-nuclear + Nucleoplasm/Nucleoli | 待确认 |
| 结构域 | InterPro + Pfam | 0个域 | 无注释 |
| PPI | STRING + IntAct | 13 + 13 | 数据充分 |

**互证加分明细**:
- IntAct实验互作丰富(15条) (+0.5)
- InterPro注释丰富(8个结构域) (+0.5)
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐⭐ (70.5/100)

**核心优势**:
1. Very novel -- PubMed=24篇
2. HPA主定位核

**风险/不确定性**:
1. HPA IF图像可进一步分析
2. 结构数据可接受

**下一步建议**:
- [ ] 获取 HPA IF 图像确认核定位
- [ ] 查阅最新关键文献补充功能细节
- [ ] 设计体外 DNA/染色质结合实验

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6ZP82
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CCDC141
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6ZP82
- STRING: https://string-db.org/cgi/network?identifiers=CCDC141&species=9606
