---
type: protein-evaluation
gene: "DNAJC4"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DNAJC4 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DNAJC4 / HSPF2, MCG18 |
| 蛋白名称 | DnaJ homolog subfamily C member 4 |
| 蛋白大小 | 241 aa / 27.6 kDa |
| UniProt ID | Q9NNZ3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Membrane |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 241 aa / 27.6 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=8 篇 (≤20→10) |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=77.4; PDB: 无 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR052763, IPR001623, IPR036869; Pfam: PF00226 |
| 🔗 PPI 网络 | 10/10 | ×3 | 30 | STRING 15 partners; IntAct 5 interactions |
| ➕ 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **134.5/180** | |
| **归一化总分** | | | **74.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- membrane (GO:0016020)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8 |
| PubMed broad count | 11 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HSPF2, MCG18 |

**关键文献**:
1. DNAJB8 facilitates autophagic-lysosomal degradation of viral Vif protein and restricts HIV-1 virion infectivity by rescuing APOBEC3G expression in host cells.. *FASEB journal : official publication of the Federation of American Societies for Experimental Biology*. PMID: 36723955
2. Dexamethasone acutely regulates endocrine parameters in stallions and subsequently affects gene expression in testicular germ cells.. *Animal reproduction science*. PMID: 25487569
3. Comprehensive Transcriptome Profiling of Dairy Goat Mammary Gland Identifies Genes and Networks Crucial for Lactation and Fatty Acid Metabolism.. *Frontiers in genetics*. PMID: 33101357
4. Core temperature correlates with expression of selected stress and immunomodulatory genes in febrile patients with sepsis and noninfectious SIRS.. *Cell stress & chaperones*. PMID: 19496026
5. Dense spermatozoa in stallion ejaculates contain lower concentrations of mRNAs encoding the sperm specific calcium channel 1, ornithine decarboxylase antizyme 3, aromatase, and estrogen receptor alpha than less dense spermatozoa.. *Theriogenology*. PMID: 24857629

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.4 |
| 高置信度残基 (pLDDT>90) 占比 | 41.1% |
| 置信残基 (pLDDT 70-90) 占比 | 19.9% |
| 中等置信 (pLDDT 50-70) 占比 | 32.0% |
| 低置信 (pLDDT<50) 占比 | 7.1% |
| 有序区域 (pLDDT>70) 占比 | 61.0% |
| 可用 PDB 条目 | 无 |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=77.4，有序区 61.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052763, IPR001623, IPR036869; Pfam: PF00226 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| VEGFB | 0.806 | 0.000 | — |
| HSPA9 | 0.691 | 0.488 | — |
| DNAJC11 | 0.689 | 0.051 | — |
| NUDT22 | 0.686 | 0.000 | — |
| DNAJC24 | 0.507 | 0.051 | — |
| DNAJC28 | 0.503 | 0.000 | — |
| MTX1 | 0.496 | 0.000 | — |
| CDC5L | 0.492 | 0.475 | — |
| DNAJC9 | 0.487 | 0.051 | — |
| C15orf62 | 0.481 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EGFR | psi-mi:"MI:0112"(ubiquitin reconstruction) | pubmed:20029029|imex:IM-17166 |
| HTT | psi-mi:"MI:0018"(two hybrid) | pubmed:17500595|imex:IM-21753 |
| FAM9B | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| WFS1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| PGAM2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 5
- 调控相关比例: 7 / 15 = 47%

**评价**: STRING 15 个预测互作，IntAct 5 个实验互作。调控相关配体占比 47%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.4 + PDB: 无 | pLDDT=77.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 5 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐ (REJECTED)

**核心优势**:
1. DNAJC4 — DnaJ homolog subfamily C member 4，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小241 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NNZ3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000110011-DNAJC4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DNAJC4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NNZ3
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 12:17:41
