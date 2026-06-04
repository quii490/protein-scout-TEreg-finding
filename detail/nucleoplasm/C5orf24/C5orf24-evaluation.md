---
type: protein-evaluation
gene: "C5orf24"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## C5orf24 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | C5orf24 |
| 蛋白名称 | UPF0461 protein C5orf24 |
| 蛋白大小 | 188 aa / 20.1 kDa |
| UniProt ID | Q7Z6I8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 5/10 | ×4 | 20 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 188 aa / 20.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=55.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR040419; Pfam: PF17724 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 14 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **119/180** | |
| **归一化总分** | | | **66.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据存在但较为混杂，部分数据源指向非核区室。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 7 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. A feeding-induced myokine modulates glucose homeostasis.. *Nature metabolism*. PMID: 39747483
2. CircRNA-miRNA-mRNA networks in plasma extracellular vesicles as biomarkers for first-onset schizophrenia.. *BMC psychiatry*. PMID: 40634861
3. A novel enzyme-linked ligand-sorbent assay (ELLSA) to screening pulmonary tuberculosis: a retrospective cross-sectional study.. *Microbes and infection*. PMID: 38537770
4. From Gene Discovery to Stroke Risk: C5orf24's Pivotal Role Uncovered.. *Molecular neurobiology*. PMID: 40038197
5. Gene expression differences in PTSD are uniquely related to the intrusion symptom cluster: A transcriptome-wide analysis in military service members.. *Brain, behavior, and immunity*. PMID: 31039430

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 55.1 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 6.9% |
| 中等置信 (pLDDT 50-70) 占比 | 59.0% |
| 低置信 (pLDDT<50) 占比 | 34.0% |
| 有序区域 (pLDDT>70) 占比 | 6.9% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=55.1），有序残基占 6.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR040419; Pfam: PF17724 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| STRADA | 0.685 | 0.685 | — |
| PKNOX2 | 0.591 | 0.591 | — |
| LSMEM2 | 0.506 | 0.000 | — |
| CAB39 | 0.491 | 0.487 | — |
| CATSPER3 | 0.447 | 0.000 | — |
| ZNF551 | 0.431 | 0.000 | — |
| PKNOX1 | 0.431 | 0.420 | — |
| ANKRD13C | 0.428 | 0.000 | — |
| STK11 | 0.422 | 0.422 | — |
| FOXC2 | 0.420 | 0.421 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 14，IntAct interactions: 0
- 调控相关比例: 0 / 14 = 0%

**评价**: STRING 14 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=55.1 + PDB: 无 | pLDDT=55.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 待确认 |
| PPI | STRING + IntAct | 14 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. C5orf24 — UPF0461 protein C5orf24，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小188 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=55.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7Z6I8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000181904-C5orf24/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=C5orf24
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7Z6I8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
