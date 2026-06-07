---
type: protein-evaluation
gene: "TEX19"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TEX19 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TEX19 |
| 蛋白名称 | Testis-expressed protein 19 |
| 蛋白大小 | 164 aa / 18.5 kDa |
| UniProt ID | Q8NA77 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 164 aa / 18.5 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=22 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=56.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR029093; Pfam: PF15553 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **106.0/180** | |
| **归一化总分** | | | **58.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 22 |
| PubMed broad count | 29 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Tex19, a mammalian-specific protein with a restricted expression in pluripotent stem cells and germ line.. *Stem cells (Dayton, Ohio)*. PMID: 18096721
2. In silico modeling of the interaction between TEX19 and LIRE1, and analysis of TEX19 gene missense SNPs.. *Molecular genetics & genomic medicine*. PMID: 34036740
3. The mammalian-specific Tex19.1 gene plays an essential role in spermatogenesis and placenta-supported development.. *Human reproduction (Oxford, England)*. PMID: 23674551
4. Thermal inkjet bioprinting drastically alters cell phenotype.. *Biofabrication*. PMID: 37160133
5. Human germ/stem cell-specific gene TEX19 influences cancer cell proliferation and cancer prognosis.. *Molecular cancer*. PMID: 28446200

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 56.3 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 26.8% |
| 中等置信 (pLDDT 50-70) 占比 | 36.0% |
| 低置信 (pLDDT<50) 占比 | 37.2% |
| 有序区域 (pLDDT>70) 占比 | 26.8% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=56.3），有序残基占 26.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029093; Pfam: PF15553 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TEX48 | 0.571 | 0.000 | — |
| SECTM1 | 0.462 | 0.000 | — |
| TEX9 | 0.447 | 0.000 | — |
| UTS2R | 0.438 | 0.000 | — |
| C5orf47 | 0.437 | 0.000 | — |
| TEX22 | 0.433 | 0.000 | — |
| TEX11 | 0.425 | 0.000 | — |
| SYCP1 | 0.421 | 0.000 | — |
| ZNF561 | 0.420 | 0.421 | — |
| RAD21L1 | 0.416 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ZNF648 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ZNF490 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TRIM63 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:31391242|imex:IM-25805| |
| TRIM55 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:31391242|imex:IM-25805| |
| KIF1B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| RNF11 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| ATXN3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:32814053|imex:IM-28217| |
| GRN | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:32814053|imex:IM-28217| |
| WFS1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:32814053|imex:IM-28217| |
| ZNF316 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=56.3 + PDB: 无 | pLDDT=56.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TEX19 — Testis-expressed protein 19，非常新颖，仅有少数基础研究。
2. 蛋白大小164 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 22 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=56.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NA77
- Protein Atlas: https://www.proteinatlas.org/ENSG00000182459-TEX19/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TEX19
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NA77
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8NA77 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR029093; |
| Pfam | PF15553; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000182459-TEX19/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ATXN3 | Intact | false |
| GRN | Intact | false |
| RNF11 | Intact | false |
| WFS1 | Intact | false |
| ZNF490 | Intact | false |
| ZNF648 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
