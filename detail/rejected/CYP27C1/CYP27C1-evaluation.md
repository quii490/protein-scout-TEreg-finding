---
type: protein-evaluation
gene: "CYP27C1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CYP27C1 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CYP27C1 |
| 蛋白名称 | Cytochrome P450 27C1 |
| 蛋白大小 | 542 aa / 60.9 kDa |
| UniProt ID | Q4G0S4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: Vesicles; UniProt: Mitochondrion membrane |
| 蛋白大小 | 10/10 | x1 | 10 | 542 aa / 60.9 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=19 篇 (≤20→10) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=85.4; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 2/10 | x3 | 6 | STRING 0 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.0/180** | |
| **归一化总分** | | | **61.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles | Enhanced |
| UniProt | Mitochondrion membrane | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 19 |
| PubMed broad count | 27 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Prognostic and Therapeutic Value of Metabolism-Related Genes in Nephroblastoma: A Focus on the Key Gene NNMT and Its Regulative Effect on Metabolism.. *Cell Biochem Funct*. PMID: 40574709
2. Light environment and seasonal variation in the visual system of the red shiner (Cyprinella lutrensis).. *J Exp Biol*. PMID: 39935365
3. Visual pigment chromophore usage in Nicaraguan Midas cichlids: phenotypic plasticity and genetic assimilation of cyp27c1 expression.. *Hydrobiologia*. PMID: 40741213
4. In silico structural features of the CgNR5A: CgDAX complex and its role in regulating gene expression of CYP target genes in Crassostrea gigas.. *Chemosphere*. PMID: 38815811
5. Enzymatic vitamin A(2) production enables red-shifted optogenetics.. *Pflugers Arch*. PMID: 37987804

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.4 |
| 高置信度残基 (pLDDT>90) 占比 | 71.0% |
| 置信残基 (pLDDT 70-90) 占比 | 13.1% |
| 中等置信 (pLDDT 50-70) 占比 | 4.6% |
| 低置信 (pLDDT<50) 占比 | 11.3% |
| 有序区域 (pLDDT>70) 占比 | 84.1% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=85.4，有序区 84.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q4G0S4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P48039 | psi-mi:"MI:0112"(ubiquitin reconstruction) | pubmed:- |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 3
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.4 + PDB: 无 | pLDDT=85.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Mitochondrion membrane / Vesicles | 一致 |
| PPI | STRING + IntAct | 0 + 3 interactions | 数据有限 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CYP27C1 -- Cytochrome P450 27C1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小542 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 19 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q4G0S4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000186684-CYP27C1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CYP27C1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q4G0S4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
