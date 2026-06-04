---
type: protein-evaluation
gene: "SDCBP2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SDCBP2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SDCBP2 / SITAC18 |
| 蛋白名称 | Syntenin-2 |
| 蛋白大小 | 292 aa / 31.6 kDa |
| UniProt ID | Q9H190 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Golgi apparatus, Cytosol; UniProt: Cytoplasm; Nucleus, nucleolus; Nucleus, nucleoplasm; Cell me |
| 蛋白大小 | 10/10 | ×1 | 10 | 292 aa / 31.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=81.2; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR051230, IPR001478, IPR036034; Pfam: PF00595 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **135.5/180** | |
| **归一化总分** | | | **75.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Golgi apparatus, Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus, nucleolus; Nucleus, nucleoplasm; Cell membrane; Nucleus speckle | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（批量模式），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- Golgi apparatus (GO:0005794)
- nuclear speck (GO:0016607)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 24 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SITAC18 |

**关键文献**:
1. SDCBP-AS1 destabilizes β-catenin by regulating ubiquitination and SUMOylation of hnRNP K to suppress gastric tumorigenicity and metastasis.. *Cancer communications (London, England)*. PMID: 36209503
2. The plasma peptides of sepsis.. *Clinical proteomics*. PMID: 32636717
3. Targeting SDCBP2 in acute myeloid leukemia.. *Cellular signalling*. PMID: 37714445
4. SDCBP2 promotes tumor progression and is a novel ferroptosis-related prognostic biomarker in lung adenocarcinoma.. *Frontiers in immunology*. PMID: 41409290
5. Mapping Small Extracellular Vesicle Secretion Potential in Healthy Human Gingiva Using Spatial Transcriptomics.. *Current issues in molecular biology*. PMID: 40699655

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.2 |
| 高置信度残基 (pLDDT>90) 占比 | 55.8% |
| 置信残基 (pLDDT 70-90) 占比 | 21.6% |
| 中等置信 (pLDDT 50-70) 占比 | 7.9% |
| 低置信 (pLDDT<50) 占比 | 14.7% |
| 有序区域 (pLDDT>70) 占比 | 77.4% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（批量模式），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=81.2，有序区 77.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051230, IPR001478, IPR036034; Pfam: PF00595 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CD63 | 0.992 | 0.000 | — |
| SDC1 | 0.923 | 0.000 | — |
| PDCD6IP | 0.798 | 0.143 | — |
| CD9 | 0.786 | 0.000 | — |
| CD81 | 0.780 | 0.000 | — |
| TSG101 | 0.777 | 0.000 | — |
| B4E171_HUMAN | 0.721 | 0.000 | — |
| CD6 | 0.720 | 0.052 | — |
| UNC93B1 | 0.718 | 0.000 | — |
| DDR1 | 0.666 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000371233.1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| ZCCHC17 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| BEND7 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| DPPA2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TIFA | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| PAFAH1B3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| PRR13 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MMTAG2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| SEC23A | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| NUF2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.2 + PDB: 无 | pLDDT=81.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus, nucleolus; Nucleus, nucleoplas / Nucleoplasm; 额外: Golgi apparatus, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. SDCBP2 — Syntenin-2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小292 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H190
- Protein Atlas: https://www.proteinatlas.org/ENSG00000125775-SDCBP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SDCBP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H190
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
