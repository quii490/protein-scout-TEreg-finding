---
type: protein-evaluation
gene: "CBR3"
date: 2026-06-02
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CBR3 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CBR3 / SDR21C2 |
| 蛋白全名 | Carbonyl reductase [NADPH] 3 |
| 蛋白大小 | 277 aa / 30.9 kDa |
| UniProt ID | O75828 |
| 子定位分类 | nucleus-cytoplasm |
| HPA IF 主定位 | Nucleoplasm, Cytosol |
| HPA IF 附加定位 | 无 |
| HPA Reliability | Supported |
| 评估日期 | 2026-06-02 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | x4 | 28 | HPA主定位核 |
| 蛋白大小 | 10/10 | x1 | 10 | 277 aa (200-800 aa ideal range) |
| 研究新颖性 | 6/10 | x5 | 30 | PubMed=76 (Moderately novel) |
| 三维结构 | 8/10 | x3 | 24 | PDB实验结构(1条目) + AlphaFold(pLDDT=96.6) |
| 调控结构域 | 7/10 | x2 | 14 | PubMed≤100基线，无注释结构域 |
| PPI网络 | 6/10 | x3 | 18 | STRING实验分>0.5 (1条) |
| 互证加分 | — | max+3 | +2.5 | PDB实验结构(1条目) (+1.0); IntAct实验互作丰富(15条) (+0.5); STRING实验分>0.7 (+0.5); InterPro注释丰 |
| **加权总分** | | | **126.5/180** | |
| **归一化总分 (÷1.83)** | | | **69.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | Nucleoplasm, Cytosol | Supported |
| UniProt | Cytoplasm (ECO:0000269) | Swiss-Prot/TrEMBL |
| GO-CC | cytosol (IDA:UniProtKB); extracellular space (HDA:UniProtKB); nucleoplasm (IDA:HPA) | |

暂无PAE图

暂无HPA IF图像数据。

**结论**: HPA主定位核

#### 3.2 蛋白大小评估

277 aa (200-800 aa ideal range)

**评价**: 277 aa / 30.9 kDa，适宜大小的蛋白，适合常规生化实验和结构生物学分析。

**评分: 10/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 76 |
| PubMed symbol_only | 179 |
| PubMed broad | 186 |
| 别名 | SDR21C2 |
| 新颖性分级 | Moderately novel |

**评价**: PubMed 76 篇 (strict)，中等新颖度。已有一部分研究基础，但仍有较大探索空间。

**评分: 6/10**。

**关键文献**:
1. **Human carbonyl reductases.** *Current drug metabolism* (2010 Oct) PMID:20942781 -- Malátková P et al.
2. **Functional Validation of Doxorubicin-Induced Cardiotoxicity-Related Genes.** *JACC. CardioOncology* (2024 Feb) PMID:38510289 -- Fonoudi H et al.
3. **Apobec1 complementation factor overexpression promotes hepatic steatosis, fibrosis, and hepatocellular cancer.** *The Journal of clinical investigation* (2021 Jan 4) PMID:33445170 -- Blanc V et al.
4. **Long noncoding RNA CBR3-AS1 mediates tumorigenesis and radiosensitivity of non-small cell lung cancer through redox and DNA repair by CBR3-AS1 /miR-409-3p/SOD1 axis.** *Cancer letters* (2022 Feb 1) PMID:34801596 -- Liu S et al.
5. **CBR3-AS1 Accelerates the Malignant Proliferation of Gestational Choriocarcinoma Cells by Stabilizing SETD4.** *Disease markers* (2022) PMID:35655916 -- Zhang Y et al.


#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 96.6 |
| pLDDT > 90 (Very High) | 94.2% |
| pLDDT 70-90 (High) | 4.3% |
| pLDDT 50-70 (Medium) | 0.7% |
| pLDDT < 50 (Low) | 0.7% |
| 有序区域 (pLDDT>70) 占比 | 98.5% |
| AlphaFold 版本 | v6 |
| 实验结构 (PDB) | 2HRB (X-ray, 1.90 A, A=6-277) |

暂无PAE图

**评价**: 实验结构（PDB: 2HRB (X-ray, 1.90 A, A=6-277)）提供可靠信息；AlphaFold pLDDT=96.6，有序区域 98%。

**评分: 8/10**。

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
| CBR1 | 0.983 | 0.727 | — |
| CYP3A4 | 0.952 | 0.000 | — |
| CYP2D6 | 0.932 | 0.000 | — |
| CYP1A1 | 0.929 | 0.000 | — |
| CYP2E1 | 0.926 | 0.000 | — |
| AKR1A1 | 0.923 | 0.045 | — |
| PTGES3 | 0.919 | 0.057 | — |
| CYP2A13 | 0.917 | 0.000 | — |
| CYP2A6 | 0.917 | 0.000 | — |
| PTGES2 | 0.906 | 0.000 | — |


**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 调控相关? |
|---------|------|------|----------|
| ARIH2 | 0398(two hybrid pooling approach) | pubmed:16169070|imex | — |
| RAB35 | 0398(two hybrid pooling approach) | pubmed:16169070|imex | — |
| SGK1 | 0006(anti bait coimmunoprecipitation) | pubmed:17353931 | — |
| GABARAP | 0007(anti tag coimmunoprecipitation) | pubmed:20562859|imex | — |
| GABARAPL1 | 0007(anti tag coimmunoprecipitation) | pubmed:20562859|imex | — |
| USP3 | 0007(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed | — |
| NDUFS3 | 0007(anti tag coimmunoprecipitation) | pubmed:27499296|imex | — |
| SDCBP | 0397(two hybrid array) | imex:IM-27438|doi:10 | — |
| CBR1 | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| BTBD9 | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |


**已知复合体成员** (GO Cellular Component):
- cytosol (IDA:UniProtKB)
- extracellular space (HDA:UniProtKB)
- nucleoplasm (IDA:HPA)

**PPI 互证分析**:
- STRING partners (score>0.4): 15
- IntAct 物理互作: 14
- 调控相关比例: 0/15 (0%)

**评价**: STRING实验分>0.5 (1条)

**评分: 6/10**。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 定位 | UniProt + HPA | Non-nuclear + Nucleoplasm/Nucleoli | 待确认 |
| 结构域 | InterPro + Pfam | 0个域 | 无注释 |
| PPI | STRING + IntAct | 15 + 14 | 数据充分 |

**互证加分明细**:
- PDB实验结构(1条目) (+1.0)
- IntAct实验互作丰富(15条) (+0.5)
- STRING实验分>0.7 (+0.5)
- InterPro注释丰富(4个结构域) (+0.5)
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐ (69.1/100)

**核心优势**:
1. Moderately novel -- PubMed=76篇
2. HPA主定位核

**风险/不确定性**:
1. HPA IF图像可进一步分析
2. 结构数据可接受

**下一步建议**:
- [ ] 获取 HPA IF 图像确认核定位
- [ ] 查阅最新关键文献补充功能细节
- [ ] 设计体外 DNA/染色质结合实验

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75828
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CBR3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75828
- STRING: https://string-db.org/cgi/network?identifiers=CBR3&species=9606
