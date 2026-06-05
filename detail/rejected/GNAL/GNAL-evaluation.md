---
type: protein-evaluation
gene: "GNAL"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GNAL — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GNAL |
| 蛋白名称 | Guanine nucleotide-binding protein G(olf) subunit alpha |
| 蛋白大小 | 381 aa / 44.3 kDa |
| UniProt ID | P38405 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Plasma membrane, Cytosol; UniProt: Cell membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 381 aa / 44.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=93.1; PDB: 8EL8, 8IW1, 8KGK, 8KH4 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000367, IPR001019, IPR011025, IPR027417; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.0/180** | |
| **归一化总分** | | | **68.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cytosol | Approved |
| UniProt | Cell membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- extracellular exosome (GO:0070062)
- heterotrimeric G-protein complex (GO:0005834)
- plasma membrane (GO:0005886)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 0 |
| 别名(未计入scoring) | 无 |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.1 |
| 高置信度残基 (pLDDT>90) 占比 | 85.3% |
| 置信残基 (pLDDT 70-90) 占比 | 10.2% |
| 中等置信 (pLDDT 50-70) 占比 | 2.6% |
| 低置信 (pLDDT<50) 占比 | 1.8% |
| 有序区域 (pLDDT>70) 占比 | 95.5% |
| 可用 PDB 条目 | 8EL8, 8IW1, 8KGK, 8KH4 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（8EL8, 8IW1, 8KGK, 8KH4）+ AlphaFold高质量预测（pLDDT=93.1），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000367, IPR001019, IPR011025, IPR027417; Pfam: PF00503 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ADCY9 | 0.986 | 0.792 | — |
| DRD1 | 0.984 | 0.257 | — |
| GNG13 | 0.980 | 0.400 | — |
| GNB1 | 0.978 | 0.574 | — |
| ADCY3 | 0.977 | 0.258 | — |
| ADCY5 | 0.975 | 0.470 | — |
| GNAS | 0.975 | 0.723 | — |
| ADCY2 | 0.968 | 0.513 | — |
| ADCY8 | 0.964 | 0.258 | — |
| ADCY7 | 0.960 | 0.409 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| BABAM1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| SPATA2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| USP3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| Haus1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| 616370" | psi-mi:"MI:0096"(pull down) | pubmed:23606334|imex:IM-21247 |
| FNDC5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GNAS | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CHIA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MAGED2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MLF2 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.1 + PDB: 8EL8, 8IW1, 8KGK, 8KH4 | pLDDT=93.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane / Plasma membrane, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GNAL — Guanine nucleotide-binding protein G(olf) subunit alpha，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小381 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P38405
- Protein Atlas: https://www.proteinatlas.org/ENSG00000141404-GNAL/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GNAL
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P38405
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000141404-GNAL/subcellular

![](https://images.proteinatlas.org/51160/1047_G9_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/51160/1047_G9_7_blue_red_green.jpg)
![](https://images.proteinatlas.org/51160/1048_G9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/51160/1048_G9_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/51160/1182_B9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/51160/1182_B9_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P38405-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
