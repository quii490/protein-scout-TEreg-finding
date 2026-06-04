---
type: protein-evaluation
gene: "CNPY3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CNPY3 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CNPY3 / CTG4A, ERDA5, PRAT4A, TNRC5 |
| 蛋白名称 | Protein canopy homolog 3 |
| 蛋白大小 | 278 aa / 30.7 kDa |
| UniProt ID | Q9BT09 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Endoplasmic reticulum, Plasma membrane; UniProt: Endoplasmic reticulum |
| 蛋白大小 | 10/10 | ×1 | 10 | 278 aa / 30.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=17 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=72.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR021852; Pfam: PF11938 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.5/180** | |
| **归一化总分** | | | **63.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Endoplasmic reticulum, Plasma membrane | Approved |
| UniProt | Endoplasmic reticulum | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- endoplasmic reticulum lumen (GO:0005788)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 17 |
| PubMed broad count | 28 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CTG4A, ERDA5, PRAT4A, TNRC5 |

**关键文献**:
1. Cnpy3(2xHA) mice reveal neuronal expression of Cnpy3 in the brain.. *Journal of neuroscience methods*. PMID: 36280087
2. Generation of CNPY3 knock out cell line in the H1 (WA01) hESC background.. *Stem cell research*. PMID: 39961165
3. Canopy FGF signaling regulator 3 affects prognosis, immune infiltration, and PI3K/AKT pathway in colon adenocarcinoma.. *World journal of gastrointestinal oncology*. PMID: 39072149
4. CNPY3 Promotes Human Breast Cancer Progression and Metastasis via Modulation of the Tumor Microenvironment.. *Current issues in molecular biology*. PMID: 41296387
5. Drosophila canopy b is a cochaperone of glycoprotein 93.. *The Journal of biological chemistry*. PMID: 28275054

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.6 |
| 高置信度残基 (pLDDT>90) 占比 | 30.2% |
| 置信残基 (pLDDT 70-90) 占比 | 30.6% |
| 中等置信 (pLDDT 50-70) 占比 | 15.1% |
| 低置信 (pLDDT<50) 占比 | 24.1% |
| 有序区域 (pLDDT>70) 占比 | 60.8% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=72.6，有序区 60.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR021852; Pfam: PF11938 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HSP90B1 | 0.955 | 0.094 | — |
| LY96 | 0.878 | 0.000 | — |
| UNC93B1 | 0.860 | 0.000 | — |
| LRRC40 | 0.818 | 0.734 | — |
| TLR4 | 0.806 | 0.000 | — |
| TLR9 | 0.748 | 0.163 | — |
| TLR8 | 0.722 | 0.168 | — |
| TLR1 | 0.700 | 0.241 | — |
| TLR7 | 0.699 | 0.000 | — |
| TLR3 | 0.688 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| tig | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| OGN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CHAD | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SLITRK4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| XPOT | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| BOD1L1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| PKDREJ | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| PLEC | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.6 + PDB: 无 | pLDDT=72.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum / Endoplasmic reticulum, Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CNPY3 — Protein canopy homolog 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小278 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 17 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BT09
- Protein Atlas: https://www.proteinatlas.org/ENSG00000137161-CNPY3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CNPY3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BT09
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
