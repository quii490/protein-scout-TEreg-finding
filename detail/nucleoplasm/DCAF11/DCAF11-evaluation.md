---
type: protein-evaluation
gene: "DCAF11"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DCAF11 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DCAF11 / WDR23 |
| 蛋白名称 | DDB1- and CUL4-associated factor 11 |
| 蛋白大小 | 546 aa / 61.7 kDa |
| UniProt ID | Q8TEB1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | x4 | 32 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | x1 | 10 | 546 aa / 61.7 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=22 篇 (≤40→8) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=82.7; PDB: 无 |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR051859, IPR017399, IPR015943, IPR020472, IPR036 |
| PPI 网络 | 2/10 | x3 | 6 | STRING 0 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.0/180** | |
| **归一化总分** | | | **70.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- Cul4-RING E3 ubiquitin ligase complex (GO:0080008)
- nucleoplasm (GO:0005654)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 22 |
| PubMed broad count | 28 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: WDR23 |

**关键文献**:
1. Targeted protein degradation via intramolecular bivalent glues.. *Nature*. PMID: 38383787
2. Discovery of electrophilic degraders that exploit S(N)Ar chemistry.. *bioRxiv : the preprint server for biology*. PMID: 39386645
3. Chemical Specification of E3 Ubiquitin Ligase Engagement by Cysteine-Reactive Chemistry.. *Journal of the American Chemical Society*. PMID: 37767920
4. Regulating Nrf2 activity: ubiquitin ligases and signaling molecules in redox homeostasis.. *Trends in biochemical sciences*. PMID: 39875264
5. Discovery of a Drug-like, Natural Product-Inspired DCAF11 Ligand Chemotype.. *Nature communications*. PMID: 38036533

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.7 |
| 高置信度残基 (pLDDT>90) 占比 | 64.3% |
| 置信残基 (pLDDT 70-90) 占比 | 13.6% |
| 中等置信 (pLDDT 50-70) 占比 | 6.0% |
| 低置信 (pLDDT<50) 占比 | 16.1% |
| 有序区域 (pLDDT>70) 占比 | 77.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=82.7，有序区 77.9%）。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051859, IPR017399, IPR015943, IPR020472, IPR036322; Pfam: PF00400 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高。

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
| 三维结构 | AlphaFold pLDDT=82.7 + PDB: 无 | pLDDT=82.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 0 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DCAF11 -- DDB1- and CUL4-associated factor 11，非常新颖，仅有少数基础研究。
2. 蛋白大小546 aa，大小适中（200-800 aa），适合常规生化实验。

**风险/不确定性**:
1. PubMed 22 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TEB1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100897-DCAF11/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DCAF11
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TEB1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000100897-DCAF11/subcellular

![](https://images.proteinatlas.org/31157/402_E5_1_red_green.jpg)
![](https://images.proteinatlas.org/31157/402_E5_2_red_green.jpg)
![](https://images.proteinatlas.org/31157/405_E5_3_red_green.jpg)
![](https://images.proteinatlas.org/31157/405_E5_4_red_green.jpg)
![](https://images.proteinatlas.org/31157/409_E5_1_red_green.jpg)
![](https://images.proteinatlas.org/31157/409_E5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8TEB1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
