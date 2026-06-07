---
type: protein-evaluation
gene: "ANKRD34B"
date: 2026-06-03
tags: [protein-scout, nucleoplasm, evaluation, full-reevaluate]
status: scored
---
## ANKRD34B

A5PLL1 | Ankyrin repeat domain-containing protein 34B | 514aa | pLDDT 55.2 | PM=4 | norm=56.8/100

| 维度 | 得分 | 权重 | 加权 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | 28 |
| 蛋白大小 | 6/10 | ×1 | 6 |
| 研究新颖性 | 10/10 | ×5 | 50 |
| 三维结构 | 2/10 | ×3 | 6 |
| 调控结构域 | 4/10 | ×2 | 8 |
| PPI 网络 | 2/10 | ×3 | 6 |
| **加权总分** | | | **104/180** |
| 互证加分 | | | +0.5 |
| **PubMed strict** | 4 | | |
| **归一化总分 (÷1.83)** | | | **56.8/100** |

**UniProt**: A5PLL1 — Cytoplasm (no evidence code), Nucleus (ECO:0000250). No annotated function. GO-CC: nucleus (IEA:UniProtKB-SubCell), pi-body (IBA:GO_Central).

**HPA IF 状态**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

### 核定位评定
HPA 主定位 Nucleoplasm 与 Mitochondria 双定位 (Approved)，额外定位 Cytosol。UniProt 注释为 Cytoplasm + Nucleus (ECO:0000250)，GO-CC 包含 nucleus (IEA) 和 pi-body (IBA:GO_Central, 一种核内 piRNA 相关结构)。核定位证据来自 HPA approved IF 和 UniProt，但 Mitochondria 共主定位降低了核内特异性。pi-body 注释（piRNA 加工核结构）为潜在亮点，但证据级别较低。评为 7/10。

### 蛋白大小
514 aa，56.4 kDa，中等大小蛋白。InterPro: Ankyrin repeat (IPR002110/IPR036770/IPR042637)。Pfam: Ank_2 (PF12796) + DUF4593 (PF13637, uncharacterized)。分子量适中。评为 6/10。

### 研究新颖性
PubMed strict count = 4（极低）。文献均为组学/生物信息学研究：(1) PMID 20184659 (2010) — 鼠胚胎干细胞 Brachyury+ 细胞转录组分析；(2) PMID 32309439 (2020) — 基于机器学习的阿尔茨海默病甲基化基因生物标志物鉴定；(3) PMID 39336722 (2024) — Nellore 牛性状 GWAS 基因优先级排序；(4) PMID 35110962 (2022) — PBMC 标记物筛选预测女性骨质疏松风险。无直接功能研究。评为 10/10。

### PDB 结构
**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。
AlphaFold v6: mean_pLDDT = 55.2，pct_gt_90 = 19.8%，pct_70_90 = 8.0%，pct_lt_50 = 62.3%。置信度偏低，超过 62% 残基 pLDDT < 50。无实验 PDB 结构。结构预测质量较差。评为 2/10。

### 调控结构域
InterPro: Ankyrin repeat (IPR002110/IPR036770/IPR042637)。Pfam: Ank_2 (PF12796) + DUF4593 (PF13637)。纯 ANK 重复 + 未知功能结构域组合。缺乏已知功能模块。评为 4/10。

### PPI 网络
STRING: 仅 3 个伙伴，FAM151B (0.507, textmining)、RMDN2 (0.420)、NWD2 (0.402)，均为低置信度。IntAct: 无实验互作记录。UniProt: 无 curated interaction。PPI 网络近乎缺失，是该列表中最弱的互作组之一。评为 2/10。

### 关键文献
- PMID 20184659: Global transcriptomic analysis of Brachyury+ ES cells (Genes Cells, 2010)
- PMID 32309439: Identification of methylated gene biomarkers in Alzheimer's disease (Biomed Res Int, 2020)
- PMID 39336722: Genetic foundations of Nellore traits GWAS (Genes, 2024)

### 人工复核建议
PPI 网络完全缺失（0 实验互作，STRING 仅 3 个低质量预测），UniProt 功能注释空白，研究极度匮乏。pi-body 注释提供微弱的 piRNA 生物学线索，但证据级别不足以支持深入追踪。该蛋白信息量过于稀少，不建议优先推进实验验证。

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000189127-ANKRD34B/subcellular

![](https://images.proteinatlas.org/43327/1788_B3_18_cr597093b210048_red_green.jpg)
![](https://images.proteinatlas.org/43327/1788_B3_3_cr597093b20f92f_red_green.jpg)
![](https://images.proteinatlas.org/43327/474_C5_1_red_green.jpg)
![](https://images.proteinatlas.org/43327/474_C5_2_red_green.jpg)
![](https://images.proteinatlas.org/43327/860_G6_2_red_green.jpg)
![](https://images.proteinatlas.org/43327/860_G6_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-A5PLL1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | A5PLL1 |
| SMART | SM00248; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR042637;IPR002110;IPR036770; |
| Pfam | PF12796;PF13637; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000189127-ANKRD34B/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| YWHAZ | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
