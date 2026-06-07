---
type: protein-evaluation
gene: "PTOV1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PTOV1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PTOV1 / ACID2 |
| 蛋白名称 | Prostate tumor-overexpressed gene 1 protein |
| 蛋白大小 | 416 aa / 46.9 kDa |
| UniProt ID | Q86YD1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Cytoplasm; Nucleus; Cell membrane; Cytoplasm, perinuclear re |
| 蛋白大小 | 10/10 | ×1 | 10 | 416 aa / 46.9 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=46 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR021394, IPR038196; Pfam: PF11232 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **110.0/180** | |
| **归一化总分** | | | **61.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Cytoplasm; Nucleus; Cell membrane; Cytoplasm, perinuclear region | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleoplasm (GO:0005654)
- perinuclear region of cytoplasm (GO:0048471)
- plasma membrane (GO:0005886)
- transcription regulator complex (GO:0005667)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 46 |
| PubMed broad count | 65 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ACID2 |

**关键文献**:
1. LncRNA PTOV1-AS2 Promotes Colon Cancer Progression through the miR-145-5p/FSCN1 Axis.. *Journal of oncology*. PMID: 36960218
2. PTOV1 exerts pro-oncogenic role in colorectal cancer by modulating SQSTM1-mediated autophagic degradation of p53.. *Journal of translational medicine*. PMID: 39905441
3. SGK2, 14-3-3, and HUWE1 Cooperate to Control the Localization, Stability, and Function of the Oncoprotein PTOV1.. *Molecular cancer research : MCR*. PMID: 34654719
4. The role of prostate tumor overexpressed 1 in cancer progression.. *Oncotarget*. PMID: 28029646
5. PTOV1 interacts with ZNF449 to promote colorectal cancer development.. *Communications biology*. PMID: 40133702

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.2 |
| 高置信度残基 (pLDDT>90) 占比 | 12.3% |
| 置信残基 (pLDDT 70-90) 占比 | 46.9% |
| 中等置信 (pLDDT 50-70) 占比 | 13.0% |
| 低置信 (pLDDT<50) 占比 | 27.9% |
| 有序区域 (pLDDT>70) 占比 | 59.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=67.2），有序残基占 59.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR021394, IPR038196; Pfam: PF11232 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FLOT1 | 0.923 | 0.292 | — |
| FLOT2 | 0.781 | 0.000 | — |
| KLHDC2 | 0.709 | 0.621 | — |
| CREBBP | 0.700 | 0.512 | — |
| MED6 | 0.698 | 0.070 | — |
| HDAC1 | 0.666 | 0.481 | — |
| HDAC4 | 0.630 | 0.335 | — |
| SYN3 | 0.586 | 0.000 | — |
| SYN2 | 0.554 | 0.000 | — |
| CAMK2G | 0.546 | 0.046 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TMCC2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| DMTN | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| PIN1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| SPTAN1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| BECN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| 1C | psi-mi:"MI:0096"(pull down) | imex:IM-15828|pubmed:22593156 |
| RASSF9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-20985|pubmed:24366813 |
| CUL2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| YWHAQ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HDAC1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.2 + PDB: 无 | pLDDT=67.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Cell membrane; Cytoplasm, peri / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. PTOV1 — Prostate tumor-overexpressed gene 1 protein，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小416 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 46 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=67.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86YD1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000104960-PTOV1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PTOV1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86YD1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000104960-PTOV1/subcellular

![](https://images.proteinatlas.org/51812/1042_A10_1_red_green.jpg)
![](https://images.proteinatlas.org/51812/1042_A10_4_red_green.jpg)
![](https://images.proteinatlas.org/51812/761_B2_1_red_green.jpg)
![](https://images.proteinatlas.org/51812/761_B2_2_red_green.jpg)
![](https://images.proteinatlas.org/51812/910_B12_1_red_green.jpg)
![](https://images.proteinatlas.org/51812/910_B12_7_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86YD1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q86YD1 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR021394;IPR038196; |
| Pfam | PF11232; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000104960-PTOV1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AFAP1L1 | Bioplex | false |
| CDCA4 | Bioplex | false |
| CREBBP | Biogrid | false |
| FKBP5 | Opencell | false |
| FLOT1 | Biogrid | false |
| FOXJ1 | Bioplex | false |
| FTL | Bioplex | false |
| HDAC1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
