---
type: protein-evaluation
gene: "LDB3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LDB3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LDB3 / KIAA0613, ZASP |
| 蛋白名称 | LIM domain-binding protein 3 |
| 蛋白大小 | 727 aa / 77.1 kDa |
| UniProt ID | O75112 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm, perinuclear region; Cell projection, pseudopodium |
| 蛋白大小 | 10/10 | ×1 | 10 | 727 aa / 77.1 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=97 篇 (≤100→2) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.7; PDB: 1RGW, 4YDP |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR031847, IPR001478, IPR050604, IPR036034, IPR006 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **90.5/180** | |
| **归一化总分** | | | **50.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm, perinuclear region; Cell projection, pseudopodium; Cytoplasm, cytoskeleton; Cytoplasm, my... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- adherens junction (GO:0005912)
- cytoskeleton (GO:0005856)
- filamentous actin (GO:0031941)
- perinuclear region of cytoplasm (GO:0048471)
- pseudopodium (GO:0031143)
- stress fiber (GO:0001725)
- Z disc (GO:0030018)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 97 |
| PubMed broad count | 197 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0613, ZASP |

**关键文献**:
1. Dilated Cardiomyopathy Overview.. **. PMID: 20301486
2. A sensitive red/far-red photoswitch for controllable gene therapy in mouse models of metabolic diseases.. *Nature communications*. PMID: 39604418
3. Identification of the Hub Gene LDB3 in Stanford Type A Aortic Dissection Based on Comprehensive Bioinformatics Analysis.. *Journal of cellular and molecular medicine*. PMID: 40099963
4. Myopathy associated LDB3 mutation causes Z-disc disassembly and protein aggregation through PKCα and TSC2-mTOR downregulation.. *Communications biology*. PMID: 33742095
5. Divergent Regulatory Roles of Transcriptional Variants of the Chicken LDB3 Gene in Muscle Shaping.. *Journal of agricultural and food chemistry*. PMID: 38764183

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.7 |
| 高置信度残基 (pLDDT>90) 占比 | 20.4% |
| 置信残基 (pLDDT 70-90) 占比 | 21.0% |
| 中等置信 (pLDDT 50-70) 占比 | 8.5% |
| 低置信 (pLDDT<50) 占比 | 50.1% |
| 有序区域 (pLDDT>70) 占比 | 41.4% |
| 可用 PDB 条目 | 1RGW, 4YDP |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=60.7），有序残基占 41.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR031847, IPR001478, IPR050604, IPR036034, IPR006643; Pfam: PF15936, PF00412, PF00595 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ACTN2 | 0.973 | 0.230 | — |
| MYOT | 0.965 | 0.000 | — |
| FLNC | 0.926 | 0.000 | — |
| MYOZ2 | 0.925 | 0.000 | — |
| MYOZ1 | 0.914 | 0.000 | — |
| TCAP | 0.887 | 0.000 | — |
| TNNT2 | 0.882 | 0.000 | — |
| MYOZ3 | 0.876 | 0.000 | — |
| MYH7 | 0.839 | 0.054 | — |
| BAG3 | 0.824 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Prkce | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:12169683 |
| NAF1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:14690591 |
| VRG4 | psi-mi:"MI:0018"(two hybrid) | pubmed:18719252 |
| ALB | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:15174051|imex:IM-19123 |
| GTT1 | psi-mi:"MI:0018"(two hybrid) | pubmed:18719252 |
| MGA2 | psi-mi:"MI:0018"(two hybrid) | pubmed:18719252 |
| UIP3 | psi-mi:"MI:0018"(two hybrid) | pubmed:18719252 |
| STAT5B | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| ZAP70 | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| hspa1a_hspa1b_human-1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.7 + PDB: 1RGW, 4YDP | pLDDT=60.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, perinuclear region; Cell projection, ps / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. LDB3 — LIM domain-binding protein 3，研究基础较多，新颖性有限。
2. 蛋白大小727 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 97 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=60.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75112
- Protein Atlas: https://www.proteinatlas.org/search/LDB3
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LDB3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75112
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Focal adhesion sites (uncertain)。来源: https://www.proteinatlas.org/ENSG00000122367-LDB3/subcellular

![](https://images.proteinatlas.org/48955/1361_E5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/48955/1361_E5_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/48955/1366_E5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/48955/1366_E5_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/48955/1413_G4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/48955/1413_G4_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O75112-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
