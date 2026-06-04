---
type: protein-evaluation
gene: "LENG9"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LENG9 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LENG9 |
| 蛋白名称 | Leukocyte receptor cluster member 9 |
| 蛋白大小 | 501 aa / 53.2 kDa |
| UniProt ID | Q96B70 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli fibrillar center; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 501 aa / 53.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR019510, IPR009097, IPR042653, IPR040459, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 12 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **129.5/180** | |
| **归一化总分** | | | **71.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli fibrillar center | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6 |
| PubMed broad count | 8 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Salivary proteomic signatures in severe dental fluorosis.. *Scientific reports*. PMID: 39112609
2. Genome-wide identification of alternative splicing associated with histone deacetylase inhibitor in cutaneous T-cell lymphomas.. *Frontiers in genetics*. PMID: 36147491
3. Development and validation of a six-RNA binding proteins prognostic signature and candidate drugs for prostate cancer.. *Genomics*. PMID: 32882325
4. The Gallus gallus RJF reference genome reveals an MHCY haplotype organized in gene blocks that contain 107 loci including 45 specialized, polymorphic MHC class I loci, 41 C-type lectin-like loci, and other loci amid hundreds of transposable elements.. *G3 (Bethesda, Md.)*. PMID: 35997588
5. Genome-wide survey and expression profiling of CCCH-zinc finger family reveals a functional module in macrophage activation.. *PloS one*. PMID: 18682727

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.0 |
| 高置信度残基 (pLDDT>90) 占比 | 21.6% |
| 置信残基 (pLDDT 70-90) 占比 | 31.5% |
| 中等置信 (pLDDT 50-70) 占比 | 11.4% |
| 低置信 (pLDDT<50) 占比 | 35.5% |
| 有序区域 (pLDDT>70) 占比 | 53.1% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=65.0），有序残基占 53.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019510, IPR009097, IPR042653, IPR040459, IPR000571; Pfam: PF10469, PF04457, PF00642 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CDC42EP5 | 0.644 | 0.000 | — |
| LENG8 | 0.621 | 0.000 | — |
| TTYH1 | 0.551 | 0.000 | — |
| CARNMT1 | 0.465 | 0.466 | — |
| LENG1 | 0.456 | 0.047 | — |
| DENND10 | 0.442 | 0.000 | — |
| ZC3HAV1L | 0.428 | 0.000 | — |
| TMCO4 | 0.423 | 0.000 | — |
| ASCC1 | 0.417 | 0.000 | — |
| PHYHIP | 0.416 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CARNMT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| B4GALT2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 12，IntAct interactions: 2
- 调控相关比例: 0 / 12 = 0%

**评价**: STRING 12 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.0 + PDB: 无 | pLDDT=65.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoli fibrillar center | 待确认 |
| PPI | STRING + IntAct | 12 + 2 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. LENG9 — Leukocyte receptor cluster member 9，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小501 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=65.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96B70
- Protein Atlas: https://www.proteinatlas.org/ENSG00000275183-LENG9/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LENG9
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96B70
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
