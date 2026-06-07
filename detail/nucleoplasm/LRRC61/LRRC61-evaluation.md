---
type: protein-evaluation
gene: "LRRC61"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LRRC61 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LRRC61 |
| 蛋白名称 | Leucine-rich repeat-containing protein 61 |
| 蛋白大小 | 259 aa / 28.0 kDa |
| UniProt ID | Q9BV99 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 259 aa / 28.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=84.5; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001611, IPR032675; Pfam: PF13855 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.0/180** | |
| **归一化总分** | | | **68.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3 |
| PubMed broad count | 4 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Establish six-gene prognostic model for glioblastoma based on multi-omics data of TCGA database.. *Yi chuan = Hereditas*. PMID: 34284982
2. Biological significance of genome-wide DNA methylation profiles in keloids.. *The Laryngoscope*. PMID: 27312686
3. Causal network analysis of head and neck keloid tissue identifies potential master regulators.. *The Laryngoscope*. PMID: 26990118

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.5 |
| 高置信度残基 (pLDDT>90) 占比 | 62.2% |
| 置信残基 (pLDDT 70-90) 占比 | 18.9% |
| 中等置信 (pLDDT 50-70) 占比 | 12.4% |
| 低置信 (pLDDT<50) 占比 | 6.6% |
| 有序区域 (pLDDT>70) 占比 | 81.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=84.5，有序区 81.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001611, IPR032675; Pfam: PF13855 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ZBED6CL | 0.936 | 0.094 | — |
| KRBA1 | 0.637 | 0.094 | — |
| FAM184A | 0.613 | 0.613 | — |
| ACTR3C | 0.607 | 0.095 | — |
| DNAJC27 | 0.601 | 0.601 | — |
| GPR12 | 0.528 | 0.000 | — |
| ADGRL2 | 0.514 | 0.514 | — |
| ADGRL3 | 0.514 | 0.514 | — |
| ADGRL1 | 0.514 | 0.514 | — |
| ZNF584 | 0.507 | 0.094 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.5 + PDB: 无 | pLDDT=84.5, v6 | 仅预测 |
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

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. LRRC61 — Leucine-rich repeat-containing protein 61，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小259 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BV99
- Protein Atlas: https://www.proteinatlas.org/ENSG00000127399-LRRC61/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LRRC61
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BV99
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000127399-LRRC61/subcellular

![](https://images.proteinatlas.org/19355/1183_B6_1_red_green.jpg)
![](https://images.proteinatlas.org/19355/1183_B6_2_red_green.jpg)
![](https://images.proteinatlas.org/19355/185_B2_1_red_green.jpg)
![](https://images.proteinatlas.org/19355/185_B2_2_red_green.jpg)
![](https://images.proteinatlas.org/19355/242_B2_1_red_green.jpg)
![](https://images.proteinatlas.org/19355/242_B2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BV99-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BV99 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 138..178; /note="LRRCT" |
| InterPro | IPR001611;IPR032675; |
| Pfam | PF13855; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000127399-LRRC61/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| C1orf216 | Intact | false |
| DNALI1 | Intact | false |
| EFHC1 | Intact | false |
| ENKD1 | Intact | false |
| FAM184A | Biogrid | false |
| FAM222B | Intact | false |
| HGS | Intact | false |
| ICAM5 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
