---
type: protein-evaluation
gene: "DGCR8"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DGCR8 — REJECTED (研究热度过高 (PubMed strict=480，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DGCR8 / C22orf12, DGCRK6 |
| 蛋白名称 | Microprocessor complex subunit DGCR8 |
| 蛋白大小 | 773 aa / 86.0 kDa |
| UniProt ID | Q8WYQ5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nuclear bodies; UniProt: Nucleus; Nucleus, nucleolus |
| 蛋白大小 | 10/10 | ×1 | 10 | 773 aa / 86.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=480 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.2; PDB: 1X47, 2YT4, 3LE4, 5B16, 6LXD, 6LXE, 6V5B |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR040375, IPR014720, IPR001202, IPR036020; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear bodies | Supported |
| UniProt | Nucleus; Nucleus, nucleolus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- glutamatergic synapse (GO:0098978)
- microprocessor complex (GO:0070877)
- nuclear body (GO:0016604)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 480 |
| PubMed broad count | 776 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C22orf12, DGCRK6 |

**关键文献**:
1. The biogenesis and regulation of animal microRNAs.. *Nature reviews. Molecular cell biology*. PMID: 39702526
2. HNRNPA2B1 Is a Mediator of m(6)A-Dependent Nuclear RNA Processing Events.. *Cell*. PMID: 26321680
3. Regulation of MicroRNAs.. *Methods in molecular biology (Clifton, N.J.)*. PMID: 34432271
4. Retraction Note.. *European review for medical and pharmacological sciences*. PMID: 41059755
5. EnABLing microprocessor for apoptosis.. *Molecular & cellular oncology*. PMID: 27182551

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.2 |
| 高置信度残基 (pLDDT>90) 占比 | 23.2% |
| 置信残基 (pLDDT 70-90) 占比 | 21.2% |
| 中等置信 (pLDDT 50-70) 占比 | 12.5% |
| 低置信 (pLDDT<50) 占比 | 43.1% |
| 有序区域 (pLDDT>70) 占比 | 44.4% |
| 可用 PDB 条目 | 1X47, 2YT4, 3LE4, 5B16, 6LXD, 6LXE, 6V5B, 6V5C, 7CNC, 9ASM |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=63.2），有序残基占 44.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR040375, IPR014720, IPR001202, IPR036020; Pfam: PF00035 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DROSHA | 0.999 | 0.991 | — |
| DDX17 | 0.996 | 0.520 | — |
| DDX5 | 0.993 | 0.306 | — |
| DICER1 | 0.993 | 0.271 | — |
| HNRNPA2B1 | 0.991 | 0.000 | — |
| METTL14 | 0.989 | 0.000 | — |
| METTL3 | 0.985 | 0.000 | — |
| AGO2 | 0.984 | 0.000 | — |
| MECP2 | 0.974 | 0.231 | — |
| TARBP2 | 0.966 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| drosha | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| "Su | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| pasha | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| EEF1D | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| CUL3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| SRPK1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:23602568|imex:IM-17935 |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| MECP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZBTB48 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MPHOSPH10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.2 + PDB: 1X47, 2YT4, 3LE4, 5B16, 6LXD,  | pLDDT=63.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus, nucleolus / Nucleoplasm, Nuclear bodies | 一致 |
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
1. DGCR8 — Microprocessor complex subunit DGCR8，研究基础较多，新颖性有限。
2. 蛋白大小773 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 480 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=63.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 480 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WYQ5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000128191-DGCR8/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DGCR8
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WYQ5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
