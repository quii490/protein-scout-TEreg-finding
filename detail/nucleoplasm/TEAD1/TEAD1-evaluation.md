---
type: protein-evaluation
gene: "TEAD1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TEAD1 — REJECTED (研究热度过高 (PubMed strict=352，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TEAD1 / TCF13, TEF1 |
| 蛋白名称 | Transcriptional enhancer factor TEF-1 |
| 蛋白大小 | 426 aa / 47.9 kDa |
| UniProt ID | P28347 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 426 aa / 47.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=352 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=76.5; PDB: 2HZD, 3KYS, 4RE1, 4Z8E, 5NNX, 6HIL, 6IM5 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000818, IPR038096, IPR050937, IPR016361, IPR041 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **102.0/180** | |
| **归一化总分** | | | **56.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- TEAD-YAP complex (GO:0140552)
- transcription regulator complex (GO:0005667)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 352 |
| PubMed broad count | 691 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TCF13, TEF1 |

**关键文献**:
1. TM7SF3 controls TEAD1 splicing to prevent MASH-induced liver fibrosis.. *Cell metabolism*. PMID: 38670107
2. YAP1 inhibits the senescence of alveolar epithelial cells by targeting Prdx3 to alleviate pulmonary fibrosis.. *Experimental & molecular medicine*. PMID: 38945958
3. TAX1BP3 Is a SUMOylated Nucleocytoplasmic Shuttling Protein and Protects Against Vascular Neointimal Hyperplasia.. *Circulation*. PMID: 40955569
4. TEA domain transcription factor 1(TEAD1) induces cardiac fibroblasts cells remodeling through BRD4/Wnt4 pathway.. *Signal transduction and targeted therapy*. PMID: 38374140
5. Multi-omics analyses reveal biological and clinical insights in recurrent stage I non-small cell lung cancer.. *Nature communications*. PMID: 39929832

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.5 |
| 高置信度残基 (pLDDT>90) 占比 | 46.7% |
| 置信残基 (pLDDT 70-90) 占比 | 19.7% |
| 中等置信 (pLDDT 50-70) 占比 | 11.7% |
| 低置信 (pLDDT<50) 占比 | 21.8% |
| 有序区域 (pLDDT>70) 占比 | 66.4% |
| 可用 PDB 条目 | 2HZD, 3KYS, 4RE1, 4Z8E, 5NNX, 6HIL, 6IM5, 7CMM, 7ZJP, 8Q68 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2HZD, 3KYS, 4RE1, 4Z8E, 5NNX, 6HIL, 6IM5, 7CMM, 7ZJP, 8Q68）+ AlphaFold极高置信度预测（pLDDT=76.5），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000818, IPR038096, IPR050937, IPR016361, IPR041086; Pfam: PF01285, PF17725 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| WWTR1 | 0.999 | 0.909 | — |
| YAP1 | 0.999 | 0.995 | — |
| VGLL4 | 0.984 | 0.905 | — |
| VGLL1 | 0.978 | 0.461 | — |
| TEAD2 | 0.944 | 0.784 | — |
| TEAD4 | 0.922 | 0.835 | — |
| VGLL2 | 0.915 | 0.000 | — |
| VGLL3 | 0.910 | 0.124 | — |
| MCAT | 0.890 | 0.000 | — |
| TCF7L2 | 0.857 | 0.108 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| vg | psi-mi:"MI:0096"(pull down) | pubmed:9869635 |
| HLA-DMB | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| INSR | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| GCAT | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| Yap1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:21376238|imex:IM-15800 |
| ENO1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| Sox2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21532573|imex:IM-17312 |
| RAD51 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LMNA | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| TEAD4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.5 + PDB: 2HZD, 3KYS, 4RE1, 4Z8E, 5NNX,  | pLDDT=76.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. TEAD1 — Transcriptional enhancer factor TEF-1，研究基础较多，新颖性有限。
2. 蛋白大小426 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 352 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 352 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P28347
- Protein Atlas: https://www.proteinatlas.org/ENSG00000187079-TEAD1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TEAD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P28347
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000187079-TEAD1/subcellular

![](https://images.proteinatlas.org/57339/983_G8_5_red_green.jpg)
![](https://images.proteinatlas.org/57339/983_G8_6_red_green.jpg)
![](https://images.proteinatlas.org/57339/991_G8_1_red_green.jpg)
![](https://images.proteinatlas.org/57339/991_G8_2_red_green.jpg)
![](https://images.proteinatlas.org/57339/997_C9_1_red_green.jpg)
![](https://images.proteinatlas.org/57339/997_C9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P28347-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P28347 |
| SMART | SM00426; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR000818;IPR038096;IPR050937;IPR016361;IPR041086; |
| Pfam | PF01285;PF17725; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000187079-TEAD1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| YAP1 | Intact, Biogrid | true |
| BRAF | Intact | false |
| CIC | Biogrid | false |
| CTTN | Opencell | false |
| FOXK2 | Biogrid | false |
| LMNA | Biogrid | false |
| MAX | Biogrid | false |
| MEF2C | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
