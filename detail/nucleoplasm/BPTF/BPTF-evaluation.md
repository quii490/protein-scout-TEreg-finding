---
type: protein-evaluation
gene: "BPTF"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## BPTF — REJECTED (研究热度过高 (PubMed strict=153，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BPTF / FAC1, FALZ |
| 蛋白名称 | Nucleosome-remodeling factor subunit BPTF |
| 蛋白大小 | 3046 aa / 338.3 kDa |
| UniProt ID | Q12830 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 0/10 | ×1 | 0 | 3046 aa / 338.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=153 篇 (>100→REJECTED) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 2F6J, 2F6N, 2FSA, 2FUI, 2FUU, 2RI7, 3QZS |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR038028, IPR001487, IPR036427, IPR018359, IPR018 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **65.0/180** | |
| **归一化总分** | | | **36.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- ATPase complex (GO:1904949)
- cell body (GO:0044297)
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- dendrite (GO:0030425)
- extracellular exosome (GO:0070062)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 153 |
| PubMed broad count | 226 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FAC1, FALZ |

**关键文献**:
1. Epigenetic regulation of melanogenesis.. *Ageing research reviews*. PMID: 33984527
2. Phenotypic expansion of the BPTF-related neurodevelopmental disorder with dysmorphic facies and distal limb anomalies.. *American journal of medical genetics. Part A*. PMID: 33522091
3. BPTF regulates androgen receptor activity by enhancing chromatin accessibility and stabilizing the AR-FOXA1 interaction.. *Nature communications*. PMID: 41381516
4. SAR by (Protein-Observed) (19)F NMR.. *Accounts of chemical research*. PMID: 31718149
5. Pathogenic variants in SMARCA1 cause an X-linked neurodevelopmental disorder modulated by NURF complex composition.. *Nature communications*. PMID: 41213919

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v? |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 2F6J, 2F6N, 2FSA, 2FUI, 2FUU, 2RI7, 3QZS, 3QZT, 3QZV, 3UV2 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR038028, IPR001487, IPR036427, IPR018359, IPR018501; Pfam: PF00439, PF02791, PF00628 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SMARCA5 | 0.999 | 0.827 | — |
| SMARCA1 | 0.999 | 0.867 | — |
| H3-3B | 0.998 | 0.962 | — |
| H3-4 | 0.997 | 0.930 | — |
| H3C13 | 0.997 | 0.930 | — |
| RBBP4 | 0.996 | 0.778 | — |
| H3C12 | 0.996 | 0.910 | — |
| H3-5 | 0.995 | 0.906 | — |
| H3-2 | 0.995 | 0.906 | — |
| C17orf49 | 0.990 | 0.715 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |
| - | psi-mi:"MI:0096"(pull down) | imex:IM-11882|pubmed:17884155 |
| H4C16 | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:21596426|imex:IM-15795 |
| EBI-4288838 | psi-mi:"MI:0096"(pull down) | pubmed:21596426|imex:IM-15795 |
| H3C13 | psi-mi:"MI:0096"(pull down) | pubmed:21596426|imex:IM-15795 |
| EBI-4291433 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:21596426|imex:IM-15795 |
| Tfcp2l1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20362541|imex:IM-16928 |
| DLST | psi-mi:"MI:0030"(cross-linking study) | doi:10.1016/j.cels.2017.10.010 |
| H3C1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| H2BC9 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 2F6J, 2F6N, 2FSA, 2FUI, 2FUU,  | pLDDT=0, v? | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. BPTF — Nucleosome-remodeling factor subunit BPTF，研究基础较多，新颖性有限。
2. 蛋白大小3046 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 153 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 153 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q12830
- Protein Atlas: https://www.proteinatlas.org/ENSG00000171634-BPTF/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BPTF
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q12830
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000171634-BPTF/subcellular

![](https://images.proteinatlas.org/29069/2253_E5_148_red_green.jpg)
![](https://images.proteinatlas.org/29069/2253_E5_187_red_green.jpg)
![](https://images.proteinatlas.org/29069/366_B3_1_red_green.jpg)
![](https://images.proteinatlas.org/29069/370_B3_1_red_green.jpg)
![](https://images.proteinatlas.org/29069/370_B3_2_red_green.jpg)
![](https://images.proteinatlas.org/29069/373_B3_1_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q12830 |
| SMART | SM00297;SM00571;SM00249; |
| UniProt Domain [FT] | DOMAIN 240..300; /note="DDT"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00063"; DOMAIN 2927..3031; /note="Bromo"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00035" |
| InterPro | IPR038028;IPR001487;IPR036427;IPR018359;IPR018501;IPR028941;IPR019786;IPR011011;IPR001965;IPR019787;IPR013083; |
| Pfam | PF00439;PF02791;PF00628;PF15613; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000171634-BPTF/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| RBBP4 | Biogrid, Opencell | true |
| SMARCA1 | Intact, Biogrid, Opencell | true |
| SMARCA5 | Intact, Biogrid, Opencell | true |
| BRD3 | Biogrid | false |
| C17orf49 | Biogrid | false |
| CHD4 | Biogrid | false |
| EED | Biogrid | false |
| EIF3B | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
