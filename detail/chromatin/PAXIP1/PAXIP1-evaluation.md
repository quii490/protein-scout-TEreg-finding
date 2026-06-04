---
type: protein-evaluation
gene: "PAXIP1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PAXIP1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | PAXIP1 / CAGF29|CAGF28|TNRC2|PTIP |
| 蛋白全称 | PAX-interacting protein 1 |
| 蛋白大小 | 1069 aa |
| UniProt ID | Q6ZW49 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 8/10 | ×1 | **8** | 1069 aa，尚可接受 |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed 53 篇，中等研究热度 |
| 三维结构 | 8/10 | ×3 | **24** | 1 个 PDB 结构 + AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 9 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+2.0** | UniProt + GO 核定位互证 (+1); PDB + AlphaFold 结构互证 (+0.5); 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **115/183** |  |
| **归一化总分** |  |  | **62.8/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| HPA IF | Nucleoplasm, Vesicles (HPA016950, Approved) | A-431, U-251MG |
| UniProt | Nucleus matrix, Chromosome | 实验证据/预测 |
| GO-CC | GO:0005634 | IBA|IEA |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/chromatin/PAXIP1/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/chromatin/PAXIP1/IF_images/U-251MG_1.jpg|U-251MG]]

**结论**: Protein Atlas IF (HPA016950, Approved) 确认定位于 Nucleoplasm 和 Vesicles，A-431 和 U-251MG 细胞系均显示清晰的核质染色。UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 1069 aa，尚可接受

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 53 |

**关键文献**:
1. Shen et al. (2025). "Targeting pancreatic cancer glutamine dependency confers vulnerability to GPX4-dependent ferroptosis.". *Cell Rep Med*. PMID: 39879992
2. van et al. (2023). "CRISPR screens in sister chromatid cohesion defective cells reveal PAXIP1-PAGR1 as regulator of chromatin association of cohesin.". *Nucleic Acids Res*. PMID: 37702151
3. Ashkin et al. (2025). "A STAG2-PAXIP1/PAGR1 axis suppresses lung tumorigenesis.". *J Exp Med*. PMID: 39652422
4. Harvey-Jones et al. (2024). "Longitudinal profiling identifies co-occurring BRCA1/2 reversions, TP53BP1, RIF1 and PAXIP1 mutations in PARP inhibitor-resistant advanced breast cancer.". *Ann Oncol*. PMID: 38244928
5. Ding et al. (2025). "Glucose-Responsive PAGR1-Regulated Skeletal Muscle Gene Program Controls Systemic Glucose Homeostasis and Hepatic Metabolism.". *Adv Sci (Weinh)*. PMID: 40703063
**评价**: PubMed 53 篇，中等研究热度

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 1069 aa |
| PDB 条数 | 1 |
| 已注释结构域 | 9 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/chromatin/PAXIP1/PAXIP1-PAE.png]]

**评价**: 1 个 PDB 结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | BRCT_dom |
| InterPro | BRCT_dom_sf |
| InterPro | DDR_Transcriptional_Reg |
| Pfam | BRCT |
| Pfam | BRCT_2 |
| Pfam | PTCB-BRCT |
| Pfam | RTT107_BRCT_5 |
| SMART | BRCT |
| PROSITE | BRCT |

**染色质调控潜力分析**: 9 个已注释结构域，新颖蛋白基线水平

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

- C:histone methyltransferase complex (GO:0035097, IDA:UniProtKB)
- C:MLL3/4 complex (GO:0044666, IDA:UniProtKB)
- P:chromatin remodeling (GO:0006338, IDA:UniProtKB)


**PPI 互证分析**:
- （待补充：综合 STRING、IntAct 和 GO 数据库的互作信息，分析 PPI 网络的一致性）
**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 1 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 9 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
UniProt + GO 核定位互证 (+1)
PDB + AlphaFold 结构互证 (+0.5)
多库结构域一致 (+0.5)
**总计**: +2.0

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 53 篇，中等研究热度
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 1 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 
### IF图像状态

| 项目 | 内容 |
|---|---|
| Ensembl | ENSG00000157212 |
| 蛋白证据 | Evidence at protein level |
| HPA抗体 | HPA016950 |
| IF可靠性 | Approved |
| 主定位 | Nucleoplasm, Vesicles |
| 已下载细胞系 | A-431, U-251MG |
| HPA链接 | https://www.proteinatlas.org/ENSG00000157212-PAXIP1/subcellular |

> **IF状态**: downloaded

数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=PAXIP1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000157212-PAXIP1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22PAXIP1%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q6ZW49
- STRING: https://string-db.org/network/9606.ENSG00000157212
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6ZW49


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[PAXIP1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/chromatin/PAXIP1/PAXIP1-PAE.png]]




