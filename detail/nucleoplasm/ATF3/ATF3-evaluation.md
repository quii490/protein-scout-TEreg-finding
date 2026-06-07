---
type: protein-evaluation
gene: "ATF3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ATF3 — REJECTED (研究热度过高 (PubMed strict=1809，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ATF3 |
| 蛋白名称 | Cyclic AMP-dependent transcription factor ATF-3 |
| 蛋白大小 | 181 aa / 20.6 kDa |
| UniProt ID | P18847 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nucleoli, Basal body; 额外: Vesicles, Centrosome; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 181 aa / 20.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1809 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=75.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000837, IPR004827, IPR046347; Pfam: PF00170 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.0/180** | |
| **归一化总分** | | | **45.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli, Basal body; 额外: Vesicles, Centrosome | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centrosome (GO:0005813)
- CHOP-ATF3 complex (GO:1990622)
- chromatin (GO:0000785)
- ciliary basal body (GO:0036064)
- Golgi apparatus (GO:0005794)
- nuclear body (GO:0016604)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1809 |
| PubMed broad count | 2773 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Atf3-mediated metabolic reprogramming in hepatic macrophage orchestrates metabolic dysfunction-associated steatohepatitis.. *Science advances*. PMID: 39047111
2. HIF1α/ATF3 partake in PGK1 K191/K192 succinylation by modulating P4HA1/succinate signaling in glioblastoma.. *Neuro-oncology*. PMID: 38441561
3. Spatiotemporal ATF3 Expression Determines VSMC Fate in Abdominal Aortic Aneurysm.. *Circulation research*. PMID: 38686580
4. ATF3 Deficiency Exacerbates Ageing-Induced Atherosclerosis and Clinical Intervention Strategy.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 40641410
5. Integrator loss leads to dsRNA formation that triggers the integrated stress response.. *Cell*. PMID: 40233738

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.9 |
| 高置信度残基 (pLDDT>90) 占比 | 37.0% |
| 置信残基 (pLDDT 70-90) 占比 | 27.6% |
| 中等置信 (pLDDT 50-70) 占比 | 14.4% |
| 低置信 (pLDDT<50) 占比 | 21.0% |
| 有序区域 (pLDDT>70) 占比 | 64.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=75.9，有序区 64.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000837, IPR004827, IPR046347; Pfam: PF00170 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| JUN | 0.999 | 0.931 | — |
| FOS | 0.994 | 0.353 | — |
| JUND | 0.994 | 0.684 | — |
| ATF4 | 0.989 | 0.622 | — |
| SMAD3 | 0.988 | 0.510 | — |
| DDIT3 | 0.988 | 0.877 | — |
| TP53 | 0.982 | 0.743 | — |
| CEBPB | 0.980 | 0.492 | — |
| JUNB | 0.964 | 0.774 | — |
| MDM2 | 0.942 | 0.823 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.9 + PDB: 无 | pLDDT=75.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Nucleoli, Basal body; 额外: Vesicles, C | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. ATF3 — Cyclic AMP-dependent transcription factor ATF-3，研究基础较多，新颖性有限。
2. 蛋白大小181 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 1809 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1809 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P18847
- Protein Atlas: https://www.proteinatlas.org/ENSG00000162772-ATF3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ATF3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P18847
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000162772-ATF3/subcellular

![](https://images.proteinatlas.org/1562/2265_G6_112_blue_red_green.jpg)
![](https://images.proteinatlas.org/1562/2265_G6_136_blue_red_green.jpg)
![](https://images.proteinatlas.org/1562/2232_H4_22_red_green.jpg)
![](https://images.proteinatlas.org/1562/2232_H4_35_red_green.jpg)
![](https://images.proteinatlas.org/1562/2234_G4_13_red_green.jpg)
![](https://images.proteinatlas.org/1562/2234_G4_58_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P18847-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P18847 |
| SMART | SM00338; |
| UniProt Domain [FT] | DOMAIN 86..149; /note="bZIP"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00978" |
| InterPro | IPR000837;IPR004827;IPR046347; |
| Pfam | PF00170; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000162772-ATF3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ATF2 | Intact, Biogrid | true |
| ATF4 | Intact, Biogrid | true |
| DDIT3 | Intact, Biogrid | true |
| FHL2 | Intact, Biogrid | true |
| JUN | Intact, Biogrid, Opencell | true |
| JUNB | Intact, Biogrid | true |
| JUND | Intact, Biogrid | true |
| NFE2L2 | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
