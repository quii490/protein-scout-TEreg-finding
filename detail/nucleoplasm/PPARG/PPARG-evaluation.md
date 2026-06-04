---
type: protein-evaluation
gene: "PPARG"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PPARG — REJECTED (研究热度过高 (PubMed strict=2465，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PPARG / NR1C3 |
| 蛋白名称 | Peroxisome proliferator-activated receptor gamma |
| 蛋白大小 | 505 aa / 57.6 kDa |
| UniProt ID | P37231 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Vesicles; UniProt: Nucleus; Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 505 aa / 57.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=2465 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=76.1; PDB: 1FM6, 1FM9, 1I7I, 1K74, 1KNU, 1NYX, 1PRG |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR003074, IPR035500, IPR000536, IPR050234, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Vesicles | Enhanced |
| UniProt | Nucleus; Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- receptor complex (GO:0043235)
- RNA polymerase II transcription regulator complex (GO:0090575)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2465 |
| PubMed broad count | 4175 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NR1C3 |

**关键文献**:
1. Integrated analysis of single-cell and bulk RNA sequencing data reveals a myeloid cell-related regulon predicting neoadjuvant immunotherapy response across cancers.. *Journal of translational medicine*. PMID: 38773508
2. Identification and experimental validation of immune-related gene PPARG is involved in ulcerative colitis.. *Biochimica et biophysica acta. Molecular basis of disease*. PMID: 38880160
3. ZNF384: A Potential Therapeutic Target for Psoriasis and Alzheimer's Disease Through Inflammation and Metabolism.. *Frontiers in immunology*. PMID: 35669784
4. Identification of matrix stiffness-related molecular subtypes in HCC via integrating multi-omics analysis and machine learning algorithms.. *Journal of translational medicine*. PMID: 40598539
5. Identification of Five Hub Genes Based on Single-Cell RNA Sequencing Data and Network Pharmacology in Patients With Acute Myocardial Infarction.. *Frontiers in public health*. PMID: 35757636

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.1 |
| 高置信度残基 (pLDDT>90) 占比 | 54.7% |
| 置信残基 (pLDDT 70-90) 占比 | 14.1% |
| 中等置信 (pLDDT 50-70) 占比 | 3.8% |
| 低置信 (pLDDT<50) 占比 | 27.5% |
| 有序区域 (pLDDT>70) 占比 | 68.8% |
| 可用 PDB 条目 | 1FM6, 1FM9, 1I7I, 1K74, 1KNU, 1NYX, 1PRG, 1RDT, 1WM0, 1ZEO |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1FM6, 1FM9, 1I7I, 1K74, 1KNU, 1NYX, 1PRG, 1RDT, 1WM0, 1ZEO）+ AlphaFold极高置信度预测（pLDDT=76.1），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003074, IPR035500, IPR000536, IPR050234, IPR001723; Pfam: PF00104, PF12577, PF00105 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PPARGC1A | 0.999 | 0.992 | — |
| NCOR1 | 0.999 | 0.984 | — |
| NCOR2 | 0.999 | 0.984 | — |
| RXRA | 0.999 | 0.999 | — |
| MED1 | 0.999 | 0.986 | — |
| NCOA1 | 0.999 | 0.992 | — |
| CREBBP | 0.998 | 0.982 | — |
| NCOA2 | 0.998 | 0.965 | — |
| RELA | 0.998 | 0.834 | — |
| SIRT1 | 0.998 | 0.345 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TRAF2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| SMARCD3 | psi-mi:"MI:0096"(pull down) | imex:IM-14404|pubmed:14701856 |
| SMARCA4 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-14404|pubmed:14701856 |
| KCNIP4 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MIF4GD | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| RPL30 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| CLU | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| CHD8 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| STMN1 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| PSMD1 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.1 + PDB: 1FM6, 1FM9, 1I7I, 1K74, 1KNU,  | pLDDT=76.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Nucleus / Nucleoplasm, Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. PPARG — Peroxisome proliferator-activated receptor gamma，研究基础较多，新颖性有限。
2. 蛋白大小505 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2465 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 2465 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P37231
- Protein Atlas: https://www.proteinatlas.org/ENSG00000132170-PPARG/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PPARG
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P37231
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
