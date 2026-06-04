---
type: protein-evaluation
gene: "SMS"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SMS — REJECTED (研究热度过高 (PubMed strict=1344，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SMS |
| 蛋白名称 | Spermine synthase |
| 蛋白大小 | 366 aa / 41.3 kDa |
| UniProt ID | P52788 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nuclear bodies; 额外: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 366 aa / 41.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1344 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=94.8; PDB: 3C6K, 3C6M |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR030374, IPR030373, IPR029063, IPR035246, IPR037 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.0/180** | |
| **归一化总分** | | | **44.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies; 额外: Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1344 |
| PubMed broad count | 15335 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Biological functions of sphingomyelins.. *Progress in lipid research*. PMID: 23684760
2. Smith-Magenis Syndrome-Clinical Review, Biological Background and Related Disorders.. *Genes*. PMID: 35205380
3. The effect of developmental and environmental factors on secondary metabolites in medicinal plants.. *Plant physiology and biochemistry : PPB*. PMID: 31951944
4. Smith-Magenis syndrome.. *European journal of human genetics : EJHG*. PMID: 18231123
5. Smith-Magenis syndrome.. *Handbook of clinical neurology*. PMID: 23622179

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.8 |
| 高置信度残基 (pLDDT>90) 占比 | 87.4% |
| 置信残基 (pLDDT 70-90) 占比 | 9.3% |
| 中等置信 (pLDDT 50-70) 占比 | 3.3% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 96.7% |
| 可用 PDB 条目 | 3C6K, 3C6M |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（3C6K, 3C6M）+ AlphaFold高质量预测（pLDDT=94.8），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR030374, IPR030373, IPR029063, IPR035246, IPR037163; Pfam: PF17284, PF01564, PF17950 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MTAP | 0.986 | 0.000 | — |
| ODC1 | 0.984 | 0.076 | — |
| SRM | 0.971 | 0.000 | — |
| AGMAT | 0.878 | 0.000 | — |
| AZIN2 | 0.870 | 0.076 | — |
| ARG2 | 0.856 | 0.000 | — |
| PAOX | 0.837 | 0.000 | — |
| ARG1 | 0.832 | 0.000 | — |
| MTRR | 0.822 | 0.778 | — |
| PHEX | 0.821 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| mreB | psi-mi:"MI:0096"(pull down) | pubmed:15690043|mint:MINT-5217 |
| radA | psi-mi:"MI:0096"(pull down) | pubmed:16606699 |
| rnk | psi-mi:"MI:0397"(two hybrid array) | pubmed:24561554|imex:IM-22059 |
| mnb | psi-mi:"MI:0018"(two hybrid) | pubmed:15575970|mint:MINT-7952 |
| EZH2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| vers | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| EloC | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| TFE3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| FTSJ1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| Hsp60B | psi-mi:"MI:0397"(two hybrid array) | imex:IM-9552|pubmed:19079254 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.8 + PDB: 3C6K, 3C6M | pLDDT=94.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nuclear bodies; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. SMS — Spermine synthase，研究基础较多，新颖性有限。
2. 蛋白大小366 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1344 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1344 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P52788
- Protein Atlas: https://www.proteinatlas.org/ENSG00000102172-SMS/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SMS
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P52788
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
