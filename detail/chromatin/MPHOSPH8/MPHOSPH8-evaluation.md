---
type: protein-evaluation
gene: "MPHOSPH8"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MPHOSPH8 核蛋白评估报告

### 1. 基本信息

| 项目         | 内容                                                                     |
| ---------- | ---------------------------------------------------------------------- |
| 基因名 / 别名   | MPHOSPH8 / MPP8, Twa1                                                  |
| 蛋白大小       | 858 aa                                                                 |
| UniProt ID | Q3TYA6 (Mouse)                                                         |
| 蛋白全名       | M-phase phosphoprotein 8 (Two-hybrid partner M-phase phosphoprotein 8) |
| 评估日期       | 2026-05-30                                                             |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/chromatin/MPHOSPH8/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/chromatin/MPHOSPH8/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 9/10 | ×4 | 36 | UniProt Nucleus+Chromosome + Chromo domain（组蛋白甲基化读取器），严格染色质结合蛋白 |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 858 aa (800–1200 aa) |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed=6 篇（≤20 篇） |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold 中等（pLDDT avg 57.4，有序区 41%），chromo domain 折叠可辨识，新颖蛋白基线 |
| 🧬 调控结构域 | 10/10 | ×2 | 20 | 明确的 Chromo domain（组蛋白甲基化读取器）+ Ankyrin repeat + 多库一致 |
| 🔗 PPI 网络 | 4/10 | ×3 | 12 | STRING 15 partners（mouse），无 IntAct 实验互作，邻居含表观遗传调控因子 |
| ➕ 互证加分 | — | max +3 | +2 | 人同源物 HPA Nuclear bodies+Nucleoplasm + GO Nucleus+Chromosome + Chromo domain + 表观遗传功能明确 |
| **原始总分** |  |  | **146/183** |  |
| **归一化总分** |  |  | **79.8/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| UniProt | Nucleus, Chromosome | ECO evidence |
| GO | GO:0005634 Nucleus (IBA, IEA) | — |
| HPA | Protein Atlas: 人同源物 IF — Nuclear bodies, Nucleoplasm (human ortholog) | HPA IF (human ortholog) |


**结论**: UniProt Nucleus+Chromosome + Chromo domain（组蛋白甲基化读取器），严格染色质结合蛋白

#### 3.2 蛋白大小评估

**评价**: 858 aa (800–1200 aa)，M-phase phosphoprotein 8。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 6 |
| 关键词 | Chromo domain, Ankyrin repeat, Chromatin, Methylation reader, M-phase |

**关键文献**:
1. Gu et al. (2021). "Silencing of LINE-1 retrotransposons is a selective dependency of myeloid leukemia.". *Nat Genet*. PMID: 33833453
2. Fan et al. (2025). "TEX10: A Novel Drug Target and Potential Therapeutic Direction for Sleep Apnea Syndrome.". *Nat Sci Sleep*. PMID: 40330585
3. Rodríguez et al. (2024). "PRC1.6 localizes on chromatin with the human silencing hub (HUSH) complex for promoter-specific silencing.". *bioRxiv*. PMID: 39026796
4. Hagelkruys et al. (2022). "The HUSH complex controls brain architecture and protocadherin fidelity.". *Sci Adv*. PMID: 36332029
5. Li et al. (2016). "Lentivirus-mediated silencing of MPHOSPH8 inhibits MTC proliferation and enhances apoptosis.". *Oncol Lett*. PMID: 27313751
**评价**: PubMed 6 篇（≤20 篇），新颖性评分 10/10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 57.4 |
| 有序区域 (pLDDT>70) 占比 | 41% |
| 可用 PDB 条目 | 0 (无) |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/chromatin/MPHOSPH8/MPHOSPH8-PAE.png]]

**评价**: AlphaFold 中等（pLDDT avg 57.4，有序区 41%），chromo domain 折叠可辨识，新颖蛋白基线

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/UniProt | Ankyrin repeat (IPR002110), Ankyrin repeat-containing superfamily (IPR036770), Chromo-like domain superfamily (IPR016197), Chromo/chromo shadow domain (IPR000953), Chromo domain (IPR023780) |

**染色质调控潜力分析**: 明确的 Chromo domain（组蛋白甲基化读取器）+ Ankyrin repeat + 多库一致

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | 功能类别 | 调控相关？ |
|---------|------|---------|-----------|
| 查询中 | IntAct (mouse) | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| 15 partners | — | 多种功能类别 | 部分调控相关 |

**已知复合体成员** (GO Cellular Component):
- GO Nucleus + Chromosome (chromo domain 相关)

**PPI 互证分析**:
- IntAct 实验互作: 0 entries
- STRING 预测互作: 15 partners
- 调控相关比例: 评估中

**评价**: STRING 15 partners（mouse），无 IntAct 实验互作，邻居含表观遗传调控因子

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT | avg 57.4 | 一致 |
| 结构域 | InterPro/UniProt | 多域注释 | 一致 |
| PPI | STRING + IntAct | 15/0 partners/interactions | 一致 |
| 定位 | HPA / UniProt / GO | Nucleus, Chromosome | 一致 |

**互证加分明细**:
- 人同源物 HPA Nuclear bodies+Nucleoplasm + GO Nucleus+Chromosome + Chromo domain + 表观遗传功能明确

**总计**: +2 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ ( 80/100 )

**核心优势**:
1. 极度新颖（PubMed=6），几乎未被研究
2. 明确的 Chromo domain（组蛋白甲基化读取器）+ Ankyrin repeat + 多库一致
3. AlphaFold 中等（pLDDT avg 57.4，有序区 41%），chromo domain 折叠可辨识，新颖蛋白基线

**风险/不确定性**:
1. 小鼠基因，需验证人类同源物功能保守性
2. 核定位证据充足
3. 无 IntAct 实验互作，PPI 仅基于 STRING 预测

**下一步建议**:
- [ ] 通过人同源物验证 HPA IF 核定位
- [ ] 查询 mouse 特异性文献，确认功能保守性
- [ ] 设计 Co-IP/MS 实验验证 PPI 网络
- [ ] 进行结构域功能验证实验

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprot/Q3TYA6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q3TYA6
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MPHOSPH8
- HPA: https://www.proteinatlas.org/MPHOSPH8


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[MPHOSPH8-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/chromatin/MPHOSPH8/MPHOSPH8-PAE.png]]




