---
type: protein-evaluation
gene: "NFKBID"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NFKBID 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | NFKBID / TA-NFKBH|IkappaBNS|IkBNS |
| 蛋白名称 | NF-kappa-B inhibitor delta |
| 蛋白大小 | 313 aa |
| UniProt ID | Q8NI38 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 加权 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 8/10 | ×4 | **32** | UniProt Nucleus，中等可信度 |
| 📏 蛋白大小 | 10/10 | ×1 | **10** | 313 aa，适合生化实验和结构解析 |
| 🆕 研究新颖性 | 4/10 | ×5 | 20 | PubMed 76篇，有一定研究空间 |
| 🏗️ 三维结构 | 6/10 | ×3 | **18** | 无 PDB 结构，AlphaFold 预测可用，新颖蛋白基线分 |
| 🧬 调控结构域 | 7/10 | ×2 | **14** | 7 个结构域注释，新颖蛋白基线（存在新域发现潜力） |
| 🔗 PPI 网络 | 4/10 | ×3 | **12** | STRING 15 partners，调控比例较低 |
| ➕ 互证加分 | — | — | **+1.5** | 核定位: UniProt + GO 双库一致 (+1); 结构域: 多库注释一致 (+0.5) |
|  | **原始总分** |  | **107/183** | **106.0/183** |  |  |  |
|  | **归一化总分** |  | **58.5/100** | **57.9/100** |  |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_conserved_high_confidence | 高置信度保守 |
| Protein Atlas (IF) | IF image available (embedded below) | See IF_images/ |
| UniProt | Nucleus | 实验/预测 |
| GO Cellular Component | GO:0005634 | N/A |


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NFKBID/IF_images/HeLa_HPA054778_1.jpg|HeLa]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NFKBID/IF_images/U2OS_HPA054778_2.jpg|U2OS]]

**结论**: UniProt Nucleus，中等可信度

#### 3.2 蛋白大小评估

**评价**: 313 aa，313 aa，适合生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 76 |
| 核定位分数 (weighted max) | 6 |
| Research hotness | 5.306 |

**评价**: PubMed 76篇，有一定研究空间

**关键文献**:
1. Tang M et al. (2022). "[Bioinformatics analysis of IκB gene family expression in human lung adenocarcinoma]". *Xi Bao Yu Fen Zi Mian Yi Xue Za Zhi*. PMID: 35851087
2. Khan IA & Moretto M (2022). "Nfkbid-mediated humoral immunity during secondary toxoplasmosis". *Trends Parasitol*. PMID: 35190281
3. Kang L et al. (2023). "Hsa_circ_0007321 regulates Zika virus replication through miR-492/NFKBID/NF-κB signaling pathway". *J Virol*. PMID: 38051045
4. Kübelbeck T et al. (2025). "Regulation and Function of the Atypical IκBs-Bcl-3, IκB(NS), and IκBζ-in Lymphocytes and Autoimmunity". *Eur J Immunol*. PMID: 40359334
5. Souza SP et al. (2021). "Genetic mapping reveals Nfkbid as a central regulator of humoral immunity to Toxoplasma gondii". *PLoS Pathog*. PMID: 34871323
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 313 aa |
| PDB 条目数 | 0 |
| UniProt 注释结构域数 | 7 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NFKBID/NFKBID-PAE.png]]

**评价**: 无 PDB 结构，AlphaFold 预测可用，新颖蛋白基线分

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | Ankyrin_rpt |
| InterPro | Ankyrin_rpt-contain_sf |
| Pfam | Ank_2 |
| Pfam | Ank_5 |
| SMART | ANK |
| PROSITE | ANK_REP_REGION |
| PROSITE | ANK_REPEAT |

**染色质调控潜力分析**: 7 个结构域注释，新颖蛋白基线（存在新域发现潜力）

#### 3.6 PPI 网络

**实验验证互作** (IntAct):

IntAct 实验互作: 0 条

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| REL | 0 |  | 否 |
| NFKB2 | 0 |  | 否 |
| NFKBIB | 0 |  | 否 |
| NFKB1 | 0 |  | 否 |
| RELB | 0 |  | 否 |
| RELA | 0 |  | 否 |
| NFKBIE | 0 |  | 否 |
| ZC3H12A | 0 |  | 否 |
| SS18 | 0 |  | 否 |
| NFKBIA | 0 |  | 否 |

**已知复合体成员** (GO Cellular Component):

—

**PPI 互证分析**: STRING 15 partners，调控比例较低

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 0 entries | 仅预测 |
| 结构域 | UniProt / InterPro / Pfam | 7 domains | 多库一致 |
| PPI | STRING + IntAct | 15 STRING + 0 IntAct | 单源 |
| 定位 | Protein Atlas / UniProt / GO | Nucleus | 多源一致 |

**互证加分明细**:
核定位: UniProt + GO 双库一致 (+1)
结构域: 多库注释一致 (+0.5)
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ★★★☆☆ (3/5)

**核心优势**:
1. 新颖性: PubMed 76 篇，有一定研究空间
2. 核定位: 明确核定位

**风险/不确定性**:
1. HPA IF 数据可进一步验证
2. 无 PDB 实验结构，仅 AlphaFold 预测

**下一步建议**:
- [ ] 验证核定位: IF 实验确认亚核定位
- [ ] 功能研究: 基于 PPI 网络设计功能实验
- [ ] 结构分析: AlphaFold 预测为基础，设计突变实验

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=NFKBID
- Protein Atlas: https://www.proteinatlas.org/ENSG00000167604-NFKBID
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22NFKBID%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q8NI38
- STRING: https://string-db.org/network/9606.ENSG00000167604
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NI38


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[NFKBID-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NFKBID/NFKBID-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8NI38 |
| SMART | SM00248; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR002110;IPR036770; |
| Pfam | PF12796;PF13857; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000167604-NFKBID/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ANXA11 | Intact | false |
| ARHGEF2 | Intact | false |
| BEX2 | Intact | false |
| C1orf109 | Intact | false |
| C1orf94 | Intact | false |
| C4orf45 | Intact | false |
| CRYBA2 | Intact | false |
| CTRC | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
