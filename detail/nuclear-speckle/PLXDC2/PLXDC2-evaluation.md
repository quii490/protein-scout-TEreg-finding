---
type: protein-evaluation
gene: "PLXDC2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PLXDC2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PLXDC2 / TEM7R |
| 蛋白名称 | Plexin domain-containing protein 2 |
| 蛋白大小 | 529 aa / 59.6 kDa |
| UniProt ID | Q6UX71 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nuclear bodies; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 529 aa / 59.6 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=50 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=69.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR002165, IPR031152, IPR016201; Pfam: PF01437 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **98.0/180** | |
| **归一化总分** | | | **54.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies | Supported |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 50 |
| PubMed broad count | 69 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TEM7R |

**关键文献**:
1. Secreted PTEN binds PLXDC2 on macrophages to drive antitumor immunity and tumor suppression.. *Developmental cell*. PMID: 39197453
2. Loss of Plxdc2 exacerbates microglia-mediated neuroinflammation and ischemic brain injury.. *Experimental neurology*. PMID: 40345569
3. Prospective isolation of mouse and human hematopoietic stem cells using PLXDC2.. *Communications biology*. PMID: 41372396
4. Microglial PLXDC2 Modulates Aβ Phagocytosis and Inflammatory Responses.. *Biomolecules & therapeutics*. PMID: 41126775
5. Plexin Domain Containing 2, a Protein Specifically Expressed and Elevated in Human Pancreatic Cancer Tissue and Serum, Influences Cell Proliferation by Correlating With Cortactin.. *Cancer medicine*. PMID: 41365610

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.6 |
| 高置信度残基 (pLDDT>90) 占比 | 40.3% |
| 置信残基 (pLDDT 70-90) 占比 | 16.6% |
| 中等置信 (pLDDT 50-70) 占比 | 11.2% |
| 低置信 (pLDDT<50) 占比 | 31.9% |
| 有序区域 (pLDDT>70) 占比 | 56.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=69.6），有序残基占 56.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002165, IPR031152, IPR016201; Pfam: PF01437 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HCLS1 | 0.775 | 0.000 | — |
| CTTN | 0.765 | 0.000 | — |
| SERPINF1 | 0.609 | 0.000 | — |
| ZP4 | 0.539 | 0.000 | — |
| AKR1C4 | 0.501 | 0.473 | — |
| TMTC2 | 0.501 | 0.000 | — |
| RBM6 | 0.477 | 0.000 | — |
| ARHGAP22 | 0.442 | 0.000 | — |
| LRRC42 | 0.437 | 0.437 | — |
| KIAA1217 | 0.432 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Zbp1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21903422|imex:IM-17322 |
| LRRC42 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HACL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| AKR1C4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| IGFBP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| INSL5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZFYVE27 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| UPK3BL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SLC31A1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CTDNEP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=69.6 + PDB: 无 | pLDDT=69.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PLXDC2 — Plexin domain-containing protein 2，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小529 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 50 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=69.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6UX71
- Protein Atlas: https://www.proteinatlas.org/ENSG00000120594-PLXDC2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PLXDC2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6UX71
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (supported)。来源: https://www.proteinatlas.org/ENSG00000120594-PLXDC2/subcellular

![](https://images.proteinatlas.org/17268/1283_D1_2_red_green.jpg)
![](https://images.proteinatlas.org/17268/1283_D1_3_red_green.jpg)
![](https://images.proteinatlas.org/17268/1286_D1_1_red_green.jpg)
![](https://images.proteinatlas.org/17268/1286_D1_4_red_green.jpg)
![](https://images.proteinatlas.org/17268/1573_G11_1_red_green.jpg)
![](https://images.proteinatlas.org/17268/1573_G11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6UX71-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6UX71 |
| SMART | SM00423; |
| UniProt Domain [FT] | DOMAIN 327..372; /note="PSI" |
| InterPro | IPR002165;IPR031152;IPR016201; |
| Pfam | PF01437; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000120594-PLXDC2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AKR1C4 | Intact | false |
| ZBP1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
