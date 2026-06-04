---
type: protein-evaluation
gene: "ANKRD12"
date: 2026-06-03
tags: [protein-scout, nucleoplasm, evaluation, full-reevaluate]
status: scored
---
## ANKRD12

Q6UB98 | Ankyrin repeat domain-containing protein 12 | 2062aa | pLDDT 41.1 | PM=18 | norm=62.8/100

| 维度 | 得分 | 权重 | 加权 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32 |
| 蛋白大小 | 10/10 | ×1 | 10 |
| 研究新颖性 | 10/10 | ×5 | 50 |
| 三维结构 | 1/10 | ×3 | 3 |
| 调控结构域 | 4/10 | ×2 | 8 |
| PPI 网络 | 4/10 | ×3 | 12 |
| **加权总分** | | | **115/180** |
| 互证加分 | | | +0.5 |
| **PubMed strict** | 18 | | |
| **归一化总分 (÷1.83)** | | | **62.8/100** |

**UniProt**: Q6UB98 — Nucleus (ECO:0000269 PubMed). May recruit HDACs to p160 coactivators/nuclear receptor complex to inhibit ligand-dependent transactivation. GO-CC: nucleoplasm (IDA:HPA), cytosol (IDA:HPA). Aliases: ANCO2, KIAA0874.

**HPA IF 状态**: HPA IF 原图未可靠获取（HPA 检索页无可用的 subcellular IF 原图）。核定位基于 HPA localization/reliability + UniProt + GO-CC。

### 核定位评定
HPA 主定位 Nucleoplasm (Supported)，额外定位 Cytosol。UniProt 注释为 Nucleus (ECO:0000269 PubMed)，功能描述显示其通过募集 HDAC 至 p160 共激活因子/核受体复合物抑制配体依赖性转录激活，明确指向核内转录调控功能。GO-CC 中 nucleoplasm 为 IDA:HPA 证据。核定位证据来自多方（HPA IF + UniProt PubMed + GO-CC），但因 Cytosol 额外定位和 Supported reliability，评为 8/10。

### 蛋白大小
2062 aa，235.7 kDa，极大型蛋白。仅含 Ankyrin repeat (IPR002110/IPR036770/IPR053210)。Pfam: Ank (PF00023) + Ank_2 (PF12796)。超长序列提示可能含大量 ANK 重复单元，结构灵活性高但结晶难度大。评为 10/10。

### 研究新颖性
PubMed strict count = 18（≤20 档）。主要研究方向：(1) 神经精神遗传学 — PMID 37231097 (2023) 发现稀有编码变异影响成人认知功能，PMID 39472661 (2025) 鉴定为抑郁症状新基因，PMID 38982111 (2024) 关联饮酒行为；(2) circRNA 功能 — PMID 36428974 (2022) 发现 CircANKRD12 在内皮细胞氧化应激中被诱导；(3) 结直肠癌 — PMID 23718802 (2013) 报道 ANKRD12 表达与临床病理特征关联。研究以 GWAS/转录组关联为主，缺乏深度分子机制研究。评为 10/10。

### PDB 结构
PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于 AlphaFold pLDDT 统计。
AlphaFold v6: mean_pLDDT = 41.1，pct_gt_90 = 7.2%，pct_70_90 = 8.8%，pct_lt_50 = 77.1%。极端低置信度，超过 77% 残基 pLDDT < 50，提示蛋白高度无序或 AlphaFold 预测失败（分子量过大）。无实验 PDB 结构。评为 1/10。

### 调控结构域
InterPro: Ankyrin repeat (IPR002110/IPR036770/IPR053210)。Pfam: Ank (PF00023) + Ank_2 (PF12796)。纯 ANK 重复蛋白，功能注释指向 HDAC 募集和转录共抑制活性。ANK 重复提供蛋白互作支架，但缺乏催化或 DNA 结合结构域。评为 4/10。

### PPI 网络
STRING 请求失败（HTTP 502）。IntAct: CDK6 (磷酸化底物)、CDK4 (磷酸化底物)、FOXM1 (磷酸化底物)、COPS5 (TAP)、HDAC3 (co-IP)、HNRNPD (cross-linking)、DISC1 (Y2H)、MEOX2 (Y2H) 等 15 条记录。UniProt: 无 curated interaction。PPI 证据以磷酸化底物关系和高通量筛选为主，HDAC3 互作与 UniProt 功能注释一致，但高质量实验验证互作较少。评为 4/10。

### 关键文献
- PMID 37231097: Rare protein coding genetic variation impact on adult cognitive function (Nat Genet, 2023)
- PMID 39472661: Whole exome sequencing identified six novel genes for depressive symptoms (Mol Psychiatry, 2025)
- PMID 36428974: CircANKRD12 induced in endothelial cell response to oxidative stress (Cells, 2022)

### 人工复核建议
2062 aa 的超大分子量导致 AlphaFold 结构预测几乎完全失败（pLDDT 41.1），需谨慎解读结构部分。该蛋白作为 HDAC 共抑制因子在转录调控中的角色有文献支持，但分子机制研究薄弱。ANCO2 别名提示其与核受体共激活因子的拮抗关系，可能在 TE 调控中有潜在角色。
