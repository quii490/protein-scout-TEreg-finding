---
type: protein-evaluation
gene: "KBTBD2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KBTBD2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KBTBD2 / BKLHD1, KIAA1489 |
| 蛋白名称 | Kelch repeat and BTB domain-containing protein 2 |
| 蛋白大小 | 623 aa / 71.3 kDa |
| UniProt ID | Q8IY47 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nucleoli fibrillar center; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 623 aa / 71.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=86.2; PDB: 8GQ6, 8H33, 8H34, 8H35, 8H36, 8H37, 8H38 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011705, IPR017096, IPR000210, IPR030586, IPR047 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 11 partners; IntAct 5 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **146.0/180** | |
| **归一化总分** | | | **81.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli fibrillar center | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- Cul3-RING ubiquitin ligase complex (GO:0031463)
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 14 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BKLHD1, KIAA1489 |

**关键文献**:
1. Long non-coding RNA NEAT1 mediated RPRD1B stability facilitates fatty acid metabolism and lymph node metastasis via c-Jun/c-Fos/SREBP1 axis in gastric cancer.. *Journal of experimental & clinical cancer research : CR*. PMID: 36171622
2. Systematic druggable genome-wide mendelian randomization identifies therapeutic targets for childhood asthma.. *Medicine*. PMID: 41398767
3. Insulin resistance and diabetes caused by genetic or diet-induced KBTBD2 deficiency in mice.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 27708159
4. KBTBD2 promotes proliferation and migration of gastric cancer via activating EGFR signaling pathway.. *Pathology, research and practice*. PMID: 38237399
5. Integrative Computational Framework, Dyscovr, Links Mutated Driver Genes to Expression Dysregulation Across 19 Cancer Types.. *bioRxiv : the preprint server for biology*. PMID: 39605479

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.2 |
| 高置信度残基 (pLDDT>90) 占比 | 64.8% |
| 置信残基 (pLDDT 70-90) 占比 | 20.5% |
| 中等置信 (pLDDT 50-70) 占比 | 8.0% |
| 低置信 (pLDDT<50) 占比 | 6.6% |
| 有序区域 (pLDDT>70) 占比 | 85.3% |
| 可用 PDB 条目 | 8GQ6, 8H33, 8H34, 8H35, 8H36, 8H37, 8H38, 8H3A, 8H3F, 8H3R |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（8GQ6, 8H33, 8H34, 8H35, 8H36, 8H37, 8H38, 8H3A, 8H3F, 8H3R）+ AlphaFold极高置信度预测（pLDDT=86.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011705, IPR017096, IPR000210, IPR030586, IPR047074; Pfam: PF07707, PF00651, PF01344 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CUL3 | 0.740 | 0.647 | — |
| FMR1 | 0.537 | 0.515 | — |
| SYPL2 | 0.507 | 0.000 | — |
| COP1 | 0.465 | 0.000 | — |
| AP5B1 | 0.464 | 0.091 | — |
| SPATA33 | 0.447 | 0.000 | — |
| A1CF | 0.444 | 0.000 | — |
| LSM5 | 0.444 | 0.000 | — |
| BCAS1 | 0.430 | 0.091 | — |
| FAM53C | 0.409 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CUL3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| FMR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CAMK2D | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:29426014|imex:IM-26302| |
| ALOX15B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LMO1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 11，IntAct interactions: 5
- 调控相关比例: 0 / 11 = 0%

**评价**: STRING 11 个预测互作，IntAct 5 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.2 + PDB: 8GQ6, 8H33, 8H34, 8H35, 8H36,  | pLDDT=86.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Nucleoli fibrillar center | 一致 |
| PPI | STRING + IntAct | 11 + 5 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. KBTBD2 — Kelch repeat and BTB domain-containing protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小623 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IY47
- Protein Atlas: https://www.proteinatlas.org/ENSG00000170852-KBTBD2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KBTBD2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IY47
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000170852-KBTBD2/subcellular

![](https://images.proteinatlas.org/21133/146_E2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/21133/146_E2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/21133/147_E2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/21133/147_E2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/21133/148_E2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/21133/148_E2_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IY47-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8IY47 |
| SMART | SM00875;SM00225;SM00612; |
| UniProt Domain [FT] | DOMAIN 31..98; /note="BTB"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00037"; DOMAIN 133..229; /note="BACK"; /evidence="ECO:0000255" |
| InterPro | IPR011705;IPR017096;IPR000210;IPR030586;IPR047074;IPR015915;IPR006652;IPR011333; |
| Pfam | PF07707;PF00651;PF01344; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000170852-KBTBD2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CUL3 | Biogrid | false |
| PIK3R1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
