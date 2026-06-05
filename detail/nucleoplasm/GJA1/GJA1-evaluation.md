---
type: protein-evaluation
gene: "GJA1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GJA1 — REJECTED (研究热度过高 (PubMed strict=686，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GJA1 / GJAL |
| 蛋白名称 | Gap junction alpha-1 protein |
| 蛋白大小 | 382 aa / 43.0 kDa |
| UniProt ID | P17302 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Vesicles, Cell Junctions; 额外: Nucleoplasm; UniProt: Cell membrane; Cell junction, gap junction; Endoplasmic reti |
| 蛋白大小 | 10/10 | ×1 | 10 | 382 aa / 43.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=686 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=69.8; PDB: 2LL2, 7F92, 7F93, 7F94, 7XQ9, 7XQB, 7XQD |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR035091, IPR000500, IPR002261, IPR013124, IPR034 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles, Cell Junctions; 额外: Nucleoplasm | Approved |
| UniProt | Cell membrane; Cell junction, gap junction; Endoplasmic reticulum; Cell junction | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- apical plasma membrane (GO:0016324)
- cell junction (GO:0030054)
- cell-cell contact zone (GO:0044291)
- connexin complex (GO:0005922)
- cytoplasm (GO:0005737)
- endoplasmic reticulum membrane (GO:0005789)
- focal adhesion (GO:0005925)
- gap junction (GO:0005921)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 686 |
| PubMed broad count | 1966 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GJAL |

**关键文献**:
1. PIEZO channels link mechanical forces to uterine contractions in parturition.. *Science (New York, N.Y.)*. PMID: 41231991
2. YTHDF3 Induces the Translation of m(6)A-Enriched Gene Transcripts to Promote Breast Cancer Brain Metastasis.. *Cancer cell*. PMID: 33125861
3. GJA1-20k and Mitochondrial Dynamics.. *Frontiers in physiology*. PMID: 35399255
4. Dissecting regulatory non-coding GWAS loci reveals fibroblast causal genes with pathophysiological relevance to heart failure.. *Nature communications*. PMID: 41073375
5. Liraglutide improves follicle development in polycystic ovary syndrome by inhibiting CXCL10 secretion.. *Reproductive biology and endocrinology : RB&E*. PMID: 39107809

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.8 |
| 高置信度残基 (pLDDT>90) 占比 | 29.8% |
| 置信残基 (pLDDT 70-90) 占比 | 28.3% |
| 中等置信 (pLDDT 50-70) 占比 | 11.3% |
| 低置信 (pLDDT<50) 占比 | 30.6% |
| 有序区域 (pLDDT>70) 占比 | 58.1% |
| 可用 PDB 条目 | 2LL2, 7F92, 7F93, 7F94, 7XQ9, 7XQB, 7XQD, 7XQF, 7XQG, 7XQH |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=69.8），有序残基占 58.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR035091, IPR000500, IPR002261, IPR013124, IPR034634; Pfam: PF00029, PF03508 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TJP1 | 0.999 | 0.597 | — |
| SRC | 0.998 | 0.334 | — |
| GJA5 | 0.996 | 0.287 | — |
| GJC1 | 0.993 | 0.173 | — |
| GJB6 | 0.981 | 0.091 | — |
| PKP2 | 0.973 | 0.110 | — |
| GJA3 | 0.968 | 0.292 | — |
| GJB1 | 0.968 | 0.091 | — |
| CAV1 | 0.965 | 0.329 | — |
| GJB2 | 0.963 | 0.091 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Dbn1 | psi-mi:"MI:0096"(pull down) | pubmed:15084279 |
| Prkce | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:11139474 |
| Sgsm3 | psi-mi:"MI:0018"(two hybrid) | pubmed:15709751|mint:MINT-5217 |
| TJP1 | psi-mi:"MI:0096"(pull down) | pubmed:16944923|imex:IM-18990| |
| Gjb3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:18055446|imex:IM-19526 |
| Gjc1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:18055446|imex:IM-19526 |
| Cnst | psi-mi:"MI:0096"(pull down) | pubmed:19864490|imex:IM-19064 |
| TFCP2 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| DSC2 | psi-mi:"MI:0096"(pull down) | imex:IM-20978|pubmed:21220045 |
| LAMP1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=69.8 + PDB: 2LL2, 7F92, 7F93, 7F94, 7XQ9,  | pLDDT=69.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane; Cell junction, gap junction; Endopl / Vesicles, Cell Junctions; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. GJA1 — Gap junction alpha-1 protein，研究基础较多，新颖性有限。
2. 蛋白大小382 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 686 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=69.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 686 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P17302
- Protein Atlas: https://www.proteinatlas.org/ENSG00000152661-GJA1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GJA1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P17302
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (uncertain)。来源: https://www.proteinatlas.org/ENSG00000152661-GJA1/subcellular

![](https://images.proteinatlas.org/47551/1607_C3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/47551/1607_C3_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/47551/1667_C3_4_cr57ea313c6793b_blue_red_green.jpg)
![](https://images.proteinatlas.org/47551/1667_C3_9_cr58036d70359d6_blue_red_green.jpg)
![](https://images.proteinatlas.org/47551/1786_D4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/47551/1786_D4_6_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P17302-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
