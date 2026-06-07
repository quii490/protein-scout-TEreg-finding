---
type: protein-evaluation
gene: "FBXL5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FBXL5 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FBXL5 / FBL4, FBL5, FLR1 |
| 蛋白名称 | F-box/LRR-repeat protein 5 |
| 蛋白大小 | 691 aa / 78.6 kDa |
| UniProt ID | Q9UKA1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm, perinuclear region; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 691 aa / 78.6 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=77 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=69.6; PDB: 3U9J, 3U9M, 3V5X, 3V5Y, 3V5Z, 6VCD |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036047, IPR001810, IPR012312, IPR045808, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **101.5/180** | |
| **归一化总分** | | | **56.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm, perinuclear region; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleus (GO:0005634)
- perinuclear region of cytoplasm (GO:0048471)
- SCF ubiquitin ligase complex (GO:0019005)
- ubiquitin ligase complex (GO:0000151)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 77 |
| PubMed broad count | 103 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FBL4, FBL5, FLR1 |

**关键文献**:
1. Abnormal mitochondrial iron metabolism damages alveolar type II epithelial cells involved in bleomycin-induced pulmonary fibrosis.. *Theranostics*. PMID: 38773980
2. A regulatory module comprising G3BP1-FBXL5-IRP2 axis determines sodium arsenite-induced ferroptosis.. *Journal of hazardous materials*. PMID: 38118197
3. F-box and leucine-rich repeat protein 5 (FBXL5): sensing intracellular iron and oxygen.. *Journal of inorganic biochemistry*. PMID: 24508277
4. Integrated hepatic ferroptosis gene signature dictates pathogenic features of ferroptosis.. *Hepatology communications*. PMID: 40434703
5. Role of FBXL5 in redox homeostasis and spindle assembly during oocyte maturation in mice.. *FASEB journal : official publication of the Federation of American Societies for Experimental Biology*. PMID: 37462473

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.6 |
| 高置信度残基 (pLDDT>90) 占比 | 45.0% |
| 置信残基 (pLDDT 70-90) 占比 | 13.5% |
| 中等置信 (pLDDT 50-70) 占比 | 9.1% |
| 低置信 (pLDDT<50) 占比 | 32.4% |
| 有序区域 (pLDDT>70) 占比 | 58.5% |
| 可用 PDB 条目 | 3U9J, 3U9M, 3V5X, 3V5Y, 3V5Z, 6VCD |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FBXL5/FBXL5-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=69.6），有序残基占 58.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036047, IPR001810, IPR012312, IPR045808, IPR001611; Pfam: PF12937, PF01814, PF13516 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SKP1 | 0.999 | 0.987 | — |
| CUL1 | 0.999 | 0.838 | — |
| IREB2 | 0.999 | 0.981 | — |
| ACO1 | 0.945 | 0.625 | — |
| RBX1 | 0.880 | 0.510 | — |
| CIAO2B | 0.879 | 0.796 | — |
| MMS19 | 0.875 | 0.778 | — |
| CIAO1 | 0.759 | 0.597 | — |
| FBXL14 | 0.726 | 0.000 | — |
| HERC2 | 0.724 | 0.624 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Dmel\CG12081 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| ORC4 | psi-mi:"MI:0663"(confocal microscopy) | imex:IM-15364|pubmed:21988832 |
| EP300 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| rpoB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| SkpA | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG14151 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Fas2 | psi-mi:"MI:0963"(interactome parallel affinity cap | pubmed:21447707|imex:IM-17304 |
| MYB | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| COPS5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| ECI2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=69.6 + PDB: 3U9J, 3U9M, 3V5X, 3V5Y, 3V5Z,  | pLDDT=69.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, perinuclear region; Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FBXL5 — F-box/LRR-repeat protein 5，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小691 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 77 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=69.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UKA1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000118564-FBXL5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FBXL5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UKA1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FBXL5/FBXL5-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9UKA1 |
| SMART | SM00256;SM00367; |
| UniProt Domain [FT] | DOMAIN 202..248; /note="F-box"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00080" |
| InterPro | IPR036047;IPR001810;IPR012312;IPR045808;IPR001611;IPR006553;IPR032675; |
| Pfam | PF12937;PF01814;PF13516; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000118564-FBXL5/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| SKP1 | Intact, Biogrid | true |
| ACO1 | Biogrid | false |
| CIAO1 | Biogrid | false |
| CIAO2B | Biogrid | false |
| CITED2 | Biogrid | false |
| COPS5 | Biogrid | false |
| CUL1 | Biogrid | false |
| DCTN1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
