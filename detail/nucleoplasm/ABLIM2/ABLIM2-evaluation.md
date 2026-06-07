---
type: protein-evaluation
gene: "ABLIM2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ABLIM2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ABLIM2 / KIAA1808 |
| 蛋白名称 | Actin-binding LIM protein 2 |
| 蛋白大小 | 611 aa / 67.8 kDa |
| UniProt ID | Q6H8Q1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Mitochondria; 额外: Nucleoplasm; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 611 aa / 67.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.4; PDB: 1V6G, 1WIG, 2L3X |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR032402, IPR051618, IPR003128, IPR036886, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **119.5/180** | |
| **归一化总分** | | | **66.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria; 额外: Nucleoplasm | Uncertain |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- actin cytoskeleton (GO:0015629)
- cytoplasm (GO:0005737)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 19 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1808 |

**关键文献**:
1. Alternative Splicing Mechanisms Underlying Opioid-Induced Hyperalgesia.. *Genes*. PMID: 34680965
2. Actin binding LIM protein 3 (abLIM3).. *International journal of molecular medicine*. PMID: 16328021
3. The plasma peptides of sepsis.. *Clinical proteomics*. PMID: 32636717
4. Genomic organisation and tissue specific expression of ABLIM2 gene in human, mouse and rat.. *Biochimica et biophysica acta*. PMID: 16005990
5. Identification of genetic biomarkers associated with pharmacokinetics and pharmacodynamics of apixaban in Chinese healthy volunteers.. *Expert opinion on drug metabolism & toxicology*. PMID: 36867504

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.4 |
| 高置信度残基 (pLDDT>90) 占比 | 29.1% |
| 置信残基 (pLDDT 70-90) 占比 | 21.6% |
| 中等置信 (pLDDT 50-70) 占比 | 7.2% |
| 低置信 (pLDDT<50) 占比 | 42.1% |
| 有序区域 (pLDDT>70) 占比 | 50.7% |
| 可用 PDB 条目 | 1V6G, 1WIG, 2L3X |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=65.4），有序残基占 50.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR032402, IPR051618, IPR003128, IPR036886, IPR001781; Pfam: PF16182, PF00412, PF02209 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ABRA | 0.956 | 0.292 | — |
| SRF | 0.695 | 0.000 | — |
| ASXL2 | 0.619 | 0.610 | — |
| NTN1 | 0.597 | 0.000 | — |
| KDM1B | 0.586 | 0.586 | — |
| DCC | 0.585 | 0.000 | — |
| TRIO | 0.572 | 0.000 | — |
| AFAP1 | 0.556 | 0.000 | — |
| REST | 0.542 | 0.000 | — |
| RAC1 | 0.531 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TTN | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| yqjI | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| SREBF2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| LIN7C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| C6orf142 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:26871637|imex:IM-25013| |
| SPRED1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| JPH3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| PANK2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| FGFR3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| GFAP | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.4 + PDB: 1V6G, 1WIG, 2L3X | pLDDT=65.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Mitochondria; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. ABLIM2 — Actin-binding LIM protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小611 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=65.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6H8Q1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163995-ABLIM2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ABLIM2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6H8Q1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Mitochondria (uncertain)。来源: https://www.proteinatlas.org/ENSG00000163995-ABLIM2/subcellular

![](https://images.proteinatlas.org/35808/1611_A2_1_red_green.jpg)
![](https://images.proteinatlas.org/35808/1611_A2_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6H8Q1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6H8Q1 |
| SMART | SM00132;SM00153; |
| UniProt Domain [FT] | DOMAIN 22..81; /note="LIM zinc-binding 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00125"; DOMAIN 81..141; /note="LIM zinc-binding 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00125"; DOMAIN 151..210; /note="LIM zinc-binding 3"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00125"; DOMAIN 210..270; /note="LIM zinc-binding 4"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00125"; DOMAIN 543..611; /note="HP"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00595" |
| InterPro | IPR032402;IPR051618;IPR003128;IPR036886;IPR001781; |
| Pfam | PF16182;PF00412;PF02209; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000163995-ABLIM2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ABRA | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
