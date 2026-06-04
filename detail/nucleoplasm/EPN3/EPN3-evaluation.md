---
type: protein-evaluation
gene: "EPN3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EPN3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EPN3 |
| 蛋白名称 | Epsin-3 |
| 蛋白大小 | 632 aa / 68.2 kDa |
| UniProt ID | Q9H201 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Vesicles; 额外: Nucleoplasm; UniProt: Cytoplasm; Cytoplasm, perinuclear region; Cytoplasmic vesicl |
| 蛋白大小 | 10/10 | ×1 | 10 | 632 aa / 68.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=18 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR013809, IPR008942, IPR003903; Pfam: PF01417, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Nucleoplasm | Supported |
| UniProt | Cytoplasm; Cytoplasm, perinuclear region; Cytoplasmic vesicle, clathrin-coated vesicle; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- clathrin vesicle coat (GO:0030125)
- clathrin-coated pit (GO:0005905)
- clathrin-coated vesicle (GO:0030136)
- cytoplasmic side of plasma membrane (GO:0009898)
- endosome (GO:0005768)
- extracellular exosome (GO:0070062)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 18 |
| PubMed broad count | 29 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Epsin 3 potentiates the NF‑κB signaling pathway to regulate apoptosis in breast cancer.. *Molecular medicine reports*. PMID: 34779498
2. Epsin3 promotes non-small cell lung cancer progression via modulating EGFR stability.. *Cell & bioscience*. PMID: 39910656
3. Interferon-alpha responsible EPN3 regulates hepatitis B virus replication.. *Frontiers in medicine*. PMID: 35935763
4. Comprehensive transcriptomic analysis of prostate cancer lung metastases.. *PloS one*. PMID: 39146303
5. Lowering expression of Epsin-3 inhibits migration and invasion of lung adenocarcinoma cells by inhibiting the epithelial-mesenchymal transition.. *Scientific reports*. PMID: 39048677

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.7 |
| 高置信度残基 (pLDDT>90) 占比 | 23.1% |
| 置信残基 (pLDDT 70-90) 占比 | 9.2% |
| 中等置信 (pLDDT 50-70) 占比 | 15.2% |
| 低置信 (pLDDT<50) 占比 | 52.5% |
| 有序区域 (pLDDT>70) 占比 | 32.3% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=59.7），有序残基占 32.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013809, IPR008942, IPR003903; Pfam: PF01417, PF02809 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EPS15 | 0.999 | 0.497 | — |
| CLTCL1 | 0.981 | 0.422 | — |
| SNAP91 | 0.981 | 0.095 | — |
| CLTC | 0.981 | 0.422 | — |
| HIP1R | 0.971 | 0.391 | — |
| ITSN1 | 0.970 | 0.108 | — |
| EPS15L1 | 0.969 | 0.297 | — |
| ITSN2 | 0.960 | 0.108 | — |
| EPN2 | 0.953 | 0.486 | — |
| PICALM | 0.944 | 0.095 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HSP90B1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| YWHAE | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| FAM168A | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| RPS27A | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| RNF8 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| MID1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TRIM26 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| DAZAP2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| LITAF | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| NTAQ1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.7 + PDB: 无 | pLDDT=59.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm, perinuclear region; Cytoplas / Vesicles; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. EPN3 — Epsin-3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小632 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 18 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=59.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H201
- Protein Atlas: https://www.proteinatlas.org/ENSG00000049283-EPN3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EPN3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H201
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
