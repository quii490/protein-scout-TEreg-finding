---
type: protein-evaluation
gene: "PLAA"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PLAA 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PLAA / PLAP |
| 蛋白名称 | Phospholipase A-2-activating protein |
| 蛋白大小 | 795 aa / 87.2 kDa |
| UniProt ID | Q9Y263 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane, Cytosol; 额外: Nucleoplasm; UniProt: Nucleus; Cytoplasm; Synapse |
| 蛋白大小 | 10/10 | ×1 | 10 | 795 aa / 87.2 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=85 篇 (≤100→2) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=84.0; PDB: 2K89, 2K8A, 2K8B, 2K8C, 3EBB |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011989, IPR016024, IPR015155, IPR038122, IPR013 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **106.0/180** | |
| **归一化总分** | | | **58.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cytosol; 额外: Nucleoplasm | Supported |
| UniProt | Nucleus; Cytoplasm; Synapse | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytoplasmic ubiquitin ligase complex (GO:0000153)
- extracellular exosome (GO:0070062)
- nucleus (GO:0005634)
- synapse (GO:0045202)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 85 |
| PubMed broad count | 363 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PLAP |

**关键文献**:
1. Linear ubiquitination at damaged lysosomes induces local NFKB activation and controls cell survival.. *Autophagy*. PMID: 39744815
2. PTP4A2 promotes lysophagy by dephosphorylation of VCP/p97 at Tyr805.. *Autophagy*. PMID: 36300783
3. Allelic heterogeneity and abnormal vesicle recycling in PLAA-related neurodevelopmental disorders.. *Frontiers in molecular neuroscience*. PMID: 38650658
4. PLAA suppresses ovarian cancer metastasis via METTL3-mediated m(6)A modification of TRPC3 mRNA.. *Oncogene*. PMID: 35869392
5. PLAA/UFD-3 regulates P-bodies through its intrinsic disordered domain.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 40560612

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.0 |
| 高置信度残基 (pLDDT>90) 占比 | 56.6% |
| 置信残基 (pLDDT 70-90) 占比 | 28.1% |
| 中等置信 (pLDDT 50-70) 占比 | 4.2% |
| 低置信 (pLDDT<50) 占比 | 11.2% |
| 有序区域 (pLDDT>70) 占比 | 84.7% |
| 可用 PDB 条目 | 2K89, 2K8A, 2K8B, 2K8C, 3EBB |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（2K89, 2K8A, 2K8B, 2K8C, 3EBB）+ AlphaFold极高置信度预测（pLDDT=84.0），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011989, IPR016024, IPR015155, IPR038122, IPR013535; Pfam: PF09070, PF08324, PF00400 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| YOD1 | 0.995 | 0.967 | — |
| UFD1 | 0.992 | 0.958 | — |
| VCP | 0.992 | 0.934 | — |
| UBC | 0.987 | 0.981 | — |
| UBXN6 | 0.974 | 0.644 | — |
| NPLOC4 | 0.972 | 0.841 | — |
| UBB | 0.967 | 0.954 | — |
| NSFL1C | 0.944 | 0.900 | — |
| RPS27A | 0.936 | 0.918 | — |
| UBA52 | 0.904 | 0.900 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Pkc98E | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG1999 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| flw | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Plap | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| P5CDh1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| EBI-6248077 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-17346|pubmed:22190034| |
| ENSP00000380460.3 | psi-mi:"MI:0096"(pull down) | imex:IM-17346|pubmed:22190034| |
| FAF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |
| Nsfl1c | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |
| FAF2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.0 + PDB: 2K89, 2K8A, 2K8B, 2K8C, 3EBB | pLDDT=84.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Synapse / Plasma membrane, Cytosol; 额外: Nucleoplasm | 一致 |
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
1. PLAA — Phospholipase A-2-activating protein，研究基础较多，新颖性有限。
2. 蛋白大小795 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 85 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y263
- Protein Atlas: https://www.proteinatlas.org/ENSG00000137055-PLAA/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PLAA
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y263
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
