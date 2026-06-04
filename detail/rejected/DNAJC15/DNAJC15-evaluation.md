---
type: protein-evaluation
gene: "DNAJC15"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DNAJC15 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DNAJC15 |
| 蛋白名称 | DnaJ homolog subfamily C member 15 |
| 蛋白大小 | 150 aa / 16.4 kDa |
| UniProt ID | Q9Y5T4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Mitochondrion inner membrane |
| 蛋白大小 | 8/10 | ×1 | 8 | 150 aa / 16.4 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=32 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=78.9; PDB: 无 |
| 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 22 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **99.0/180** | |
| **归一化总分** | | | **55.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | No data |
| UniProt | Mitochondrion inner membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 32 |
| PubMed broad count | 39 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Modulation of the immunogenic landscape in colorectal cancer by mitochondrial methylation-controlled J protein.. *Mol Biomed*. PMID: 42113076
2. Stress adaptation of mitochondrial protein import by OMA1-mediated degradation of DNAJC15.. *Nat Struct Mol Biol*. PMID: 41760807
3. Identification of marker genes associated with oxidative stress in hypertrophic cardiomyopathy using bioinformatics analysis and experimental validation.. *Sci Rep*. PMID: 40770404
4. Quantitative Proteome and Phosphoproteome Profiling across Three Cell Lines Revealed Potential Proteins Relevant to Nasopharyngeal Carcinoma Metastasis.. *J Proteome Res*. PMID: 39970938
5. Absence of MCJ/DnaJC15 promotes brown adipose tissue thermogenesis.. *Nat Commun*. PMID: 39805849

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.9 |
| 高置信度残基 (pLDDT>90) 占比 | 49.3% |
| 置信残基 (pLDDT 70-90) 占比 | 14.0% |
| 中等置信 (pLDDT 50-70) 占比 | 27.3% |
| 低置信 (pLDDT<50) 占比 | 9.3% |
| 有序区域 (pLDDT>70) 占比 | 63.3% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/DNAJC15/DNAJC15-PAE.png]]

**评价**: AlphaFold 中等质量（pLDDT=78.9，有序区 63.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PAM16 | 0.000 | 0.000 | — |
| TIMM44 | 0.000 | 0.000 | — |
| HSPA9 | 0.000 | 0.000 | — |
| TIMM17A | 0.000 | 0.000 | — |
| TIMM17B | 0.000 | 0.000 | — |
| GRPEL1 | 0.000 | 0.000 | — |
| TIMM23 | 0.000 | 0.000 | — |
| TIMM21 | 0.000 | 0.000 | — |
| TIMM50 | 0.000 | 0.000 | — |
| DNAJC19 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q9Y5T4 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:O60830 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q99595 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9Y3D7 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q8IUQ4 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:Q8IZU0 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:O14556 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 22
- 调控相关比例: 1 / 20 = 5%

**评价**: STRING 25 个预测互作，IntAct 22 个实验互作。调控相关配体占比 5%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.9 + PDB: 无 | pLDDT=78.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Mitochondrion inner membrane / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 25 + 22 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. DNAJC15 — DnaJ homolog subfamily C member 15，非常新颖，仅有少数基础研究。
2. 蛋白大小150 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 32 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y5T4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000120675-DNAJC15/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DNAJC15
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y5T4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/DNAJC15/DNAJC15-PAE.png]]
