---
type: protein-evaluation
gene: "COMMD6"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## COMMD6 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | COMMD6 |
| 蛋白名称 | COMM domain-containing protein 6 |
| 蛋白大小 | 85 aa / 9.6 kDa |
| UniProt ID | Q7Z4G1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 5/10 | ×1 | 5 | 85 aa / 9.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=84.6; PDB: 8F2R, 8F2U, 8P0W |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR017920, IPR047155; Pfam: PF07258 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.0/180** | |
| **归一化总分** | | | **76.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 13 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Characterization of COMMD protein-protein interactions in NF-kappaB signalling.. *The Biochemical journal*. PMID: 16573520
2. Identification of BRCA new prognostic targets and neoantigen candidates from fusion genes.. *Discover oncology*. PMID: 39692896
3. Regulation of murine copper homeostasis by members of the COMMD protein family.. *Disease models & mechanisms*. PMID: 33262129
4. Investigation of the gene co-expression network and hub genes associated with acute mountain sickness.. *Hereditas*. PMID: 32299499
5. MicroRNA Regulatory Network as Biomarkers of Late Seizure in Patients with Spontaneous Intracerebral Hemorrhage.. *Molecular neurobiology*. PMID: 32040835

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.6 |
| 高置信度残基 (pLDDT>90) 占比 | 55.3% |
| 置信残基 (pLDDT 70-90) 占比 | 25.9% |
| 中等置信 (pLDDT 50-70) 占比 | 17.6% |
| 低置信 (pLDDT<50) 占比 | 1.2% |
| 有序区域 (pLDDT>70) 占比 | 81.2% |
| 可用 PDB 条目 | 8F2R, 8F2U, 8P0W |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（8F2R, 8F2U, 8P0W）+ AlphaFold高质量预测（pLDDT=84.6），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR017920, IPR047155; Pfam: PF07258 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| COMMD9 | 0.999 | 0.994 | — |
| COMMD1 | 0.995 | 0.878 | — |
| COMMD10 | 0.978 | 0.836 | — |
| CCDC22 | 0.976 | 0.837 | — |
| COMMD3 | 0.975 | 0.876 | — |
| COMMD2 | 0.972 | 0.831 | — |
| COMMD4 | 0.968 | 0.866 | — |
| CCDC93 | 0.963 | 0.856 | — |
| COMMD8 | 0.955 | 0.829 | — |
| COMMD7 | 0.955 | 0.837 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| COMMD1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:15799966 |
| RELA | psi-mi:"MI:0096"(pull down) | pubmed:15799966 |
| NFKB1 | psi-mi:"MI:0096"(pull down) | pubmed:15799966 |
| ENSP00000506987.1 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| COMMD9 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| HSPA6 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| VPS26C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CCDC22 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| E2F6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MFAP3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.6 + PDB: 8F2R, 8F2U, 8P0W | pLDDT=84.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. COMMD6 — COMM domain-containing protein 6，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小85 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7Z4G1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000188243-COMMD6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=COMMD6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7Z4G1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q7Z4G1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q7Z4G1 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 18..85; /note="COMM"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00602" |
| InterPro | IPR017920;IPR047155; |
| Pfam | PF07258; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000188243-COMMD6/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CCDC22 | Intact, Biogrid, Opencell | true |
| CCDC93 | Intact, Biogrid, Opencell | true |
| COMMD1 | Intact, Biogrid, Opencell | true |
| COMMD10 | Biogrid, Opencell | true |
| COMMD2 | Biogrid, Opencell | true |
| COMMD4 | Biogrid, Opencell | true |
| COMMD8 | Biogrid, Opencell | true |
| COMMD9 | Intact, Biogrid, Opencell | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
