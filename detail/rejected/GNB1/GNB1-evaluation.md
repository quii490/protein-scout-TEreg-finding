---
type: protein-evaluation
gene: "GNB1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GNB1 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GNB1 |
| 蛋白名称 | Guanine nucleotide-binding protein G(I)/G(S)/G(T) subunit beta-1 |
| 蛋白大小 | 340 aa / 37.4 kDa |
| UniProt ID | P62873 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Plasma membrane; 额外: Golgi apparatus; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 340 aa / 37.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=97.1; PDB: 4KFM, 4PNK, 5HE0, 5HE1, 5HE2, 5HE3, 5UKK |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR016346, IPR015943, IPR001632, IPR020472, IPR019 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.0/180** | |
| **归一化总分** | | | **70.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane; 额外: Golgi apparatus | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- extracellular vesicle (GO:1903561)
- heterotrimeric G-protein complex (GO:0005834)
- lysosomal membrane (GO:0005765)
- membrane (GO:0016020)
- photoreceptor disc membrane (GO:0097381)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 0 |
| 别名(未计入scoring) | 无 |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 97.1 |
| 高置信度残基 (pLDDT>90) 占比 | 97.1% |
| 置信残基 (pLDDT 70-90) 占比 | 2.6% |
| 中等置信 (pLDDT 50-70) 占比 | 0.3% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 99.7% |
| 可用 PDB 条目 | 4KFM, 4PNK, 5HE0, 5HE1, 5HE2, 5HE3, 5UKK, 5UKL, 5UKM, 5UZ7 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（4KFM, 4PNK, 5HE0, 5HE1, 5HE2, 5HE3, 5UKK, 5UKL, 5UKM, 5UZ7）+ AlphaFold极高置信度预测（pLDDT=97.1），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016346, IPR015943, IPR001632, IPR020472, IPR019775; Pfam: PF25391 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GNGT1 | 0.999 | 0.999 | — |
| GNG13 | 0.999 | 0.995 | — |
| GNAI1 | 0.999 | 0.995 | — |
| GNAI2 | 0.999 | 0.990 | — |
| GNAS | 0.999 | 0.992 | — |
| GNG4 | 0.999 | 0.997 | — |
| GNG5 | 0.999 | 0.995 | — |
| GNG3 | 0.999 | 0.995 | — |
| GNAI3 | 0.999 | 0.996 | — |
| PDCL | 0.999 | 0.994 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MAP3K3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| RIPK3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| GRK2 | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:12764189 |
| MCC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| DISC1 | psi-mi:"MI:0018"(two hybrid) | pubmed:17043677|imex:IM-16650 |
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| AFP | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| EPHA7 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| CYFIP1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| NOL11 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=97.1 + PDB: 4KFM, 4PNK, 5HE0, 5HE1, 5HE2,  | pLDDT=97.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Plasma membrane; 额外: Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐ (REJECTED)

**核心优势**:
1. GNB1 — Guanine nucleotide-binding protein G(I)/G(S)/G(T) subunit beta-1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小340 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P62873
- Protein Atlas: https://www.proteinatlas.org/ENSG00000078369-GNB1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GNB1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P62873
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000078369-GNB1/subcellular

![](https://images.proteinatlas.org/40736/2147_F4_20_blue_red_green.jpg)
![](https://images.proteinatlas.org/40736/2147_F4_79_blue_red_green.jpg)
![](https://images.proteinatlas.org/40736/2152_B10_31_blue_red_green.jpg)
![](https://images.proteinatlas.org/40736/2152_B10_40_blue_red_green.jpg)
![](https://images.proteinatlas.org/40736/2171_G8_78_blue_red_green.jpg)
![](https://images.proteinatlas.org/40736/2171_G8_9_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P62873-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
