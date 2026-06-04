---
type: protein-evaluation
gene: "GINS2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GINS2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GINS2 / PSF2 |
| 蛋白名称 | DNA replication complex GINS protein PSF2 |
| 蛋白大小 | 185 aa / 21.4 kDa |
| UniProt ID | Q9Y248 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus; Chromosome |
| 蛋白大小 | 8/10 | ×1 | 8 | 185 aa / 21.4 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=76 篇 (≤80→4) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=93.1; PDB: 2E9X, 2EHO, 2Q9Q, 6XTX, 6XTY, 7PFO, 7PLO |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR021151, IPR036224, IPR007257, IPR056784; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **122.0/180** | |
| **归一化总分** | | | **67.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus; Chromosome | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- CMG complex (GO:0071162)
- GINS complex (GO:0000811)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 76 |
| PubMed broad count | 102 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PSF2 |

**关键文献**:
1. GINS2 promotes oral squamous cell carcinoma progression and immune evasion by recruiting PD-L1(+) neutrophils and modulating the PTP4A1/PKM2 axis.. *Frontiers in immunology*. PMID: 41322418
2. GINS2 Promotes Osteosarcoma Tumorigenesis via STAT3/MYC Axis.. *Journal of oncology*. PMID: 36873736
3. GINS2 promotes the progression of human HNSCC by altering RRM2 expression.. *Cancer biomarkers : section A of Disease markers*. PMID: 38517779
4. Loss of GINS2 inhibits cell proliferation and tumorigenesis in human gliomas.. *CNS neuroscience & therapeutics*. PMID: 30338650
5. GINS2 regulates the proliferation and apoptosis of colon cancer cells through PTP4A1.. *Molecular medicine reports*. PMID: 35137928

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.1 |
| 高置信度残基 (pLDDT>90) 占比 | 84.9% |
| 置信残基 (pLDDT 70-90) 占比 | 9.7% |
| 中等置信 (pLDDT 50-70) 占比 | 2.2% |
| 低置信 (pLDDT<50) 占比 | 3.2% |
| 有序区域 (pLDDT>70) 占比 | 94.6% |
| 可用 PDB 条目 | 2E9X, 2EHO, 2Q9Q, 6XTX, 6XTY, 7PFO, 7PLO, 8B9D, 8OK2, 9E2Z |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（2E9X, 2EHO, 2Q9Q, 6XTX, 6XTY, 7PFO, 7PLO, 8B9D, 8OK2, 9E2Z）+ AlphaFold极高置信度预测（pLDDT=93.1），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR021151, IPR036224, IPR007257, IPR056784; Pfam: PF25005, PF05916 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MCM5 | 0.999 | 0.994 | — |
| MCM4 | 0.999 | 0.991 | — |
| GINS4 | 0.999 | 0.997 | — |
| CDC45 | 0.999 | 0.996 | — |
| GINS3 | 0.999 | 0.997 | — |
| MCM3 | 0.999 | 0.991 | — |
| GINS1 | 0.999 | 0.999 | — |
| MCM7 | 0.999 | 0.997 | — |
| MCM2 | 0.998 | 0.991 | — |
| MCM6 | 0.998 | 0.989 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GINS4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| PSF1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| CHEK2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17525332|imex:IM-19727 |
| CSNK1G2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PLEKHG4B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| SIK1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LZIC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| H2AX | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GINS3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MCM7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.1 + PDB: 2E9X, 2EHO, 2Q9Q, 6XTX, 6XTY,  | pLDDT=93.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. GINS2 — DNA replication complex GINS protein PSF2，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小185 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 76 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y248
- Protein Atlas: https://www.proteinatlas.org/ENSG00000131153-GINS2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GINS2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y248
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
