---
type: protein-evaluation
gene: "PCLO"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PCLO — REJECTED (研究热度过高 (PubMed strict=107，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PCLO / ACZ, KIAA0559 |
| 蛋白名称 | Protein piccolo |
| 蛋白大小 | 5142 aa / 560.7 kDa |
| UniProt ID | Q9Y6V0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Plasma membrane; 额外: Nuclear speckles; UniProt: Presynaptic active zone |
| 蛋白大小 | 0/10 | ×1 | 0 | 5142 aa / 560.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=107 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.1; PDB: 1UJD |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000008, IPR035892, IPR042720, IPR001478, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **58.5/180** | |
| **归一化总分** | | | **32.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane; 额外: Nuclear speckles | Approved |
| UniProt | Presynaptic active zone | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- axon (GO:0030424)
- cytoskeleton (GO:0005856)
- cytoskeleton of presynaptic active zone (GO:0048788)
- extracellular exosome (GO:0070062)
- GABA-ergic synapse (GO:0098982)
- glutamatergic synapse (GO:0098978)
- postsynaptic density (GO:0014069)
- synapse (GO:0045202)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 107 |
| PubMed broad count | 224 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ACZ, KIAA0559 |

**关键文献**:
1. The PCLO gene and depressive disorders: replication in a population-based study.. *Human molecular genetics*. PMID: 19942622
2. Gene structure and genetic localization of the PCLO gene encoding the presynaptic active zone protein Piccolo.. *International journal of developmental neuroscience : the official journal of the International Society for Developmental Neuroscience*. PMID: 12175852
3. Whole-exome sequencing analysis identifies risk genes for schizophrenia.. *Nature communications*. PMID: 40753099
4. Identification of neoantigen epitopes in cervical cancer by multi-omics analysis.. *European journal of medical research*. PMID: 40826144
5. Schizophrenia risk conferred by rare protein-truncating variants is conserved across diverse human populations.. *Nature genetics*. PMID: 36914870

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.1 |
| 高置信度残基 (pLDDT>90) 占比 | 31.5% |
| 置信残基 (pLDDT 70-90) 占比 | 4.2% |
| 中等置信 (pLDDT 50-70) 占比 | 33.1% |
| 低置信 (pLDDT<50) 占比 | 31.2% |
| 有序区域 (pLDDT>70) 占比 | 35.7% |
| 可用 PDB 条目 | 1UJD |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=66.1），有序残基占 35.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000008, IPR035892, IPR042720, IPR001478, IPR036034; Pfam: PF00168, PF00595, PF05715 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RAPGEF4 | 0.989 | 0.095 | — |
| RAB3A | 0.934 | 0.000 | — |
| BSN | 0.904 | 0.071 | — |
| RIMS2 | 0.892 | 0.091 | — |
| RABAC1 | 0.874 | 0.071 | — |
| CTBP2 | 0.831 | 0.045 | — |
| LRP1B | 0.693 | 0.000 | — |
| SYN1 | 0.691 | 0.000 | — |
| MUC16 | 0.685 | 0.095 | — |
| UNC13A | 0.670 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Rabac1 | psi-mi:"MI:0018"(two hybrid) | pubmed:10707984 |
| Bsn | psi-mi:"MI:0663"(confocal microscopy) | pubmed:10707984 |
| Gria1 | psi-mi:"MI:0663"(confocal microscopy) | pubmed:10707984 |
| FLOT1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| SEC22B | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| HMGN2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H1-1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| HMGA1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| TNIK | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.1 + PDB: 1UJD | pLDDT=66.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Presynaptic active zone / Plasma membrane; 额外: Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. PCLO — Protein piccolo，研究基础较多，新颖性有限。
2. 蛋白大小5142 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 107 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=66.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 107 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y6V0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000186472-PCLO/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PCLO
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y6V0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
