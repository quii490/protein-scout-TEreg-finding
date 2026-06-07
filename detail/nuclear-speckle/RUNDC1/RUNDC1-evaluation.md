---
type: protein-evaluation
gene: "RUNDC1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## RUNDC1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RUNDC1 |
| 蛋白名称 | RUN domain-containing protein 1 |
| 蛋白大小 | 613 aa / 67.6 kDa |
| UniProt ID | Q96C34 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles; 额外: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 613 aa / 67.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=70.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR004012, IPR037213, IPR058732; Pfam: PF02759, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 13 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **132/180** | |
| **归一化总分** | | | **73.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles; 额外: Cytosol | Approved |
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
| PubMed strict count | 4 |
| PubMed broad count | 6 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. RUNDC1 inhibits autolysosome formation and survival of zebrafish via clasping ATG14-STX17-SNAP29 complex.. *Cell death and differentiation*. PMID: 37684417
2. A high-throughput loss-of-function screening identifies novel p53 regulators.. *Cell cycle (Georgetown, Tex.)*. PMID: 16929179
3. Cis-eQTLs in seven duck tissues identify novel candidate genes for growth and carcass traits.. *BMC genomics*. PMID: 38689208
4. Gene expression analysis on a photodiode array-based bioluminescence analyzer by using sensitivity-improved SRPP.. *The Analyst*. PMID: 20498880

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.0 |
| 高置信度残基 (pLDDT>90) 占比 | 18.8% |
| 置信残基 (pLDDT 70-90) 占比 | 41.6% |
| 中等置信 (pLDDT 50-70) 占比 | 11.4% |
| 低置信 (pLDDT<50) 占比 | 28.2% |
| 有序区域 (pLDDT>70) 占比 | 60.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=70.0，有序区 60.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004012, IPR037213, IPR058732; Pfam: PF02759, PF26030 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CCDC186 | 0.545 | 0.000 | — |
| VPS50 | 0.544 | 0.000 | — |
| VPS51 | 0.496 | 0.000 | — |
| EIPR1 | 0.495 | 0.000 | — |
| VPS54 | 0.484 | 0.000 | — |
| TMF1 | 0.455 | 0.000 | — |
| RAB2A | 0.442 | 0.077 | — |
| PTGES3L | 0.441 | 0.000 | — |
| ICA1 | 0.439 | 0.094 | — |
| VPS53 | 0.427 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 13，IntAct interactions: 0
- 调控相关比例: 0 / 13 = 0%

**评价**: STRING 13 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.0 + PDB: 无 | pLDDT=70.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nuclear speckles; 额外: Cytosol | 待确认 |
| PPI | STRING + IntAct | 13 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. RUNDC1 — RUN domain-containing protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小613 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96C34
- Protein Atlas: https://www.proteinatlas.org/ENSG00000198863-RUNDC1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RUNDC1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96C34
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (approved)。来源: https://www.proteinatlas.org/ENSG00000198863-RUNDC1/subcellular

![](https://images.proteinatlas.org/23726/224_H1_1_red_green.jpg)
![](https://images.proteinatlas.org/23726/224_H1_2_red_green.jpg)
![](https://images.proteinatlas.org/23726/261_H1_1_red_green.jpg)
![](https://images.proteinatlas.org/23726/261_H1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96C34-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96C34 |
| SMART | SM00593; |
| UniProt Domain [FT] | DOMAIN 421..602; /note="RUN"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00178" |
| InterPro | IPR004012;IPR037213;IPR058732; |
| Pfam | PF02759;PF26030; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000198863-RUNDC1/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
