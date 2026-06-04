---
type: protein-evaluation
gene: "COG6"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## COG6 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | COG6 / KIAA1134 |
| 蛋白名称 | Conserved oligomeric Golgi complex subunit 6 |
| 蛋白大小 | 657 aa / 73.3 kDa |
| UniProt ID | Q9Y2V7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Nuclear speckles, Golgi apparatus; UniProt: Golgi apparatus membrane |
| 蛋白大小 | 10/10 | x1 | 10 | 657 aa / 73.3 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=37 篇 (<=40->8) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=85.9; PDB: 无 |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR010490, IPR048369, IPR048368; Pfam: PF20653, PF |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.5/180** | |
| **归一化总分** | | | **64.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles, Golgi apparatus | Approved |
| UniProt | Golgi apparatus membrane | Swiss-Prot/TremBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- Golgi membrane (GO:0000139)
- Golgi transport complex (GO:0017119)
- trans-Golgi network membrane (GO:0032588)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 37 |
| PubMed broad count | 65 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1134 |

**关键文献**:
1. Blood DNA methylation profiling identifies cathepsin Z dysregulation in pulmonary arterial hypertension.. *Nature communications*. PMID: 38184627
2. COG6-CDG: Novel variants and novel malformation.. *Birth defects research*. PMID: 35068072
3. COG6 is an essential host factor for influenza A virus infection.. *Microbiology spectrum*. PMID: 40910953
4. Secondary Hemophagocytic Syndrome Associated with COG6 Gene Defect: Report and Review.. *JIMD reports*. PMID: 29445937
5. Arabidopsis COG6 is essential for pollen tube growth and Golgi structure maintenance.. *Biochemical and biophysical research communications*. PMID: 32499114

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.9 |
| 高置信度残基 (pLDDT>90) 占比 | 56.9% |
| 置信残基 (pLDDT 70-90) 占比 | 34.1% |
| 中等置信 (pLDDT 50-70) 占比 | 4.1% |
| 低置信 (pLDDT<50) 占比 | 4.9% |
| 有序区域 (pLDDT>70) 占比 | 91.0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=85.9，有序区 91.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR010490, IPR048369, IPR048368; Pfam: PF20653, PF06419 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| COG5 | 0.999 | 0.905 | — |
| COG4 | 0.999 | 0.917 | — |
| COG2 | 0.999 | 0.919 | — |
| COG7 | 0.999 | 0.909 | — |
| COG8 | 0.999 | 0.925 | — |
| COG1 | 0.999 | 0.913 | — |
| COG3 | 0.999 | 0.985 | — |
| STX6 | 0.914 | 0.232 | — |
| SNAP29 | 0.905 | 0.142 | — |
| GOSR2 | 0.897 | 0.087 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| COG5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| COG3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| COG4 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| COG8 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| SNX4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:15263065|mint:MINT-5217 |
| NPL6 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14729968|imex:IM-19865 |
| RSC3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14729968|imex:IM-19865 |
| UBC7 | psi-mi:"MI:0397"(two hybrid array) | pubmed:14690591 |
| cogc-6 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:19123269 |
| cogc-8 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:19123269 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.9 + PDB: 无 | pLDDT=85.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus membrane / Nuclear speckles, Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ***

**核心优势**:
1. COG6 -- Conserved oligomeric Golgi complex subunit 6，非常新颖，仅有少数基础研究。
2. 蛋白大小657 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 37 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y2V7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000133103-COG6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=COG6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y2V7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
