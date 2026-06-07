---
type: protein-evaluation
gene: "CDAN1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CDAN1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CDAN1 / Codanin-1 |
| 蛋白大小 | 1227 aa / 134.1 kDa |
| UniProt ID | Q8IWY9 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 4/10 | ×4 | 16 | Cytoplasm; Nucleus; Membrane |
| 📏 蛋白大小 | 5/10 | ×1 | 5 | 1227 aa / 134.1 kDa |
| 🆕 研究新颖性 | 6/10 | ×5 | 30 | PubMed 56 篇 |
| 🏗️ 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=71.4，PDB: 9CVC, 9IMZ |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR040031 - Codanin-1; InterPro: IPR028171 - Codan |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 20 partners, IntAct 14 interactions |
| ➕ 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** |  |  | **104/183** |  |
| **归一化总分** |  |  | **56.8/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| UniProt | Cytoplasm; Nucleus; Membrane | Swiss-Prot/TrEMBL |
| Protein Atlas (IF) | Nuclear speckles; Nucleoplasm | Approved |

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CDAN1/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CDAN1/IF_images/A-431_2.jpg|A-431]]

**结论**: 核定位信号较弱，HPA Approved。

#### 3.2 蛋白大小评估

**评价**: 大小偏大/偏小，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 56 |
| 研究方向 | 待补充关键文献摘要 |

**评价**: 有一定研究基础，但仍存在未探索的niche空间。

**关键文献**:
1. Colin E et al. (2025). "MMS22L is a novel key actor of normal and pathological erythropoiesis". *Hemasphere*. PMID: 41446536
2. Sedor SF & Shao S (2025). "Mechanism of ASF1 engagement by CDAN1". *Nat Commun*. PMID: 40091041
3. Sedor SF & Shao S (2024). "Mechanism of ASF1 Inhibition by CDAN1". *bioRxiv*. PMID: 39149339
4. Noy-Lotan S et al. (2021). "Cdan1 Is Essential for Primitive Erythropoiesis". *Front Physiol*. PMID: 34234691
5. King R et al. (2022). "The congenital dyserythropoieitic anemias: genetics and pathophysiology". *Curr Opin Hematol*. PMID: 35441598
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.4 |
| 高置信度残基 (pLDDT>90) 占比 | 31.5% |
| 置信残基 (pLDDT 70-90) 占比 | 32.5% |
| 有序区域 (pLDDT>70) 占比 | 64.0% |
| 可用 PDB 条目 | 9CVC, 9IMZ |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CDAN1/CDAN1-PAE.png]]

**评价**: PDB 实验结构（9CVC, 9IMZ）+ AlphaFold 高质量预测（pLDDT=71.4），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR040031 - Codanin-1; InterPro: IPR028171 - Codanin-1_C; Pfam: PF15296 - Codanin-1_C |

**染色质调控潜力分析**: 存在注释结构域：InterPro: IPR040031 - Codanin-1; InterPro: IPR028171 - Codan...。新颖蛋白基线不扣分。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| SEC23B | 0.944 | — | — |
| C15orf41 | 0.923 | — | — |
| ASF1A | 0.897 | — | — |
| ASF1B | 0.89 | — | — |
| STRC | 0.811 | — | — |
| CATSPER2 | 0.801 | — | — |
| AARS2 | 0.782 | — | — |
| PRDM15 | 0.781 | — | — |
| IPO4 | 0.767 | — | — |
| KLF1 | 0.742 | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| intact:EBI-717097|uniprotkb:Q8IV52|uniprotkb:Q9BRD5|uniprotkb:Q6FI20|uniprotkb:H0Y4Z0|uniprotkb:Q59EH6|intact:EBI-28968232|ensembl:ENSP00000344220.4 | — | — | — | — |
| intact:EBI-1055650|uniprotkb:Q53G51|uniprotkb:Q9NVZ0|ensembl:ENSP00000263382.3|ensembl:ENSP00000499863.1 | — | — | — | — |
| intact:EBI-749553|uniprotkb:Q6IA08|uniprotkb:Q9P014|ensembl:ENSP00000229595.5 | — | — | — | — |
| intact:EBI-21829186 | — | — | — | — |
| intact:EBI-8456413|uniprotkb:Q96BM4|uniprotkb:Q5VW47|uniprotkb:Q8WX43|intact:MINT-4722654|ensembl:ENSP00000366387.4 | — | — | — | — |

**已知复合体成员** (GO Cellular Component):
- 无 GO-CC 注释

**PPI 互证分析**:
- STRING + IntAct 共同确认: 0
- 仅 STRING 预测: 20
- 仅 IntAct 实验: 14
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 20 个预测互作，IntAct 14 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.4 + PDB: 9CVC, 9IMZ | pLDDT=71.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Membrane | 一致 |
| PPI | STRING + IntAct | 20 + 14 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致: +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CDAN1 — Codanin-1，有一定研究基础，但仍存在未探索的niche空间。
2. 蛋白大小1227 aa，大小偏大/偏小，实验操作有一定难度。

**风险/不确定性**:
1. 已有一定研究，需确认独特研究角度
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新 5 篇关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外 DNA/染色质结合实验

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IWY9
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CDAN1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/CDAN1


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[CDAN1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CDAN1/CDAN1-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8IWY9 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR040031;IPR028171; |
| Pfam | PF15296; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000140326-CDAN1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ASF1A | Biogrid, Bioplex | true |
| ASF1B | Intact, Biogrid, Bioplex | true |
| H3C1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
