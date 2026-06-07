---
type: protein-evaluation
gene: "CREBBP"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CREBBP — REJECTED (研究热度过高 (PubMed strict=838，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CREBBP / CBP |
| 蛋白名称 | CREB-binding protein |
| 蛋白大小 | 2442 aa / 265.4 kDa |
| UniProt ID | Q92793 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nuclear bodies; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 2/10 | ×1 | 2 | 2442 aa / 265.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=838 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=52.5; PDB: 1JSP, 1LIQ, 1RDT, 1WO3, 1WO4, 1WO5, 1WO6 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001487, IPR036427, IPR018359, IPR031162, IPR013 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **73.5/180** | |
| **归一化总分** | | | **40.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear bodies | Enhanced |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- histone acetyltransferase complex (GO:0000123)
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- transcription regulator complex (GO:0005667)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 838 |
| PubMed broad count | 2603 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CBP |

**关键文献**:
1. Follicular lymphoma t(14;18)-negative is genetically a heterogeneous disease.. *Blood advances*. PMID: 33211828
2. Rubinstein-Taybi Syndrome.. **. PMID: 20301699
3. Histone lysine acetyltransferase inhibitors: an emerging class of drugs for cancer therapy.. *Trends in pharmacological sciences*. PMID: 38383216
4. Evolutionary trajectories of small cell lung cancer under therapy.. *Nature*. PMID: 38480884
5. CREBBP/EP300 mutations promoted tumor progression in diffuse large B-cell lymphoma through altering tumor-associated macrophage polarization via FBXW7-NOTCH-CCL2/CSF1 axis.. *Signal transduction and targeted therapy*. PMID: 33431788

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 52.5 |
| 高置信度残基 (pLDDT>90) 占比 | 18.3% |
| 置信残基 (pLDDT 70-90) 占比 | 14.5% |
| 中等置信 (pLDDT 50-70) 占比 | 5.8% |
| 低置信 (pLDDT<50) 占比 | 61.4% |
| 有序区域 (pLDDT>70) 占比 | 32.8% |
| 可用 PDB 条目 | 1JSP, 1LIQ, 1RDT, 1WO3, 1WO4, 1WO5, 1WO6, 1WO7, 1ZOQ, 2D82 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=52.5），有序残基占 32.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001487, IPR036427, IPR018359, IPR031162, IPR013178; Pfam: PF00439, PF09030, PF08214 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MYB | 0.999 | 0.984 | — |
| CTNNB1 | 0.999 | 0.886 | — |
| IRF3 | 0.999 | 0.944 | — |
| NCOA3 | 0.999 | 0.987 | — |
| KAT2B | 0.999 | 0.793 | — |
| STAT1 | 0.999 | 0.983 | — |
| NCOA1 | 0.999 | 0.984 | — |
| HIF1A | 0.999 | 0.991 | — |
| CREB1 | 0.999 | 0.996 | — |
| RELA | 0.999 | 0.991 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TP53 | psi-mi:"MI:0096"(pull down) | pubmed:9194564 |
| NCOA6 | psi-mi:"MI:0096"(pull down) | pubmed:10866662 |
| DAXX | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:11799127 |
| KHDRBS1 | psi-mi:"MI:0428"(imaging technique) | pubmed:12496368 |
| RELA | psi-mi:"MI:0096"(pull down) | imex:IM-14434|pubmed:16291753 |
| NAP1L1 | psi-mi:"MI:0018"(two hybrid) | pubmed:11940655|imex:IM-19548 |
| CTNNB1 | psi-mi:"MI:0018"(two hybrid) | pubmed:21751375|imex:IM-16570 |
| vIRF-1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:22810585|imex:IM-17331 |
| IFNAR2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-11864|pubmed:17923090 |
| RPA2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17525332|imex:IM-19727 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=52.5 + PDB: 1JSP, 1LIQ, 1RDT, 1WO3, 1WO4,  | pLDDT=52.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm, Nuclear bodies | 一致 |
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
1. CREBBP — CREB-binding protein，研究基础较多，新颖性有限。
2. 蛋白大小2442 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 838 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=52.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 838 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q92793
- Protein Atlas: https://www.proteinatlas.org/ENSG00000005339-CREBBP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CREBBP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q92793
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000005339-CREBBP/subcellular

![](https://images.proteinatlas.org/4212/653_C5_1_red_green.jpg)
![](https://images.proteinatlas.org/4212/653_C5_3_red_green.jpg)
![](https://images.proteinatlas.org/4212/658_C5_1_red_green.jpg)
![](https://images.proteinatlas.org/4212/658_C5_3_red_green.jpg)
![](https://images.proteinatlas.org/4212/659_C5_1_red_green.jpg)
![](https://images.proteinatlas.org/4212/659_C5_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q92793-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q92793 |
| SMART | SM00297;SM01250;SM00551;SM00291; |
| UniProt Domain [FT] | DOMAIN 587..666; /note="KIX"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00311"; DOMAIN 1085..1192; /note="Bromo"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00035"; DOMAIN 1323..1700; /note="CBP/p300-type HAT"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01065" |
| InterPro | IPR001487;IPR036427;IPR018359;IPR031162;IPR013178;IPR003101;IPR036529;IPR009110;IPR014744;IPR037073;IPR056484;IPR010303;IPR038547;IPR035898;IPR013083;IPR000197;IPR000433;IPR043145; |
| Pfam | PF00439;PF09030;PF08214;PF02172;PF23570;PF06001;PF02135;PF00569; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000005339-CREBBP/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AKT1 | Intact, Biogrid | true |
| AR | Intact, Biogrid | true |
| CREB1 | Intact, Biogrid | true |
| CSNK2A1 | Biogrid, Opencell | true |
| CSNK2A2 | Biogrid, Opencell | true |
| CTNNB1 | Intact, Biogrid | true |
| DAXX | Intact, Biogrid | true |
| FOXO1 | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
