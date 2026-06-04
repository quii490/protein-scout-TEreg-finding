---
type: protein-evaluation
gene: "ATXN1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ATXN1 — REJECTED (研究热度过高 (PubMed strict=250，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ATXN1 / ATX1, SCA1 |
| 蛋白名称 | Ataxin-1 |
| 蛋白大小 | 815 aa / 86.9 kDa |
| UniProt ID | P54253 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nucleoli, Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 815 aa / 86.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=250 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=50.9; PDB: 1OA8, 2M41, 4APT, 4AQP, 4J2J, 4J2L, 6QIU |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR020997, IPR043404, IPR003652, IPR036096; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **79.5/180** | |
| **归一化总分** | | | **44.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli, Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nuclear inclusion body (GO:0042405)
- nuclear matrix (GO:0016363)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- postsynapse (GO:0098794)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 250 |
| PubMed broad count | 775 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ATX1, SCA1 |

**关键文献**:
1. Antagonistic roles of canonical and Alternative-RPA in disease-associated tandem CAG repeat instability.. *Cell*. PMID: 37827155
2. Hereditary Ataxia Overview.. **. PMID: 20301317
3. Interactome Mapping Provides a Network of Neurodegenerative Disease Proteins and Uncovers Widespread Protein Aggregation in Affected Brains.. *Cell reports*. PMID: 32814053
4. Genetic variability in sporadic amyotrophic lateral sclerosis.. *Brain : a journal of neurology*. PMID: 37043475
5. UTteR control through miRs: fine-tuning ATXN1 levels to prevent ataxia.. *Genes & development*. PMID: 32873576

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 50.9 |
| 高置信度残基 (pLDDT>90) 占比 | 14.8% |
| 置信残基 (pLDDT 70-90) 占比 | 3.1% |
| 中等置信 (pLDDT 50-70) 占比 | 6.7% |
| 低置信 (pLDDT<50) 占比 | 75.3% |
| 有序区域 (pLDDT>70) 占比 | 17.9% |
| 可用 PDB 条目 | 1OA8, 2M41, 4APT, 4AQP, 4J2J, 4J2L, 6QIU |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=50.9），有序残基占 17.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR020997, IPR043404, IPR003652, IPR036096; Pfam: PF12547, PF08517 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CIC | 0.996 | 0.982 | — |
| UBQLN4 | 0.992 | 0.322 | — |
| KAT5 | 0.979 | 0.312 | — |
| NCOR2 | 0.979 | 0.476 | — |
| RBM17 | 0.975 | 0.301 | — |
| ATXN1L | 0.970 | 0.359 | — |
| ATXN2 | 0.969 | 0.313 | — |
| RBPJ | 0.967 | 0.370 | — |
| PQBP1 | 0.946 | 0.311 | — |
| PUM2 | 0.916 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000416360.1 | psi-mi:"MI:0018"(two hybrid) | pubmed:11001934|imex:IM-19618 |
| UBQLN4 | psi-mi:"MI:0018"(two hybrid) | pubmed:11001934|imex:IM-19618 |
| ATP6V0D1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| GCFC2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| CCNK | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| CDK6 | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| NUDT21 | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| CRK | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| BEND2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| EFEMP2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=50.9 + PDB: 1OA8, 2M41, 4APT, 4AQP, 4J2J,  | pLDDT=50.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm; 额外: Nucleoli, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. ATXN1 — Ataxin-1，研究基础较多，新颖性有限。
2. 蛋白大小815 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 250 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=50.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 250 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P54253
- Protein Atlas: https://www.proteinatlas.org/ENSG00000124788-ATXN1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ATXN1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P54253
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
