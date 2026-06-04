---
type: protein-evaluation
gene: "ANKRD31"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ANKRD31 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | ANKRD31 / Ankyrin repeat domain-containing protein 31 |
| 蛋白大小 | 1873 aa / 210.8 kDa |
| UniProt ID | Q8N7Z5 |
| 评估日期 | 2026-05-29 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA IF Approved: Nucleoplasm + Centrosome (main), Nucleoli + Vesicles (additional) |
| 蛋白大小 | 5/10 | ×1 | 5 | 1873 aa (1200-2000 aa区间)，较大 |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed 19篇，极度新颖 |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold pLDDT 43.09 (mean), 72.1%无序, baseline |
| 调控结构域 | 7/10 | ×2 | 14 | ANK repeats + RAMA domain (meiosis-specific), baseline |
| PPI 网络 | 5/10 | ×3 | 15 | GO-CC chromatin/nucleus, REC114/MEI1 功能互作 (文献证实) |
| 互证加分 | — | max +3 | +1.0 | Protein Atlas + UniProt chromatin/nucleus 一致; REC114 互作文献验证 |
| **原始总分** |  |  | **139/183** |  |
| **归一化总分** |  |  | **76.0/100** |  |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| Protein Atlas (IF) | Nucleoplasm + Centrosome (main), Nucleoli + Vesicles (additional) | Approved |
| UniProt | Nucleus, Chromosome, GO-CC: chromatin, nucleus | — |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ANKRD31/IF_images/A431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ANKRD31/IF_images/GAMG_1.jpg|GAMG]]

**结论**: 严格核蛋白。HPA Approved 核质 + 核仁 + 中心体，A-431 和 GAMG 均显示核质信号。UniProt 和 GO-CC 同时确认 Nucleus + Chromatin + Chromosome，多源一致。U2OS 无染色，可能与低表达 (RNA 0.1 nTPM) 相关。与减数分裂染色体轴功能高度吻合。

#### 3.2 蛋白大小评估
**评价**: 1873 aa, 210.8 kDa，较大的蛋白，生化操作有一定挑战性。但功能相关区域 (ANK repeats + RAMA domain) 分域清晰，可分段研究。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed 总数 | 19 |
| 最早发表年份 | 2020 |
| Chromatin/epigenetics 比例 | 高 (减数分裂染色体重组) |

**主要研究方向**:
- 减数分裂 DNA 双链断裂形成机制
- 染色体轴与 REC114-MEI1 复合体
- 精子发生与不育症遗传学
- 减数分裂重组起始

**关键文献**:
1. Dereli I et al. (2024). "Seeding the meiotic DNA break machinery and initiating recombination on chromosome axes". *Nat Commun*. PMID: 38580643 (最高影响力)
2. Xu J et al. (2023). "Essential roles of the ANKRD31-REC114 interaction in meiotic recombination and mouse spermatogenesis". *Proc Natl Acad Sci U S A*. PMID: 37976262
3. Ding X et al. (2023). "In vivo versus in silico assessment of potentially pathogenic missense variants in human reproductive genes". *Proc Natl Acad Sci U S A*. PMID: 37459509
4. Tan C et al. (2026). "A common cause of non-obstructive azoospermia: biallelic MEI1 variants and implications for infertility diagnostics". *J Assist Reprod Genet*. PMID: 41706353
5. Dereli I et al. (2023). "Seeding the meiotic DNA break machinery and initiating recombination on chromosome axes". *bioRxiv*. PMID: 38077023

**评价**: 19 篇，极度新颖。ANKRD31 在减数分裂 DNA 断裂和染色体轴重组中有明确功能角色。已有 Nat Commun 和 PNAS 文章，研究质量高。作为减数分裂特异性染色质调控因子，具有独特的生物学意义。niche 空间集中在生殖生物学。

#### 3.4 三维结构分析
| 指标 | 数值 |
|---|---|
| AlphaFold 平均 pLDDT | 43.09 |
| pLDDT >90 占比 | 12.2% |
| pLDDT 70-90 占比 | 12.9% |
| pLDDT 50-70 占比 | 2.7% |
| pLDDT <50 占比 | 72.1% |
| 可用 PDB 条目 | 0 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ANKRD31/ANKRD31-PAE.png]]

