---
type: protein-evaluation
gene: "BHLHA9"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BHLHA9 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BHLHA9 / BHLHF42 |
| 蛋白名称 | Class A basic helix-loop-helix protein 9 |
| 蛋白大小 | 235 aa / 24.1 kDa |
| UniProt ID | Q7RTU4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 235 aa / 24.1 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=23 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011598, IPR050283, IPR036638; Pfam: PF00010 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **119.5/180** | |
| **归一化总分** | | | **66.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 23 |
| PubMed broad count | 33 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BHLHF42 |

**关键文献**:
1. The duplication 17p13.3 phenotype: analysis of 21 families delineates developmental, behavioral and brain abnormalities, and rare variant phenotypes.. *American journal of medical genetics. Part A*. PMID: 23813913
2. Split hand/foot malformation with long bone deficiency associated with BHLHA9 gene duplication: a case report and review of literature.. *BMC medical genetics*. PMID: 31200655
3. Bhlha9 regulates apical ectodermal ridge formation during limb development.. *Journal of bone and mineral metabolism*. PMID: 28324176
4. Duplications of BHLHA9 are associated with ectrodactyly and tibia hemimelia inherited in non-Mendelian fashion.. *Journal of medical genetics*. PMID: 22147889
5. BHLHA9 homozygous duplication in a consanguineous family: A challenge for genetic counseling.. *American journal of medical genetics. Part A*. PMID: 36565049

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.7 |
| 高置信度残基 (pLDDT>90) 占比 | 23.8% |
| 置信残基 (pLDDT 70-90) 占比 | 6.8% |
| 中等置信 (pLDDT 50-70) 占比 | 37.0% |
| 低置信 (pLDDT<50) 占比 | 32.3% |
| 有序区域 (pLDDT>70) 占比 | 30.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=64.7），有序残基占 30.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011598, IPR050283, IPR036638; Pfam: PF00010 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TRARG1 | 0.920 | 0.000 | — |
| PITPNA | 0.834 | 0.000 | — |
| YWHAE | 0.807 | 0.000 | — |
| TIMM22 | 0.770 | 0.000 | — |
| SCARF1 | 0.759 | 0.000 | — |
| PAFAH1B1 | 0.757 | 0.000 | — |
| CRK | 0.646 | 0.000 | — |
| C4orf46 | 0.587 | 0.000 | — |
| RD3L | 0.573 | 0.000 | — |
| ASCL5 | 0.532 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.7 + PDB: 无 | pLDDT=64.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. BHLHA9 — Class A basic helix-loop-helix protein 9，非常新颖，仅有少数基础研究。
2. 蛋白大小235 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 23 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=64.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7RTU4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000205899-BHLHA9/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BHLHA9
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7RTU4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q7RTU4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q7RTU4 |
| SMART | SM00353; |
| UniProt Domain [FT] | DOMAIN 65..117; /note="bHLH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00981" |
| InterPro | IPR011598;IPR050283;IPR036638; |
| Pfam | PF00010; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000205899-BHLHA9/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BCL2L2 | Intact | false |
| BCL2L2-PABPN1 | Intact | false |
| GOLGA6L9 | Intact | false |
| KIAA0753 | Intact | false |
| KRT31 | Intact | false |
| MCRS1 | Intact | false |
| NECAB1 | Intact | false |
| POMC | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
