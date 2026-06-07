---
type: protein-evaluation
gene: "FOXD4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FOXD4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FOXD4 / FKHL9, FOXD4A, FREAC5 |
| 蛋白名称 | Forkhead box protein D4 |
| 蛋白大小 | 439 aa / 47.3 kDa |
| UniProt ID | Q12950 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 439 aa / 47.3 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=21 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=55.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001766, IPR050211, IPR030456, IPR036388, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.0/180** | |
| **归一化总分** | | | **71.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 21 |
| PubMed broad count | 39 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FKHL9, FOXD4A, FREAC5 |

**关键文献**:
1. Human FOX gene family (Review).. *International journal of oncology*. PMID: 15492844
2. Diagnostic and prognostic values of forkhead box D4 gene in colonic adenocarcinoma.. *International journal of clinical and experimental pathology*. PMID: 33165349
3. Loss of Foxd4 Impacts Neurulation and Cranial Neural Crest Specification During Early Head Development.. *Frontiers in cell and developmental biology*. PMID: 35178396
4. On becoming neural: what the embryo can tell us about differentiating neural stem cells.. *American journal of stem cells*. PMID: 23862097
5. Update of human and mouse forkhead box (FOX) gene families.. *Human genomics*. PMID: 20650821

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 55.7 |
| 高置信度残基 (pLDDT>90) 占比 | 13.9% |
| 置信残基 (pLDDT 70-90) 占比 | 6.8% |
| 中等置信 (pLDDT 50-70) 占比 | 24.8% |
| 低置信 (pLDDT<50) 占比 | 54.4% |
| 有序区域 (pLDDT>70) 占比 | 20.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=55.7），有序残基占 20.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001766, IPR050211, IPR030456, IPR036388, IPR036390; Pfam: PF00250 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FOXD4L1 | 0.859 | 0.698 | — |
| DLAT | 0.686 | 0.686 | — |
| PDHB | 0.666 | 0.666 | — |
| PDHA1 | 0.644 | 0.628 | — |
| PDK3 | 0.631 | 0.621 | — |
| PDHX | 0.622 | 0.622 | — |
| PDK2 | 0.620 | 0.609 | — |
| CBWD1 | 0.600 | 0.000 | — |
| PPP2R2A | 0.544 | 0.544 | — |
| DMRT3 | 0.529 | 0.045 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MDFI | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| AKAP8L | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SLC4A7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ENSP00000371940.2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PDHX | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| AHCYL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FOXD2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GGPS1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PDHA1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DLAT | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=55.7 + PDB: 无 | pLDDT=55.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. FOXD4 — Forkhead box protein D4，非常新颖，仅有少数基础研究。
2. 蛋白大小439 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 21 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=55.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q12950
- Protein Atlas: https://www.proteinatlas.org/ENSG00000170122-FOXD4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FOXD4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q12950
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000170122-FOXD4/subcellular

![](https://images.proteinatlas.org/12836/136_F8_1_red_green.jpg)
![](https://images.proteinatlas.org/12836/136_F8_2_red_green.jpg)
![](https://images.proteinatlas.org/12836/97_F8_1_red_green.jpg)
![](https://images.proteinatlas.org/12836/97_F8_2_red_green.jpg)
![](https://images.proteinatlas.org/12836/99_F8_1_red_green.jpg)
![](https://images.proteinatlas.org/12836/99_F8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q12950-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q12950 |
| SMART | SM00339; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR001766;IPR050211;IPR030456;IPR036388;IPR036390; |
| Pfam | PF00250; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000170122-FOXD4/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AKAP8L | Intact | false |
| FOXD4L1 | Biogrid | false |
| HSPA9 | Bioplex | false |
| IQGAP3 | Bioplex | false |
| KRTAP10-6 | Intact | false |
| KRTAP12-2 | Intact | false |
| MDFI | Intact | false |
| PDK3 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