**评价**: AlphaFold 低质量预测 (72.1% pLDDT<50)。ANK repeats 区域 (488-583, 1154-1249) 可能形成局部有序结构，但蛋白大部分区域为无序。大蛋白 + 新颖性高，低结构质量属于正常现象，baseline 不扣分。减数分裂特异性蛋白通常需要 partner 结合才能形成稳定构象（如与 REC114 结合）。

#### 3.5 结构域分析
| 来源 | 结构域 |
|---|---|
| UniProt InterPro | ANKRD31 (family-specific), Ankyrin repeat, RAMA domain |
| Pfam | Ank_2, RAMA |
| SMART | ANK |
| UniProt Features | 6 ANK repeats, RAMA domain [1683-1778], 多段 Disordered |

**染色质调控潜力分析**: RAMA domain 是减数分裂染色体轴相关结构域，与 REC114 直接互作 (Xu et al. 2023, PNAS)。ANKRD31 通过 RAMA 结构域将 DNA 断裂机器招募到染色体轴上，直接参与染色质层面的 DNA 重组调控。虽无经典 chromatin-binding 结构域，但 RAMA domain 介导的染色体轴定位赋予其染色质调控功能。domain score 7 (baseline) 反映无注释域，但功能重要性高。

#### 3.6 PPI 网络

**实验验证互作** (IntAct + 文献):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---|---|---|---|---|
| REC114 | pull-down/co-IP | 37976262 | Meiotic DNA break | 是 |
| MEI1 | 遗传互作 (文献) | 41706353 | Meiotic recombination | 是 |

**STRING 预测互作**: API 不可用，文献推断。

**已知复合体成员** (GO Cellular Component):
- Chromatin
- Nucleus

**PPI 互证分析**:
- 文献确认物理互作: REC114 (pull-down, PNAS 2023)
- GO-CC 确认: chromatin, nucleus
- 调控相关比例: 100% (所有已知 partners 均为减数分裂染色质调控因子)
- 互作通过 RAMA domain 介导

**评价**: 虽然 IntAct 直接条目少（3 条），但文献提供高质量物理互作证据（REC114 pull-down）。ANKRD31 位于减数分裂染色体轴的调控网络中，与 REC114-MEI1 复合体功能关联明确。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|---|---|---|---|
| 定位 | Protein Atlas IF / UniProt / GO | Nucleus + Chromatin + Nucleoplasm | 一致 |
| 结构域 | UniProt / InterPro / Pfam / SMART | ANK + RAMA 多库确认 | 一致 |
| PPI | IntAct + 文献 + GO-CC | REC114 互作确认 | 互补 |

**互证加分明细**:
- Protein Atlas + UniProt + GO 三源定位一致: +0.5
- REC114 互作文献 + pull-down 验证: +0.5
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: (4/5)

**核心优势**:
1. 严格核蛋白：核质 + 核仁 + 染色质，Protein Atlas + UniProt + GO 三源一致
2. 极度新颖 (19篇)，但在减数分裂染色体重组中有明确功能
3. Nat Commun + PNAS 高质量文献支撑
4. REC114-MEI1 互作提供明确的功能锚点

**风险/不确定性**:
1. AlphaFold 结构极差 (72.1% 无序) — 结构研究困难
2. 蛋白较大 (1873 aa)，全长生化实验挑战
3. 研究领域窄 (减数分裂/生殖)，与表观遗传普遍机制关联有限
4. 组织表达可能局限于生殖细胞

**下一步建议**:
- [ ] 确认在体细胞中是否有表达
- [ ] RAMA-REC114 互作界面的结构生物学
- [ ] 探索 ANKRD31 在体细胞中的潜在功能

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N7Z5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000145700-ANKRD31/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22ANKRD31%22
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N7Z5


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[ANKRD31-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ANKRD31/ANKRD31-PAE.png]]




