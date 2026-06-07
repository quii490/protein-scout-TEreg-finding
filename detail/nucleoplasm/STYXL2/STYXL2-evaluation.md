---
type: protein-evaluation
gene: "STYXL2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## STYXL2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | STYXL2 / DUSP27 |
| 蛋白名称 | Serine/threonine/tyrosine-interacting-like protein 2 |
| 蛋白大小 | 1158 aa / 130.2 kDa |
| UniProt ID | Q5VZP5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; UniProt: Cytoplasm, myofibril, sarcomere |
| 蛋白大小 | 8/10 | ×1 | 8 | 1158 aa / 130.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=1 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=55.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR020405, IPR000340, IPR029021, IPR000387, IPR020 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 6 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.0/180** | |
| **归一化总分** | | | **64.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Cytoplasm, myofibril, sarcomere | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- sarcomere (GO:0030017)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1 |
| PubMed broad count | 10 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DUSP27 |

**关键文献**:
1. Styxl2 regulates de novo sarcomere assembly by binding to non-muscle myosin IIs and promoting their degradation.. *eLife*. PMID: 38829202

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 55.0 |
| 高置信度残基 (pLDDT>90) 占比 | 17.5% |
| 置信残基 (pLDDT 70-90) 占比 | 18.6% |
| 中等置信 (pLDDT 50-70) 占比 | 10.2% |
| 低置信 (pLDDT<50) 占比 | 53.7% |
| 有序区域 (pLDDT>70) 占比 | 36.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=55.0），有序残基占 36.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR020405, IPR000340, IPR029021, IPR000387, IPR020422; Pfam: PF00782 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KLHL38 | 0.567 | 0.000 | — |
| EFHB | 0.515 | 0.000 | — |
| XIRP2 | 0.458 | 0.092 | — |
| YIF1B | 0.453 | 0.000 | — |
| LRFN4 | 0.437 | 0.094 | — |
| DUSP11 | 0.416 | 0.048 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| YPEL5 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 6，IntAct interactions: 1
- 调控相关比例: 0 / 6 = 0%

**评价**: STRING 6 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=55.0 + PDB: 无 | pLDDT=55.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, myofibril, sarcomere / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 6 + 1 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. STYXL2 — Serine/threonine/tyrosine-interacting-like protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1158 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 1 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=55.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5VZP5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000198842-STYXL2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=STYXL2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5VZP5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000198842-STYXL2/subcellular

![](https://images.proteinatlas.org/12912/1585_B4_2_red_green.jpg)
![](https://images.proteinatlas.org/12912/1585_B4_3_red_green.jpg)
![](https://images.proteinatlas.org/12912/1616_B4_2_red_green.jpg)
![](https://images.proteinatlas.org/12912/1616_B4_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5VZP5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q5VZP5 |
| SMART | SM00195; |
| UniProt Domain [FT] | DOMAIN 132..280; /note="Tyrosine-protein phosphatase"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00160" |
| InterPro | IPR020405;IPR000340;IPR029021;IPR000387;IPR020422; |
| Pfam | PF00782; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000198842-STYXL2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| YPEL5 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
