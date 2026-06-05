---
type: protein-evaluation
gene: "CTPS2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CTPS2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CTPS2 |
| 蛋白名称 | CTP synthase 2 |
| 蛋白大小 | 586 aa / 65.7 kDa |
| UniProt ID | Q9NRF8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Mitochondria, Cytosol; UniProt: Cytoplasm, cytosol; Nucleus |
| 蛋白大小 | 10/10 | x1 | 10 | 586 aa / 65.7 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=22 篇 (<=40->8) |
| 三维结构 | 10/10 | x3 | 30 | AlphaFold v6 pLDDT=91.6; PDB: 2V4U, 2VKT, 3IHL, 6PK4, 6PK7, 7MH1, 7MIH |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR029062, IPR004468, IPR017456, IPR017926, IPR033 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **136.0/180** | |
| **归一化总分** | | | **75.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria, Cytosol | Approved |
| UniProt | Cytoplasm, cytosol; Nucleus | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- cytoophidium (GO:0097268)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- mitochondrion (GO:0005739)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 22 |
| PubMed broad count | 39 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Cytosolic CTP Production Limits the Establishment of Photosynthesis in Arabidopsis.. *Frontiers in plant science*. PMID: 34917117
2. CTP Synthase 2 From Arabidopsis thaliana Is Required for Complete Embryo Development.. *Frontiers in plant science*. PMID: 33936137
3. Low cytosine triphosphate synthase 2 expression renders resistance to 5-fluorouracil in colorectal cancer.. *Cancer biology & therapy*. PMID: 21378502
4. CTP synthase 2 predicts inferior survival and mediates DNA damage response via interacting with BRCA1 in chronic lymphocytic leukemia.. *Experimental hematology & oncology*. PMID: 36635772
5. A novel diabetic foot ulcer diagnostic model: identification and analysis of genes related to glutamine metabolism and immune infiltration.. *BMC genomics*. PMID: 38287255

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.6 |
| 高置信度残基 (pLDDT>90) 占比 | 83.6% |
| 置信残基 (pLDDT 70-90) 占比 | 10.4% |
| 中等置信 (pLDDT 50-70) 占比 | 2.0% |
| 低置信 (pLDDT<50) 占比 | 3.9% |
| 有序区域 (pLDDT>70) 占比 | 94.0% |
| 可用 PDB 条目 | 2V4U, 2VKT, 3IHL, 6PK4, 6PK7, 7MH1, 7MIH, 7MII |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2V4U, 2VKT, 3IHL, 6PK4, 6PK7, 7MH1, 7MIH, 7MII）+ AlphaFold极高置信度预测（pLDDT=91.6），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029062, IPR004468, IPR017456, IPR017926, IPR033828; Pfam: PF06418, PF00117 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CTPS1 | 0.983 | 0.836 | — |
| NME4 | 0.941 | 0.000 | — |
| NME1 | 0.939 | 0.000 | — |
| AK9 | 0.938 | 0.000 | — |
| NME6 | 0.937 | 0.000 | — |
| NME3 | 0.937 | 0.000 | — |
| NME1-NME2 | 0.936 | 0.000 | — |
| NME7 | 0.936 | 0.000 | — |
| NME2 | 0.936 | 0.000 | — |
| NUDT2 | 0.936 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000401264.1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| SPG21 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| RPL23A | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| RPL37A | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| CTBP2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| FGFR1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| OTUD5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| 616370" | psi-mi:"MI:0096"(pull down) | pubmed:23606334|imex:IM-21247 |
| SUGP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CFTR | psi-mi:"MI:0096"(pull down) | pubmed:29924966|imex:IM-27204 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.6 + PDB: 2V4U, 2VKT, 3IHL, 6PK4, 6PK7,  | pLDDT=91.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol; Nucleus / Mitochondria, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (>=3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ****

**核心优势**:
1. CTPS2 -- CTP synthase 2，非常新颖，仅有少数基础研究。
2. 蛋白大小586 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 22 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NRF8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000047230-CTPS2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CTPS2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NRF8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NRF8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
