---
type: protein-evaluation
gene: "ACYP1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ACYP1 — REJECTED (核定位证据不足 (核定位得分 3/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ACYP1 / ACYPE |
| 蛋白名称 | Acylphosphatase-1 |
| 蛋白大小 | 99 aa / 11.3 kDa |
| UniProt ID | P07311 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 3/10 | ×4 | 12 | HPA: 暂无HPA定位数据; UniProt: 无注释 |
| 蛋白大小 | 5/10 | ×1 | 5 | 99 aa / 11.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=96.3; PDB: 2K7J, 2K7K, 2VH7, 2W4C, 2W4P, 3TOQ, 6CBU |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR020456, IPR001792, IPR036046, IPR017968; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 12 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **124.5/180** | |
| **归一化总分** | | | **69.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无数据 |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据不足，HPA与UniProt存在矛盾或缺乏核注释。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 19 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ACYPE |

**关键文献**:
1. Targeting ACYP1-mediated glycolysis reverses lenvatinib resistance and restricts hepatocellular carcinoma progression.. *Drug resistance updates : reviews and commentaries in antimicrobial and anticancer chemotherapy*. PMID: 37210811
2. High-Throughput Screening and Proteomic Characterization of Compounds Targeting Myeloid-Derived Suppressor Cells.. *Molecular & cellular proteomics : MCP*. PMID: 37586548
3. ACYP1 Is a Pancancer Prognostic Indicator and Affects the Immune Microenvironment in LIHC.. *Frontiers in oncology*. PMID: 35586489
4. Identification and prognostic value of metabolism-related genes in gastric cancer.. *Aging*. PMID: 32920549
5. Vaccination accelerates hepatic erythroblastosis induced by blood-stage malaria.. *Malaria journal*. PMID: 31996238

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 96.3 |
| 高置信度残基 (pLDDT>90) 占比 | 93.9% |
| 置信残基 (pLDDT 70-90) 占比 | 2.0% |
| 中等置信 (pLDDT 50-70) 占比 | 3.0% |
| 低置信 (pLDDT<50) 占比 | 1.0% |
| 有序区域 (pLDDT>70) 占比 | 95.9% |
| 可用 PDB 条目 | 2K7J, 2K7K, 2VH7, 2W4C, 2W4P, 3TOQ, 6CBU |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（2K7J, 2K7K, 2VH7, 2W4C, 2W4P, 3TOQ, 6CBU）+ AlphaFold极高置信度预测（pLDDT=96.3），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR020456, IPR001792, IPR036046, IPR017968; Pfam: PF00708 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ACOT12 | 0.923 | 0.000 | — |
| ALDH9A1 | 0.910 | 0.000 | — |
| ACYP2 | 0.909 | 0.000 | — |
| ALDH1B1 | 0.909 | 0.000 | — |
| ALDH3A2 | 0.908 | 0.000 | — |
| ACSS2 | 0.908 | 0.000 | — |
| ALDH7A1 | 0.905 | 0.000 | — |
| ACSS1 | 0.904 | 0.000 | — |
| ALDH2 | 0.900 | 0.000 | — |
| NDUFAB1 | 0.681 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ERBB3 | psi-mi:"MI:0112"(ubiquitin reconstruction) | pubmed:31980649|imex:IM-26434 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 12，IntAct interactions: 1
- 调控相关比例: 0 / 12 = 0%

**评价**: STRING 12 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=96.3 + PDB: 2K7J, 2K7K, 2VH7, 2W4C, 2W4P,  | pLDDT=96.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 12 + 1 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. ACYP1 — Acylphosphatase-1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小99 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P07311
- Protein Atlas: https://www.proteinatlas.org/search/ACYP1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ACYP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P07311
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/ACYP1/ACYP1-PAE.png]]
