---
type: protein-evaluation
gene: "NHLH2"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NHLH2 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | NHLH2 / NSCL2|bHLHa34 |
| 蛋白名称 | Helix-loop-helix protein 2 |
| 蛋白大小 | 135 aa |
| UniProt ID | Q02577 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 加权 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 8/10 | ×4 | **32** | UniProt Nucleus，中等可信度 |
| 📏 蛋白大小 | 8/10 | ×1 | **8** | 135 aa，可接受范围 |
| 🆕 研究新颖性 | 4/10 | ×5 | 20 | PubMed 61篇，有一定研究空间 |
| 🏗️ 三维结构 | 6/10 | ×3 | **18** | 无 PDB 结构，AlphaFold 预测可用，新颖蛋白基线分 |
| 🧬 调控结构域 | 10/10 | ×2 | **20** | 明确染色质/DNA 调控结构域: bhlh, bhlh_dom, hlh, hlh_dna-bd_sf |
| 🔗 PPI 网络 | 4/10 | ×3 | **12** | STRING 15 partners，调控比例较低 |
| ➕ 互证加分 | — | — | **+1.5** | 核定位: UniProt + GO 双库一致 (+1); 结构域: 多库注释一致 (+0.5) |
|  | **原始总分** |  | **111/183** | **110.0/183** |  |  |  |
|  | **归一化总分** |  | **60.7/100** | **60.1/100** |  |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_conserved_high_confidence | 高置信度保守 |
| Protein Atlas (IF) | IF image available (embedded below) | See IF_images/ |
| UniProt | Nucleus | 实验/预测 |
| GO Cellular Component | GO:0005634 | N/A |


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NHLH2/IF_images/HEK293_HPA055238_1.jpg|HEK293]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NHLH2/IF_images/SiHa_HPA055238_2.jpg|SiHa]]

**结论**: UniProt Nucleus，中等可信度

#### 3.2 蛋白大小评估

**评价**: 135 aa，135 aa，可接受范围。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 61 |
| 核定位分数 (weighted max) | 6 |
| Research hotness | 4.1587 |

**评价**: PubMed 61篇，有一定研究空间

**关键文献**:
1. Good DJ et al. (2020). "Pro-opiomelanocortin Neurons and the Transcriptional Regulation of Motivated Exercise". *Exerc Sport Sci Rev*. PMID: 32168170
2. Good DJ et al. (2015). "A Genetic Basis for Motivated Exercise". *Exerc Sport Sci Rev*. PMID: 26196864
3. Wankhade UD & Good DJ (2011). "Melanocortin 4 receptor is a transcriptional target of nescient helix-loop-helix-2". *Mol Cell Endocrinol*. PMID: 21664420
4. Carraro RS et al. (2021). "Arcuate Nucleus Overexpression of NHLH2 Reduces Body Mass and Attenuates Obesity-Associated Anxiety/Depression-like Behavior". *J Neurosci*. PMID: 34675088
5. Schmid T et al. (2020). "GnRH neurogenesis depends on embryonic pheromone receptor expression". *Mol Cell Endocrinol*. PMID: 32931849
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 135 aa |
| PDB 条目数 | 0 |
| UniProt 注释结构域数 | 6 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NHLH2/NHLH2-PAE.png]]

**评价**: 无 PDB 结构，AlphaFold 预测可用，新颖蛋白基线分

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | bHLH_dom |
| InterPro | HLH_DNA-bd_sf |
| InterPro | TAL-like |
| Pfam | HLH |
| SMART | HLH |
| PROSITE | BHLH |

**染色质调控潜力分析**: 明确染色质/DNA 调控结构域: bhlh, bhlh_dom, hlh, hlh_dna-bd_sf

#### 3.6 PPI 网络

**实验验证互作** (IntAct):

IntAct 实验互作: 0 条

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| BEX1 | 0 |  | 否 |
| BEX2 | 0 |  | 否 |
| LDB2 | 0 |  | 否 |
| LDB1 | 0 |  | 否 |
| LMO2 | 0 |  | 否 |
| MC4R | 0 |  | 否 |
| PCSK1 | 0 |  | 否 |
| TCF3 | 0 |  | 否 |
| OTP | 0 |  | 否 |
| ID1 | 0 |  | 否 |

**已知复合体成员** (GO Cellular Component):

- C:chromatin (GO:0000785, ISA:NTNU_SB)
- C:transcription regulator complex (GO:0005667, TAS:BHF-UCL)

**PPI 互证分析**: STRING 15 partners，调控比例较低

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 0 entries | 仅预测 |
| 结构域 | UniProt / InterPro / Pfam | 6 domains | 多库一致 |
| PPI | STRING + IntAct | 15 STRING + 0 IntAct | 单源 |
| 定位 | Protein Atlas / UniProt / GO | Nucleus | 多源一致 |

**互证加分明细**:
核定位: UniProt + GO 双库一致 (+1)
结构域: 多库注释一致 (+0.5)
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ★★★☆☆ (3/5)

**核心优势**:
1. 新颖性: PubMed 61 篇，有一定研究空间
2. 核定位: 明确核定位

**风险/不确定性**:
1. HPA IF 数据可进一步验证
2. 无 PDB 实验结构，仅 AlphaFold 预测

**下一步建议**:
- [ ] 验证核定位: IF 实验确认亚核定位
- [ ] 功能研究: 基于 PPI 网络设计功能实验
- [ ] 结构分析: AlphaFold 预测为基础，设计突变实验

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=NHLH2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000177551-NHLH2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22NHLH2%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q02577
- STRING: https://string-db.org/network/9606.ENSG00000177551
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q02577


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[NHLH2-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NHLH2/NHLH2-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q02577 |
| SMART | SM00353; |
| UniProt Domain [FT] | DOMAIN 77..129; /note="bHLH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00981" |
| InterPro | IPR011598;IPR036638;IPR040238; |
| Pfam | PF00010; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000177551-NHLH2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AP3B1 | Bioplex | false |
| ARFGEF1 | Bioplex | false |
| ARFGEF2 | Bioplex | false |
| BHLHA15 | Bioplex | false |
| CUEDC1 | Bioplex | false |
| HBB | Bioplex | false |
| HES1 | Biogrid | false |
| MYF5 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
