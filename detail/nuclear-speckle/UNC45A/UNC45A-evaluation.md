---
type: protein-evaluation
gene: "UNC45A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## UNC45A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | UNC45A / SMAP1 |
| 蛋白名称 | Protein unc-45 homolog A |
| 蛋白大小 | 944 aa / 103.1 kDa |
| UniProt ID | Q9H3U1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles; 额外: Cytosol; UniProt: Cytoplasm; Cytoplasm, perinuclear region; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 944 aa / 103.1 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=46 篇 (≤60→6) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=86.1; PDB: 2DBA |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011989, IPR016024, IPR011990, IPR019734, IPR024 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **117.0/180** | |
| **归一化总分** | | | **65.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles; 额外: Cytosol | Supported |
| UniProt | Cytoplasm; Cytoplasm, perinuclear region; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- Golgi apparatus (GO:0005794)
- nuclear speck (GO:0016607)
- perinuclear region of cytoplasm (GO:0048471)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 46 |
| PubMed broad count | 67 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SMAP1 |

**关键文献**:
1. UNC45A deficiency causes microvillus inclusion disease-like phenotype by impairing myosin VB-dependent apical trafficking.. *The Journal of clinical investigation*. PMID: 35575086
2. Uncovering the Relationship Between Genes and Phenotypes Beyond the Gut in Microvillus Inclusion Disease.. *Cellular and molecular gastroenterology and hepatology*. PMID: 38307491
3. Pain/Stress, Mitochondrial Dysfunction, and Neurodevelopment in Preterm Infants.. *Developmental neuroscience*. PMID: 38286121
4. UNC45A localizes to centrosomes and regulates cancer cell proliferation through ChK1 activation.. *Cancer letters*. PMID: 25444911
5. A Functional Relationship Between UNC45A and MYO5B Connects Two Rare Diseases With Shared Enteropathy.. *Cellular and molecular gastroenterology and hepatology*. PMID: 35421597

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.1 |
| 高置信度残基 (pLDDT>90) 占比 | 47.9% |
| 置信残基 (pLDDT 70-90) 占比 | 43.0% |
| 中等置信 (pLDDT 50-70) 占比 | 5.3% |
| 低置信 (pLDDT<50) 占比 | 3.8% |
| 有序区域 (pLDDT>70) 占比 | 90.9% |
| 可用 PDB 条目 | 2DBA |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=86.1，有序区 90.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011989, IPR016024, IPR011990, IPR019734, IPR024660; Pfam: PF13432, PF13181, PF11701 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HSP90AA1 | 0.946 | 0.719 | — |
| AHSA1 | 0.828 | 0.000 | — |
| HSP90AB1 | 0.810 | 0.595 | — |
| MARCHF10 | 0.681 | 0.681 | — |
| CSNK1A1 | 0.668 | 0.624 | — |
| FAM83H | 0.660 | 0.360 | — |
| CSE1L | 0.626 | 0.623 | — |
| MYO1C | 0.623 | 0.462 | — |
| MYO1E | 0.619 | 0.539 | — |
| MAX | 0.596 | 0.591 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000407487.2 | psi-mi:"MI:0096"(pull down) | pubmed:40125554|imex:IM-30289 |
| PHLDA3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| WRAP73 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| BRF2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MYC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| PTP4A3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| GSTK1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ILK | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| 7242199 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EBI-6248077 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-17346|pubmed:22190034| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.1 + PDB: 2DBA | pLDDT=86.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm, perinuclear region; Nucleus / Nuclear speckles; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. UNC45A — Protein unc-45 homolog A，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小944 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 46 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H3U1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000140553-UNC45A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=UNC45A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H3U1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (supported)。来源: https://www.proteinatlas.org/ENSG00000140553-UNC45A/subcellular

![](https://images.proteinatlas.org/39228/711_C3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/39228/711_C3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/39228/723_C3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/39228/723_C3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/39228/866_C3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/39228/866_C3_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H3U1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
