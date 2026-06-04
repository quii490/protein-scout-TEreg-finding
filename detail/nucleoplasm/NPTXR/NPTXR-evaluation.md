---
type: protein-evaluation
gene: "NPTXR"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation, recovery, re-evaluation]
status: scored
---

## NPTXR 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NPTXR |
| 蛋白名称 | Neuronal pentraxin receptor |
| 蛋白大小 | 500 aa / 52.8 kDa |
| UniProt ID | O95502 |
| 数据采集时间 | 2026-06-03 23:52:41 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Plasma membrane, Cytosol; 额外: Nucleoplasm; UniProt: Membrane |
| 蛋白大小 | 10/10 | x1 | 10 | 500 aa / 52.8 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=37 篇 (21-40 -> 8) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=76.0; PDB: 无 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR013320, IPR051360, IPR001759; Pfam: PF0035 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | -- | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.5/180** | |
| **归一化总分** | | | **61.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cytosol; 额外: Nucleoplasm | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

**GO Cellular Component**:
- glutamatergic synapse (GO:0098978)
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 37 |
| PubMed broad count | 53 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Proteomic signature of dementia risk in type 2 diabetes.. *Journal of advanced research*. PMID: 40829688
2. Therapeutic Potential of Antibody Targeting Neuronal Pentraxin Receptor in Esophageal Squamous Cell Carcinoma.. *Annals of surgical oncology*. PMID: 38717547
3. Identification of immune-inflammation targets for intracranial aneurysms: a multiomics and epigenome-wide study integrating summary-data-based Mendelian randomization, single-cell-type expression analysis, and DNA methylation regulation.. *International journal of surgery (London, England)*. PMID: 39051921
4. Targeted Proteomics upon Treatment with Tofersen Identifies Novel Response Markers for Superoxide Dismutase 1-Linked Amyotrophic Lateral Sclerosis.. *Annals of neurology*. PMID: 40781905
5. Extracellular matrix dysfunction and synaptic alterations in schizophrenia.. *Molecular psychiatry*. PMID: 40858782

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.0 |
| 高置信度残基 (pLDDT>90) 占比 | 42.0% |
| 置信残基 (pLDDT 70-90) 占比 | 26.6% |
| 中等置信 (pLDDT 50-70) 占比 | 5.8% |
| 低置信 (pLDDT<50) 占比 | 25.6% |
| 有序区域 (pLDDT>70) 占比 | 68.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。**

**评价**: AlphaFold 中等质量（pLDDT=76.0，有序区 68.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013320, IPR051360, IPR001759; Pfam: PF00354 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RCN2 | 0.928 | 0.077 | — |
| CBX6 | 0.895 | 0.000 | — |
| NPR1 | 0.848 | 0.000 | — |
| NPTX2 | 0.836 | 0.436 | — |
| NPR3 | 0.817 | 0.000 | — |
| NPR2 | 0.802 | 0.000 | — |
| NPPA | 0.742 | 0.000 | — |
| NPTX1 | 0.655 | 0.213 | — |
| OCA2 | 0.637 | 0.000 | — |
| NPPC | 0.581 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| IL5RA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SFTPC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PHC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CYB5D2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PARD3B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| FBXO2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SELENON | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PTX4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| NPTX1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SIAE | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.0 + PDB: 无 | pLDDT=76.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Plasma membrane, Cytosol; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ 

**核心优势**:
1. NPTXR -- Neuronal pentraxin receptor，非常新颖，仅有少数基础研究。
2. 蛋白大小500 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 37 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O95502
- Protein Atlas: https://www.proteinatlas.org/ENSG00000221890-NPTXR/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NPTXR
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O95502
- STRING: https://string-db.org/network/9606.NPTXR
- Packet data timestamp: 2026-06-03 23:52:41

---
*本报告为全量重评估 (Full Re-evaluation) -- Recovery from false-rejection。所有评分基于最新harvest packet数据，使用标准/180评分体系计算。*
