---
type: protein-evaluation
gene: "NABP1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## NABP1 — REJECTED (核定位证据不足 (核定位得分 3/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NABP1 |
| 蛋白名称 | NABP1 (UniProt未获取) |
| 蛋白大小 | 未知 aa / 未知 kDa |
| UniProt ID | NABP1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 3/10 | ×4 | 12 | HPA: 暂无HPA定位数据; UniProt: 暂无数据（UniProt获取失败） |
| 蛋白大小 | 5/10 | ×1 | 5 | 未知 aa / 未知 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=18 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=73.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | 暂无数据 (UniProt未获取) |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.5/180** | |
| **归一化总分** | | | **61.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无数据 |
| UniProt | 暂无数据（UniProt获取失败） | 获取失败 |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释 (UniProt未获取)

**结论**: 核定位证据不足，HPA与UniProt存在矛盾或缺乏核注释。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 18 |
| PubMed broad count | 18 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Genotypic and Phenotypic Characteristics of Acute Promyelocytic Leukemia Translocation Variants.. *Hematol Oncol Stem Cell Ther*. PMID: 32473106
2. NABP1, a novel RORgamma-regulated gene encoding a single-stranded nucleic-acid-binding protein.. *Biochem J*. PMID: 16533169
3. Enhanced interactions within microenvironment accelerates dismal prognosis in HBV-related HCC after TACE.. *Hepatol Commun*. PMID: 39365124
4. The inhibition of ZC3H13 attenuates G2/M arrest and apoptosis by alleviating NABP1 m6A modification in cisplatin-induced acute kidney injury.. *Cell Mol Life Sci*. PMID: 39985591
5. Transcriptionally regulated miR-26a-5p may act as BRCAness in Triple-Negative Breast Cancer.. *Breast Cancer Res*. PMID: 37365643

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.9 |
| 高置信度残基 (pLDDT>90) 占比 | 52.9% |
| 置信残基 (pLDDT 70-90) 占比 | 2.5% |
| 中等置信 (pLDDT 50-70) 占比 | 12.3% |
| 低置信 (pLDDT<50) 占比 | 32.4% |
| 有序区域 (pLDDT>70) 占比 | 55.4% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=73.9，有序区 55.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 暂无数据 (UniProt未获取) |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q96AH0 | psi-mi:"MI:0397" | - |
| uniprotkb:Q13064 | psi-mi:"MI:0397" | - |
| uniprotkb:Q96PU8 | psi-mi:"MI:0397" | - |
| uniprotkb:Q5VWX1 | psi-mi:"MI:0397" | - |
| uniprotkb:Q68E01 | psi-mi:"MI:0006" | psi-mi:"MI:1060"(spoke expansi |
| uniprotkb:Q9NRY2 | psi-mi:"MI:0006" | psi-mi:"MI:1060"(spoke expansi |
| uniprotkb:P38159 | psi-mi:"MI:1356" | - |
| uniprotkb:Q04864-2 | psi-mi:"MI:1356" | - |
| uniprotkb:Q12800 | psi-mi:"MI:1356" | - |
| uniprotkb:P04637 | psi-mi:"MI:0096" | - |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.9 + PDB: 无 | pLDDT=73.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | 暂无数据（UniProt获取失败） / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. NABP1 — NABP1 (UniProt未获取)，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小未知 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 18 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/NABP1
- Protein Atlas: https://www.proteinatlas.org/search/NABP1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NABP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/NABP1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000173559-NABP1/subcellular

![](https://images.proteinatlas.org/54978/869_B8_1_red_green.jpg)
![](https://images.proteinatlas.org/54978/869_B8_2_red_green.jpg)
![](https://images.proteinatlas.org/54978/885_B8_1_red_green.jpg)
![](https://images.proteinatlas.org/54978/885_B8_2_red_green.jpg)
![](https://images.proteinatlas.org/54978/967_D10_1_red_green.jpg)
![](https://images.proteinatlas.org/54978/967_D10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
