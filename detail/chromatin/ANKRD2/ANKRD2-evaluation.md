---
type: protein-evaluation
gene: "ANKRD2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ANKRD2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ANKRD2 / ARPP |
| 蛋白名称 | Ankyrin repeat domain-containing protein 2 |
| 蛋白大小 | 360 aa / 39.9 kDa |
| UniProt ID | Q9GZV1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Vesicles; UniProt: Cytoplasm, myofibril, sarcomere, I band; Cytoplasm, cytosol; |
| 蛋白大小 | 10/10 | ×1 | 10 | 360 aa / 39.9 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=59 篇 (≤60→6) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=76.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR002110, IPR036770; Pfam: PF00023, PF12796 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 8 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.5/180** | |
| **归一化总分** | | | **63.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles | Enhanced |
| UniProt | Cytoplasm, myofibril, sarcomere, I band; Cytoplasm, cytosol; Nucleus; Nucleus, PML body | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- euchromatin (GO:0000791)
- I band (GO:0031674)
- nucleus (GO:0005634)
- PML body (GO:0016605)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 59 |
| PubMed broad count | 78 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ARPP |

**关键文献**:
1. The Ankrd2 protein, a link between the sarcomere and the nucleus in skeletal muscle.. *Journal of molecular biology*. PMID: 15136035
2. Ankrd2 in Mechanotransduction and Oxidative Stress Response in Skeletal Muscle: New Cues for the Pathogenesis of Muscular Laminopathies.. *Oxidative medicine and cellular longevity*. PMID: 31428229
3. Differential expression and localization of Ankrd2 isoforms in human skeletal and cardiac muscles.. *Histochemistry and cell biology*. PMID: 27393496
4. Ankrd1 is a transcriptional repressor for the androgen receptor that is downregulated by testosterone.. *Biochemical and biophysical research communications*. PMID: 23811403
5. ZASP interacts with the mechanosensing protein Ankrd2 and p53 in the signalling network of striated muscle.. *PloS one*. PMID: 24647531

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.8 |
| 高置信度残基 (pLDDT>90) 占比 | 52.2% |
| 置信残基 (pLDDT 70-90) 占比 | 15.3% |
| 中等置信 (pLDDT 50-70) 占比 | 8.3% |
| 低置信 (pLDDT<50) 占比 | 24.2% |
| 有序区域 (pLDDT>70) 占比 | 67.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=76.8，有序区 67.5%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002110, IPR036770; Pfam: PF00023, PF12796 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TTN | 0.969 | 0.331 | — |
| TCAP | 0.941 | 0.292 | — |
| MYPN | 0.748 | 0.094 | — |
| YBX1 | 0.745 | 0.292 | — |
| CSRP3 | 0.735 | 0.051 | — |
| LDB3 | 0.721 | 0.334 | — |
| MYOZ2 | 0.708 | 0.045 | — |
| MYH7 | 0.671 | 0.113 | — |
| MYH3 | 0.656 | 0.113 | — |
| TP53 | 0.648 | 0.295 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MAPK6 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ENSP00000306163.5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| - | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| FCMR | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| HBP1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| MICB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ZBTB3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| ENST00000307518 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 8
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 8 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.8 + PDB: 无 | pLDDT=76.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, myofibril, sarcomere, I band; Cytoplasm / Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 8 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. ANKRD2 — Ankyrin repeat domain-containing protein 2，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小360 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 59 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9GZV1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000165887-ANKRD2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ANKRD2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9GZV1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (enhanced)。来源: https://www.proteinatlas.org/ENSG00000165887-ANKRD2/subcellular

![](https://images.proteinatlas.org/40842/534_B12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/40842/534_B12_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/40842/539_B12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/40842/539_B12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/40842/552_B12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/40842/552_B12_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9GZV1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
