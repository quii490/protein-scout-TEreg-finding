---
type: protein-evaluation
gene: "TBX22"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TBX22 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TBX22 / TBOX22 |
| 蛋白名称 | T-box transcription factor TBX22 |
| 蛋白大小 | 520 aa / 57.9 kDa |
| UniProt ID | Q9Y458 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 520 aa / 57.9 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=49 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=58.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR008967, IPR046360, IPR036960, IPR001699, IPR018 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **114.0/180** | |
| **归一化总分** | | | **63.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 49 |
| PubMed broad count | 71 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TBOX22 |

**关键文献**:
1. TBX22 and tongue-tie.. *The Cleft palate-craniofacial journal : official publication of the American Cleft Palate-Craniofacial Association*. PMID: 21905918
2. Regulation of Tbx22 during facial and palatal development.. *Developmental dynamics : an official publication of the American Association of Anatomists*. PMID: 20845426
3. Isolation and developmental expression analysis of Tbx22, the mouse homolog of the human X-linked cleft palate gene.. *Developmental dynamics : an official publication of the American Association of Anatomists*. PMID: 12412015
4. T-Box Transcription Factor 22 Is an Immune Microenvironment-Related Biomarker Associated With the BRAF (V600E) Mutation in Papillary Thyroid Carcinoma.. *Frontiers in cell and developmental biology*. PMID: 33392186
5. Essential role of Msx1 in regulating anterior-posterior patterning of the secondary palate in mice.. *Journal of genetics and genomics = Yi chuan xue bao*. PMID: 34857492

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 58.4 |
| 高置信度残基 (pLDDT>90) 占比 | 29.6% |
| 置信残基 (pLDDT 70-90) 占比 | 6.7% |
| 中等置信 (pLDDT 50-70) 占比 | 6.9% |
| 低置信 (pLDDT<50) 占比 | 56.7% |
| 有序区域 (pLDDT>70) 占比 | 36.3% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=58.4），有序残基占 36.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008967, IPR046360, IPR036960, IPR001699, IPR018186; Pfam: PF00907 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CLPP | 0.994 | 0.000 | — |
| CLPX | 0.961 | 0.000 | — |
| CLPS | 0.940 | 0.000 | — |
| CLPB | 0.868 | 0.000 | — |
| SP100 | 0.668 | 0.045 | — |
| MSX1 | 0.641 | 0.071 | — |
| IRF6 | 0.620 | 0.000 | — |
| BARX1 | 0.619 | 0.054 | — |
| RGS9BP | 0.610 | 0.000 | — |
| SUMO1 | 0.600 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HSP90AB1 | psi-mi:"MI:0729"(luminescence based mammalian inte | imex:IM-17906|pubmed:22939624| |
| GOPC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ENSG00000122367 | psi-mi:"MI:0432"(one hybrid) | imex:IM-26689|pubmed:31481462 |
| ENSG00000183354 | psi-mi:"MI:0432"(one hybrid) | imex:IM-26689|pubmed:31481462 |
| ENSG00000283930 | psi-mi:"MI:0432"(one hybrid) | imex:IM-26689|pubmed:31481462 |
| ENSG00000148120 | psi-mi:"MI:0432"(one hybrid) | imex:IM-26689|pubmed:31481462 |
| ENSG00000177694 | psi-mi:"MI:0432"(one hybrid) | imex:IM-26689|pubmed:31481462 |
| - | psi-mi:"MI:0432"(one hybrid) | imex:IM-26689|pubmed:31481462 |
| VENTX | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| PITX1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=58.4 + PDB: 无 | pLDDT=58.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TBX22 — T-box transcription factor TBX22，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小520 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 49 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=58.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y458
- Protein Atlas: https://www.proteinatlas.org/ENSG00000122145-TBX22/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TBX22
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y458
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
