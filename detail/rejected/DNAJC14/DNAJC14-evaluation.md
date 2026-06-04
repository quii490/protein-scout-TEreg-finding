---
type: protein-evaluation
gene: "DNAJC14"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DNAJC14 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DNAJC14 |
| 蛋白名称 | DnaJ homolog subfamily C member 14 |
| 蛋白大小 | 702 aa / 78.6 kDa |
| UniProt ID | Q6Y2X3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Endoplasmic reticulum membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 702 aa / 78.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=18 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.7; PDB: 无 |
| 调控结构域 | 5/10 | ×2 | 10 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 13 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **105.5/180** | |
| **归一化总分** | | | **58.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | No data |
| UniProt | Endoplasmic reticulum membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 18 |
| PubMed broad count | 29 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Molecular mechanisms of NS2(pro) activation in hepaciviruses and pestiviruses: regulation, intrinsic activity, and structural determinants.. *Curr Opin Virol*. PMID: 42143427
2. Transcriptome Analysis Reveals the Mechanism by which Probiotic Alleviate the Response of Juvenile American Shad (Alosa sapidissima) to High Temperatures.. *Probiotics Antimicrob Proteins*. PMID: 40782190
3. DNAJC14 gene-edited pigs are resistant to classical pestiviruses.. *Trends Biotechnol*. PMID: 41130838
4. Characterization of the First Marine Pestivirus, Phocoena Pestivirus (PhoPeV).. *Viruses*. PMID: 39861896
5. Fathers' preconception smoking and offspring DNA methylation.. *Clin Epigenetics*. PMID: 37649101

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.7 |
| 高置信度残基 (pLDDT>90) 占比 | 17.7% |
| 置信残基 (pLDDT 70-90) 占比 | 18.2% |
| 中等置信 (pLDDT 50-70) 占比 | 16.7% |
| 低置信 (pLDDT<50) 占比 | 47.4% |
| 有序区域 (pLDDT>70) 占比 | 35.9% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/DNAJC14/DNAJC14-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=59.7），有序残基占 35.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DRD1 | 0.000 | 0.000 | — |
| SARNP | 0.000 | 0.000 | — |
| CANX | 0.000 | 0.000 | — |
| HSPA5 | 0.000 | 0.000 | — |
| IGSF8 | 0.000 | 0.000 | — |
| TMUB2 | 0.000 | 0.000 | — |
| CHRM2 | 0.000 | 0.000 | — |
| PDCL | 0.000 | 0.000 | — |
| DNAJC28 | 0.000 | 0.000 | — |
| TLK2 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:P82979 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:- |
| uniprotkb:Q6Y2X3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q8XA11 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q96EB6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| intact:EBI-54267945 | psi-mi:"MI:2195"(clash) | pubmed:- |
| intact:EBI-54262435 | psi-mi:"MI:2195"(clash) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 13
- 调控相关比例: 2 / 20 = 10%

**评价**: STRING 25 个预测互作，IntAct 13 个实验互作。调控相关配体占比 10%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.7 + PDB: 无 | pLDDT=59.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 25 + 13 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. DNAJC14 — DnaJ homolog subfamily C member 14，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小702 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 18 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=59.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6Y2X3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000135392-DNAJC14/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DNAJC14
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6Y2X3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/DNAJC14/DNAJC14-PAE.png]]
