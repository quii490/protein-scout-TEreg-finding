---
type: protein-evaluation
gene: "CLEC16A"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CLEC16A — REJECTED (研究热度过高 (PubMed strict=103，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CLEC16A / KIAA0350 |
| 蛋白名称 | Protein CLEC16A |
| 蛋白大小 | 1053 aa / 117.7 kDa |
| UniProt ID | Q2KHT3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Vesicles; UniProt: Endosome membrane; Lysosome membrane |
| 蛋白大小 | 8/10 | ×1 | 8 | 1053 aa / 117.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=103 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=70.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039272, IPR045820, IPR019155; Pfam: PF19439, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 11 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **69.5/180** | |
| **归一化总分** | | | **38.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Vesicles | Approved |
| UniProt | Endosome membrane; Lysosome membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- endosome membrane (GO:0010008)
- Golgi apparatus (GO:0005794)
- lysosomal membrane (GO:0005765)
- vesicle (GO:0031982)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 103 |
| PubMed broad count | 169 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0350 |

**关键文献**:
1. CLEC16A in astrocytes promotes mitophagy and limits pathology in a multiple sclerosis mouse model.. *Nature neuroscience*. PMID: 40033124
2. Protein disorder in the regulatory control of mitophagy.. *Autophagy reports*. PMID: 37547544
3. CLEC16A-An Emerging Master Regulator of Autoimmunity and Neurodegeneration.. *International journal of molecular sciences*. PMID: 37175930
4. An intrinsically disordered protein region encoded by the human disease gene CLEC16A regulates mitophagy.. *Autophagy*. PMID: 35604110
5. CLEC16A interacts with retromer and TRIM27, and its loss impairs endosomal trafficking and neurodevelopment.. *Human genetics*. PMID: 36538041

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.8 |
| 高置信度残基 (pLDDT>90) 占比 | 43.4% |
| 置信残基 (pLDDT 70-90) 占比 | 19.7% |
| 中等置信 (pLDDT 50-70) 占比 | 4.8% |
| 低置信 (pLDDT<50) 占比 | 32.1% |
| 有序区域 (pLDDT>70) 占比 | 63.1% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=70.8，有序区 63.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039272, IPR045820, IPR019155; Pfam: PF19439, PF09758 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RNF41 | 0.903 | 0.338 | — |
| GPN1 | 0.834 | 0.000 | — |
| DEXI | 0.808 | 0.000 | — |
| TFB1M | 0.749 | 0.000 | — |
| SH2B3 | 0.727 | 0.000 | — |
| PTPN2 | 0.700 | 0.000 | — |
| HLA-DRB1 | 0.682 | 0.000 | — |
| CIITA | 0.681 | 0.000 | — |
| NAA25 | 0.662 | 0.000 | — |
| BACH2 | 0.661 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| dmsB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| WRAP73 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RAB39B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Rnf41 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:24949970|imex:IM-23039 |
| MFAP4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SLC18A2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| RAB43 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| RASSF8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ENST00000409790 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 11
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 11 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.8 + PDB: 无 | pLDDT=70.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endosome membrane; Lysosome membrane / Nucleoplasm, Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 11 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CLEC16A — Protein CLEC16A，研究基础较多，新颖性有限。
2. 蛋白大小1053 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 103 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 103 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q2KHT3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000038532-CLEC16A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CLEC16A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q2KHT3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
