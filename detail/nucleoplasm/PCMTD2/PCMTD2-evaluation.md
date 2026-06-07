---
type: protein-evaluation
gene: "PCMTD2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PCMTD2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PCMTD2 / C20orf36 |
| 蛋白名称 | Protein-L-isoaspartate O-methyltransferase domain-containing protein 2 |
| 蛋白大小 | 361 aa / 41.1 kDa |
| UniProt ID | Q9NV79 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Mitochondria; 额外: Nucleoplasm; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 361 aa / 41.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=82.9; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000682, IPR029063; Pfam: PF01135 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.5/180** | |
| **归一化总分** | | | **68.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria; 额外: Nucleoplasm | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 9 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C20orf36 |

**关键文献**:
1. Changes in leukocyte gene expression profiles induced by antineoplastic chemotherapy.. *Oncology letters*. PMID: 22783446
2. Integrated Proteomics Reveal ALDH1A1 as an Oncogenic Driver and Regulatory Hub in Hepatocellular Carcinoma.. *Cancer genomics & proteomics*. PMID: 42055623
3. The CUL5 E3 ligase complex negatively regulates central signaling pathways in CD8(+) T cells.. *Nature communications*. PMID: 38242867
4. A genome-wide association study of European advanced cancer patients treated with opioids identifies regulatory variants on chromosome 20 associated with pain intensity.. *European journal of pain (London, England)*. PMID: 39629963
5. Mental retardation in a girl with a subtelomeric deletion on chromosome 20q and complete deletion of the myelin transcription factor 1 gene (MYT1).. *Clinical genetics*. PMID: 18341605

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.9 |
| 高置信度残基 (pLDDT>90) 占比 | 71.5% |
| 置信残基 (pLDDT 70-90) 占比 | 6.9% |
| 中等置信 (pLDDT 50-70) 占比 | 3.9% |
| 低置信 (pLDDT<50) 占比 | 17.7% |
| 有序区域 (pLDDT>70) 占比 | 78.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=82.9，有序区 78.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000682, IPR029063; Pfam: PF01135 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CUL5 | 0.754 | 0.721 | — |
| PRPSAP1 | 0.577 | 0.000 | — |
| CHST10 | 0.498 | 0.000 | — |
| ZNF337 | 0.489 | 0.000 | — |
| ELOB | 0.486 | 0.422 | — |
| PRDM13 | 0.473 | 0.000 | — |
| ANKRD16 | 0.471 | 0.000 | — |
| RNF7 | 0.463 | 0.464 | — |
| VWC2L | 0.461 | 0.000 | — |
| EEF1AKMT1 | 0.460 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Iqcb1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| Rpgrip1l | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| CUL5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| ATP13A2 | psi-mi:"MI:0112"(ubiquitin reconstruction) | pubmed:22645275|imex:IM-17891 |
| IFITM3 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| KSR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27086506|imex:IM-25748 |
| ACSL6 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SEPTIN3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| VAC14 | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-23318|pubmed:25416956 |
| TRIP13 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.9 + PDB: 无 | pLDDT=82.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Mitochondria; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PCMTD2 — Protein-L-isoaspartate O-methyltransferase domain-containing protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小361 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NV79
- Protein Atlas: https://www.proteinatlas.org/ENSG00000203880-PCMTD2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PCMTD2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NV79
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Mitochondria (approved)。来源: https://www.proteinatlas.org/ENSG00000203880-PCMTD2/subcellular

![](https://images.proteinatlas.org/57849/1005_B4_1_red_green.jpg)
![](https://images.proteinatlas.org/57849/1005_B4_2_red_green.jpg)
![](https://images.proteinatlas.org/57849/1015_B4_1_red_green.jpg)
![](https://images.proteinatlas.org/57849/1015_B4_2_red_green.jpg)
![](https://images.proteinatlas.org/57849/1061_B11_1_red_green.jpg)
![](https://images.proteinatlas.org/57849/1061_B11_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NV79-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NV79 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR000682;IPR029063; |
| Pfam | PF01135; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000203880-PCMTD2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ATXN1 | Intact | false |
| CAPZB | Opencell | false |
| CUL5 | Biogrid | false |
| ELOB | Biogrid | false |
| ELOC | Biogrid | false |
| HTRA2 | Intact | false |
| JPH3 | Intact | false |
| NOS3 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
