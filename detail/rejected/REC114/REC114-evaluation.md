---
type: protein-evaluation
gene: "REC114"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## REC114 — REJECTED (核定位证据不足 (核定位得分 3/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | REC114 / C15orf60 |
| 蛋白名称 | Meiotic recombination protein REC114 |
| 蛋白大小 | 266 aa / 29.2 kDa |
| UniProt ID | Q7Z4M0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 3/10 | ×4 | 12 | HPA: 暂无HPA定位数据; UniProt: Chromosome |
| 蛋白大小 | 10/10 | ×1 | 10 | 266 aa / 29.2 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=38 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=72.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR029168; Pfam: PF15165 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 7 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **107.5/180** | |
| **归一化总分** | | | **59.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Chromosome | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromosome (GO:0005694)

**结论**: 核定位证据不足，HPA与UniProt存在矛盾或缺乏核注释。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 38 |
| PubMed broad count | 65 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C15orf60 |

**关键文献**:
1. Genetic factors as potential molecular markers of human oocyte and embryo quality.. *Journal of assisted reproduction and genetics*. PMID: 33895934
2. SCF ubiquitin E3 ligase regulates DNA double-strand breaks in early meiotic recombination.. *Nucleic acids research*. PMID: 35489071
3. Evolutionary conservation of the structure and function of meiotic Rec114-Mei4 and Mer2 complexes.. *Genes & development*. PMID: 37442581
4. Structure and DNA-bridging activity of the essential Rec114-Mei4 trimer interface.. *Genes & development*. PMID: 37442580
5. A bi-allelic REC114 loss-of-function variant causes meiotic arrest and nonobstructive azoospermia.. *Clinical genetics*. PMID: 38148155

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.4 |
| 高置信度残基 (pLDDT>90) 占比 | 38.0% |
| 置信残基 (pLDDT 70-90) 占比 | 22.9% |
| 中等置信 (pLDDT 50-70) 占比 | 11.7% |
| 低置信 (pLDDT<50) 占比 | 27.4% |
| 有序区域 (pLDDT>70) 占比 | 60.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=72.4，有序区 60.9%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029168; Pfam: PF15165 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MEI4 | 0.997 | 0.095 | — |
| ANKRD31 | 0.987 | 0.797 | — |
| CD151 | 0.983 | 0.000 | — |
| CCDC36 | 0.953 | 0.000 | — |
| TTF2 | 0.937 | 0.000 | — |
| MEI1 | 0.906 | 0.000 | — |
| SPO11 | 0.871 | 0.000 | — |
| C11orf80 | 0.824 | 0.000 | — |
| FCSK | 0.728 | 0.000 | — |
| HORMAD1 | 0.719 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| D6VZV6 | psi-mi:"MI:0018"(two hybrid) | imex:IM-26321|pubmed:14992724 |
| MEI4 | psi-mi:"MI:0416"(fluorescence microscopy) | pubmed:16783010|imex:IM-20454 |
| REC107 | psi-mi:"MI:0416"(fluorescence microscopy) | pubmed:16783010|imex:IM-20454 |
| REC102 | psi-mi:"MI:0018"(two hybrid) | imex:IM-26322|pubmed:17558514 |
| REC104 | psi-mi:"MI:0018"(two hybrid) | imex:IM-26321|pubmed:14992724 |
| SKI8 | psi-mi:"MI:0018"(two hybrid) | imex:IM-26321|pubmed:14992724 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 7
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 7 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.4 + PDB: 无 | pLDDT=72.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Chromosome / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 7 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. REC114 — Meiotic recombination protein REC114，非常新颖，仅有少数基础研究。
2. 蛋白大小266 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 38 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7Z4M0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000183324-REC114/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=REC114
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7Z4M0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q7Z4M0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
