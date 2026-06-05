---
type: protein-evaluation
gene: "ANKRD30B"
date: 2026-06-03
tags: [protein-scout, nucleoplasm, evaluation, full-reevaluate]
status: scored
---
## ANKRD30B

Q9BXX2 | Ankyrin repeat domain-containing protein 30B | 1392aa | pLDDT 51.6 | PM=4 | norm=58.5/100

| 维度 | 得分 | 权重 | 加权 |
|---|---|---|---|---|
| 核定位特异性 | 6/10 | ×4 | 24 |
| 蛋白大小 | 10/10 | ×1 | 10 |
| 研究新颖性 | 10/10 | ×5 | 50 |
| 三维结构 | 2/10 | ×3 | 6 |
| 调控结构域 | 4/10 | ×2 | 8 |
| PPI 网络 | 3/10 | ×3 | 9 |
| **加权总分** | | | **107/180** |
| 互证加分 | | | +0.5 |
| **PubMed strict** | 4 | | |
| **归一化总分 (÷1.83)** | | | **58.5/100** |

**UniProt**: Q9BXX2 — No annotated function, no subcellular locations, no GO-CC entries. UniProt annotation is minimal for this protein.

**HPA IF 状态**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

### 核定位评定
HPA 主定位 Nucleoli (Approved)，额外定位 Nucleoplasm。UniProt 无任何亚细胞定位注释，GO-CC 为空。HPA IF reliability 为 Approved，Nucleoli 主定位 + Nucleoplasm 额外定位提示该蛋白主要分布于核仁，部分定位于核质。核仁-核质双分布模式在大型 ANK 重复蛋白中较常见。因 Nucleoplasm 非主定位，评为 6/10。

### 蛋白大小
1392 aa，158.0 kDa，大型蛋白。InterPro: Ankyrin repeat (IPR002110/IPR036770/IPR050657) + IPR039497。Pfam: Ank_2 (PF12796) + DUF4593 (PF14915, uncharacterized domain)。大分子量提示含多个结构单元。评为 10/10。

### 研究新颖性
PubMed strict count = 4（极低）。文献均为基因组/表观基因组关联研究：(1) PMID 30712078 (2019) — 跨脑区 DNA 甲基化和基因表达整合分析鉴定 ANKRD30B 为阿尔茨海默病新基因；(2) PMID 32303053 (2020) — ANKRD30B 在 Williams 综合征中潜在的 DNA 甲基化调控角色；(3) PMID 40945769 (2026) — 全外显子测序关联自杀思维的炎症通路；(4) PMID 41290930 (2025) — 三阴性乳腺癌间质转录组学。无直接功能或生化研究。评为 10/10（极高新颖性）。

### PDB 结构
PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于 AlphaFold pLDDT 统计。
AlphaFold v6: mean_pLDDT = 51.6，pct_gt_90 = 8.6%，pct_70_90 = 25.0%，pct_lt_50 = 54.8%。整体置信度低，超过半数残基 pLDDT < 50。无实验 PDB 结构。结构预测质量较差，可能与蛋白尺寸和大规模无序区域相关。评为 2/10。

### 调控结构域
InterPro: Ankyrin repeat (IPR002110/IPR036770/IPR050657) + IPR039497。Pfam: Ank_2 (PF12796) + DUF4593 (PF14915, 功能未知结构域)。ANK 重复提供蛋白互作支架，DUF4593 结构域功能未知。评为 4/10。

### PPI 网络
STRING: ANKRD30A (0.492, exp 0.360)、ASB15 (0.511)、ANKRD39 (0.507)、NFKBIA (0.505)、CDKN2C (0.487, weak) 等 9 个伙伴，多数为低置信度。IntAct: ANKRD30A (co-IP, PMID 33961781)、TRIM44 (co-IP)、CFAP299 (co-IP) 等少量记录。整体 PPI 网络稀少且置信度低。评为 3/10。

### 关键文献
- PMID 30712078: Integrated DNA methylation and gene expression profiling implicates ANKRD30B in Alzheimer's disease (Acta Neuropathol, 2019)
- PMID 32303053: ANKRD30B methylation in Williams syndrome (Neuropsychopharmacology, 2020)
- PMID 40945769: WES analysis of suicidal thoughts implicates inflammatory pathways (J Affect Disord, 2026)

### 人工复核建议
UniProt 注释近乎空白（无功能、无定位、无 GO-CC），研究极度稀缺。核定位全部依赖 HPA IF (Approved)，UniProt 无独立验证。该蛋白在当前阶段的信息量极少，可能适合作为"探索性候选"，但不适合作为优先研究对象。若 HPA IF 原图可获取，建议核实核仁/核质信号的真实性。

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (approved)。来源: https://www.proteinatlas.org/ENSG00000180777-ANKRD30B/subcellular

![](https://images.proteinatlas.org/43287/2058_E9_2_red_green.jpg)
![](https://images.proteinatlas.org/43287/2058_E9_4_red_green.jpg)
![](https://images.proteinatlas.org/43287/2089_C1_1_red_green.jpg)
![](https://images.proteinatlas.org/43287/2089_C1_2_red_green.jpg)
![](https://images.proteinatlas.org/43287/2142_G1_1_red_green.jpg)
![](https://images.proteinatlas.org/43287/2142_G1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
