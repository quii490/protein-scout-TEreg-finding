---
type: protein-evaluation
gene: "ARID1B"
date: 2026-05-28
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ARID1B 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | ARID1B / BAF250B, OSA2, KIAA1235, DAN15, p250R, hOsa2 |
| 蛋白大小 | 2319 aa / 243.9 kDa |
| UniProt ID | Q8NFD5 |
| 评估日期 | 2026-05-28 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 10/10 | ×3 | 30.0 | 实验验证 Nucleus (PubMed: 11988099)，SWI/SNF 核心组分 |
| 📏 蛋白大小 | 2/10 | ×2 | 4.0 | 2319 aa / 243.9 kDa，过于巨大，生化操作困难 |
| 🆕 研究新颖性 | 2/10 | ×3 | 6.0 | 520 篇 PubMed，375 篇 chromatin 相关，有一定关注度 |
| 🏗️ 三维结构 | 2/10 | ×3 | 6.0 | 平均 pLDDT 46.2，仅 23.5% >70，PAE 均值 27.08，高度无序 |
| 🧬 调控结构域 | 10/10 | ×2 | 20.0 | ARID DNA-binding domain + BAF250_C，6 个数据库确认 |
| 🔗 PPI | PROSITE-ProRule + 1 篇实验文献 (PubMed: 11988099) |
| GO (UniProt) | C:nucleus, nucleoplasm, SWI/SNF complex, bBAF/npBAF/nBAF complex, chromatin | 多个证据级别 |
| GO (HPA) | C:cytosol (IDA:HPA) | 少量胞质信号 |
| Protein Atlas (IF) | Nucleoplasm | Supported |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/ARID1B/IF_images/131_G10_1_red_green.jpg|131_G10_1]]
![[Projects/TEreg-finding/protein-interested/detail/rejected/ARID1B/IF_images/131_G10_2_red_green.jpg|131_G10_2]]

**结论**: ARID1B 核定位有实验证据支持。作为 SWI/SNF (BAF) 复合体核心亚基，其主要定位在细胞核和 SWI/SNF 复合体。GO 注释中存在 "cytosol (IDA:HPA)" 条目，提示可能有少量胞质分布，但这不影响其作为核染色质重塑蛋白的核心功能定性。SWI/SNF 复合体的组装发生在核内，胞质信号可能反映新合成蛋白的暂态。

**IF 图像**:

#### 3.2 蛋白大小评估
**评价**: 2319 aa / 243.9 kDa。与 ARID1A 类似，属于巨蛋白级别，全长蛋白的重组表达和体外生化实验极其困难。位于 2000-3000 aa 区间，评分较低。对于实验研究，需要使用截短片段（ARID domain: aa 1136-1227）。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed 总数 (全文搜索) | 520 |
| PubMed (Title/Abstract + gene/protein) | 281 |
| Chromatin/epigenetics 相关 | 375 (72.1%) |
| 最早发表年份 | ~2002 |

**主要研究方向**:
- Coffin-Siris 综合征 (CSS)：ARID1B 单倍剂量不足导致智力障碍
- 神经发育与染色质重塑
- SWI/SNF 复合体亚基组成变化
- 癌症中的 ARID1B 突变（不如 ARID1A 频繁）
- ARID1A/ARID1B 的功能冗余与特异性

**评价**: ARID1B 有 520 篇论文，远少于 ARID1A（2475 篇），但仍属于研究较多的染色质调控蛋白。与 ARID1A 不同，ARID1B 的研究重心在神经发育和 Coffin-Siris 综合征，其在 TE 调控中的角色几乎未被探索。虽然论文总量较多，但 TE 调控方向可能存在 niche 空间。评分适当上调——虽然 520 篇落入 500-2000 区间（2 分），但其 TE 调控方向的空白提供了一定创新机会。

#### 3.4 三维结构分析
| 指标 | 数值 |
|---|---|
| AlphaFold 平均 pLDDT | 46.2 |
| 有序区域 (pLDDT>70) 占比 | 23.5% (544/2319 aa) |
| pLDDT>90 区域占比 | 16.8% (389/2319 aa) |
| α-helix 含量 | PDB 无 HELIX 记录（AlphaFold 模型） |
| β-sheet 含量 | PDB 无 SHEET 记录 |
| 可用 PDB 条目 | 无全长实验结构 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/ARID1B/ARID1B-PAE.png]]

**PAE 数值分析**:
- PAE 矩阵尺寸: 2319×2319
- PAE 总体均值: 27.08
- PAE <5 Å 占比: 2.0%
- PAE <10 Å 占比: 3.8%

**评价**: 与 ARID1A 几乎相同的结构特征。平均 pLDDT 46.2，76.5% 残基无序。PAE 数据也与 ARID1A 高度一致（均值 27.08 vs 27.13）。作为 ARID1A 的旁系同源物（paralog），两个蛋白共享高度相似的结构域架构但整体折叠不良。这是大型骨架蛋白的典型特征：长段内在无序区域提供蛋白-蛋白相互作用界面，ARID domain 作为唯一的折叠域提供 DNA 结合功能。

#### 3.5 结构域分析
| 来源 | 结构域 |
|---|---|
| CDD | cd16877 - ARID_ARID1B (ARID DNA-binding domain) |
| Pfam | PF01388 - ARID; PF12031 - BAF250_C |
| SMART | SM01014 - ARID; SM00501 - BRIGHT |
| PROSITE | PS51011 - ARID |
| InterPro | IPR038040 - ARID_ARID1B; IPR001606 - ARID_dom; IPR036431 - ARID_dom_sf; IPR021906 - BAF250/Osa; IPR033388 - BAF250_C |
| Gene3D | 1.10.150.60 - ARID DNA-binding domain |
| PANTHER | PTHR12656:SF11 - ARID1B |

