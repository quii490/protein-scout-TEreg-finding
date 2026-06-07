---
type: protein-evaluation
gene: "ATRX"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ATRX — REJECTED (研究热度过高 (PubMed strict=1093，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ATRX / RAD54L, XH2 |
| 蛋白名称 | Transcriptional regulator ATRX |
| 蛋白大小 | 2492 aa / 282.6 kDa |
| UniProt ID | P46100 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nuclear bodies; UniProt: Nucleus; Chromosome, telomere; Nucleus, PML body |
| 蛋白大小 | 2/10 | ×1 | 2 | 2492 aa / 282.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1093 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=51.8; PDB: 2JM1, 2LBM, 2LD1, 3QL9, 3QLA, 3QLC, 3QLN |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR025766, IPR041430, IPR058901, IPR052131, IPR014 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies | Supported |
| UniProt | Nucleus; Chromosome, telomere; Nucleus, PML body | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromosome, subtelomeric region (GO:0099115)
- chromosome, telomeric region (GO:0000781)
- condensed chromosome, centromeric region (GO:0000779)
- heterochromatin (GO:0000792)
- nuclear body (GO:0016604)
- nuclear chromosome (GO:0000228)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1093 |
| PubMed broad count | 2093 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RAD54L, XH2 |

**关键文献**:
1. Driver mutations in histone H3.3 and chromatin remodelling genes in paediatric glioblastoma.. *Nature*. PMID: 22286061
2. Glioneuronal tumor with ATRX alteration, kinase fusion and anaplastic features (GTAKA): a molecularly distinct brain tumor type with recurrent NTRK gene fusions.. *Acta neuropathologica*. PMID: 36933012
3. Anaplastic astrocytoma with piloid features, a novel molecular class of IDH wildtype glioma with recurrent MAPK pathway, CDKN2A/B and ATRX alterations.. *Acta neuropathologica*. PMID: 29564591
4. Non-functional pancreatic neuroendocrine tumours: ATRX/DAXX and alternative lengthening of telomeres (ALT) are prognostically independent from ARX/PDX1 expression and tumour size.. *Gut*. PMID: 33849943
5. ATRX, a guardian of chromatin.. *Trends in genetics : TIG*. PMID: 36894374

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 51.8 |
| 高置信度残基 (pLDDT>90) 占比 | 5.9% |
| 置信残基 (pLDDT 70-90) 占比 | 30.3% |
| 中等置信 (pLDDT 50-70) 占比 | 5.6% |
| 低置信 (pLDDT<50) 占比 | 58.2% |
| 有序区域 (pLDDT>70) 占比 | 36.2% |
| 可用 PDB 条目 | 2JM1, 2LBM, 2LD1, 3QL9, 3QLA, 3QLC, 3QLN, 4W5A, 5GRQ, 5Y18 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=51.8），有序残基占 36.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR025766, IPR041430, IPR058901, IPR052131, IPR014001; Pfam: PF17981, PF26143, PF00271 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RAD51 | 0.999 | 0.886 | — |
| DAXX | 0.999 | 0.991 | — |
| H3-3B | 0.999 | 0.984 | — |
| H3-4 | 0.995 | 0.911 | — |
| H3C12 | 0.995 | 0.924 | — |
| RAD52 | 0.993 | 0.129 | — |
| H3C13 | 0.992 | 0.911 | — |
| H3-5 | 0.991 | 0.911 | — |
| SP100 | 0.991 | 0.058 | — |
| H3-2 | 0.991 | 0.911 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NEK1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14690447 |
| DAXX | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:12953102|imex:IM-30197 |
| CCSER2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| CEP126 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| LUC7L2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| PTN | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| PTPN4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| EIF4A2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| H3-3a | psi-mi:"MI:0096"(pull down) | imex:IM-13648|pubmed:20211137 |
| EBI-2859666 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=51.8 + PDB: 2JM1, 2LBM, 2LD1, 3QL9, 3QLA,  | pLDDT=51.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome, telomere; Nucleus, PML body / Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. ATRX — Transcriptional regulator ATRX，研究基础较多，新颖性有限。
2. 蛋白大小2492 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 1093 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=51.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1093 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P46100
- Protein Atlas: https://www.proteinatlas.org/ENSG00000085224-ATRX/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ATRX
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P46100
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (supported)。来源: https://www.proteinatlas.org/ENSG00000085224-ATRX/subcellular

![](https://images.proteinatlas.org/64684/1152_C9_1_red_green.jpg)
![](https://images.proteinatlas.org/64684/1152_C9_2_red_green.jpg)
![](https://images.proteinatlas.org/64684/1156_C9_1_red_green.jpg)
![](https://images.proteinatlas.org/64684/1156_C9_2_red_green.jpg)
![](https://images.proteinatlas.org/64684/1202_G2_1_red_green.jpg)
![](https://images.proteinatlas.org/64684/1202_G2_5_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P46100-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P46100 |
| SMART | SM00487;SM00490; |
| UniProt Domain [FT] | DOMAIN 159..296; /note="ADD"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00865"; DOMAIN 1581..1768; /note="Helicase ATP-binding"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00541"; DOMAIN 2025..2205; /note="Helicase C-terminal"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00542" |
| InterPro | IPR025766;IPR041430;IPR058901;IPR052131;IPR014001;IPR001650;IPR027417;IPR038718;IPR049730;IPR000330;IPR011011;IPR013083; |
| Pfam | PF17981;PF26143;PF00271;PF00176; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000085224-ATRX/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DAXX | Intact, Biogrid | true |
| EZH2 | Intact, Biogrid | true |
| H3-3A | Intact, Biogrid | true |
| H3-3B | Intact, Biogrid | true |
| BLM | Biogrid | false |
| BMI1 | Biogrid | false |
| BRD4 | Biogrid | false |
| BRD9 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
