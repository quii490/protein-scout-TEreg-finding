---
type: protein-evaluation
gene: "NAB1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NAB1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | NAB1 / — |
| 蛋白名称 | NGFI-A-binding protein 1 |
| 蛋白大小 | 487 aa |
| UniProt ID | Q13506 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 加权 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 8/10 | ×4 | **32** | UniProt Nucleus，中等可信度 |
| 📏 蛋白大小 | 10/10 | ×1 | **10** | 487 aa，适合生化实验和结构解析 |
| 🆕 研究新颖性 | 4/10 | ×5 | 20 | PubMed 62篇，有一定研究空间 |
| 🏗️ 三维结构 | 8/10 | ×3 | **24** | 1 个 PDB 实验结构 + AlphaFold 预测 |
| 🧬 调控结构域 | 7/10 | ×2 | **14** | 8 个结构域注释，新颖蛋白基线（存在新域发现潜力） |
| 🔗 PPI 网络 | 4/10 | ×3 | **12** | STRING 15 partners，调控比例较低 |
| ➕ 互证加分 | — | — | **+2.0** | 核定位: UniProt + GO 双库一致 (+1); 三维结构: AlphaFold + PDB 双源 (+0.5); 结构域: 多库注释一致 (+0.5) |
|  | **原始总分** |  | **113/183** | **112.0/183** |  |  |  |
|  | **归一化总分** |  | **61.7/100** | **61.2/100** |  |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_conserved_high_confidence | 高置信度保守 |
| Protein Atlas (IF) | IF image available (embedded below) | See IF_images/ |
| UniProt | Nucleus | 实验/预测 |
| GO Cellular Component | GO:0005634 | N/A |


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NAB1/IF_images/A-431_HPA002738_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NAB1/IF_images/U-251MG_HPA002738_2.jpg|U-251MG]]

**结论**: UniProt Nucleus，中等可信度

#### 3.2 蛋白大小评估

**评价**: 487 aa，487 aa，适合生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 62 |
| 核定位分数 (weighted max) | 6 |
| Research hotness | 4.3996 |

**评价**: PubMed 62篇，有一定研究空间

**关键文献**:
1. Du WW et al. (2025). "A Novel Protein NAB1-356 Encoded by circRNA circNAB1 Mitigates Atrial Fibrillation by Reducing Inflammation and Fibrosis". *Adv Sci (Weinh)*. PMID: 40145839
2. Ollila HM et al. (2023). "Narcolepsy risk loci outline role of T cell autoimmunity and infectious triggers in narcolepsy". *Nat Commun*. PMID: 37188663
3. Chen J et al. (2018). "Non-dormant Axillary Bud 1 regulates axillary bud outgrowth in sorghum". *J Integr Plant Biol*. PMID: 29740955
4. Khatri B et al. (2022). "Genome-wide association study identifies Sjögren's risk loci with functional implications in immune and glandular cells". *Nat Commun*. PMID: 35896530
5. Blifernez O et al. (2011). "Protein arginine methylation modulates light-harvesting antenna translation in Chlamydomonas reinhardtii". *Plant J*. PMID: 21175895
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 487 aa |
| PDB 条目数 | 1 |
| UniProt 注释结构域数 | 8 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NAB1/NAB1-PAE.png]]

**评价**: 1 个 PDB 实验结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | Nab1_C |
| InterPro | NAB_co-repressor_dom |
| InterPro | NAB_fam |
| InterPro | Nab_N |
| InterPro | NCD2_sf |
| Pfam | Nab1 |
| Pfam | NCD2 |
| Pfam | SAM_NCD1 |

**染色质调控潜力分析**: 8 个结构域注释，新颖蛋白基线（存在新域发现潜力）

#### 3.6 PPI 网络

**实验验证互作** (IntAct):

IntAct 实验互作: 0 条

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| EGR1 | 0 |  | 否 |
| EGR2 | 0 |  | 否 |
| EGR3 | 0 |  | 否 |
| EGR4 | 0 |  | 否 |
| SRF | 0 |  | 否 |
| SOX10 | 0 |  | 否 |
| NAB2 | 0 |  | 否 |
| STAT2 | 0 |  | 否 |
| CREB1 | 0 |  | 否 |
| AKTIP | 0 |  | 否 |

**已知复合体成员** (GO Cellular Component):

—

**PPI 互证分析**: STRING 15 partners，调控比例较低

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 1 entries | 一致 |
| 结构域 | UniProt / InterPro / Pfam | 8 domains | 多库一致 |
| PPI | STRING + IntAct | 15 STRING + 0 IntAct | 单源 |
| 定位 | Protein Atlas / UniProt / GO | Nucleus | 多源一致 |

**互证加分明细**:
核定位: UniProt + GO 双库一致 (+1)
三维结构: AlphaFold + PDB 双源 (+0.5)
结构域: 多库注释一致 (+0.5)
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ★★★☆☆ (3/5)

**核心优势**:
1. 新颖性: PubMed 62 篇，有一定研究空间
2. 核定位: 明确核定位

**风险/不确定性**:
1. 无 HPA IF 实验数据
2. 1 PDB 结构可用

**下一步建议**:
- [ ] 验证核定位: IF 实验确认亚核定位
- [ ] 功能研究: 基于 PPI 网络设计功能实验
- [ ] 结构分析: 基于 PDB 结构设计功能实验

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=NAB1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000138386-NAB1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22NAB1%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q13506
- STRING: https://string-db.org/network/9606.ENSG00000138386
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13506


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[NAB1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NAB1/NAB1-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q13506 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR006986;IPR006989;IPR039040;IPR006988;IPR038398; |
| Pfam | PF04902;PF04905;PF04904; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000138386-NAB1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| EEF1AKMT3 | Bioplex | false |
| EGR1 | Biogrid | false |
| MVK | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
