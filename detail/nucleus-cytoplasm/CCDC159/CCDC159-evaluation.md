---
type: protein-evaluation
gene: "CCDC159"
date: 2026-06-02
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CCDC159 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CCDC159 / CCDC159 |
| 蛋白全名 | Coiled-coil domain-containing protein 159 |
| 蛋白大小 | 297 aa / 33.7 kDa |
| UniProt ID | P0C7I6 |
| 子定位分类 | nucleus-cytoplasm |
| HPA IF 主定位 | Nucleoplasm, Nuclear bodies |
| HPA IF 附加定位 | Cytosol |
| HPA Reliability | Approved |
| 评估日期 | 2026-06-02 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 6/10 | x4 | 24 | HPA主定位核，附加Cytosol/Vesicles |
| 蛋白大小 | 10/10 | x1 | 10 | 297 aa (200-800 aa ideal range) |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed=4 (Extremely novel) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold中等(pLDDT=76.7, >70%=62.6%) |
| 调控结构域 | 7/10 | x2 | 14 | 新颖蛋白基线，无注释结构域 |
| PPI网络 | 3/10 | x3 | 9 | 仅有低置信度STRING关联 (8条) |
| 互证加分 | — | max+3 | 0 | 无额外互证加分 |
| **加权总分** | | | **128.0/180** | |
| **归一化总分 (÷1.83)** | | | **69.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | Nucleoplasm, Nuclear bodies, Cytosol | Approved |
| UniProt | 无UniProt注释 | Swiss-Prot/TrEMBL |
| GO-CC | sperm head-tail coupling apparatus (ISS:UniProtKB) | |

暂无PAE图

暂无HPA IF图像数据。

**结论**: HPA主定位核，附加Cytosol/Vesicles

#### 3.2 蛋白大小评估

297 aa (200-800 aa ideal range)

**评价**: 297 aa / 33.7 kDa，适宜大小的蛋白，适合常规生化实验和结构生物学分析。

**评分: 10/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 4 |
| PubMed symbol_only | 4 |
| PubMed broad | 4 |
| 别名 | CCDC159 |
| 新颖性分级 | Extremely novel |

**评价**: 仅 PubMed 4 篇 (strict)，极度新颖。该蛋白几乎未被系统研究，是探索新型核蛋白功能的绝佳候选。

**评分: 10/10**。

**关键文献**:
1. **Coiled-coil domain containing 159 is required for spermatid head and tail assembly in mice†.** *Biology of reproduction* (2024 May 9) PMID:38236177 -- Ge T et al.
2. **Identification and analysis of pyroptosis-related key genes in heart failure.** *Journal of cardiothoracic surgery* (2025 Jul 14) PMID:40660343 -- Zhang J et al.
3. **A model-free and distribution-free multi-omics integration approach for detecting novel lung adenocarcinoma genes.** *Scientific reports* (2024 Aug 3) PMID:39097651 -- Zhao S et al.
4. **Vincristine induces sperm malformation and motility dysfunction in mice by downregulating Tssk4 and Ccdc159.** *Reproductive toxicology (Elmsford, N.Y.)* (2026 May) PMID:41831660 -- Zhou C et al.


#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 76.7 |
| pLDDT > 90 (Very High) | 51.5% |
| pLDDT 70-90 (High) | 11.1% |
| pLDDT 50-70 (Medium) | 11.8% |
| pLDDT < 50 (Low) | 25.6% |
| 有序区域 (pLDDT>70) 占比 | 62.6% |
| AlphaFold 版本 | v6 |
| 实验结构 (PDB) | 无 |

暂无PAE图

**评价**: AlphaFold 中等质量（pLDDT=76.7，有序区域 63%）。作为新颖蛋白，此水平可接受。

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
| PLPPR2 | 0.634 | 0.000 | — |
| CCDC146 | 0.517 | 0.000 | — |
| SWSAP1 | 0.483 | 0.000 | — |
| SINHCAF | 0.473 | 0.000 | — |
| CIAO3 | 0.469 | 0.000 | — |
| UROS | 0.468 | 0.000 | — |
| TMEM205 | 0.455 | 0.000 | — |
| RELT | 0.428 | 0.000 | — |


**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 调控相关? |
|---------|------|------|----------|
| — | — | — | — |


**已知复合体成员** (GO Cellular Component):
- sperm head-tail coupling apparatus (ISS:UniProtKB)

**PPI 互证分析**:
- STRING partners (score>0.4): 8
- IntAct 物理互作: 0
- 调控相关比例: 0/8 (0%)

**评价**: 仅有低置信度STRING关联 (8条)

**评分: 3/10**。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 定位 | UniProt + HPA | Non-nuclear + Nucleoplasm/Nucleoli | 待确认 |
| 结构域 | InterPro + Pfam | 0个域 | 无注释 |
| PPI | STRING + IntAct | 8 + 0 | 数据有限 |

**互证加分明细**:
- 无额外互证加分
**总分**: 0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐ (69.9/100)

**核心优势**:
1. Extremely novel -- PubMed=4篇
2. HPA主定位核，附加Cytosol/Vesicles

**风险/不确定性**:
1. HPA IF图像可进一步分析
2. 结构数据可接受

**下一步建议**:
- [ ] 获取 HPA IF 图像确认核定位
- [ ] 查阅最新关键文献补充功能细节
- [ ] 设计体外 DNA/染色质结合实验

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P0C7I6
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CCDC159
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P0C7I6
- STRING: https://string-db.org/cgi/network?identifiers=CCDC159&species=9606
