---
type: protein-evaluation
gene: "CBLC"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CBLC — REJECTED (研究热度过高 (PubMed strict=240，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CBLC / CBL3, RNF57 |
| 蛋白名称 | E3 ubiquitin-protein ligase CBL-C |
| 蛋白大小 | 474 aa / 52.5 kDa |
| UniProt ID | Q9ULV8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Nucleoplasm; 额外: Aggresome; UniProt: 无注释 |
| 蛋白大小 | 10/10 | x1 | 10 | 474 aa / 52.5 kDa |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=240 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | x3 | 30 | AlphaFold v6 pLDDT=80.1; PDB: 3OP0, 3VRN, 3VRO, 3VRP, 3VRQ, 3VRR |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR024162, IPR014741, IPR036537, IPR003153, IPR014 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **84.0/180** | |
| **归一化总分** | | | **46.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Aggresome | Approved |
| UniProt | 无注释 | Swiss-Prot/TremBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- membrane raft (GO:0045121)
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 240 |
| PubMed broad count | 452 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CBL3, RNF57 |

**关键文献**:
1. Late-onset methylmalonic acidemia and homocysteinemia (cblC disease): systematic review.. *Orphanet journal of rare diseases*. PMID: 38245797
2. Cobalamin C defect: natural history, pathophysiology, and treatment.. *Journal of inherited metabolic disease*. PMID: 20632110
3. Molecular genetic characterization of cblC defects in 126 pedigrees and prenatal genetic diagnosis of pedigrees with combined methylmalonic aciduria and homocystinuria.. *BMC medical genetics*. PMID: 30157807
4. Mutations in Hcfc1 and Ronin result in an inborn error of cobalamin metabolism and ribosomopathy.. *Nature communications*. PMID: 35013307
5. The c-Cbl oncoprotein.. *The international journal of biochemistry & cell biology*. PMID: 9675877

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.1 |
| 高置信度残基 (pLDDT>90) 占比 | 53.4% |
| 置信残基 (pLDDT 70-90) 占比 | 25.3% |
| 中等置信 (pLDDT 50-70) 占比 | 5.3% |
| 低置信 (pLDDT<50) 占比 | 16.0% |
| 有序区域 (pLDDT>70) 占比 | 78.7% |
| 可用 PDB 条目 | 3OP0, 3VRN, 3VRO, 3VRP, 3VRQ, 3VRR |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（3OP0, 3VRN, 3VRO, 3VRP, 3VRQ, 3VRR）+ AlphaFold极高置信度预测（pLDDT=80.1），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR024162, IPR014741, IPR036537, IPR003153, IPR014742; Pfam: PF02262, PF02761, PF02762 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EGFR | 0.997 | 0.989 | — |
| SRC | 0.979 | 0.973 | — |
| FYN | 0.954 | 0.932 | — |
| YES1 | 0.924 | 0.923 | — |
| CBLB | 0.913 | 0.095 | — |
| CBL | 0.912 | 0.091 | — |
| SH3KBP1 | 0.859 | 0.094 | — |
| SH3GL3 | 0.814 | 0.095 | — |
| SH3GLB2 | 0.801 | 0.000 | — |
| SH3GL2 | 0.800 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| OXA1L | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| UBE2L6 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-11696|pubmed:19549727 |
| UBE2R2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-11696|pubmed:19549727 |
| HIP2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-11696|pubmed:19549727 |
| UBE2H | psi-mi:"MI:0397"(two hybrid array) | imex:IM-11696|pubmed:19549727 |
| UBE2I | psi-mi:"MI:0397"(two hybrid array) | imex:IM-11696|pubmed:19549727 |
| UBE2L3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-11696|pubmed:19549727 |
| recN | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| BIRC2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15696|pubmed:22493164 |
| TRAF4 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15696|pubmed:22493164 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.1 + PDB: 3OP0, 3VRN, 3VRO, 3VRP, 3VRQ,  | pLDDT=80.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Aggresome | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (>=3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CBLC -- E3 ubiquitin-protein ligase CBL-C，研究基础较多，新颖性有限。
2. 蛋白大小474 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 240 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 240 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9ULV8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000142273-CBLC/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CBLC
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9ULV8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
