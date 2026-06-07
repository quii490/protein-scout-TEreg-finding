---
type: protein-evaluation
gene: "FAM171A1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM171A1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM171A1 / APCN, C10orf38 |
| 蛋白名称 | Protein FAM171A1 |
| 蛋白大小 | 890 aa / 97.9 kDa |
| UniProt ID | Q5VUB5 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM171A1/IF_images/Hep-G2_1.jpg|Hep-G2]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM171A1/IF_images/U2OS_1.jpg|U2OS]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Plasma membrane; 额外: Nucleoplasm; UniProt: Cell membrane |
| 蛋白大小 | 8/10 | ×1 | 8 | 890 aa / 97.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=8 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=57.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR018890, IPR049175, IPR048530; Pfam: PF20771, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 11 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.0/180** | |
| **归一化总分** | | | **64.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane; 额外: Nucleoplasm | Approved |
| UniProt | Cell membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8 |
| PubMed broad count | 12 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: APCN, C10orf38 |

**关键文献**:
1. Identification of Important Modules and Biomarkers in Breast Cancer Based on WGCNA.. *OncoTargets and therapy*. PMID: 32764968
2. Astroprincin (FAM171A1, C10orf38): A Regulator of Human Cell Shape and Invasive Growth.. *The American journal of pathology*. PMID: 30312582
3. Transcriptome and DNA methylation analysis reveals molecular mechanisms underlying intrahepatic cholangiocarcinoma progression.. *Journal of cellular and molecular medicine*. PMID: 34013637
4. Screening Potential Diagnostic Biomarkers for Age-Related Sarcopenia in the Elderly Population by WGCNA and LASSO.. *BioMed research international*. PMID: 36147639
5. Estrogen receptor-α regulation of microRNA-590 targets FAM171A1-a modifier of breast cancer invasiveness.. *Oncogenesis*. PMID: 30631046

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 57.1 |
| 高置信度残基 (pLDDT>90) 占比 | 21.5% |
| 置信残基 (pLDDT 70-90) 占比 | 11.1% |
| 中等置信 (pLDDT 50-70) 占比 | 10.7% |
| 低置信 (pLDDT<50) 占比 | 56.7% |
| 有序区域 (pLDDT>70) 占比 | 32.6% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM171A1/FAM171A1-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=57.1），有序残基占 32.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR018890, IPR049175, IPR048530; Pfam: PF20771, PF10577 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RASSF10 | 0.634 | 0.239 | — |
| PCDHGB1 | 0.534 | 0.361 | — |
| UNKL | 0.517 | 0.000 | — |
| NMT2 | 0.491 | 0.000 | — |
| ARHGEF4 | 0.438 | 0.000 | — |
| ADGRA3 | 0.432 | 0.000 | — |
| CERK | 0.429 | 0.000 | — |
| CAMKK1 | 0.426 | 0.000 | — |
| DUSP7 | 0.414 | 0.000 | — |
| TNFRSF17 | 0.412 | 0.377 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MDM2 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| ETS1 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| MYH9 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| RASSF10 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| FAM171B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PCDHGB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TNFRSF17 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| EGLN3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26972000|imex:IM-22750 |
| TMEM17 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |
| Fmr1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28671696|doi:10.1038/nn |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 11，IntAct interactions: 15
- 调控相关比例: 0 / 11 = 0%

**评价**: STRING 11 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=57.1 + PDB: 无 | pLDDT=57.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane / Plasma membrane; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 11 + 15 interactions | 数据充分 |

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
1. FAM171A1 — Protein FAM171A1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小890 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=57.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5VUB5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000148468-FAM171A1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM171A1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5VUB5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM171A1/FAM171A1-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q5VUB5 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR018890;IPR049175;IPR048530; |
| Pfam | PF20771;PF10577; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000148468-FAM171A1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DYNLL1 | Biogrid, Opencell | true |
| EPHA2 | Biogrid | false |
| NTRK1 | Biogrid | false |
| RASSF10 | Intact | false |
| RHOB | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
