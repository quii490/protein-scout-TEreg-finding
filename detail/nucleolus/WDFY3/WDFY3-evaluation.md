---
type: protein-evaluation
gene: "WDFY3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## WDFY3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | WDFY3 / KIAA0993 |
| 蛋白名称 | WD repeat and FYVE domain-containing protein 3 |
| 蛋白大小 | 3526 aa / 395.3 kDa |
| UniProt ID | Q8IZQ1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Nucleoli, Plasma membrane; UniProt: Nucleus membrane; Cytoplasm, cytosol; Nucleus, PML body; Mem |
| 蛋白大小 | 0/10 | ×1 | 0 | 3526 aa / 395.3 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=69 篇 (≤80→4) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 3WIM, 6W9N |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR056252, IPR011989, IPR016024, IPR000409, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **83.5/180** | |
| **归一化总分** | | | **46.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoli, Plasma membrane | Approved |
| UniProt | Nucleus membrane; Cytoplasm, cytosol; Nucleus, PML body; Membrane; Perikaryon; Cell projection, axon | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- autophagosome (GO:0005776)
- autophagosome membrane (GO:0000421)
- axon (GO:0030424)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- inclusion body (GO:0016234)
- membrane (GO:0016020)
- nuclear envelope (GO:0005635)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 69 |
| PubMed broad count | 113 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0993 |

**关键文献**:
1. De novo genic mutations among a Chinese autism spectrum disorder cohort.. *Nature communications*. PMID: 27824329
2. Pathogenic WDFY3 variants cause neurodevelopmental disorders and opposing effects on brain size.. *Brain : a journal of neurology*. PMID: 31327001
3. Inherited and multiple de novo mutations in autism/developmental delay risk genes suggest a multifactorial model.. *Molecular autism*. PMID: 30564305
4. The spectrum of neurodevelopmental, neuromuscular and neurodegenerative disorders due to defective autophagy.. *Autophagy*. PMID: 34130600
5. Targeted proteomics addresses selectivity and complexity of protein degradation by autophagy.. *Autophagy*. PMID: 39245437

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v? |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 3WIM, 6W9N |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR056252, IPR011989, IPR016024, IPR000409, IPR036372; Pfam: PF23295, PF02138, PF01363 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SQSTM1 | 0.992 | 0.735 | — |
| ATG5 | 0.992 | 0.304 | — |
| GABARAP | 0.987 | 0.951 | — |
| MAP1LC3C | 0.939 | 0.424 | — |
| ATG12 | 0.924 | 0.292 | — |
| TRAF6 | 0.921 | 0.510 | — |
| ATG16L1 | 0.910 | 0.292 | — |
| GABARAPL1 | 0.840 | 0.424 | — |
| NBR1 | 0.839 | 0.000 | — |
| MAP1LC3B | 0.837 | 0.628 | — |

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
| 三维结构 | AlphaFold pLDDT=0 + PDB: 3WIM, 6W9N | pLDDT=0, v? | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus membrane; Cytoplasm, cytosol; Nucleus, PML / Cytosol; 额外: Nucleoli, Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐

**核心优势**:
1. WDFY3 — WD repeat and FYVE domain-containing protein 3，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小3526 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 69 篇，已有一定研究基础
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IZQ1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163625-WDFY3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=WDFY3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IZQ1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
