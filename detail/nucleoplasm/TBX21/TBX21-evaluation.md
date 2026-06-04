---
type: protein-evaluation
gene: "TBX21"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TBX21 — REJECTED (研究热度过高 (PubMed strict=431，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TBX21 / TBET, TBLYM |
| 蛋白名称 | T-box transcription factor TBX21 |
| 蛋白大小 | 535 aa / 58.3 kDa |
| UniProt ID | Q9UL17 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 535 aa / 58.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=431 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR008967, IPR046360, IPR036960, IPR001699, IPR018 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 9 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **84.0/180** | |
| **归一化总分** | | | **46.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- neuronal cell body (GO:0043025)
- nucleus (GO:0005634)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 431 |
| PubMed broad count | 726 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TBET, TBLYM |

**关键文献**:
1. Fusobacterium nucleatum facilitates anti-PD-1 therapy in microsatellite stable colorectal cancer.. *Cancer cell*. PMID: 39303724
2. Lung tumor-infiltrating T(reg) have divergent transcriptional profiles and function linked to checkpoint blockade response.. *Science immunology*. PMID: 37713507
3. Deciphering the immune modulation through deep transcriptomic profiling and therapeutic implications of DNA damage repair pattern in hepatocellular carcinoma.. *Cancer letters*. PMID: 38135208
4. Integrated analysis of ATAC-seq and RNA-seq reveals the transcriptional regulation network in SLE.. *International immunopharmacology*. PMID: 36738683
5. Rapamycin prevents spontaneous abortion by triggering decidual stromal cell autophagy-mediated NK cell residence.. *Autophagy*. PMID: 33030400

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.9 |
| 高置信度残基 (pLDDT>90) 占比 | 29.5% |
| 置信残基 (pLDDT 70-90) 占比 | 5.4% |
| 中等置信 (pLDDT 50-70) 占比 | 10.3% |
| 低置信 (pLDDT<50) 占比 | 54.8% |
| 有序区域 (pLDDT>70) 占比 | 34.9% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=60.9），有序残基占 34.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008967, IPR046360, IPR036960, IPR001699, IPR018186; Pfam: PF00907 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GATA3 | 0.997 | 0.311 | — |
| RUNX3 | 0.991 | 0.091 | — |
| RUNX1 | 0.974 | 0.091 | — |
| IFNG | 0.964 | 0.000 | — |
| CD4 | 0.947 | 0.000 | — |
| CD8A | 0.944 | 0.000 | — |
| IL17A | 0.937 | 0.000 | — |
| FOXP3 | 0.934 | 0.000 | — |
| KDM6B | 0.925 | 0.046 | — |
| GZMB | 0.918 | 0.046 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EXOC5 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| HOXC11 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| ZNF490 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| Alx4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| Dlx1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| Gsc | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| Pax9 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| Tead4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| Tlx3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 9
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 9 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.9 + PDB: 无 | pLDDT=60.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 9 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. TBX21 — T-box transcription factor TBX21，研究基础较多，新颖性有限。
2. 蛋白大小535 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 431 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=60.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 431 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UL17
- Protein Atlas: https://www.proteinatlas.org/ENSG00000073861-TBX21/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TBX21
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UL17
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
