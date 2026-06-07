---
type: protein-evaluation
gene: "CYB5RL"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CYB5RL 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CYB5RL |
| 蛋白名称 | NADH-cytochrome b5 reductase-like |
| 蛋白大小 | 315 aa / 35.9 kDa |
| UniProt ID | Q6IPT4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 315 aa / 35.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=1 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=92.1; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001834, IPR008333, IPR017927, IPR039261, IPR019 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.0/180** | |
| **归一化总分** | | | **76.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- endoplasmic reticulum membrane (GO:0005789)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1 |
| PubMed broad count | 1 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Collaborating genomic, transcriptomic and microbiomic alterations lead to canine extreme intestinal polyposis.. *Oncotarget*. PMID: 30018743

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.1 |
| 高置信度残基 (pLDDT>90) 占比 | 85.1% |
| 置信残基 (pLDDT 70-90) 占比 | 9.2% |
| 中等置信 (pLDDT 50-70) 占比 | 1.9% |
| 低置信 (pLDDT<50) 占比 | 3.8% |
| 有序区域 (pLDDT>70) 占比 | 94.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=92.1，有序区 94.3%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001834, IPR008333, IPR017927, IPR039261, IPR019180; Pfam: PF00970, PF00175, PF09791 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CYB5B | 0.994 | 0.108 | — |
| CYB5A | 0.994 | 0.108 | — |
| DHODH | 0.928 | 0.469 | — |
| DPYD | 0.877 | 0.469 | — |
| UMPS | 0.854 | 0.000 | — |
| SCD | 0.824 | 0.000 | — |
| FDXR | 0.701 | 0.456 | — |
| POR | 0.698 | 0.071 | — |
| TMEM116 | 0.627 | 0.048 | — |
| CAD | 0.616 | 0.048 | — |

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
| 三维结构 | AlphaFold pLDDT=92.1 + PDB: 无 | pLDDT=92.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

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
1. CYB5RL — NADH-cytochrome b5 reductase-like，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小315 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6IPT4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000215883-CYB5RL/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CYB5RL
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6IPT4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000215883-CYB5RL/subcellular

![](https://images.proteinatlas.org/42671/736_C2_1_red_green.jpg)
![](https://images.proteinatlas.org/42671/736_C2_2_red_green.jpg)
![](https://images.proteinatlas.org/42671/752_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/42671/752_A3_2_red_green.jpg)
![](https://images.proteinatlas.org/42671/805_C2_1_red_green.jpg)
![](https://images.proteinatlas.org/42671/805_C2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6IPT4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6IPT4 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 19..55; /note="Oxidoreductase-like"; DOMAIN 75..177; /note="FAD-binding FR-type"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00716" |
| InterPro | IPR001834;IPR008333;IPR017927;IPR039261;IPR019180;IPR001433;IPR017938; |
| Pfam | PF00970;PF00175;PF09791; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000215883-CYB5RL/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
