---
type: protein-evaluation
gene: "CDC14A"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CDC14A 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CDC14A / Dual specificity protein phosphatase CDC14A |
| 蛋白大小 | 594 aa / 66.6 kDa |
| UniProt ID | Q9UNH5 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 4/10 | ×4 | 16 | Nucleus; Cytoplasm, cytoskeleton, microtubule organizing cen... |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 594 aa / 66.6 kDa |
| 🆕 研究新颖性 | 2/10 | ×5 | 30 | PubMed 84 篇 |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=72.5，PDB: 无 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR044506 - CDC14_C; InterPro: IPR029260 - DSPn; I |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 20 partners, IntAct 16 interactions |
| ➕ 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
|  | **原始总分** |  | **83/183** | **80.0/183** |  |  |  |
|  | **归一化总分** |  | **45.4/100** | **43.7/100** |  |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| UniProt | Nucleus; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Cyt... | Swiss-Prot/TrEMBL |
| Protein Atlas (IF) | Nuclear speckles | Approved |

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CDC14A/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CDC14A/IF_images/A-431_2.jpg|A-431]]

**结论**: 核定位信号较弱，HPA Approved。

#### 3.2 蛋白大小评估

**评价**: 大小适中，适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 84 |
| 研究方向 | 待补充关键文献摘要 |

**评价**: 有一定研究基础，但仍存在未探索的niche空间。

**关键文献**:
1. Wen Z et al. (2020). "Cdc14a has a role in spermatogenesis, sperm maturation and male fertility". *Exp Cell Res*. PMID: 32679235
2. Wang M et al. (2025). "Multi-omics derivation of a core gene signature for predicting therapeutic response and characterizing immune dysregulation in inflammatory bowel disease". *Front Immunol*. PMID: 40821793
3. Mailand N et al. (2002). "Deregulated human Cdc14A phosphatase disrupts centrosome separation and chromosome segregation". *Nat Cell Biol*. PMID: 11901424
4. Imtiaz A et al. (2018). "CDC14A phosphatase is essential for hearing and male fertility in mouse and human". *Hum Mol Genet*. PMID: 29293958
5. Connell GJ et al. (2023). "A temporal difference in the stabilization of two mRNAs with a 3' iron-responsive element during iron deficiency". *RNA*. PMID: 37160355
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.5 |
| 高置信度残基 (pLDDT>90) 占比 | 53.2% |
| 置信残基 (pLDDT 70-90) 占比 | 5.9% |
| 有序区域 (pLDDT>70) 占比 | 59.1% |
| 可用 PDB 条目 | 无 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CDC14A/CDC14A-PAE.png]]

**评价**: AlphaFold 中等质量（pLDDT=72.5，有序区 59.1%）。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR044506 - CDC14_C; InterPro: IPR029260 - DSPn; InterPro: IPR029021 - Prot-tyrosine_phosphatase-like; InterPr |

**染色质调控潜力分析**: 存在注释结构域：InterPro: IPR044506 - CDC14_C; InterPro: IPR029260 - DSPn; I...。新颖蛋白基线不扣分。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| SIRT1 | 0.992 | — | — |
| SIRT2 | 0.991 | — | — |
| ESPL1 | 0.947 | — | — |
| FZR1 | 0.928 | — | — |
| CDK1 | 0.914 | — | — |
| CDC14B | 0.905 | — | — |
| INCENP | 0.847 | — | — |
| WEE1 | 0.842 | — | — |
| CDC16 | 0.838 | — | — |
| CDC7 | 0.832 | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| intact:EBI-2514978|uniprotkb:Q9Y3Q5|uniprotkb:O95811|uniprotkb:Q15752|ensembl:ENSP00000356234.3 | — | — | — | — |
| intact:EBI-7851002|uniprotkb:B1AQ15|uniprotkb:A6MA65|uniprotkb:O43171|uniprotkb:Q52LH9|uniprotkb:B1AQ14|uniprotkb:O60728|intact:MINT-8330048|uniprotkb:Q8IXX0|uniprotkb:O60727|intact:EBI-17281556|intact:EBI-23863446|ensembl:ENSP00000336739.3 | — | — | — | — |
| intact:EBI-1166928|uniprotkb:A6NDE5|uniprotkb:A8K2J2|uniprotkb:Q6XYC7|ensembl:ENSP00000417190.2 | — | — | — | — |
| intact:EBI-725606|uniprotkb:Q6IAA7|ensembl:ENSP00000322238.4|ensembl:ENSP00000450861.1 | — | — | — | — |
| intact:EBI-359832|uniprotkb:O70457|uniprotkb:P35214|uniprotkb:Q6FH52|uniprotkb:Q9UDP2|uniprotkb:Q9UN99|ensembl:ENSP00000306330.3 | — | — | — | — |

**已知复合体成员** (GO Cellular Component):
- 无 GO-CC 注释

**PPI 互证分析**:
- STRING + IntAct 共同确认: 0
- 仅 STRING 预测: 20
- 仅 IntAct 实验: 16
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 20 个预测互作，IntAct 16 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.5 + PDB: 无 | pLDDT=72.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, cytoskeleton, microtubule orga | 一致 |
| PPI | STRING + IntAct | 20 + 16 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CDC14A — Dual specificity protein phosphatase CDC14A，有一定研究基础，但仍存在未探索的niche空间。
2. 蛋白大小594 aa，大小适中，适合常规生化实验和结构解析。

**风险/不确定性**:
1. 已有一定研究，需确认独特研究角度
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新 5 篇关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外 DNA/染色质结合实验

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UNH5
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CDC14A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/CDC14A


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[CDC14A-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CDC14A/CDC14A-PAE.png]]




