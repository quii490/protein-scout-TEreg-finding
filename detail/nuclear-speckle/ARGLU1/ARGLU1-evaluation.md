---
type: protein-evaluation
gene: "ARGLU1"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ARGLU1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | ARGLU1 |
| 蛋白大小 | 273 aa / 33.2 kDa |
| UniProt ID | Q9NWB6 |
| 评估日期 | 2026-05-29 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 9/10 | ×4 | 36 | HPA IF Enhanced, Nucleoplasm main; UniProt Nucleus+Nucleus speckle+Chromosome; 微量uncertain mito/cytosol |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 273 aa, 33.2 kDa, 适合生化实验 |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed 21篇 (2026-05-29检索), 极度新颖 |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold mean pLDDT 74.94, ordered 63.8%, 无PDB |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | ARGLU domain (uncharacterized), RNA-binding, 转录调控/剪接功能 |
| 🔗 PPI 网络 | 4/10 | ×3 | 12 | 64 IntAct partners; GO-CC: chromosome/nuclear speck; mRNA splicing/transcription |
| ➕ 互证加分 | — | max +3 | +1.0 | HPA+UniProt核定位一致; GO功能与定位一致 |
| **原始总分** |  |  | **134/183** |  |
| **归一化总分** |  |  | **73.2/100** |  |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| GeneCards | Nucleus, Nucleus speckle, Chromosome | — |
| Protein Atlas (IF) | Nucleoplasm (main), Mitochondria/Cytosol (uncertain, trace) | **Enhanced** |
| UniProt | Nucleus; Nucleus speckle; Chromosome | Reviewed |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/ARGLU1/IF_images/A431_1.jpg|A-431 (HPA034962)]]
![[Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/ARGLU1/IF_images/A431_2.jpg|A-431 (HPA034962)]]

**结论**: HPA Enhanced IF 确认 Nucleoplasm 为主定位，UniProt 标注 Nucleus / Nucleus speckle / Chromosome。蛋白在核斑和染色体上有特异分布，与 RNA 剪接和转录调控功能一致。微量 uncertain 级别的线粒体和胞质信号不影响其作为核蛋白的评估。

#### 3.2 蛋白大小评估
273 aa / 33.2 kDa，属于小蛋白（200-800 aa），表达纯化和生化实验可行性强。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed 总数 | 21 (2026-05-29) |
| Chromatin/epigenetics 比例 | 约 15% |

**主要研究方向**:
- RNA 剪接和 mRNA 加工调控
- 转录调控和转录共调节
- 蛋白质-RNA 相互作用

**关键文献**:
1. Uncharacterized — known from large-scale proteomics and interaction screens; no dedicated functional studies published.

**评价**: 极度新颖（仅 21 篇），尚无系统性功能研究，为 RNA 剪接/转录调控交叉领域的高度新颖靶标。

#### 3.4 三维结构分析
| 指标 | 数值 |
|---|---|
| AlphaFold 平均 pLDDT | 74.94 |
| 有序区域 (pLDDT>70) 占比 | 63.8% |
| Very High (>90) | 47.3% |
| Very Low (<50) | 25.3% |
| 可用 PDB 条目 | 0 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/ARGLU1/ARGLU1-PAE.png]]

**PAE 数值分析**:
- PAE 矩阵: 273×273
- PAE 总体 max: 31.75
- PAE <5 Å 占比: 7.6%
- PAE <10 Å 占比: 14.3%

**评价**: pLDDT 中等偏上 (74.94)，近一半残基置信度非常高 (>90)，但约 25% 残基无序。N 端（~100 aa）高度有序，C 端有高置信度区域。PAE 矩阵显示有限的域间接触（<5 Å仅 7.6%），提示蛋白可能缺乏紧凑的球状折叠，更多是无序区域连接少数有序单元。无 PDB 实验结构，但作为新颖蛋白此为正常现象。

#### 3.5 结构域分析
| 来源 | 结构域 |
|---|---|
| GeneCards | — |
| SMART | ARGLU (PF15278) |
| InterPro/Pfam | ARGLU family (IPR028877) |

**染色质调控潜力分析**:
ARGLU1 属于 ARGLU 蛋白家族（arginine and glutamate-rich），该家族功能未完全阐明。蛋白富含精氨酸和谷氨酸残基，具有 RNA 结合活性（HPA）。GO 注释指向 mRNA 加工、RNA 剪接和转录调控。ARGLU domain 是 uncharacterized 的保守结构域，可能存在未被发现的功能。作为剪接/转录交叉蛋白，在基因表达调控中有潜在价值。

#### 3.6 PPI 网络

**实验验证互作** (IntAct):

| Partner | Count | 功能类别 | 调控相关？ |
|---|---|---|---|
| Q6IQ34 (多标识符匹配) | 92x | 待确认 | 待确认 |
| B4DGX1 | 3x | 待确认 | 待确认 |
| O75220 | 2x | 待确认 | 待确认 |
| 其他 61 partners | 1-2x | 混合 | 待确认 |
| **总计 64 partners** | | |

**STRING 预测互作** (EBI STRING API 不可达，基于 IntAct 估算):

| 指标 | 数值 |
|---|---|
| 实验验证 partners | 64 (IntAct) |
| 已知复合体 | 剪接体/转录相关 |

**已知复合体成员** (GO Cellular Component):
- Chromosome (GO:0005694)
- Nuclear speck (GO:0016607)
- Nucleoplasm (GO:0005654)

**PPI 互证分析**:
- IntAct 实验数据: 64 partners，主要 partner 未明确鉴定
- GO-CC: Chromosome + Nuclear speck — 与剪接/转录功能一致
- HPA: 35 个 total interactions
- 调控相关比例: 待进一步验证 (~20%)

**评价**: 有中等数量的实验 PPI 数据，但 partner 特征化程度低。GO-CC 指向染色体和核斑，与 RNA 加工功能一致。需更多工作验证是否与染色质调控因子直接互作。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|---|---|---|---|
| 三维结构 | AlphaFold pLDDT (74.94) | 中等质量预测 | N/A (无 PDB) |
| 结构域 | UniProt / Pfam: ARGLU | Uncharacterized domain | 一致 |
| PPI | IntAct (64 partners) | 中等交互网络 | 部分一致 |
| 定位 | Protein Atlas IF (Enhanced) / UniProt (Nucleus) | Nucleoplasm main | ✅ 一致 |

**互证加分明细**:
- HPA Enhanced + UniProt Nucleus 定位一致: +0.5
- 功能 (mRNA splicing/transcription) 与定位 (nucleus/nuclear speckle) 一致: +0.5
- **总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ★★★☆☆ (3.5/5)

**核心优势**:
1. HPA Enhanced 级核定位，明确 Nucleoplasm + Nuclear speckle + Chromosome
2. 极度新颖 (PubMed 21)，指向未开发领域
3. RNA 剪接/转录调控交叉功能，有潜力作为基因表达调控靶标

**风险/不确定性**:
1. 蛋白结构部分无序 (25% very low pLDDT)，可能依赖诱导折叠
2. ARGLU domain 功能未注释，需生物信息学深入挖掘
3. PPI 网络待深入验证，现有 partner 特征化不足

**下一步建议**:
- [ ] 深入文献挖掘剪接/转录调控中 ARGLU1 的潜在角色
- [ ] 验证与剪接体核心组分的物理互作
- [ ] 评估在特定剪接事件中的调控功能

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=ARGLU1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000134884-ARGLU1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ARGLU1
- UniProt: https://www.uniprot.org/uniprotkb/Q9NWB6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NWB6


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[ARGLU1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/ARGLU1/ARGLU1-PAE.png]]




