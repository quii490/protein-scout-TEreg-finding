---
type: protein-evaluation
gene: "ANKRD36B"
date: 2026-06-03
tags: [protein-scout, nucleoplasm, evaluation, full-reevaluate]
status: scored
---
## ANKRD36B

Q8N2N9 | Ankyrin repeat domain-containing protein 36B | 1353aa | pLDDT 59.2 | PM=5 | norm=65.6/100

| 维度 | 得分 | 权重 | 加权 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | 28 |
| 蛋白大小 | 10/10 | ×1 | 10 |
| 研究新颖性 | 10/10 | ×5 | 50 |
| 三维结构 | 3/10 | ×3 | 9 |
| 调控结构域 | 4/10 | ×2 | 8 |
| PPI 网络 | 5/10 | ×3 | 15 |
| **加权总分** | | | **120/180** |
| 互证加分 | | | +0.5 |
| **PubMed strict** | 5 | | |
| **归一化总分 (÷1.83)** | | | **65.6/100** |

**UniProt**: Q8N2N9 — No annotated function, no subcellular locations, no GO-CC entries. Multiple splice isoform interactions annotated in UniProt.

**HPA IF 状态**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

### 核定位评定
HPA 主定位 Nucleoplasm 与 Cytosol 双定位 (Approved)，无额外定位。UniProt 无任何亚细胞定位或 GO-CC 注释。HPA IF reliability 为 Approved 提供核定位主要证据，但缺乏 UniProt/GO 独立验证。Cytosol 共主定位提示可能为核质穿梭蛋白。评为 7/10。

### 蛋白大小
1353 aa，153.6 kDa，大型蛋白。InterPro: Ankyrin repeat (IPR002110/IPR036770/IPR050657) + IPR039497。Pfam: Ank_2 (PF12796) + DUF4593 (PF14915)。与 ANKRD36 共享相同结构域架构（ANK 重复 + DUF4593）。评为 10/10。

### 研究新颖性
PubMed strict count = 5（极低）。相关文献：(1) PMID 35038288 (2022) — 全外显子测序揭示卵巢颗粒细胞瘤中稀有遗传变异涉及 ANKRD36B；(2) PMID 36872244 (2023) — 特发性膜性肾病向终末期肾病转化中生物信息学分析鉴定 ANKRD36B；(3) PMID 38178908 (2023) — 越南阿尔茨海默病患者血浆游离 RNA 谱关联慢性炎症与凋亡。无直接蛋白功能研究。评为 10/10。

### PDB 结构
PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于 AlphaFold pLDDT 统计。
AlphaFold v6: mean_pLDDT = 59.2，pct_gt_90 = 15.2%，pct_70_90 = 33.7%，pct_lt_50 = 44.6%。置信度中等偏下，近 45% 残基 pLDDT < 50。无实验 PDB 结构。pLDDT 分布与 ANKRD36 类似，显示该家族蛋白整体结构灵活性高。评为 3/10。

### 调控结构域
InterPro: Ankyrin repeat (IPR002110/IPR036770/IPR050657) + IPR039497。Pfam: Ank_2 (PF12796) + DUF4593 (PF14915)。纯 ANK 重复架构。评为 4/10。

### PPI 网络
STRING: ANKRD36 (0.983, exp 0.092)、ANKRD36C (0.896, exp 0.279)、ANKRD39 (0.671)、SNAPC2 (0.606, exp 0.606) 等 15 个伙伴。IntAct: EXOC1 (Y2H)、FMR1 (Y2H)、TRAF3IP1 (Y2H)、TNIK (Y2H)、STXBP1 (Y2H)、DVL3 (Y2H array)、EXOC8 (Y2H)、TNFAIP8L1 (Y2H)、NDUFB7 (Y2H)、TXN2 (Y2H)、MAB21L3 (Y2H) 等 15 条记录。UniProt curated: 多个 isoforms 分别与 FAM9B、AKAP17A、DVL3、EHHADH、EXOC8、GEM、GLIS2、TADA3、TNFAIP8L1、TXN2 等互作。PPI 数据以 Y2H 为主，含 SNAPC2 (snRNA 激活复合物) 实验验证互作。评为 5/10。

### 关键文献
- PMID 35038288: Rare genetic variations in ovarian granulosa cell tumor WES (Bosn J Basic Med Sci, 2022)
- PMID 36872244: Bioinformatics analysis of key genes in IMN to ESRD transformation (Zhongguo Zhong Yao Za Zhi, 2023)
- PMID 38178908: Plasma cfRNA profiling of Vietnamese Alzheimer's patients (Front Mol Neurosci, 2023)

### 人工复核建议
与 ANKRD36 共享相同结构域架构和类似表达模式，可能为功能冗余的家族成员。UniProt 注释极少，建议将 ANKRD36/36B/36C 作为蛋白家族整体评估而非单独追踪单个成员。SNAPC2 互作提供了 snRNA 转录相关功能的线索。

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000196912-ANKRD36B/subcellular

![](https://images.proteinatlas.org/51757/1002_E3_1_red_green.jpg)
![](https://images.proteinatlas.org/51757/1002_E3_2_red_green.jpg)
![](https://images.proteinatlas.org/51757/1004_E3_2_red_green.jpg)
![](https://images.proteinatlas.org/51757/1004_E3_3_red_green.jpg)
![](https://images.proteinatlas.org/57661/1060_F6_1_red_green.jpg)
![](https://images.proteinatlas.org/57661/1060_F6_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
