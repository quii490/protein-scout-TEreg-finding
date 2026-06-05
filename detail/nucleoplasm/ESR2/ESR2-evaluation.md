---
type: protein-evaluation
gene: "ESR2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ESR2 — REJECTED (研究热度过高 (PubMed strict=930，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ESR2 / ESTRB, NR3A2 |
| 蛋白名称 | Estrogen receptor beta |
| 蛋白大小 | 530 aa / 59.2 kDa |
| UniProt ID | Q92731 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Vesicles; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 530 aa / 59.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=930 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=69.3; PDB: 1L2J, 1NDE, 1QKM, 1U3Q, 1U3R, 1U3S, 1U9E |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR021064, IPR028355, IPR024178, IPR035500, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- mitochondrion (GO:0005739)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 930 |
| PubMed broad count | 1593 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ESTRB, NR3A2 |

**关键文献**:
1. Estrogens in Male Physiology.. *Physiological reviews*. PMID: 28539434
2. Calponin 2 regulates ketogenesis to mitigate acute kidney injury.. *JCI insight*. PMID: 37751293
3. Estradiol alleviated chemotherapy-induced premature ovarian failure by blocking the ferroptosis via activating ESR2/Sirt1/Nrf2 pathway.. *Biochemical pharmacology*. PMID: 41173058
4. Estrogen receptor beta (ESR2) gene polymorphism and susceptibility to dementia.. *Acta neurologica Belgica*. PMID: 32335869
5. Integrative genomic and bioinformatic prioritization of drug repurposing candidates for prostate cancer.. *BMC pharmacology & toxicology*. PMID: 40764606

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.3 |
| 高置信度残基 (pLDDT>90) 占比 | 45.3% |
| 置信残基 (pLDDT 70-90) 占比 | 10.6% |
| 中等置信 (pLDDT 50-70) 占比 | 3.8% |
| 低置信 (pLDDT<50) 占比 | 40.4% |
| 有序区域 (pLDDT>70) 占比 | 55.9% |
| 可用 PDB 条目 | 1L2J, 1NDE, 1QKM, 1U3Q, 1U3R, 1U3S, 1U9E, 1X76, 1X78, 1X7B |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=69.3），有序残基占 55.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR021064, IPR028355, IPR024178, IPR035500, IPR000536; Pfam: PF12497, PF00104, PF00105 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NCOA1 | 0.999 | 0.984 | — |
| ESR1 | 0.998 | 0.830 | — |
| NCOA3 | 0.997 | 0.850 | — |
| SRC | 0.995 | 0.629 | — |
| NCOA2 | 0.993 | 0.779 | — |
| SP1 | 0.988 | 0.523 | — |
| MED1 | 0.988 | 0.691 | — |
| CAV1 | 0.971 | 0.049 | — |
| NCOR1 | 0.970 | 0.119 | — |
| JUN | 0.967 | 0.057 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000343925.4 | psi-mi:"MI:0029"(cosedimentation through density g | imex:IM-13781|pubmed:21182203 |
| PRMT2 | psi-mi:"MI:0096"(pull down) | pubmed:12039952 |
| ATHB-9 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17376809|imex:IM-19756 |
| BIM1 | psi-mi:"MI:0018"(two hybrid) | pubmed:18830673|imex:IM-19179 |
| Foxl2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12116|pubmed:20005806 |
| PPP5C | psi-mi:"MI:0018"(two hybrid) | pubmed:14764652|imex:IM-19817 |
| ESR1 | psi-mi:"MI:0096"(pull down) | imex:IM-13781|pubmed:21182203 |
| ZC3H18 | psi-mi:"MI:0029"(cosedimentation through density g | imex:IM-13781|pubmed:21182203 |
| RFC2 | psi-mi:"MI:0029"(cosedimentation through density g | imex:IM-13781|pubmed:21182203 |
| RPL36AL | psi-mi:"MI:0029"(cosedimentation through density g | imex:IM-13781|pubmed:21182203 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=69.3 + PDB: 1L2J, 1NDE, 1QKM, 1U3Q, 1U3R,  | pLDDT=69.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Vesicles | 一致 |
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
1. ESR2 — Estrogen receptor beta，研究基础较多，新颖性有限。
2. 蛋白大小530 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 930 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=69.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 930 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q92731
- Protein Atlas: https://www.proteinatlas.org/ENSG00000140009-ESR2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ESR2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q92731
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000140009-ESR2/subcellular

![](https://images.proteinatlas.org/68406/1984_B8_19_cr5e5cf7eb9d768_red_green.jpg)
![](https://images.proteinatlas.org/68406/1984_B8_27_cr5e5cf7eb9f573_red_green.jpg)
![](https://images.proteinatlas.org/68406/2013_E10_1_red_green.jpg)
![](https://images.proteinatlas.org/68406/2013_E10_2_red_green.jpg)
![](https://images.proteinatlas.org/68406/2048_A2_1_red_green.jpg)
![](https://images.proteinatlas.org/68406/2048_A2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q92731-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
