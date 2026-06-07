---
type: protein-evaluation
gene: "LMNA"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## LMNA — REJECTED (研究热度过高 (PubMed strict=1717，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LMNA / LMN1 |
| 蛋白名称 | Prelamin-A/C |
| 蛋白大小 | 664 aa / 74.1 kDa |
| UniProt ID | P02545 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles; UniProt: Nucleus lamina; Nucleus envelope; Nucleus, nucleoplasm; Nucl |
| 蛋白大小 | 10/10 | ×1 | 10 | 664 aa / 74.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1717 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=76.4; PDB: 1IFR, 1IVT, 1X8Y, 2XV5, 2YPT, 3GEF, 3V4Q |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR018039, IPR039008, IPR001322, IPR036415; Pfam:  |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **90.5/180** | |
| **归一化总分** | | | **50.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles | Supported |
| UniProt | Nucleus lamina; Nucleus envelope; Nucleus, nucleoplasm; Nucleus matrix; Nucleus speckle | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- intermediate filament (GO:0005882)
- lamin filament (GO:0005638)
- nuclear envelope (GO:0005635)
- nuclear lamina (GO:0005652)
- nuclear matrix (GO:0016363)
- nuclear membrane (GO:0031965)
- nuclear speck (GO:0016607)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1717 |
| PubMed broad count | 2623 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: LMN1 |

**关键文献**:
1. Identification of pathogenic gene mutations in LMNA and MYBPC3 that alter RNA splicing.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 28679633
2. LMNA-related cardiomyopathy: From molecular pathology to cardiac gene therapy.. *Journal of advanced research*. PMID: 39827909
3. Lamin A/C deficiency-mediated ROS elevation contributes to pathogenic phenotypes of dilated cardiomyopathy in iPSC model.. *Nature communications*. PMID: 39143095
4. Emery-Dreifuss muscular dystrophy.. *Handbook of clinical neurology*. PMID: 21496632
5. Epigenetics in LMNA-Related Cardiomyopathy.. *Cells*. PMID: 36899919

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.4 |
| 高置信度残基 (pLDDT>90) 占比 | 58.1% |
| 置信残基 (pLDDT 70-90) 占比 | 11.3% |
| 中等置信 (pLDDT 50-70) 占比 | 4.8% |
| 低置信 (pLDDT<50) 占比 | 25.8% |
| 有序区域 (pLDDT>70) 占比 | 69.4% |
| 可用 PDB 条目 | 1IFR, 1IVT, 1X8Y, 2XV5, 2YPT, 3GEF, 3V4Q, 3V4W, 3V5B, 6GHD |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1IFR, 1IVT, 1X8Y, 2XV5, 2YPT, 3GEF, 3V4Q, 3V4W, 3V5B, 6GHD）+ AlphaFold极高置信度预测（pLDDT=76.4），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR018039, IPR039008, IPR001322, IPR036415; Pfam: PF00038, PF00932 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000503633.1 | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-25511|pubmed:25910212 |
| ENSP00000506771.1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| MED19 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15175163 |
| Prkce | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:12169683 |
| GRB2 | psi-mi:"MI:0096"(pull down) | pubmed:12577067|mint:MINT-5216 |
| CDH1 | psi-mi:"MI:0107"(surface plasmon resonance) | pubmed:16212417 |
| KAT5 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| CFTR | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12000|pubmed:17110338 |
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |
| Invs | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.4 + PDB: 1IFR, 1IVT, 1X8Y, 2XV5, 2YPT,  | pLDDT=76.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus lamina; Nucleus envelope; Nucleus, nucleop / Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. LMNA — Prelamin-A/C，研究基础较多，新颖性有限。
2. 蛋白大小664 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1717 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1717 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P02545
- Protein Atlas: https://www.proteinatlas.org/ENSG00000160789-LMNA/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LMNA
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P02545
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P02545-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (supported)。来源: https://www.proteinatlas.org/ENSG00000160789-LMNA/subcellular

![](https://images.proteinatlas.org/6523/1841_C4_1_red_green.jpg)
![](https://images.proteinatlas.org/6523/1841_C4_2_red_green.jpg)
![](https://images.proteinatlas.org/6523/1905_E12_1_red_green.jpg)
![](https://images.proteinatlas.org/6523/1905_E12_3_red_green.jpg)
![](https://images.proteinatlas.org/6523/1908_A2_1_red_green.jpg)
![](https://images.proteinatlas.org/6523/1908_A2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P02545 |
| SMART | SM01391; |
| UniProt Domain [FT] | DOMAIN 31..387; /note="IF rod"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01188"; DOMAIN 428..545; /note="LTD"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01187" |
| InterPro | IPR018039;IPR039008;IPR001322;IPR036415; |
| Pfam | PF00038;PF00932; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000160789-LMNA/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ALOX12 | Intact, Biogrid | true |
| BANF1 | Biogrid, Opencell | true |
| DUSP13 | Intact, Biogrid | true |
| EMD | Intact, Biogrid | true |
| H2AX | Intact, Biogrid | true |
| KPNA6 | Biogrid, Opencell | true |
| LMNB1 | Intact, Biogrid, Opencell, Bioplex | true |
| LMNB2 | Intact, Biogrid, Opencell, Bioplex | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
