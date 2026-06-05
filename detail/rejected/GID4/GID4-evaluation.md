---
type: protein-evaluation
gene: "GID4"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GID4 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GID4 / C17orf39, VID24 |
| 蛋白名称 | Glucose-induced degradation protein 4 homolog |
| 蛋白大小 | 300 aa / 33.5 kDa |
| UniProt ID | Q8IVV7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 300 aa / 33.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=74.4; PDB: 6CCR, 6CCT, 6CCU, 6CD8, 6CD9, 6CDC, 6CDG |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR018618; Pfam: PF09783 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **124.0/180** | |
| **归一化总分** | | | **68.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- ubiquitin ligase complex (GO:0000151)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 0 |
| 别名(未计入scoring) | 无 |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.4 |
| 高置信度残基 (pLDDT>90) 占比 | 47.3% |
| 置信残基 (pLDDT 70-90) 占比 | 10.3% |
| 中等置信 (pLDDT 50-70) 占比 | 16.0% |
| 低置信 (pLDDT<50) 占比 | 26.3% |
| 有序区域 (pLDDT>70) 占比 | 57.6% |
| 可用 PDB 条目 | 6CCR, 6CCT, 6CCU, 6CD8, 6CD9, 6CDC, 6CDG, 6WZX, 6WZZ, 7NSC |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（6CCR, 6CCT, 6CCU, 6CD8, 6CD9, 6CDC, 6CDG, 6WZX, 6WZZ, 7NSC）+ AlphaFold极高置信度预测（pLDDT=74.4），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR018618; Pfam: PF09783 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ARMC8 | 0.998 | 0.982 | — |
| GID8 | 0.996 | 0.955 | — |
| RMND5A | 0.991 | 0.859 | — |
| RANBP9 | 0.990 | 0.965 | — |
| RANBP10 | 0.990 | 0.947 | — |
| WDR26 | 0.972 | 0.720 | — |
| MKLN1 | 0.915 | 0.609 | — |
| MAEA | 0.914 | 0.609 | — |
| RMND5B | 0.853 | 0.121 | — |
| FBP1 | 0.759 | 0.508 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| BUD14 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| CFT1 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| RNA14 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| VID24 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| VID30 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| GDB1 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| BOI2 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| ATG9 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| HSP82 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| RMND5A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.4 + PDB: 6CCR, 6CCT, 6CCU, 6CD8, 6CD9,  | pLDDT=74.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GID4 — Glucose-induced degradation protein 4 homolog，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小300 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IVV7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000141034-GID4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GID4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IVV7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000141034-GID4/subcellular

![](https://images.proteinatlas.org/44348/2179_E7_54_blue_red_green.jpg)
![](https://images.proteinatlas.org/44348/2179_E7_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/44348/616_C5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/44348/616_C5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/44348/619_C5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/44348/619_C5_4_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IVV7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
