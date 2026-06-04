---
type: protein-evaluation
gene: "DCTN1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DCTN1 — REJECTED (研究热度过高 (PubMed strict=192，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DCTN1 |
| 蛋白名称 | Dynactin subunit 1 |
| 蛋白大小 | 1278 aa / 141.7 kDa |
| UniProt ID | Q14203 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Microtubules; 额外: Cytokinetic bridge, Mitotic spindle, Prima; UniProt: Cytoplasm; Cytoplasm, cytoskeleton; Cytoplasm, cytoskeleton, |
| 蛋白大小 | 5/10 | ×1 | 5 | 1278 aa / 141.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=192 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=76.6; PDB: 1TXQ, 2COY, 2HKN, 2HKQ, 2HL3, 2HL5, 2HQH |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036859, IPR000938, IPR022157; Pfam: PF01302, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **89.0/180** | |
| **归一化总分** | | | **49.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Microtubules; 额外: Cytokinetic bridge, Mitotic spindle, Primary cilium, Basal body, Acrosome, Perinuclear theca | Supported |
| UniProt | Cytoplasm; Cytoplasm, cytoskeleton; Cytoplasm, cytoskeleton, microtubule organizing center, centroso... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- acrosomal vesicle (GO:0001669)
- axon (GO:0030424)
- cell cortex (GO:0005938)
- cell cortex region (GO:0099738)
- cell leading edge (GO:0031252)
- centriolar subdistal appendage (GO:0120103)
- centriole (GO:0005814)
- centrosome (GO:0005813)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 192 |
| PubMed broad count | 375 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Monogenic Parkinson's Disease: Genotype, Phenotype, Pathophysiology, and Genetic Testing.. *Genes*. PMID: 35328025
2. Distal hereditary motor neuropathies.. *Revue neurologique*. PMID: 38702287
3. PLK2 disrupts autophagic flux to promote SNCA/α-synuclein pathology.. *Autophagy*. PMID: 39773002
4. Amyotrophic Lateral Sclerosis Overview.. **. PMID: 20301623
5. DCTN1-related neurodegeneration: Perry syndrome and beyond.. *Parkinsonism & related disorders*. PMID: 28625595

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.6 |
| 高置信度残基 (pLDDT>90) 占比 | 28.1% |
| 置信残基 (pLDDT 70-90) 占比 | 48.7% |
| 中等置信 (pLDDT 50-70) 占比 | 7.0% |
| 低置信 (pLDDT<50) 占比 | 16.2% |
| 有序区域 (pLDDT>70) 占比 | 76.8% |
| 可用 PDB 条目 | 1TXQ, 2COY, 2HKN, 2HKQ, 2HL3, 2HL5, 2HQH, 3E2U, 3TQ7, 9B7J |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1TXQ, 2COY, 2HKN, 2HKQ, 2HL3, 2HL5, 2HQH, 3E2U, 3TQ7, 9B7J）+ AlphaFold极高置信度预测（pLDDT=76.6），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036859, IPR000938, IPR022157; Pfam: PF01302, PF12455 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DCTN6 | 0.999 | 0.966 | — |
| DCTN5 | 0.999 | 0.958 | — |
| ACTR10 | 0.999 | 0.974 | — |
| DCTN2 | 0.999 | 0.999 | — |
| CLIP1 | 0.999 | 0.981 | — |
| DYNC1H1 | 0.999 | 0.998 | — |
| ACTR1A | 0.999 | 0.982 | — |
| DCTN3 | 0.999 | 0.976 | — |
| DCTN4 | 0.999 | 0.983 | — |
| BICD2 | 0.998 | 0.994 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSMUSP00000109552.4 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| ACTR1B | psi-mi:"MI:0029"(cosedimentation through density g | pubmed:12857853 |
| PGAM1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| CASP4 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| AKTIP | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MYC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| DISC1 | psi-mi:"MI:0018"(two hybrid) | pubmed:17043677|imex:IM-16650 |
| BZW1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| RFXANK | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| GSTK1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.6 + PDB: 1TXQ, 2COY, 2HKN, 2HKQ, 2HL3,  | pLDDT=76.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm, cytoskeleton; Cytoplasm, cyt / Microtubules; 额外: Cytokinetic bridge, Mitotic spin | 一致 |
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
1. DCTN1 — Dynactin subunit 1，研究基础较多，新颖性有限。
2. 蛋白大小1278 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 192 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 192 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q14203
- Protein Atlas: https://www.proteinatlas.org/ENSG00000204843-DCTN1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DCTN1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q14203
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
