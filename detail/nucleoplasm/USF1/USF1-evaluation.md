---
type: protein-evaluation
gene: "USF1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## USF1 — REJECTED (研究热度过高 (PubMed strict=549，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | USF1 / BHLHB11, USF |
| 蛋白名称 | Upstream stimulatory factor 1 |
| 蛋白大小 | 310 aa / 33.5 kDa |
| UniProt ID | P22415 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 310 aa / 33.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=549 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.9; PDB: 1AN4 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011598, IPR036638, IPR051732; Pfam: PF00010 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.5/180** | |
| **归一化总分** | | | **44.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- Golgi apparatus (GO:0005794)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- transcription regulator complex (GO:0005667)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 549 |
| PubMed broad count | 816 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BHLHB11, USF |

**关键文献**:
1. The ménage à trois of autophagy, lipid droplets and liver disease.. *Autophagy*. PMID: 33794741
2. Inhibition of DUSP18 impairs cholesterol biosynthesis and promotes anti-tumor immunity in colorectal cancer.. *Nature communications*. PMID: 38992029
3. Exosomal LOC85009 inhibits docetaxel resistance in lung adenocarcinoma through regulating ATG5-induced autophagy.. *Drug resistance updates : reviews and commentaries in antimicrobial and anticancer chemotherapy*. PMID: 36641841
4. HOXA9 Regulome and Pharmacological Interventions in Leukemia.. *Advances in experimental medicine and biology*. PMID: 39017854
5. Identify the co-expressed genes of hypertensive nephropathy and diabetic nephropathy.. *Scientific reports*. PMID: 40461634

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.9 |
| 高置信度残基 (pLDDT>90) 占比 | 27.7% |
| 置信残基 (pLDDT 70-90) 占比 | 4.5% |
| 中等置信 (pLDDT 50-70) 占比 | 18.1% |
| 低置信 (pLDDT<50) 占比 | 49.7% |
| 有序区域 (pLDDT>70) 占比 | 32.2% |
| 可用 PDB 条目 | 1AN4 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=60.9），有序残基占 32.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011598, IPR036638, IPR051732; Pfam: PF00010 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| USF2 | 0.999 | 0.889 | — |
| GTF2I | 0.958 | 0.735 | — |
| EP300 | 0.912 | 0.301 | — |
| SP1 | 0.901 | 0.053 | — |
| FOSL1 | 0.846 | 0.645 | — |
| SMARCD3 | 0.819 | 0.075 | — |
| TAF7 | 0.814 | 0.325 | — |
| MED1 | 0.801 | 0.000 | — |
| ESR1 | 0.796 | 0.053 | — |
| RFX5 | 0.752 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000357000.3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| USF2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| KAT2B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12076|pubmed:19303849 |
| PPP1CC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12076|pubmed:19303849 |
| HDAC9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12076|pubmed:19303849 |
| XRCC5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12076|pubmed:19303849 |
| TOP2B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12076|pubmed:19303849 |
| XRCC6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12076|pubmed:19303849 |
| PRKDC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12076|pubmed:19303849 |
| PARP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12076|pubmed:19303849 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.9 + PDB: 1AN4 | pLDDT=60.9, v6 | 预测+实验 |
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
1. USF1 — Upstream stimulatory factor 1，研究基础较多，新颖性有限。
2. 蛋白大小310 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 549 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=60.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 549 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P22415
- Protein Atlas: https://www.proteinatlas.org/ENSG00000158773-USF1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=USF1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P22415
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000158773-USF1/subcellular

![](https://images.proteinatlas.org/1480/924_C8_1_red_green.jpg)
![](https://images.proteinatlas.org/1480/924_C8_2_red_green.jpg)
![](https://images.proteinatlas.org/1480/932_C8_1_red_green.jpg)
![](https://images.proteinatlas.org/1480/932_C8_3_red_green.jpg)
![](https://images.proteinatlas.org/1480/971_C8_1_red_green.jpg)
![](https://images.proteinatlas.org/1480/971_C8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P22415-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
