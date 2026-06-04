---
type: protein-evaluation
gene: "BRPF1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BRPF1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BRPF1 / BR140 |
| 蛋白名称 | Peregrin |
| 蛋白大小 | 1214 aa / 137.5 kDa |
| UniProt ID | P55201 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Chromosome; Cytoplasm |
| 蛋白大小 | 5/10 | ×1 | 5 | 1214 aa / 137.5 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=92 篇 (≤100→2) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.5; PDB: 2D9E, 2RS9, 2X35, 2X4W, 2X4X, 2X4Y, 3L42 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001487, IPR036427, IPR018359, IPR042008, IPR049 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **86.0/180** | |
| **归一化总分** | | | **47.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus; Chromosome; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- histone acetyltransferase complex (GO:0000123)
- MOZ/MORF histone acetyltransferase complex (GO:0070776)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 92 |
| PubMed broad count | 129 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BR140 |

**关键文献**:
1. Essential gene screening identifies the bromodomain-containing protein BRPF1 as a new actionable target for endocrine therapy-resistant breast cancers.. *Molecular cancer*. PMID: 39113071
2. Structural and biophysical characterization of the nucleosome-binding PZP domain.. *STAR protocols*. PMID: 33982013
3. BRPF1-KAT6A/KAT6B Complex: Molecular Structure, Biological Function and Human Disease.. *Cancers*. PMID: 36077605
4. Multifunctional acyltransferase HBO1: a key regulatory factor for cellular functions.. *Cellular & molecular biology letters*. PMID: 39543485
5. The Phenotypic and Genotypic Spectrum of BRPF1-Related Disorder: 29 New Patients and Literature Review.. *Clinical genetics*. PMID: 39837771

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.5 |
| 高置信度残基 (pLDDT>90) 占比 | 27.2% |
| 置信残基 (pLDDT 70-90) 占比 | 29.5% |
| 中等置信 (pLDDT 50-70) 占比 | 9.4% |
| 低置信 (pLDDT<50) 占比 | 33.9% |
| 有序区域 (pLDDT>70) 占比 | 56.7% |
| 可用 PDB 条目 | 2D9E, 2RS9, 2X35, 2X4W, 2X4X, 2X4Y, 3L42, 3MO8, 4LC2, 4QYD |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=67.5），有序残基占 56.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001487, IPR036427, IPR018359, IPR042008, IPR049583; Pfam: PF00439, PF10513, PF13831 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MEAF6 | 0.999 | 0.786 | — |
| ING5 | 0.999 | 0.751 | — |
| KAT6A | 0.999 | 0.795 | — |
| KAT6B | 0.999 | 0.441 | — |
| KAT7 | 0.997 | 0.621 | — |
| H3C13 | 0.978 | 0.908 | — |
| H3C12 | 0.978 | 0.908 | — |
| H3-2 | 0.965 | 0.908 | — |
| H3-4 | 0.965 | 0.908 | — |
| BRPF3 | 0.964 | 0.594 | — |

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
| 三维结构 | AlphaFold pLDDT=67.5 + PDB: 2D9E, 2RS9, 2X35, 2X4W, 2X4X,  | pLDDT=67.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome; Cytoplasm / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐

**核心优势**:
1. BRPF1 — Peregrin，研究基础较多，新颖性有限。
2. 蛋白大小1214 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 92 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=67.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P55201
- Protein Atlas: https://www.proteinatlas.org/ENSG00000156983-BRPF1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BRPF1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P55201
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
