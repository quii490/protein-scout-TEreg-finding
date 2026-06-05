---
type: protein-evaluation
gene: "TSEN34"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TSEN34 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TSEN34 / LENG5, SEN34 |
| 蛋白名称 | tRNA-splicing endonuclease subunit Sen34 |
| 蛋白大小 | 310 aa / 33.7 kDa |
| UniProt ID | Q9BSV6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus; Nucleus, nucleolus |
| 蛋白大小 | 10/10 | ×1 | 10 | 310 aa / 33.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=83.6; PDB: 6Z9U, 7UXA, 7ZRZ, 8HMY, 8HMZ, 8ISS |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011856, IPR036167, IPR006677, IPR006676, IPR016 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 12 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **154.0/180** | |
| **归一化总分** | | | **85.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus; Nucleus, nucleolus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- tRNA-intron endonuclease complex (GO:0000214)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 9 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: LENG5, SEN34 |

**关键文献**:
1. Clinical, neuroradiological and genetic findings in pontocerebellar hypoplasia.. *Brain : a journal of neurology*. PMID: 20952379
2. A splice site mutation in the TSEN2 causes a new syndrome with craniofacial and central nervous system malformations, and atypical hemolytic uremic syndrome.. *Clinical genetics*. PMID: 34964109
3. Pontocerebellar hypoplasia type 2 and TSEN2: review of the literature and two novel mutations.. *European journal of medical genetics*. PMID: 23562994
4. Autosomal-Recessive Mutations in the tRNA Splicing Endonuclease Subunit TSEN15 Cause Pontocerebellar Hypoplasia and Progressive Microcephaly.. *American journal of human genetics*. PMID: 27392077

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.6 |
| 高置信度残基 (pLDDT>90) 占比 | 64.8% |
| 置信残基 (pLDDT 70-90) 占比 | 20.3% |
| 中等置信 (pLDDT 50-70) 占比 | 1.9% |
| 低置信 (pLDDT<50) 占比 | 12.9% |
| 有序区域 (pLDDT>70) 占比 | 85.1% |
| 可用 PDB 条目 | 6Z9U, 7UXA, 7ZRZ, 8HMY, 8HMZ, 8ISS |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（6Z9U, 7UXA, 7ZRZ, 8HMY, 8HMZ, 8ISS）+ AlphaFold极高置信度预测（pLDDT=83.6），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011856, IPR036167, IPR006677, IPR006676, IPR016690; Pfam: PF01974, PF26577 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TSEN54 | 0.999 | 0.331 | — |
| TSEN15 | 0.999 | 0.863 | — |
| TSEN2 | 0.999 | 0.840 | — |
| CLP1 | 0.969 | 0.695 | — |
| CPSF4 | 0.808 | 0.000 | — |
| CSTF2 | 0.807 | 0.060 | — |
| CPSF1 | 0.805 | 0.000 | — |
| RARS2 | 0.776 | 0.000 | — |
| SEPSECS | 0.703 | 0.000 | — |
| RTCB | 0.656 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Clp1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| TSEN15 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TSEN2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PRKCB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| Batf3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| L1TD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| POLD3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:38554706|imex:IM-30175 |
| AFG2B | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:38554706|imex:IM-30175 |
| AFG2A | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:38554706|imex:IM-30175 |
| ENST00000396388 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 12
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 12 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.6 + PDB: 6Z9U, 7UXA, 7ZRZ, 8HMY, 8HMZ,  | pLDDT=83.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus, nucleolus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 12 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TSEN34 — tRNA-splicing endonuclease subunit Sen34，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小310 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BSV6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000170892-TSEN34/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TSEN34
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BSV6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000170892-TSEN34/subcellular

![](https://images.proteinatlas.org/48208/837_G9_1_red_green.jpg)
![](https://images.proteinatlas.org/48208/837_G9_2_red_green.jpg)
![](https://images.proteinatlas.org/48208/850_G7_1_red_green.jpg)
![](https://images.proteinatlas.org/48208/850_G7_2_red_green.jpg)
![](https://images.proteinatlas.org/48208/858_G7_1_red_green.jpg)
![](https://images.proteinatlas.org/48208/858_G7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BSV6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
