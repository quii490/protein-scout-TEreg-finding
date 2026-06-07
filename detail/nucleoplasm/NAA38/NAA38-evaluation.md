---
type: protein-evaluation
gene: "NAA38"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NAA38 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | NAA38 / MGC14151|PFAAP2 |
| 蛋白名称 | N-alpha-acetyltransferase 38, NatC auxiliary subunit |
| 蛋白大小 | 125 aa |
| UniProt ID | Q9BRA0 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 加权 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | **24** | 核+胞质，有核定位证据 |
| 📏 蛋白大小 | 8/10 | ×1 | **8** | 125 aa，可接受范围 |
| 🆕 研究新颖性 | 10/10 | ×5 | **50** | PubMed 12篇，极度新颖 |
| 🏗️ 三维结构 | 8/10 | ×3 | **24** | 1 个 PDB 实验结构 + AlphaFold 预测 |
| 🧬 调控结构域 | 7/10 | ×2 | **14** | 8 个结构域注释，新颖蛋白基线（存在新域发现潜力） |
| 🔗 PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极少 |
| ➕ 互证加分 | — | — | **+1.0** | 三维结构: AlphaFold + PDB 双源 (+0.5); 结构域: 多库注释一致 (+0.5) |
| **原始总分** |  |  | **126.5/183** |  |
| **归一化总分** |  |  | **69.1/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_conserved_high_confidence | 高置信度保守 |
| Protein Atlas (IF) | IF image available (embedded below) | See IF_images/ |
| UniProt | N/A | 实验/预测 |
| GO Cellular Component | GO:0005634 | N/A |


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NAA38/IF_images/HEK293_HPA059189_1.jpg|HEK293]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NAA38/IF_images/PC-3_HPA059189_2.jpg|PC-3]]

**结论**: 核+胞质，有核定位证据

#### 3.2 蛋白大小评估

**评价**: 125 aa，125 aa，可接受范围。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 12 |
| 核定位分数 (weighted max) | 6 |
| Research hotness | 3.8061 |

**评价**: PubMed 12篇，极度新颖

**关键文献**:
1. Sklar J et al. (2025). "Immune cell-based transcriptomic Mendelian randomization and colocalization study on type 1 diabetes". *BMC Med*. PMID: 41299435
2. Deng S et al. (2021). "Molecular mechanism of N-terminal acetylation by the ternary NatC complex". *Structure*. PMID: 34019809
3. Kaneko Y et al. (2026). "Inhibition of N-Terminal Acetyltransferase C Mitigates Endoplasmic Reticulum Stress-Mediated Muscle Atrophy in Cancer Cachexia". *J Cachexia Sarcopenia Muscle*. PMID: 41852114
4. Deng S et al. (2023). "Molecular role of NAA38 in thermostability and catalytic activity of the human NatC N-terminal acetyltransferase". *Structure*. PMID: 36638802
5. Cao JY et al. (2019). "A Genome-wide Haploid Genetic Screen Identifies Regulators of Glutathione Abundance and Ferroptosis Sensitivity". *Cell Rep*. PMID: 30726737
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 125 aa |
| PDB 条目数 | 1 |
| UniProt 注释结构域数 | 8 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NAA38/NAA38-PAE.png]]

**评价**: 1 个 PDB 实验结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | LSM_dom_sf |
| InterPro | LSMD1_Sm |
| InterPro | Sm |
| InterPro | Sm_dom_euk/arc |
| InterPro | snRNP_SmB/NAA38-like |
| Pfam | LSM |
| SMART | Sm |
| PROSITE | SM |

**染色质调控潜力分析**: 8 个结构域注释，新颖蛋白基线（存在新域发现潜力）

#### 3.6 PPI 网络

**实验验证互作** (IntAct):

IntAct 实验互作: 63 条

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| — | — | — | — |

**已知复合体成员** (GO Cellular Component):

- C:NatC complex (GO:0031417, IDA:UniProtKB)

**PPI 互证分析**: PPI 数据极少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 1 entries | 一致 |
| 结构域 | UniProt / InterPro / Pfam | 8 domains | 多库一致 |
| PPI | STRING + IntAct | 0 STRING + 63 IntAct | 单源 |
| 定位 | Protein Atlas / UniProt / GO | Nucleus | 多源一致 |

**互证加分明细**:
三维结构: AlphaFold + PDB 双源 (+0.5)
结构域: 多库注释一致 (+0.5)
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ★★★☆☆ (3/5)

**核心优势**:
1. 新颖性: PubMed 12 篇，极度新颖
2. 核定位: 部分核定位

**风险/不确定性**:
1. HPA IF 数据可进一步验证
2. 1 PDB 结构可用

**下一步建议**:
- [ ] 验证核定位: IF 实验确认亚核定位
- [ ] 功能研究: 基于 PPI 网络设计功能实验
- [ ] 结构分析: 基于 PDB 结构设计功能实验

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=NAA38
- Protein Atlas: https://www.proteinatlas.org/ENSG00000183011-NAA38
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22NAA38%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q9BRA0
- STRING: https://string-db.org/network/9606.ENSG00000183011
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BRA0


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[NAA38-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NAA38/NAA38-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BRA0 |
| SMART | SM00651; |
| UniProt Domain [FT] | DOMAIN 40..118; /note="Sm"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01346" |
| InterPro | IPR010920;IPR034110;IPR047575;IPR001163;IPR050914; |
| Pfam | PF01423; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000183011-NAA38/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| KLK6 | Intact | false |
| N4BP2L2 | Intact | false |
| NAA35 | Intact | false |
| PDE9A | Intact | false |
| PRR20C | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
