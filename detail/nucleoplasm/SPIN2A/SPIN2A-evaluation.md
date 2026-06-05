---
type: protein-evaluation
gene: "SPIN2A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SPIN2A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SPIN2A / DXF34, SPIN2 |
| 蛋白名称 | Spindlin-2A |
| 蛋白大小 | 258 aa / 29.2 kDa |
| UniProt ID | Q99865 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 258 aa / 29.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=80.5; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR003671, IPR042567; Pfam: PF02513 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 4 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **135.5/180** | |
| **归一化总分** | | | **75.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 5 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DXF34, SPIN2 |

**关键文献**:
1. Insights into X-Linked Susceptibility to Parkinson's Disease in the South African Population.. *medRxiv : the preprint server for health sciences*. PMID: 41480044
2. Cytoplasmic sequences of the growth hormone receptor necessary for signal transduction.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 8302873

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.5 |
| 高置信度残基 (pLDDT>90) 占比 | 64.3% |
| 置信残基 (pLDDT 70-90) 占比 | 10.5% |
| 中等置信 (pLDDT 50-70) 占比 | 2.7% |
| 低置信 (pLDDT<50) 占比 | 22.5% |
| 有序区域 (pLDDT>70) 占比 | 74.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=80.5，有序区 74.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003671, IPR042567; Pfam: PF02513 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| IL3 | 0.497 | 0.000 | — |
| MYOZ1 | 0.476 | 0.000 | — |
| SPINDOC | 0.446 | 0.000 | — |
| LUZP6 | 0.433 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SIPA1L3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| UBA52 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PRKACG | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| AFG2B | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:38554706|imex:IM-30175 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 4，IntAct interactions: 4
- 调控相关比例: 0 / 4 = 0%

**评价**: STRING 4 个预测互作，IntAct 4 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.5 + PDB: 无 | pLDDT=80.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 4 + 4 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. SPIN2A — Spindlin-2A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小258 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q99865
- Protein Atlas: https://www.proteinatlas.org/ENSG00000147059-SPIN2A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SPIN2A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q99865
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000147059-SPIN2A/subcellular

![](https://images.proteinatlas.org/69835/1337_E8_2_red_green.jpg)
![](https://images.proteinatlas.org/69835/1337_E8_3_red_green.jpg)
![](https://images.proteinatlas.org/69835/1338_E8_1_red_green.jpg)
![](https://images.proteinatlas.org/69835/1338_E8_2_red_green.jpg)
![](https://images.proteinatlas.org/69835/1511_F10_1_red_green.jpg)
![](https://images.proteinatlas.org/69835/1511_F10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q99865-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
