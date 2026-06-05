---
type: protein-evaluation
gene: "PAF1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PAF1 — REJECTED (研究热度过高 (PubMed strict=266，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PAF1 / PD2 |
| 蛋白名称 | RNA polymerase II-associated factor 1 homolog |
| 蛋白大小 | 531 aa / 60.0 kDa |
| UniProt ID | Q8N7H5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nucleoli fibrillar center, Vesicles; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 531 aa / 60.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=266 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.9; PDB: 4M6T, 5ZYQ, 6GMH, 6TED, 7OOP, 7OPC, 7OPD |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR007133; Pfam: PF03985 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli fibrillar center, Vesicles | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- Cdc73/Paf1 complex (GO:0016593)
- cytoplasm (GO:0005737)
- fibrillar center (GO:0001650)
- membrane (GO:0016020)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 266 |
| PubMed broad count | 458 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PD2 |

**关键文献**:
1. Parafibromin--functional insights.. *Journal of internal medicine*. PMID: 19522828
2. Structure of activated transcription complex Pol II-DSIF-PAF-SPT6.. *Nature*. PMID: 30135578
3. Beyond gene expression: how MYC relieves transcription stress.. *Trends in cancer*. PMID: 37422352
4. ARF alters PAF1 complex integrity to selectively repress oncogenic transcription programs upon p53 loss.. *Molecular cell*. PMID: 39532099
5. Multiple direct and indirect roles of the Paf1 complex in transcription elongation, splicing, and histone modifications.. *Cell reports*. PMID: 39244754

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.9 |
| 高置信度残基 (pLDDT>90) 占比 | 10.0% |
| 置信残基 (pLDDT 70-90) 占比 | 41.1% |
| 中等置信 (pLDDT 50-70) 占比 | 18.6% |
| 低置信 (pLDDT<50) 占比 | 30.3% |
| 有序区域 (pLDDT>70) 占比 | 51.1% |
| 可用 PDB 条目 | 4M6T, 5ZYQ, 6GMH, 6TED, 7OOP, 7OPC, 7OPD, 7UNC, 7UND, 8A3Y |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=66.9），有序残基占 51.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007133; Pfam: PF03985 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CDC73 | 0.999 | 0.998 | — |
| SUPT5H | 0.999 | 0.984 | — |
| CTR9 | 0.999 | 0.997 | — |
| RTF1 | 0.999 | 0.997 | — |
| LEO1 | 0.999 | 0.998 | — |
| WDR61 | 0.998 | 0.976 | — |
| POLR2A | 0.996 | 0.996 | — |
| SUPT16H | 0.994 | 0.986 | — |
| SUPT4H1 | 0.994 | 0.911 | — |
| SSRP1 | 0.985 | 0.963 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CAB3 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| RTF1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| SPT16 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| CDC73 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| CTR9 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| SSA1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| POB3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:11927560|imex:IM-19478 |
| SPT5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:11927560|imex:IM-19478 |
| LEO1 | psi-mi:"MI:0018"(two hybrid) | pubmed:18719252 |
| HSP60 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.9 + PDB: 4M6T, 5ZYQ, 6GMH, 6TED, 7OOP,  | pLDDT=66.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Nucleoli fibrillar center, Vesicl | 一致 |
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
1. PAF1 — RNA polymerase II-associated factor 1 homolog，研究基础较多，新颖性有限。
2. 蛋白大小531 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 266 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=66.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 266 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N7H5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000006712-PAF1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PAF1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N7H5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000006712-PAF1/subcellular

![](https://images.proteinatlas.org/71954/1469_H11_2_red_green.jpg)
![](https://images.proteinatlas.org/71954/1469_H11_3_red_green.jpg)
![](https://images.proteinatlas.org/71954/1478_H11_1_red_green.jpg)
![](https://images.proteinatlas.org/71954/1478_H11_3_red_green.jpg)
![](https://images.proteinatlas.org/71954/1495_A8_2_red_green.jpg)
![](https://images.proteinatlas.org/71954/1495_A8_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8N7H5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
