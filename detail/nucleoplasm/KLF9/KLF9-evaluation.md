---
type: protein-evaluation
gene: "KLF9"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## KLF9 — REJECTED (研究热度过高 (PubMed strict=288，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KLF9 / BTEB, BTEB1 |
| 蛋白名称 | Krueppel-like factor 9 |
| 蛋白大小 | 244 aa / 27.2 kDa |
| UniProt ID | Q13886 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Plasma membrane, Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 244 aa / 27.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=288 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036236, IPR013087; Pfam: PF00096 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.0/180** | |
| **归一化总分** | | | **44.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Plasma membrane, Cytosol | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 288 |
| PubMed broad count | 483 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BTEB, BTEB1 |

**关键文献**:
1. Multi-modal analysis of human hepatic stellate cells identifies novel therapeutic targets for metabolic dysfunction-associated steatotic liver disease.. *Journal of hepatology*. PMID: 39522884
2. Regulation of Nrf2 by Mitochondrial Reactive Oxygen Species in Physiology and Pathology.. *Biomolecules*. PMID: 32079324
3. Integrative multiomics analysis reveals the subtypes and key mechanisms of platinum resistance in gastric cancer: identification of KLF9 as a promising therapeutic target.. *Journal of translational medicine*. PMID: 40775648
4. Klf9 Loss of Function Protects Against Glucocorticoids Induced Skeletal Muscle Wasting.. *Journal of cachexia, sarcopenia and muscle*. PMID: 40717541
5. LncRNA-LncDACH1 mediated phenotypic switching of smooth muscle cells during neointimal hyperplasia in male arteriovenous fistulas.. *Nature communications*. PMID: 38702316

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.5 |
| 高置信度残基 (pLDDT>90) 占比 | 10.7% |
| 置信残基 (pLDDT 70-90) 占比 | 31.1% |
| 中等置信 (pLDDT 50-70) 占比 | 16.8% |
| 低置信 (pLDDT<50) 占比 | 41.4% |
| 有序区域 (pLDDT>70) 占比 | 41.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=62.5），有序残基占 41.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036236, IPR013087; Pfam: PF00096 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SIN3A | 0.911 | 0.434 | — |
| PGR | 0.898 | 0.311 | — |
| TRPM3 | 0.666 | 0.000 | — |
| FKBP5 | 0.642 | 0.070 | — |
| JUN | 0.581 | 0.091 | — |
| TSC22D3 | 0.539 | 0.047 | — |
| JUND | 0.526 | 0.091 | — |
| KLF6 | 0.519 | 0.000 | — |
| TXNIP | 0.492 | 0.051 | — |
| CEBPD | 0.490 | 0.091 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Rabac1 | psi-mi:"MI:0112"(ubiquitin reconstruction) | pubmed:30925931|imex:IM-26645 |
| GTF2H2 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:19934020|imex:IM-26889 |
| TPM3 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:35140242|imex:IM-28767 |
| CPVL | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:35140242|imex:IM-28767 |
| PPP1CA | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:35140242|imex:IM-28767 |
| CNBP | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:35140242|imex:IM-28767 |
| ANKHD1 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:35140242|imex:IM-28767 |
| SORD | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:35140242|imex:IM-28767 |
| STRAP | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:35140242|imex:IM-28767 |
| ERBIN | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:35140242|imex:IM-28767 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.5 + PDB: 无 | pLDDT=62.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Plasma membrane, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. KLF9 — Krueppel-like factor 9，研究基础较多，新颖性有限。
2. 蛋白大小244 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 288 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=62.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 288 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13886
- Protein Atlas: https://www.proteinatlas.org/ENSG00000119138-KLF9/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KLF9
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13886
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000119138-KLF9/subcellular

![](https://images.proteinatlas.org/29308/321_A12_3_red_green.jpg)
![](https://images.proteinatlas.org/29308/321_A12_4_red_green.jpg)
![](https://images.proteinatlas.org/29308/323_A12_2_red_green.jpg)
![](https://images.proteinatlas.org/29308/323_A12_3_red_green.jpg)
![](https://images.proteinatlas.org/29308/326_A12_1_red_green.jpg)
![](https://images.proteinatlas.org/29308/326_A12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q13886-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q13886 |
| SMART | SM00355; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR036236;IPR013087; |
| Pfam | PF00096; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000119138-KLF9/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PGR | Biogrid | false |
| SIN3A | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
