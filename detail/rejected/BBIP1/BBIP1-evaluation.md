---
type: protein-evaluation
gene: "BBIP1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## BBIP1 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BBIP1 / BBIP10, NCRNA00081 |
| 蛋白名称 | BBSome-interacting protein 1 |
| 蛋白大小 | 92 aa / 10.5 kDa |
| UniProt ID | A8MTZ0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cell projection, cilium; Cytoplasm |
| 蛋白大小 | 5/10 | ×1 | 5 | 92 aa / 10.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=8 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=81.8; PDB: 6XT9 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR028233; Pfam: PF14777 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 9 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **114.0/180** | |
| **归一化总分** | | | **63.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无数据 |
| UniProt | Cell projection, cilium; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- BBSome (GO:0034464)
- ciliary membrane (GO:0060170)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8 |
| PubMed broad count | 12 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BBIP10, NCRNA00081 |

**关键文献**:
1. Bardet-Biedl Syndrome Overview.. **. PMID: 20301537
2. Direct Molecular Fishing of New Protein Partners for Human Thromboxane Synthase.. *Acta naturae*. PMID: 29340222
3. Temperature Incubation Influences Gonadal Gene Expression during Leopard Gecko Development.. *Animals : an open access journal from MDPI*. PMID: 36428413
4. Exome sequencing of Bardet-Biedl syndrome patient identifies a null mutation in the BBSome subunit BBIP1 (BBS18).. *Journal of medical genetics*. PMID: 24026985
5. Identification of marker genes and cell subtypes in castration-resistant prostate cancer cells.. *Journal of Cancer*. PMID: 33442423

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.8 |
| 高置信度残基 (pLDDT>90) 占比 | 55.4% |
| 置信残基 (pLDDT 70-90) 占比 | 14.1% |
| 中等置信 (pLDDT 50-70) 占比 | 28.3% |
| 低置信 (pLDDT<50) 占比 | 2.2% |
| 有序区域 (pLDDT>70) 占比 | 69.5% |
| 可用 PDB 条目 | 6XT9 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 高质量预测（pLDDT=81.8，有序区 69.5%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR028233; Pfam: PF14777 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BBS9 | 0.999 | 0.000 | — |
| BBS5 | 0.999 | 0.422 | — |
| BBS1 | 0.999 | 0.292 | — |
| BBS2 | 0.999 | 0.292 | — |
| BBS7 | 0.999 | 0.292 | — |
| BBS4 | 0.999 | 0.655 | — |
| TTC8 | 0.997 | 0.422 | — |
| RAB3IP | 0.949 | 0.000 | — |
| BBS10 | 0.892 | 0.000 | — |
| ARL6 | 0.840 | 0.191 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ARL6 | psi-mi:"MI:0416"(fluorescence microscopy) | imex:IM-14958|pubmed:20603001 |
| BBS4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:22500027|imex:IM-17327 |
| BBS1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:22500027|imex:IM-17327 |
| BBS7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:22500027|imex:IM-17327 |
| BBS2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:22500027|imex:IM-17327 |
| PCM1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:22500027|imex:IM-17327 |
| H1-4 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| BBS5 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| TTC8 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 9
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 9 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.8 + PDB: 6XT9 | pLDDT=81.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell projection, cilium; Cytoplasm / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 9 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. BBIP1 — BBSome-interacting protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小92 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A8MTZ0
- Protein Atlas: https://www.proteinatlas.org/search/BBIP1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BBIP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A8MTZ0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/BBIP1/BBIP1-PAE.png]]
