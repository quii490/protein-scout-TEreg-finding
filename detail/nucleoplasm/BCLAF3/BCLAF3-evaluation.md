---
type: protein-evaluation
gene: "BCLAF3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BCLAF3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BCLAF3 / CXorf23 |
| 蛋白名称 | BCLAF1 and THRAP3 family member 3 |
| 蛋白大小 | 711 aa / 83.9 kDa |
| UniProt ID | A2AJT9 |
| 评估日期 | 2026-06-03 |
| 数据采集时间 | 2026-06-03 03:32:59 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 10/10 | x4 | 40 | HPA: Nucleoplasm; UniProt: Nucleus, N... |
| 蛋白大小 | 10/10 | x1 | 10 | 711 aa / 83.9 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=0 篇 (<=20->10) |
| 三维结构 | 3/10 | x3 | 9 | AlphaFold v6 pLDDT=48.7 |
| 调控结构域 | 5/10 | x2 | 10 | InterPro: 1; Pfam: 1; IPR029199 |
| PPI 网络 | 8/10 | x3 | 24 | STRING 15 partners; IntAct 6 interactions |
| 互证加分 | -- | max +3 | 1.0 | 多库定位一致 (3源): +0.5; STRING + IntAct 双源验证: +0.5 |
| **原始总分** | | | **144.0/180** | |
| **归一化总分 (/1.83)** | | | **78.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoplasm | Approved |
| UniProt | Nucleus, Nucleus speckle | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- mediator complex (GO:0016592)
- mitochondrion (GO:0005739)

**结论**: 核定位证据充分，多个数据源一致支持核定位，定位特异性高。

#### 3.2 蛋白大小评估

**评价**: 711 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 1 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CXorf23 |

**评价**: 极度新颖，几乎未被系统研究（PubMed <= 20篇）。新颖性评分 10/10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 48.7 |
| 高置信度残基 (pLDDT>90) 占比 | 0.8% |
| 置信残基 (pLDDT 70-90) 占比 | 9.1% |
| 中等置信 (pLDDT 50-70) 占比 | 29.1% |
| 低置信 (pLDDT<50) 占比 | 60.9% |
| 有序区域 (pLDDT>70) 占比 | 9.9% |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold低质量预测（pLDDT=48.7），大部分区域无序。三维结构评分 3/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029199; Pfam: PF15440 |

**染色质调控潜力分析**: 存在 2 个已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score > 0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MED21 | 0.543 | 0.000 | -- |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Erh | tandem affinity purification | imex:IM-11719|pubmed:20360068 |
| EPHA1 | two hybrid fragment pooling approach | pubmed:31413325|imex:IM-26801 |
| URS00000A07C1_10090 | pull down | pubmed:29867223|imex:IM-24989 |
| MATR3 | anti tag coimmunoprecipitation | pubmed:26496610|imex:IM-24272 |
| ERH | anti tag coimmunoprecipitation | pubmed:33961781|imex:IM-29278|doi:10.1016/j.cell.2021.04.011 |
| EBI-2532663 | anti tag coimmunoprecipitation | imex:IM-30341|pubmed:40739040 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 6

**评价**: 互作网络中等：STRING 15 预测 + IntAct 6 实验互作。PPI 评分 8/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold v6 | pLDDT=48.7 | 单一来源 |
| 定位 | UniProt + HPA | Nucleoplasm / Nucleus, Nucleus speckle | 一致 |
| PPI | STRING + IntAct | 15 + 6 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
**总分**: +1.0 / max +3

### 4. 总体评价

**归一化总分**: 78.7/100

**核心优势**:
1. BCLAF3 -- BCLAF1 and THRAP3 family member 3，极度新颖，几乎未被系统研究（PubMed <= 20篇）。
2. 蛋白大小711 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。
3. 存在 2 个已知结构域，有明确的结构-功能切入点。
4. 核定位信号明确，多个数据源一致支持。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. AlphaFold pLDDT 较低（48.7），存在显著无序区
3. 暂无PDB实验结构，结构证据完全依赖AlphaFold预测

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] 考虑通过AlphaFold预测 + MD模拟获取结构信息

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/A2AJT9
- Protein Atlas: https://www.proteinatlas.org/search/BCLAF3
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BCLAF3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A2AJT9
- STRING: https://string-db.org/network/9606.BCLAF3
- Packet data timestamp: 2026-06-03 03:32:59

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000173681-BCLAF3/subcellular

![](https://images.proteinatlas.org/27215/218_F6_1_red_green.jpg)
![](https://images.proteinatlas.org/27215/218_F6_2_red_green.jpg)
![](https://images.proteinatlas.org/27215/219_F6_1_red_green.jpg)
![](https://images.proteinatlas.org/27215/219_F6_2_red_green.jpg)
![](https://images.proteinatlas.org/27215/220_F6_1_red_green.jpg)
![](https://images.proteinatlas.org/27215/220_F6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-A2AJT9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | A2AJT9 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR029199; |
| Pfam | PF15440; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000173681-BCLAF3/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
