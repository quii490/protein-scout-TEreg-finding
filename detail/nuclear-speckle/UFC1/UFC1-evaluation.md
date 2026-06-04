---
type: protein-evaluation
gene: "UFC1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## UFC1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | UFC1 |
| 蛋白名称 | Ubiquitin-fold modifier-conjugating enzyme 1 |
| 蛋白大小 | 167 aa / 19.5 kDa |
| UniProt ID | Q9Y3C8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nuclear speckles; 额外: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 167 aa / 19.5 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=66 篇 (≤80→4) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=93.5; PDB: 2K07, 2Z6O, 2Z6P, 3EVX, 7NVJ, 7NVK, 7NW1 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR016135, IPR014806; Pfam: PF08694 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **102.0/180** | |
| **归一化总分** | | | **56.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles; 额外: Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- extracellular exosome (GO:0070062)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 66 |
| PubMed broad count | 104 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. VCP/p97 UFMylation stabilizes BECN1 and facilitates the initiation of autophagy.. *Autophagy*. PMID: 38762759
2. Ufl1 deficiency causes kidney atrophy associated with disruption of endoplasmic reticulum homeostasis.. *Journal of genetics and genomics = Yi chuan xue bao*. PMID: 34148841
3. A non-canonical scaffold-type E3 ligase complex mediates protein UFMylation.. *The EMBO journal*. PMID: 36121123
4. Structural study of UFL1-UFC1 interaction uncovers the role of UFL1 N-terminal helix in ufmylation.. *EMBO reports*. PMID: 37988244
5. Identification of altered immune cell types and molecular mechanisms in Alzheimer's disease progression by single-cell RNA sequencing.. *Frontiers in aging neuroscience*. PMID: 39610716

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.5 |
| 高置信度残基 (pLDDT>90) 占比 | 88.0% |
| 置信残基 (pLDDT 70-90) 占比 | 7.8% |
| 中等置信 (pLDDT 50-70) 占比 | 3.0% |
| 低置信 (pLDDT<50) 占比 | 1.2% |
| 有序区域 (pLDDT>70) 占比 | 95.8% |
| 可用 PDB 条目 | 2K07, 2Z6O, 2Z6P, 3EVX, 7NVJ, 7NVK, 7NW1, 7OVC, 8BZR, 8C0D |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（2K07, 2Z6O, 2Z6P, 3EVX, 7NVJ, 7NVK, 7NW1, 7OVC, 8BZR, 8C0D）+ AlphaFold极高置信度预测（pLDDT=93.5），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016135, IPR014806; Pfam: PF08694 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| UBA5 | 0.999 | 0.979 | — |
| UFM1 | 0.998 | 0.830 | — |
| ELAVL1 | 0.987 | 0.000 | — |
| UFL1 | 0.960 | 0.696 | — |
| DDRGK1 | 0.954 | 0.719 | — |
| UBE2M | 0.867 | 0.102 | — |
| UFSP2 | 0.857 | 0.000 | — |
| UFSP1 | 0.850 | 0.000 | — |
| CDK5RAP3 | 0.805 | 0.330 | — |
| NEDD8 | 0.627 | 0.219 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| VHL | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| CDK5RAP3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| UBA5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| Dmel\CG11164 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Mef2c | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| KIRREL3 | psi-mi:"MI:0018"(two hybrid) | pubmed:25902260|imex:IM-26159 |
| ANKRD11 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| NTAQ1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| DDRGK1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GEMIN4 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.5 + PDB: 2K07, 2Z6O, 2Z6P, 3EVX, 7NVJ,  | pLDDT=93.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nuclear speckles; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. UFC1 — Ubiquitin-fold modifier-conjugating enzyme 1，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小167 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 66 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y3C8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000143222-UFC1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=UFC1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y3C8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
