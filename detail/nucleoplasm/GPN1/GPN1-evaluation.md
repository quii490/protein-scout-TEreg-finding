---
type: protein-evaluation
gene: "GPN1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GPN1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPN1 / MBDIN, RPAP4, XAB1 |
| 蛋白名称 | GPN-loop GTPase 1 |
| 蛋白大小 | 374 aa / 41.7 kDa |
| UniProt ID | Q9HCN4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; 额外: Mitochondria; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 374 aa / 41.7 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=30 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=79.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR003593, IPR004130, IPR030230, IPR027417; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.5/180** | |
| **归一化总分** | | | **68.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Mitochondria | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- mitochondrion (GO:0005739)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 30 |
| PubMed broad count | 41 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MBDIN, RPAP4, XAB1 |

**关键文献**:
1. Gpn1 and Gpn3 associate tightly and their protein levels are mutually dependent in mammalian cells.. *FEBS letters*. PMID: 25241168
2. Identification of Domains and Factors Involved in MINIYO Nuclear Import.. *Frontiers in plant science*. PMID: 31552063
3. Genome-wide transcriptomic response of whole blood to radiation.. *Scientific reports*. PMID: 40473848
4. Npa3 interacts with Gpn3 and assembly factor Rba50 for RNA polymerase II biogenesis.. *FASEB journal : official publication of the Federation of American Societies for Experimental Biology*. PMID: 32985767
5. O-fucosylation affects abundance but not localization of select nucleocytoplasmic proteins in toxoplasma gondii.. *Glycobiology*. PMID: 40888172

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.3 |
| 高置信度残基 (pLDDT>90) 占比 | 43.3% |
| 置信残基 (pLDDT 70-90) 占比 | 34.8% |
| 中等置信 (pLDDT 50-70) 占比 | 5.9% |
| 低置信 (pLDDT<50) 占比 | 16.0% |
| 有序区域 (pLDDT>70) 占比 | 78.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=79.3，有序区 78.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003593, IPR004130, IPR030230, IPR027417; Pfam: PF03029 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RPAP2 | 0.995 | 0.880 | — |
| GPN3 | 0.987 | 0.956 | — |
| RPAP1 | 0.987 | 0.620 | — |
| GPN2 | 0.982 | 0.964 | — |
| POLR2B | 0.975 | 0.904 | — |
| POLR2J | 0.962 | 0.785 | — |
| POLR2C | 0.950 | 0.883 | — |
| RPAP3 | 0.935 | 0.174 | — |
| XPA | 0.932 | 0.230 | — |
| POLR2G | 0.915 | 0.848 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ZBED1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| NPA3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| CSNK2A1 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:22113938|imex:IM-16640 |
| WDR48 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| fla AII.2 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| EBI-1257123 | psi-mi:"MI:0096"(pull down) | pubmed:19367725|imex:IM-20587 |
| CUL5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| CUL3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| POLR2M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RPAP2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.3 + PDB: 无 | pLDDT=79.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm, Cytosol; 额外: Mitochondria | 一致 |
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
1. GPN1 — GPN-loop GTPase 1，非常新颖，仅有少数基础研究。
2. 蛋白大小374 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 30 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9HCN4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000198522-GPN1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPN1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9HCN4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000198522-GPN1/subcellular

![](https://images.proteinatlas.org/36793/593_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/36793/593_A3_2_red_green.jpg)
![](https://images.proteinatlas.org/36793/594_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/36793/594_A3_2_red_green.jpg)
![](https://images.proteinatlas.org/36793/596_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/36793/596_A3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9HCN4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9HCN4 |
| SMART | SM00382; |
| UniProt Domain [FT] | DOMAIN 18..268; /note="GPN-loop core GTPase"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01416" |
| InterPro | IPR003593;IPR004130;IPR030230;IPR027417; |
| Pfam | PF03029; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000198522-GPN1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| GPN2 | Intact, Biogrid, Bioplex | true |
| GPN3 | Intact, Biogrid | true |
| PIH1D1 | Biogrid, Bioplex | true |
| POLR1A | Biogrid, Bioplex | true |
| POLR1C | Biogrid, Opencell | true |
| POLR1D | Biogrid, Opencell | true |
| POLR2B | Biogrid, Opencell, Bioplex | true |
| POLR2C | Biogrid, Opencell, Bioplex | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
