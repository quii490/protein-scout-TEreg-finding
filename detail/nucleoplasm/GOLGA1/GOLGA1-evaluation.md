---
type: protein-evaluation
gene: "GOLGA1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GOLGA1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GOLGA1 |
| 蛋白名称 | Golgin subfamily A member 1 |
| 蛋白大小 | 767 aa / 88.2 kDa |
| UniProt ID | Q92805 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Golgi apparatus; UniProt: Golgi apparatus membrane; Golgi apparatus, trans-Golgi netwo |
| 蛋白大小 | 10/10 | ×1 | 10 | 767 aa / 88.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=78.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR051952, IPR000237; Pfam: PF01465 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.5/180** | |
| **归一化总分** | | | **67.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus | Enhanced |
| UniProt | Golgi apparatus membrane; Golgi apparatus, trans-Golgi network membrane; Cytoplasmic vesicle, secret... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- acrosomal vesicle (GO:0001669)
- cytosol (GO:0005829)
- Golgi apparatus (GO:0005794)
- Golgi membrane (GO:0000139)
- perinuclear region of cytoplasm (GO:0048471)
- trans-Golgi network (GO:0005802)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

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
| AlphaFold 平均 pLDDT | 78.2 |
| 高置信度残基 (pLDDT>90) 占比 | 53.7% |
| 置信残基 (pLDDT 70-90) 占比 | 20.9% |
| 中等置信 (pLDDT 50-70) 占比 | 5.6% |
| 低置信 (pLDDT<50) 占比 | 19.8% |
| 有序区域 (pLDDT>70) 占比 | 74.6% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=78.2，有序区 74.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051952, IPR000237; Pfam: PF01465 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GOLGA4 | 0.921 | 0.097 | — |
| RAB6A | 0.895 | 0.256 | — |
| GCC1 | 0.868 | 0.128 | — |
| TGOLN2 | 0.861 | 0.079 | — |
| GCC2 | 0.860 | 0.084 | — |
| GOLGB1 | 0.803 | 0.125 | — |
| VTI1A | 0.792 | 0.091 | — |
| ARL1 | 0.781 | 0.331 | — |
| GOLGA2 | 0.762 | 0.052 | — |
| STX6 | 0.757 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ORF | psi-mi:"MI:0096"(pull down) | imex:IM-17346|pubmed:22190034| |
| Cenpf | psi-mi:"MI:0051"(fluorescence technology) | pubmed:18827011|imex:IM-20258 |
| ATF4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| KRT27 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TFIP11 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| EFHC2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PPP1R13B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ENSP00000362656.4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| UBE2I | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| LZTS1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.2 + PDB: 无 | pLDDT=78.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus membrane; Golgi apparatus, trans-G / Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. GOLGA1 — Golgin subfamily A member 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小767 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q92805
- Protein Atlas: https://www.proteinatlas.org/ENSG00000136935-GOLGA1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GOLGA1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q92805
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
