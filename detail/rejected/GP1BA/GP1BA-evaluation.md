---
type: protein-evaluation
gene: "GP1BA"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GP1BA — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=117，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GP1BA |
| 蛋白名称 | Platelet glycoprotein Ib alpha chain |
| 蛋白大小 | 652 aa / 71.5 kDa |
| UniProt ID | P07359 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 652 aa / 71.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=117 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.3; PDB: 1GWB, 1M0Z, 1M10, 1OOK, 1P8V, 1P9A, 1QYY |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000483, IPR001611, IPR003591, IPR032675, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 9 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **61.5/180** | |
| **归一化总分** | | | **34.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cell surface (GO:0009986)
- external side of plasma membrane (GO:0009897)
- extracellular exosome (GO:0070062)
- glycoprotein Ib-IX-V complex (GO:1990779)
- membrane (GO:0016020)
- plasma membrane (GO:0005886)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 117 |
| PubMed broad count | 179 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Differential Impact In Vivo of Pf4-ΔCre-Mediated and Gp1ba-ΔCre-Mediated Depletion of Cyclooxygenase-1 in Platelets in Mice.. *Arteriosclerosis, thrombosis, and vascular biology*. PMID: 38660804
2. Gene of the issue: GP1BA gene mutations associated with bleeding.. *Platelets*. PMID: 28961024
3. Characterization of zebrafish gp1ba mutant and modelling Bernard Soulier syndrome.. *Blood coagulation & fibrinolysis : an international journal in haemostasis and thrombosis*. PMID: 35802508
4. Murine hematopoietic progenitor cell lines with erythroid and megakaryocyte potential.. *Nature communications*. PMID: 40775216
5. Revealing Causal Protein Biomarkers and Potential Therapeutic Targets for Histologic-Specific Lung Cancer.. *Journal of cellular and molecular medicine*. PMID: 41340014

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.3 |
| 高置信度残基 (pLDDT>90) 占比 | 37.1% |
| 置信残基 (pLDDT 70-90) 占比 | 7.4% |
| 中等置信 (pLDDT 50-70) 占比 | 8.4% |
| 低置信 (pLDDT<50) 占比 | 47.1% |
| 有序区域 (pLDDT>70) 占比 | 44.5% |
| 可用 PDB 条目 | 1GWB, 1M0Z, 1M10, 1OOK, 1P8V, 1P9A, 1QYY, 1SQ0, 1U0N, 2BP3 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=64.3），有序残基占 44.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000483, IPR001611, IPR003591, IPR032675, IPR000372; Pfam: PF13855, PF01462 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| VWF | 0.999 | 0.982 | — |
| GP9 | 0.999 | 0.783 | — |
| FLNA | 0.999 | 0.967 | — |
| GP1BB | 0.999 | 0.651 | — |
| SELP | 0.999 | 0.294 | — |
| F2 | 0.992 | 0.946 | — |
| ITGAM | 0.982 | 0.050 | — |
| GP5 | 0.979 | 0.292 | — |
| YWHAZ | 0.979 | 0.840 | — |
| ITGB2 | 0.978 | 0.057 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| F2 | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:12855810 |
| VWF | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:15039442 |
| FLNA | psi-mi:"MI:0813"(proximity ligation assay) | pubmed:25241761|imex:IM-18707 |
| F12 | psi-mi:"MI:0813"(proximity ligation assay) | pubmed:25241761|imex:IM-18707 |
| NECTIN2 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:29997244|imex:IM-26441| |
| GP1BB | psi-mi:"MI:0227"(reverse phase chromatography) | pubmed:18674540|imex:IM-24276 |
| GP9 | psi-mi:"MI:0227"(reverse phase chromatography) | pubmed:18674540|imex:IM-24276 |
| S | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-29399|pubmed:34964720 |
| ECE1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-30316|pubmed:38413612| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 9
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 9 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.3 + PDB: 1GWB, 1M0Z, 1M10, 1OOK, 1P8V,  | pLDDT=64.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 9 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. GP1BA — Platelet glycoprotein Ib alpha chain，研究基础较多，新颖性有限。
2. 蛋白大小652 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 117 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=64.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P07359
- Protein Atlas: https://www.proteinatlas.org/ENSG00000185245-GP1BA/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GP1BA
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P07359
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P07359-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