**染色质调控潜力分析**: ARID1B 与 ARID1A 共享相同的结构域架构：ARID DNA-binding domain (aa 1136-1227) + BAF250_C domain。ARID 域识别富含 AT 的 DNA 序列；BAF250_C 是 BAF250 亚家族的特征域。作为 SWI/SNF 核心亚基，ARID1B 直接参与 ATP 依赖性染色质重塑。ARID1A 和 ARID1B 在许多 SWI/SNF 复合体中互斥存在，决定了复合体的功能和基因组定位特性。

#### 3.6 PPI :
| Partner | Score | 功能类别 | 与调控相关？ |
|---|---|---|---|
| SMARCA4 | 0.999 | SWI/SNF ATPase (BRG1) | 是 |
| SMARCA2 | 0.999 | SWI/SNF ATPase (BRM) | 是 |
| SMARCB1 | 0.999 | SWI/SNF core (BAF47/INI1) | 是 |
| SMARCC1 | 0.999 | SWI/SNF core (BAF155) | 是 |
| SMARCC2 | 0.999 | SWI/SNF core (BAF170) | 是 |
| SMARCD1 | 0.998 | SWI/SNF core (BAF60A) | 是 |
| SMARCD2 | 0.995 | SWI/SNF core (BAF60B) | 是 |
| SMARCD3 | 0.993 | SWI/SNF core (BAF60C) | 是 |
| SMARCE1 | 0.999 | SWI/SNF core (BAF57) | 是 |
| ARID1A | 0.999 | Paralog (BAF250A) | 是 |
| ACTL6A | 0.995 | SWI/SNF actin-related | 是 |
| PBRM1 | 0.998 | PBAF complex (BAF180) | 是 |
| ARID2 | 0.997 | PBAF complex (BAF200) | 是 |
| DPF1 | 0.991 | SWI/SNF (BAF45B) | 是 |
| DPF2 | 0.999 | SWI/SNF (BAF45D) | 是 |
| DPF3 | 0.995 | SWI/SNF (BAF45C) | 是 |
| BCL7A | 0.989 | SWI/SNF associated | 是 |
| BCL7C | 0.991 | SWI/SNF associated | 是 |
| SS18 | 0.989 | SWI/SNF associated | 是 |
| BRD9 | 0.989 | SWI/SNF (GBAF/BRM-associated) | 是 |

**UniProt 实验互作** (IntAct):

| Partner | 实验次数 | 功能类别 |
|---|---|---|
| SMARCC2 | 7 | SWI/SNF core |
| SMARCA4 | 5 | SWI/SNF ATPase |
| SMARCA2 | 4 | SWI/SNF ATPase |
| DPYSL2 | 2 | CRMP2 (non-regulatory) |

**humanPPI** (prodata.swmed.edu): - Top 10 重叠数: N/A
- STRING top partners 与 UniProt IntAct 实验数据一致（SMARCA4, SMARCA2, SMARCC2 双验证）

**调控相关比例**: 19/20 (95.0%)

**评价**: PPI ，UniProt IntAct 进一步验证了与 SMARCC2 (7 次实验)、SMARCA4 (5 次)、SMARCA2 (4 次) 的物理相互作用。值得注意的是 ARID1A 是 ARID1B 的 top partner，反映了两者在复合体中的互斥关系。| Nucleus + SWI/SNF complex | 完全一致 |

**互证加分明细**:
- 结构域：≥3 个独立来源检出 ARID domain (+0.5)，域功能在 GO 中与染色质重塑一致 (+0.5)
- 定位：UniProt + GO 多个来源确认核定位 (+0.5)
- 进化保守：Osa2 (Drosophila) 明确同源物，SWI/SNF 复合体功能保守 (+0.5)
**总分**: +2.0 / max +3

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|---|---|---|---|
| 三维结构 | AlphaFold + PDB | 见 3.4 节 | — |
| 结构域 | UniProt / InterPro / Pfam | 见 3.5 节 | — |
| PPI | STRING | 见 3.6 节 | — |
| 定位 | Protein Atlas IF / UniProt / GO | Nucleus | ✅ |

### 4. 总体评价

**推荐等级**: ★★★☆☆ (3/5)

**核心优势**:
1. **SWI/SNF 核心亚基**：与 ARID1A 平行的 BAF250B，相同功能重要性
2. **PPI - [ ] 利用 Coffin-Siris 综合征患者细胞系研究 ARID1B 缺失对 TE 表达的影响
- [ ] 比较 ARID1A vs ARID1B 在 TE 调控中的功能差异（mutual exclusive 复合体）
- [ ] 考虑 ARID1B 在神经元特异性 SWI/SNF (nBAF) 复合体中的独特角色

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NFD5
- PubMed: 520 articles (search: "ARID1B")
- STRING: https://string-db.org (ARID1B, 9606)
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NFD5
- EBI Proteins API: https://www.ebi.ac.uk/proteins/api/proteins/Q8NFD5

![[Projects/TEreg-finding/protein-interested/detail/rejected/ARID1B/ARID1B-PAE.png]]


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/ARID1B/ARID1B-PAE.png]]




