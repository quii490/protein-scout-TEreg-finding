---
type: protein-evaluation
gene: "DACT1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DACT1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DACT1 / DPR1, HNG3 |
| 蛋白名称 | Dapper homolog 1 |
| 蛋白大小 | 836 aa / 90.2 kDa |
| UniProt ID | Q9NYF0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Cytoplasm; Nucleus; Synapse |
| 蛋白大小 | 8/10 | ×1 | 8 | 836 aa / 90.2 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=69 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=50.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR024843; Pfam: PF15268 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **98.0/180** | |
| **归一化总分** | | | **54.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Cytoplasm; Nucleus; Synapse | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- synapse (GO:0045202)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 69 |
| PubMed broad count | 140 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DPR1, HNG3 |

**关键文献**:
1. TGF-β-induced DACT1 biomolecular condensates repress Wnt signalling to promote bone metastasis.. *Nature cell biology*. PMID: 33723425
2. Dact1 is a postsynaptic protein required for dendrite, spine, and excitatory synapse development in the mouse forebrain.. *The Journal of neuroscience : the official journal of the Society for Neuroscience*. PMID: 20335472
3. Identification and characterization of rat Dact1 and Dact2 genes in silico.. *International journal of molecular medicine*. PMID: 15870912
4. Dact1 is expressed during chicken and mouse skeletal myogenesis and modulated in human muscle diseases.. *Comparative biochemistry and physiology. Part B, Biochemistry & molecular biology*. PMID: 34252542
5. Effects of DACT1 methylation status on invasion and metastasis of nasopharyngeal carcinoma.. *Biological research*. PMID: 31182157

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 50.3 |
| 高置信度残基 (pLDDT>90) 占比 | 2.4% |
| 置信残基 (pLDDT 70-90) 占比 | 12.2% |
| 中等置信 (pLDDT 50-70) 占比 | 21.4% |
| 低置信 (pLDDT<50) 占比 | 64.0% |
| 有序区域 (pLDDT>70) 占比 | 14.6% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=50.3），有序残基占 14.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR024843; Pfam: PF15268 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DVL2 | 0.992 | 0.647 | — |
| DVL1 | 0.966 | 0.307 | — |
| VANGL2 | 0.890 | 0.201 | — |
| DVL3 | 0.758 | 0.131 | — |
| CTNNB1 | 0.753 | 0.300 | — |
| SESTD1 | 0.749 | 0.586 | — |
| VANGL1 | 0.744 | 0.144 | — |
| CTNND1 | 0.703 | 0.121 | — |
| PTK7 | 0.697 | 0.000 | — |
| DBF4 | 0.694 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |
| APPL1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| PPP1CC | psi-mi:"MI:0018"(two hybrid) | pubmed:21382349|imex:IM-17664 |
| DISC1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| SESTD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| MICAL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| AHCYL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| KCNE3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| GOPC | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| PDZD2 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=50.3 + PDB: 无 | pLDDT=50.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Synapse / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DACT1 — Dapper homolog 1，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小836 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 69 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=50.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NYF0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000165617-DACT1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DACT1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NYF0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
