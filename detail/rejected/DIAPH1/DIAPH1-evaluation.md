---
type: protein-evaluation
gene: "DIAPH1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DIAPH1 — REJECTED (核定位证据不足 (核定位得分 3/10 <= 3); 研究热度过高 (PubMed strict=208，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DIAPH1 |
| 蛋白名称 | Protein diaphanous homolog 1 |
| 蛋白大小 | 1272 aa / 141.3 kDa |
| UniProt ID | O60610 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 3/10 | x4 | 12 | HPA: Plasma membrane, Cytosol; UniProt: Cell membrane; Cell projection, ruffle membrane; Cytoplasm,  |
| 蛋白大小 | 5/10 | x1 | 5 | 1272 aa / 141.3 kDa |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=208 篇 (>100->REJECTED) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=72.8; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **60.5/180** | |
| **归一化总分** | | | **33.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cytosol | Uncertain |
| UniProt | Cell membrane; Cell projection, ruffle membrane; Cytoplasm, cytoskeleton; Cytoplasm, cytoskeleton, m... | Swiss-Prot/TremBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据不足，HPA与UniProt存在矛盾或缺乏核注释。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 208 |
| PubMed broad count | 334 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Genetic Hearing Loss Overview.. **. PMID: 20301607
2. Identification and validation of biomarkers associated with mitotic catastrophe in high-altitude hypoxia.. *Hereditas*. PMID: 42169094
3. Acute hyperglycemia induces NETosis and futile recanalization after ischemic stroke via RAGE/DIAPH1 pathway.. *Eur J Pharmacol*. PMID: 41990906
4. Recessive loss of DIAPH1 function causes a progressive neurodevelopmental syndrome with variable immunological involvement.. *Genet Med*. PMID: 41860019
5. DIAPH1 regulates the Wnt/β-catenin pathway resulting in microcephaly and visual impairment.. *BMC Med Genomics*. PMID: 41963888

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.8 |
| 高置信度残基 (pLDDT>90) 占比 | 31.5% |
| 置信残基 (pLDDT 70-90) 占比 | 32.6% |
| 中等置信 (pLDDT 50-70) 占比 | 10.3% |
| 低置信 (pLDDT<50) 占比 | 25.6% |
| 有序区域 (pLDDT>70) 占比 | 64.1% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=72.8，有序区 64.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RHOA | 0.000 | 0.000 | — |
| RHOC | 0.000 | 0.000 | — |
| AGER | 0.000 | 0.000 | — |
| PFN4 | 0.000 | 0.000 | — |
| PFN1 | 0.000 | 0.000 | — |
| PFN3 | 0.000 | 0.000 | — |
| RHOD | 0.000 | 0.000 | — |
| ACTG1 | 0.000 | 0.000 | — |
| ACTB | 0.000 | 0.000 | — |
| DIAPH3 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:O08808 | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:- |
| uniprotkb:O60610 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q8BKX1 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:O43852 | psi-mi:"MI:0030"(cross-linking study) | pubmed:- |
| uniprotkb:Q93079 | psi-mi:"MI:0030"(cross-linking study) | pubmed:- |
| uniprotkb:Q71DI3 | psi-mi:"MI:0030"(cross-linking study) | pubmed:- |
| uniprotkb:O60610-2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:O15427 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:G3V4T2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.8 + PDB: 无 | pLDDT=72.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane; Cell projection, ruffle membrane; C / Plasma membrane, Cytosol | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ** (REJECTED)

**核心优势**:
1. DIAPH1 -- Protein diaphanous homolog 1，研究基础较多，新颖性有限。
2. 蛋白大小1272 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 208 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（<=3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O60610
- Protein Atlas: https://www.proteinatlas.org/ENSG00000131504-DIAPH1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DIAPH1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O60610
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
