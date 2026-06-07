---
type: protein-evaluation
gene: "ANKRD37"
date: 2026-06-03
tags: [protein-scout, nucleoplasm, evaluation, full-reevaluate]
status: scored
---
## ANKRD37

Q7Z713 | Ankyrin repeat domain-containing protein 37 | 158aa | pLDDT 72.3 | PM=25 | norm=59.0/100

| 维度 | 得分 | 权重 | 加权 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | 28 |
| 蛋白大小 | 2/10 | ×1 | 2 |
| 研究新颖性 | 8/10 | ×5 | 40 |
| 三维结构 | 5/10 | ×3 | 15 |
| 调控结构域 | 4/10 | ×2 | 8 |
| PPI 网络 | 5/10 | ×3 | 15 |
| **加权总分** | | | **108/180** |
| 互证加分 | | | +0.5 |
| **PubMed strict** | 25 | | |
| **归一化总分 (÷1.83)** | | | **59.0/100** |

**UniProt**: Q7Z713 — Nucleus (ECO:0000269 PubMed), Cytoplasm (ECO:0000269 PubMed). GO-CC: cytoplasm (IBA:GO_Central), cytosol (IDA:HPA), male germ cell nucleus (IEA:Ensembl), mitochondrion (IDA:HPA), nucleoplasm (IDA:HPA). Alias: LPR2BP.

**HPA IF 状态**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

### 核定位评定
HPA 主定位 Nucleoplasm 与 Cytosol 双定位 (Supported)，无额外定位。UniProt 明确注释 Nucleus (ECO:0000269 PubMed) 与 Cytoplasm，GO-CC 包含 nucleoplasm (IDA:HPA) 和 male germ cell nucleus (IEA:Ensembl)。核定位证据来自 UniProt PubMed 实验证据和 HPA IDA 级别注释，但 Cytosol 共主定位和 Supported reliability 降低了特异性。评为 7/10。

### 蛋白大小
158 aa，16.9 kDa，极小型蛋白，为该 15 个基因中最小者。仅含 Ank_2 (PF12796) 单一 Pfam 结构域。InterPro: Ankyrin repeat (IPR002110/IPR036770/IPR050776)。小分子量意味着结构域数目有限，但便于重组表达和体外实验操作。评为 2/10。

### 研究新颖性
PubMed strict count = 25（21-40 档）。该蛋白在缺氧生物学中有一系列研究：(1) PMID 35641902 (2022) — 缺氧分类器工具中包含 ANKRD37；(2) PMID 35218282 (2022) — ANKRD37 通过 NF-kB 通路抑制滋养层迁移与侵袭，关联子痫前期；(3) PMID 39596293 (2024) — 在淋巴内皮细胞中鲜少研究的分子；(4) PMID 36195640 (2022) — ANKRD37 与人类海马体积的因果关联。缺氧/HIF 通路是其核心研究场景。评为 8/10。

### PDB 结构
PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于 AlphaFold pLDDT 统计。
AlphaFold v6: mean_pLDDT = 72.3，pct_gt_90 = 33.5%，pct_70_90 = 25.3%，pct_lt_50 = 28.5%。置信度中等偏上。无实验 PDB 结构。158 个残基的小蛋白，AlphaFold 预测相对可靠。评为 5/10。

### 调控结构域
InterPro: Ankyrin repeat (IPR002110/IPR036770/IPR050776)。Pfam: Ank_2 (PF12796)。小型 ANK 重复蛋白，架构极简。评为 4/10。

### PPI 网络
STRING: FEM1B (0.719, exp 0.095+textmining 0.698)、BNIP3 (0.593, textmining 0.528)、HIF1A (0.510, exp 0.292)、C4orf47 (0.506)、AFF4 (0.449, exp 0.334) 等 14 个伙伴。IntAct: ZNF76 (Y2H)、HIF1AN (Y2H)、HIF1A (ChIP)、CDK9 (ChIP)、BRD4 (ChIP)、POLR2A (ChIP)、MED1 (ChIP) 等 13 条记录，多条来自同一 ChIP 研究 (PMID 23746844)。UniProt curated: HIF1AN (7 experiments)、ZNF76 (3 experiments)。PPI 体现了紧密的缺氧转录调控网络连接：HIF1A (ChIP 验证)、HIF1AN (直接互作 7 实验)、BRD4 (超级增强子)、CDK9/POLR2A/MED1 (转录延伸复合物)。评为 5/10。

### 关键文献
- PMID 35218282: ANKRD37 inhibits trophoblast migration via NF-kB pathway in preeclampsia (J Gene Med, 2022)
- PMID 35641902: Hypoxia classifier for transcriptome datasets (BMC Bioinformatics, 2022)
- PMID 36195640: Causal association of ANKRD37 with human hippocampal volume (Mol Psychiatry, 2022)

### 人工复核建议
缺氧生物学是该蛋白最清晰的功能场景。HIF1AN（HIF 羟化酶抑制因子）的 7 次实验验证互作特别值得关注，提示 ANKRD37 可能参与 HIF 通路的反馈调控。NF-kB 通路互作（子痫前期研究）扩展了其功能范围。158 aa 的小尺寸使其成为良好的结构生物学和生化研究对象。推荐作为中优先级候选。

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000186352-ANKRD37/subcellular

![](https://images.proteinatlas.org/58127/1191_C4_1_red_green.jpg)
![](https://images.proteinatlas.org/58127/1191_C4_2_red_green.jpg)
![](https://images.proteinatlas.org/58127/1194_C4_3_red_green.jpg)
![](https://images.proteinatlas.org/58127/1194_C4_4_red_green.jpg)
![](https://images.proteinatlas.org/58127/1248_H10_1_red_green.jpg)
![](https://images.proteinatlas.org/58127/1248_H10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q7Z713 |
| SMART | SM00248; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR050776;IPR002110;IPR036770; |
| Pfam | PF12796; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000186352-ANKRD37/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| HIF1AN | Intact | false |
| ZNF76 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
