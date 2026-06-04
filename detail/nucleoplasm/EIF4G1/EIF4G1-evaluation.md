---
type: protein-evaluation
gene: "EIF4G1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EIF4G1 — REJECTED (研究热度过高 (PubMed strict=227，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EIF4G1 / EIF4F, EIF4G, EIF4GI |
| 蛋白名称 | Eukaryotic translation initiation factor 4 gamma 1 |
| 蛋白大小 | 1599 aa / 175.5 kDa |
| UniProt ID | Q04637 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Cytoplasm; Nucleus; Cytoplasm, Stress granule |
| 蛋白大小 | 5/10 | ×1 | 5 | 1599 aa / 175.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=227 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=55.0; PDB: 1LJ2, 1UG3, 2W97, 4AZA, 4F02, 5EHC, 5EI3 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR016024, IPR003891, IPR003890, IPR003307; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **76.5/180** | |
| **归一化总分** | | | **42.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus; Cytoplasm, Stress granule | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytoplasmic stress granule (GO:0010494)
- cytosol (GO:0005829)
- eukaryotic translation initiation factor 4F complex (GO:0016281)
- membrane (GO:0016020)
- nucleus (GO:0005634)
- ribosome (GO:0005840)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 227 |
| PubMed broad count | 422 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: EIF4F, EIF4G, EIF4GI |

**关键文献**:
1. A unifying model for mTORC1-mediated regulation of mRNA translation.. *Nature*. PMID: 22552098
2. Reprograming immunosuppressive microenvironment by eIF4G1 targeting to eradicate pancreatic ductal adenocarcinoma.. *Cell reports. Medicine*. PMID: 39303711
3. FMRP drives mRNP targets into translationally silenced complexes.. *Molecular cell*. PMID: 40645180
4. Identification of HPCAL1 as a specific autophagy receptor involved in ferroptosis.. *Autophagy*. PMID: 35403545
5. ALDH2/eIF3E Interaction Modulates Protein Translation Critical for Cardiomyocyte Ferroptosis in Acute Myocardial Ischemia Injury.. *Circulation*. PMID: 41111418

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 55.0 |
| 高置信度残基 (pLDDT>90) 占比 | 12.3% |
| 置信残基 (pLDDT 70-90) 占比 | 24.5% |
| 中等置信 (pLDDT 50-70) 占比 | 7.8% |
| 低置信 (pLDDT<50) 占比 | 55.4% |
| 有序区域 (pLDDT>70) 占比 | 36.8% |
| 可用 PDB 条目 | 1LJ2, 1UG3, 2W97, 4AZA, 4F02, 5EHC, 5EI3, 5EIR, 5T46, 5ZK5 |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=55.0），有序残基占 36.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016024, IPR003891, IPR003890, IPR003307; Pfam: PF02847, PF02854, PF02020 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EIF4B | 0.999 | 0.761 | — |
| EIF4E | 0.999 | 0.970 | — |
| EIF4A2 | 0.999 | 0.872 | — |
| PABPC1 | 0.999 | 0.880 | — |
| EIF4A1 | 0.999 | 0.989 | — |
| EIF3B | 0.998 | 0.966 | — |
| EIF1 | 0.996 | 0.865 | — |
| EIF3E | 0.994 | 0.840 | — |
| EIF4H | 0.993 | 0.119 | — |
| EIF4A3 | 0.991 | 0.363 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| eIF4E1 | psi-mi:"MI:0096"(pull down) | pubmed:14685270|imex:IM-23094 |
| eIF4A | psi-mi:"MI:0018"(two hybrid) | pubmed:14760701 |
| Tsc1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Srp9 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| tey | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Fas2 | psi-mi:"MI:0963"(interactome parallel affinity cap | pubmed:21447707|imex:IM-17304 |
| TIF4631 | psi-mi:"MI:0111"(dihydrofolate reductase reconstru | pubmed:31454312|imex:IM-26944 |
| Ino80 | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| Ten-m | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| Lsd-2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-16527|pubmed:25294943 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 2 / 15 = 13%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 13%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=55.0 + PDB: 1LJ2, 1UG3, 2W97, 4AZA, 4F02,  | pLDDT=55.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Cytoplasm, Stress granule / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. EIF4G1 — Eukaryotic translation initiation factor 4 gamma 1，研究基础较多，新颖性有限。
2. 蛋白大小1599 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 227 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=55.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 227 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q04637
- Protein Atlas: https://www.proteinatlas.org/ENSG00000114867-EIF4G1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EIF4G1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q04637
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
