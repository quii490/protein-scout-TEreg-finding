---
type: protein-evaluation
gene: "DNAJB9"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DNAJB9 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3); 研究热度过高 (PubMed strict=146，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DNAJB9 |
| 蛋白名称 | DnaJ homolog subfamily B member 9 |
| 蛋白大小 | 223 aa / 25.5 kDa |
| UniProt ID | Q9UBS3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: Endoplasmic reticulum, Cytosol; UniProt: Endoplasmic reticulum lumen |
| 蛋白大小 | 10/10 | x1 | 10 | 223 aa / 25.5 kDa |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=146 篇 (>100->REJECTED) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold v6 pLDDT=65.6; PDB: 无 |
| 调控结构域 | 5/10 | x2 | 10 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **56.0/180** | |
| **归一化总分** | | | **31.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Endoplasmic reticulum, Cytosol | Approved |
| UniProt | Endoplasmic reticulum lumen | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 146 |
| PubMed broad count | 159 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Lesson for the clinical nephrologist: unexplained progressive kidney disease with minimal proteinuria: a needle in the haystack.. *J Nephrol*. PMID: 42153899
2. A rare case of renal AHL amyloidosis with marked complement deposition: clinicopathologic and proteomic findings.. *BMC Nephrol*. PMID: 42062954
3. A case of lupus nephritis combined with fibrillary glomerulonephritis diagnosed using mass spectrometry and immunohistochemistry of DNAJB9.. *Clin Nephrol*. PMID: 42021711
4. New biomarkers for the detection of fetal death derived from large-scale proteomic analysis of maternal plasma.. *Am J Obstet Gynecol*. PMID: 41935727
5. Fibrillary Glomerulonephritis and Apolipoprotein A-IV Amyloidosis: A Rare Dual Pathology Diagnosed by Mass Spectrometry and DNAJB9 Immunohistochemistry.. *Kidney Med*. PMID: 41884769

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.6 |
| 高置信度残基 (pLDDT>90) 占比 | 3.1% |
| 置信残基 (pLDDT 70-90) 占比 | 42.2% |
| 中等置信 (pLDDT 50-70) 占比 | 26.9% |
| 低置信 (pLDDT<50) 占比 | 27.8% |
| 有序区域 (pLDDT>70) 占比 | 45.3% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=65.6），有序残基占 45.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HSPA5 | 0.000 | 0.000 | — |
| XBP1 | 0.000 | 0.000 | — |
| SIL1 | 0.000 | 0.000 | — |
| HYOU1 | 0.000 | 0.000 | — |
| HSP90B1 | 0.000 | 0.000 | — |
| HSPA13 | 0.000 | 0.000 | — |
| HSPA6 | 0.000 | 0.000 | — |
| EDEM1 | 0.000 | 0.000 | — |
| HSPA1B | 0.000 | 0.000 | — |
| HSPA1A | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:P53350 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:P63167 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q16658 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:P60660 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q15560 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q969G6 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:O95907 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q8NEG0 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:P97554 | psi-mi:"MI:0232"(transcriptional complementation a | pubmed:- |
| uniprotkb:Q9UBS3 | psi-mi:"MI:0096"(pull down) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.6 + PDB: 无 | pLDDT=65.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum lumen / Endoplasmic reticulum, Cytosol | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ** (REJECTED)

**核心优势**:
1. DNAJB9 -- DnaJ homolog subfamily B member 9，研究基础较多，新颖性有限。
2. 蛋白大小223 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 146 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=65.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（<=3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UBS3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000128590-DNAJB9/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DNAJB9
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UBS3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
