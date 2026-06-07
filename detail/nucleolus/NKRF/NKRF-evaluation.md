---
type: protein-evaluation
gene: "NKRF"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NKRF 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | NKRF / XTBD3|ITBA4|NRF |
| 蛋白名称 | NF-kappa-B-repressing factor |
| 蛋白大小 | 690 aa |
| UniProt ID | O15226 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/NKRF/IF_images/U-251MG_1.jpg|U-251MG]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/NKRF/IF_images/A-431_1.jpg|A-431]]

### 2. 评分总览

| 维度 | 得分 | 加权 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 8/10 | ×4 | **32** | UniProt Nucleus，中等可信度 |
| 📏 蛋白大小 | 10/10 | ×1 | **10** | 690 aa，适合生化实验和结构解析 |
| 🆕 研究新颖性 | 4/10 | ×5 | 20 | PubMed 80篇，有一定研究空间 |
| 🏗️ 三维结构 | 8/10 | ×3 | **24** | 2 个 PDB 实验结构 + AlphaFold 预测 |
| 🧬 调控结构域 | 7/10 | ×2 | **14** | 14 个结构域注释，新颖蛋白基线（存在新域发现潜力） |
| 🔗 PPI 网络 | 4/10 | ×3 | **12** | STRING 15 partners，调控比例较低 |
| ➕ 互证加分 | — | — | **+2.0** | 核定位: UniProt + GO 双库一致 (+1); 三维结构: AlphaFold + PDB 双源 (+0.5); 结构域: 多库注释一致 (+0.5) |
|  | **原始总分** |  | **113/183** | **112.0/183** |  |
|  | **归一化总分** |  | **61.7/100** | **61.2/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_conserved_high_confidence | 高置信度保守 |
| Protein Atlas (IF) | 暂无数据（HPA IF 图像已本地嵌入。

| UniProt | Nucleus, nucleolus | 实验/预测 |
| GO Cellular Component | GO:0005634 | N/A |

**结论**: UniProt Nucleus，中等可信度

#### 3.2 蛋白大小评估

**评价**: 690 aa，690 aa，适合生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 80 |
| 核定位分数 (weighted max) | 6 |
| Research hotness | 6.1933 |

**关键文献**:
1. Ashraf et al. (2021). "Pathogenicity and virulence of Japanese encephalitis virus: Neuroinflammation and neuronal cell damage.". *Virulence*. PMID: 33724154
2. Lin et al. (2025). "Nucleus-translocated GCLM promotes chemoresistance in colorectal cancer through a moonlighting function.". *Nat Commun*. PMID: 39747101
3. Guo et al. (2023). "NKRF in Cardiac Fibroblasts Protects against Cardiac Remodeling Post-Myocardial Infarction via Human Antigen R.". *Adv Sci (Weinh)*. PMID: 37667861
4. Gu et al. (2025). "Genome-Wide Identification of Microglia-Related RNA-Binding Proteins and Regulated Alternative Splicing in Spinal Cord Injury.". *ACS Omega*. PMID: 40893312
5. Alexandrova et al. (2020). "Full-length NF-κB repressing factor contains an XRN2 binding domain.". *Biochem J*. PMID: 32011671
**评价**: PubMed 80篇，有一定研究空间

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 690 aa |
| PDB 条目数 | 2 |
| UniProt 注释结构域数 | 14 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleolus/NKRF/NKRF-PAE.png]]

**评价**: 2 个 PDB 实验结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | dsRBD_dom |
| InterPro | DSRM_CARF/NKRF |
| InterPro | G_patch_dom |
| InterPro | R3H_dom |
| InterPro | R3H_dom_sf |
| InterPro | R3H_NRF |
| Pfam | DSRM_CARF |
| Pfam | G-patch |
| Pfam | R3H |
| SMART | DSRM |
| SMART | G_patch |
| SMART | R3H |
| PROSITE | G_PATCH |
| PROSITE | R3H |

**染色质调控潜力分析**: 14 个结构域注释，新颖蛋白基线（存在新域发现潜力）

#### 3.6 PPI 网络

**实验验证互作** (IntAct):

IntAct 实验互作: 0 条

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| DHX15 | 0 |  | 否 |
| KEAP1 | 0 |  | 否 |
| JUN | 0 |  | 否 |
| XRN2 | 0 |  | 否 |
| RELA | 0 |  | 否 |
| POU2F3 | 0 |  | 否 |
| DCAF11 | 0 |  | 否 |
| STAU1 | 0 |  | 否 |
| MAF | 0 |  | 否 |
| PRKRA | 0 |  | 否 |

**已知复合体成员** (GO Cellular Component):

—

**PPI 互证分析**: STRING 15 partners，调控比例较低

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 2 entries | 一致 |
| 结构域 | UniProt / InterPro / Pfam | 14 domains | 多库一致 |
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
1. 新颖性: PubMed 80 篇，有一定研究空间
2. 核定位: 明确核定位

**风险/不确定性**:
1. HPA IF 数据可进一步验证
2. 2 PDB 结构可用

**下一步建议**:
- [ ] 验证核定位: IF 实验确认亚核定位
- [ ] 功能研究: 基于 PPI 网络设计功能实验
- [ ] 结构分析: 基于 PDB 结构设计功能实验

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=NKRF
- Protein Atlas: https://www.proteinatlas.org/ENSG00000186416-NKRF
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22NKRF%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/O15226
- STRING: https://string-db.org/network/9606.ENSG00000186416
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O15226


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[NKRF-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/NKRF/NKRF-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O15226 |
| SMART | SM00358;SM00443;SM00393; |
| UniProt Domain [FT] | DOMAIN 551..596; /note="G-patch"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00092"; DOMAIN 600..664; /note="R3H"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00382" |
| InterPro | IPR014720;IPR058828;IPR000467;IPR001374;IPR036867;IPR034071; |
| Pfam | PF26535;PF01585;PF01424; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000186416-NKRF/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DHX58 | Intact, Biogrid | true |
| ILF3 | Biogrid, Opencell | true |
| NIFK | Biogrid, Bioplex | true |
| PRKRA | Intact, Biogrid, Bioplex | true |
| RPL19 | Biogrid, Opencell, Bioplex | true |
| RPL31 | Biogrid, Bioplex | true |
| RPL4 | Biogrid, Opencell, Bioplex | true |
| STAU1 | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
