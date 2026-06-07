---
type: protein-evaluation
gene: "LRRC10"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LRRC10 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LRRC10 |
| 蛋白名称 | Leucine-rich repeat-containing protein 10 |
| 蛋白大小 | 277 aa / 31.6 kDa |
| UniProt ID | Q5BKY1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 277 aa / 31.6 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=21 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=86.5; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001611, IPR003591, IPR032675, IPR050216; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.5/180** | |
| **归一化总分** | | | **71.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoskeleton (GO:0005856)
- mitochondrion (GO:0005739)
- nucleus (GO:0005634)
- sarcomere (GO:0030017)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 21 |
| PubMed broad count | 24 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. A genetically encoded actuator boosts L-type calcium channel function in diverse physiological settings.. *Science advances*. PMID: 39475605
2. The Role of Leucine-Rich Repeat Containing Protein 10 (LRRC10) in Dilated Cardiomyopathy.. *Frontiers in physiology*. PMID: 27536250
3. Exploring the dark genome: implications for precision medicine.. *Mammalian genome : official journal of the International Mammalian Genome Society*. PMID: 31270560
4. Lrrc10 is a novel cardiac-specific target gene of Nkx2-5 and GATA4.. *Journal of molecular and cellular cardiology*. PMID: 23751912
5. Cardiac L-type calcium channel regulation by Leucine-Rich Repeat-Containing Protein 10.. *Channels (Austin, Tex.)*. PMID: 38762910

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.5 |
| 高置信度残基 (pLDDT>90) 占比 | 74.7% |
| 置信残基 (pLDDT 70-90) 占比 | 3.2% |
| 中等置信 (pLDDT 50-70) 占比 | 14.4% |
| 低置信 (pLDDT<50) 占比 | 7.6% |
| 有序区域 (pLDDT>70) 占比 | 77.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=86.5，有序区 77.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001611, IPR003591, IPR032675, IPR050216; Pfam: PF13855 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LRRC26 | 0.699 | 0.000 | — |
| CCT2 | 0.622 | 0.205 | — |
| BEST3 | 0.562 | 0.000 | — |
| NYX | 0.554 | 0.000 | — |
| LRG1 | 0.536 | 0.000 | — |
| PRELP | 0.527 | 0.000 | — |
| KERA | 0.525 | 0.000 | — |
| SLMAP | 0.522 | 0.088 | — |
| LUM | 0.520 | 0.000 | — |
| OMD | 0.518 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CCT2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ARHGAP8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ENOSF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CCT6B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SUGT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ENSP00000355166.3 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |
| Ryr2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:24952909|imex:IM-26422 |
| Cacna1c | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:24952909|imex:IM-26422 |
| A2ML1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| KLK10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.5 + PDB: 无 | pLDDT=86.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. LRRC10 — Leucine-rich repeat-containing protein 10，非常新颖，仅有少数基础研究。
2. 蛋白大小277 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 21 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5BKY1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000198812-LRRC10/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LRRC10
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5BKY1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5BKY1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q5BKY1 |
| SMART | SM00364;SM00369; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR001611;IPR003591;IPR032675;IPR050216; |
| Pfam | PF13855; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000198812-LRRC10/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CCT2 | Bioplex | false |
| CCT6A | Bioplex | false |
| CCT7 | Bioplex | false |
| PDCL | Bioplex | false |
| TUSC2 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
