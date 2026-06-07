---
type: protein-evaluation
gene: "CRTC2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CRTC2 — REJECTED (研究热度过高 (PubMed strict=205，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CRTC2 / TORC2 |
| 蛋白名称 | CREB-regulated transcription coactivator 2 |
| 蛋白大小 | 693 aa / 73.3 kDa |
| UniProt ID | Q53ET0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 693 aa / 73.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=205 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=48.6; PDB: 4HTM |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR024786, IPR024785, IPR024784, IPR024783; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.5/180** | |
| **归一化总分** | | | **44.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- extracellular exosome (GO:0070062)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 205 |
| PubMed broad count | 523 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TORC2 |

**关键文献**:
1. Dysfunction of autophagy in high-fat diet-induced non-alcoholic fatty liver disease.. *Autophagy*. PMID: 37700498
2. Sam68 promotes hepatic gluconeogenesis via CRTC2.. *Nature communications*. PMID: 34099657
3. Hepatic glycogen directly regulates gluconeogenesis through an AMPK/CRTC2 axis in mice.. *The Journal of clinical investigation*. PMID: 40454488
4. Biological functions of CRTC2 and its role in metabolism-related diseases.. *Journal of cell communication and signaling*. PMID: 36856929
5. The CREB coactivator CRTC2 controls hepatic lipid metabolism by regulating SREBP1.. *Nature*. PMID: 26147081

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 48.6 |
| 高置信度残基 (pLDDT>90) 占比 | 5.1% |
| 置信残基 (pLDDT 70-90) 占比 | 5.3% |
| 中等置信 (pLDDT 50-70) 占比 | 18.2% |
| 低置信 (pLDDT<50) 占比 | 71.4% |
| 有序区域 (pLDDT>70) 占比 | 10.4% |
| 可用 PDB 条目 | 4HTM |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=48.6），有序残基占 10.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR024786, IPR024785, IPR024784, IPR024783; Pfam: PF12886, PF12885, PF12884 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CREB1 | 0.999 | 0.927 | — |
| SIK2 | 0.992 | 0.633 | — |
| CREBBP | 0.984 | 0.258 | — |
| SIK1 | 0.975 | 0.311 | — |
| SIK1B | 0.965 | 0.068 | — |
| OGT | 0.963 | 0.000 | — |
| EP300 | 0.961 | 0.312 | — |
| CRTC3 | 0.952 | 0.000 | — |
| PPP3CC | 0.946 | 0.458 | — |
| AKT2 | 0.945 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SIK3 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:16306228 |
| SIK1 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:16306228 |
| MEIS1 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | imex:IM-13602|pubmed:20159610 |
| YWHAH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAZ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAQ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAG | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CDC23 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ATPAF2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=48.6 + PDB: 4HTM | pLDDT=48.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm | 一致 |
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
1. CRTC2 — CREB-regulated transcription coactivator 2，研究基础较多，新颖性有限。
2. 蛋白大小693 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 205 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=48.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 205 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q53ET0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000160741-CRTC2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CRTC2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q53ET0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000160741-CRTC2/subcellular

![](https://images.proteinatlas.org/28454/255_E9_1_red_green.jpg)
![](https://images.proteinatlas.org/28454/255_E9_2_red_green.jpg)
![](https://images.proteinatlas.org/28454/256_E9_1_red_green.jpg)
![](https://images.proteinatlas.org/28454/256_E9_2_red_green.jpg)
![](https://images.proteinatlas.org/28454/257_E9_1_red_green.jpg)
![](https://images.proteinatlas.org/28454/257_E9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q53ET0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q53ET0 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR024786;IPR024785;IPR024784;IPR024783; |
| Pfam | PF12886;PF12885;PF12884; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000160741-CRTC2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| YWHAB | Intact, Biogrid, Opencell | true |
| YWHAE | Biogrid, Opencell | true |
| YWHAG | Intact, Biogrid, Opencell | true |
| YWHAH | Biogrid, Opencell | true |
| YWHAQ | Biogrid, Opencell | true |
| YWHAZ | Biogrid, Opencell | true |
| ACTR2 | Opencell | false |
| ARL6IP6 | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
