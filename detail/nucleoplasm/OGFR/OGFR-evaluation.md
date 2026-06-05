---
type: protein-evaluation
gene: "OGFR"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## OGFR 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | OGFR |
| 蛋白名称 | Opioid growth factor receptor |
| 蛋白大小 | 677 aa / 73.3 kDa |
| UniProt ID | Q9NZT2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 677 aa / 73.3 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=62 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR006757, IPR006770, IPR039574; Pfam: PF04680, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 9 partners; IntAct 8 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **100.0/180** | |
| **归一化总分** | | | **55.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- membrane (GO:0016020)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 62 |
| PubMed broad count | 150 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. CIRBP-OGFR axis safeguards against cardiomyocyte apoptosis and cardiotoxicity induced by chemotherapy.. *International journal of biological sciences*. PMID: 35541895
2. Revealing Stress Granule Compositional Heterogeneity through Antibody-Guided Proximity Labeling.. *Analytical chemistry*. PMID: 40198209
3. The biology of the opioid growth factor receptor (OGFr).. *Brain research. Brain research reviews*. PMID: 11890982
4. Targeting OGF/OGFR signal to mitigate doxorubicin-induced cardiotoxicity.. *Free radical biology & medicine*. PMID: 39122201
5. Altered G-Protein Transduction Protein Gene Expression in the Testis of Infertile Patients with Nonobstructive Azoospermia.. *DNA and cell biology*. PMID: 37610843

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.5 |
| 高置信度残基 (pLDDT>90) 占比 | 30.1% |
| 置信残基 (pLDDT 70-90) 占比 | 4.9% |
| 中等置信 (pLDDT 50-70) 占比 | 6.9% |
| 低置信 (pLDDT<50) 占比 | 58.1% |
| 有序区域 (pLDDT>70) 占比 | 35.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=60.5），有序残基占 35.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR006757, IPR006770, IPR039574; Pfam: PF04680, PF04664 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PENK | 0.987 | 0.000 | — |
| CSNK1G2 | 0.538 | 0.000 | — |
| HELZ2 | 0.500 | 0.000 | — |
| PPP1R12C | 0.491 | 0.000 | — |
| CDK4 | 0.475 | 0.475 | — |
| OPRD1 | 0.428 | 0.000 | — |
| HAP1 | 0.426 | 0.000 | — |
| OPRM1 | 0.410 | 0.000 | — |
| UPF1 | 0.403 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GSTK1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| HSCB | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28380382|imex:IM-25655 |
| CDK4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SELENBP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| WASF3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TGIF2LY | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PRKCE | psi-mi:"MI:0096"(pull down) | pubmed:32707033|imex:IM-29257| |
| ENST00000290291 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 9，IntAct interactions: 8
- 调控相关比例: 0 / 9 = 0%

**评价**: STRING 9 个预测互作，IntAct 8 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.5 + PDB: 无 | pLDDT=60.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 9 + 8 interactions | 数据充分 |

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
1. OGFR — Opioid growth factor receptor，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小677 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 62 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=60.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NZT2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000060491-OGFR/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=OGFR
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NZT2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000060491-OGFR/subcellular

![](https://images.proteinatlas.org/17899/143_B2_1_red_green.jpg)
![](https://images.proteinatlas.org/17899/143_B2_2_red_green.jpg)
![](https://images.proteinatlas.org/17899/144_B2_1_red_green.jpg)
![](https://images.proteinatlas.org/17899/144_B2_2_red_green.jpg)
![](https://images.proteinatlas.org/17899/145_B2_1_red_green.jpg)
![](https://images.proteinatlas.org/17899/145_B2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NZT2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
