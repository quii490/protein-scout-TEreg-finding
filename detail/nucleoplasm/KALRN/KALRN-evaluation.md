---
type: protein-evaluation
gene: "KALRN"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KALRN 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KALRN / DUET, DUO, HAPIP, TRAD |
| 蛋白名称 | Kalirin |
| 蛋白大小 | 2986 aa / 340.3 kDa |
| UniProt ID | O60229 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Cytoplasm; Cytoplasm, cytoskeleton |
| 蛋白大小 | 2/10 | ×1 | 2 | 2986 aa / 340.3 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=72 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.2; PDB: 5QQD, 5QQE, 5QQF, 5QQG, 5QQH, 5QQI, 5QQJ |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001251, IPR036865, IPR035899, IPR000219, IPR003 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **93.5/180** | |
| **归一化总分** | | | **51.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Approved |
| UniProt | Cytoplasm; Cytoplasm, cytoskeleton | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- actin cytoskeleton (GO:0015629)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- extrinsic component of membrane (GO:0019898)
- nucleoplasm (GO:0005654)
- postsynaptic density (GO:0014069)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 72 |
| PubMed broad count | 211 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DUET, DUO, HAPIP, TRAD |

**关键文献**:
1. Identification and characterization of human KALRN mRNA and Kalirin protein isoforms.. *Cerebral cortex (New York, N.Y. : 1991)*. PMID: 39656879
2. KALRN: A central regulator of synaptic function and synaptopathies.. *Gene*. PMID: 33189799
3. KALRN Rare and Common Variants and Susceptibility to Ischemic Stroke in Chinese Han Population.. *Neuromolecular medicine*. PMID: 25917671
4. KALRN mutations promote antitumor immunity and immunotherapy response in cancer.. *Journal for immunotherapy of cancer*. PMID: 33037113
5. Resequencing and association analysis of the KALRN and EPHB1 genes and their contribution to schizophrenia susceptibility.. *Schizophrenia bulletin*. PMID: 21041834

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.2 |
| 高置信度残基 (pLDDT>90) 占比 | 33.1% |
| 置信残基 (pLDDT 70-90) 占比 | 26.3% |
| 中等置信 (pLDDT 50-70) 占比 | 6.0% |
| 低置信 (pLDDT<50) 占比 | 34.6% |
| 有序区域 (pLDDT>70) 占比 | 59.4% |
| 可用 PDB 条目 | 5QQD, 5QQE, 5QQF, 5QQG, 5QQH, 5QQI, 5QQJ, 5QQK, 5QQL, 5QQM |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=67.2），有序残基占 59.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001251, IPR036865, IPR035899, IPR000219, IPR003961; Pfam: PF13716, PF00041, PF07679 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PAM | 0.973 | 0.234 | — |
| RAC1 | 0.959 | 0.642 | — |
| DLG4 | 0.956 | 0.250 | — |
| RHOG | 0.921 | 0.301 | — |
| ARHGAP31 | 0.877 | 0.000 | — |
| DAPK3 | 0.873 | 0.057 | — |
| DAPK2 | 0.859 | 0.057 | — |
| RABIF | 0.848 | 0.000 | — |
| DISC1 | 0.838 | 0.342 | — |
| MYLK | 0.819 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| COIL | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| GFI1B | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| DISC1 | psi-mi:"MI:0018"(two hybrid) | pubmed:17043677|imex:IM-16650 |
| NDEL1 | psi-mi:"MI:0018"(two hybrid) | pubmed:17043677|imex:IM-16650 |
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |
| ENO3 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| FASLG | psi-mi:"MI:0084"(phage display) | pubmed:19807924|imex:IM-20398 |
| Dlg4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-11694|pubmed:19455133 |
| ATXN7 | psi-mi:"MI:0018"(two hybrid) | pubmed:21078624|imex:IM-17207 |
| CACNA1A | psi-mi:"MI:0018"(two hybrid) | pubmed:21078624|imex:IM-17207 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.2 + PDB: 5QQD, 5QQE, 5QQF, 5QQG, 5QQH,  | pLDDT=67.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm, cytoskeleton / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. KALRN — Kalirin，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小2986 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 72 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=67.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O60229
- Protein Atlas: https://www.proteinatlas.org/ENSG00000160145-KALRN/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KALRN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O60229
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
