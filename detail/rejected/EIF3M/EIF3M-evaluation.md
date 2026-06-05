---
type: protein-evaluation
gene: "EIF3M"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EIF3M — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EIF3M / HFLB5, PCID1 |
| 蛋白名称 | Eukaryotic translation initiation factor 3 subunit M |
| 蛋白大小 | 374 aa / 42.5 kDa |
| UniProt ID | Q7L2H7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Cytosol; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 374 aa / 42.5 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=35 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=55.3; PDB: 3J8B, 3J8C, 6FEC, 6YBD, 6ZMW, 6ZON, 6ZP4 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR016024, IPR045237, IPR027528, IPR040750, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **101.5/180** | |
| **归一化总分** | | | **56.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- cytosol (GO:0005829)
- eukaryotic 43S preinitiation complex (GO:0016282)
- eukaryotic 48S preinitiation complex (GO:0033290)
- eukaryotic translation initiation factor 3 complex (GO:0005852)
- eukaryotic translation initiation factor 3 complex, eIF3m (GO:0071541)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 35 |
| PubMed broad count | 50 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HFLB5, PCID1 |

**关键文献**:
1. EIF3M as a pan-cancer biomarker: prognostic significance and immune infiltration association.. *Frontiers in molecular biosciences*. PMID: 41341921
2. Comprehensive analysis of the oncogenic potential of eukaryotic initiation factor 3M via SAAL1 interaction in lung adenocarcinoma.. *American journal of cancer research*. PMID: 39553230
3. High expression of eukaryotic initiation factor 3M predicts poor prognosis in colon adenocarcinoma patients.. *Oncology letters*. PMID: 31897202
4. Inhibition of K63 ubiquitination by G-Protein pathway suppressor 2 (GPS2) regulates mitochondria-associated translation.. *Pharmacological research*. PMID: 39094987
5. In-situ cross-linking mass spectrometry reveals compartment-specific proteasomal interactions and structural heterogeneity.. *Nature communications*. PMID: 41315310

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 55.3 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 6.4% |
| 中等置信 (pLDDT 50-70) 占比 | 71.1% |
| 低置信 (pLDDT<50) 占比 | 22.5% |
| 有序区域 (pLDDT>70) 占比 | 6.4% |
| 可用 PDB 条目 | 3J8B, 3J8C, 6FEC, 6YBD, 6ZMW, 6ZON, 6ZP4, 6ZVJ, 7A09, 7QP6 |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=55.3），有序残基占 6.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016024, IPR045237, IPR027528, IPR040750, IPR000717; Pfam: PF18005, PF01399 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EIF3C | 0.999 | 0.993 | — |
| EIF3D | 0.999 | 0.990 | — |
| EIF3I | 0.999 | 0.987 | — |
| EIF3G | 0.999 | 0.985 | — |
| EIF3E | 0.999 | 0.997 | — |
| EIF3H | 0.999 | 0.997 | — |
| EIF3F | 0.999 | 0.997 | — |
| EIF3K | 0.999 | 0.996 | — |
| EIF3A | 0.999 | 0.997 | — |
| EIF3L | 0.999 | 0.991 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ERBB3 | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| - | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| ACTB | psi-mi:"MI:0071"(molecular sieving) | pubmed:15047060 |
| EIF3F | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| Pykl1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| AstC-R1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| mub | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG7786 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| eIF3f2 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| eIF3f1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=55.3 + PDB: 3J8B, 3J8C, 6FEC, 6YBD, 6ZMW,  | pLDDT=55.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. EIF3M — Eukaryotic translation initiation factor 3 subunit M，非常新颖，仅有少数基础研究。
2. 蛋白大小374 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 35 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=55.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7L2H7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000149100-EIF3M/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EIF3M
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7L2H7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q7L2H7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
