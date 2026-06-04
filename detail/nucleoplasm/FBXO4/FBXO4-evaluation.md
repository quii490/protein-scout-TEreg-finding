---
type: protein-evaluation
gene: "FBXO4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FBXO4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FBXO4 / FBX4 |
| 蛋白名称 | F-box only protein 4 |
| 蛋白大小 | 387 aa / 44.1 kDa |
| UniProt ID | Q9UKT5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 387 aa / 44.1 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=26 篇 (≤40→8) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=78.4; PDB: 3L2O, 3L82, 9JKB |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036047, IPR001810, IPR039588, IPR027417; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **119.0/180** | |
| **归一化总分** | | | **66.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- SCF ubiquitin ligase complex (GO:0019005)
- ubiquitin ligase complex (GO:0000151)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 26 |
| PubMed broad count | 49 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FBX4 |

**关键文献**:
1. Tumor suppressor mediated ubiquitylation of hnRNPK is a barrier to oncogenic translation.. *Nature communications*. PMID: 36329064
2. F-Box protein 4 inhibits progression of papillary thyroid cancer.. *Steroids*. PMID: 33285173
3. The E3 Ubiquitin Ligase Fbxo4 Functions as a Tumor Suppressor: Its Biological Importance and Therapeutic Perspectives.. *Cancers*. PMID: 35565262
4. Fbxo4-mediated degradation of Fxr1 suppresses tumorigenesis in head and neck squamous cell carcinoma.. *Nature communications*. PMID: 29142209
5. Structure of the CUL1-RBX1-SKP1-FBXO4 SCF ubiquitin ligase complex.. *Biochemical and biophysical research communications*. PMID: 39406020

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.4 |
| 高置信度残基 (pLDDT>90) 占比 | 38.2% |
| 置信残基 (pLDDT 70-90) 占比 | 32.3% |
| 中等置信 (pLDDT 50-70) 占比 | 17.3% |
| 低置信 (pLDDT<50) 占比 | 12.1% |
| 有序区域 (pLDDT>70) 占比 | 70.5% |
| 可用 PDB 条目 | 3L2O, 3L82, 9JKB |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（3L2O, 3L82, 9JKB）+ AlphaFold高质量预测（pLDDT=78.4），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036047, IPR001810, IPR039588, IPR027417; Pfam: PF12937 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SKP1 | 0.999 | 0.988 | — |
| TERF1 | 0.996 | 0.985 | — |
| CUL1 | 0.983 | 0.873 | — |
| SKP2 | 0.958 | 0.000 | — |
| CCND1 | 0.956 | 0.822 | — |
| FBXW7 | 0.949 | 0.051 | — |
| BTRC | 0.945 | 0.000 | — |
| FBXO2 | 0.942 | 0.000 | — |
| FBXW11 | 0.932 | 0.000 | — |
| FBXW8 | 0.837 | 0.299 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| vir | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| TERF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-14430|pubmed:16275645 |
| CUL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:16278047 |
| SKP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:16278047 |
| NEDD8 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ENSP00000281623.3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| Dmel\CG4911 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| HSP90AB1 | psi-mi:"MI:0729"(luminescence based mammalian inte | imex:IM-17906|pubmed:22939624| |
| AMD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DEFA1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.4 + PDB: 3L2O, 3L82, 9JKB | pLDDT=78.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoplasm | 一致 |
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
1. FBXO4 — F-box only protein 4，非常新颖，仅有少数基础研究。
2. 蛋白大小387 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 26 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UKT5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000151876-FBXO4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FBXO4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UKT5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FBXO4/IF_images/80_B8_1_blue_red_green.jpg]]
![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FBXO4/IF_images/80_B8_2_blue_red_green.jpg]]
