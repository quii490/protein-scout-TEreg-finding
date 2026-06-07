---
type: protein-evaluation
gene: "CCDC8"
date: 2026-06-02
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CCDC8 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CCDC8 / CCDC8 |
| 蛋白全名 | Coiled-coil domain-containing protein 8 |
| 蛋白大小 | 538 aa / 59.4 kDa |
| UniProt ID | Q9H0W5 |
| 子定位分类 | nucleus-cytoplasm |
| HPA IF 主定位 | Plasma membrane, Cytosol |
| HPA IF 附加定位 | Nucleoplasm |
| HPA Reliability | Approved |
| 评估日期 | 2026-06-02 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16 | HPA核为附加定位，主定位非核 |
| 蛋白大小 | 10/10 | x1 | 10 | 538 aa (200-800 aa ideal range) |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed=46 (Very novel) |
| 三维结构 | 6/10 | x3 | 18 | 新颖蛋白基线，无可靠结构 |
| 调控结构域 | 7/10 | x2 | 14 | 新颖蛋白基线，无注释结构域 |
| PPI网络 | 6/10 | x3 | 18 | STRING实验分>0.5 (8条) |
| 互证加分 | — | max+3 | +2.0 | PDB实验结构(1条目) (+1.0); IntAct实验互作丰富(15条) (+0.5); STRING实验分>0.7 (+0.5) |
| **加权总分** | | | **118.0/180** | |
| **归一化总分 (÷1.83)** | | | **64.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | Nucleoplasm, Plasma membrane, Cytosol | Approved |
| UniProt | Cytoplasm (ECO:0000269); Cytoplasm, cytoskeleton, microtubule organizing center, centrosome (ECO:0000269) | Swiss-Prot/TrEMBL |
| GO-CC | 3M complex (IDA:UniProtKB); centrosome (IDA:UniProtKB); cytoplasm (IDA:UniProtKB); cytosol (IDA:HPA); nucleoplasm (IDA:HPA) | |

暂无PAE图

HPA IF 图像可用 (6张)，待下载。

**结论**: HPA核为附加定位，主定位非核

#### 3.2 蛋白大小评估

538 aa (200-800 aa ideal range)

**评价**: 538 aa / 59.4 kDa，适宜大小的蛋白，适合常规生化实验和结构生物学分析。

**评分: 10/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 46 |
| PubMed symbol_only | 65 |
| PubMed broad | 67 |
| 别名 | CCDC8 |
| 新颖性分级 | Very novel |

**评价**: PubMed 46 篇 (strict)，非常新颖。仅有少数基础研究，研究空间充足。

**评分: 8/10**。

**关键文献**:
1. **3-M Syndrome.** (1993) PMID:20301654 -- Adam MP et al.
2. **Analysis of the toxicity and mechanisms of osteoporosis caused by cigarette toxicants using network toxicology and molecular docking techniques.** *The Science of the total environment* (2025 Oct 20) PMID:40925315 -- Xie W et al.
3. **Overexpressed coiled-coil domain containing protein 8 (CCDC8) mediates newly synthesized HIV-1 Gag lysosomal degradation.** *Scientific reports* (2020 Jul 10) PMID:32651437 -- Jiang X et al.
4. **Impaired plasma membrane localization of ubiquitin ligase complex underlies 3-M syndrome development.** *The Journal of clinical investigation* (2019 Jul 25) PMID:31343991 -- Wang P et al.
5. **Interstitial cystitis-related gene CCDC8 accelerates tumorigenesis by participating in CUL7-mediated degradation of P53 in bladder cancer.** *Oncogene* (2026 Mar) PMID:41644704 -- Wang J et al.


#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 46.4 |
| pLDDT > 90 (Very High) | 0.0% |
| pLDDT 70-90 (High) | 6.5% |
| pLDDT 50-70 (Medium) | 19.1% |
| pLDDT < 50 (Low) | 74.3% |
| 有序区域 (pLDDT>70) 占比 | 6.5% |
| AlphaFold 版本 | v6 |
| 实验结构 (PDB) | 4LG6 (X-ray, 1.80 A, B=494-510) |

暂无PAE图

**评价**: AlphaFold 预测置信度偏低（pLDDT=46.4，有序区域 6%）。作为新颖蛋白，属正常现象。

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
| OBSL1 | 0.999 | 0.742 | — |
| CUL7 | 0.997 | 0.644 | — |
| ANKRA2 | 0.980 | 0.949 | — |
| TP53 | 0.808 | 0.684 | — |
| CUL9 | 0.803 | 0.301 | — |
| FBXW8 | 0.795 | 0.626 | — |
| KAT5 | 0.655 | 0.335 | — |
| MAPK14 | 0.653 | 0.644 | — |
| RBX1 | 0.641 | 0.180 | — |
| UBC | 0.595 | 0.354 | — |


**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 调控相关? |
|---------|------|------|----------|
| KLHL2 | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| RBBP7 | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| IL20RA | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| CSGALNACT2 | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| CASQ2 | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| GOPC | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| PB2 | 0007(anti tag coimmunoprecipitation) | pubmed:28169297|imex | — |
| PB1 | 0007(anti tag coimmunoprecipitation) | pubmed:28169297|imex | — |
| CALM1 | 0007(anti tag coimmunoprecipitation) | pubmed:33961781|imex | — |
| TDRKH | 0007(anti tag coimmunoprecipitation) | pubmed:33961781|imex | — |


**已知复合体成员** (GO Cellular Component):
- 3M complex (IDA:UniProtKB)
- centrosome (IDA:UniProtKB)
- cytoplasm (IDA:UniProtKB)
- cytosol (IDA:HPA)
- nucleoplasm (IDA:HPA)
- plasma membrane (IDA:LIFEdb)

**PPI 互证分析**:
- STRING partners (score>0.4): 15
- IntAct 物理互作: 10
- 调控相关比例: 0/15 (0%)

**评价**: STRING实验分>0.5 (8条)

**评分: 6/10**。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 定位 | UniProt + HPA | Non-nuclear + Nucleoplasm/Nucleoli | 待确认 |
| 结构域 | InterPro + Pfam | 0个域 | 无注释 |
| PPI | STRING + IntAct | 15 + 10 | 数据充分 |

**互证加分明细**:
- PDB实验结构(1条目) (+1.0)
- IntAct实验互作丰富(15条) (+0.5)
- STRING实验分>0.7 (+0.5)
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐ (64.5/100)

**核心优势**:
1. Very novel -- PubMed=46篇
2. HPA核为附加定位，主定位非核

**风险/不确定性**:
1. HPA IF图像可进一步分析
2. AlphaFold预测质量待提升

**下一步建议**:
- [ ] 获取 HPA IF 图像确认核定位
- [ ] 查阅最新关键文献补充功能细节
- [ ] 设计体外 DNA/染色质结合实验

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H0W5
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CCDC8
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H0W5
- STRING: https://string-db.org/cgi/network?identifiers=CCDC8&species=9606

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H0W5 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR026526; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000169515-CCDC8/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ANKRA2 | Intact, Biogrid | true |
| CALM1 | Biogrid, Opencell | true |
| NPM1 | Biogrid, Opencell | true |
| CALM2 | Opencell | false |
| CALM3 | Opencell | false |
| CAPZA2 | Biogrid | false |
| CCT2 | Biogrid | false |
| CDK1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
