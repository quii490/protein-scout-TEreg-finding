---
type: protein-evaluation
gene: "VXN"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## VXN 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | VXN / C8orf46 |
| 蛋白名称 | Vexin |
| 蛋白大小 | 207 aa / 22.6 kDa |
| UniProt ID | Q8TAG6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles; UniProt: Cell membrane; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 207 aa / 22.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR040470, IPR027900; Pfam: PF15505 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 3 partners; IntAct 6 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles | Approved |
| UniProt | Cell membrane; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 15 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C8orf46 |

**关键文献**:
1. The proteome of granulovacuolar degeneration and neurofibrillary tangles in Alzheimer's disease.. *Acta neuropathologica*. PMID: 33492460
2. C8orf46 homolog encodes a novel protein Vexin that is required for neurogenesis in Xenopus laevis.. *Developmental biology*. PMID: 29518376

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.2 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 23.7% |
| 中等置信 (pLDDT 50-70) 占比 | 58.9% |
| 低置信 (pLDDT<50) 占比 | 17.4% |
| 有序区域 (pLDDT>70) 占比 | 23.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=60.2），有序残基占 23.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR040470, IPR027900; Pfam: PF15505 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FAM227B | 0.615 | 0.000 | — |
| RNF144A | 0.443 | 0.000 | — |
| C8orf48 | 0.435 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CABP2 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| ZNF76 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| NTAQ1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| FHL2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CEP70 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TRIM61 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 3，IntAct interactions: 6
- 调控相关比例: 0 / 3 = 0%

**评价**: STRING 3 个预测互作，IntAct 6 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.2 + PDB: 无 | pLDDT=60.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane; Nucleus / Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 3 + 6 interactions | 数据充分 |

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
1. VXN — Vexin，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小207 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=60.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TAG6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000169085-VXN/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=VXN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TAG6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (approved)。来源: https://www.proteinatlas.org/ENSG00000169085-VXN/subcellular

![](https://images.proteinatlas.org/75134/1559_A7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/75134/1559_A7_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/75134/1561_B5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/75134/1561_B5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/75134/1562_B5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/75134/1562_B5_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8TAG6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8TAG6 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR040470;IPR027900; |
| Pfam | PF15505; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000169085-VXN/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CABP2 | Intact | false |
| CEP70 | Intact | false |
| FHL2 | Intact | false |
| NTAQ1 | Intact | false |
| ZNF76 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
