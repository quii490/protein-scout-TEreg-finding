---
type: protein-evaluation
gene: "OAF"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## OAF 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | OAF / NS5ATP13TP2 |
| 蛋白名称 | Out at first protein homolog |
| 蛋白大小 | 273 aa / 30.7 kDa |
| UniProt ID | Q86UD1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 273 aa / 30.7 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=55 篇 (≤60→6) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=87.4; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR026315, IPR053897, IPR053894; Pfam: PF22873, PF |
| PPI 网络 | 6/10 | ×3 | 18 | STRING 3 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **127.0/180** | |
| **归一化总分** | | | **70.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 55 |
| PubMed broad count | 366 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NS5ATP13TP2 |

**关键文献**:
1. OAF is a DAF-like gene that controls ovule development in plants.. *Communications biology*. PMID: 37156904
2. ALB, HP, OAF and RBP4 as novel protein biomarkers for identifying cured patients with pulmonary tuberculosis by DIA.. *Clinica chimica acta; international journal of clinical chemistry*. PMID: 35964702
3. Identification of OAF and PVRL1 as candidate genes for an ocular anomaly characterized by Peters anomaly type 2 and ectopia lentis.. *Experimental eye research*. PMID: 29305299
4. Plasma cell myeloma--new biological insights and advances in therapy.. *Blood*. PMID: 2465790
5. Myeloma bone disease: pathogenesis, current treatments and future targets.. *British medical bulletin*. PMID: 25190762

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.4 |
| 高置信度残基 (pLDDT>90) 占比 | 70.0% |
| 置信残基 (pLDDT 70-90) 占比 | 16.5% |
| 中等置信 (pLDDT 50-70) 占比 | 9.5% |
| 低置信 (pLDDT<50) 占比 | 4.0% |
| 有序区域 (pLDDT>70) 占比 | 86.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=87.4，有序区 86.5%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026315, IPR053897, IPR053894; Pfam: PF22873, PF14941 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TCN2 | 0.452 | 0.000 | — |
| DNAJC24 | 0.448 | 0.000 | — |
| LEMD2 | 0.431 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SFTA2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| BOC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ST3GAL4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ST8SIA4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SIAE | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PLA2G10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ARL4C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| F9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| EPHA7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LYPD4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 3，IntAct interactions: 15
- 调控相关比例: 1 / 3 = 33%

**评价**: STRING 3 个预测互作，IntAct 15 个实验互作。调控相关配体占比 33%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.4 + PDB: 无 | pLDDT=87.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 待确认 |
| PPI | STRING + IntAct | 3 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. OAF — Out at first protein homolog，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小273 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 55 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86UD1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000184232-OAF/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=OAF
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86UD1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000184232-OAF/subcellular

![](https://images.proteinatlas.org/47412/1142_F5_1_red_green.jpg)
![](https://images.proteinatlas.org/47412/1142_F5_2_red_green.jpg)
![](https://images.proteinatlas.org/47412/1216_D11_5_red_green.jpg)
![](https://images.proteinatlas.org/47412/1216_D11_6_red_green.jpg)
![](https://images.proteinatlas.org/47412/619_A9_1_red_green.jpg)
![](https://images.proteinatlas.org/47412/619_A9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86UD1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q86UD1 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR026315;IPR053897;IPR053894; |
| Pfam | PF22873;PF14941; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000184232-OAF/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| C1QTNF9B | Bioplex | false |
| CBLN4 | Bioplex | false |
| CD160 | Bioplex | false |
| CST11 | Bioplex | false |
| EDN3 | Bioplex | false |
| ELSPBP1 | Bioplex | false |
| EPDR1 | Bioplex | false |
| FAM174A | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
