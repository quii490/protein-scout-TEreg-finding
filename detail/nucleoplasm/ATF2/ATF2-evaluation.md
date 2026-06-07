---
type: protein-evaluation
gene: "ATF2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ATF2 — REJECTED (研究热度过高 (PubMed strict=1408，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ATF2 / CREB2, CREBP1 |
| 蛋白名称 | Cyclic AMP-dependent transcription factor ATF-2 |
| 蛋白大小 | 505 aa / 54.5 kDa |
| UniProt ID | P15336 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Cytoplasm; Mitochondrion outer membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 505 aa / 54.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1408 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=57.8; PDB: 1BHI, 1T2K, 4H36, 6ZQS, 6ZR5, 8YPE, 8YPF |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR004827, IPR046347, IPR051027, IPR016378, IPR036 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **78.0/180** | |
| **归一化总分** | | | **43.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus; Cytoplasm; Mitochondrion outer membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- H4 histone acetyltransferase complex (GO:1902562)
- mitochondrial outer membrane (GO:0005741)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- RNA polymerase II transcription regulator complex (GO:0090575)
- site of double-strand break (GO:0035861)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1408 |
| PubMed broad count | 1918 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CREB2, CREBP1 |

**关键文献**:
1. Hepatocyte-derived MASP1-enriched small extracellular vesicles activate HSCs to promote liver fibrosis.. *Hepatology (Baltimore, Md.)*. PMID: 35849032
2. Increased ATF2 expression predicts poor prognosis and inhibits sorafenib-induced ferroptosis in gastric cancer.. *Redox biology*. PMID: 36473315
3. MG53 protects against septic cardiac dysfunction by ubiquitinating ATF2.. *Journal of advanced research*. PMID: 40107350
4. SIRT6 Lysine-Demyristoylates ATF2 to Ameliorate Vascular Injury via PRKCD/VE-Cadherin Pathway Regulating Vascular Endothelial Barrier.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 40810740
5. ATF2/BAP1 Axis Mediates Neuronal Apoptosis After Subarachnoid Hemorrhage via P53 Pathway.. *Stroke*. PMID: 38965653

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 57.8 |
| 高置信度残基 (pLDDT>90) 占比 | 13.1% |
| 置信残基 (pLDDT 70-90) 占比 | 12.1% |
| 中等置信 (pLDDT 50-70) 占比 | 25.1% |
| 低置信 (pLDDT<50) 占比 | 49.7% |
| 有序区域 (pLDDT>70) 占比 | 25.2% |
| 可用 PDB 条目 | 1BHI, 1T2K, 4H36, 6ZQS, 6ZR5, 8YPE, 8YPF |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=57.8），有序残基占 25.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004827, IPR046347, IPR051027, IPR016378, IPR036236; Pfam: PF00170 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 无PPI数据
- STRING partners: 0，IntAct interactions: 0
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=57.8 + PDB: 1BHI, 1T2K, 4H36, 6ZQS, 6ZR5,  | pLDDT=57.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Mitochondrion outer membrane / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 0 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. ATF2 — Cyclic AMP-dependent transcription factor ATF-2，研究基础较多，新颖性有限。
2. 蛋白大小505 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1408 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=57.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1408 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P15336
- Protein Atlas: https://www.proteinatlas.org/ENSG00000115966-ATF2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ATF2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P15336
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000115966-ATF2/subcellular

![](https://images.proteinatlas.org/22134/189_B4_1_red_green.jpg)
![](https://images.proteinatlas.org/22134/189_B4_2_red_green.jpg)
![](https://images.proteinatlas.org/22134/190_B4_1_red_green.jpg)
![](https://images.proteinatlas.org/22134/190_B4_2_red_green.jpg)
![](https://images.proteinatlas.org/22134/191_B4_1_red_green.jpg)
![](https://images.proteinatlas.org/22134/191_B4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P15336-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P15336 |
| SMART | SM00338; |
| UniProt Domain [FT] | DOMAIN 352..415; /note="bZIP"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00978" |
| InterPro | IPR004827;IPR046347;IPR051027;IPR016378;IPR036236;IPR013087; |
| Pfam | PF00170; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000115966-ATF2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ATF3 | Intact, Biogrid | true |
| BACH1 | Intact, Biogrid, Bioplex | true |
| BATF3 | Intact, Biogrid, Bioplex | true |
| CEBPG | Intact, Biogrid | true |
| CENPQ | Intact, Biogrid | true |
| FOS | Intact, Biogrid, Bioplex | true |
| FOSB | Intact, Biogrid, Bioplex | true |
| FOSL1 | Intact, Biogrid, Bioplex | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
