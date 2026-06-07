---
type: protein-evaluation
gene: "PAX8"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PAX8 — REJECTED (研究热度过高 (PubMed strict=1190，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PAX8 |
| 蛋白名称 | Paired box protein Pax-8 |
| 蛋白大小 | 450 aa / 48.2 kDa |
| UniProt ID | Q06710 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 450 aa / 48.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1190 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=57.7; PDB: 2K27 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR009057, IPR043182, IPR001523, IPR022130, IPR043 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.5/180** | |
| **归一化总分** | | | **49.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1190 |
| PubMed broad count | 2660 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. METTL3 regulates thyroid cancer differentiation and chemosensitivity by modulating PAX8.. *International journal of biological sciences*. PMID: 38993572
2. Targeting PAX8 sensitizes ovarian cancer cells to ferroptosis by inhibiting glutathione synthesis.. *Apoptosis : an international journal on programmed cell death*. PMID: 38853202
3. Of travelling homeoproteins and medulloblastomas.. *Oncogene*. PMID: 40760093
4. PAX8 Interacts with the SWI/SNF Complex at Enhancers to Drive Proliferation in Ovarian Cancer.. *Molecular cancer research : MCR*. PMID: 39918415
5. Paired-Box Gene 8 (PAX8) and Its Association With Epithelial Carcinomas.. *Cureus*. PMID: 34540435

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 57.7 |
| 高置信度残基 (pLDDT>90) 占比 | 22.7% |
| 置信残基 (pLDDT 70-90) 占比 | 6.4% |
| 中等置信 (pLDDT 50-70) 占比 | 10.9% |
| 低置信 (pLDDT<50) 占比 | 60.0% |
| 有序区域 (pLDDT>70) 占比 | 29.1% |
| 可用 PDB 条目 | 2K27 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=57.7），有序残基占 29.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009057, IPR043182, IPR001523, IPR022130, IPR043565; Pfam: PF00292, PF12403 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PPARG | 0.994 | 0.045 | — |
| NKX2-1 | 0.980 | 0.310 | — |
| FOXE1 | 0.940 | 0.000 | — |
| TG | 0.933 | 0.000 | — |
| PRKCB | 0.918 | 0.000 | — |
| TSHR | 0.917 | 0.000 | — |
| PRKACG | 0.913 | 0.000 | — |
| PRKACA | 0.913 | 0.000 | — |
| PRKACB | 0.913 | 0.000 | — |
| PRKCA | 0.911 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CXCL9 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| PKM | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| CHUK | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| Nkx2-1 | psi-mi:"MI:0663"(confocal microscopy) | pubmed:12441357 |
| Wbp2 | psi-mi:"MI:0084"(phage display) | pubmed:14531730|mint:MINT-5216 |
| ANXA7 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| RPLP2 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| SERINC1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:20195357|imex:IM-20475 |
| HSPA1A | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| NCL | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=57.7 + PDB: 2K27 | pLDDT=57.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. PAX8 — Paired box protein Pax-8，研究基础较多，新颖性有限。
2. 蛋白大小450 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1190 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=57.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1190 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q06710
- Protein Atlas: https://www.proteinatlas.org/ENSG00000125618-PAX8/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PAX8
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q06710
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000125618-PAX8/subcellular

![](https://images.proteinatlas.org/30062/295_D7_1_red_green.jpg)
![](https://images.proteinatlas.org/30062/295_D7_2_red_green.jpg)
![](https://images.proteinatlas.org/30062/296_D7_1_red_green.jpg)
![](https://images.proteinatlas.org/30062/296_D7_2_red_green.jpg)
![](https://images.proteinatlas.org/30062/297_D7_1_red_green.jpg)
![](https://images.proteinatlas.org/30062/297_D7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q06710-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q06710 |
| SMART | SM00351; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR009057;IPR043182;IPR001523;IPR022130;IPR043565;IPR036388; |
| Pfam | PF00292;PF12403; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000125618-PAX8/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AURKA | Biogrid | false |
| CDK3 | Intact | false |
| DOK4 | Intact | false |
| EP300 | Biogrid | false |
| GCM2 | Intact | false |
| HOXC8 | Intact | false |
| HOXC9 | Intact | false |
| LONRF1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
