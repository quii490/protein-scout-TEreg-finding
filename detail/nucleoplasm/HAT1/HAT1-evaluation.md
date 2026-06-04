---
type: protein-evaluation
gene: "HAT1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## HAT1 — REJECTED (研究热度过高 (PubMed strict=233，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HAT1 / KAT1 |
| 蛋白名称 | Histone acetyltransferase type B catalytic subunit |
| 蛋白大小 | 419 aa / 49.5 kDa |
| UniProt ID | O14929 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus matrix; Mitochondrion; Cytoplasm; Nucleus; Nucleus m |
| 蛋白大小 | 10/10 | ×1 | 10 | 419 aa / 49.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=233 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=92.8; PDB: 2P0W, 6VO5, 9MJG |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR016181, IPR048776, IPR019467, IPR037113, IPR017 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **93.0/180** | |
| **归一化总分** | | | **51.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus matrix; Mitochondrion; Cytoplasm; Nucleus; Nucleus matrix; Nucleus, nucleoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- chromosome, telomeric region (GO:0000781)
- mitochondrion (GO:0005739)
- nuclear matrix (GO:0016363)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- protein-containing complex (GO:0032991)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 233 |
| PubMed broad count | 378 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KAT1 |

**关键文献**:
1. Histone acetyltransferase 1 is a succinyltransferase for histones and non-histones and promotes tumorigenesis.. *EMBO reports*. PMID: 33372411
2. HAT1/HDAC2 mediated ACSL4 acetylation confers radiosensitivity by inducing ferroptosis in nasopharyngeal carcinoma.. *Cell death & disease*. PMID: 40050614
3. The Nuclear Localization of ACLY Guards Early Embryo Development Through Recruiting P300 and HAT1 to Promote Histone Acetylation and Transcription.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 40470746
4. Understanding HAT1: A Comprehensive Review of Noncanonical Roles and Connection with Disease.. *Genes*. PMID: 37107673
5. HAT1: Landscape of Biological Function and Role in Cancer.. *Cells*. PMID: 37048148

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.8 |
| 高置信度残基 (pLDDT>90) 占比 | 80.2% |
| 置信残基 (pLDDT 70-90) 占比 | 15.5% |
| 中等置信 (pLDDT 50-70) 占比 | 4.3% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 95.7% |
| 可用 PDB 条目 | 2P0W, 6VO5, 9MJG |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（2P0W, 6VO5, 9MJG）+ AlphaFold高质量预测（pLDDT=92.8），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016181, IPR048776, IPR019467, IPR037113, IPR017380; Pfam: PF21183, PF10394 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RBBP7 | 0.999 | 0.973 | — |
| H4C6 | 0.998 | 0.903 | — |
| NASP | 0.997 | 0.986 | — |
| H3C12 | 0.995 | 0.842 | — |
| H4C7 | 0.992 | 0.434 | — |
| RBBP4 | 0.982 | 0.945 | — |
| H3-3B | 0.978 | 0.587 | — |
| H3-4 | 0.973 | 0.486 | — |
| ORC3 | 0.973 | 0.954 | — |
| ORC5 | 0.970 | 0.954 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Q8LBA8 | psi-mi:"MI:0018"(two hybrid) | doi:10.1016/j.molp.2022.09.004 |
| NOT9B | psi-mi:"MI:1356"(validated two hybrid) | doi:10.1038/nmeth.4343|pubmed: |
| TCP9 | psi-mi:"MI:1356"(validated two hybrid) | doi:10.1038/nmeth.4343|pubmed: |
| HAT4 | psi-mi:"MI:1356"(validated two hybrid) | doi:10.1038/nmeth.4343|pubmed: |
| HAT2 | psi-mi:"MI:1356"(validated two hybrid) | doi:10.1038/nmeth.4343|pubmed: |
| HAT22 | psi-mi:"MI:1356"(validated two hybrid) | doi:10.1038/nmeth.4343|pubmed: |
| HAT9 | psi-mi:"MI:0397"(two hybrid array) | doi:10.1038/nmeth.4343|pubmed: |
| TCP4 | psi-mi:"MI:0397"(two hybrid array) | doi:10.1038/nmeth.4343|pubmed: |
| ATHB-4 | psi-mi:"MI:1356"(validated two hybrid) | doi:10.1038/nmeth.4343|pubmed: |
| HAT3 | psi-mi:"MI:1356"(validated two hybrid) | doi:10.1038/nmeth.4343|pubmed: |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.8 + PDB: 2P0W, 6VO5, 9MJG | pLDDT=92.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus matrix; Mitochondrion; Cytoplasm; Nucleus; / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. HAT1 — Histone acetyltransferase type B catalytic subunit，研究基础较多，新颖性有限。
2. 蛋白大小419 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 233 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 233 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O14929
- Protein Atlas: https://www.proteinatlas.org/ENSG00000128708-HAT1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HAT1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O14929
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/HAT1/IF_images/A-431_1.jpg]]
![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/HAT1/IF_images/U-251MG_1.jpg]]


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/HAT1/HAT1-PAE.png]]


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/HAT1/HAT1-PAE.png]]
