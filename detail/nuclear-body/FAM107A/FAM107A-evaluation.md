---
type: protein-evaluation
gene: "FAM107A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM107A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM107A / DRR1, TU3A |
| 蛋白名称 | Actin-associated protein FAM107A |
| 蛋白大小 | 144 aa / 17.5 kDa |
| UniProt ID | O95990 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-body/FAM107A/IF_images/HUVEC-TERT2_1.jpg|HUVEC/TERT2]]
![[Projects/TEreg-finding/protein-interested/detail/nuclear-body/FAM107A/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles; UniProt: Nucleus; Cytoplasm, cytoskeleton, stress fiber; Cell junctio |
| 蛋白大小 | 8/10 | ×1 | 8 | 144 aa / 17.5 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=45 篇 (≤60→6) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=75.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR009533; Pfam: PF06625 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 13 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.5/180** | |
| **归一化总分** | | | **61.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles | Supported |
| UniProt | Nucleus; Cytoplasm, cytoskeleton, stress fiber; Cell junction, focal adhesion; Cell projection, ruff... | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- actin cytoskeleton (GO:0015629)
- cytoplasm (GO:0005737)
- focal adhesion (GO:0005925)
- neuron projection (GO:0043005)
- nuclear speck (GO:0016607)
- nucleus (GO:0005634)
- ruffle membrane (GO:0032587)
- stress fiber (GO:0001725)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 45 |
| PubMed broad count | 92 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DRR1, TU3A |

**关键文献**:
1. Molecular identity of human outer radial glia during cortical development.. *Cell*. PMID: 26406371
2. Combined deletion and DNA methylation result in silencing of FAM107A gene in laryngeal tumors.. *Scientific reports*. PMID: 28710449
3. FAM107A as a tumor suppressor in esophageal squamous carcinoma inhibits growth and metastasis.. *Pathology, research and practice*. PMID: 37977035
4. Decreased FAM107A Expression in Patients with Non-small Cell Lung Cancer.. *Advances in experimental medicine and biology*. PMID: 25753555
5. FAM107A Inactivation Associated with Promoter Methylation Affects Prostate Cancer Progression through the FAK/PI3K/AKT Pathway.. *Cancers*. PMID: 36010909

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.1 |
| 高置信度残基 (pLDDT>90) 占比 | 22.9% |
| 置信残基 (pLDDT 70-90) 占比 | 44.4% |
| 中等置信 (pLDDT 50-70) 占比 | 21.5% |
| 低置信 (pLDDT<50) 占比 | 11.1% |
| 有序区域 (pLDDT>70) 占比 | 67.3% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-body/FAM107A/FAM107A-PAE.png]]

**评价**: AlphaFold 中等质量（pLDDT=75.1，有序区 67.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009533; Pfam: PF06625 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PTPRZ1 | 0.651 | 0.000 | — |
| HOPX | 0.644 | 0.000 | — |
| FKBPL | 0.610 | 0.610 | — |
| SPARCL1 | 0.465 | 0.000 | — |
| LIFR | 0.447 | 0.000 | — |
| CRYAB | 0.442 | 0.000 | — |
| GPR158 | 0.425 | 0.000 | — |
| TBR1 | 0.420 | 0.000 | — |
| ANKRD49 | 0.420 | 0.421 | — |
| GPM6A | 0.417 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| KRT15 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| BEGAIN | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| KRTAP4-12 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TRAF2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CCDC85B | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TRIM37 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| LDOC1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TADA2A | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| VIM | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| USHBP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 13，IntAct interactions: 15
- 调控相关比例: 0 / 13 = 0%

**评价**: STRING 13 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.1 + PDB: 无 | pLDDT=75.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, cytoskeleton, stress fiber; Ce / Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 13 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FAM107A — Actin-associated protein FAM107A，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小144 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 45 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O95990
- Protein Atlas: https://www.proteinatlas.org/ENSG00000168309-FAM107A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM107A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O95990
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-body/FAM107A/FAM107A-PAE.png]]




