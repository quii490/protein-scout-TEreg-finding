---
type: protein-evaluation
gene: "EIF5B"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EIF5B — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EIF5B / IF2, KIAA0741 |
| 蛋白名称 | Eukaryotic translation initiation factor 5B |
| 蛋白大小 | 1220 aa / 138.8 kDa |
| UniProt ID | O60841 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Cytosol; 额外: Plasma membrane; UniProt: Cytoplasm |
| 蛋白大小 | 5/10 | ×1 | 5 | 1220 aa / 138.8 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=88 篇 (≤100→2) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.9; PDB: 7TQL, 8PJ3, 8PJ4, 8PJ5 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR029459, IPR027417, IPR005225, IPR000795, IPR015 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **66.5/180** | |
| **归一化总分** | | | **36.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Plasma membrane | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- synapse (GO:0045202)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 88 |
| PubMed broad count | 151 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: IF2, KIAA0741 |

**关键文献**:
1. eIF5B and eIF1A reorient initiator tRNA to allow ribosomal subunit joining.. *Nature*. PMID: 35732735
2. Hepatitis C Virus Translation Regulation.. *International journal of molecular sciences*. PMID: 32230899
3. Human eIF5 and eIF1A Compete for Binding to eIF5B.. *Biochemistry*. PMID: 30211544
4. Established and Emerging Regulatory Roles of Eukaryotic Translation Initiation Factor 5B (eIF5B).. *Frontiers in genetics*. PMID: 34512736
5. IGF2BP3-induced activation of EIF5B contributes to progression of hepatocellular carcinoma cells.. *Oncology research*. PMID: 37305324

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.9 |
| 高置信度残基 (pLDDT>90) 占比 | 19.9% |
| 置信残基 (pLDDT 70-90) 占比 | 39.8% |
| 中等置信 (pLDDT 50-70) 占比 | 3.6% |
| 低置信 (pLDDT<50) 占比 | 36.6% |
| 有序区域 (pLDDT>70) 占比 | 59.7% |
| 可用 PDB 条目 | 7TQL, 8PJ3, 8PJ4, 8PJ5 |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=65.9），有序残基占 59.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029459, IPR027417, IPR005225, IPR000795, IPR015760; Pfam: PF00009, PF14578, PF11987 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ATP5IF1 | 0.998 | 0.142 | — |
| RPS3 | 0.998 | 0.978 | — |
| RPS15 | 0.997 | 0.985 | — |
| RPS12 | 0.995 | 0.975 | — |
| RPS2 | 0.993 | 0.974 | — |
| RPS9 | 0.993 | 0.968 | — |
| RPS23 | 0.993 | 0.983 | — |
| FAU | 0.993 | 0.993 | — |
| RACK1 | 0.992 | 0.975 | — |
| EIF5 | 0.992 | 0.281 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| esn | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG3081 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| vas | psi-mi:"MI:0045"(experimental interaction detectio | pubmed:unassigned4 |
| spir | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| Golgin97 | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| HERC2 | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| Set1 | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| kst | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| Ten-m | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-16527|pubmed:25294943 |
| PpD3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-16527|pubmed:25294943 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.9 + PDB: 7TQL, 8PJ3, 8PJ4, 8PJ5 | pLDDT=65.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Cytosol; 额外: Plasma membrane | 一致 |
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
1. EIF5B — Eukaryotic translation initiation factor 5B，研究基础较多，新颖性有限。
2. 蛋白大小1220 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 88 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=65.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O60841
- Protein Atlas: https://www.proteinatlas.org/ENSG00000158417-EIF5B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EIF5B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O60841
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
