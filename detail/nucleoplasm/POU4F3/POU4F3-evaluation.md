---
type: protein-evaluation
gene: "POU4F3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## POU4F3 — REJECTED (研究热度过高 (PubMed strict=119，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | POU4F3 / BRN3C |
| 蛋白名称 | POU domain, class 4, transcription factor 3 |
| 蛋白大小 | 338 aa / 37.1 kDa |
| UniProt ID | Q15319 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 338 aa / 37.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=119 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001356, IPR017970, IPR009057, IPR010982, IPR013 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 10 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.0/180** | |
| **归一化总分** | | | **44.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 119 |
| PubMed broad count | 226 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BRN3C |

**关键文献**:
1. Genetic Hearing Loss Overview.. **. PMID: 20301607
2. Cochlear organoids reveal transcriptional programs of postnatal hair cell differentiation from supporting cells.. *Cell reports*. PMID: 37952154
3. Autosomal Dominant Non-Syndromic Hearing Loss (DFNA): A Comprehensive Narrative Review.. *Biomedicines*. PMID: 37371710
4. AAV-mediated Gene Cocktails Enhance Supporting Cell Reprogramming and Hair Cell Regeneration.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 38810137
5. Optimized in vivo base editing restores auditory function in a DFNA15 mouse model.. *Nature communications*. PMID: 40968144

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.7 |
| 高置信度残基 (pLDDT>90) 占比 | 31.7% |
| 置信残基 (pLDDT 70-90) 占比 | 8.0% |
| 中等置信 (pLDDT 50-70) 占比 | 17.2% |
| 低置信 (pLDDT<50) 占比 | 43.2% |
| 有序区域 (pLDDT>70) 占比 | 39.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=64.7），有序残基占 39.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001356, IPR017970, IPR009057, IPR010982, IPR013847; Pfam: PF00046, PF00157 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GFI1 | 0.907 | 0.045 | — |
| ATOH1 | 0.818 | 0.000 | — |
| MYO7A | 0.796 | 0.000 | — |
| DIAPH1 | 0.674 | 0.000 | — |
| OTOF | 0.631 | 0.000 | — |
| BARHL1 | 0.608 | 0.000 | — |
| SLC26A5 | 0.606 | 0.000 | — |
| TMC1 | 0.604 | 0.045 | — |
| ESPN | 0.604 | 0.000 | — |
| MYO6 | 0.592 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DUSP21 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| KRTAP6-3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| GOLGA2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| NHLRC4 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| PLA2G10 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| KRT31 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ENSP00000495718.1 | psi-mi:"MI:0432"(one hybrid) | imex:IM-25511|pubmed:25910212 |
| SNCG | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| H2AC11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| S100A4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 10
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 10 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.7 + PDB: 无 | pLDDT=64.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 10 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. POU4F3 — POU domain, class 4, transcription factor 3，研究基础较多，新颖性有限。
2. 蛋白大小338 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 119 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=64.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 119 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q15319
- Protein Atlas: https://www.proteinatlas.org/ENSG00000091010-POU4F3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=POU4F3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q15319
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000091010-POU4F3/subcellular

![](https://images.proteinatlas.org/38215/428_H8_1_red_green.jpg)
![](https://images.proteinatlas.org/38215/428_H8_2_red_green.jpg)
![](https://images.proteinatlas.org/38215/433_H8_1_red_green.jpg)
![](https://images.proteinatlas.org/38215/433_H8_2_red_green.jpg)
![](https://images.proteinatlas.org/38215/440_H8_1_red_green.jpg)
![](https://images.proteinatlas.org/38215/440_H8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q15319-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
