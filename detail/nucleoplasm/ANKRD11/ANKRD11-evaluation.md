---
type: protein-evaluation
gene: "ANKRD11"
date: 2026-05-28
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ANKRD11 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | ANKRD11 / ANCO1 |
| 蛋白大小 | 2663 aa / 297.9 kDa |
| UniProt ID | Q6UB99 (Swiss-Prot) |
| 评估日期 | 2026-05-28 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 7/10 | ×3 | 21 | Protein Atlas 核质 Enhanced，有胞质背景；UniProt: Nucleus |
| 📏 蛋白大小 | 2/10 | ×2 | 4 | 2663 aa，极为巨大，远超理想范围 |
| 🆕 研究新颖性 | 5/10 | ×3 | 15 | PubMed 232 篇，chromatin 26 篇，epigenetics 20 篇 |
| 🏗️ 三维结构 | 2/10 | ×3 | 6 | pLDDT 均值 39.2，83.8% 残基 <50，几乎全无序 |
| 🧬 调控结构域 | 3/10 | ×2 | 6 | 仅 4 个 ANK 重复，无经典染色质结合域，蛋白主要无序 |
| 🔗 PPI | 3/10 | ×3 | **9** | 详见 3.6 PPI 分析 |
| ➕ 互证加分 | — | max +3 | +2.0 | 结构域 ≥3 来源确认 (+0.5)，功能与染色质一致 (+0.5)，定位 ≥2 来源 (+0.5)，进化保守 (+0.5) |
| **原始总分** | | | **79/158** | |
| **归一化总分** | | | **50.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Region:Disordered(1-90); Region:Disordered(128-169) | Nucleoplasm (主要) + Cytosol (次要) | Enhanced |
|---|---|---|---|
| UniProt | Nucleus | Swiss-Prot reviewed |
|---|---|---|

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/ANKRD11/IF_images/U2OS_HPA041593_1.jpg|U2OS_HPA041593_1]]
![[Projects/TEreg-finding/protein-interested/detail/rejected/ANKRD11/IF_images/U2OS_HPA041593_2.jpg|U2OS_HPA041593_2]]

**结论**: ANKRD11 是主要核蛋白。Protein Atlas 多抗体（CAB019288、HPA041593、HPA049470）在多种细胞系（A-431、U2OS、U-251MG、SiHa）中一致显示核质定位（Enhanced），有微弱胞质背景。UniProt 标注为 Nucleus。得分 7/10。

**IF 图像**:

#### 3.2 蛋白大小评估
**评价**: 2663 aa（297.9 kDa），属于 2000-3000 aa 区间。这是 ANKRD11 最大的实验障碍——过于巨大，重组合成困难，常规生化实验（pull-down、IP 效率、结晶）均面临挑战。虽然 Intrinsically Disordered Regions (IDRs) 占绝大部分，可考虑分段表达策略，但全长蛋白的研究难度很高。得分 2/10。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed 总数 | 232 |
| 最早发表年份 | ~2004 |
| Chromatin/epigenetics 比例 | 46/232 (20%) |

**主要研究方向**:
- KBG 综合征致病基因（发育障碍，主要研究方向）
- 染色质调控：HDAC 招募、组蛋白乙酰化调控（2004-2024）
- 神经发育中的表观遗传调控
- 骨稳态调节

**评价**: 发表于 200-500 区间，有一定研究基础。chromatin/epigenetics 方向已占约 20%，ANKKD11 作为染色质调控因子的身份已被确认，但在结构机制和 TE 调控方面的研究仍有空间。得分 5/10。

#### 3.4 三维结构分析
| 指标 | 数值 |
|---|---|
| AlphaFold 平均 pLDDT | 39.2 |
| PDB 实验结构 | — |
| 有序区域 (pLDDT>70) 占比 | 12.3% |
| pLDDT >90 占比 | 5.9% |
| pLDDT <50 占比 | 83.8% |
| PAE 矩阵尺寸 | 2663×2663 |
| PAE 总体均值 | 27.42 |
| PAE <5 Å 占比 | 0.5% |
| PAE <10 Å 占比 | 0.8% |
| 可用 PDB 条目 | 无实验结构 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/ANKRD11/ANKRD11-PAE.png]]

**结构特点**:
- 蛋白几乎完全无序（83.8% 残基 pLDDT <50）
- N 端 ANK 重复区（aa 167-292）是少数有折叠结构的区域
- 蛋白包含大量 Basic/Acidic 偏倚区域（K/E-rich），属于典型的 IDR
- C 端（aa 2369-2663）含降解调控区

**评价**: pLDDT 均值 39.2，远超一半序列不可预测其三维结构。PAE 矩阵大面积高值（仅 0.5% 残基对 PAE <5 Å），确认该蛋白主要以内源无序蛋白 (IDP) 形式存在。实验结构解析几乎不可能（全长），仅 N 端 ANK 重复区可单独研究。得分 2/10。

#### 3.5 结构域分析
| 来源 | 结构域 |
|---|---|
| UniProt | Ankyrin repeat ×4 (aa 167-292) |
| SMART | ANK (SM00248) |
| InterPro | Ankyrin_rpt (IPR002110), ANKRD11 (IPR042636) |
| Pfam | Ank_2 (PF12796) |
| PROSITE | ANK_REP_REGION (PS50297), ANK_REPEAT (PS50088) |

