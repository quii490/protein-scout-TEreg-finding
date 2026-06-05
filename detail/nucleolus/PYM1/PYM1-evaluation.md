---
type: protein-evaluation
gene: "PYM1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PYM1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PYM1 / PYM, WIBG |
| 蛋白名称 | Partner of Y14 and mago |
| 蛋白大小 | 204 aa / 22.7 kDa |
| UniProt ID | Q9BRP8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nucleoli, Cytosol; 额外: Cell Junctions; UniProt: Cytoplasm; Nucleus, nucleolus; Nucleus, nucleoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 204 aa / 22.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=74.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039333, IPR015362, IPR036348; Pfam: PF09282 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli, Cytosol; 额外: Cell Junctions | Supported |
| UniProt | Cytoplasm; Nucleus, nucleolus; Nucleus, nucleoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cell junction (GO:0030054)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- exon-exon junction complex (GO:0035145)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6 |
| PubMed broad count | 20 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PYM, WIBG |

**关键文献**:
1. Identification of antiviral roles for the exon-junction complex and nonsense-mediated decay in flaviviral infection.. *Nature microbiology*. PMID: 30833725
2. Genome-Wide Association Study and Phenotype Prediction of Reproductive Traits in Large White Pigs.. *Animals : an open access journal from MDPI*. PMID: 39682314
3. PYM1 limits non-canonical Exon Junction Complex occupancy in a gene architecture dependent manner to tune mRNA expression.. *Nature communications*. PMID: 40885765
4. PYM1 limits non-canonical Exon Junction Complex occupancy in a gene architecture dependent manner to tune mRNA expression.. *bioRxiv : the preprint server for biology*. PMID: 40161626
5. A novel double heme substitution produces a functional bo3 variant of the quinol oxidase aa3 of Bacillus cereus. Purification and paratial characterization.. *The Journal of biological chemistry*. PMID: 12805383

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.0 |
| 高置信度残基 (pLDDT>90) 占比 | 32.8% |
| 置信残基 (pLDDT 70-90) 占比 | 33.8% |
| 中等置信 (pLDDT 50-70) 占比 | 10.3% |
| 低置信 (pLDDT<50) 占比 | 23.0% |
| 有序区域 (pLDDT>70) 占比 | 66.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=74.0，有序区 66.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039333, IPR015362, IPR036348; Pfam: PF09282 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MAGOH | 0.999 | 0.998 | — |
| RBM8A | 0.999 | 0.997 | — |
| MAGOHB | 0.999 | 0.925 | — |
| EIF4A3 | 0.982 | 0.591 | — |
| UPF3B | 0.981 | 0.542 | — |
| UPF1 | 0.953 | 0.000 | — |
| CASC3 | 0.951 | 0.237 | — |
| UPF2 | 0.951 | 0.000 | — |
| CCDC9 | 0.900 | 0.000 | — |
| UPF3A | 0.839 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RBM8A | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12182|pubmed:19410547 |
| MAGOH | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12182|pubmed:19410547 |
| RPL23 | psi-mi:"MI:0027"(cosedimentation) | imex:IM-12182|pubmed:19410547 |
| RPS6 | psi-mi:"MI:0027"(cosedimentation) | imex:IM-12182|pubmed:19410547 |
| PRNP | psi-mi:"MI:0089"(protein array) | pubmed:18482256|imex:IM-19010 |
| purL | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| EIF4A3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:23084401|imex:IM-18688 |
| NCBP3 | psi-mi:"MI:0096"(pull down) | pubmed:26382858|imex:IM-26480 |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| RTN4IP1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.0 + PDB: 无 | pLDDT=74.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus, nucleolus; Nucleus, nucleoplas / Nucleoplasm, Nucleoli, Cytosol; 额外: Cell Junctions | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. PYM1 — Partner of Y14 and mago，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小204 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BRP8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000170473-PYM1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PYM1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BRP8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000170473-PYM1/subcellular

![](https://images.proteinatlas.org/39717/1454_D12_1_red_green.jpg)
![](https://images.proteinatlas.org/39717/1454_D12_3_red_green.jpg)
![](https://images.proteinatlas.org/39717/1502_D12_2_red_green.jpg)
![](https://images.proteinatlas.org/39717/1502_D12_3_red_green.jpg)
![](https://images.proteinatlas.org/39717/1529_C9_1_red_green.jpg)
![](https://images.proteinatlas.org/39717/1529_C9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BRP8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
