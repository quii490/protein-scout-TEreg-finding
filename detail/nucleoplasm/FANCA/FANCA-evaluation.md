---
type: protein-evaluation
gene: "FANCA"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FANCA — REJECTED (研究热度过高 (PubMed strict=549，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FANCA / FAA, FACA, FANCH |
| 蛋白名称 | Fanconi anemia group A protein |
| 蛋白大小 | 1455 aa / 162.8 kDa |
| UniProt ID | O15360 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 5/10 | ×1 | 5 | 1455 aa / 162.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=549 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=74.9; PDB: 7KZP, 7KZQ, 7KZR, 7KZS, 7KZT, 7KZV |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR003516, IPR055387, IPR055386, IPR055277, IPR031 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **89.0/180** | |
| **归一化总分** | | | **49.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- Fanconi anaemia nuclear complex (GO:0043240)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 549 |
| PubMed broad count | 840 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FAA, FACA, FANCH |

**关键文献**:
1. Origin, functional role, and clinical impact of Fanconi anemia FANCA mutations.. *Blood*. PMID: 21273304
2. Identification of a robust DNA methylation signature for Fanconi anemia.. *American journal of human genetics*. PMID: 37865086
3. Pathogenic mutations identified by a multimodality approach in 117 Japanese Fanconi anemia patients.. *Haematologica*. PMID: 30792206
4. Fanconi Anemia.. **. PMID: 20301575
5. Molecular analysis of Fanconi anemia: the experience of the Bone Marrow Failure Study Group of the Italian Association of Pediatric Onco-Hematology.. *Haematologica*. PMID: 24584348

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.9 |
| 高置信度残基 (pLDDT>90) 占比 | 7.4% |
| 置信残基 (pLDDT 70-90) 占比 | 65.8% |
| 中等置信 (pLDDT 50-70) 占比 | 14.6% |
| 低置信 (pLDDT<50) 占比 | 12.2% |
| 有序区域 (pLDDT>70) 占比 | 73.2% |
| 可用 PDB 条目 | 7KZP, 7KZQ, 7KZR, 7KZS, 7KZT, 7KZV |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（7KZP, 7KZQ, 7KZR, 7KZS, 7KZT, 7KZV）+ AlphaFold极高置信度预测（pLDDT=74.9），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003516, IPR055387, IPR055386, IPR055277, IPR031729; Pfam: PF24783, PF03511, PF24781 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FANCF | 0.999 | 0.998 | — |
| CENPS | 0.999 | 0.994 | — |
| CENPX | 0.999 | 0.994 | — |
| FANCE | 0.999 | 0.998 | — |
| FANCC | 0.999 | 0.998 | — |
| FANCB | 0.999 | 0.998 | — |
| FANCM | 0.999 | 0.994 | — |
| FAAP24 | 0.999 | 0.994 | — |
| FAAP20 | 0.999 | 0.994 | — |
| FANCI | 0.999 | 0.800 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000373952.3 | psi-mi:"MI:0588"(three hybrid) | pubmed:12649160|imex:IM-19947 |
| FANCF | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:11063725 |
| FANCG | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:11063725 |
| GRB2 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| SRC | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| FYN | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| CRK | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| NCK1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| PIK3R1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| PLCG1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.9 + PDB: 7KZP, 7KZQ, 7KZR, 7KZS, 7KZT,  | pLDDT=74.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. FANCA — Fanconi anemia group A protein，研究基础较多，新颖性有限。
2. 蛋白大小1455 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 549 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 549 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O15360
- Protein Atlas: https://www.proteinatlas.org/ENSG00000187741-FANCA/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FANCA
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O15360
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
