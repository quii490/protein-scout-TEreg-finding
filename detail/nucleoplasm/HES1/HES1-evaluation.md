---
type: protein-evaluation
gene: "HES1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## HES1 — REJECTED (研究热度过高 (PubMed strict=2001，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HES1 / BHLHB39, HL, HRY |
| 蛋白名称 | Transcription factor HES-1 |
| 蛋白大小 | 280 aa / 29.5 kDa |
| UniProt ID | Q14469 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 280 aa / 29.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=2001 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.6; PDB: 2MH3, 7C4O |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011598, IPR050370, IPR036638, IPR003650; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.5/180** | |
| **归一化总分** | | | **44.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- nuclear matrix (GO:0016363)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- protein-containing complex (GO:0032991)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2001 |
| PubMed broad count | 3395 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BHLHB39, HL, HRY |

**关键文献**:
1. A natural small molecule alleviates liver fibrosis by targeting apolipoprotein L2.. *Nature chemical biology*. PMID: 39103634
2. Hes1: the maestro in neurogenesis.. *Cellular and molecular life sciences : CMLS*. PMID: 27233500
3. Oscillations, clocks and segmentation.. *Current opinion in genetics & development*. PMID: 12888011
4. The IGF2BP3/Notch/Jag1 pathway: A key regulator of hepatic stellate cell ferroptosis in liver fibrosis.. *Clinical and translational medicine*. PMID: 39113232
5. Disrupting Notch signaling related HES1 in myeloid cells reinvigorates antitumor T cell responses.. *Experimental hematology & oncology*. PMID: 39702544

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.6 |
| 高置信度残基 (pLDDT>90) 占比 | 25.7% |
| 置信残基 (pLDDT 70-90) 占比 | 21.8% |
| 中等置信 (pLDDT 50-70) 占比 | 29.6% |
| 低置信 (pLDDT<50) 占比 | 22.9% |
| 有序区域 (pLDDT>70) 占比 | 47.5% |
| 可用 PDB 条目 | 2MH3, 7C4O |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=68.6），有序残基占 47.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011598, IPR050370, IPR036638, IPR003650; Pfam: PF07527, PF00010 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FANCF | 0.999 | 0.994 | — |
| FANCA | 0.999 | 0.994 | — |
| FANCG | 0.999 | 0.994 | — |
| FANCL | 0.999 | 0.994 | — |
| FANCC | 0.998 | 0.994 | — |
| FANCE | 0.998 | 0.994 | — |
| NEUROG3 | 0.971 | 0.064 | — |
| TLE1 | 0.953 | 0.872 | — |
| RBPJ | 0.946 | 0.737 | — |
| FANCD2 | 0.933 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ASGR2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| LTBR | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| SSA1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SSA2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SSB1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SSE1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| moeA2 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| A0A384KY07 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| APH1A | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| RBPJ | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | imex:IM-26501|pubmed:24244701 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.6 + PDB: 2MH3, 7C4O | pLDDT=68.6, v6 | 预测+实验 |
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
1. HES1 — Transcription factor HES-1，研究基础较多，新颖性有限。
2. 蛋白大小280 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2001 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=68.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 2001 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q14469
- Protein Atlas: https://www.proteinatlas.org/ENSG00000114315-HES1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HES1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q14469
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000114315-HES1/subcellular

![](https://images.proteinatlas.org/66929/1346_B6_3_red_green.jpg)
![](https://images.proteinatlas.org/66929/1346_B6_5_red_green.jpg)
![](https://images.proteinatlas.org/66929/1351_B6_5_red_green.jpg)
![](https://images.proteinatlas.org/66929/1351_B6_6_red_green.jpg)
![](https://images.proteinatlas.org/66929/1765_A1_1_red_green.jpg)
![](https://images.proteinatlas.org/66929/1765_A1_6_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q14469-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
