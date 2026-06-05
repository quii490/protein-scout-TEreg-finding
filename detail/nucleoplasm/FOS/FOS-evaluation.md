---
type: protein-evaluation
gene: "FOS"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FOS — REJECTED (研究热度过高 (PubMed strict=20815，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FOS / G0S7 |
| 蛋白名称 | Protein c-Fos |
| 蛋白大小 | 380 aa / 40.7 kDa |
| UniProt ID | P01100 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Endoplasmic reticulum; Cytoplasm, cytosol |
| 蛋白大小 | 10/10 | ×1 | 10 | 380 aa / 40.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=20815 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=57.2; PDB: 1A02, 1FOS, 1S9K |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000837, IPR004827, IPR046347; Pfam: PF00170 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus; Endoplasmic reticulum; Cytoplasm, cytosol | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytosol (GO:0005829)
- endoplasmic reticulum (GO:0005783)
- nuclear matrix (GO:0016363)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- protein-DNA complex (GO:0032993)
- RNA polymerase II transcription regulator complex (GO:0090575)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 20815 |
| PubMed broad count | 39976 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: G0S7 |

**关键文献**:
1. Immediate Early Gene c-fos in the Brain: Focus on Glial Cells.. *Brain sciences*. PMID: 35741573
2. Regulation of c-Fos gene transcription by stimulus-responsive protein kinases.. *Gene*. PMID: 35143939
3. The neurotrophic activity of PACAP on rat cerebellar granule cells is associated with activation of the protein kinase A pathway and c-fos gene expression.. *Annals of the New York Academy of Sciences*. PMID: 9928001
4. Encounters with Fos and Jun on the road to AP-1.. *Seminars in cancer biology*. PMID: 2133107
5. Phorbol-12-myristate 13-acetate inhibits Nephronectin gene expression via Protein kinase C alpha and c-Jun/c-Fos transcription factors.. *Scientific reports*. PMID: 34645824

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 57.2 |
| 高置信度残基 (pLDDT>90) 占比 | 16.8% |
| 置信残基 (pLDDT 70-90) 占比 | 4.5% |
| 中等置信 (pLDDT 50-70) 占比 | 22.4% |
| 低置信 (pLDDT<50) 占比 | 56.3% |
| 有序区域 (pLDDT>70) 占比 | 21.3% |
| 可用 PDB 条目 | 1A02, 1FOS, 1S9K |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=57.2），有序残基占 21.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000837, IPR004827, IPR046347; Pfam: PF00170 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FOSB | 0.999 | 0.359 | — |
| JUND | 0.999 | 0.907 | — |
| JUN | 0.999 | 0.999 | — |
| JUNB | 0.999 | 0.907 | — |
| ESR1 | 0.999 | 0.522 | — |
| MAF | 0.998 | 0.753 | — |
| NFATC2 | 0.998 | 0.939 | — |
| FOSL2 | 0.998 | 0.000 | — |
| CREB1 | 0.998 | 0.000 | — |
| FOSL1 | 0.998 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ICOS | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:18641334|imex:IM-26306 |
| CD28 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:18641334|imex:IM-26306 |
| PIK3R1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:18641334|imex:IM-26306 |
| EDF1 | psi-mi:"MI:0096"(pull down) | pubmed:10567391 |
| TSPAN2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| GAMT | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| GRHPR | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| GLB1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| MTERF4 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| ZMYM6 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=57.2 + PDB: 1A02, 1FOS, 1S9K | pLDDT=57.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Endoplasmic reticulum; Cytoplasm, cytosol / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. FOS — Protein c-Fos，研究基础较多，新颖性有限。
2. 蛋白大小380 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 20815 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=57.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 20815 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P01100
- Protein Atlas: https://www.proteinatlas.org/ENSG00000170345-FOS/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FOS
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P01100
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000170345-FOS/subcellular

![](https://images.proteinatlas.org/18531/115_D1_1_red_green.jpg)
![](https://images.proteinatlas.org/18531/115_D1_2_red_green.jpg)
![](https://images.proteinatlas.org/18531/116_D1_1_red_green.jpg)
![](https://images.proteinatlas.org/18531/116_D1_2_red_green.jpg)
![](https://images.proteinatlas.org/18531/117_D1_1_red_green.jpg)
![](https://images.proteinatlas.org/18531/117_D1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P01100-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
