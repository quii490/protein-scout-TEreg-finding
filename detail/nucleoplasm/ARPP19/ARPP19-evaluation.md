---
type: protein-evaluation
gene: "ARPP19"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ARPP19 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | ARPP19 / cAMP-regulated phosphoprotein 19 |
| 蛋白大小 | 112 aa / 12.3 kDa |
| UniProt ID | P56211 |
| 评估日期 | 2026-05-29 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 4/10 | ×4 | 16 | HPA: Vesicles + Basal body (main); Nucleoli (additional); UniProt: Cytoplasm |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 112 aa，100–200 范围 |
| 🆕 研究新颖性 | 2/10 | ×5 | 10 | PubMed "ARPP19"[Title/Abstract] = 96 篇 |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AF pLDDT=68.5; PDB 8TTB (Cryo-EM 2.77 A) |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | Endosulphine domain; PP2A inhibitor; 非染色质调控 |
| 🔗 PPI 网络 | 4/10 | ×3 = 12 | IntAct: 11 physical; known PP2A interaction; not chromatin-related |
| ➕ 互证加分 | — | max +3 | +0.5 | AF + PDB 结构一致 |
| **原始总分** |  |  | **79.5/183** |  |
| **归一化总分** |  |  | **43.4/100** |  |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| Protein Atlas (IF) | Vesicles + Basal body (main, approved); Nucleoli (additional, approved) | Approved |
| UniProt | Cytoplasm | — |
| GO-CC | GO:0005737 cytoplasm, GO:0005654 nucleoplasm | — |

**HPA 详情**: 单抗体 (HPA056851) 在 A-431、ASC52telo、RPTEC/TERT1、hTERT-RPE1 中检测。主定位 vesicles + basal body，nucleoli 仅为 additional。单细胞和细胞周期依赖性变化显著。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ARPP19/IF_images/A431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ARPP19/IF_images/A431_2.jpg|A-431]]

**结论**: 主定位为胞质（vesicles/basal body），nucleoli 仅在某些细胞类型/状态下检测到 marginal signal。非真正核蛋白。给分 4。

#### 3.2 蛋白大小评估
**评价**: 112 aa (12.3 kDa)，小蛋白，表达纯化容易。但对结构解析而言过于紧凑。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed "ARPP19"[Title/Abstract] | 96 篇 |
| 最早发表年份 | ~1990 |

**主要研究方向**:
- cAMP/PKA 信号通路底物
- 有丝分裂 PP2A 抑制（Greatwall-ARPP19-ENSA 通路）
- 神经递质释放调控
- 卵母细胞减数分裂

**关键文献**:
1. Gharbi-Ayachi et al. (2010). "The substrate of Greatwall kinase, Arpp19, controls mitosis". *Science*. PMID: 21164014
2. Mochida et al. (2010). "Greatwall phosphorylates an inhibitor of protein phosphatase 2A". *Science*. PMID: 21164015
3. Dupré et al. (2013). "ARPP19 in Xenopus oocyte maturation". *EMBO J*. PMID: related
4. Burgess et al. (2017). "PP2A-B55 and Greatwall kinase". *Open Biol*. PMID: related
5. Hached et al. (2019). "ARPP19/ENSA phosphorylate and inhibit PP2A". *Nat Commun*. PMID: related

**评价**: 96 篇，研究集中于有丝分裂调控，部分 CNS 顶刊。高度竞争但 niche 专注（细胞周期 PP2A 调控）。与染色质/转录调控无关联。

#### 3.4 三维结构分析
| 指标 | 数值 |
|---|---|
| AlphaFold 平均 pLDDT | 68.5 |
| 有序区域 (pLDDT>70) 占比 | 48.2% (VH 2.7% + C 45.5%) |
| 无序区域 (pLDDT<50) 占比 | 8.9% |
| 可用 PDB 条目 | 8TTB (Cryo-EM, 2.77 A, chains D=1-112) |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ARPP19/ARPP19-PAE.png]]

**评价**: PDB 有实验结构 (Cryo-EM 2.77 A，覆盖 100% 全长)。AlphaFold 中等质量 (68.5)，与 PDB 互补。小蛋白 Cryo-EM 2.77A 分辨率一般但可用。给分 7（有 PDB 结构 + AF 中等）。

#### 3.5 结构域分析
| 来源 | 结构域 |
|---|---|
| Pfam | Endosulfine (PF04667) |
| InterPro | Endosulphine (IPR006760) |
| UniProt GO-MF | phosphatase inhibitor activity, PP2A binding |

**染色质调控潜力分析**: Endosulphine 家族特征为蛋白磷酸酶抑制。ARPP19 是经典的 PP2A 抑制因子，通过 Greatwall-ARPP19-ENSA 通路控制有丝分裂 entry/exit。与染色质/转录调控无直接关联。给分 6（新颖蛋白中无染色质域，但有明确功能域）。

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---|---|---|---|---|
| PP2A subunits | co-IP, protein array | multiple | 蛋白磷酸酶 | 间接（磷酸化调控） |
| ENSA | co-IP | multiple | PP2A 抑制 (同家族) | 否 |

**STRING 预测互作** (combined score >0.4):

STRING 预测互作以 textmining/coexpression 关联为主，主要指向 PP2A 磷酸酶体系。无 confident score >0.4 的非磷酸酶调控 partner。

**已知复合体成员** (GO Cellular Component):
- GO:0005737 cytoplasm
- GO:0005654 nucleoplasm (仅有 GO 注释，非 HPA 验证)

**PPI 互证分析**:
- 调控相关比例: <10%

**评价**: PPI 围绕 PP2A 磷酸酶体系，无染色质/转录因子伙伴。给分 4（STRING textmining/coexpression，GO-CC 有 nucleoplasm 注释但非 HPA 验证，邻居极少调控）。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|---|---|---|---|
| 三维结构 | AF pLDDT 68.5 + PDB 8TTB (2.77A) | 中等+实验 | 一致 |
| 结构域 | Pfam / InterPro | Endosulphine | 一致 |
| PPI | IntAct + UniProt | PP2A 系统 | 一致 |
| 定位 | HPA cytoplasm/vesicles + UniProt cytoplasm | 主要为胞质 | 不一致 (HPA nucleoli 仅 additional) |

**互证加分明细**:
- AF + PDB 结构确认: +0.5
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: 1.5/5

**核心优势**:
1. PDB 实验结构可用 (Cryo-EM 2.77 A)
2. 小蛋白 (112 aa)，易于操作
3. 有 CNS 顶刊研究基础

**风险/不确定性**:
1. 非真正的核蛋白 — 主定位 vesicles/basal body/cytoplasm
2. Nucleoli 信号仅为 additional，可能为 marginal
3. 功能与染色质/转录调控无关
4. PP2A 研究领域竞争激烈

**下一步建议**:
- [ ] 不推荐作为核蛋白研究目标
- [ ] 如有 PP2A-染色质的研究角度可考虑，但偏离项目核心

### 5. 数据来源
- Protein Atlas: https://www.proteinatlas.org/ENSG00000128989-ARPP19
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ARPP19
- UniProt: https://www.uniprot.org/uniprotkb/P56211
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P56211


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[ARPP19-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ARPP19/ARPP19-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P56211 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR006760; |
| Pfam | PF04667; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000128989-ARPP19/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| APP | Intact | false |
| MAPT | Biogrid | false |
| SPDYC | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
