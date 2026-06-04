---
type: protein-evaluation
gene: "CAPS2"
date: 2026-06-02
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CAPS2 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CAPS2 / CAPS2 | KIAA1591 |
| 蛋白全名 | Calcium-dependent secretion activator 2 |
| 蛋白大小 | 1296 aa / 147.7 kDa |
| UniProt ID | Q86UW7 |
| 子定位分类 | nucleolus |
| HPA IF 主定位 | Nucleoli |
| HPA IF 附加定位 | Nucleoplasm, Vesicles, Centrosome |
| HPA Reliability | Approved |
| 评估日期 | 2026-06-02 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | x4 | 28 | HPA主定位核 |
| 蛋白大小 | 5/10 | x1 | 5 | 1296 aa (small or large) |
| 研究新颖性 | 6/10 | x5 | 30 | PubMed=60 (Moderately novel) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold中等(pLDDT=79.0, >70%=79.3%) |
| 调控结构域 | 7/10 | x2 | 14 | PubMed≤100基线，无注释结构域 |
| PPI网络 | 3/10 | x3 | 9 | 仅有低置信度STRING关联 (2条) |
| 互证加分 | — | max+3 | +1.0 | IntAct实验互作丰富(11条) (+0.5); InterPro注释丰富(8个结构域) (+0.5) |
| **加权总分** | | | **108.0/180** | |
| **归一化总分 (÷1.83)** | | | **59.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | Nucleoplasm, Nucleoli, Vesicles, Centrosome | Approved |
| UniProt | Cytoplasmic vesicle membrane (ECO:0000305); Synapse; Cell projection, cilium (ECO:0000269); Cytoplasm, cytoskeleton, cil | Swiss-Prot/TrEMBL |
| GO-CC | centrosome (IDA:UniProtKB); ciliary basal body (IDA:UniProtKB); cilium (IDA:UniProtKB); cytoplasmic vesicle membrane (IEA:UniProtKB-SubCell); glutamatergic synapse (IBA:GO_Central) | |

暂无PAE图

HPA IF 图像可用 (12张)，待下载。

**结论**: HPA主定位核

#### 3.2 蛋白大小评估

1296 aa (small or large)

**评价**: 1296 aa / 147.7 kDa，大蛋白，实验操作有一定挑战。

**评分: 5/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 60 |
| PubMed symbol_only | 99 |
| PubMed broad | 106 |
| 别名 | CAPS2 | KIAA1591 |
| 新颖性分级 | Moderately novel |

**评价**: PubMed 60 篇 (strict)，中等新颖度。已有一部分研究基础，但仍有较大探索空间。

**评分: 6/10**。

**关键文献**:
1. **LINE-1 retrotransposons contribute to mouse PV interneuron development.** *Nature neuroscience* (2024 Jul) PMID:38773348 -- Bodea GO et al.
2. **GABA(B) receptors induce phasic release from medial habenula terminals through activity-dependent recruitment of release-ready vesicles.** *Proceedings of the National Academy of Sciences of the United States of America* (2024 Feb 20) PMID:38346189 -- Koppensteiner P et al.
3. **The secretory granule-associated protein CAPS2 regulates neurotrophin release and cell survival.** *The Journal of neuroscience : the official journal of the Society for Neuroscience* (2004 Jan 7) PMID:14715936 -- Sadakata T et al.
4. **Developmentally regulated Ca2+-dependent activator protein for secretion 2 (CAPS2) is involved in BDNF secretion and is associated with autism susceptibility.** *Cerebellum (London, England)* (2009 Sep) PMID:19238500 -- Sadakata T et al.
5. **Mouse models of mutations and variations in autism spectrum disorder-associated genes: mice expressing Caps2/Cadps2 copy number and alternative splicing variants.** *International journal of environmental research and public health* (2013 Nov 27) PMID:24287856 -- Sadakata T et al.


#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 79.0 |
| pLDDT > 90 (Very High) | 41.4% |
| pLDDT 70-90 (High) | 37.9% |
| pLDDT 50-70 (Medium) | 5.5% |
| pLDDT < 50 (Low) | 15.2% |
| 有序区域 (pLDDT>70) 占比 | 79.3% |
| AlphaFold 版本 | v6 |
| 实验结构 (PDB) | 无 |

暂无PAE图

**评价**: AlphaFold 中等质量（pLDDT=79.0，有序区域 79%）。作为新颖蛋白，此水平可接受。

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
| KISS1R | 0.429 | 0.000 | — |
| EFCAB6 | 0.403 | 0.129 | — |


**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 调控相关? |
|---------|------|------|----------|
| MEGF10 | 0018(two hybrid) | pubmed:unassigned5 | — |
| CADPS2 | 0096(pull down) | imex:IM-15829|pubmed | — |
| UBE2D2 | 0397(two hybrid array) | imex:IM-9597|pubmed: | — |
| UBE2D3 | 0397(two hybrid array) | imex:IM-9597|pubmed: | — |
| UBE2D4 | 0397(two hybrid array) | imex:IM-9597|pubmed: | — |
| UBE2U | 0397(two hybrid array) | imex:IM-9597|pubmed: | — |
| UBE2W | 0397(two hybrid array) | imex:IM-9597|pubmed: | — |
| SAXO5 | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| TTC3 | 0399(two hybrid fragment pooling approac | pubmed:35914814|imex | — |
| WDR4 | 0399(two hybrid fragment pooling approac | pubmed:35914814|imex | — |


**已知复合体成员** (GO Cellular Component):
- centrosome (IDA:UniProtKB)
- ciliary basal body (IDA:UniProtKB)
- cilium (IDA:UniProtKB)
- cytoplasmic vesicle membrane (IEA:UniProtKB-SubCell)
- glutamatergic synapse (IBA:GO_Central)
- nucleoplasm (IDA:HPA)
- parallel fiber to Purkinje cell synapse (IEA:Ensembl)
- postsynaptic membrane (IEA:Ensembl)
- presynaptic membrane (IEA:Ensembl)

**PPI 互证分析**:
- STRING partners (score>0.4): 2
- IntAct 物理互作: 11
- 调控相关比例: 0/2 (0%)

**评价**: 仅有低置信度STRING关联 (2条)

**评分: 3/10**。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 定位 | UniProt + HPA | Non-nuclear + Nucleoplasm/Nucleoli | 待确认 |
| 结构域 | InterPro + Pfam | 0个域 | 无注释 |
| PPI | STRING + IntAct | 2 + 11 | 数据充分 |

**互证加分明细**:
- IntAct实验互作丰富(11条) (+0.5)
- InterPro注释丰富(8个结构域) (+0.5)
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐ (59.0/100)

**核心优势**:
1. Moderately novel -- PubMed=60篇
2. HPA主定位核

**风险/不确定性**:
1. HPA IF图像可进一步分析
2. 结构数据可接受

**下一步建议**:
- [ ] 获取 HPA IF 图像确认核定位
- [ ] 查阅最新关键文献补充功能细节
- [ ] 设计体外 DNA/染色质结合实验

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86UW7
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CAPS2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86UW7
- STRING: https://string-db.org/cgi/network?identifiers=CAPS2&species=9606
