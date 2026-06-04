---
type: protein-evaluation
gene: "Tnni3k"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## Tnni3k 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | Tnni3k / CARK |
| 蛋白名称 | Serine/threonine-protein kinase TNNI3K |
| 蛋白大小 | 835 aa / 92.9 kDa |
| UniProt ID | Q59H18 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 835 aa / 92.9 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=65 篇 (≤80→4) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=79.6; PDB: 4YFF, 4YFI, 6B5J, 7MGJ, 7MGK |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR002110, IPR036770, IPR011009, IPR000719, IPR017 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **112.0/180** | |
| **归一化总分** | | | **62.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 65 |
| PubMed broad count | 122 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CARK |

**关键文献**:
1. The Diverse Roles of TNNI3K in Cardiac Disease and Potential for Treatment.. *International journal of molecular sciences*. PMID: 34203974
2. TNNI3K could be a novel molecular target for the treatment of cardiac diseases.. *Recent patents on cardiovascular drug discovery*. PMID: 19925440
3. Knockout of cardiac troponin I-interacting kinase leads to cardiac dysfunction and remodelling.. *Clinical and experimental pharmacology & physiology*. PMID: 35781726
4. TNNI3K in cardiovascular disease and prospects for therapy.. *Journal of molecular and cellular cardiology*. PMID: 25787061
5. Adenovirus-mediated overexpression of cardiac troponin I-interacting kinase promotes cardiomyocyte hypertrophy.. *Clinical and experimental pharmacology & physiology*. PMID: 21314842

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.6 |
| 高置信度残基 (pLDDT>90) 占比 | 52.1% |
| 置信残基 (pLDDT 70-90) 占比 | 23.7% |
| 中等置信 (pLDDT 50-70) 占比 | 6.2% |
| 低置信 (pLDDT<50) 占比 | 18.0% |
| 有序区域 (pLDDT>70) 占比 | 75.8% |
| 可用 PDB 条目 | 4YFF, 4YFI, 6B5J, 7MGJ, 7MGK |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（4YFF, 4YFI, 6B5J, 7MGJ, 7MGK）+ AlphaFold极高置信度预测（pLDDT=79.6），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002110, IPR036770, IPR011009, IPR000719, IPR017441; Pfam: PF12796, PF07714 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TNNI3 | 0.986 | 0.516 | — |
| FPGT-TNNI3K | 0.902 | 0.900 | — |
| FPGT | 0.804 | 0.000 | — |
| SEC16B | 0.718 | 0.091 | — |
| GNPDA2 | 0.663 | 0.049 | — |
| TMEM18 | 0.660 | 0.000 | — |
| LRRIQ3 | 0.657 | 0.100 | — |
| ASB3 | 0.638 | 0.614 | — |
| QPCTL | 0.619 | 0.000 | — |
| DNAJC27 | 0.617 | 0.110 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TNNI3 | psi-mi:"MI:0018"(two hybrid) | pubmed:12721663 |
| ACTC1 | psi-mi:"MI:0018"(two hybrid) | pubmed:12721663 |
| ACTA1 | psi-mi:"MI:0018"(two hybrid) | pubmed:12721663 |
| MYBPC3 | psi-mi:"MI:0018"(two hybrid) | pubmed:12721663 |
| AIP | psi-mi:"MI:0018"(two hybrid) | pubmed:12721663 |
| FABP3 | psi-mi:"MI:0018"(two hybrid) | pubmed:12721663 |
| HADHB | psi-mi:"MI:0018"(two hybrid) | pubmed:12721663 |
| ENSP00000322251.3 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:12721663 |
| FBXO4 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| HSP90AB1 | psi-mi:"MI:0729"(luminescence based mammalian inte | imex:IM-17906|pubmed:22939624| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.6 + PDB: 4YFF, 4YFI, 6B5J, 7MGJ, 7MGK | pLDDT=79.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. Tnni3k — Serine/threonine-protein kinase TNNI3K，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小835 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 65 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q59H18
- Protein Atlas: https://www.proteinatlas.org/ENSG00000116783-TNNI3K/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=Tnni3k
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q59H18
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
