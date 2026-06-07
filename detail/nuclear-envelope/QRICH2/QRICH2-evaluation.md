---
type: protein-evaluation
gene: "QRICH2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## QRICH2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | QRICH2 |
| 蛋白名称 | Glutamine-rich protein 2 |
| 蛋白大小 | 1663 aa / 180.8 kDa |
| UniProt ID | Q9H0J4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nuclear membrane; 额外: Vesicles; UniProt: Nucleus membrane; Nucleus; Cytoplasm; Cell projection, ciliu |
| 蛋白大小 | 5/10 | ×1 | 5 | 1663 aa / 180.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=44.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR032013; Pfam: PF16043 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 11 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **125.0/180** | |
| **归一化总分** | | | **69.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear membrane; 额外: Vesicles | Uncertain |
| UniProt | Nucleus membrane; Nucleus; Cytoplasm; Cell projection, cilium, flagellum | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nuclear membrane (GO:0031965)
- sperm flagellum (GO:0036126)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 22 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Whole-genome sequencing identifies new candidate genes for nonobstructive azoospermia.. *Andrology*. PMID: 36017582
2. Cerebrospinal Fluid Protein Biomarker Discovery in CLN3.. *Journal of proteome research*. PMID: 37338096
3. Loss-of-function missense variant of AKAP4 induced male infertility through reduced interaction with QRICH2 during sperm flagella development.. *Human molecular genetics*. PMID: 34415320
4. A Key regulatory protein QRICH2 governing sperm function with profound antioxidant properties, enhancing sperm viability.. *Reproductive biology*. PMID: 38772286
5. Genetic variants in QRICH2 gene among Jordanians with sperm motility disorders.. *The Libyan journal of medicine*. PMID: 40107860

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 44.6 |
| 高置信度残基 (pLDDT>90) 占比 | 0.4% |
| 置信残基 (pLDDT 70-90) 占比 | 18.3% |
| 中等置信 (pLDDT 50-70) 占比 | 10.8% |
| 低置信 (pLDDT<50) 占比 | 70.4% |
| 有序区域 (pLDDT>70) 占比 | 18.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=44.6），有序残基占 18.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR032013; Pfam: PF16043 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CFAP44 | 0.808 | 0.099 | — |
| CFAP43 | 0.794 | 0.000 | — |
| QRICH1 | 0.739 | 0.058 | — |
| CFAP69 | 0.706 | 0.000 | — |
| DNAH1 | 0.701 | 0.055 | — |
| ARMC2 | 0.699 | 0.050 | — |
| TTC21A | 0.694 | 0.061 | — |
| WDR66 | 0.669 | 0.098 | — |
| CFAP70 | 0.654 | 0.112 | — |
| TTC29 | 0.637 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EIPR1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| 14786024 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| NUP98 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| PANK2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| 40038273 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ZNRD2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| GAPDH | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MPDU1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| SNAI1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MAGEB2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 11
- 调控相关比例: 2 / 15 = 13%

**评价**: STRING 15 个预测互作，IntAct 11 个实验互作。调控相关配体占比 13%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=44.6 + PDB: 无 | pLDDT=44.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus membrane; Nucleus; Cytoplasm; Cell project / Nucleoplasm, Nuclear membrane; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 11 interactions | 数据充分 |

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
1. QRICH2 — Glutamine-rich protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1663 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=44.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H0J4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000129646-QRICH2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=QRICH2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H0J4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000129646-QRICH2/subcellular

![](https://images.proteinatlas.org/52219/2191_C9_18_blue_red_green.jpg)
![](https://images.proteinatlas.org/52219/2191_C9_30_blue_red_green.jpg)
![](https://images.proteinatlas.org/52219/1361_B6_1_red_green.jpg)
![](https://images.proteinatlas.org/52219/1361_B6_2_red_green.jpg)
![](https://images.proteinatlas.org/52219/1366_B6_1_red_green.jpg)
![](https://images.proteinatlas.org/52219/1366_B6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H0J4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H0J4 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR032013; |
| Pfam | PF16043; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000129646-QRICH2/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