**染色质调控潜力分析**:
- ANKRD11 的染色质调控功能已被实验证实：通过与 HDAC3 等组蛋白去乙酰化酶互作，调控组蛋白乙酰化水平和基因表达。
- 然而，**从结构域角度看**，ANKRD11 仅含有 4 个 ANK 重复（蛋白-蛋白互作模块），没有经典的染色质结合域（bromodomain、chromodomain、PHD、SANT 等）。
- 蛋白的 83.8% 是 IDR，功能可能通过液-液相分离 (LLPS) 机制实现——这在转录调控中越来越被认可，但缺乏直接的结构域证据。
- PubMed >200 且无经典调控结构域注释，AlphaFold 结构质量差。

得分 3/10（虽有明确染色质调控功能但结构域证据薄弱，蛋白主要无序）。

#### 3.6 PPI :
| Partner | Score | 功能类别 | 与调控相关？ |
|---|---|---|---|
| NIPBL | 0.710 | Cohesin loader，染色质结构 | 是 |
| TP53 | 0.689 | 转录因子 | 是 |
| NCOA3 | 0.670 | 核受体共激活因子 | 是 |
| SETD5 | 0.669 | 组蛋白甲基转移酶 | 是 |
| HDAC3 | 0.658 | 组蛋白去乙酰化酶 | 是 |
| NCOA2 | 0.656 | 核受体共激活因子 | 是 |
| ZNF778 | 0.644 | 锌指蛋白 | 是 |
| SMC1A | 0.607 | Cohesin 亚基 | 是 |
| NCOA1 | 0.601 | 核受体共激活因子 | 是 |
| GPS2 | 0.591 | 转录抑制复合体 | 是 |
| SMC3 | 0.581 | Cohesin 亚基 | 是 |
| MED13L | 0.570 | Mediator 复合体 | 是 |
| AFF4 | 0.565 | 超级延伸复合体 | 是 |
| BRD4 | 0.562 | Bromodomain 蛋白，转录 | 是 |
| HDAC5 | 0.547 | 组蛋白去乙酰化酶 | 是 |
| ARID1B | 0.544 | SWI/SNF 染色质重塑 | 是 |
| EHMT1 | 0.527 | 组蛋白甲基转移酶 | 是 |
| RAD21 | 0.523 | Cohesin 亚基 | 是 |
| TRIP12 | 0.522 | E3 泛素连接酶 | 否 |
| KMT2A | 0.514 | 组蛋白甲基转移酶 | 是 |

**调控相关比例**: 19/20 (95%)

**评价**: ANKRD11 的 PPI 与 UniProt 功能注释完全吻合。Cohesin 复合体（NIPBL/SMC1A/SMC3/RAD21）的高频出现暗示 ANKRD11 参与三维染色质组织。BRD4、EHMT1、KMT2A、SETD5、ARID1B 的互作进一步支持其作为表观遗传枢纽的角色。得分 10/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|---|---|---|---|
| 三维结构 | AlphaFold pLDDT + PDB | 蛋白几乎全无序，无实验结构 | 一致（无序） |
| 结构域 | UniProt / InterPro / SMART / Pfam / PROSITE | ANK repeats 多重确认 | ✅ ≥3 来源 |
| PPI | STRING + humanPPI | 仅获 STRING 数据 | 待验证 |
| 定位 | Protein Atlas IF / UniProt | 两者均确认核定位 | ✅ 一致 |

**互证加分明细**:
- 结构域 ≥3 来源一致确认 ANK repeats (+0.5)
- 域功能：ANKRD11 的染色质调控功能在 UniProt 和文献中一致 (+0.5)
- 定位 ≥2 来源一致确认核定位 (+0.5)
- 进化保守性：ANKRD11 在脊椎动物中高度保守，模式生物有明确同源物 (+0.5)
- 三维结构无实验验证：不加分
- PPI 双数据库未完成：不加分
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ★★★☆☆ (3/5)

**核心优势**:
1. **PPI ，实验操作极困难
2. **研究热度中等**（232 篇），chromatin 方向已有一定竞争，新颖性空间有限
3. **KBG 综合征主导研究方向**，可能转移对染色质调控机制的关注
4. **全长结构解析不可行**，仅可分段研究

**下一步建议**:
- [ ] 考虑 N 端 ANK 重复区（aa 167-292）分段表达和结构研究
- [ ] 评估 TE 调控中 ANKRD11 是否参与转座子区域的组蛋白修饰调控
- [ ] 检索 humanPPI 完善 PPI 互证

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6UB99
- Protein Atlas: https://www.proteinatlas.org/ENSG00000167522-ANKRD11
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6UB99
- STRING: https://string-db.org (ANKRD11, species 9606)
- PubMed: 232 total, 26 chromatin, 20 epigenetics
- humanPPI:

![[Projects/TEreg-finding/protein-interested/detail/rejected/ANKRD11/ANKRD11-PAE.png]]


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/ANKRD11/ANKRD11-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6UB99 |
| SMART | SM00248; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR042636;IPR002110;IPR036770; |
| Pfam | PF12796; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000167522-ANKRD11/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CDCA7L | Biogrid | false |
| CSNK2B | Opencell | false |
| GOLGA2 | Biogrid | false |
| GPS2 | Bioplex | false |
| HDAC3 | Biogrid | false |
| HOOK2 | Biogrid | false |
| IMMT | Biogrid | false |
| KPNA3 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
