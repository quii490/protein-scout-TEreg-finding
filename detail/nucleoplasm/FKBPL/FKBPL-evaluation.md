---
type: protein-evaluation
gene: "FKBPL"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FKBPL 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FKBPL / DIR1, NG7 |
| 蛋白名称 | FK506-binding protein-like |
| 蛋白大小 | 349 aa / 38.2 kDa |
| UniProt ID | Q9UIM3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Mitotic spindle; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 349 aa / 38.2 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=56 篇 (≤60→6) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=77.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR050754, IPR011990, IPR019734; Pfam: PF00515, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **101.5/180** | |
| **归一化总分** | | | **56.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Mitotic spindle | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- extracellular region (GO:0005576)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 56 |
| PubMed broad count | 73 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DIR1, NG7 |

**关键文献**:
1. Proteome-wide Mendelian randomization identifies therapeutic targets for ankylosing spondylitis.. *Frontiers in immunology*. PMID: 38566994
2. Hsa_circ_0001402 alleviates vascular neointimal hyperplasia through a miR-183-5p-dependent regulation of vascular smooth muscle cell proliferation, migration, and autophagy.. *Journal of advanced research*. PMID: 37499939
3. Cytosolic FKBPL and ER-resident CKAP4 co-regulates ER-phagy and protein secretion.. *Nature communications*. PMID: 39251576
4. The therapeutic and diagnostic potential of FKBPL; a novel anticancer protein.. *Drug discovery today*. PMID: 22265918
5. CRISPR/Cas9-mediated gene editing in trophoblast cells via mechanoporation for preeclampsia insight.. *Cell death & disease*. PMID: 41285723

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.1 |
| 高置信度残基 (pLDDT>90) 占比 | 52.7% |
| 置信残基 (pLDDT 70-90) 占比 | 19.5% |
| 中等置信 (pLDDT 50-70) 占比 | 2.3% |
| 低置信 (pLDDT<50) 占比 | 25.5% |
| 有序区域 (pLDDT>70) 占比 | 72.2% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=77.1，有序区 72.2%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050754, IPR011990, IPR019734; Pfam: PF00515, PF13432 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HSP90AA1 | 0.990 | 0.725 | — |
| HSP90AB1 | 0.974 | 0.308 | — |
| ANKRD49 | 0.889 | 0.842 | — |
| CDKN1A | 0.876 | 0.292 | — |
| GTSE1 | 0.817 | 0.000 | — |
| RBCK1 | 0.811 | 0.736 | — |
| ESR1 | 0.745 | 0.354 | — |
| CSNK1D | 0.635 | 0.630 | — |
| CSNK1E | 0.627 | 0.622 | — |
| FAM107A | 0.610 | 0.610 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Traf1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| UNC119 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| MATR3 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| EIPR1 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |
| EBI-9374562 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |
| ENSP00000412439.2 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |
| GTF3C5 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |
| MAP3K8 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |
| MAOA | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |
| RABGGTA | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.1 + PDB: 无 | pLDDT=77.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Mitotic spindle | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FKBPL — FK506-binding protein-like，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小349 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 56 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UIM3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000204315-FKBPL/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FKBPL
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UIM3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
