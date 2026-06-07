---
type: protein-evaluation
gene: "GPS2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GPS2 — REJECTED (研究热度过高 (PubMed strict=109，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPS2 |
| 蛋白名称 | G protein pathway suppressor 2 |
| 蛋白大小 | 327 aa / 36.7 kDa |
| UniProt ID | Q13227 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Mitochondrion; Cytoplasm, cytosol |
| 蛋白大小 | 10/10 | ×1 | 10 | 327 aa / 36.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=109 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.2; PDB: 2L5G |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026094; Pfam: PF15991 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.5/180** | |
| **归一化总分** | | | **44.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus; Mitochondrion; Cytoplasm, cytosol | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- mitochondrion (GO:0005739)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- transcription regulator complex (GO:0005667)
- transcription repressor complex (GO:0017053)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 109 |
| PubMed broad count | 148 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. G protein pathway suppressor 2 suppresses aerobic glycolysis through RACK1-mediated HIF-1α degradation in breast cancer.. *Free radical biology & medicine*. PMID: 38942092
2. Liquid-liquid phase separation of GPS2-LATS1 promotes colorectal cancer progression by reprogramming lipid metabolism.. *Oncogene*. PMID: 40715488
3. Inhibition of K63 ubiquitination by G-Protein pathway suppressor 2 (GPS2) regulates mitochondria-associated translation.. *Pharmacological research*. PMID: 39094987
4. ANKRD26 and its interacting partners TRIO, GPS2, HMMR and DIPA regulate adipogenesis in 3T3-L1 cells.. *PloS one*. PMID: 22666460
5. Recurrent FOXK1::GRHL and GPS2::GRHL fusions in trichogerminoma.. *The Journal of pathology*. PMID: 35049062

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.2 |
| 高置信度残基 (pLDDT>90) 占比 | 17.1% |
| 置信残基 (pLDDT 70-90) 占比 | 16.2% |
| 中等置信 (pLDDT 50-70) 占比 | 22.3% |
| 低置信 (pLDDT<50) 占比 | 44.3% |
| 有序区域 (pLDDT>70) 占比 | 33.3% |
| 可用 PDB 条目 | 2L5G |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=62.2），有序残基占 33.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026094; Pfam: PF15991 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TBL1Y | 0.999 | 0.702 | — |
| TBL1X | 0.999 | 0.844 | — |
| TBL1XR1 | 0.999 | 0.704 | — |
| NCOR1 | 0.999 | 0.780 | — |
| HDAC3 | 0.998 | 0.855 | — |
| NCOR2 | 0.997 | 0.684 | — |
| GPS1 | 0.958 | 0.000 | — |
| EP300 | 0.840 | 0.300 | — |
| TADA3 | 0.777 | 0.614 | — |
| ABCG1 | 0.755 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MAP3K7CL | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ATF4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| BRME1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CHD3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| SETDB1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| PBK | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| SPDL1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| GOLGA2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| vif | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-17346|pubmed:22190034| |
| HDAC3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:21258344|imex:IM-17039 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.2 + PDB: 2L5G | pLDDT=62.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Mitochondrion; Cytoplasm, cytosol / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. GPS2 — G protein pathway suppressor 2，研究基础较多，新颖性有限。
2. 蛋白大小327 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 109 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=62.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 109 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13227
- Protein Atlas: https://www.proteinatlas.org/ENSG00000132522-GPS2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPS2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13227
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000132522-GPS2/subcellular

![](https://images.proteinatlas.org/67540/1249_B9_3_red_green.jpg)
![](https://images.proteinatlas.org/67540/1249_B9_4_red_green.jpg)
![](https://images.proteinatlas.org/67540/1258_B9_1_red_green.jpg)
![](https://images.proteinatlas.org/67540/1258_B9_2_red_green.jpg)
![](https://images.proteinatlas.org/67540/1284_G6_1_red_green.jpg)
![](https://images.proteinatlas.org/67540/1284_G6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q13227-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q13227 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR026094; |
| Pfam | PF15991; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000132522-GPS2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ATF4 | Intact, Biogrid | true |
| HDAC1 | Intact, Biogrid | true |
| HDAC3 | Intact, Biogrid, Opencell | true |
| MAP3K7CL | Intact, Biogrid | true |
| NCOR2 | Intact, Biogrid | true |
| RALBP1 | Intact, Biogrid, Bioplex | true |
| TBL1XR1 | Biogrid, Bioplex | true |
| AKAP8L | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
