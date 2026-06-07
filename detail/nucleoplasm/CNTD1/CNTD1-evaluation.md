---
type: protein-evaluation
gene: "CNTD1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CNTD1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CNTD1 / CNTD |
| 蛋白名称 | Cyclin N-terminal domain-containing protein 1 |
| 蛋白大小 | 330 aa / 36.9 kDa |
| UniProt ID | Q8N815 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoplasm; 额外: Vesicles; UniProt: Nucleus; Cytoplasm; Chromosome |
| 蛋白大小 | 10/10 | x1 | 10 | 330 aa / 36.9 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=6 篇 (<=20->10) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=84.6; PDB: 无 |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR036915, IPR006671; Pfam: PF00134 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **135.0/180** | |
| **归一化总分** | | | **75.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles | Approved |
| UniProt | Nucleus; Cytoplasm; Chromosome | Swiss-Prot/TremBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromosome (GO:0005694)
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)
- site of double-strand break (GO:0035861)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6 |
| PubMed broad count | 9 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CNTD |

**关键文献**:
1. RNF212B E3 ligase is essential for crossover designation and maturation during male and female meiosis in the mouse.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 38865271
2. Cyclin N-Terminal Domain-Containing-1 Coordinates Meiotic Crossover Formation with Cell-Cycle Progression in a Cyclin-Independent Manner.. *Cell reports*. PMID: 32640224
3. Proline-rich protein PRR19 functions with cyclin-like CNTD1 to promote meiotic crossing over in mouse.. *Nature communications*. PMID: 32555348
4. Mammalian CNTD1 is critical for meiotic crossover maturation and deselection of excess precrossover sites.. *The Journal of cell biology*. PMID: 24891606
5. MRNA and miRNA expression patterns associated to pathways linked to metal mixture health effects.. *Gene*. PMID: 24080485

**评价**: 极度新颖，几乎未被系统研究（PubMed <=20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.6 |
| 高置信度残基 (pLDDT>90) 占比 | 61.2% |
| 置信残基 (pLDDT 70-90) 占比 | 21.5% |
| 中等置信 (pLDDT 50-70) 占比 | 5.2% |
| 低置信 (pLDDT<50) 占比 | 12.1% |
| 有序区域 (pLDDT>70) 占比 | 82.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=84.6，有序区 82.7%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036915, IPR006671; Pfam: PF00134 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RNF212 | 0.844 | 0.067 | — |
| MSH5 | 0.764 | 0.071 | — |
| SPO11 | 0.762 | 0.000 | — |
| UNC119 | 0.741 | 0.000 | — |
| MSH4 | 0.721 | 0.061 | — |
| WNK4 | 0.631 | 0.000 | — |
| SUN1 | 0.626 | 0.000 | — |
| PPIE | 0.620 | 0.000 | — |
| CCNB1IP1 | 0.606 | 0.000 | — |
| RAD51 | 0.564 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=84.6 + PDB: 无 | pLDDT=84.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Chromosome / Nucleoplasm; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ****

**核心优势**:
1. CNTD1 -- Cyclin N-terminal domain-containing protein 1，极度新颖，几乎未被系统研究（PubMed <=20篇）。
2. 蛋白大小330 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N815
- Protein Atlas: https://www.proteinatlas.org/ENSG00000176563-CNTD1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CNTD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N815
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000176563-CNTD1/subcellular

![](https://images.proteinatlas.org/72363/1833_H7_1_red_green.jpg)
![](https://images.proteinatlas.org/72363/1833_H7_2_red_green.jpg)
![](https://images.proteinatlas.org/72363/2008_A10_16_cr5f1ab7c429d3d_red_green.jpg)
![](https://images.proteinatlas.org/72363/2008_A10_29_cr5f1ab7c42a05f_red_green.jpg)
![](https://images.proteinatlas.org/72363/2017_H10_31_red_green.jpg)
![](https://images.proteinatlas.org/72363/2017_H10_32_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8N815-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8N815 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 27..178; /note="Cyclin N-terminal" |
| InterPro | IPR036915;IPR006671; |
| Pfam | PF00134; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000176563-CNTD1/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
