---
type: protein-evaluation
gene: "GPR3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GPR3 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=108，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPR3 / ACCA |
| 蛋白名称 | G-protein coupled receptor 3 |
| 蛋白大小 | 330 aa / 35.0 kDa |
| UniProt ID | P46089 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cell membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 330 aa / 35.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=108 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=81.8; PDB: 8U8F, 8WW2, 8X2K, 9LYB, 9LYC, 9LYD |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000276, IPR017452, IPR000984, IPR000723; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 14 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **76.0/180** | |
| **归一化总分** | | | **42.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cell membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- plasma membrane (GO:0005886)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 108 |
| PubMed broad count | 130 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ACCA |

**关键文献**:
1. Lipolysis drives expression of the constitutively active receptor GPR3 to induce adipose thermogenesis.. *Cell*. PMID: 34048700
2. Activation of GPR3-β-arrestin2-PKM2 pathway in Kupffer cells stimulates glycolysis and inhibits obesity and liver pathogenesis.. *Nature communications*. PMID: 38280848
3. GPR3, GPR6, and GPR12 as novel molecular targets: their biological functions and interaction with cannabidiol.. *Acta pharmacologica Sinica*. PMID: 29941868
4. GPR3 and GPR6, novel molecular targets for cannabidiol.. *Biochemical and biophysical research communications*. PMID: 28571738
5. Structural basis of oligomerization-modulated activation and autoinhibition of orphan receptor GPR3.. *Cell reports*. PMID: 40158220

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.8 |
| 高置信度残基 (pLDDT>90) 占比 | 57.0% |
| 置信残基 (pLDDT 70-90) 占比 | 20.9% |
| 中等置信 (pLDDT 50-70) 占比 | 8.5% |
| 低置信 (pLDDT<50) 占比 | 13.6% |
| 有序区域 (pLDDT>70) 占比 | 77.9% |
| 可用 PDB 条目 | 8U8F, 8WW2, 8X2K, 9LYB, 9LYC, 9LYD |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（8U8F, 8WW2, 8X2K, 9LYB, 9LYC, 9LYD）+ AlphaFold极高置信度预测（pLDDT=81.8），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000276, IPR017452, IPR000984, IPR000723; Pfam: PF00001 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ARRB2 | 0.931 | 0.407 | — |
| ARRB1 | 0.765 | 0.407 | — |
| GPR18 | 0.716 | 0.000 | — |
| GPR55 | 0.669 | 0.000 | — |
| PDE3A | 0.595 | 0.046 | — |
| APH1A | 0.571 | 0.000 | — |
| GPR4 | 0.555 | 0.000 | — |
| DMWD | 0.534 | 0.531 | — |
| GPR1 | 0.512 | 0.000 | — |
| GPR31 | 0.496 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GNPAT | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| RXYLT1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| ZNF593 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| APOD | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DMWD | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Arrb1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:24069330|imex:IM-21839 |
| APP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:24069330|imex:IM-21839 |
| Arrb2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:24069330|imex:IM-21839 |
| TNFRSF10B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ACTB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 14
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 14 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.8 + PDB: 8U8F, 8WW2, 8X2K, 9LYB, 9LYC,  | pLDDT=81.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 14 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. GPR3 — G-protein coupled receptor 3，研究基础较多，新颖性有限。
2. 蛋白大小330 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 108 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P46089
- Protein Atlas: https://www.proteinatlas.org/ENSG00000181773-GPR3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPR3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P46089
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P46089-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
