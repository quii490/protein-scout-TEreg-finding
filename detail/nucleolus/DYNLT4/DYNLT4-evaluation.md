---
type: protein-evaluation
gene: "DYNLT4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DYNLT4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DYNLT4 / TCTEX1D4 |
| 蛋白名称 | Dynein light chain Tctex-type 4 |
| 蛋白大小 | 221 aa / 23.4 kDa |
| UniProt ID | Q5JR98 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Vesicles; UniProt: Cell projection, cilium, flagellum; Cytoplasmic vesicle, sec |
| 蛋白大小 | 10/10 | ×1 | 10 | 221 aa / 23.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=1 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=73.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR005334, IPR038586; Pfam: PF03645 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles | Supported |
| UniProt | Cell projection, cilium, flagellum; Cytoplasmic vesicle, secretory vesicle, acrosome; Cytoplasm, cyt... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- acrosomal vesicle (GO:0001669)
- axoneme (GO:0005930)
- cytoplasm (GO:0005737)
- cytoplasmic dynein complex (GO:0005868)
- microtubule organizing center (GO:0005815)
- nucleolus (GO:0005730)
- nucleus (GO:0005634)
- sperm flagellum (GO:0036126)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1 |
| PubMed broad count | 2 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TCTEX1D4 |

**关键文献**:
1. Multi-ancestry exome-wide study identifies variants associated with Alzheimer's disease protection.. *Journal of Alzheimer's disease : JAD*. PMID: 41428483

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.3 |
| 高置信度残基 (pLDDT>90) 占比 | 47.1% |
| 置信残基 (pLDDT 70-90) 占比 | 10.0% |
| 中等置信 (pLDDT 50-70) 占比 | 14.9% |
| 低置信 (pLDDT<50) 占比 | 28.1% |
| 有序区域 (pLDDT>70) 占比 | 57.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=73.3，有序区 57.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR005334, IPR038586; Pfam: PF03645 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PPP1CC | psi-mi:"MI:0047"(far western blotting) | pubmed:21382349|imex:IM-17664 |
| PPP1CA | psi-mi:"MI:0018"(two hybrid) | pubmed:21382349|imex:IM-17664 |
| MDFI | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TRO | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ABHD17B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| C2CD5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| DYNC2I1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| DYNLT2B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| DYNC2I2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| BAG3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.3 + PDB: 无 | pLDDT=73.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell projection, cilium, flagellum; Cytoplasmic ve / Vesicles | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DYNLT4 — Dynein light chain Tctex-type 4，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小221 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5JR98
- Protein Atlas: https://www.proteinatlas.org/ENSG00000188396-DYNLT4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DYNLT4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5JR98
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (supported)。来源: https://www.proteinatlas.org/ENSG00000188396-DYNLT4/subcellular

![](https://images.proteinatlas.org/50116/1984_D4_20_cr615af7af18943_blue_red_green.jpg)
![](https://images.proteinatlas.org/50116/1984_D4_9_cr5e5cf3d026ca3_blue_red_green.jpg)
![](https://images.proteinatlas.org/50116/2013_D8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/50116/2013_D8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/50116/2063_E1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/50116/2063_E1_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5JR98-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q5JR98 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR005334;IPR038586; |
| Pfam | PF03645; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000188396-DYNLT4/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BAG3 | Bioplex | false |
| DYNLT1 | Bioplex | false |
| DYNLT2B | Bioplex | false |
| FIS1 | Bioplex | false |
| GET4 | Bioplex | false |
| MDFI | Intact | false |
| PPP1CC | Biogrid | false |
| PRSS8 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
