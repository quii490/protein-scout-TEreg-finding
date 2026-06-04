---
type: protein-evaluation
gene: "UVSSA"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## UVSSA 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | UVSSA / -- |
| 蛋白全称 | UV-stimulated scaffold protein A |
| 蛋白大小 | 709 aa |
| UniProt ID | Q2YD98 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/chromatin/UVSSA/IF_images/PC-3_1.jpg|PC-3]]
![[Projects/TEreg-finding/protein-interested/detail/chromatin/UVSSA/IF_images/U2OS_1.jpg|U2OS]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 6/10 | ×4 | **24** | Nuclear + cyto, some evidence |
| 蛋白大小 | 10/10 | ×1 | **10** | 709 aa，处于理想范围 |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed 49 篇，高度新颖 |
| 三维结构 | 10/10 | ×3 | **30** | 12 个 PDB 结构 |
| 调控结构域 | 7/10 | ×2 | **14** | 7 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+1.0** | PDB + AlphaFold 结构互证 (+0.5); 多库结构域一致 (+0.5) |
|  | **原始总分** |  | **114.5/183** | **114.0/183** |  |  |  |
|  | **归一化总分** |  | **62.6/100** | **62.3/100** |  |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| HPA IF | 暂无数据（待细胞分析），核定位基于 UniProt + GO 注释 | -- |
| UniProt | Chromosome | 实验证据/预测 |
| GO-CC | N/A | N/A |

**结论**: Nuclear + cyto, some evidence

#### 3.2 蛋白大小评估

**评价**: 709 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 49 |

**评价**: PubMed 49 篇，高度新颖

**关键文献**:
1. Nieto Moreno N et al. (2023). "Transcription-Coupled Nucleotide Excision Repair and the Transcriptional Response to UV-Induced DNA Damage". *Annu Rev Biochem*. PMID: 37040775
2. Mevissen TET et al. (2024). "STK19 positions TFIIH for cell-free transcription-coupled DNA repair". *Cell*. PMID: 39547228
3. van den Heuvel D et al. (2024). "STK19 facilitates the clearance of lesion-stalled RNAPII during transcription-coupled DNA repair". *Cell*. PMID: 39547229
4. Ramadhin AR et al. (2024). "STK19 drives transcription-coupled repair by stimulating repair complex stability, RNA Pol II ubiquitylation, and TFIIH recruitment". *Mol Cell*. PMID: 39547223
5. van Sluis M et al. (2024). "Transcription-coupled DNA-protein crosslink repair by CSB and CRL4(CSA)-mediated degradation". *Nat Cell Biol*. PMID: 38600236
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 709 aa |
| PDB 条数 | 12 |
| 已注释结构域 | 7 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/chromatin/UVSSA/UVSSA-PAE.png]]

**评价**: 12 个 PDB 结构

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | ENTH_VHS |
| InterPro | UVSSA |
| InterPro | UVSSA_C |
| InterPro | UVSSA_N_a-solenoid_rpt |
| Pfam | DUF2043 |
| Pfam | UVSSA_N |
| PROSITE | ZF_UVSSA |

**染色质调控潜力分析**: 7 个已注释结构域，新颖蛋白基线水平

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

- F:chromatin-protein adaptor activity (GO:0140463, IDA:UniProtKB)
- F:RNA polymerase II complex binding (GO:0000993, IDA:UniProtKB)

**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 12 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 7 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
PDB + AlphaFold 结构互证 (+0.5)
多库结构域一致 (+0.5)
**总计**: +1.0

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 49 篇，高度新颖
2. 核定位: 部分核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 12 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=UVSSA
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163945-UVSSA
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22UVSSA%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q2YD98
- STRING: https://string-db.org/network/9606.ENSG00000163945
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q2YD98


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[UVSSA-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/chromatin/UVSSA/UVSSA-PAE.png]]




