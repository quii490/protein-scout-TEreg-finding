---
type: protein-evaluation
gene: "CENPM"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CENPM 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CENPM / C22orf18, ICEN39, PANE1 |
| 蛋白名称 | Centromere protein M |
| 蛋白大小 | 180 aa / 19.7 kDa |
| UniProt ID | Q9NSP4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Nucleus; Cytoplasm; Chromosome, centromere, kinetochore |
| 蛋白大小 | 8/10 | ×1 | 8 | 180 aa / 19.7 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=59 篇 (≤60→6) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=89.2; PDB: 4P0T, 4WAU, 7PKN, 7QOO, 7R5S, 7R5V, 7XHN |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR020987, IPR027417; Pfam: PF11111 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **124.0/180** | |
| **归一化总分** | | | **68.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus; Cytoplasm; Chromosome, centromere, kinetochore | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- inner kinetochore (GO:0000939)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 59 |
| PubMed broad count | 71 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C22orf18, ICEN39, PANE1 |

**关键文献**:
1. TSC/mTORC1 mediates mTORC2/AKT1 signaling in c-MYC-induced murine hepatocarcinogenesis via centromere protein M.. *The Journal of clinical investigation*. PMID: 39325536
2. The prognostic value and mechanisms of centromere protein M in patients with lung adenocarcinoma.. *Translational cancer research*. PMID: 36388055
3. Upregulation of centromere protein M promotes tumorigenesis: A potential predictive target for cancer in humans.. *Molecular medicine reports*. PMID: 33000180
4. E2F1-driven CENPM expression promotes glycolytic reprogramming and tumorigenicity in glioblastoma.. *Cell biology and toxicology*. PMID: 39707034
5. Single-cell RNA sequencing reveals the communications between tumor microenvironment components and tumor metastasis in osteosarcoma.. *Frontiers in immunology*. PMID: 39324133

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.2 |
| 高置信度残基 (pLDDT>90) 占比 | 70.0% |
| 置信残基 (pLDDT 70-90) 占比 | 22.8% |
| 中等置信 (pLDDT 50-70) 占比 | 3.3% |
| 低置信 (pLDDT<50) 占比 | 3.9% |
| 有序区域 (pLDDT>70) 占比 | 92.8% |
| 可用 PDB 条目 | 4P0T, 4WAU, 7PKN, 7QOO, 7R5S, 7R5V, 7XHN, 7XHO, 7YWX, 7YYH |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（4P0T, 4WAU, 7PKN, 7QOO, 7R5S, 7R5V, 7XHN, 7XHO, 7YWX, 7YYH）+ AlphaFold极高置信度预测（pLDDT=89.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR020987, IPR027417; Pfam: PF11111 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CENPU | 0.999 | 0.943 | — |
| CENPA | 0.999 | 0.897 | — |
| CENPO | 0.999 | 0.939 | — |
| CENPK | 0.999 | 0.968 | — |
| CENPT | 0.999 | 0.852 | — |
| CENPQ | 0.999 | 0.944 | — |
| CENPH | 0.999 | 0.953 | — |
| CENPN | 0.999 | 0.953 | — |
| CENPC | 0.999 | 0.926 | — |
| CENPL | 0.999 | 0.953 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CENPH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12152|pubmed:19070575 |
| DOK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| OXLD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PCP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Cenpi | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| CENPO | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| CENPQ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| CENPU | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| MKI67 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26949251|imex:IM-26415 |
| DNM1L | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.2 + PDB: 4P0T, 4WAU, 7PKN, 7QOO, 7R5S,  | pLDDT=89.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Chromosome, centromere, kineto / 暂无HPA定位数据 | 一致 |
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
1. CENPM — Centromere protein M，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小180 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 59 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NSP4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100162-CENPM/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CENPM
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NSP4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CENPM/CENPM-PAE.png]]
