---
type: protein-evaluation
gene: "CEP112"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CEP112 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CEP112 / CCDC46 |
| 蛋白名称 | Centrosomal protein of 112 kDa |
| 蛋白大小 | 955 aa / 112.7 kDa |
| UniProt ID | Q8N8E3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Centrosome; 额外: Midbody ring, Cytosol; UniProt: Cytoplasm, cytoskeleton, microtubule organizing center, cent |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 955 aa / 112.7 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=14 篇 (≤20→10) |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=75.8; PDB: 无 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR055310, IPR027831; Pfam: PF14846 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 13 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **131.5/180** | |
| **归一化总分** | | | **73.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Centrosome; 额外: Midbody ring, Cytosol | Approved |
| UniProt | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Nucleus; Cyt... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centrosome (GO:0005813)
- inhibitory synapse (GO:0060077)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 14 |
| PubMed broad count | 17 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CCDC46 |

**关键文献**:
1. Genetic etiological spectrum of sperm morphological abnormalities.. *Journal of assisted reproduction and genetics*. PMID: 39417902
2. CEP112 coordinates translational regulation of essential fertility genes during spermiogenesis through phase separation in humans and mice.. *Nature communications*. PMID: 39349455
3. Noncoding RNA Ginir functions as an oncogene by associating with centrosomal proteins.. *PLoS biology*. PMID: 30296263
4. Loss-of-function mutations in centrosomal protein 112 is associated with human acephalic spermatozoa phenotype.. *Clinical genetics*. PMID: 31654588
5. CRISPR/Cas9-Mediated Integration of Large Transgene into Pig CEP112 Locus.. *G3 (Bethesda, Md.)*. PMID: 31818875

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.8 |
| 高置信度残基 (pLDDT>90) 占比 | 34.0% |
| 置信残基 (pLDDT 70-90) 占比 | 39.1% |
| 中等置信 (pLDDT 50-70) 占比 | 9.7% |
| 低置信 (pLDDT<50) 占比 | 17.2% |
| 有序区域 (pLDDT>70) 占比 | 73.1% |
| 可用 PDB 条目 | 无 |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=75.8，有序区 73.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR055310, IPR027831; Pfam: PF14846 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| UBA52 | 0.627 | 0.622 | — |
| PMFBP1 | 0.623 | 0.000 | — |
| ERC1 | 0.617 | 0.610 | — |
| TSGA10 | 0.592 | 0.000 | — |
| SUN5 | 0.571 | 0.000 | — |
| CDK5RAP2 | 0.518 | 0.497 | — |
| TTC29 | 0.517 | 0.000 | — |
| CEP135 | 0.498 | 0.161 | — |
| SPATC1L | 0.464 | 0.000 | — |
| CEP131 | 0.432 | 0.051 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| efp | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| dgt | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| YWHAH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAZ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAQ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAG | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| API5 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| PRPS2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ERC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 13，IntAct interactions: 15
- 调控相关比例: 1 / 13 = 8%

**评价**: STRING 13 个预测互作，IntAct 15 个实验互作。调控相关配体占比 8%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.8 + PDB: 无 | pLDDT=75.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, microtubule organizing ce / Nucleoplasm, Centrosome; 额外: Midbody ring, Cytosol | 一致 |
| PPI | STRING + IntAct | 13 + 15 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. CEP112 — Centrosomal protein of 112 kDa，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小955 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 14 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N8E3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000154240-CEP112/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CEP112
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N8E3
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 04:48:16

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000154240-CEP112/subcellular

![](https://images.proteinatlas.org/69724/1806_C6_2_red_green.jpg)
![](https://images.proteinatlas.org/69724/1806_C6_3_red_green.jpg)
![](https://images.proteinatlas.org/69724/1861_B6_33_red_green.jpg)
![](https://images.proteinatlas.org/69724/1861_B6_34_red_green.jpg)
![](https://images.proteinatlas.org/69724/2058_F11_2_red_green.jpg)
![](https://images.proteinatlas.org/69724/2058_F11_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
