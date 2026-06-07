---
type: protein-evaluation
gene: "NEMP1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NEMP1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | NEMP1 / KIAA0286 |
| 蛋白名称 | Nuclear envelope integral membrane protein 1 |
| 蛋白大小 | 444 aa |
| UniProt ID | O14524 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/NEMP1/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/NEMP1/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 加权 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 5/10 | ×4 | **20** | 核定位证据较弱 |
| 📏 蛋白大小 | 10/10 | ×1 | **10** | 444 aa，适合生化实验和结构解析 |
| 🆕 研究新颖性 | 10/10 | ×5 | **50** | PubMed 12篇，极度新颖 |
| 🏗️ 三维结构 | 6/10 | ×3 | **18** | 无 PDB 结构，AlphaFold 预测可用，新颖蛋白基线分 |
| 🧬 调控结构域 | 7/10 | ×2 | **14** | 2 个结构域，新颖蛋白基线 |
| 🔗 PPI 网络 | 4/10 | ×3 | **12** | STRING 15 partners，调控比例较低 |
| ➕ 互证加分 | — | — | **+0.5** | PPI: IntAct + STRING 双源 (+0.5) |
| **原始总分** |  |  | **124.5/183** |  |
| **归一化总分** |  |  | **68.0/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_conserved_high_confidence | 高置信度保守 |
| Protein Atlas (IF) | 暂无数据（HPA IF 图像已本地嵌入。

| UniProt | N/A | 实验/预测 |
| GO Cellular Component | N/A | N/A |

**结论**: 核定位证据较弱

#### 3.2 蛋白大小评估

**评价**: 444 aa，444 aa，适合生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 12 |
| 核定位分数 (weighted max) | 5 |
| Research hotness | 4.0145 |

**关键文献**:
1. Hakim et al. (2025). "Nuclear Envelope Membrane Protein 1 plays crucial and conserved roles in female meiosis.". *Res Sq*. PMID: 40799732
2. Tsatskis et al. (2020). "The NEMP family supports metazoan fertility and nuclear envelope stiffness.". *Sci Adv*. PMID: 32923640
3. Hodzic et al. (2022). "The inner nuclear membrane protein NEMP1 supports nuclear envelope openings and enucleation of erythroblasts.". *PLoS Biol*. PMID: 36215313
4. Ganguly et al. (2026). "The Nemp1-Nesprin complex mediates cellular responses to matrix mechanics.". *Proc Natl Acad Sci U S A*. PMID: 41730104
5. Kropotova et al. (2016). "A Group of Weakly Bound to Neurons Extracellular Metallopeptidases (NEMPs).". *Neurochem Res*. PMID: 27350576
**评价**: PubMed 12篇，极度新颖

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 444 aa |
| PDB 条目数 | 0 |
| UniProt 注释结构域数 | 2 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/NEMP1/NEMP1-PAE.png]]

**评价**: 无 PDB 结构，AlphaFold 预测可用，新颖蛋白基线分

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | NEMP_fam |
| Pfam | NEMP |

**染色质调控潜力分析**: 2 个结构域，新颖蛋白基线

#### 3.6 PPI 网络

**实验验证互作** (IntAct):

IntAct 实验互作: 150 条

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| RANGAP1 | 0 |  | 否 |
| RANBP2 | 0 |  | 否 |
| UBE2I | 0 |  | 否 |
| RGPD2 | 0 |  | 否 |
| RAN | 0 |  | 否 |
| DLGAP5 | 0 |  | 否 |
| B2M | 0 |  | 否 |
| RCC1 | 0 |  | 否 |
| UBALD1 | 0 |  | 否 |
| CCDC77 | 0 |  | 否 |

**已知复合体成员** (GO Cellular Component):

—

**PPI 互证分析**: STRING 15 partners，调控比例较低

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 0 entries | 仅预测 |
| 结构域 | UniProt / InterPro / Pfam | 2 domains | 多库一致 |
| PPI | STRING + IntAct | 15 STRING + 150 IntAct | 双源 |
| 定位 | Protein Atlas / UniProt / GO | Nucleus | 部分一致 |

**互证加分明细**:
PPI: IntAct + STRING 双源 (+0.5)
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ★★★☆☆ (3/5)

**核心优势**:
1. 新颖性: PubMed 12 篇，极度新颖
2. 核定位: 部分核定位

**风险/不确定性**:
1. 无 HPA IF 实验数据
2. 无 PDB 实验结构，仅 AlphaFold 预测

**下一步建议**:
- [ ] 验证核定位: IF 实验确认亚核定位
- [ ] 功能研究: 基于 PPI 网络设计功能实验
- [ ] 结构分析: AlphaFold 预测为基础，设计突变实验

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=NEMP1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000166881-NEMP1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22NEMP1%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/O14524
- STRING: https://string-db.org/network/9606.ENSG00000166881
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O14524


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[NEMP1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/NEMP1/NEMP1-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O14524 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR019358; |
| Pfam | PF10225; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000166881-NEMP1/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
