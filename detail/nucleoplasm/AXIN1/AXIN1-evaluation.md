---
type: protein-evaluation
gene: "AXIN1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## AXIN1 — REJECTED (研究热度过高 (PubMed strict=464，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | AXIN1 / AXIN |
| 蛋白名称 | Axin-1 |
| 蛋白大小 | 862 aa / 95.6 kDa |
| UniProt ID | O15169 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Vesicles, Primary cilium; 额外: Nucleoli, Primary; UniProt: Cytoplasm; Nucleus; Membrane; Cell membrane |
| 蛋白大小 | 8/10 | ×1 | 8 | 862 aa / 95.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=464 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.1; PDB: 1DK8, 1EMU, 1O9U, 3ZDI, 4B7T, 4NM0, 4NM3 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR043581, IPR014936, IPR032101, IPR001158, IPR038 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **79.5/180** | |
| **归一化总分** | | | **44.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Vesicles, Primary cilium; 额外: Nucleoli, Primary cilium tip, Primary cilium transition zone | Approved |
| UniProt | Cytoplasm; Nucleus; Membrane; Cell membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- beta-catenin destruction complex (GO:0030877)
- cell cortex (GO:0005938)
- cell periphery (GO:0071944)
- cytoplasm (GO:0005737)
- cytoplasmic vesicle (GO:0031410)
- cytosol (GO:0005829)
- lateral plasma membrane (GO:0016328)
- microtubule cytoskeleton (GO:0015630)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 464 |
| PubMed broad count | 760 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: AXIN |

**关键文献**:
1. β-Catenin signaling in hepatocellular carcinoma.. *The Journal of clinical investigation*. PMID: 35166233
2. CRKL dictates anti-PD-1 resistance by mediating tumor-associated neutrophil infiltration in hepatocellular carcinoma.. *Journal of hepatology*. PMID: 38403027
3. AXIN1 boosts antiviral response through IRF3 stabilization and induced phase separation.. *Signal transduction and targeted therapy*. PMID: 39384753
4. The scaffold protein AXIN1: gene ontology, signal network, and physiological function.. *Cell communication and signaling : CCS*. PMID: 38291457
5. Mesenchymal stem cell-derived apoptotic vesicles ameliorate impaired ovarian folliculogenesis in polycystic ovary syndrome and ovarian aging by targeting WNT signaling.. *Theranostics*. PMID: 38855175

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.1 |
| 高置信度残基 (pLDDT>90) 占比 | 24.5% |
| 置信残基 (pLDDT 70-90) 占比 | 14.0% |
| 中等置信 (pLDDT 50-70) 占比 | 11.8% |
| 低置信 (pLDDT<50) 占比 | 49.7% |
| 有序区域 (pLDDT>70) 占比 | 38.5% |
| 可用 PDB 条目 | 1DK8, 1EMU, 1O9U, 3ZDI, 4B7T, 4NM0, 4NM3, 4NM5, 4NM7, 4NU1 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=61.1），有序残基占 38.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR043581, IPR014936, IPR032101, IPR001158, IPR038207; Pfam: PF16646, PF08833, PF00778 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BTRC | 0.999 | 0.843 | — |
| GSK3A | 0.999 | 0.936 | — |
| CTNNB1 | 0.999 | 0.982 | — |
| DVL1 | 0.999 | 0.699 | — |
| AXIN2 | 0.999 | 0.503 | — |
| LRP6 | 0.999 | 0.851 | — |
| APC | 0.999 | 0.994 | — |
| CSNK1A1 | 0.999 | 0.718 | — |
| GSK3B | 0.999 | 0.996 | — |
| DVL2 | 0.999 | 0.982 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000262320.3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| CRMP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| EEF1A1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| ANP32A | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| GAK | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| UTP14A | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| SH3GL1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| Ctnnb1 | psi-mi:"MI:0065"(isothermal titration calorimetry) | imex:IM-14500|pubmed:16293619 |
| SMYD2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| CSNK1E | psi-mi:"MI:0663"(confocal microscopy) | imex:IM-15364|pubmed:21988832 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.1 + PDB: 1DK8, 1EMU, 1O9U, 3ZDI, 4B7T,  | pLDDT=61.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Membrane; Cell membrane / Nucleoplasm, Vesicles, Primary cilium; 额外: Nucleol | 一致 |
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
1. AXIN1 — Axin-1，研究基础较多，新颖性有限。
2. 蛋白大小862 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 464 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=61.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 464 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O15169
- Protein Atlas: https://www.proteinatlas.org/ENSG00000103126-AXIN1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AXIN1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O15169
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000103126-AXIN1/subcellular

![](https://images.proteinatlas.org/12987/2183_A11_39_blue_red_green.jpg)
![](https://images.proteinatlas.org/12987/2183_A11_70_blue_red_green.jpg)
![](https://images.proteinatlas.org/12987/2184_C11_18_blue_red_green.jpg)
![](https://images.proteinatlas.org/12987/2184_C11_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/12987/2206_F12_137_blue_red_green.jpg)
![](https://images.proteinatlas.org/12987/2206_F12_95_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O15169-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
