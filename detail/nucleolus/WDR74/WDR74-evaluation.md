---
type: protein-evaluation
gene: "WDR74"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## WDR74 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | WDR74 / NSA1 |
| 蛋白名称 | WD repeat-containing protein 74 |
| 蛋白大小 | 385 aa / 42.4 kDa |
| UniProt ID | Q6RFH5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm, Nucleoli; UniProt: Nucleus, nucleolus; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 385 aa / 42.4 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=21 篇 (≤40→8) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=83.3; PDB: 8FKP, 8FKR, 8FKT, 8FKV |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR015943, IPR036322, IPR001680, IPR037379; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **141.0/180** | |
| **归一化总分** | | | **78.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli | Supported |
| UniProt | Nucleus, nucleolus; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- preribosome, large subunit precursor (GO:0030687)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 21 |
| PubMed broad count | 29 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NSA1 |

**关键文献**:
1. Identification of WDR74 and TNFRSF12A as biomarkers for early osteoarthritis using machine learning and immunohistochemistry.. *Frontiers in immunology*. PMID: 39935469
2. Increased CAPG inhibits ferroptosis to drive tumor proliferation and sorafenib resistance in hepatocellular carcinoma via the WDR74-p53-SLC7A11 pathway.. *International journal of biological sciences*. PMID: 40959275
3. A Pan-Cancer Analysis of the Oncogenic Role of WD Repeat Domain 74 in Multiple Tumors.. *Frontiers in genetics*. PMID: 35559034
4. WDR74 modulates melanoma tumorigenesis and metastasis through the RPL5-MDM2-p53 pathway.. *Oncogene*. PMID: 32005977
5. WDR74 rs11231247 contributes to the susceptibility and prognosis of non-small cell lung cancer.. *Pathology, research and practice*. PMID: 36701849

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.3 |
| 高置信度残基 (pLDDT>90) 占比 | 65.2% |
| 置信残基 (pLDDT 70-90) 占比 | 15.6% |
| 中等置信 (pLDDT 50-70) 占比 | 6.0% |
| 低置信 (pLDDT<50) 占比 | 13.2% |
| 有序区域 (pLDDT>70) 占比 | 80.8% |
| 可用 PDB 条目 | 8FKP, 8FKR, 8FKT, 8FKV |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（8FKP, 8FKR, 8FKT, 8FKV）+ AlphaFold高质量预测（pLDDT=83.3），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR015943, IPR036322, IPR001680, IPR037379; Pfam: PF00400 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BOP1 | 0.999 | 0.969 | — |
| EBNA1BP2 | 0.998 | 0.941 | — |
| WDR12 | 0.998 | 0.941 | — |
| PES1 | 0.997 | 0.954 | — |
| MAK16 | 0.997 | 0.978 | — |
| MRTO4 | 0.997 | 0.938 | — |
| NSA2 | 0.997 | 0.938 | — |
| FTSJ3 | 0.997 | 0.824 | — |
| RPF1 | 0.997 | 0.976 | — |
| DDX18 | 0.994 | 0.953 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RGS2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| "l | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Rtnl1 | psi-mi:"MI:0963"(interactome parallel affinity cap | pubmed:21447707|imex:IM-17304 |
| HDAC11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-18733|pubmed:23752268 |
| RRP1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-26310|pubmed:20926688 |
| ARHGEF19 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| ARHGAP23 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| FGD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| ARHGEF4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| CCNJL | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.3 + PDB: 8FKP, 8FKR, 8FKT, 8FKV | pLDDT=83.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus, nucleolus; Nucleus / Nucleoplasm, Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. WDR74 — WD repeat-containing protein 74，非常新颖，仅有少数基础研究。
2. 蛋白大小385 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 21 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6RFH5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000133316-WDR74/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=WDR74
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6RFH5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000133316-WDR74/subcellular

![](https://images.proteinatlas.org/38419/593_D2_1_red_green.jpg)
![](https://images.proteinatlas.org/38419/593_D2_2_red_green.jpg)
![](https://images.proteinatlas.org/38419/594_D2_1_red_green.jpg)
![](https://images.proteinatlas.org/38419/594_D2_2_red_green.jpg)
![](https://images.proteinatlas.org/38419/596_D2_1_red_green.jpg)
![](https://images.proteinatlas.org/38419/596_D2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6RFH5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
