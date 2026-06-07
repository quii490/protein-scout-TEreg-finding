---
type: protein-evaluation
gene: "CHPF2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CHPF2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CHPF2 / CHSY3, CSGLCAT, KIAA1402 |
| 蛋白名称 | Chondroitin sulfate glucuronyltransferase |
| 蛋白大小 | 772 aa / 85.9 kDa |
| UniProt ID | Q9P2E5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Nucleoplasm, Cytosol; UniProt: Golgi apparatus, Golgi stack membrane |
| 蛋白大小 | 10/10 | x1 | 10 | 772 aa / 85.9 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=84.3; PDB: 无 |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR008428, IPR051227; Pfam: PF05679 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.5/180** | |
| **归一化总分** | | | **68.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Approved |
| UniProt | Golgi apparatus, Golgi stack membrane | Swiss-Prot/TremBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- Golgi apparatus (GO:0005794)
- Golgi cisterna membrane (GO:0032580)
- Golgi membrane (GO:0000139)
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 16 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CHSY3, CSGLCAT, KIAA1402 |

**关键文献**:
1. Astrocyte Extracellular Matrix Modulates Neuronal Dendritic Development.. *Glia*. PMID: 40192069
2. Astrocyte extracellular matrix modulates neuronal dendritic development.. *bioRxiv : the preprint server for biology*. PMID: 39211148
3. Discovery and Validation of a New Biomarker Integrating Ferroptosis and Glycolysis-Related Genes in Bladder Cancer.. *IUBMB life*. PMID: 40401561
4. Exosomal lncRNA DUXAP8 affecting CHPF2 in the pathogenesis of intracranial aneurysms.. *Gene*. PMID: 38341004
5. Four Immune-Related Genes (FN1, UGCG, CHPF2 and THBS2) as Potential Diagnostic and Prognostic Biomarkers for Carbon Nanotube-Induced Mesothelioma.. *International journal of general medicine*. PMID: 34511983

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.3 |
| 高置信度残基 (pLDDT>90) 占比 | 55.2% |
| 置信残基 (pLDDT 70-90) 占比 | 29.9% |
| 中等置信 (pLDDT 50-70) 占比 | 6.9% |
| 低置信 (pLDDT<50) 占比 | 8.0% |
| 有序区域 (pLDDT>70) 占比 | 85.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=84.3，有序区 85.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008428, IPR051227; Pfam: PF05679 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CSGALNACT2 | 0.936 | 0.091 | — |
| CSGALNACT1 | 0.933 | 0.091 | — |
| CHPF | 0.894 | 0.000 | — |
| CHSY3 | 0.847 | 0.450 | — |
| CHSY1 | 0.802 | 0.091 | — |
| B4GALNT1 | 0.674 | 0.000 | — |
| B3GAT3 | 0.659 | 0.000 | — |
| B4GALT7 | 0.656 | 0.000 | — |
| MOGS | 0.648 | 0.000 | — |
| CHST13 | 0.598 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SCGB2A2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DPEP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GOLT1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Ptpn13 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| FEN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| ATP1B3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SFTPC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TMEM106A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PTCH1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| BTNL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.3 + PDB: 无 | pLDDT=84.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus, Golgi stack membrane / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CHPF2 -- Chondroitin sulfate glucuronyltransferase，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小772 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9P2E5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000033100-CHPF2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CHPF2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9P2E5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000033100-CHPF2/subcellular

![](https://images.proteinatlas.org/20992/189_H9_1_red_green.jpg)
![](https://images.proteinatlas.org/20992/189_H9_2_red_green.jpg)
![](https://images.proteinatlas.org/20992/190_H9_1_red_green.jpg)
![](https://images.proteinatlas.org/20992/190_H9_2_red_green.jpg)
![](https://images.proteinatlas.org/20992/191_H9_1_red_green.jpg)
![](https://images.proteinatlas.org/20992/191_H9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9P2E5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9P2E5 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR008428;IPR051227; |
| Pfam | PF05679; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000033100-CHPF2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| TMPRSS4 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
