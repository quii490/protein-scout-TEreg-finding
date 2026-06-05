---
type: protein-evaluation
gene: "ETV5"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ETV5 — REJECTED (研究热度过高 (PubMed strict=274，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ETV5 / ERM |
| 蛋白名称 | ETS translocation variant 5 |
| 蛋白大小 | 510 aa / 57.8 kDa |
| UniProt ID | P41161 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 510 aa / 57.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=274 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=57.1; PDB: 4UNO, 5ILV |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000418, IPR046328, IPR006715, IPR036388, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.5/180** | |
| **归一化总分** | | | **44.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)
- synapse (GO:0045202)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 274 |
| PubMed broad count | 585 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ERM |

**关键文献**:
1. Histone serotonylation regulates ependymoma tumorigenesis.. *Nature*. PMID: 39085609
2. IGFBP5 is an ROR1 ligand promoting glioblastoma invasion via ROR1/HER2-CREB signaling axis.. *Nature communications*. PMID: 36949068
3. E-twenty-six-specific sequence variant 5 (ETV5) facilitates hepatocellular carcinoma progression and metastasis through enhancing polymorphonuclear myeloid-derived suppressor cell (PMN-MDSC)-mediated immunosuppression.. *Gut*. PMID: 40015948
4. YTHDF2 Is a Therapeutic Target for HCC by Suppressing Immune Evasion and Angiogenesis Through ETV5/PD-L1/VEGFA Axis.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 38247171
5. Role of Calcium Signaling Pathway-Related Gene Regulatory Networks in Ischemic Stroke Based on Multiple WGCNA and Single-Cell Analysis.. *Oxidative medicine and cellular longevity*. PMID: 34987704

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 57.1 |
| 高置信度残基 (pLDDT>90) 占比 | 18.2% |
| 置信残基 (pLDDT 70-90) 占比 | 5.1% |
| 中等置信 (pLDDT 50-70) 占比 | 21.6% |
| 低置信 (pLDDT<50) 占比 | 55.1% |
| 有序区域 (pLDDT>70) 占比 | 23.3% |
| 可用 PDB 条目 | 4UNO, 5ILV |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=57.1），有序残基占 23.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000418, IPR046328, IPR006715, IPR036388, IPR036390; Pfam: PF00178, PF04621 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| COP1 | 0.906 | 0.864 | — |
| DET1 | 0.906 | 0.801 | — |
| DUX4 | 0.861 | 0.000 | — |
| STK40 | 0.834 | 0.832 | — |
| SLC45A3 | 0.811 | 0.000 | — |
| GDNF | 0.784 | 0.000 | — |
| TMPRSS2 | 0.727 | 0.000 | — |
| BCL6B | 0.713 | 0.045 | — |
| ZBTB16 | 0.667 | 0.045 | — |
| GNPDA2 | 0.663 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| AMH | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| CISH | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| CCR5 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| CYP3A5 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| SLC22A2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| HOXD9 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| SEZ6L2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| DHRS7 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| HDAC11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-18733|pubmed:23752268 |
| DET1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=57.1 + PDB: 4UNO, 5ILV | pLDDT=57.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. ETV5 — ETS translocation variant 5，研究基础较多，新颖性有限。
2. 蛋白大小510 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 274 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=57.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 274 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P41161
- Protein Atlas: https://www.proteinatlas.org/ENSG00000244405-ETV5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ETV5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P41161
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P41161-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
