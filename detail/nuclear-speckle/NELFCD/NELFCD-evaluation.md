---
type: protein-evaluation
gene: "NELFCD"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NELFCD 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | NELFCD / HSPC130|TH1|NELF-C|NELF-D |
| 蛋白名称 | Negative elongation factor C/D |
| 蛋白大小 | 590 aa |
| UniProt ID | Q8IXH7 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/NELFCD/IF_images/NIH-3T3_1.jpg|NIH 3T3]]
![[Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/NELFCD/IF_images/MCF-7_1.jpg|MCF-7]]

### 2. 评分总览

| 维度 | 得分 | 加权 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | **24** | 核+胞质，有核定位证据 |
| 📏 蛋白大小 | 10/10 | ×1 | **10** | 590 aa，适合生化实验和结构解析 |
| 🆕 研究新颖性 | 10/10 | ×5 | **50** | PubMed 14篇，极度新颖 |
| 🏗️ 三维结构 | 10/10 | ×3 | **30** | 16 个 PDB 实验结构，实验验证充分 |
| 🧬 调控结构域 | 7/10 | ×2 | **14** | 2 个结构域，新颖蛋白基线 |
| 🔗 PPI 网络 | 4/10 | ×3 | **12** | STRING 15 partners，调控比例较低 |
| ➕ 互证加分 | — | — | **+1.0** | 三维结构: AlphaFold + PDB 双源 (+0.5); PPI: IntAct + STRING 双源 (+0.5) |
| **原始总分** |  |  | **140.5/183** |  |
| **归一化总分** |  |  | **76.8/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_conserved_high_confidence | 高置信度保守 |
| Protein Atlas (IF) | 暂无数据（HPA IF 图像已本地嵌入。

| UniProt | N/A | 实验/预测 |
| GO Cellular Component | N/A | N/A |

**结论**: 核+胞质，有核定位证据

#### 3.2 蛋白大小评估

**评价**: 590 aa，590 aa，适合生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 14 |
| 核定位分数 (weighted max) | 6 |
| Research hotness | 4.6549 |

**关键文献**:
1. Hong et al. (2025). "Dissecting immune cell-specific genetics in migraine: a multi-omics framework for target discovery and therapeutic prioritization.". *J Headache Pain*. PMID: 41029193
2. Nakayama et al. (2026). "NELF prevents transcriptional readthrough into DNA replication zones in cancer cells.". *EMBO Rep*. PMID: 41721097
3. Nakayama et al. (2024). "NELF coordinates Pol II transcription termination and DNA replication initiation.". *bioRxiv*. PMID: 38352431
4. Song et al. (2018). "Overexpression of NELFCD promotes colorectal cancer cells proliferation, migration, and invasion.". *Onco Targets Ther*. PMID: 30584332
5. Zhao et al. (2024). "Whole-genome resequencing of native and imported dairy goat identifies genes associated with productivity and immunity.". *Front Vet Sci*. PMID: 39040818
**评价**: PubMed 14篇，极度新颖

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 590 aa |
| PDB 条目数 | 16 |
| UniProt 注释结构域数 | 2 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/NELFCD/NELFCD-PAE.png]]

**评价**: 16 个 PDB 实验结构，实验验证充分

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | TH1 |
| Pfam | TH1 |

**染色质调控潜力分析**: 2 个结构域，新颖蛋白基线

#### 3.6 PPI 网络

**实验验证互作** (IntAct):

IntAct 实验互作: 84 条

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| NELFA | 0 |  | 否 |
| NELFE | 0 |  | 否 |
| NELFB | 0 |  | 否 |
| SUPT5H | 0 |  | 否 |
| SUPT4H1 | 0 |  | 否 |
| POLR2A | 0 |  | 否 |
| NCBP1 | 0 |  | 否 |
| POLR2B | 0 |  | 否 |
| POLR2C | 0 |  | 否 |
| PCCB | 0 |  | 否 |

**已知复合体成员** (GO Cellular Component):

- C:NELF complex (GO:0032021, IDA:UniProtKB)

**PPI 互证分析**: STRING 15 partners，调控比例较低

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 16 entries | 一致 |
| 结构域 | UniProt / InterPro / Pfam | 2 domains | 多库一致 |
| PPI | STRING + IntAct | 15 STRING + 84 IntAct | 双源 |
| 定位 | Protein Atlas / UniProt / GO | Nucleus | 多源一致 |

**互证加分明细**:
三维结构: AlphaFold + PDB 双源 (+0.5)
PPI: IntAct + STRING 双源 (+0.5)
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ★★★★☆ (4/5)

**核心优势**:
1. 新颖性: PubMed 14 篇，极度新颖
2. 核定位: 部分核定位

**风险/不确定性**:
1. HPA IF 数据可进一步验证
2. 16 PDB 结构可用

**下一步建议**:
- [ ] 验证核定位: IF 实验确认亚核定位
- [ ] 功能研究: 基于 PPI 网络设计功能实验
- [ ] 结构分析: 基于 PDB 结构设计功能实验

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=NELFCD
- Protein Atlas: https://www.proteinatlas.org/ENSG00000101158-NELFCD
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22NELFCD%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q8IXH7
- STRING: https://string-db.org/network/9606.ENSG00000101158
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IXH7


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[NELFCD-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/NELFCD/NELFCD-PAE.png]]


