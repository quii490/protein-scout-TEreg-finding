---
type: protein-evaluation
gene: "EPB41"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EPB41 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EPB41 / E41P |
| 蛋白名称 | Protein 4.1 |
| 蛋白大小 | 864 aa / 97.0 kDa |
| UniProt ID | P11171 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane, Cell Junctions; 额外: Nuclear bodies, Cytokin; UniProt: Cytoplasm, cytoskeleton; Cytoplasm, cell cortex; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 864 aa / 97.0 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=56 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.0; PDB: 1GG3, 2RQ1, 3QIJ |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR008379, IPR019749, IPR021187, IPR000798, IPR014 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **109.5/180** | |
| **归一化总分** | | | **60.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cell Junctions; 额外: Nuclear bodies, Cytokinetic bridge, Mitotic spindle, Cytosol | Approved |
| UniProt | Cytoplasm, cytoskeleton; Cytoplasm, cell cortex; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- basolateral plasma membrane (GO:0016323)
- cell cortex (GO:0005938)
- cell junction (GO:0030054)
- cortical cytoskeleton (GO:0030863)
- cytoskeleton (GO:0005856)
- cytosol (GO:0005829)
- intercellular bridge (GO:0045171)
- mitotic spindle (GO:0072686)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 56 |
| PubMed broad count | 100 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: E41P |

**关键文献**:
1. Are EPB41 and alpha-synuclein diagnostic biomarkers of sport-related concussion? Findings from the NCAA and Department of Defense CARE Consortium.. *Journal of sport and health science*. PMID: 36403906
2. Cytoskeletal Protein 4.1R in Health and Diseases.. *Biomolecules*. PMID: 38397451
3. Cloning and characterization of 4.1G (EPB41L2), a new member of the skeletal protein 4.1 (EPB41) gene family.. *Genomics*. PMID: 9598318
4. GADD45A and EPB41 as tumor suppressor genes in meningioma pathogenesis.. *Cancer genetics and cytogenetics*. PMID: 16157202
5. EPB41 suppresses the Wnt/β-catenin signaling in non-small cell lung cancer by sponging ALDOC.. *Cancer letters*. PMID: 33242559

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.0 |
| 高置信度残基 (pLDDT>90) 占比 | 30.3% |
| 置信残基 (pLDDT 70-90) 占比 | 12.7% |
| 中等置信 (pLDDT 50-70) 占比 | 12.3% |
| 低置信 (pLDDT<50) 占比 | 44.7% |
| 有序区域 (pLDDT>70) 占比 | 43.0% |
| 可用 PDB 条目 | 1GG3, 2RQ1, 3QIJ |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=63.0），有序残基占 43.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008379, IPR019749, IPR021187, IPR000798, IPR014847; Pfam: PF05902, PF08736, PF09380 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GYPC | 0.997 | 0.377 | — |
| ANK1 | 0.997 | 0.000 | — |
| ANK2 | 0.996 | 0.000 | — |
| ANK3 | 0.996 | 0.000 | — |
| ADD1 | 0.994 | 0.000 | — |
| ADD3 | 0.993 | 0.000 | — |
| ADD2 | 0.993 | 0.000 | — |
| DMTN | 0.991 | 0.000 | — |
| SPTB | 0.984 | 0.294 | — |
| EZR | 0.940 | 0.120 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SNU13 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| HSPE1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| VAMP3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| TMEM33 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| TIMM13 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| COX5B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MTPN | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| RAB11B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| HADHA | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| RAB2A | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.0 + PDB: 1GG3, 2RQ1, 3QIJ | pLDDT=63.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton; Cytoplasm, cell cortex; N / Plasma membrane, Cell Junctions; 额外: Nuclear bodie | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. EPB41 — Protein 4.1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小864 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 56 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=63.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P11171
- Protein Atlas: https://www.proteinatlas.org/ENSG00000159023-EPB41/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EPB41
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P11171
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
