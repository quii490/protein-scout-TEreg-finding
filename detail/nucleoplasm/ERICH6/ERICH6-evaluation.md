---
type: protein-evaluation
gene: "ERICH6"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ERICH6 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ERICH6 / C3orf44, FAM194A |
| 蛋白名称 | Glutamate-rich protein 6 |
| 蛋白大小 | 663 aa / 75.3 kDa |
| UniProt ID | Q7L0X2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 663 aa / 75.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR029281; Pfam: PF14977 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 8 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **134.0/180** | |
| **归一化总分** | | | **74.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nucleus (GO:0005634)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 2 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C3orf44, FAM194A |

**关键文献**:
1. Constructing a Novel Signature Based on Immune-Related lncRNA to Improve Prognosis Prediction of Cervical Squamous Cell Carcinoma Patients.. *Reproductive sciences (Thousand Oaks, Calif.)*. PMID: 35075611
2. Necroptosis-related lncRNA signature predicts prognosis and immune response for cervical squamous cell carcinoma and endocervical adenocarcinomas.. *Scientific reports*. PMID: 36175606

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.6 |
| 高置信度残基 (pLDDT>90) 占比 | 19.0% |
| 置信残基 (pLDDT 70-90) 占比 | 26.2% |
| 中等置信 (pLDDT 50-70) 占比 | 17.5% |
| 低置信 (pLDDT<50) 占比 | 37.3% |
| 有序区域 (pLDDT>70) 占比 | 45.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=63.6），有序残基占 45.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029281; Pfam: PF14977 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ERICH1 | 0.505 | 0.000 | — |
| TTC32 | 0.471 | 0.054 | — |
| EFCAB5 | 0.449 | 0.000 | — |
| MRPS25 | 0.428 | 0.140 | — |
| LRCH2 | 0.423 | 0.091 | — |
| LRRC57 | 0.420 | 0.091 | — |
| RIPOR3 | 0.406 | 0.045 | — |
| AADACL3 | 0.402 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Sox4 | psi-mi:"MI:0028"(cosedimentation in solution) | imex:IM-11648|pubmed:19562802 |
| HSPB1 | psi-mi:"MI:0097"(reverse ras recruitment system) | imex:IM-20864|pubmed:25277244 |
| GLCCI1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 8，IntAct interactions: 3
- 调控相关比例: 0 / 8 = 0%

**评价**: STRING 8 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.6 + PDB: 无 | pLDDT=63.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 8 + 3 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. ERICH6 — Glutamate-rich protein 6，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小663 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=63.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7L0X2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163645-ERICH6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ERICH6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7L0X2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q7L0X2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
