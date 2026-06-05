---
type: protein-evaluation
gene: "AASDHPPT"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## AASDHPPT — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | AASDHPPT |
| 蛋白名称 | L-aminoadipate-semialdehyde dehydrogenase-phosphopantetheinyl transferase |
| 蛋白大小 | 309 aa / 35.8 kDa |
| UniProt ID | Q9NRN7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm, cytosol |
| 蛋白大小 | 10/10 | ×1 | 10 | 309 aa / 35.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=90.3; PDB: 2BYD, 2C43, 2CG5 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR008278, IPR037143, IPR055066, IPR050559; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.0/180** | |
| **归一化总分** | | | **68.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm, cytosol | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 6 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Mitochondrial phosphopantetheinylation is required for oxidative metabolism.. *Metabolism: clinical and experimental*. PMID: 41061852
2. Mitochondrial Phosphopantetheinylation is Required for Oxidative Function.. *bioRxiv : the preprint server for biology*. PMID: 38766035
3. Glycerophosphatidylcholine PC(36:1) absence and 3'-phosphoadenylate (pAp) accumulation are hallmarks of the human glioma metabolome.. *Scientific reports*. PMID: 30283018
4. Identification of key gene modules and genes in colorectal cancer by co-expression analysis weighted gene co-expression network analysis.. *Bioscience reports*. PMID: 32815531
5. Identifying novel autoantibody signatures in ovarian cancer using high-density protein microarrays.. *Clinical biochemistry*. PMID: 19094976

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.3 |
| 高置信度残基 (pLDDT>90) 占比 | 82.2% |
| 置信残基 (pLDDT 70-90) 占比 | 6.1% |
| 中等置信 (pLDDT 50-70) 占比 | 4.2% |
| 低置信 (pLDDT<50) 占比 | 7.4% |
| 有序区域 (pLDDT>70) 占比 | 88.3% |
| 可用 PDB 条目 | 2BYD, 2C43, 2CG5 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2BYD, 2C43, 2CG5）+ AlphaFold高质量预测（pLDDT=90.3），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008278, IPR037143, IPR055066, IPR050559; Pfam: PF22624, PF01648 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FASN | 0.987 | 0.900 | — |
| AASDH | 0.982 | 0.332 | — |
| COASY | 0.913 | 0.000 | — |
| HAT1 | 0.883 | 0.000 | — |
| MCAT | 0.880 | 0.000 | — |
| TMEM126B | 0.851 | 0.000 | — |
| DLD | 0.845 | 0.071 | — |
| TMEM126A | 0.831 | 0.000 | — |
| H4C6 | 0.811 | 0.000 | — |
| H4C7 | 0.811 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TRAF2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MDFI | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| HLA-B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EIF1B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| SLX4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12200|pubmed:19596235 |
| BABAM1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| USP22 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| ULK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| DLD | psi-mi:"MI:0030"(cross-linking study) | doi:10.1016/j.cels.2017.10.010 |
| SOD1 | psi-mi:"MI:0030"(cross-linking study) | doi:10.1016/j.cels.2017.10.010 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.3 + PDB: 2BYD, 2C43, 2CG5 | pLDDT=90.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. AASDHPPT — L-aminoadipate-semialdehyde dehydrogenase-phosphopantetheinyl transferase，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小309 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NRN7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000149313-AASDHPPT/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AASDHPPT
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NRN7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NRN7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
