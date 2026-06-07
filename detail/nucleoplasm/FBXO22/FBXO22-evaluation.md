---
type: protein-evaluation
gene: "FBXO22"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FBXO22 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FBXO22 / FBX22 |
| 蛋白名称 | F-box only protein 22 |
| 蛋白大小 | 403 aa / 44.5 kDa |
| UniProt ID | Q8NEZ5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm; Nucleus; Cytoplasm, myofibril, sarcomere, Z line |
| 蛋白大小 | 10/10 | ×1 | 10 | 403 aa / 44.5 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=76 篇 (≤80→4) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=86.2; PDB: 8S7D, 8S7E, 8UA3, 8UA6 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR036047, IPR001810, IPR019494; Pfam: PF00646, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.0/180** | |
| **归一化总分** | | | **62.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm; Nucleus; Cytoplasm, myofibril, sarcomere, Z line | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleus (GO:0005634)
- Z disc (GO:0030018)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 76 |
| PubMed broad count | 101 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FBX22 |

**关键文献**:
1. Nrf2 Activation Promotes Lung Cancer Metastasis by Inhibiting the Degradation of Bach1.. *Cell*. PMID: 31257023
2. A CRISPR activation screen identifies FBXO22 supporting targeted protein degradation.. *Nature chemical biology*. PMID: 38965383
3. Recruitment of FBXO22 for targeted degradation of NSD2.. *Nature chemical biology*. PMID: 38965384
4. FBXO22 promotes the development of hepatocellular carcinoma by regulating the ubiquitination and degradation of p21.. *Journal of experimental & clinical cancer research : CR*. PMID: 30808376
5. The diagnostic yield, candidate genes, and pitfalls for a genetic study of intellectual disability in 118 middle eastern families.. *Scientific reports*. PMID: 36344539

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.2 |
| 高置信度残基 (pLDDT>90) 占比 | 64.8% |
| 置信残基 (pLDDT 70-90) 占比 | 21.8% |
| 中等置信 (pLDDT 50-70) 占比 | 7.2% |
| 低置信 (pLDDT<50) 占比 | 6.2% |
| 有序区域 (pLDDT>70) 占比 | 86.6% |
| 可用 PDB 条目 | 8S7D, 8S7E, 8UA3, 8UA6 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FBXO22/FBXO22-PAE.png]]

**评价**: PDB实验结构（8S7D, 8S7E, 8UA3, 8UA6）+ AlphaFold高质量预测（pLDDT=86.2），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036047, IPR001810, IPR019494; Pfam: PF00646, PF10442 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SKP1 | 0.999 | 0.994 | — |
| CUL1 | 0.968 | 0.818 | — |
| NFKBIA | 0.901 | 0.000 | — |
| RBX1 | 0.778 | 0.554 | — |
| BACH1 | 0.759 | 0.625 | — |
| KDM4A | 0.748 | 0.292 | — |
| KDM4B | 0.666 | 0.510 | — |
| WDR12 | 0.620 | 0.000 | — |
| TP53 | 0.614 | 0.510 | — |
| NAE1 | 0.596 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| COPS5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| COPS6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| CFTR | psi-mi:"MI:0096"(pull down) | pubmed:29924966|imex:IM-27204 |
| SKP1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| 708601" | psi-mi:"MI:0096"(pull down) | pubmed:24189400|imex:IM-21413 |
| PLEKHA7 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-25739|pubmed:28877994 |
| BACH1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NCOR2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| CHEK2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:23178491|imex:IM-25034 |
| CPAP | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.2 + PDB: 8S7D, 8S7E, 8UA3, 8UA6 | pLDDT=86.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Cytoplasm, myofibril, sarcomer / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FBXO22 — F-box only protein 22，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小403 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 76 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NEZ5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000167196-FBXO22/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FBXO22
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NEZ5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FBXO22/FBXO22-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8NEZ5 |
| SMART | SM01204; |
| UniProt Domain [FT] | DOMAIN 21..67; /note="F-box" |
| InterPro | IPR036047;IPR001810;IPR019494; |
| Pfam | PF00646;PF10442; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000167196-FBXO22/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CUL1 | Intact, Biogrid | true |
| SKP1 | Intact, Biogrid | true |
| BACH1 | Biogrid | false |
| BSG | Biogrid | false |
| COPS5 | Biogrid | false |
| COPS6 | Biogrid | false |
| KDM4A | Biogrid | false |
| KDM4B | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
