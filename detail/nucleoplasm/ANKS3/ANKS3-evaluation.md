---
type: protein-evaluation
gene: "ANKS3"
date: 2026-06-03
tags: [protein-scout, nucleoplasm, evaluation, full-reevaluate]
status: scored
---
## ANKS3

Q6ZW76 | Ankyrin repeat and SAM domain-containing protein 3 | 656aa | pLDDT 68.6 | PM=20 | norm=74.3/100

| 维度 | 得分 | 权重 | 加权 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | 28 |
| 蛋白大小 | 8/10 | ×1 | 8 |
| 研究新颖性 | 10/10 | ×5 | 50 |
| 三维结构 | 6/10 | ×3 | 18 |
| 调控结构域 | 5/10 | ×2 | 10 |
| PPI 网络 | 8/10 | ×3 | 24 |
| **加权总分** | | | **138/180** |
| 互证加分 | | | +0.5 |
| **PubMed strict** | 20 | | |
| **归一化总分 (÷1.83)** | | | **75.4/100** |

**UniProt**: Q6ZW76 — Cell projection, cilium (ECO:0000250), Cytoplasm (ECO:0000250). May be involved in vasopressin signaling in the kidney. GO-CC: cilium (IBA:GO_Central), cytoplasm (ISS:UniProtKB). Alias: KIAA1977.

**HPA IF 状态**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

### 核定位评定
HPA 主定位 Nucleoplasm (Approved)，额外定位 Cytosol。UniProt 注释完全指向纤毛和细胞质定位（cilium ECO:0000250, cytoplasm ECO:0000250），GO-CC 仅有 cilium 和 cytoplasm，**无任何核定位注释**。这形成了 HPA (Nucleoplasm Approved) 与 UniProt (cilium only) 之间的显著矛盾。可能原因：(1) HPA 抗体存在非特异性核信号；(2) 该蛋白在特定条件下发生纤毛-核质穿梭。鉴于 HPA Approved 级别 IF 数据通常可靠，保留 Nucleoplasm 分类但标注矛盾。评为 7/10（因 UniProt 不支持核定位而扣分）。

### 蛋白大小
656 aa，72.0 kDa，中等偏大蛋白。结构域架构：Ankyrin repeat (IPR002110/IPR036770) + SAM (IPR001660/IPR013761/IPR047238)。Pfam: Ank_2 (PF12796) + SAM_1 (PF00536) + DUF4593 (PF13637)。ANK + SAM 双结构域组合赋予蛋白信号支架功能。评为 8/10。

### 研究新颖性
PubMed strict count = 20（≤20 档，边界值）。该蛋白在肾纤毛病领域有集中研究：(1) PMID 25671767 (2015) — Anks3 与 nephronophthisis 蛋白互作，为正常肾脏发育所需 (Kidney Int)；(2) PMID 24998259 (2014) — ANKS3 SAM 结构域与 ANKS6 互作的结构表征 (BMC Struct Biol)；(3) PMID 26188091 (2015) — Anks3 改变 Nek7 激酶的亚细胞定位 (BBRC)；(4) PMID 29290488 (2018) — Bicc1 SAM 聚合物晶体结构及与 ANKS3/ANKS6 互作 (Structure)；(5) PMID 29899363 (2018) — Anks3 耗竭在 mIMCD-3 细胞中的代谢表型分析 (Sci Rep)。研究集中在纤毛病变和 SAM 介导的蛋白聚合物形成，有扎实的结构生物学和功能研究基础。评为 10/10。

### PDB 结构
PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于 AlphaFold pLDDT 统计。
2 个 X-ray 实验结构：4NJ8 (1.60A, aa 421-490)、4NL9 (1.50A, aa 421-490)，均为 SAM 结构域高分辨率晶体结构。SAM 结构域有明确的结构信息，但仅覆盖全长 656aa 中的约 70aa。AlphaFold v6: mean_pLDDT = 68.6，pct_gt_90 = 36.9%，pct_70_90 = 21.5%，pct_lt_50 = 32.5%。置信度中等偏上。评为 6/10。

