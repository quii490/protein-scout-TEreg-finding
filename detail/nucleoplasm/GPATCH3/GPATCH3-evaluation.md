---
type: protein-evaluation
gene: "GPATCH3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GPATCH3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPATCH3 / GPATC3 |
| 蛋白名称 | G patch domain-containing protein 3 |
| 蛋白大小 | 525 aa / 59.3 kDa |
| UniProt ID | Q96I76 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 525 aa / 59.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000467, IPR040341; Pfam: PF01585 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 5 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 0 |
| 别名(未计入scoring) | 无 |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.1 |
| 高置信度残基 (pLDDT>90) 占比 | 3.4% |
| 置信残基 (pLDDT 70-90) 占比 | 50.9% |
| 中等置信 (pLDDT 50-70) 占比 | 25.7% |
| 低置信 (pLDDT<50) 占比 | 20.0% |
| 有序区域 (pLDDT>70) 占比 | 54.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=67.1），有序残基占 54.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000467, IPR040341; Pfam: PF01585 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ZNF408 | 0.999 | 0.045 | — |
| ZBTB17 | 0.626 | 0.045 | — |
| AMMECR1L | 0.590 | 0.000 | — |
| ZGPAT | 0.585 | 0.000 | — |
| CC2D1B | 0.578 | 0.000 | — |
| RSPRY1 | 0.570 | 0.000 | — |
| ZC3H14 | 0.565 | 0.000 | — |
| EAF1 | 0.550 | 0.000 | — |
| ZNF212 | 0.537 | 0.045 | — |
| EFCAB1 | 0.532 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| A0A0F7RGP3 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| HSPA5 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| DHX15 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PAXBP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ENST00000361720 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 5
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 5 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.1 + PDB: 无 | pLDDT=67.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 5 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. GPATCH3 — G patch domain-containing protein 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小525 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=67.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96I76
- Protein Atlas: https://www.proteinatlas.org/ENSG00000198746-GPATCH3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPATCH3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96I76
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000198746-GPATCH3/subcellular

![](https://images.proteinatlas.org/54973/859_H6_1_red_green.jpg)
![](https://images.proteinatlas.org/54973/859_H6_2_red_green.jpg)
![](https://images.proteinatlas.org/54973/862_H6_1_red_green.jpg)
![](https://images.proteinatlas.org/54973/862_H6_2_red_green.jpg)
![](https://images.proteinatlas.org/54973/879_B2_1_red_green.jpg)
![](https://images.proteinatlas.org/54973/879_B2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96I76-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96I76 |
| SMART | SM00443; |
| UniProt Domain [FT] | DOMAIN 410..458; /note="G-patch"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00092" |
| InterPro | IPR000467;IPR040341; |
| Pfam | PF01585; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000198746-GPATCH3/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
