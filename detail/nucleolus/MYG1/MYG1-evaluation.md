---
type: protein-evaluation
gene: "MYG1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MYG1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MYG1 / C12orf10 |
| 蛋白名称 | MYG1 exonuclease |
| 蛋白大小 | 376 aa / 42.5 kDa |
| UniProt ID | Q9HB07 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus, nucleoplasm; Mitochondrion matrix; Nucleus, nucleol |
| 蛋白大小 | 10/10 | ×1 | 10 | 376 aa / 42.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=17 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=89.9; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR003226; Pfam: PF03690 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.5/180** | |
| **归一化总分** | | | **76.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus, nucleoplasm; Mitochondrion matrix; Nucleus, nucleolus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- mitochondrial matrix (GO:0005759)
- mitochondrion (GO:0005739)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 17 |
| PubMed broad count | 24 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C12orf10 |

**关键文献**:
1. MYG1 drives glycolysis and colorectal cancer development through nuclear-mitochondrial collaboration.. *Nature communications*. PMID: 38862489
2. Characterization of MYG1 gene and protein: subcellular distribution and function.. *Biology of the cell*. PMID: 19014353
3. Myg1 exonuclease couples the nuclear and mitochondrial translational programs through RNA processing.. *Nucleic acids research*. PMID: 31081026
4. MYG1 promotes proliferation and inhibits autophagy in lung adenocarcinoma cells via the AMPK/mTOR complex 1 signaling pathway.. *Oncology letters*. PMID: 33692866
5. Promoter polymorphism -119C/G in MYG1 (C12orf10) gene is related to vitiligo susceptibility and Arg4Gln affects mitochondrial entrance of Myg1.. *BMC medical genetics*. PMID: 20377893

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.9 |
| 高置信度残基 (pLDDT>90) 占比 | 83.2% |
| 置信残基 (pLDDT 70-90) 占比 | 4.0% |
| 中等置信 (pLDDT 50-70) 占比 | 1.6% |
| 低置信 (pLDDT<50) 占比 | 11.2% |
| 有序区域 (pLDDT>70) 占比 | 87.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=89.9，有序区 87.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003226; Pfam: PF03690 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NDUFS8 | 0.714 | 0.000 | — |
| NDUFS2 | 0.675 | 0.000 | — |
| NDUFS1 | 0.671 | 0.000 | — |
| SDHA | 0.665 | 0.000 | — |
| SDHC | 0.645 | 0.000 | — |
| MFSD5 | 0.638 | 0.000 | — |
| NOTCH2NLA | 0.622 | 0.622 | — |
| PFDN5 | 0.616 | 0.000 | — |
| LHPP | 0.602 | 0.575 | — |
| GALT | 0.599 | 0.591 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| COPS5 | psi-mi:"MI:0018"(two hybrid) | pubmed:18624398|imex:IM-19021 |
| HSPB1 | psi-mi:"MI:0097"(reverse ras recruitment system) | imex:IM-20864|pubmed:25277244 |
| CMTM5 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| FAM9B | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| AGTRAP | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| ARL6IP1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| REEP6 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| WWOX | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TMEM229B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| DESI2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.9 + PDB: 无 | pLDDT=89.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus, nucleoplasm; Mitochondrion matrix; Nucleu / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. MYG1 — MYG1 exonuclease，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小376 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 17 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9HB07
- Protein Atlas: https://www.proteinatlas.org/ENSG00000139637-MYG1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MYG1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9HB07
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000139637-MYG1/subcellular

![](https://images.proteinatlas.org/38627/579_B4_1_red_green.jpg)
![](https://images.proteinatlas.org/38627/579_B4_2_red_green.jpg)
![](https://images.proteinatlas.org/38627/581_B4_1_red_green.jpg)
![](https://images.proteinatlas.org/38627/581_B4_2_red_green.jpg)
![](https://images.proteinatlas.org/38627/591_B4_1_red_green.jpg)
![](https://images.proteinatlas.org/38627/591_B4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9HB07-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
