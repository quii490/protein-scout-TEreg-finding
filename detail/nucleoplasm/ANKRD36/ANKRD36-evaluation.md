---
type: protein-evaluation
gene: "ANKRD36"
date: 2026-06-03
tags: [protein-scout, nucleoplasm, evaluation, full-reevaluate]
status: scored
---
## ANKRD36

A6QL64 | Ankyrin repeat domain-containing protein 36A | 1915aa | pLDDT 49.7 | PM=12 | norm=63.9/100

| 维度 | 得分 | 权重 | 加权 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | 28 |
| 蛋白大小 | 10/10 | ×1 | 10 |
| 研究新颖性 | 10/10 | ×5 | 50 |
| 三维结构 | 2/10 | ×3 | 6 |
| 调控结构域 | 4/10 | ×2 | 8 |
| PPI 网络 | 5/10 | ×3 | 15 |
| **加权总分** | | | **117/180** |
| 互证加分 | | | +0.5 |
| **PubMed strict** | 12 | | |
| **归一化总分 (÷1.83)** | | | **63.9/100** |

**UniProt**: A6QL64 — No annotated function, no subcellular locations, no GO-CC entries. Aliases: ANKRD36A, KIAA1641. UniProt annotation is essentially empty for this large protein.

**HPA IF 状态**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

### 核定位评定
HPA 主定位 Nucleoplasm 与 Cytosol 双定位 (Approved)，无额外定位。UniProt 无任何亚细胞定位注释。HPA IF reliability 为 Approved，Nucleoplasm 列为主定位之一。核定位证据几乎全部依赖 HPA，但 Approved 级别的主定位赋予一定可信度。Cytosol 共主定位提示可能为核质穿梭蛋白。评为 7/10。

### 蛋白大小
1915 aa，214.5 kDa，极大型蛋白。InterPro: Ankyrin repeat (IPR002110/IPR036770/IPR050657) + IPR039497。Pfam: Ank_2 (PF12796) + DUF4593 (PF14915)。序列超长，可能含大量 ANK 重复单元。评为 10/10。

### 研究新颖性
PubMed strict count = 12（≤20 档）。主要发现：(1) PMID 31793082 (2020) — 环状 RNA ANKRD36 通过 miR-31-3p 调控 MRC-5 细胞 LPS 诱导损伤；(2) PMID 36860636 (2022) — WGCNA 分析糖尿病肾病中 ANKRD36 为潜在靶点；(3) PMID 34827175 (2021) — 整合基因组分析鉴定 ANKRD36 为慢性髓系白血病疾病进展的新型生物标志物；(4) PMID 37034737 (2023) — 单核转录组 TWAS 关联抑郁发病机制。研究聚焦于 circRNA 和生物标志物层面，缺乏蛋白功能研究。评为 10/10。

### PDB 结构
PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于 AlphaFold pLDDT 统计。
AlphaFold v6: mean_pLDDT = 49.7，pct_gt_90 = 7.8%，pct_70_90 = 26.1%，pct_lt_50 = 60.3%。整体置信度低，60% 残基 pLDDT < 50，提示大量无序区域。无实验 PDB 结构。结构预测可信度低，可能与过大的分子量导致预测困难相关。评为 2/10。

### 调控结构域
InterPro: Ankyrin repeat (IPR002110/IPR036770/IPR050657) + IPR039497。Pfam: Ank_2 (PF12796) + DUF4593 (PF14915)。纯 ANK 重复 + 未知 DUF 结构域。评为 4/10。

### PPI 网络
STRING: ANKRD36C (0.999, textmining+cooccurrence)、ANKRD36B (0.983, exp 0.092)、TMEM269 (0.652)、FAHD2B (0.629) 等 15 个伙伴。IntAct: FMR1 (Y2H)、DISC1 (Y2H)、EVI5L (validated Y2H)、STAC3 (Y2H)、GOLGA2 (validated Y2H)、HMBOX1 (validated Y2H)、IKZF1 (validated Y2H)、CEP76 (validated Y2H)、KRT37/40 (co-IP)、TYW5 (co-IP)、ITSN1 (Y2H) 等 14 条记录。PPI 以 ANKRD36 家族内同源互作和 Y2H 筛选为主，部分 validated Y2H 提供较高置信度。评为 5/10。

### 关键文献
- PMID 34827175: ANKRD36 as novel biomarker of disease progression in CML (Biology, 2021)
- PMID 36860636: WGCNA uncovers ANKRD36 in diabetic kidney disease (J Transl Intern Med, 2022)
- PMID 31793082: circANKRD36 regulates LPS-induced MRC-5 cell injury via miR-31-3p (BioFactors, 2020)

### 人工复核建议
UniProt 注释近乎空白（无功能、无定位、无 GO-CC），1915 aa 超大蛋白却无任何实验表征。CML 生物标志物研究（PMID 34827175）提供了一定疾病关联，但缺乏分子机制。ANKRD36 家族（36/36B/36C）可能功能冗余，建议综合考虑家族成员。

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000135976-ANKRD36/subcellular

![](https://images.proteinatlas.org/51757/1002_E3_1_red_green.jpg)
![](https://images.proteinatlas.org/51757/1002_E3_2_red_green.jpg)
![](https://images.proteinatlas.org/51757/1004_E3_2_red_green.jpg)
![](https://images.proteinatlas.org/51757/1004_E3_3_red_green.jpg)
![](https://images.proteinatlas.org/57661/1060_F6_1_red_green.jpg)
![](https://images.proteinatlas.org/57661/1060_F6_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
