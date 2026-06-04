---
type: protein-evaluation
gene: "GAREM1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GAREM1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GAREM1 / C18orf11, FAM59A, GAREM |
| 蛋白名称 | GRB2-associated and regulator of MAPK protein 1 |
| 蛋白大小 | 876 aa / 97.2 kDa |
| UniProt ID | Q9H706 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 876 aa / 97.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=58.1; PDB: 2DKZ |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR025946, IPR052281, IPR013761; Pfam: PF12736 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.5/180** | |
| **归一化总分** | | | **64.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 16 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C18orf11, FAM59A, GAREM |

**关键文献**:
1. GAREM1 is involved in controlling body mass in mice and humans.. *Biochemical and biophysical research communications*. PMID: 36084556
2. Effect of the glycine-rich domain in GAREM2 on its unique subcellular localization upon EGF stimulation.. *Cellular & molecular biology letters*. PMID: 33931009
3. PAK5 Promotes Esophageal Squamous Cell Carcinoma Progression Revealed by Transcriptomic Profiling.. *Journal of visualized experiments : JoVE*. PMID: 41490050
4. Increased KCNQ3 expression in papillary thyroid cancer promotes proliferation and migration.. *Cancer cell international*. PMID: 41250218
5. A brain-specific Grb2-associated regulator of extracellular signal-regulated kinase (Erk)/mitogen-activated protein kinase (MAPK) (GAREM) subtype, GAREM2, contributes to neurite outgrowth of neuroblastoma cells by regulating Erk signaling.. *The Journal of biological chemistry*. PMID: 24003223

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 58.1 |
| 高置信度残基 (pLDDT>90) 占比 | 16.1% |
| 置信残基 (pLDDT 70-90) 占比 | 21.5% |
| 中等置信 (pLDDT 50-70) 占比 | 10.4% |
| 低置信 (pLDDT<50) 占比 | 52.1% |
| 有序区域 (pLDDT>70) 占比 | 37.6% |
| 可用 PDB 条目 | 2DKZ |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=58.1），有序残基占 37.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR025946, IPR052281, IPR013761; Pfam: PF12736 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GRB2 | 0.975 | 0.785 | — |
| SHC1 | 0.815 | 0.618 | — |
| ARHGEF5 | 0.693 | 0.000 | — |
| YWHAE | 0.651 | 0.203 | — |
| GAREM2 | 0.637 | 0.610 | — |
| GRAP2 | 0.635 | 0.621 | — |
| TRIM51GP | 0.593 | 0.042 | — |
| PTPN11 | 0.559 | 0.000 | — |
| ITSN2 | 0.530 | 0.405 | — |
| GDI1 | 0.506 | 0.410 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GRB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15417|pubmed:21706016 |
| CRKL | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| EFNA1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SHC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| Acadl | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| Acad9 | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| Acot9 | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| Acads | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| Echs1 | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| Auh | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=58.1 + PDB: 2DKZ | pLDDT=58.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. GAREM1 — GRB2-associated and regulator of MAPK protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小876 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=58.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H706
- Protein Atlas: https://www.proteinatlas.org/ENSG00000141441-GAREM1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GAREM1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H706
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
