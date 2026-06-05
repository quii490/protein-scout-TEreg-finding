---
type: protein-evaluation
gene: "MFSD8"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MFSD8 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MFSD8 / CLN7 |
| 蛋白名称 | Major facilitator superfamily domain-containing protein 8 |
| 蛋白大小 | 518 aa / 57.6 kDa |
| UniProt ID | Q8NHS3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Vesicles; 额外: Nucleoplasm; UniProt: Endosome membrane; Lysosome membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 518 aa / 57.6 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=79 篇 (≤80→4) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=83.3; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011701, IPR020846, IPR051068, IPR036259; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **93.5/180** | |
| **归一化总分** | | | **51.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Nucleoplasm | Supported |
| UniProt | Endosome membrane; Lysosome membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chloride channel complex (GO:0034707)
- endosome membrane (GO:0010008)
- lysosomal membrane (GO:0005765)
- mitochondrion (GO:0005739)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 79 |
| PubMed broad count | 108 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CLN7 |

**关键文献**:
1. Neuronal Ceroid Lipofuscinoses Overview.. **. PMID: 20301601
2. Aberrant upregulation of the glycolytic enzyme PFKFB3 in CLN7 neuronal ceroid lipofuscinosis.. *Nature communications*. PMID: 35087090
3. AAV9/MFSD8 gene therapy is effective in preclinical models of neuronal ceroid lipofuscinosis type 7 disease.. *The Journal of clinical investigation*. PMID: 35025759
4. Novel MFSD8 mutation causing non-syndromic asymmetric adult-onset macular dystrophy.. *Ophthalmic genetics*. PMID: 35801630
5. Loss of mfsd8 alters the secretome during Dictyostelium aggregation.. *European journal of cell biology*. PMID: 37742391

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.3 |
| 高置信度残基 (pLDDT>90) 占比 | 52.3% |
| 置信残基 (pLDDT 70-90) 占比 | 32.8% |
| 中等置信 (pLDDT 50-70) 占比 | 2.5% |
| 低置信 (pLDDT<50) 占比 | 12.4% |
| 有序区域 (pLDDT>70) 占比 | 85.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=83.3，有序区 85.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011701, IPR020846, IPR051068, IPR036259; Pfam: PF07690 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CLN8 | 0.963 | 0.000 | — |
| CLN3 | 0.952 | 0.071 | — |
| CLN6 | 0.947 | 0.000 | — |
| CLN5 | 0.938 | 0.000 | — |
| PPT1 | 0.915 | 0.000 | — |
| DNAJC5 | 0.838 | 0.000 | — |
| CTSD | 0.789 | 0.000 | — |
| KCTD7 | 0.776 | 0.000 | — |
| CTSF | 0.708 | 0.000 | — |
| TPP1 | 0.687 | 0.045 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DNAJC19 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CYB5R1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| EPHX1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LPAR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YIPF3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SLC22A9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| P2RY12 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ADGRE5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| IPPK | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.3 + PDB: 无 | pLDDT=83.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endosome membrane; Lysosome membrane / Vesicles; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. MFSD8 — Major facilitator superfamily domain-containing protein 8，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小518 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 79 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NHS3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000164073-MFSD8/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MFSD8
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NHS3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (supported)。来源: https://www.proteinatlas.org/ENSG00000164073-MFSD8/subcellular

![](https://images.proteinatlas.org/44802/550_E7_1_red_green.jpg)
![](https://images.proteinatlas.org/44802/550_E7_2_red_green.jpg)
![](https://images.proteinatlas.org/44802/559_E7_1_red_green.jpg)
![](https://images.proteinatlas.org/44802/559_E7_2_red_green.jpg)
![](https://images.proteinatlas.org/44802/567_E7_1_red_green.jpg)
![](https://images.proteinatlas.org/44802/567_E7_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8NHS3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
