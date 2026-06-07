---
type: protein-evaluation
gene: "NUB1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NUB1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | NUB1 / BS4|NYREN18|NUB1L |
| 蛋白名称 | NEDD8 ultimate buster 1 |
| 蛋白大小 | 615 aa |
| UniProt ID | Q9Y5A7 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 加权 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 8/10 | ×4 | **32** | UniProt Nucleus，中等可信度 |
| 📏 蛋白大小 | 10/10 | ×1 | **10** | 615 aa，适合生化实验和结构解析 |
| 🆕 研究新颖性 | 4/10 | ×5 | 20 | PubMed 76篇，有一定研究空间 |
| 🏗️ 三维结构 | 10/10 | ×3 | **30** | 9 个 PDB 实验结构，实验验证充分 |
| 🧬 调控结构域 | 10/10 | ×2 | **20** | 明确染色质/DNA 调控结构域: sash1/nub1_homeodomain, sash1_homeodomain |
| 🔗 PPI 网络 | 4/10 | ×3 | **12** | STRING 15 partners，调控比例较低 |
| ➕ 互证加分 | — | — | **+2.0** | 核定位: UniProt + GO 双库一致 (+1); 三维结构: AlphaFold + PDB 双源 (+0.5); 结构域: 多库注释一致 (+0.5) |
|  | **原始总分** |  | **125/183** | **124.0/183** |  |  |  |
|  | **归一化总分** |  | **68.3/100** | **67.8/100** |  |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_conserved_high_confidence | 高置信度保守 |
| Protein Atlas (IF) | IF image available (embedded below) | See IF_images/ |
| UniProt | Nucleus | 实验/预测 |
| GO Cellular Component | GO:0005634 | N/A |


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NUB1/IF_images/HEK293_HPA050722_1.jpg|HEK293]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NUB1/IF_images/MCF-7_HPA050722_2.jpg|MCF-7]]

**结论**: UniProt Nucleus，中等可信度

#### 3.2 蛋白大小评估

**评价**: 615 aa，615 aa，适合生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 76 |
| 核定位分数 (weighted max) | 6 |
| Research hotness | 4.8163 |

**评价**: PubMed 76篇，有一定研究空间

**关键文献**:
1. Sendo S et al. (2024). "Dysregulated NUB1 and Neddylation Enhances Rheumatoid Arthritis Fibroblast-Like Synoviocyte Inflammatory Responses". *Arthritis Rheumatol*. PMID: 38566346
2. Arshad M et al. (2021). "NUB1 and FAT10 Proteins as Potential Novel Biomarkers in Cancer: A Translational Perspective". *Cells*. PMID: 34571823
3. Arkinson C et al. (2025). "NUB1 traps unfolded FAT10 for ubiquitin-independent degradation by the 26S proteasome". *Nat Struct Mol Biol*. PMID: 40217121
4. Tang R et al. (2023). "Single-cell RNA sequencing reveals the transcriptomic landscape of kidneys in patients with ischemic acute kidney injury". *Chin Med J (Engl)*. PMID: 37083129
5. Guarascio R et al. (2020). "Negative Regulator of Ubiquitin-Like Protein 1 modulates the autophagy-lysosomal pathway via p62 to facilitate the extracellular release of tau following proteasome impairment". *Hum Mol Genet*. PMID: 31691796
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 615 aa |
| PDB 条目数 | 9 |
| UniProt 注释结构域数 | 12 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NUB1/NUB1-PAE.png]]

**评价**: 9 个 PDB 实验结构，实验验证充分

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | NUB1 |
| InterPro | NUB1_ubiquitin-like_dom |
| InterPro | SASH1/NUB1_homeodomain |
| InterPro | TPR-like_helical_dom_sf |
| InterPro | UBA |
| InterPro | UBA-like_sf |
| InterPro | Ubiquitin-like_domsf |
| Pfam | SASH1_Homeodomain |
| Pfam | UBA |
| Pfam | Ubiquitin_5 |
| SMART | UBA |
| PROSITE | UBA |

**染色质调控潜力分析**: 明确染色质/DNA 调控结构域: sash1/nub1_homeodomain, sash1_homeodomain

#### 3.6 PPI 网络

**实验验证互作** (IntAct):

IntAct 实验互作: 0 条

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| NEDD8 | 0 |  | 否 |
| PSMD4 | 0 |  | 否 |
| AIPL1 | 0 |  | 否 |
| UBD | 0 |  | 否 |
| SNCAIP | 0 |  | 否 |
| PSMD2 | 0 |  | 否 |
| SENP8 | 0 |  | 否 |
| PSME2 | 0 |  | 否 |
| PSMD5 | 0 |  | 否 |
| VCP | 0 |  | 否 |

**已知复合体成员** (GO Cellular Component):

—

**PPI 互证分析**: STRING 15 partners，调控比例较低

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 9 entries | 一致 |
| 结构域 | UniProt / InterPro / Pfam | 12 domains | 多库一致 |
| PPI | STRING + IntAct | 15 STRING + 0 IntAct | 单源 |
| 定位 | Protein Atlas / UniProt / GO | Nucleus | 多源一致 |

**互证加分明细**:
核定位: UniProt + GO 双库一致 (+1)
三维结构: AlphaFold + PDB 双源 (+0.5)
结构域: 多库注释一致 (+0.5)
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ★★★★☆ (4/5)

**核心优势**:
1. 新颖性: PubMed 76 篇，有一定研究空间
2. 核定位: 明确核定位

**风险/不确定性**:
1. HPA IF 数据可进一步验证
2. 9 PDB 结构可用

**下一步建议**:
- [ ] 验证核定位: IF 实验确认亚核定位
- [ ] 功能研究: 基于 PPI 网络设计功能实验
- [ ] 结构分析: 基于 PDB 结构设计功能实验

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=NUB1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000013374-NUB1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22NUB1%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q9Y5A7
- STRING: https://string-db.org/network/9606.ENSG00000013374
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y5A7


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[NUB1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NUB1/NUB1-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9Y5A7 |
| SMART | SM00165; |
| UniProt Domain [FT] | DOMAIN 374..413; /note="UBA 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00212"; DOMAIN 424..470; /note="UBA 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00212"; DOMAIN 489..529; /note="UBA 3"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00212" |
| InterPro | IPR039749;IPR041207;IPR058666;IPR011990;IPR015940;IPR009060;IPR029071; |
| Pfam | PF26285;PF00627;PF18037; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000013374-NUB1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AIPL1 | Intact, Biogrid | true |
| TERF1 | Intact, Biogrid | true |
| UBD | Intact, Biogrid | true |
| NEDD8 | Biogrid | false |
| PSMC5 | Opencell | false |
| PSMD2 | Biogrid | false |
| PSMD4 | Biogrid | false |
| SF3B4 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
