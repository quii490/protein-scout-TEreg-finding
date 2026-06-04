---
type: protein-evaluation
gene: "EED"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EED — REJECTED (研究热度过高 (PubMed strict=558，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EED |
| 蛋白名称 | Polycomb protein EED |
| 蛋白大小 | 441 aa / 50.2 kDa |
| UniProt ID | O75530 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus; Chromosome |
| 蛋白大小 | 10/10 | ×1 | 10 | 441 aa / 50.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=558 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=86.5; PDB: 3IIW, 3IIY, 3IJ0, 3IJ1, 3IJC, 3JPX, 3JZG |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR051243, IPR015943, IPR019775, IPR036322, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **95.5/180** | |
| **归一化总分** | | | **53.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Nucleus; Chromosome | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin silencing complex (GO:0005677)
- cytosol (GO:0005829)
- ESC/E(Z) complex (GO:0035098)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- pronucleus (GO:0045120)
- sex chromatin (GO:0001739)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 558 |
| PubMed broad count | 1970 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Identification of immune-related genes in diagnosing atherosclerosis with rheumatoid arthritis through bioinformatics analysis and machine learning.. *Frontiers in immunology*. PMID: 36969166
2. Role of histone H3 lysine 27 methylation in Polycomb-group silencing.. *Science (New York, N.Y.)*. PMID: 12351676
3. EED-Related Overgrowth.. **. PMID: 30973693
4. Gene-repressing epigenetic reader EED unexpectedly enhances cyclinD1 gene activation.. *Molecular therapy. Nucleic acids*. PMID: 36923952
5. AI-driven designed protein epigenomics.. *Clinical research in oncology*. PMID: 38037660

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.5 |
| 高置信度残基 (pLDDT>90) 占比 | 79.1% |
| 置信残基 (pLDDT 70-90) 占比 | 3.4% |
| 中等置信 (pLDDT 50-70) 占比 | 0.5% |
| 低置信 (pLDDT<50) 占比 | 17.0% |
| 有序区域 (pLDDT>70) 占比 | 82.5% |
| 可用 PDB 条目 | 3IIW, 3IIY, 3IJ0, 3IJ1, 3IJC, 3JPX, 3JZG, 3JZH, 3JZN, 3K26 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（3IIW, 3IIY, 3IJ0, 3IJ1, 3IJC, 3JPX, 3JZG, 3JZH, 3JZN, 3K26）+ AlphaFold极高置信度预测（pLDDT=86.5），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051243, IPR015943, IPR019775, IPR036322, IPR001680; Pfam: PF00400 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EZH1 | 0.999 | 0.997 | — |
| JARID2 | 0.999 | 0.974 | — |
| AEBP2 | 0.999 | 0.984 | — |
| RBBP4 | 0.999 | 0.989 | — |
| RBBP7 | 0.999 | 0.916 | — |
| SUZ12 | 0.999 | 0.997 | — |
| EZH2 | 0.999 | 0.998 | — |
| RNF2 | 0.997 | 0.516 | — |
| BMI1 | 0.989 | 0.583 | — |
| PHC1 | 0.989 | 0.095 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.5 + PDB: 3IIW, 3IIY, 3IJ0, 3IJ1, 3IJC,  | pLDDT=86.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. EED — Polycomb protein EED，研究基础较多，新颖性有限。
2. 蛋白大小441 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 558 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 558 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75530
- Protein Atlas: https://www.proteinatlas.org/ENSG00000074266-EED/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EED
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75530
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
