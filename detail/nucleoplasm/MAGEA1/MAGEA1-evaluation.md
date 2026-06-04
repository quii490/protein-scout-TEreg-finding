---
type: protein-evaluation
gene: "MAGEA1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## MAGEA1 — REJECTED (研究热度过高 (PubMed strict=175，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MAGEA1 / MAGE1, MAGE1A |
| 蛋白名称 | Melanoma-associated antigen 1 |
| 蛋白大小 | 309 aa / 34.3 kDa |
| UniProt ID | P43355 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 309 aa / 34.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=175 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=74.7; PDB: 1W72, 3BO8 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR037445, IPR021072, IPR041898, IPR041899, IPR002 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **90.0/180** | |
| **归一化总分** | | | **50.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 175 |
| PubMed broad count | 601 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MAGE1, MAGE1A |

**关键文献**:
1. MLLT3 Regulates Melanoma Stemness and Progression by Inhibiting HMGB1 Nuclear Entry and MAGEA1 M(5)C Modification.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 39716999
2. MAGEA1 inhibits the expression of BORIS via increased promoter methylation.. *Journal of cell science*. PMID: 30498011
3. MAGEA1 interacts with FBXW7 and regulates ubiquitin ligase-mediated turnover of NICD1 in breast and ovarian cancer cells.. *Oncogene*. PMID: 28459460
4. The melanoma-associated antigen 1 (MAGEA1) protein stimulates the E3 ubiquitin-ligase activity of TRIM31 within a TRIM31-MAGEA1-NSE4 complex.. *Cell cycle (Georgetown, Tex.)*. PMID: 25590999
5. Cancer-testis antigen expression in synovial sarcoma: NY-ESO-1, PRAME, MAGEA4, and MAGEA1.. *Human pathology*. PMID: 27993576

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.7 |
| 高置信度残基 (pLDDT>90) 占比 | 51.8% |
| 置信残基 (pLDDT 70-90) 占比 | 14.9% |
| 中等置信 (pLDDT 50-70) 占比 | 5.2% |
| 低置信 (pLDDT<50) 占比 | 28.2% |
| 有序区域 (pLDDT>70) 占比 | 66.7% |
| 可用 PDB 条目 | 1W72, 3BO8 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1W72, 3BO8）+ AlphaFold高质量预测（pLDDT=74.7），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR037445, IPR021072, IPR041898, IPR041899, IPR002190; Pfam: PF01454, PF12440 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GAGE1 | 0.966 | 0.000 | — |
| GAGE12F | 0.958 | 0.000 | — |
| GAGE2A | 0.942 | 0.000 | — |
| CTAG1B | 0.910 | 0.000 | — |
| HSPA4 | 0.891 | 0.052 | — |
| DDX43 | 0.882 | 0.065 | — |
| TRIM31 | 0.878 | 0.626 | — |
| SNW1 | 0.847 | 0.510 | — |
| CTAG2 | 0.845 | 0.000 | — |
| CSAG1 | 0.820 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SH3GLB2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| UQCRB | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MIEF1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TRIM31 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| SGK1 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-11703|pubmed:20368287 |
| ANKHD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| VMA1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:27107014|imex:IM-24995 |
| CCP1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:27107014|imex:IM-24995 |
| PRP45 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:27107014|imex:IM-24995 |
| - | psi-mi:"MI:1356"(validated two hybrid) | pubmed:27107014|imex:IM-24995 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.7 + PDB: 1W72, 3BO8 | pLDDT=74.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. MAGEA1 — Melanoma-associated antigen 1，研究基础较多，新颖性有限。
2. 蛋白大小309 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 175 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 175 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P43355
- Protein Atlas: https://www.proteinatlas.org/ENSG00000198681-MAGEA1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MAGEA1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P43355
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
