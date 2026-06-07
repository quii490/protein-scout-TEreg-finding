---
type: protein-evaluation
gene: "ELP1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ELP1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ELP1 / IKBKAP, IKAP |
| 蛋白名称 | Elongator complex protein 1 |
| UniProt ID | O95163 |
| 蛋白大小 | 1332 aa |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA Nuclear bodies+Nucleoplasm + UniProt Nucleus |
| 蛋白大小 | 5/10 | ×1 | 5 | 1332 aa (偏大) |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed 53 篇 (51-100) |
| 三维结构 | 8/10 | ×3 | 24 | AF pLDDT=83.9, good=85% + PDB 5条目 |
| 调控结构域 | 8/10 | ×2 | 16 | WD40 重复 + TPR domain, Elongator 支架 |
| PPI 网络 | 8/10 | ×3 = 24 | Elongator 全复合体 (ELP2-6) |
| 互证加分 | — | max +3 | +1.5 | PDB Elongator复合体 + GO复合体一致 |
| **原始总分** |  |  | **132.5/183** |  |
| **归一化总分** |  |  | **72.4/100** |  |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|------|------|--------|
| TEreg 筛选 | 核评分 6 | Tier1 |
| Protein Atlas (IF) | Nuclear bodies, Nucleoplasm | Supported |
| UniProt | Cytoplasm, Nucleus | Reviewed |
| GO-Cellular Component | Elongator holoenzyme complex, Nucleus | IDA |


**HPA IF 图像**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ELP1/IF_images/137325_A_8_3_rna_selected.jpg|HPA IF]]

**结论**: 多源确认核定位。作为 Elongator 复合体最大亚基（支架蛋白），定位于细胞质和核质。

#### 3.2 蛋白大小评估
**评价**: 1332 aa，偏大（>1200 aa）。大蛋白的表达和纯化有一定挑战，但结构域明确。

#### 3.3 研究现状
| 指标 | 数值 |
|------|------|
| PubMed 总数 | 53 |
| 主要研究方向 | tRNA 修饰, 转录延伸, 家族性植物神经功能障碍症 |

**主要研究方向**:
- Elongator 复合体支架蛋白
- tRNA 摆动位置修饰
- 家族性植物神经功能障碍症 (FD) 致病基因

**关键文献**:
1. Slaugenhaupt et al. (2001). "IKBKAP mutation in FD". PMID: 11179008
2. Hawkes et al. (2002). "Elongator complex purification". PMID: 11714725
3. Dauden et al. (2017). "Elongator structure". PMID: 28257601

**评价**: 研究中等（53篇），以疾病机制为主。作为 Elongator 支架蛋白有明确复合体结构。

#### 3.4 三维结构分析
| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| 平均 pLDDT | 83.9 |
| 有序区域 (pLDDT>70) 占比 | 85% |
| 可用 PDB 条目 | 5CQR, 8PTX, 8PTY, 8PTZ, 8PU0 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ELP1/ELP1-PAE.png]]

**评价**: AF 预测好 + 5个PDB Cryo-EM 复合体结构。结构可信度高。

#### 3.5 结构域分析
| 来源 | 结构域 |
|------|--------|
| InterPro | Elongator complex protein 1 (IPR024590) |
| InterPro | WD40/YVTN repeat-like domain (IPR015943) |
| InterPro | TPR domain (IPR039776) |
| Pfam | IKI3 family, WD40, TPR |

**染色质调控潜力分析**: Elongator 复合体参与 RNA Pol II 转录延伸（在酵母中确证）。WD40 和 TPR 域介导蛋白-蛋白互作和复合体组装。

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作**:
| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| ELP3 | 1.00 | Elongator 催化亚基 | 是 |
| ELP5 | 1.00 | Elongator 亚基 | 是 |
| ELP4 | 1.00 | Elongator 亚基 | 是 |
| ELP2 | 1.00 | Elongator 亚基 | 是 |
| ELP6 | 0.99 | Elongator 亚基 | 是 |

**已知复合体成员** (GO Cellular Component):
- Elongator holoenzyme complex (GO:0033588)

**PPI 互证分析**:
- 完全围绕 Elongator 复合体 (ELP2-6)
- 调控相关比例: 极高 (100% Elongator 成员)

**评价**: PPI 极其聚焦于 Elongator 复合体自身组装。是核心支架蛋白。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AF + Cryo-EM 5条目 | pLDDT 83.9 + 复合体结构 | 一致 |
| PPI | STRING Elongator | ELP2-6 全复合体 | 一致 |
| 定位 | HPA / UniProt / GO | Nucleoplasm | 一致 |

**互证加分明细**:
- Cryo-EM 复合体结构 (+0.5)
- Elongator 复合体 PPI 确证 (+0.5)
- 多项证据交叉验证 (+0.5)
- **总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: 3 / 5

**核心优势**:
1. Elongator 复合体核心支架
2. Cryo-EM 复合体结构
3. 明确的复合体组装和转录延伸功能

**风险/不确定性**:
1. 蛋白大 (1332 aa)，实验操作有挑战
2. 哺乳动物 Elongator 是否直接参与转录延伸存在争议
3. 主要功能可能是 tRNA 修饰而非转录调控

**下一步建议**:
- [ ] 确认哺乳动物 Elongator 在 TE 转录中的角色
- [ ] 纯化重组 Elongator 复合体用于功能实验

### 5. 数据来源
- UniProt: O95163 (https://www.uniprot.org/uniprotkb/O95163)
- AlphaFold: AF-O95163-F1 v6 (https://alphafold.ebi.ac.uk/entry/O95163)
- Protein Atlas: ELP1 (https://www.proteinatlas.org/)
- PubMed: ELP1 (https://pubmed.ncbi.nlm.nih.gov/)
- STRING: ELP1 (https://string-db.org/)
- InterPro: O95163 (https://www.ebi.ac.uk/interpro/)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[ELP1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ELP1/ELP1-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O95163 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR056167;IPR056164;IPR056165;IPR006849;IPR056169;IPR056166;IPR015943; |
| Pfam | PF23925;PF04762;PF23797;PF23936;PF23878; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000070061-ELP1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ELP2 | Intact, Biogrid | true |
| ELP3 | Intact, Biogrid | true |
| HTT | Intact, Biogrid | true |
| IRF4 | Intact, Biogrid | true |
| SNAPIN | Intact, Biogrid | true |
| TTR | Intact, Biogrid | true |
| CAMK2A | Bioplex | false |
| CCNF | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
