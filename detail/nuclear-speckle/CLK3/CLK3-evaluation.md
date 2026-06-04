---
type: protein-evaluation
gene: "CLK3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CLK3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CLK3 |
| 蛋白名称 | Dual specificity protein kinase CLK3 |
| 蛋白大小 | 490 aa / 58.6 kDa |
| UniProt ID | P49761 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Intermediate filaments; UniProt: Nucleus; Cytoplasm; Cytoplasmic vesicle, secretory vesicle,  |
| 蛋白大小 | 10/10 | ×1 | 10 | 490 aa / 58.6 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=41 篇 (≤60→6) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=79.0; PDB: 2EU9, 2EXE, 2WU6, 2WU7, 3RAW, 6FT7, 6FYP |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR051175, IPR011009, IPR000719, IPR017441, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **124.0/180** | |
| **归一化总分** | | | **68.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Intermediate filaments | Supported |
| UniProt | Nucleus; Cytoplasm; Cytoplasmic vesicle, secretory vesicle, acrosome; Nucleus speckle | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- acrosomal vesicle (GO:0001669)
- intermediate filament cytoskeleton (GO:0045111)
- membrane (GO:0016020)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 41 |
| PubMed broad count | 63 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. The dual-specificity protein kinase Clk3 is essential for Xenopus neural development.. *Biochemical and biophysical research communications*. PMID: 34146908
2. The dual specificity protein kinase CLK3 is abundantly expressed in mature mouse spermatozoa.. *Experimental cell research*. PMID: 10585269
3. CLK3 positively promoted colorectal cancer proliferation by activating IL-6/STAT3 signaling.. *Experimental cell research*. PMID: 38885806
4. Targeting CLK3 inhibits the progression of cholangiocarcinoma by reprogramming nucleotide metabolism.. *The Journal of experimental medicine*. PMID: 32453420
5. MFAP2, upregulated by m1A methylation, promotes colorectal cancer invasiveness via CLK3.. *Cancer medicine*. PMID: 36583532

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.0 |
| 高置信度残基 (pLDDT>90) 占比 | 67.8% |
| 置信残基 (pLDDT 70-90) 占比 | 3.1% |
| 中等置信 (pLDDT 50-70) 占比 | 1.0% |
| 低置信 (pLDDT<50) 占比 | 28.2% |
| 有序区域 (pLDDT>70) 占比 | 70.9% |
| 可用 PDB 条目 | 2EU9, 2EXE, 2WU6, 2WU7, 3RAW, 6FT7, 6FYP, 6FYR, 6KHF, 6RCT |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（2EU9, 2EXE, 2WU6, 2WU7, 3RAW, 6FT7, 6FYP, 6FYR, 6KHF, 6RCT）+ AlphaFold极高置信度预测（pLDDT=79.0），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051175, IPR011009, IPR000719, IPR017441, IPR008271; Pfam: PF00069 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| COQ7 | 0.893 | 0.000 | — |
| TRA2B | 0.855 | 0.773 | — |
| CLK2 | 0.846 | 0.836 | — |
| TRA2A | 0.837 | 0.787 | — |
| RSRP1 | 0.835 | 0.786 | — |
| SRSF10 | 0.833 | 0.742 | — |
| SRSF8 | 0.831 | 0.797 | — |
| SRSF1 | 0.782 | 0.592 | — |
| TELO2 | 0.770 | 0.000 | — |
| IMMT | 0.768 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000378505.4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| RSRP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CLK2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| YWHAG | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| SLAMF7 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| SUMO3 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:17000644|imex:IM-19940 |
| HSP90AB1 | psi-mi:"MI:0729"(luminescence based mammalian inte | imex:IM-17906|pubmed:22939624| |
| RBBP6 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:23602568|imex:IM-17935 |
| TRA2A | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:23602568|imex:IM-17935 |
| SCRIB | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:23602568|imex:IM-17935 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.0 + PDB: 2EU9, 2EXE, 2WU6, 2WU7, 3RAW,  | pLDDT=79.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Cytoplasmic vesicle, secretory / Nucleoplasm; 额外: Intermediate filaments | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CLK3 — Dual specificity protein kinase CLK3，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小490 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 41 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P49761
- Protein Atlas: https://www.proteinatlas.org/ENSG00000179335-CLK3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CLK3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P49761
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