### 调控结构域
Ankyrin repeat (IPR002110/IPR036770) + SAM (IPR001660/IPR013761) + DUF4593。SAM 结构域可形成聚合物（与 ANKS6、Bicc1 的 SAM-SAM 互作已在结构上阐明），参与纤毛病变蛋白复合物的组装。ANK 重复提供额外的蛋白互作界面。SAM 介导的聚合物形成是独特的调控机制，具有结构生物学价值。评为 5/10。

### PPI 网络
STRING: ANKS6 (0.994, exp 0.970)、NEK7 (0.937, exp 0.739)、NEK8 (0.913, exp 0.596)、NEK9 (0.767)、BICC1 (0.749, exp 0.224)、NEK6 (0.746, exp 0.473)、NPHP1 (0.746, textmining 0.730)、NPHP3 (0.722, textmining 0.685) 等 15 个伙伴。所有主要伙伴均为实验验证：NEK7 (6 UniProt experiments)、ANKS6 (3 experiments)、NEK8 (3 experiments)。IntAct: GFI1B (Y2H)、NPM1 (cross-linking, nucleophosmin 核仁蛋白)、ANKS6/NEK7/NEK8 (socio-affinity scoring)、CSNK2A1/CSNK2A2 (co-IP, CK2 激酶)、TNKS (co-IP)、Xpo1 (pull-down) 等 15 条记录。PPI 网络是 15 个基因中最强的之一：高置信度、实验验证、功能聚焦（纤毛病变 + NEK 激酶家族 + SAM 聚合物）。评为 8/10。

### 关键文献
- PMID 25671767: Anks3 interacts with nephronophthisis proteins required for normal renal development (Kidney Int, 2015)
- PMID 29290488: Crystal structure of Bicc1 SAM polymer and interactions with ANKS3/ANKS6 (Structure, 2018)
- PMID 24998259: Characterization of SAM domain of ANKS6 and interaction with ANKS3 (BMC Struct Biol, 2014)
- PMID 26188091: Anks3 alters sub-cellular localization of Nek7 kinase (BBRC, 2015)

### 人工复核建议
该蛋白是 15 个基因中原始总分最高的（138/180），主要得益于极强的 PPI 网络和研究新颖性。但需注意 UniProt 与 HPA 的定位矛盾：UniProt 仅注释纤毛/细胞质而无核定位，HPA 却以 Nucleoplasm 为主定位。建议：(1) 查阅 HPA IF 原图确认核信号真实性；(2) 在纤毛细胞系中验证内源性 ANKS3 的亚细胞分布。若核定位得到独立验证，则该蛋白的 SAM 聚合物形成能力 + NEK 激酶调控 + 纤毛-核信号传导具有高度研究价值。NEK 激酶家族与细胞周期和纤毛解体的关系（NEK7 参与 NLRP3 炎症小体活化，NEK8 调控 Hippo 通路）进一步扩展了其功能范围。

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000168096-ANKS3/subcellular

![](https://images.proteinatlas.org/41409/2146_E2_38_red_green.jpg)
![](https://images.proteinatlas.org/41409/2146_E2_80_red_green.jpg)
![](https://images.proteinatlas.org/41409/2153_E10_40_red_green.jpg)
![](https://images.proteinatlas.org/41409/2153_E10_4_red_green.jpg)
![](https://images.proteinatlas.org/41409/486_B6_2_red_green.jpg)
![](https://images.proteinatlas.org/41409/486_B6_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6ZW76 |
| SMART | SM00248;SM00454; |
| UniProt Domain [FT] | DOMAIN 425..488; /note="SAM"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00184" |
| InterPro | IPR047238;IPR002110;IPR036770;IPR001660;IPR013761; |
| Pfam | PF12796;PF13637;PF00536; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000168096-ANKS3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ANKS6 | Intact, Biogrid | true |
| NEK7 | Intact, Biogrid | true |
| NEK8 | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
