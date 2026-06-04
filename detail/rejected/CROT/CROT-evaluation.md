---
type: protein-evaluation
gene: "CROT"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CROT — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CROT / COT |
| 蛋白名称 | Peroxisomal carnitine O-octanoyltransferase |
| 蛋白大小 | 612 aa / 70.2 kDa |
| UniProt ID | Q9UKG9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: Vesicles; UniProt: Peroxisome |
| 蛋白大小 | 10/10 | x1 | 10 | 612 aa / 70.2 kDa |
| 研究新颖性 | 6/10 | x5 | 30 | PubMed strict=58 篇 (≤60→6) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=97.2; PDB: 无 |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR000542, IPR042572, IPR023213, IPR039551, IPR042 |
| PPI 网络 | 2/10 | x3 | 6 | STRING 0 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **95.0/180** | |
| **归一化总分** | | | **52.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles | Approved |
| UniProt | Peroxisome | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA检测到可靠IF图像信号。

**GO Cellular Component**:
- cytosol (GO:0005829)
- peroxisomal matrix (GO:0005782)
- peroxisome (GO:0005777)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 58 |
| PubMed broad count | 126 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: COT |

**关键文献**:
1. Single Cell Gene Co-Expression Network Reveals FECH/CROT Signature as a Prognostic Marker.. *Cells*. PMID: 31295943
2. Differential Expression of Lipid Metabolism Genes, CROT and ABCG1, in Obese Patients with Comorbid Depressive Disorder and Risk of MASLD.. *Metabolites*. PMID: 40559416
3. miR‑126a‑5p‑Dbp and miR‑31a‑Crot/Mrpl4 interaction pairs crucial for the development of hypertension and stroke.. *Molecular medicine reports*. PMID: 31545431
4. Genomics of the human carnitine acyltransferase genes.. *Molecular genetics and metabolism*. PMID: 11001805
5. Integrated bioinformatics and machine learning analysis identify CROT as a regulator of immunological features in idiopathic pulmonary fibrosis.. *Biochimica et biophysica acta. Molecular basis of disease*. PMID: 41192648

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 97.2 |
| 高置信度残基 (pLDDT>90) 占比 | 97.5% |
| 置信残基 (pLDDT 70-90) 占比 | 0.7% |
| 中等置信 (pLDDT 50-70) 占比 | 0.3% |
| 低置信 (pLDDT<50) 占比 | 1.5% |
| 有序区域 (pLDDT>70) 占比 | 98.2% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度（pLDDT=97.2，有序区 98.2%）。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000542, IPR042572, IPR023213, IPR039551, IPR042231; Pfam: PF00755 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 无PPI数据
- STRING partners: 0，IntAct interactions: 0
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=97.2 + PDB: 无 | pLDDT=97.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Peroxisome / Vesicles | 一致 |
| PPI | STRING + IntAct | 0 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CROT -- Peroxisomal carnitine O-octanoyltransferase，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小612 aa，大小适中（200-800 aa），适合常规生化实验。

**风险/不确定性**:
1. PubMed 58 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UKG9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000005469-CROT/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CROT
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UKG9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
