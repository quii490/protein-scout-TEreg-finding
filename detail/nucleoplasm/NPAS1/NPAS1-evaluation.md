---
type: protein-evaluation
gene: "NPAS1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NPAS1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | NPAS1 / MOP5|PASD5|bHLHe11 |
| 蛋白名称 | Neuronal PAS domain-containing protein 1 |
| 蛋白大小 | 590 aa |
| UniProt ID | Q99742 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 加权 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 8/10 | ×4 | **32** | UniProt Nucleus，中等可信度 |
| 📏 蛋白大小 | 10/10 | ×1 | **10** | 590 aa，适合生化实验和结构解析 |
| 🆕 研究新颖性 | 6/10 | ×5 | 30 | PubMed 42篇，非常新颖 |
| 🏗️ 三维结构 | 6/10 | ×3 | **18** | 无 PDB 结构，AlphaFold 预测可用，新颖蛋白基线分 |
| 🧬 调控结构域 | 10/10 | ×2 | **20** | 明确染色质/DNA 调控结构域: bhlh, bhlh_dom, bhlh_hif1a, hlh, hlh_dna-bd_sf |
| 🔗 PPI 网络 | 4/10 | ×3 | **12** | STRING 15 partners，调控比例较低 |
| ➕ 互证加分 | — | — | **+1.5** | 核定位: UniProt + GO 双库一致 (+1); 结构域: 多库注释一致 (+0.5) |
|  | **原始总分** |  | **123/183** | **122.0/183** |  |  |  |
|  | **归一化总分** |  | **67.2/100** | **66.7/100** |  |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_conserved_high_confidence | 高置信度保守 |
| Protein Atlas (IF) | IF image available (embedded below) | See IF_images/ |
| UniProt | Nucleus | 实验/预测 |
| GO Cellular Component | GO:0005634 | N/A |


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NPAS1/IF_images/BJ_[Human_fibroblast]_HPA072259_1.jpg|BJ [Human fibroblast]]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NPAS1/IF_images/HEK293_HPA072259_2.jpg|HEK293]]

**结论**: UniProt Nucleus，中等可信度

#### 3.2 蛋白大小评估

**评价**: 590 aa，590 aa，适合生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 42 |
| 核定位分数 (weighted max) | 6 |
| Research hotness | 4.0858 |

**评价**: PubMed 42篇，非常新颖

**关键文献**:
1. Troppoli TA et al. (2024). "Neuronal PAS domain 1 identifies a major subpopulation of wakefulness-promoting GABAergic neurons in the basal forebrain". *Proc Natl Acad Sci U S A*. PMID: 38748575
2. Labouesse MA et al. (2023). "A non-canonical striatopallidal Go pathway that supports motor control". *Nat Commun*. PMID: 37872145
3. Troppoli TA et al. (2023). "Neuronal PAS domain 1 identifies a major subpopulation of wakefulness-promoting GABAergic neurons in basal forebrain". *bioRxiv*. PMID: 37986953
4. Noebels JL et al. (2024). "Transcriptional Regulation of Cortical Interneuron Development". **. PMID: 39637134
5. Zhou YD et al. (1997). "Molecular characterization of two mammalian bHLH-PAS domain proteins selectively expressed in the central nervous system". *Proc Natl Acad Sci U S A*. PMID: 9012850
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 590 aa |
| PDB 条目数 | 0 |
| UniProt 注释结构域数 | 13 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NPAS1/NPAS1-PAE.png]]

**评价**: 无 PDB 结构，AlphaFold 预测可用，新颖蛋白基线分

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | bHLH_dom |
| InterPro | HLH_DNA-bd_sf |
| InterPro | PAS |
| InterPro | PAS-like_dom_sf |
| InterPro | PAS_fold |
| InterPro | PAS_fold_3 |
| Pfam | bHLH_HIF1A |
| Pfam | PAS |
| Pfam | PAS_3 |
| SMART | HLH |
| SMART | PAS |
| PROSITE | BHLH |
| PROSITE | PAS |

**染色质调控潜力分析**: 明确染色质/DNA 调控结构域: bhlh, bhlh_dom, bhlh_hif1a, hlh, hlh_dna-bd_sf

#### 3.6 PPI 网络

**实验验证互作** (IntAct):

IntAct 实验互作: 0 条

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| ARNT | 0 |  | 否 |
| ARNT2 | 0 |  | 否 |
| LHX6 | 0 |  | 否 |
| PER1 | 0 |  | 否 |
| EGLN3 | 0 |  | 否 |
| GYPE | 0 |  | 否 |
| NPAS2 | 0 |  | 否 |
| PASD1 | 0 |  | 否 |
| BHLHE41 | 0 |  | 否 |
| ESRRG | 0 |  | 否 |

**已知复合体成员** (GO Cellular Component):

- C:chromatin (GO:0000785, ISA:NTNU_SB)

**PPI 互证分析**: STRING 15 partners，调控比例较低

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 0 entries | 仅预测 |
| 结构域 | UniProt / InterPro / Pfam | 13 domains | 多库一致 |
| PPI | STRING + IntAct | 15 STRING + 0 IntAct | 单源 |
| 定位 | Protein Atlas / UniProt / GO | Nucleus | 多源一致 |

**互证加分明细**:
核定位: UniProt + GO 双库一致 (+1)
结构域: 多库注释一致 (+0.5)
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ★★★★☆ (4/5)

**核心优势**:
1. 新颖性: PubMed 42 篇，比较新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. HPA IF 数据可进一步验证
2. 无 PDB 实验结构，仅 AlphaFold 预测

**下一步建议**:
- [ ] 验证核定位: IF 实验确认亚核定位
- [ ] 功能研究: 基于 PPI 网络设计功能实验
- [ ] 结构分析: AlphaFold 预测为基础，设计突变实验

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=NPAS1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000130751-NPAS1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22NPAS1%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q99742
- STRING: https://string-db.org/network/9606.ENSG00000130751
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q99742


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[NPAS1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NPAS1/NPAS1-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q99742 |
| SMART | SM00353;SM00091; |
| UniProt Domain [FT] | DOMAIN 45..98; /note="bHLH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00981"; DOMAIN 135..207; /note="PAS 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00140"; DOMAIN 293..359; /note="PAS 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00140"; DOMAIN 365..408; /note="PAC" |
| InterPro | IPR011598;IPR036638;IPR000014;IPR035965;IPR013767;IPR013655; |
| Pfam | PF23171;PF00989;PF08447; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000130751-NPAS1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ACTR5 | Bioplex | false |
| ACTR8 | Bioplex | false |
| AKAP1 | Bioplex | false |
| AKAP10 | Bioplex | false |
| AKAP11 | Bioplex | false |
| ANAPC5 | Bioplex | false |
| ANKLE2 | Bioplex | false |
| ANKRD11 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
