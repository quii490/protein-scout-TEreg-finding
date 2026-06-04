---
type: protein-evaluation
gene: "ACYP2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ACYP2 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ACYP2 / ACYP |
| 蛋白名称 | Acylphosphatase-2 |
| 蛋白大小 | 99 aa / 11.1 kDa |
| UniProt ID | P14621 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: 无注释 |
| 蛋白大小 | 5/10 | ×1 | 5 | 99 aa / 11.1 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=39 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=95.7; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR020456, IPR001792, IPR036046, IPR017968; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 8 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **103.0/180** | |
| **归一化总分** | | | **57.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无数据 |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- mitochondrion (GO:0005739)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 39 |
| PubMed broad count | 72 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ACYP |

**关键文献**:
1. Associations between polymorphisms of the ACYP2 gene and Liver cancer risk: A case-control study and meta-analysis.. *Molecular genetics & genomic medicine*. PMID: 31124313
2. ACPY2 gene polymorphisms on cancer risk: a systematic review and meta-analysis.. *Nucleosides, nucleotides & nucleic acids*. PMID: 35797106
3. The influence of ACYP2 polymorphisms on gastrointestinal cancer susceptibility in the Chinese Han population.. *Molecular genetics & genomic medicine*. PMID: 31070019
4. The influence of TERC, TERT and ACYP2 genes polymorphisms on plasma telomerase concentration, telomeres length and T2DM.. *Gene*. PMID: 32937184
5. Association between ACYP2 polymorphisms and the risk of renal cell cancer.. *Molecular genetics & genomic medicine*. PMID: 31487124

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 95.7 |
| 高置信度残基 (pLDDT>90) 占比 | 93.9% |
| 置信残基 (pLDDT 70-90) 占比 | 2.0% |
| 中等置信 (pLDDT 50-70) 占比 | 3.0% |
| 低置信 (pLDDT<50) 占比 | 1.0% |
| 有序区域 (pLDDT>70) 占比 | 95.9% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=95.7，有序区 95.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR020456, IPR001792, IPR036046, IPR017968; Pfam: PF00708 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ALDH1B1 | 0.915 | 0.000 | — |
| ACOT12 | 0.911 | 0.000 | — |
| ALDH9A1 | 0.910 | 0.000 | — |
| ACSS2 | 0.910 | 0.000 | — |
| ACYP1 | 0.909 | 0.000 | — |
| ALDH2 | 0.906 | 0.000 | — |
| ALDH3A2 | 0.906 | 0.000 | — |
| ALDH7A1 | 0.905 | 0.000 | — |
| ACSS1 | 0.902 | 0.000 | — |
| ZNF208 | 0.782 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000378161.3 | psi-mi:"MI:0017"(classical fluorescence spectrosco | pubmed:12374855|imex:IM-27412 |
| infB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| SULT2B1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-23318|pubmed:25416956 |
| CREBZF | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-23318|pubmed:25416956 |
| OGA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| GFPT2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CARM1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| BCS1L | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 8
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 8 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=95.7 + PDB: 无 | pLDDT=95.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 15 + 8 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. ACYP2 — Acylphosphatase-2，非常新颖，仅有少数基础研究。
2. 蛋白大小99 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 39 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P14621
- Protein Atlas: https://www.proteinatlas.org/search/ACYP2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ACYP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P14621
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/ACYP2/ACYP2-PAE.png]]
