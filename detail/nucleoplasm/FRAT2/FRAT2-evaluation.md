---
type: protein-evaluation
gene: "FRAT2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FRAT2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FRAT2 |
| 蛋白名称 | GSK-3-binding protein FRAT2 |
| 蛋白大小 | 233 aa / 24.1 kDa |
| UniProt ID | O75474 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Mitochondria; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 233 aa / 24.1 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=24 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR008014; Pfam: PF05350 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.0/180** | |
| **归一化总分** | | | **66.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Mitochondria | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 24 |
| PubMed broad count | 38 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Characterization and functional analysis of the murine Frat2 gene.. *The Journal of biological chemistry*. PMID: 15073180
2. TMEM98 is a negative regulator of FRAT mediated Wnt/ß-catenin signalling.. *PloS one*. PMID: 31961879
3. Molecular cloning and characterization of FRAT2, encoding a positive regulator of the WNT signaling pathway.. *Biochemical and biophysical research communications*. PMID: 11237732
4. WNT signaling pathway regulator-FRAT2 affects oncogenesis and prognosis of basal-like breast cancer.. *Journal of thoracic disease*. PMID: 32802426
5. Frat2 mediates the oncogenic activation of Rac by MLL fusions.. *Blood*. PMID: 23074275

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.1 |
| 高置信度残基 (pLDDT>90) 占比 | 15.9% |
| 置信残基 (pLDDT 70-90) 占比 | 13.3% |
| 中等置信 (pLDDT 50-70) 占比 | 36.5% |
| 低置信 (pLDDT<50) 占比 | 34.3% |
| 有序区域 (pLDDT>70) 占比 | 29.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=62.1），有序残基占 29.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008014; Pfam: PF05350 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GSK3B | 0.987 | 0.608 | — |
| FRAT1 | 0.951 | 0.000 | — |
| DVL3 | 0.924 | 0.000 | — |
| DVL1 | 0.920 | 0.000 | — |
| DVL2 | 0.904 | 0.000 | — |
| CTNNB1 | 0.729 | 0.000 | — |
| GSK3A | 0.611 | 0.398 | — |
| AXIN1 | 0.578 | 0.000 | — |
| PHLDA1 | 0.578 | 0.000 | — |
| FZD10 | 0.548 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GSK3B | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-17578|pubmed:23455922 |
| Xpo1 | psi-mi:"MI:0096"(pull down) | pubmed:26673895|imex:IM-24970 |
| CEP170P1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| S100A2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| GSK3A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| FCGRT | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| FAAP100 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CEP170 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TRPC4AP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SYNE2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.1 + PDB: 无 | pLDDT=62.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Mitochondria | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FRAT2 — GSK-3-binding protein FRAT2，非常新颖，仅有少数基础研究。
2. 蛋白大小233 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 24 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=62.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75474
- Protein Atlas: https://www.proteinatlas.org/ENSG00000181274-FRAT2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FRAT2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75474
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000181274-FRAT2/subcellular

![](https://images.proteinatlas.org/49763/765_H8_1_red_green.jpg)
![](https://images.proteinatlas.org/49763/765_H8_2_red_green.jpg)
![](https://images.proteinatlas.org/49763/771_H8_1_red_green.jpg)
![](https://images.proteinatlas.org/49763/771_H8_2_red_green.jpg)
![](https://images.proteinatlas.org/49763/979_C10_1_red_green.jpg)
![](https://images.proteinatlas.org/49763/979_C10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O75474-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O75474 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR008014; |
| Pfam | PF05350; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000181274-FRAT2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| GSK3A | Bioplex | false |
| GSK3B | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
