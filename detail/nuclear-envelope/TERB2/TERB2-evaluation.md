---
type: protein-evaluation
gene: "TERB2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TERB2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TERB2 / C15orf43 |
| 蛋白名称 | Telomere repeats-binding bouquet formation protein 2 |
| 蛋白大小 | 220 aa / 25.3 kDa |
| UniProt ID | Q8NHR7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli; 额外: Nucleoplasm; UniProt: Chromosome, telomere; Nucleus inner membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 220 aa / 25.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=71.4; PDB: 6GNX, 6GNY, 6J07, 6J08 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR028065; Pfam: PF15101 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **141.0/180** | |
| **归一化总分** | | | **78.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; 额外: Nucleoplasm | Uncertain |
| UniProt | Chromosome, telomere; Nucleus inner membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromosome, telomeric region (GO:0000781)
- nuclear envelope (GO:0005635)
- nuclear inner membrane (GO:0005637)
- nuclear membrane (GO:0031965)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 11 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C15orf43 |

**关键文献**:
1. The meiotic TERB1-TERB2-MAJIN complex tethers telomeres to the nuclear envelope.. *Nature communications*. PMID: 30718482
2. Distinct TERB1 Domains Regulate Different Protein Interactions in Meiotic Telomere Movement.. *Cell reports*. PMID: 29141207
3. The TERB1 MYB domain suppresses telomere erosion in meiotic prophase I.. *Cell reports*. PMID: 35081355
4. The TERB1-TERB2-MAJIN complex of mouse meiotic telomeres dates back to the common ancestor of metazoans.. *BMC evolutionary biology*. PMID: 32408858
5. Telomeric function and regulation during male meiosis in mice and humans.. *Andrology*. PMID: 38511802

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.4 |
| 高置信度残基 (pLDDT>90) 占比 | 45.9% |
| 置信残基 (pLDDT 70-90) 占比 | 8.2% |
| 中等置信 (pLDDT 50-70) 占比 | 17.3% |
| 低置信 (pLDDT<50) 占比 | 28.6% |
| 有序区域 (pLDDT>70) 占比 | 54.1% |
| 可用 PDB 条目 | 6GNX, 6GNY, 6J07, 6J08 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（6GNX, 6GNY, 6J07, 6J08）+ AlphaFold高质量预测（pLDDT=71.4），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR028065; Pfam: PF15101 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MAJIN | 0.999 | 0.929 | — |
| TERB1 | 0.999 | 0.900 | — |
| TERF1 | 0.858 | 0.000 | — |
| CCDC155 | 0.839 | 0.000 | — |
| SUN1 | 0.825 | 0.000 | — |
| SPDYA | 0.760 | 0.000 | — |
| SUN2 | 0.745 | 0.000 | — |
| HORMAD1 | 0.568 | 0.000 | — |
| HORMAD2 | 0.537 | 0.000 | — |
| C14orf39 | 0.513 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MAJIN | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 1
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.4 + PDB: 6GNX, 6GNY, 6J07, 6J08 | pLDDT=71.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Chromosome, telomere; Nucleus inner membrane / Nucleoli; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 1 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TERB2 — Telomere repeats-binding bouquet formation protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小220 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NHR7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000167014-TERB2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TERB2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NHR7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (uncertain)。来源: https://www.proteinatlas.org/ENSG00000167014-TERB2/subcellular

![](https://images.proteinatlas.org/41780/534_A4_1_red_green.jpg)
![](https://images.proteinatlas.org/41780/534_A4_2_red_green.jpg)
![](https://images.proteinatlas.org/41780/539_A4_1_red_green.jpg)
![](https://images.proteinatlas.org/41780/539_A4_2_red_green.jpg)
![](https://images.proteinatlas.org/41780/552_A4_1_red_green.jpg)
![](https://images.proteinatlas.org/41780/552_A4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8NHR7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8NHR7 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR028065; |
| Pfam | PF15101; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000167014-TERB2/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
