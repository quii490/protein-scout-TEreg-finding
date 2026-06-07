---
type: protein-evaluation
gene: "NCOA5"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NCOA5 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | NCOA5 / bA465L10.6|CIA |
| 蛋白名称 | Nuclear receptor coactivator 5 |
| 蛋白大小 | 579 aa |
| UniProt ID | Q9HCD5 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 加权 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 8/10 | ×4 | **32** | UniProt Nucleus，中等可信度 |
| 📏 蛋白大小 | 10/10 | ×1 | **10** | 579 aa，适合生化实验和结构解析 |
| 🆕 研究新颖性 | 6/10 | ×5 | 30 | PubMed 42篇，非常新颖 |
| 🏗️ 三维结构 | 8/10 | ×3 | **24** | 4 个 PDB 实验结构 + AlphaFold 预测 |
| 🧬 调控结构域 | 7/10 | ×2 | **14** | 2 个结构域，新颖蛋白基线 |
| 🔗 PPI 网络 | 4/10 | ×3 | **12** | STRING 15 partners，调控比例较低 |
| ➕ 互证加分 | — | — | **+1.5** | 核定位: UniProt + GO 双库一致 (+1); 三维结构: AlphaFold + PDB 双源 (+0.5) |
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
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NCOA5/IF_images/A-431_HPA050231_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NCOA5/IF_images/MCF-7_HPA050231_2.jpg|MCF-7]]

**结论**: UniProt Nucleus，中等可信度

#### 3.2 蛋白大小评估

**评价**: 579 aa，579 aa，适合生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 42 |
| 核定位分数 (weighted max) | 6 |
| Research hotness | 5.9341 |

**评价**: PubMed 42篇，非常新颖

**关键文献**:
1. Cheng X et al. (2026). "A genome-wide siRNA screen identifies previously unknown proviral and antiviral host factors in HBV infection". *J Hepatol*. PMID: 41314348
2. Zhang Y et al. (2023). "Hyperpolarization-activated cyclic nucleotide-gated cation channel 3 promotes HCC development in a female-biased manner". *Cell Rep*. PMID: 37733590
3. Gao S et al. (2025). "NCOA5 induces sorafenib resistance in hepatocellular carcinoma by inhibiting ferroptosis". *Cell Death Discov*. PMID: 40316542
4. Xia E et al. (2021). "Nuclear Receptor Coactivator 5 is Correlated with Progression in Breast Carcinoma". *Anticancer Agents Med Chem*. PMID: 33573580
5. Liu Y & Feng GS (2024). "NCOA5 Deficiency in Macrophages Provokes NASH and HCC". *Cell Mol Gastroenterol Hepatol*. PMID: 37935378
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 579 aa |
| PDB 条目数 | 4 |
| UniProt 注释结构域数 | 2 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NCOA5/NCOA5-PAE.png]]

**评价**: 4 个 PDB 实验结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | Anticodon-bd_dom_sf |
| InterPro | Nuc_rcpt_coact/corep |

**染色质调控潜力分析**: 2 个结构域，新颖蛋白基线

#### 3.6 PPI 网络

**实验验证互作** (IntAct):

IntAct 实验互作: 0 条

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| ESR2 | 0 |  | 否 |
| RANBP2 | 0 |  | 否 |
| NUP205 | 0 |  | 否 |
| NUP93 | 0 |  | 否 |
| NUP155 | 0 |  | 否 |
| NUP54 | 0 |  | 否 |
| NUP214 | 0 |  | 否 |
| SEC13 | 0 |  | 否 |
| NUP107 | 0 |  | 否 |
| RAE1 | 0 |  | 否 |

**已知复合体成员** (GO Cellular Component):

- F:chromatin binding (GO:0003682, IEA:Ensembl)

**PPI 互证分析**: STRING 15 partners，调控比例较低

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 4 entries | 一致 |
| 结构域 | UniProt / InterPro / Pfam | 2 domains | 多库一致 |
| PPI | STRING + IntAct | 15 STRING + 0 IntAct | 单源 |
| 定位 | Protein Atlas / UniProt / GO | Nucleus | 多源一致 |

**互证加分明细**:
核定位: UniProt + GO 双库一致 (+1)
三维结构: AlphaFold + PDB 双源 (+0.5)
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ★★★★☆ (4/5)

**核心优势**:
1. 新颖性: PubMed 42 篇，比较新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. HPA IF 数据可进一步验证
2. 4 PDB 结构可用

**下一步建议**:
- [ ] 验证核定位: IF 实验确认亚核定位
- [ ] 功能研究: 基于 PPI 网络设计功能实验
- [ ] 结构分析: 基于 PDB 结构设计功能实验

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=NCOA5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000124160-NCOA5
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22NCOA5%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q9HCD5
- STRING: https://string-db.org/network/9606.ENSG00000124160
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9HCD5


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[NCOA5-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NCOA5/NCOA5-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9HCD5 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR036621;IPR052600; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000124160-NCOA5/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ATG101 | Opencell | false |
| ATG13 | Opencell | false |
| CPSF6 | Opencell | false |
| HNRNPA1 | Biogrid | false |
| HTATIP2 | Biogrid | false |
| MATR3 | Biogrid | false |
| NXF1 | Biogrid | false |
| PAIP1 | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
