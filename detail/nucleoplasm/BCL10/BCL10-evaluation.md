---
type: protein-evaluation
gene: "BCL10"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## BCL10 — REJECTED (研究热度过高 (PubMed strict=522，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BCL10 / CIPER, CLAP |
| 蛋白名称 | B-cell lymphoma/leukemia 10 |
| 蛋白大小 | 233 aa / 26.3 kDa |
| UniProt ID | O95999 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Nucleoplasm; UniProt: Cytoplasm, perinuclear region; Membrane raft |
| 蛋白大小 | 10/10 | ×1 | 10 | 233 aa / 26.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=522 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=69.5; PDB: 2MB9, 6BZE, 6GK2, 8CZD, 8CZO |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR033238, IPR001315, IPR042143, IPR011029; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm | Supported |
| UniProt | Cytoplasm, perinuclear region; Membrane raft | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- CBM complex (GO:0032449)
- cytoplasm (GO:0005737)
- cytoplasmic microtubule (GO:0005881)
- cytosol (GO:0005829)
- immunological synapse (GO:0001772)
- lysosome (GO:0005764)
- membrane raft (GO:0045121)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 522 |
| PubMed broad count | 865 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CIPER, CLAP |

**关键文献**:
1. Naturally occurring T cell mutations enhance engineered T cell therapies.. *Nature*. PMID: 38326614
2. Emodin Alleviates Sepsis-Induced Multiorgan Damage by Inhibiting NETosis through Targeting Neutrophils BCL-10.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 40779122
3. Role of Calcium Signaling Pathway-Related Gene Regulatory Networks in Ischemic Stroke Based on Multiple WGCNA and Single-Cell Analysis.. *Oxidative medicine and cellular longevity*. PMID: 34987704
4. The CARD14sh-BCL10-MALT1 complex regulates MAVS-mediated antiviral response in keratinocytes.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 40489607
5. Germline CBM-opathies: From immunodeficiency to atopy.. *The Journal of allergy and clinical immunology*. PMID: 31060714

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.5 |
| 高置信度残基 (pLDDT>90) 占比 | 35.2% |
| 置信残基 (pLDDT 70-90) 占比 | 10.7% |
| 中等置信 (pLDDT 50-70) 占比 | 26.6% |
| 低置信 (pLDDT<50) 占比 | 27.5% |
| 有序区域 (pLDDT>70) 占比 | 45.9% |
| 可用 PDB 条目 | 2MB9, 6BZE, 6GK2, 8CZD, 8CZO |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=69.5），有序残基占 45.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR033238, IPR001315, IPR042143, IPR011029; Pfam: PF00619 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CARD10 | 0.999 | 0.525 | — |
| IKBKG | 0.999 | 0.849 | — |
| CARD11 | 0.999 | 0.926 | — |
| MALT1 | 0.999 | 0.998 | — |
| TRAF6 | 0.999 | 0.295 | — |
| CARD9 | 0.999 | 0.811 | — |
| CASP8 | 0.998 | 0.292 | — |
| IKBKB | 0.996 | 0.736 | — |
| CHUK | 0.994 | 0.626 | — |
| CARD14 | 0.988 | 0.525 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000498104.1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| AKT1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-14497|pubmed:16280327 |
| BCL3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-14497|pubmed:16280327 |
| KRT33B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| H2BC10 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| USHBP1 | psi-mi:"MI:0663"(confocal microscopy) | imex:IM-15364|pubmed:21988832 |
| IL15RA | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| SRSF1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| SLC20A1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| NHERF1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=69.5 + PDB: 2MB9, 6BZE, 6GK2, 8CZD, 8CZO | pLDDT=69.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, perinuclear region; Membrane raft / Cytosol; 额外: Nucleoplasm | 一致 |
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
1. BCL10 — B-cell lymphoma/leukemia 10，研究基础较多，新颖性有限。
2. 蛋白大小233 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 522 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=69.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 522 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O95999
- Protein Atlas: https://www.proteinatlas.org/ENSG00000142867-BCL10/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BCL10
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O95999
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000142867-BCL10/subcellular

![](https://images.proteinatlas.org/18953/2190_D1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/18953/2190_D1_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/18953/2207_A9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/18953/2207_A9_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/18953/2227_A1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/18953/2227_A1_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O95999-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
