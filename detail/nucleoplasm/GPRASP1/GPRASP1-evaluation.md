---
type: protein-evaluation
gene: "GPRASP1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GPRASP1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPRASP1 / GASP, KIAA0443 |
| 蛋白名称 | G-protein coupled receptor-associated sorting protein 1 |
| 蛋白大小 | 1395 aa / 156.9 kDa |
| UniProt ID | Q5JY77 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Cytosol; UniProt: Cytoplasm |
| 蛋白大小 | 5/10 | ×1 | 5 | 1395 aa / 156.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=41.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011989, IPR006911, IPR016024, IPR043374; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.0/180** | |
| **归一化总分** | | | **62.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Supported |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleus (GO:0005634)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 0 |
| 别名(未计入scoring) | 无 |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 41.6 |
| 高置信度残基 (pLDDT>90) 占比 | 5.4% |
| 置信残基 (pLDDT 70-90) 占比 | 10.0% |
| 中等置信 (pLDDT 50-70) 占比 | 3.5% |
| 低置信 (pLDDT<50) 占比 | 81.1% |
| 有序区域 (pLDDT>70) 占比 | 15.4% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=41.6），有序残基占 15.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011989, IPR006911, IPR016024, IPR043374; Pfam: PF04826 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| OPRD1 | 0.838 | 0.512 | — |
| OPRM1 | 0.778 | 0.294 | — |
| ADRB2 | 0.762 | 0.045 | — |
| AVPR2 | 0.655 | 0.045 | — |
| BECN2 | 0.607 | 0.300 | — |
| DRD4 | 0.568 | 0.045 | — |
| GSTM1 | 0.550 | 0.045 | — |
| BDKRB1 | 0.540 | 0.045 | — |
| RGS3 | 0.538 | 0.110 | — |
| BEX1 | 0.517 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MARK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| OPRD1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15086532|imex:IM-20433 |
| OPRK1 | psi-mi:"MI:0096"(pull down) | pubmed:15086532|imex:IM-20433 |
| OPRM1 | psi-mi:"MI:0096"(pull down) | pubmed:15086532|imex:IM-20433 |
| CHRM1 | psi-mi:"MI:0096"(pull down) | pubmed:15086532|imex:IM-20433 |
| OPRL1 | psi-mi:"MI:0096"(pull down) | pubmed:15086532|imex:IM-20433 |
| CHRM2 | psi-mi:"MI:0096"(pull down) | pubmed:15086532|imex:IM-20433 |
| HTR7 | psi-mi:"MI:0096"(pull down) | pubmed:15086532|imex:IM-20433 |
| Hrh2 | psi-mi:"MI:0096"(pull down) | pubmed:15086532|imex:IM-20433 |
| TBXA2R | psi-mi:"MI:0096"(pull down) | pubmed:15086532|imex:IM-20433 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=41.6 + PDB: 无 | pLDDT=41.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. GPRASP1 — G-protein coupled receptor-associated sorting protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1395 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=41.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5JY77
- Protein Atlas: https://www.proteinatlas.org/ENSG00000198932-GPRASP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPRASP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5JY77
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
