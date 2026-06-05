---
type: protein-evaluation
gene: "VAX2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## VAX2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | VAX2 |
| 蛋白名称 | Ventral anterior homeobox 2 |
| 蛋白大小 | 290 aa / 30.9 kDa |
| UniProt ID | Q9UIW0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 290 aa / 30.9 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=44 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR050877, IPR001356, IPR020479, IPR017970, IPR009 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 12 partners; IntAct 12 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **110.0/180** | |
| **归一化总分** | | | **61.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 44 |
| PubMed broad count | 188 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. The VAX2-LINC01189-hnRNPF signaling axis regulates cell invasion and migration in gastric cancer.. *Cell death discovery*. PMID: 37865686
2. The homeodomain protein Vax2 patterns the dorsoventral and nasotemporal axes of the eye.. *Development (Cambridge, England)*. PMID: 11830578
3. Identification and characterization of the VAX2 p.Leu139Arg variant: possible involvement of VAX2 in cone dystrophy.. *Ophthalmic genetics*. PMID: 29947570
4. A homeobox gene, vax2, controls the patterning of the eye dorsoventral axis.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 10485894
5. Vax2 regulates retinoic acid distribution and cone opsin expression in the vertebrate eye.. *Development (Cambridge, England)*. PMID: 21148184

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.9 |
| 高置信度残基 (pLDDT>90) 占比 | 30.3% |
| 置信残基 (pLDDT 70-90) 占比 | 10.3% |
| 中等置信 (pLDDT 50-70) 占比 | 40.0% |
| 低置信 (pLDDT<50) 占比 | 19.3% |
| 有序区域 (pLDDT>70) 占比 | 40.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=68.9），有序残基占 40.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050877, IPR001356, IPR020479, IPR017970, IPR009057; Pfam: PF00046 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PAX2 | 0.675 | 0.000 | — |
| SIX3 | 0.645 | 0.077 | — |
| SIX6 | 0.628 | 0.091 | — |
| TBX5 | 0.575 | 0.049 | — |
| CHMP3 | 0.534 | 0.534 | — |
| ATP6V1B1 | 0.478 | 0.000 | — |
| SIX5 | 0.458 | 0.057 | — |
| ALDH1A3 | 0.451 | 0.000 | — |
| LHX2 | 0.449 | 0.046 | — |
| SHH | 0.422 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CHMP4A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CHMP3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| POU6F2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PFDN5 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| UFSP1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| Gmeb2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| Rfxank | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| Six6 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| Pax6 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| IFNA7 | psi-mi:"MI:0432"(one hybrid) | doi:10.1093/nar/gkaa1055|pubme |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 12，IntAct interactions: 12
- 调控相关比例: 0 / 12 = 0%

**评价**: STRING 12 个预测互作，IntAct 12 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.9 + PDB: 无 | pLDDT=68.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 12 + 12 interactions | 数据充分 |

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
1. VAX2 — Ventral anterior homeobox 2，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小290 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 44 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=68.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UIW0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000116035-VAX2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=VAX2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UIW0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (approved)。来源: https://www.proteinatlas.org/ENSG00000116035-VAX2/subcellular

![](https://images.proteinatlas.org/9708/1207_C10_2_red_green.jpg)
![](https://images.proteinatlas.org/9708/1207_C10_3_red_green.jpg)
![](https://images.proteinatlas.org/9708/1372_D1_1_red_green.jpg)
![](https://images.proteinatlas.org/9708/1372_D1_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UIW0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
