---
type: protein-evaluation
gene: "STRADB"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## STRADB 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | STRADB / ALS2CR2, ILPIP |
| 蛋白名称 | STE20-related kinase adapter protein beta |
| 蛋白大小 | 418 aa / 47.0 kDa |
| UniProt ID | Q9C0K7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; 额外: Primary cilium, Primary cilium tip; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 418 aa / 47.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=74.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011009, IPR000719, IPR047173; Pfam: PF00069 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Primary cilium, Primary cilium tip | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- aggresome (GO:0016235)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleus (GO:0005634)
- serine/threonine protein kinase complex (GO:1902554)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3 |
| PubMed broad count | 7 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ALS2CR2, ILPIP |

**关键文献**:
1. Genome-Wide mRNA Expression Analysis of Acute Psychological Stress Responses.. *MEDICC review*. PMID: 35648061
2. Investigation of cytotoxic and apoptotic effects of disodium pentaborate decahydrate on ovarian cancer cells and assessment of gene profiling.. *Medical oncology (Northwood, London, England)*. PMID: 36308567
3. Causal links of 233 metabolic markers to benign prostatic hyperplasia: Mendelian randomization and RNA-sequencing insights.. *Journal of the Chinese Medical Association : JCMA*. PMID: 41968426

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.3 |
| 高置信度残基 (pLDDT>90) 占比 | 51.7% |
| 置信残基 (pLDDT 70-90) 占比 | 15.1% |
| 中等置信 (pLDDT 50-70) 占比 | 3.6% |
| 低置信 (pLDDT<50) 占比 | 29.7% |
| 有序区域 (pLDDT>70) 占比 | 66.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=74.3，有序区 66.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011009, IPR000719, IPR047173; Pfam: PF00069 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CAB39 | 0.999 | 0.825 | — |
| STK11 | 0.994 | 0.846 | — |
| CAB39L | 0.994 | 0.000 | — |
| TRAK2 | 0.929 | 0.000 | — |
| PRKAA2 | 0.916 | 0.101 | — |
| PRKAA1 | 0.913 | 0.101 | — |
| STRADA | 0.911 | 0.000 | — |
| DCAF12 | 0.884 | 0.000 | — |
| SEC63 | 0.824 | 0.752 | — |
| SEC61G | 0.821 | 0.750 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| STK11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:14676191 |
| CAB39 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:14676191 |
| NEB | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| GRB2 | psi-mi:"MI:0018"(two hybrid) | pubmed:18624398|imex:IM-19021 |
| TNIK | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| PIP4K2A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CCT3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RPS6KA3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CCT2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RPS6KA2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.3 + PDB: 无 | pLDDT=74.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm, Cytosol; 额外: Primary cilium, Primary  | 一致 |
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
1. STRADB — STE20-related kinase adapter protein beta，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小418 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9C0K7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000082146-STRADB/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=STRADB
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9C0K7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000082146-STRADB/subcellular

![](https://images.proteinatlas.org/26549/1399_E6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/26549/1399_E6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/26549/212_A3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/26549/212_A3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/26549/214_A3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/26549/214_A3_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9C0K7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
