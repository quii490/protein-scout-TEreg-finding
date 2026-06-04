---
type: protein-evaluation
gene: "ADIG"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation]
status: rejected
---

## ADIG 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ADIG / Adipogenin |
| 蛋白大小 | 80 aa / ~9.5 kDa |
| UniProt ID | Q0VDE8 |
| 评估日期 | 2026-05-29 |

### 2. 评分总览

> **淘汰原因：核定位评分 ≤3。** 该蛋白为膜蛋白（Single-pass membrane protein），核定位仅基于序列相似性推断（ISS），无实验证据。HPA 无 IF 染色数据。

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 2/10 | ×4 | 8 | 膜蛋白(主定位)+核(ISS推断)，无HPA IF数据 |
| 📏 蛋白大小 | 5/10 | ×1 | 5 | 80 aa，偏小 |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed=17，极度新颖 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AF pLDDT=68.6, >70=39% 质量差 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | 无注释结构域（新颖基线） |
| 🔗 PPI 网络 | 0/10 | ×3 | 0 | 无IntAct数据，STRING仅3个弱互作 |
| ➕ 互证加分 | — | max +3 | 0 | 无多库互证 |
| **原始总分** | | | **95** | |
| **归一化总分** | | | **51.9** | 淘汰原因：核定位不足 |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Membrane + Cytoplasm/Nucleus | — |
| Protein Atlas (IF) | 暂无数据（Pending cell analysis） | — |
| UniProt | Membrane (Single-pass) + Nucleus (ECO:0000250) | Nucleus 仅 ISS 推断 |

**结论**: ADIG 是单次跨膜蛋白。UniProt 核定位注释基于序列相似性（ISS），无实验证据。膜蛋白为主要定位。核定位 = 2 → **淘汰**。

#### 3.2 蛋白大小评估
**评价**: 80 aa，属于 50–100 aa 区间，蛋白极小，功能和结构域空间有限。

#### 3.3 研究现状
| 指标 | 数值 |
|------|------|
| PubMed 总数 | 17 |
| 最早发表年份 | 2004 |
| Chromatin/epigenetics 比例 | 0% |

**主要研究方向**:
- 脂肪细胞分化（brown/white fat cell differentiation）
- 精子发生

**关键文献**:
1. Daneschnejad et al. (2004). 初始鉴定 adipogenin 参与脂肪细胞分化。PMID: 15567149

**评价**: 研究极度稀少，但与脂肪生成相关，与染色质/转录调控无关。

#### 3.4 三维结构分析
| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 68.6 |
| 有序区域 (pLDDT>70) 占比 | 39% |
| pLDDT>90 占比 | 18% |
| pLDDT<50 占比 | 9% |
| 可用 PDB 条目 | 0 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/ADIG/ADIG-PAE.png]]

**PAE 数值分析**:
- PAE 矩阵尺寸: 80×80
- PAE 总体均值: 18.5
- PAE <5 Å 占比: 14.4%
- PAE <10 Å 占比: 25.4%

**评价**: AlphaFold 结构质量差（pLDDT 68.6），仅 39% 有序区域。无 PDB 结构。80 aa 的小蛋白预测质量低属正常现象。

#### 3.5 结构域分析
| 来源 | 结构域 |
|------|--------|
| GeneCards | 无 |
| SMART | 无 |
| InterPro/Pfam | 无 |

**染色质调控潜力分析**: 无任何注释结构域。蛋白极小（80 aa），功能域空间极为有限。

#### 3.6 PPI 网络

**实验验证互作** (IntAct): 无任何物理互作记录。

**STRING 预测互作** (combined score >0.4):
| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| PPARG | 0.625 | 核受体/脂肪生成TF | 边缘 |
| CIDEC | 0.505 | 脂滴融合 | 否 |
| ADIPOQ | 0.500 | 脂肪因子 | 否 |
| RALGAPB | 0.473 | Ral GTPase激活 | 否 |

**已知复合体成员** (GO Cellular Component):
- Membrane (GO:0016020, IEA)
- Lipid droplet (GO:0005811, IBA)
- Nucleus (GO:0005634, ISS)

**PPI 互证分析**: 无物理互作数据。STRING 仅 4 个弱互作伙伴。PPI 网络极为稀疏。

**评价**: 几乎无 PPI 信息，无可用于评估染色质调控潜力的互作数据。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AF pLDDT=68.6, 无PDB | 低质量 | N/A |
| 结构域 | 无注释域（多库一致） | 无域 | 一致 |
| PPI | 无物理互作 | 网络稀疏 | N/A |
| 定位 | HPA(无数据)/UniProt(膜) | 膜蛋白 | 部分一致 |

**互证加分明细**: 无。**总分**: +0 / max +3

### 4. 总体评价

**推荐等级**: ⭐ (1/5) — 淘汰

**淘汰原因**:
1. 膜蛋白，非核蛋白。核定位仅基于序列相似性推断（ISS），无实验证据。
2. 蛋白极小（80 aa），功能域空间极为有限。
3. 无 PPI 数据，无已知核功能。

**下一步建议**:
- 不推荐作为核蛋白研究目标。若关注脂肪生成中的膜蛋白功能，可另行评估。

### 5. 
### IF图像状态

| 项目 | 内容 |
|---|---|
| Ensembl | ENSG00000182035 |
| 蛋白证据 | Evidence at transcript level |
| HPA抗体 | HPA041124 |
| IF可靠性 | 无 |
| 主定位 | N/A |
| HPA链接 | https://www.proteinatlas.org/ENSG00000182035-ADIG/subcellular |

> **IF状态**: HPA无IF数据; 主定位: N/A)

数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q0VDE8
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22ADIG%22%5BTitle/Abstract%5D
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q0VDE8


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/ADIG/ADIG-PAE.png]]
