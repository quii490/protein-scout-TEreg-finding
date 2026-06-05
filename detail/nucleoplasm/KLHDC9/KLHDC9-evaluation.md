---
type: protein-evaluation
gene: "KLHDC9"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KLHDC9 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KLHDC9 / KARCA1 |
| 蛋白名称 | Kelch domain-containing protein 9 |
| 蛋白大小 | 349 aa / 37.8 kDa |
| UniProt ID | Q8NEP7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nucleoli, Nucleoli rim, Mitotic chromosome; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 349 aa / 37.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=92.9; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011043, IPR015915, IPR042941; Pfam: PF24681 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 7 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.0/180** | |
| **归一化总分** | | | **76.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli, Nucleoli rim, Mitotic chromosome | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3 |
| PubMed broad count | 4 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KARCA1 |

**关键文献**:
1. Methylation and transcriptome analysis reveal lung adenocarcinoma-specific diagnostic biomarkers.. *Journal of translational medicine*. PMID: 31558162
2. Gene isoforms as expression-based biomarkers predictive of drug response in vitro.. *Nature communications*. PMID: 29066719
3. Exploration of methylation-driven genes for monitoring and prognosis of patients with lung adenocarcinoma.. *Cancer cell international*. PMID: 30498398

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.9 |
| 高置信度残基 (pLDDT>90) 占比 | 86.0% |
| 置信残基 (pLDDT 70-90) 占比 | 10.0% |
| 中等置信 (pLDDT 50-70) 占比 | 0.6% |
| 低置信 (pLDDT<50) 占比 | 3.4% |
| 有序区域 (pLDDT>70) 占比 | 96.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=92.9，有序区 96.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011043, IPR015915, IPR042941; Pfam: PF24681 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CCDC190 | 0.675 | 0.000 | — |
| ARHGAP30 | 0.582 | 0.000 | — |
| SLAMF8 | 0.535 | 0.000 | — |
| PROCA1 | 0.502 | 0.000 | — |
| DRG1 | 0.471 | 0.471 | — |
| NECTIN4 | 0.467 | 0.051 | — |
| GPS2 | 0.462 | 0.000 | — |
| C15orf40 | 0.446 | 0.439 | — |
| INCA1 | 0.446 | 0.000 | — |
| POLE2 | 0.439 | 0.439 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GLRX3 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| CTSA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GLB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| THOC3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DOCK7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NT5DC2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CEACAM8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 7
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 7 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.9 + PDB: 无 | pLDDT=92.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Nucleoli, Nucleoli rim, Mitotic chrom | 待确认 |
| PPI | STRING + IntAct | 15 + 7 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. KLHDC9 — Kelch domain-containing protein 9，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小349 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NEP7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000162755-KLHDC9/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KLHDC9
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NEP7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000162755-KLHDC9/subcellular

![](https://images.proteinatlas.org/43197/1829_B2_8_red_green.jpg)
![](https://images.proteinatlas.org/43197/1829_B2_9_red_green.jpg)
![](https://images.proteinatlas.org/43197/1909_C4_2_red_green.jpg)
![](https://images.proteinatlas.org/43197/1909_C4_4_red_green.jpg)
![](https://images.proteinatlas.org/43197/2014_B5_2_red_green.jpg)
![](https://images.proteinatlas.org/43197/2014_B5_5_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8NEP7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
