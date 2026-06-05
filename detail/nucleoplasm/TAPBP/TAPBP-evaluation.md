---
type: protein-evaluation
gene: "TAPBP"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TAPBP 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TAPBP / NGS17, TAPA |
| 蛋白名称 | Tapasin |
| 蛋白大小 | 448 aa / 47.6 kDa |
| UniProt ID | O15533 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoli, Plasma membrane; 额外: Mitochondria; UniProt: Endoplasmic reticulum membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 448 aa / 47.6 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=62 篇 (≤80→4) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=87.1; PDB: 3F8U, 6ENY, 7QNG, 7QPD, 7TUE, 7TUF, 7TUG |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR007110, IPR036179, IPR013783, IPR003597, IPR050 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **104.0/180** | |
| **归一化总分** | | | **57.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli, Plasma membrane; 额外: Mitochondria | Approved |
| UniProt | Endoplasmic reticulum membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum membrane (GO:0005789)
- endoplasmic reticulum-Golgi intermediate compartment membrane (GO:0033116)
- Golgi membrane (GO:0000139)
- lumenal side of endoplasmic reticulum membrane (GO:0098553)
- MHC class I peptide loading complex (GO:0042824)
- phagocytic vesicle membrane (GO:0030670)
- Tapasin-ERp57 complex (GO:0061779)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 62 |
| PubMed broad count | 82 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NGS17, TAPA |

**关键文献**:
1. Identification of plasma protein biomarkers for ankylosing spondylitis by integrating proteome with genome.. *Clinical rheumatology*. PMID: 41094299
2. Exploring the cross-cancer effect of circulating proteins and discovering potential intervention targets for 13 site-specific cancers.. *Journal of the National Cancer Institute*. PMID: 38039160
3. A genetic variant in the TAPBP gene enhances cervical cancer susceptibility by increasing m(6)A modification.. *Archives of toxicology*. PMID: 38992170
4. A human TAPBP (TAPASIN)-related gene, TAPBP-R.. *European journal of immunology*. PMID: 11920573
5. Prognosis and therapy in thyroid cancer by gene signatures related to natural killer cells.. *The journal of gene medicine*. PMID: 38282150

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.1 |
| 高置信度残基 (pLDDT>90) 占比 | 63.2% |
| 置信残基 (pLDDT 70-90) 占比 | 25.0% |
| 中等置信 (pLDDT 50-70) 占比 | 6.9% |
| 低置信 (pLDDT<50) 占比 | 4.9% |
| 有序区域 (pLDDT>70) 占比 | 88.2% |
| 可用 PDB 条目 | 3F8U, 6ENY, 7QNG, 7QPD, 7TUE, 7TUF, 7TUG |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（3F8U, 6ENY, 7QNG, 7QPD, 7TUE, 7TUF, 7TUG）+ AlphaFold极高置信度预测（pLDDT=87.1），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007110, IPR036179, IPR013783, IPR003597, IPR050380; Pfam: PF07654 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| B2M | 0.999 | 0.926 | — |
| PDIA3 | 0.999 | 0.930 | — |
| CALR | 0.999 | 0.955 | — |
| HLA-A | 0.998 | 0.961 | — |
| HLA-B | 0.998 | 0.908 | — |
| CANX | 0.996 | 0.046 | — |
| TAP1 | 0.995 | 0.826 | — |
| TAP2 | 0.989 | 0.639 | — |
| HLA-C | 0.981 | 0.132 | — |
| HLA-G | 0.966 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TAP1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-11995|pubmed:17055437 |
| rpoB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| capR | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| TAP2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:12213826|imex:IM-19451 |
| hisD | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| Cbl | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:27474268|imex:IM-25617 |
| CALR | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| CFTR | psi-mi:"MI:0096"(pull down) | pubmed:29924966|imex:IM-27204 |
| HLA-A | psi-mi:"MI:0053"(fluorescence polarization spectro | pubmed:26439010|imex:IM-25691 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.1 + PDB: 3F8U, 6ENY, 7QNG, 7QPD, 7TUE,  | pLDDT=87.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane / Nucleoli, Plasma membrane; 额外: Mitochondria | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TAPBP — Tapasin，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小448 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 62 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O15533
- Protein Atlas: https://www.proteinatlas.org/ENSG00000231925-TAPBP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TAPBP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O15533
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O15533-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
