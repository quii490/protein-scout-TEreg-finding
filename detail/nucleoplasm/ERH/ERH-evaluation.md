---
type: protein-evaluation
gene: "ERH"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ERH — REJECTED (研究热度过高 (PubMed strict=165，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ERH |
| 蛋白名称 | Enhancer of rudimentary homolog |
| 蛋白大小 | 104 aa / 12.3 kDa |
| UniProt ID | P84090 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 104 aa / 12.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=165 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=95.9; PDB: 1W9G, 2NML, 7CNC, 7X39 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR035912, IPR000781; Pfam: PF01133 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **99.0/180** | |
| **归一化总分** | | | **55.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- methylosome (GO:0034709)
- midbody (GO:0030496)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 165 |
| PubMed broad count | 1152 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Theabrownin from Pu-erh tea attenuates hypercholesterolemia via modulation of gut microbiota and bile acid metabolism.. *Nature communications*. PMID: 31672964
2. Large-scale map of RNA-binding protein interactomes across the mRNA life cycle.. *Molecular cell*. PMID: 39303721
3. ERH: a plug-and-play protein important for gene silencing and cell cycle progression.. *The FEBS journal*. PMID: 36334004
4. ERH Gene and Its Role in Cancer Cells.. *Frontiers in oncology*. PMID: 35677162
5. ERH regulates type II interferon immune signaling through post-transcriptional regulation of JAK2 mRNA.. *Nucleic acids research*. PMID: 40586312

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 95.9 |
| 高置信度残基 (pLDDT>90) 占比 | 92.3% |
| 置信残基 (pLDDT 70-90) 占比 | 6.7% |
| 中等置信 (pLDDT 50-70) 占比 | 1.0% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 99.0% |
| 可用 PDB 条目 | 1W9G, 2NML, 7CNC, 7X39 |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1W9G, 2NML, 7CNC, 7X39）+ AlphaFold高质量预测（pLDDT=95.9），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR035912, IPR000781; Pfam: PF01133 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SNRPF | 0.983 | 0.205 | — |
| SNRPD3 | 0.982 | 0.308 | — |
| SNRPD1 | 0.982 | 0.000 | — |
| SNRPE | 0.981 | 0.000 | — |
| SNRPD2 | 0.980 | 0.096 | — |
| SNRPG | 0.979 | 0.000 | — |
| PRMT1 | 0.968 | 0.450 | — |
| CHTOP | 0.943 | 0.778 | — |
| PRMT5 | 0.936 | 0.099 | — |
| SNRPB | 0.936 | 0.187 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| P70659 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| TP53 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| TLE1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| MED31 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| RBM48 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| SETDB1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| UNC119 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| HSPA8 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| COPS6 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| IGSF21 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=95.9 + PDB: 1W9G, 2NML, 7CNC, 7X39 | pLDDT=95.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. ERH — Enhancer of rudimentary homolog，研究基础较多，新颖性有限。
2. 蛋白大小104 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 165 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 165 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P84090
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100632-ERH/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ERH
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P84090
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
