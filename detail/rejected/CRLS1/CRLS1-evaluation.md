---
type: protein-evaluation
gene: "CRLS1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CRLS1 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CRLS1 / C20orf155, CLS1 |
| 蛋白名称 | Cardiolipin synthase (CMP-forming) |
| 蛋白大小 | 301 aa / 32.6 kDa |
| UniProt ID | Q9UJA2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: 暂无HPA定位数据; UniProt: Mitochondrion inner membrane |
| 蛋白大小 | 10/10 | x1 | 10 | 301 aa / 32.6 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=34 篇 (≤40→8) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold v6 pLDDT=69.0; PDB: 无 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR050324, IPR000462, IPR043130; Pfam: PF01066 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **99.5/180** | |
| **归一化总分** | | | **55.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Mitochondrion inner membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- mitochondrial inner membrane (GO:0005743)
- mitochondrial membrane (GO:0031966)
- mitochondrion (GO:0005739)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 34 |
| PubMed broad count | 65 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C20orf155, CLS1 |

**关键文献**:
1. Ginsenoside Rg3 Restores Mitochondrial Cardiolipin Homeostasis via GRB2 to Prevent Parkinson's Disease.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 39159293
2. ANXA1 improves mitochondrial homeostasis through uncoupling protein 1 in diabetic nephropathy.. *Journal of advanced research*. PMID: 41275961
3. Cardiolipin Synthase 1 Ameliorates NASH Through Activating Transcription Factor 3 Transcriptional Inactivation.. *Hepatology (Baltimore, Md.)*. PMID: 32096565
4. CRLS1 influences liver metastasis in colon cancer by regulating lipid metabolism pathways.. *Functional & integrative genomics*. PMID: 41116087
5. Deleterious variants in CRLS1 lead to cardiolipin deficiency and cause an autosomal recessive multi-system mitochondrial disease.. *Human molecular genetics*. PMID: 35147173

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.0 |
| 高置信度残基 (pLDDT>90) 占比 | 35.2% |
| 置信残基 (pLDDT 70-90) 占比 | 20.6% |
| 中等置信 (pLDDT 50-70) 占比 | 11.6% |
| 低置信 (pLDDT<50) 占比 | 32.6% |
| 有序区域 (pLDDT>70) 占比 | 55.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=69.0），有序残基占 55.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050324, IPR000462, IPR043130; Pfam: PF01066 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CDS1 | 0.985 | 0.103 | — |
| CDS2 | 0.985 | 0.103 | — |
| PGS1 | 0.976 | 0.000 | — |
| TAZ | 0.970 | 0.000 | — |
| LCLAT1 | 0.968 | 0.000 | — |
| CDIPT | 0.950 | 0.000 | — |
| LPGAT1 | 0.946 | 0.000 | — |
| LPCAT1 | 0.941 | 0.000 | — |
| LPCAT2 | 0.940 | 0.000 | — |
| LPCAT4 | 0.926 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=69.0 + PDB: 无 | pLDDT=69.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Mitochondrion inner membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CRLS1 -- Cardiolipin synthase (CMP-forming)，非常新颖，仅有少数基础研究。
2. 蛋白大小301 aa，大小适中（200-800 aa），适合常规生化实验。

**风险/不确定性**:
1. PubMed 34 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=69.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UJA2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000088766-CRLS1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CRLS1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UJA2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UJA2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
