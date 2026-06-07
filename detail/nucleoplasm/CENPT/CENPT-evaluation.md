---
type: protein-evaluation
gene: "CENPT"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CENPT 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CENPT / Centromere protein T |
| 蛋白大小 | 561 aa / 60.4 kDa |
| UniProt ID | Q96BT3 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CENPT/IF_images/HEK293_1.jpg|HEK293]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CENPT/IF_images/MCF-7_1.jpg|MCF-7]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 9/10 | ×4 | 36 | Nucleus; Chromosome, centromere; Chromosome, centromere, kin... |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 561 aa / 60.4 kDa |
| 🆕 研究新颖性 | 4/10 | ×5 | 30 | PubMed 71 篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=56.1，PDB: 7QOO, 7R5S, 7XHN, 7XHO, 7YWX |
| 🧬 调控结构域 | 10/10 | ×2 | 20 | InterPro: IPR028255 - CENP-T; InterPro: IPR035425 - CENP-T/H |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 20 partners, IntAct 31 interactions |
| ➕ 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
|  | **原始总分** |  | **116/183** | **113.0/183** |  |  |  |
|  | **归一化总分** |  | **63.4/100** | **61.7/100** |  |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| UniProt | Nucleus; Chromosome, centromere; Chromosome, centromere, kinetochore | Swiss-Prot/TrEMBL |
| Protein Atlas (IF) | 暂无数据 | 暂无 HPA IF 数据 |

暂无数据（HPA IF 图像已本地嵌入。


**结论**: 主要定位于细胞核，HPA 暂无 HPA IF 数据。

#### 3.2 蛋白大小评估

**评价**: 大小适中，适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 71 |
| 研究方向 | 待补充关键文献摘要 |

**评价**: 有一定研究基础，但仍存在未探索的niche空间。

**关键文献**:
1. Yang H et al. (2025). "CENPT prevents renal cell carcinoma against ferroptosis by enhancing the synthesis of glutathione". *Cell Death Dis*. PMID: 40651948
2. Perpelescu M & Fukagawa T (2011). "The ABCs of CENPs". *Chromosoma*. PMID: 21751032
3. Dudka D et al. (2025). "Adaptive evolution of CENP-T modulates centromere binding". *Curr Biol*. PMID: 39947176
4. Ariyoshi M & Fukagawa T (2023). "An updated view of the kinetochore architecture". *Trends Genet*. PMID: 37775394
5. Sissoko GB et al. (2024). "Higher-order protein assembly controls kinetochore formation". *Nat Cell Biol*. PMID: 38168769
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 56.1 |
| 高置信度残基 (pLDDT>90) 占比 | 11.6% |
| 置信残基 (pLDDT 70-90) 占比 | 14.1% |
| 有序区域 (pLDDT>70) 占比 | 25.7% |
| 可用 PDB 条目 | 7QOO, 7R5S, 7XHN, 7XHO, 7YWX |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CENPT/CENPT-PAE.png]]

**评价**: AlphaFold 预测质量一般（pLDDT=56.1），有序区 25.7%。作为新颖蛋白，结构基线下不扣分。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR028255 - CENP-T; InterPro: IPR035425 - CENP-T/H4_C; InterPro: IPR032373 - CENP-T_N; InterPro: IPR009072 - H |

**染色质调控潜力分析**: 含明确的核酸结合/染色质相关结构域，多库确认。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| CENPI | 0.999 | — | — |
| CENPC | 0.999 | — | — |
| CENPN | 0.999 | — | — |
| CENPS | 0.999 | — | — |
| CENPX | 0.999 | — | — |
| CENPH | 0.999 | — | — |
| CENPW | 0.999 | — | — |
| CENPO | 0.999 | — | — |
| CENPM | 0.999 | — | — |
| CENPU | 0.999 | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| intact:EBI-2132248 | — | — | — | — |
| intact:EBI-727106|uniprotkb:Q6IAX7|ensembl:ENSP00000308057.3|ensembl:ENSP00000377296.2|ensembl:ENSP00000422223.1|ensembl:ENSP00000424073.1 | — | — | — | — |
| intact:EBI-719918|uniprotkb:Q96I29|uniprotkb:Q96IC6|uniprotkb:Q96NK9|uniprotkb:Q9H901|ensembl:ENSP00000400140.2|ensembl:ENSP00000457810.1 | — | — | — | — |
| intact:EBI-710310|uniprotkb:Q8TD37|uniprotkb:Q8TD38|uniprotkb:B3KNM1|ensembl:ENSP00000343515.5 | — | — | — | — |
| intact:EBI-5487792|intact:EBI-5487815 | — | — | — | — |

**已知复合体成员** (GO Cellular Component):
- 无 GO-CC 注释

**PPI 互证分析**:
- STRING + IntAct 共同确认: 0
- 仅 STRING 预测: 20
- 仅 IntAct 实验: 31
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 20 个预测互作，IntAct 31 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=56.1 + PDB: 7QOO, 7R5S, 7XHN, 7XHO, 7YWX | pLDDT=56.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome, centromere; Chromosome, centr | 待确认 |
| PPI | STRING + IntAct | 20 + 31 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +1.0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CENPT — Centromere protein T，有一定研究基础，但仍存在未探索的niche空间。
2. 蛋白大小561 aa，大小适中，适合常规生化实验和结构解析。

**风险/不确定性**:
1. 已有一定研究，需确认独特研究角度
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新 5 篇关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外 DNA/染色质结合实验

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96BT3
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CENPT
- AlphaFold: https://alphafold.ebi.ac.uk/entry/CENPT


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[CENPT-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CENPT/CENPT-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96BT3 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR028255;IPR035425;IPR032373;IPR009072; |
| Pfam | PF15511;PF16171; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000102901-CENPT/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CENPW | Intact, Biogrid | true |
| CENPA | Biogrid | false |
| CENPS | Biogrid | false |
| CENPU | Biogrid | false |
| COPS5 | Biogrid | false |
| H2BC8 | Biogrid | false |
| SPC24 | Intact | false |
| SPC25 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
