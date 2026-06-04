---
type: protein-evaluation
gene: "FBXO30"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FBXO30 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FBXO30 / FBX30 |
| 蛋白名称 | F-box only protein 30 |
| 蛋白大小 | 745 aa / 82.3 kDa |
| UniProt ID | Q8TB52 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Microtubules; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 745 aa / 82.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=19 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.2; PDB: 2YRE |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036047, IPR001810, IPR031890, IPR013083, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **110.5/180** | |
| **归一化总分** | | | **61.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Microtubules | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 19 |
| PubMed broad count | 23 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FBX30 |

**关键文献**:
1. F-box protein FBXO30 mediates retinoic acid receptor γ ubiquitination and regulates BMP signaling in neural tube defects.. *Cell death & disease*. PMID: 31320612
2. Fbxo30 Regulates Mammopoiesis by Targeting the Bipolar Mitotic Kinesin Eg5.. *Cell reports*. PMID: 27117404
3. Integration of bulk RNA sequencing and single-cell analysis reveals a global landscape of DNA damage response in the immune environment of Alzheimer's disease.. *Frontiers in immunology*. PMID: 36895559
4. Dietary interventions and molecular mechanisms for healthy musculoskeletal aging.. *Biogerontology*. PMID: 35727468
5. CYP24A1 is associated with fetal mummification in pigs.. *Theriogenology*. PMID: 37603936

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.2 |
| 高置信度残基 (pLDDT>90) 占比 | 28.7% |
| 置信残基 (pLDDT 70-90) 占比 | 16.4% |
| 中等置信 (pLDDT 50-70) 占比 | 14.0% |
| 低置信 (pLDDT<50) 占比 | 40.9% |
| 有序区域 (pLDDT>70) 占比 | 45.1% |
| 可用 PDB 条目 | 2YRE |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=61.2），有序残基占 45.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036047, IPR001810, IPR031890, IPR013083, IPR001293; Pfam: PF15966, PF15965 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CUL1 | 0.884 | 0.617 | — |
| SKP1 | 0.881 | 0.635 | — |
| FAU | 0.806 | 0.789 | — |
| FBXO34 | 0.704 | 0.696 | — |
| SHPRH | 0.686 | 0.093 | — |
| UBE2M | 0.633 | 0.292 | — |
| EPM2A | 0.625 | 0.000 | — |
| MYO6 | 0.622 | 0.600 | — |
| TRAF1 | 0.586 | 0.000 | — |
| NEDD8 | 0.584 | 0.151 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| APC | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| Dynll1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| CUL1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| DNALI1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| PB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28611246|imex:IM-25425 |
| SETDB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| BCL7C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MYO6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FBXO34 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| C16orf70 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.2 + PDB: 2YRE | pLDDT=61.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Microtubules | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. FBXO30 — F-box only protein 30，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小745 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 19 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=61.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TB52
- Protein Atlas: https://www.proteinatlas.org/ENSG00000118496-FBXO30/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FBXO30
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TB52
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
