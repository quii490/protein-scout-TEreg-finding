---
type: protein-evaluation
gene: "TTC21A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TTC21A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TTC21A / STI2 |
| 蛋白名称 | Tetratricopeptide repeat protein 21A |
| 蛋白大小 | 1320 aa / 150.9 kDa |
| UniProt ID | Q8NDW8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 5/10 | ×1 | 5 | 1320 aa / 150.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=15 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=81.2; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR056832, IPR056836, IPR056835, IPR056834, IPR056 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 12 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.5/180** | |
| **归一化总分** | | | **65.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cilium (GO:0005929)
- intraciliary transport particle A (GO:0030991)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed broad count | 17 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: STI2 |

**关键文献**:
1. The plasma peptides of sepsis.. *Clinical proteomics*. PMID: 32636717
2. Bi-allelic Mutations in TTC21A Induce Asthenoteratospermia in Humans and Mice.. *American journal of human genetics*. PMID: 30929735
3. High expression of TTC21A predicts unfavorable prognosis and immune infiltrates in clear cell renal cell carcinoma.. *Frontiers in genetics*. PMID: 36406111
4. Establishment and clinical significance of genetic factor screening method for patients with nonobstructive azoospermia based on whole exon sequencing technology.. *Translational andrology and urology*. PMID: 40376536
5. Identification of TTC21A as a Potential Prognostic Marker in Head and Neck Squamous Cell Carcinoma: In Silico Analysis.. *Cancer genomics & proteomics*. PMID: 38151293

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.2 |
| 高置信度残基 (pLDDT>90) 占比 | 3.0% |
| 置信残基 (pLDDT 70-90) 占比 | 86.9% |
| 中等置信 (pLDDT 50-70) 占比 | 7.8% |
| 低置信 (pLDDT<50) 占比 | 2.3% |
| 有序区域 (pLDDT>70) 占比 | 89.9% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=81.2，有序区 89.9%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR056832, IPR056836, IPR056835, IPR056834, IPR056833; Pfam: PF25058, PF25060, PF25068 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| WDR19 | 0.853 | 0.317 | — |
| IFT140 | 0.838 | 0.504 | — |
| WDR35 | 0.805 | 0.401 | — |
| IFT20 | 0.791 | 0.320 | — |
| IFT122 | 0.756 | 0.299 | — |
| CFAP43 | 0.741 | 0.000 | — |
| IFT74 | 0.738 | 0.061 | — |
| TTC29 | 0.732 | 0.000 | — |
| IFT81 | 0.724 | 0.000 | — |
| IFT52 | 0.706 | 0.292 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PDCD11 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| CEP76 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| STEAP3 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| DNAAF19 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| BBS7 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| MESD | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SKP1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| REL | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-23318|pubmed:25416956 |
| Insr | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:30300385|imex:IM-26942| |
| IFT140 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-27890|pubmed:30929735 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 12
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 12 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.2 + PDB: 无 | pLDDT=81.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 12 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TTC21A — Tetratricopeptide repeat protein 21A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1320 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 15 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NDW8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000168026-TTC21A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TTC21A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NDW8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
