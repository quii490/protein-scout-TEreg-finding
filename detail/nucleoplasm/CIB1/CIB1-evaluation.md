---
type: protein-evaluation
gene: "CIB1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CIB1 — REJECTED (研究热度过高 (PubMed strict=191，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CIB1 / CIB, KIP, PRKDCIP |
| 蛋白名称 | Calcium and integrin-binding protein 1 |
| 蛋白大小 | 191 aa / 21.7 kDa |
| UniProt ID | Q99828 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoplasm, Plasma membrane; 额外: Nuclear bodies; UniProt: Membrane; Cell membrane, sarcolemma; Cell membrane; Apical c |
| 蛋白大小 | 8/10 | x1 | 8 | 191 aa / 21.7 kDa |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=191 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | x3 | 30 | AlphaFold v6 pLDDT=75.7; PDB: 1DGU, 1DGV, 1XO5, 1Y1A, 2L4H, 2L4I, 2LM5 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR051433, IPR011992, IPR018247, IPR002048; Pfam:  |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **92.0/180** | |
| **归一化总分** | | | **51.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Plasma membrane; 额外: Nuclear bodies | Supported |
| UniProt | Membrane; Cell membrane, sarcolemma; Cell membrane; Apical cell membrane; Cell projection, ruffle me... | Swiss-Prot/TremBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- apical plasma membrane (GO:0016324)
- axon (GO:0030424)
- cell periphery (GO:0071944)
- centrosome (GO:0005813)
- cytoplasm (GO:0005737)
- endoplasmic reticulum (GO:0005783)
- extracellular exosome (GO:0070062)
- filopodium tip (GO:0032433)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 191 |
| PubMed broad count | 345 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CIB, KIP, PRKDCIP |

**关键文献**:
1. Identification of unique cell type responses in pancreatic islets to stress.. *Nature communications*. PMID: 38956087
2. The Emerging Roles of CIB1 in Cancer.. *Cellular physiology and biochemistry : international journal of experimental cellular physiology, biochemistry, and pharmacology*. PMID: 29017172
3. Deubiquitination of CIB1 by USP14 promotes lenvatinib resistance via the PAK1-ERK1/2 axis in hepatocellular carcinoma.. *International journal of biological sciences*. PMID: 38993552
4. CIB1 and platelet integrin αIIbβ3: Molecular mechanisms, disruption strategies and antithrombotic opportunities.. *Thrombosis research*. PMID: 40929801
5. CIB1: a small protein with big ambitions.. *FASEB journal : official publication of the Federation of American Societies for Experimental Biology*. PMID: 27118676

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.7 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 80.1% |
| 中等置信 (pLDDT 50-70) 占比 | 14.1% |
| 低置信 (pLDDT<50) 占比 | 5.8% |
| 有序区域 (pLDDT>70) 占比 | 80.1% |
| 可用 PDB 条目 | 1DGU, 1DGV, 1XO5, 1Y1A, 2L4H, 2L4I, 2LM5, 6OCX, 6OD0 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1DGU, 1DGV, 1XO5, 1Y1A, 2L4H, 2L4I, 2LM5, 6OCX, 6OD0）+ AlphaFold极高置信度预测（pLDDT=75.7），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051433, IPR011992, IPR018247, IPR002048; Pfam: PF13499 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CRY2 | 0.996 | 0.053 | — |
| ITGA2B | 0.983 | 0.510 | — |
| PSEN2 | 0.956 | 0.292 | — |
| ATG13 | 0.939 | 0.000 | — |
| ATG101 | 0.925 | 0.000 | — |
| CDK2 | 0.858 | 0.061 | — |
| CDK4 | 0.855 | 0.098 | — |
| PRKDC | 0.824 | 0.510 | — |
| GUF1 | 0.815 | 0.000 | — |
| CCNL2 | 0.808 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| AURKB | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| CDK4 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| BHLH63 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| hutU | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| treR | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| resE | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| thrS1 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| parC | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| A0A0F7RMC5 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.7 + PDB: 1DGU, 1DGV, 1XO5, 1Y1A, 2L4H,  | pLDDT=75.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Membrane; Cell membrane, sarcolemma; Cell membrane / Nucleoplasm, Plasma membrane; 额外: Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (>=3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CIB1 -- Calcium and integrin-binding protein 1，研究基础较多，新颖性有限。
2. 蛋白大小191 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 191 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 191 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q99828
- Protein Atlas: https://www.proteinatlas.org/ENSG00000185043-CIB1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CIB1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q99828
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
