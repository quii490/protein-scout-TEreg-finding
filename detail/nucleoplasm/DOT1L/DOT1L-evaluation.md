---
type: protein-evaluation
gene: "DOT1L"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DOT1L — REJECTED (研究热度过高 (PubMed strict=435，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DOT1L / KIAA1814, KMT4 |
| 蛋白名称 | Histone-lysine N-methyltransferase, H3 lysine-79 specific |
| 蛋白大小 | 1537 aa / 164.9 kDa |
| UniProt ID | Q8TEK3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 5/10 | ×1 | 5 | 1537 aa / 164.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=435 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=52.5; PDB: 1NW3, 2MV7, 3QOW, 3QOX, 3SR4, 3SX0, 3UWP |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR025789, IPR021169, IPR030445, IPR029063; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **76.5/180** | |
| **归一化总分** | | | **42.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromosome, telomeric region (GO:0000781)
- cytoplasm (GO:0005737)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- protein-containing complex (GO:0032991)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 435 |
| PubMed broad count | 740 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1814, KMT4 |

**关键文献**:
1. An expanded lexicon for the ubiquitin code.. *Nature reviews. Molecular cell biology*. PMID: 36284179
2. A Menin-MLL Inhibitor Induces Specific Chromatin Changes and Eradicates Disease in Models of MLL-Rearranged Leukemia.. *Cancer cell*. PMID: 31821784
3. STING mediates hepatocyte pyroptosis in liver fibrosis by Epigenetically activating the NLRP3 inflammasome.. *Redox biology*. PMID: 37018971
4. DOT1L-mediated RAP80 methylation promotes BRCA1 recruitment to elicit DNA repair.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 39172790
5. PARP1-DOT1L transcription axis drives acquired resistance to PARP inhibitor in ovarian cancer.. *Molecular cancer*. PMID: 38778348

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 52.5 |
| 高置信度残基 (pLDDT>90) 占比 | 18.3% |
| 置信残基 (pLDDT 70-90) 占比 | 13.0% |
| 中等置信 (pLDDT 50-70) 占比 | 4.0% |
| 低置信 (pLDDT<50) 占比 | 64.7% |
| 有序区域 (pLDDT>70) 占比 | 31.3% |
| 可用 PDB 条目 | 1NW3, 2MV7, 3QOW, 3QOX, 3SR4, 3SX0, 3UWP, 4EK9, 4EKG, 4EKI |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=52.5），有序残基占 31.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR025789, IPR021169, IPR030445, IPR029063; Pfam: PF08123 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MLLT10 | 0.999 | 0.978 | — |
| MLLT3 | 0.998 | 0.873 | — |
| H3C13 | 0.997 | 0.943 | — |
| H3C12 | 0.996 | 0.923 | — |
| MLLT1 | 0.995 | 0.736 | — |
| H4C6 | 0.980 | 0.926 | — |
| MLLT6 | 0.971 | 0.844 | — |
| H3C14 | 0.968 | 0.960 | — |
| H2BC11 | 0.964 | 0.907 | — |
| H2BC12 | 0.964 | 0.907 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000381657.3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:22094252|imex:IM-16588 |
| - | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:22094252|imex:IM-16588 |
| MLLT3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-13603|pubmed:20153263 |
| MLLT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-13603|pubmed:20153263 |
| HMOX2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| MLLT6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Cbx1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| CKAP5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Scai | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| KIF24 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=52.5 + PDB: 1NW3, 2MV7, 3QOW, 3QOX, 3SR4,  | pLDDT=52.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. DOT1L — Histone-lysine N-methyltransferase, H3 lysine-79 specific，研究基础较多，新颖性有限。
2. 蛋白大小1537 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 435 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=52.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 435 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TEK3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000104885-DOT1L/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DOT1L
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TEK3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
