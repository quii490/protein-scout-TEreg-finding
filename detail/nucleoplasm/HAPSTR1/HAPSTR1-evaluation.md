---
type: protein-evaluation
gene: "HAPSTR1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## HAPSTR1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HAPSTR1 / C16orf72, TAPR1 |
| 蛋白名称 | HUWE1-associated protein modifying stress responses 1 |
| 蛋白大小 | 275 aa / 30.9 kDa |
| UniProt ID | Q14CZ0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Vesicles; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 275 aa / 30.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=8 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=69.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR040308, IPR029196; Pfam: PF15251 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.5/180** | |
| **归一化总分** | | | **70.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles | Approved |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8 |
| PubMed broad count | 11 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C16orf72, TAPR1 |

**关键文献**:
1. Novel functions of a retroposed gene.. *Trends in genetics : TIG*. PMID: 36997426
2. The HAPSTR2 retrogene buffers stress signaling and resilience in mammals.. *Nature communications*. PMID: 36631436
3. Tight regulation of a nuclear HAPSTR1-HUWE1 pathway essential for mammalian life.. *Life science alliance*. PMID: 38453366
4. An LRPPRC-HAPSTR1-PSMD14 interaction regulates tumor progression in ovarian cancer.. *Aging*. PMID: 38643468
5. HAPSTR1 localizes HUWE1 to the nucleus to limit stress signaling pathways.. *Cell reports*. PMID: 37167062

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.3 |
| 高置信度残基 (pLDDT>90) 占比 | 16.0% |
| 置信残基 (pLDDT 70-90) 占比 | 33.5% |
| 中等置信 (pLDDT 50-70) 占比 | 27.6% |
| 低置信 (pLDDT<50) 占比 | 22.9% |
| 有序区域 (pLDDT>70) 占比 | 49.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=69.3），有序残基占 49.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR040308, IPR029196; Pfam: PF15251 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| FAM9B | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| INTS12 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| HUWE1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 3
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=69.3 + PDB: 无 | pLDDT=69.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 0 + 3 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. HAPSTR1 — HUWE1-associated protein modifying stress responses 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小275 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=69.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q14CZ0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000182831-HAPSTR1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HAPSTR1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q14CZ0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000182831-HAPSTR1/subcellular

![](https://images.proteinatlas.org/67492/1360_B3_2_red_green.jpg)
![](https://images.proteinatlas.org/67492/1360_B3_3_red_green.jpg)
![](https://images.proteinatlas.org/67492/1367_B3_1_red_green.jpg)
![](https://images.proteinatlas.org/67492/1367_B3_2_red_green.jpg)
![](https://images.proteinatlas.org/67492/1413_H10_2_red_green.jpg)
![](https://images.proteinatlas.org/67492/1413_H10_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q14CZ0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q14CZ0 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR040308;IPR029196; |
| Pfam | PF15251; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000182831-HAPSTR1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| FAM9B | Intact, Biogrid | true |
| AHSA1 | Biogrid | false |
| BAG6 | Biogrid | false |
| CAND1 | Biogrid | false |
| CCT2 | Biogrid | false |
| CSE1L | Biogrid | false |
| DNAJA1 | Biogrid | false |
| ENSG00000230707 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
