---
type: protein-evaluation
gene: "CNDP1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CNDP1 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3); 研究热度过高 (PubMed strict=104，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CNDP1 |
| 蛋白名称 | Beta-Ala-His dipeptidase |
| 蛋白大小 | 507 aa / 56.7 kDa |
| UniProt ID | Q96KN2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: 暂无HPA定位数据; UniProt: Secreted |
| 蛋白大小 | 10/10 | x1 | 10 | 507 aa / 56.7 kDa |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=104 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=94.0; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 18 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **64.0/180** | |
| **归一化总分** | | | **35.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | No data |
| UniProt | Secreted | Swiss-Prot/TremBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 104 |
| PubMed broad count | 128 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Metabolite-based genome-wide association analysis reveals genetic loci and candidate genes affecting breast muscle metabolites in Sansui ducks.. *Poult Sci*. PMID: 41903465
2. CNDP1 (CTG)(5) allele and cardiovascular events in high-risk patients: LURIC study results.. *Sci Rep*. PMID: 42014802
3. Berberine signature and cardiometabolic diseases using randomized controlled trial, cohort study and Mendelian randomization.. *NPJ Cardiovasc Health*. PMID: 41882153
4. CNDP1 and Diabetic Kidney Disease: From Genetic Susceptibility to Therapeutic Targeting.. *Genes (Basel)*. PMID: 42074485
5. Carnosine Dipeptidase(Cndp): An emerging therapeutic target for metabolic diseases and cancers.. *Genes Dis*. PMID: 41098976

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.0 |
| 高置信度残基 (pLDDT>90) 占比 | 90.9% |
| 置信残基 (pLDDT 70-90) 占比 | 3.4% |
| 中等置信 (pLDDT 50-70) 占比 | 3.2% |
| 低置信 (pLDDT<50) 占比 | 2.6% |
| 有序区域 (pLDDT>70) 占比 | 94.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=94.0，有序区 94.3%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CARNS1 | 0.000 | 0.000 | — |
| CNDP2 | 0.000 | 0.000 | — |
| ABAT | 0.000 | 0.000 | — |
| CARNMT1 | 0.000 | 0.000 | — |
| HDC | 0.000 | 0.000 | — |
| UPB1 | 0.000 | 0.000 | — |
| GAD2 | 0.000 | 0.000 | — |
| GAD1 | 0.000 | 0.000 | — |
| GADL1 | 0.000 | 0.000 | — |
| HAL | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:A5A3E0 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P12236 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P14406 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P16260 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P20337 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q58FF6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q5SRI9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q8TF71 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q96KP4-2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9H3S5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 18
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 18 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.0 + PDB: 无 | pLDDT=94.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Secreted / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 25 + 18 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CNDP1 -- Beta-Ala-His dipeptidase，研究基础较多，新颖性有限。
2. 蛋白大小507 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 104 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96KN2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000150656-CNDP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CNDP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96KN2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96KN2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
