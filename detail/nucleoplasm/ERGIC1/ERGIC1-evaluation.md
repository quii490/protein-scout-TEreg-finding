---
type: protein-evaluation
gene: "ERGIC1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ERGIC1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ERGIC1 / ERGIC32, KIAA1181 |
| 蛋白名称 | Endoplasmic reticulum-Golgi intermediate compartment protein 1 |
| 蛋白大小 | 290 aa / 32.6 kDa |
| UniProt ID | Q969X5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Vesicles; UniProt: Endoplasmic reticulum membrane; Endoplasmic reticulum-Golgi  |
| 蛋白大小 | 10/10 | ×1 | 10 | 290 aa / 32.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=89.0; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR045888, IPR012936, IPR039542; Pfam: PF07970, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.5/180** | |
| **归一化总分** | | | **76.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Vesicles | Enhanced |
| UniProt | Endoplasmic reticulum membrane; Endoplasmic reticulum-Golgi intermediate compartment membrane; Golgi... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- COPII-coated ER to Golgi transport vesicle (GO:0030134)
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum membrane (GO:0005789)
- endoplasmic reticulum-Golgi intermediate compartment (GO:0005793)
- endoplasmic reticulum-Golgi intermediate compartment membrane (GO:0033116)
- Golgi membrane (GO:0000139)
- membrane (GO:0016020)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 22 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ERGIC32, KIAA1181 |

**关键文献**:
1. High-throughput transcriptomic and RNAi analysis identifies AIM1, ERGIC1, TMED3 and TPX2 as potential drug targets in prostate cancer.. *PloS one*. PMID: 22761906
2. Bi-allelic loss of ERGIC1 causes relatively mild arthrogryposis.. *Clinical genetics*. PMID: 34037256
3. Selective Genetic Overlap Between Amyotrophic Lateral Sclerosis and Diseases of the Frontotemporal Dementia Spectrum.. *JAMA neurology*. PMID: 29630712
4. Mutations in ERGIC1 cause Arthrogryposis multiplex congenita, neuropathic type.. *Clinical genetics*. PMID: 28317099
5. Large-effect pleiotropic or closely linked QTL segregate within and across ten US cattle breeds.. *BMC genomics*. PMID: 24906442

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.0 |
| 高置信度残基 (pLDDT>90) 占比 | 63.1% |
| 置信残基 (pLDDT 70-90) 占比 | 32.1% |
| 中等置信 (pLDDT 50-70) 占比 | 4.5% |
| 低置信 (pLDDT<50) 占比 | 0.3% |
| 有序区域 (pLDDT>70) 占比 | 95.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=89.0，有序区 95.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR045888, IPR012936, IPR039542; Pfam: PF07970, PF13850 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SURF4 | 0.943 | 0.100 | — |
| GTPBP3 | 0.931 | 0.291 | — |
| LMAN1 | 0.875 | 0.126 | — |
| SURF2 | 0.714 | 0.000 | — |
| ERGIC3 | 0.669 | 0.613 | — |
| TRMU | 0.603 | 0.071 | — |
| GTSE1 | 0.603 | 0.071 | — |
| LMAN2 | 0.549 | 0.086 | — |
| ARRDC3 | 0.511 | 0.000 | — |
| SURF1 | 0.487 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| nef | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-17346|pubmed:22190034| |
| ERGIC3 | psi-mi:"MI:0030"(cross-linking study) | pubmed:15308636|imex:IM-19527 |
| ISG15 | psi-mi:"MI:0096"(pull down) | pubmed:26259872|imex:IM-26283 |
| EFNB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| INA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| RDH10 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| EHHADH | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| PRPF4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.0 + PDB: 无 | pLDDT=89.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane; Endoplasmic reticu / Nucleoplasm, Vesicles | 一致 |
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
1. ERGIC1 — Endoplasmic reticulum-Golgi intermediate compartment protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小290 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q969X5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000113719-ERGIC1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ERGIC1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q969X5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000113719-ERGIC1/subcellular

![](https://images.proteinatlas.org/18666/155_C7_1_red_green.jpg)
![](https://images.proteinatlas.org/18666/155_C7_2_red_green.jpg)
![](https://images.proteinatlas.org/18666/157_C7_1_red_green.jpg)
![](https://images.proteinatlas.org/18666/157_C7_2_red_green.jpg)
![](https://images.proteinatlas.org/18666/199_C7_3_red_green.jpg)
![](https://images.proteinatlas.org/18666/199_C7_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q969X5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q969X5 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR045888;IPR012936;IPR039542; |
| Pfam | PF07970;PF13850; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000113719-ERGIC1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ERGIC3 | Intact, Biogrid | true |
| EFNB1 | Biogrid | false |
| EHHADH | Intact | false |
| FAF2 | Biogrid | false |
| FLVCR1 | Biogrid | false |
| GOLGB1 | Biogrid | false |
| KLF11 | Intact | false |
| NUP58 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
