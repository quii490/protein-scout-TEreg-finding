---
type: protein-evaluation
gene: "GIMAP7"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GIMAP7 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GIMAP7 / IAN7 |
| 蛋白名称 | GTPase IMAP family member 7 |
| 蛋白大小 | 300 aa / 34.5 kDa |
| UniProt ID | Q8NHV1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Golgi apparatus, Vesicles; UniProt: Lipid droplet; Cytoplasm; Endoplasmic reticulum; Golgi appar |
| 蛋白大小 | 10/10 | ×1 | 10 | 300 aa / 34.5 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=27 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=92.7; PDB: 3ZJC |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR006703, IPR045058, IPR027417; Pfam: PF04548 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **108.5/180** | |
| **归一化总分** | | | **60.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus, Vesicles | Supported |
| UniProt | Lipid droplet; Cytoplasm; Endoplasmic reticulum; Golgi apparatus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- endoplasmic reticulum (GO:0005783)
- Golgi apparatus (GO:0005794)
- lipid droplet (GO:0005811)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 27 |
| PubMed broad count | 33 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: IAN7 |

**关键文献**:
1. Uncovering Hippo pathway-related biomarkers in acute myocardial infarction via scRNA-seq binding transcriptomics.. *Scientific reports*. PMID: 40133574
2. GIMAP7 inhibits epithelial-mesenchymal transition and glycolysis in lung adenocarcinoma cells via regulating the Smo/AMPK signaling pathway.. *Thoracic cancer*. PMID: 38151913
3. Nasal administration of anti-CD3 mAb (Foralumab) downregulates NKG7 and increases TGFB1 and GIMAP7 expression in T cells in subjects with COVID-19.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 36881624
4. GIMAP7 as a Potential Predictive Marker for Pan-Cancer Prognosis and Immunotherapy Efficacy.. *Journal of inflammation research*. PMID: 35210811
5. GIMAP7 induces oxidative stress and apoptosis of ovarian granulosa cells in polycystic ovary syndrome by inhibiting sonic hedgehog signalling pathway.. *Journal of ovarian research*. PMID: 36581994

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.7 |
| 高置信度残基 (pLDDT>90) 占比 | 86.0% |
| 置信残基 (pLDDT 70-90) 占比 | 8.0% |
| 中等置信 (pLDDT 50-70) 占比 | 3.3% |
| 低置信 (pLDDT<50) 占比 | 2.7% |
| 有序区域 (pLDDT>70) 占比 | 94.0% |
| 可用 PDB 条目 | 3ZJC |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=92.7，有序区 94.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR006703, IPR045058, IPR027417; Pfam: PF04548 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GIMAP4 | 0.929 | 0.000 | — |
| GIMAP8 | 0.895 | 0.000 | — |
| GIMAP6 | 0.888 | 0.000 | — |
| GIMAP1 | 0.833 | 0.000 | — |
| GIMAP5 | 0.830 | 0.000 | — |
| GIMAP2 | 0.815 | 0.292 | — |
| GIMAP1-GIMAP5 | 0.576 | 0.000 | — |
| SDR39U1 | 0.564 | 0.000 | — |
| TMEM204 | 0.560 | 0.000 | — |
| AIG1 | 0.558 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.7 + PDB: 3ZJC | pLDDT=92.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Lipid droplet; Cytoplasm; Endoplasmic reticulum; G / Golgi apparatus, Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GIMAP7 — GTPase IMAP family member 7，非常新颖，仅有少数基础研究。
2. 蛋白大小300 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 27 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NHV1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000179144-GIMAP7/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GIMAP7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NHV1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (supported)。来源: https://www.proteinatlas.org/ENSG00000179144-GIMAP7/subcellular

![](https://images.proteinatlas.org/20266/185_G10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/20266/185_G10_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/20266/2010_F2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/20266/2010_F2_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/20266/2055_D5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/20266/2055_D5_4_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8NHV1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
