---
type: protein-evaluation
gene: "CRKL"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CRKL — REJECTED (研究热度过高 (PubMed strict=476，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CRKL |
| 蛋白名称 | Crk-like protein |
| 蛋白大小 | 303 aa / 33.8 kDa |
| UniProt ID | P46109 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 303 aa / 33.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=476 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.5; PDB: 2BZX, 2BZY, 2DBK, 2EO3, 2LQN, 2LQW |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR035458, IPR035457, IPR000980, IPR036860, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Enhanced |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extrinsic component of postsynaptic membrane (GO:0098890)
- neuromuscular junction (GO:0031594)
- nucleoplasm (GO:0005654)
- protein-containing complex (GO:0032991)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 476 |
| PubMed broad count | 714 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. CRKL dictates anti-PD-1 resistance by mediating tumor-associated neutrophil infiltration in hepatocellular carcinoma.. *Journal of hepatology*. PMID: 38403027
2. Human Genetics of Ventricular Septal Defect.. *Advances in experimental medicine and biology*. PMID: 38884729
3. Hypoxia-induced up-regulation of VASP promotes invasiveness and metastasis of hepatocellular carcinoma.. *Theranostics*. PMID: 30279729
4. Anatomic position determines oncogenic specificity in melanoma.. *Nature*. PMID: 35355015
5. Oncogenic Signaling Adaptor Proteins.. *Journal of genetics and genomics = Yi chuan xue bao*. PMID: 26554907

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.5 |
| 高置信度残基 (pLDDT>90) 占比 | 1.3% |
| 置信残基 (pLDDT 70-90) 占比 | 62.7% |
| 中等置信 (pLDDT 50-70) 占比 | 11.2% |
| 低置信 (pLDDT<50) 占比 | 24.8% |
| 有序区域 (pLDDT>70) 占比 | 64.0% |
| 可用 PDB 条目 | 2BZX, 2BZY, 2DBK, 2EO3, 2LQN, 2LQW |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=68.5），有序残基占 64.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR035458, IPR035457, IPR000980, IPR036860, IPR036028; Pfam: PF00017, PF00018, PF07653 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BCAR1 | 0.999 | 0.749 | — |
| RAPGEF1 | 0.999 | 0.930 | — |
| CBL | 0.999 | 0.993 | — |
| ABL1 | 0.998 | 0.887 | — |
| DOCK1 | 0.995 | 0.687 | — |
| EGFR | 0.993 | 0.855 | — |
| GAB1 | 0.992 | 0.833 | — |
| STAT5A | 0.987 | 0.510 | — |
| STAT5B | 0.983 | 0.000 | — |
| CRK | 0.979 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| INSR | psi-mi:"MI:0018"(two hybrid) | pubmed:15522217 |
| MAP4K1 | psi-mi:"MI:0096"(pull down) | pubmed:9788432 |
| MAP4K5 | psi-mi:"MI:0096"(pull down) | pubmed:9788432 |
| Kidins220 | psi-mi:"MI:0096"(pull down) | imex:IM-14422|pubmed:16284401| |
| BIK | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| KHDRBS1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| TNS2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| WAC | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| GAREM1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| SHANK3 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.5 + PDB: 2BZX, 2BZY, 2DBK, 2EO3, 2LQN,  | pLDDT=68.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CRKL — Crk-like protein，研究基础较多，新颖性有限。
2. 蛋白大小303 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 476 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=68.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 476 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P46109
- Protein Atlas: https://www.proteinatlas.org/ENSG00000099942-CRKL/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CRKL
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P46109
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000099942-CRKL/subcellular

![](https://images.proteinatlas.org/532/1158_G2_1_red_green.jpg)
![](https://images.proteinatlas.org/532/1158_G2_2_red_green.jpg)
![](https://images.proteinatlas.org/532/1401_G2_3_red_green.jpg)
![](https://images.proteinatlas.org/532/1401_G2_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P46109-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P46109 |
| SMART | SM00252;SM00326; |
| UniProt Domain [FT] | DOMAIN 14..102; /note="SH2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00191"; DOMAIN 123..183; /note="SH3 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00192"; DOMAIN 235..296; /note="SH3 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00192" |
| InterPro | IPR035458;IPR035457;IPR000980;IPR036860;IPR036028;IPR001452;IPR051184; |
| Pfam | PF00017;PF00018;PF07653; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000099942-CRKL/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ABL1 | Intact, Biogrid | true |
| ARHGEF5 | Intact, Biogrid | true |
| CBL | Intact, Biogrid | true |
| CBLB | Intact, Biogrid | true |
| DOK1 | Intact, Biogrid | true |
| EGFR | Intact, Biogrid | true |
| FLT1 | Intact, Biogrid | true |
| GAB1 | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
