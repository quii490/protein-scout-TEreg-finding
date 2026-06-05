---
type: protein-evaluation
gene: "ANKRD10"
date: 2026-06-03
tags: [protein-scout, nucleoplasm, evaluation, full-reevaluate]
status: scored
---
## ANKRD10

Q9NXR5 | Ankyrin repeat domain-containing protein 10 | 420aa | pLDDT 63.7 | PM=4 | norm=68.3/100

| 维度 | 得分 | 权重 | 加权 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | ×4 | 36 |
| 蛋白大小 | 6/10 | ×1 | 6 |
| 研究新颖性 | 10/10 | ×5 | 50 |
| 三维结构 | 3/10 | ×3 | 9 |
| 调控结构域 | 4/10 | ×2 | 8 |
| PPI 网络 | 6/10 | ×3 | 18 |
| **加权总分** | | | **127/180** |
| 互证加分 | | | +0.5 |
| **PubMed strict** | 4 | | |
| **归一化总分 (÷1.83)** | | | **69.4/100** |

**UniProt**: Q9NXR5 — No annotated function (function empty). GO-CC: nucleoplasm (IDA:HPA) — single GO-CC entry with experimental evidence.

**HPA IF 状态**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

### 核定位评定
HPA 主定位 Nucleoplasm only (Supported)，无额外定位。UniProt GO-CC 仅有 nucleoplasm (IDA:HPA) 一条实验证据，UniProt subcellular_locations 为空。HPA 将 Nucleoplasm 列为主定位且无其他信号，核定位高度特异。唯一扣分在于 reliability 为 Supported（非 Approved）。评为 9/10。

### 蛋白大小
420 aa，44.8 kDa，中等大小蛋白。含 Ankyrin repeat (IPR002110/IPR036770/IPR050776)。Pfam: Ank (PF00023) + Ank_2 (PF12796)。分子量适中，适合常规生化分析。评为 6/10。

### 研究新颖性
PubMed strict count = 4（极低，≤20 档），属于几乎未被研究的蛋白。关键文献：(1) PMID 40044952 (2025) — RBPMS 通过 ANKRD10 可变剪接下调 MYC 通路抑制膀胱癌转移，是该蛋白首个功能性研究；(2) PMID 40909968 (2025) — 谷氨酰胺代谢相关基因预后模型中包含 ANKRD10；(3) PMID 33015072 (2020) — DNA 甲基化驱动基因分类中包含 ANKRD10。无深度功能或结构研究，知识空白显著。评为 10/10（极高新颖性）。

### PDB 结构
PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于 AlphaFold pLDDT 统计。
AlphaFold v6: mean_pLDDT = 63.7，pct_gt_90 = 34.0%，pct_70_90 = 3.8%，pct_lt_50 = 46.7%。近半数残基 pLDDT < 50，提示大量无序区域。无实验 PDB 结构。整体结构可信度偏低。评为 3/10。

### 调控结构域
InterPro: Ankyrin repeat (IPR002110/IPR036770/IPR050776)。Pfam: Ank (PF00023) + Ank_2 (PF12796)。纯 ANK 重复蛋白，无其他已知功能结构域。ANK 重复提供通用蛋白-蛋白互作支架，但缺乏明确的酶活性或 DNA 结合模块。评为 4/10。

### PPI 网络
STRING 请求失败（HTTP 502），无法获取 STRING 数据。IntAct: DPP9 (co-IP)、TLX3 (Y2H array)、PITX1 (Y2H array)、POU6F2 (Y2H array)、CSTF2 (validated Y2H)、SNRPC (validated Y2H) 等 15 条记录。UniProt curated: APPBP2 (3 exp)、DPP9 (2 exp)，以及 TLX3 (5 exp)、PATZ1 (3 exp)、POGZ (3 exp)、ZIC1 (3 exp) 等 17 个伙伴。PPI 以酵母双杂交筛选获得的转录因子和 RNA 加工因子为主（TLX3、PITX1、PATZ1、POGZ 均为核蛋白/转录调控因子），暗示 ANKRD10 可能作为转录调控适配器。评为 6/10。

### 关键文献
- PMID 40044952: RBPMS inhibits bladder cancer metastasis via alternative splicing of ANKRD10 (Commun Biol, 2025)
- PMID 40909968: Glutamine metabolism-related genes prognostic model in melanoma (Front Oncol, 2025)
- PMID 33015072: DNA methylation-driven gene classification in glioblastoma (Front Cell Dev Biol, 2020)

### 人工复核建议
PubMed strict=4 表明该蛋白几乎未被专门研究，新颖性极高，但这也意味着缺乏功能验证实验。核定位基于 HPA IDA 证据，相对可靠。PPI 网络以 Y2H 筛选数据为主，需独立验证。建议作为高新颖性 nucleoplasm 候选保留，但需额外的细胞生物学表征。

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000088448-ANKRD10/subcellular

![](https://images.proteinatlas.org/38878/716_H1_1_red_green.jpg)
![](https://images.proteinatlas.org/38878/716_H1_3_red_green.jpg)
![](https://images.proteinatlas.org/38878/719_H1_1_red_green.jpg)
![](https://images.proteinatlas.org/38878/719_H1_2_red_green.jpg)
![](https://images.proteinatlas.org/38878/764_H1_1_red_green.jpg)
![](https://images.proteinatlas.org/38878/764_H1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
