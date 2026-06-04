---
type: protein-evaluation
gene: "ATOH8"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ATOH8 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | ATOH8 / ATH6 / BHLHA21; Transcription factor ATOH8; Class A basic helix-loop-helix protein 21; Protein atonal homolog 8 |
| 蛋白大小 | 321 aa / ~34.7 kDa |
| UniProt ID | Q96SQ7 (ATOH8_HUMAN) |
| 评估日期 | 2026-05-29 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 8 | 10 | 32 | UniProt Nucleus (IDA, PMID:24463812) + Nucleus speckle + Nucleoplasm (IDA:HPA); 核斑定位明确 |
| 📏 蛋白大小 | 10 | 10 | 10 | 321 aa，理想实验范围 |
| 🆕 研究新颖性 | 4/10 | 10 | 20 | PubMed 79篇，51-100区间 |
| 🏗️ 三维结构 | 6 | 10 | 18 | AF avg=65.0, veryhigh=23%, verylow=29%; 无PDB; PubMed≤100基线 |
| 🧬 调控结构域 | 10 | 10 | 20 | bHLH (230-282), PROSITE-PRU00981; DNA-binding TF (IDA:UniProt); E-box binding (IDA) |
| 🔗 PPI | 4/10 | ×3 | **12** | 详见 3.6 PPI 分析 |
| ➕ 互证加分 | +1.0 | max +3 | +1.0 | bHLH多库一致; 核斑定位UniProt+HPA互证 |
| **原始总分** |  |  | **113/183** |  |
| **归一化总分** |  |  | **61.7/100** |  |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| GeneCards | 暂待确认 | — |
| Protein Atlas (IF) | Nucleoplasm (IDA:HPA) | IDA |
| UniProt | Nucleus (ECO:0000269, PMID:24463812); Nucleus speckle; Cytoplasm (by similarity) | IDA |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/ATOH8/IF_images/RT4_1.jpg|RT4_1]]
![[Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/ATOH8/IF_images/Rh30_1.jpg|Rh30_1]]

**结论**: ATOH8 定位明确：Nucleus + Nuclear speckle。HPA 验证为 nucleoplasm。有核斑定位信号，但可能也存在部分胞质信号（by similarity to mouse Atoh8）。核定位证据充分。

#### 3.2 蛋白大小评估
**评价**: 321 aa，理想实验范围。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed 总数 | 79 |
| 最早发表年份 | ~2009 (PMID:24463812) |
| Chromatin/epigenetics 比例 | 中等 (bHLH TF, 主要发育调控) |

**主要研究方向**:
- 内皮细胞分化与血管新生
- 神经发育
- 肌生成调控
- SMAD 信号通路调控
- miRNA 转录调控

**关键文献**:
1. Wu et al. (2024). "A spatiotemporal atlas of cholestatic injury and repair in mice.". *Nat Genet*. PMID: 38627596
2. Divvela et al. (2022). "Atoh8 in Development and Disease.". *Biology (Basel)*. PMID: 35053134
3. Xiao et al. (2025). "ATOH8 confers the vulnerability of tumor cells to ferroptosis by repressing SCD expression.". *Cell Death Differ*. PMID: 40133667
4. Divvela et al. (2025). "Loss of Atoh8 Impairs Macroautophagy.". *Cells*. PMID: 41440013
5. Divvela et al. (2022). "Atonal homolog 8/Math6 regulates differentiation and maintenance of skeletal muscle.". *Front Cell Dev Biol*. PMID: 36060799
**评价**: 79篇文献，研究方向集中于发育生物学（内皮、神经、肌肉）。bHLH TF家族非常庞大，但 ATOH8 研究相对较少。

#### 3.4 三维结构分析
| 指标 | 数值 |
|---|---|
| AlphaFold 平均 pLDDT | 65.0 |
| veryhigh (pLDDT>90) 占比 | 23% |
| confident (70-90) 占比 | 9% |
| 有序区域 (pLDDT>70) 占比 | 32% |
| verylow (pLDDT<50) 占比 | 29% |
| 可用 PDB 条目 | 0 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/ATOH8/ATOH8-PAE.png]]

**评价**: AlphaFold 整体中等 (avg=65.0)，bHLH域 (230-282) 区域预期有一定折叠。无实验PDB。新颖蛋白基线6分。

#### 3.5 结构域分析
| 来源 | 结构域 |
|---|---|
| GeneCards | 暂待确认 |
| SMART | 待分析 |
| InterPro/Pfam | bHLH (PROSITE-PRU00981), 230-282 |
| UniProt | bHLH domain |

**染色质调控潜力分析**: bHLH 是经典的 DNA 结合+二聚化结构域。ATOH8 通过 bHLH 结合 E-box (CANNTG) DNA 元件并形成同源/异源二聚体。该域直接赋予序列特异性 DNA 结合和转录调控能力。得分 10。

#### 3.6 PPI 网络

**实验验证互作** (IntAct):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---|---|---|---|---|
| PPP3CB | 5 experiments | IntAct | 钙调磷酸酶催化亚基 | 间接（信号通路） |

**STRING 预测互作**:

| Partner | Score | 功能类别 | 调控相关？ |
|---|---|---|---|
| （STRING API 数据获取中） | - | - | - |

**已知复合体成员** (GO Cellular Component):
- 无染色质调控复合体GO注释

**PPI 互证分析**:
- 仅 IntAct 实验: PPP3CB
- 调控相关比例: 目前数据不足以准确判断

**评价**: PPI 数据极为稀疏（仅PPP3CB in IntAct）。作为相对新颖的 TF，PPI 网络尚未充分挖掘。得分 4。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|---|---|---|---|
| 三维结构 | AlphaFold avg=65.0 + 无PDB | AF中等 | N/A |
| 结构域 | UniProt bHLH / PROSITE bHLH | 多库一致 | ✅一致 |
| 定位 | UniProt Nucleus+Nuclear speckle + HPA nucleoplasm | 多源一致 | ✅一致 |

**互证加分明细**:
- bHLH 结构域多库一致: +0.5
- 核定位 + 核斑多源互证 (UniProt + HPA): +0.5
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐ (3.5/5)

**核心优势**:
1. 明确的 bHLH DNA-binding TF 结构域，核斑定位清晰
2. 蛋白大小理想（321 aa）
3. PubMed 79 篇——niche 空间充足

**风险/不确定性**:
1. PPI 数据极度稀疏，已知互作 partner 极少
2. 无实验 PDB 结构，AF 质量中等
3. bHLH 家族竞争激烈

**下一步建议**:
- [ ] 基于 bHLH 序列进行酵母双杂交筛选互作 partner
- [ ] 确认 IF 核斑共定位（SC35/SRSF2 共染）

### 5. 数据来源
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22ATOH8%22%5BTitle%2FAbstract%5D
- UniProt: https://www.uniprot.org/uniprotkb/Q96SQ7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96SQ7


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[ATOH8-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/ATOH8/ATOH8-PAE.png]]




