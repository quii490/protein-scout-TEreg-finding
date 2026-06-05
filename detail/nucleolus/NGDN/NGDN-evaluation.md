---
type: protein-evaluation
gene: "NGDN"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation, recovery, re-evaluation]
status: scored
---

## NGDN 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NGDN / C14orf120 |
| 蛋白名称 | Neuroguidin |
| 蛋白大小 | 315 aa / 35.9 kDa |
| UniProt ID | Q8NEJ9 |
| 数据采集时间 | 2026-06-03 23:41:10 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoli, Mitochondria; 额外: Nucleoplasm; UniProt: Nucleus; Nucleus, nucleolus; Chromosome, centromer |
| 蛋白大小 | 10/10 | x1 | 10 | 315 aa / 35.9 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=6 篇 (<= 20 -> 10) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=75.8; PDB: 7MQ8 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR007146; Pfam: PF04000 |
| PPI 网络 | 2/10 | x3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | -- | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli, Mitochondria; 额外: Nucleoplasm | Approved |
| UniProt | Nucleus; Nucleus, nucleolus; Chromosome, centromere; Cytoplasm; Cell projection,... | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- axon (GO:0030424)
- chromosome, centromeric region (GO:0000775)
- dendrite (GO:0030425)
- filopodium (GO:0030175)
- mitochondrion (GO:0005739)
- nucleolus (GO:0005730)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6 |
| PubMed broad count | 15 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C14orf120 |

**关键文献**:
1. Human AATF/Che-1 forms a nucleolar protein complex with NGDN and NOL10 required for 40S ribosomal subunit synthesis.. *Nucleic acids research*. PMID: 27599843
2. High expression of neuroguidin increases the sensitivity of acute myeloid leukemia cells to chemotherapeutic drugs.. *Journal of hematology & oncology*. PMID: 25887473
3. Identification of potential mutations and genomic alterations in the epithelial and spindle cell components of biphasic synovial sarcomas using a human exome SNP chip.. *BMC medical genomics*. PMID: 26503545
4. Identification and validation of novel marker genes to predict potential gestational diabetes mellitus patients by WGCNA and machine learning.. *Ginekologia polska*. PMID: 41117218
5. Identification of the RNA polymerase I-RNA interactome.. *Nucleic acids research*. PMID: 30169671

**评价**: 极度新颖，几乎未被系统研究（PubMed <= 20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.8 |
| 高置信度残基 (pLDDT>90) 占比 | 28.6% |
| 置信残基 (pLDDT 70-90) 占比 | 37.5% |
| 中等置信 (pLDDT 50-70) 占比 | 21.6% |
| 低置信 (pLDDT<50) 占比 | 12.4% |
| 有序区域 (pLDDT>70) 占比 | 66.1% |
| 可用 PDB 条目 | 7MQ8 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=75.8，有序区 66.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007146; Pfam: PF04000 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RPS6 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| RRP1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-26310|pubmed:20926688 |
| H9A910 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:30177828|imex:IM-26452 |
| AATF | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| SLC16A1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| NOM1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MFAP1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CSNK2B | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.8 + PDB: 7MQ8 | pLDDT=75.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus, nucleolus; Chromosome, centromer / Nucleoli, Mitochondria; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐ 

**核心优势**:
1. NGDN -- Neuroguidin，极度新颖，几乎未被系统研究（PubMed <= 20篇）。
2. 蛋白大小315 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NEJ9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000129460-NGDN/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NGDN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NEJ9
- STRING: https://string-db.org/network/9606.NGDN
- Packet data timestamp: 2026-06-03 23:41:10

---
*本报告为全量重评估 (Full Re-evaluation) -- Recovery from false-rejection。所有评分基于最新harvest packet数据，使用标准/180评分体系计算。*

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (supported)。来源: https://www.proteinatlas.org/ENSG00000129460-NGDN/subcellular

![](https://images.proteinatlas.org/944/38_A5_1_red_green.jpg)
![](https://images.proteinatlas.org/944/38_A5_2_red_green.jpg)
![](https://images.proteinatlas.org/944/39_A5_1_red_green.jpg)
![](https://images.proteinatlas.org/944/39_A5_2_red_green.jpg)
![](https://images.proteinatlas.org/944/40_A5_1_red_green.jpg)
![](https://images.proteinatlas.org/944/40_A5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8NEJ9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
