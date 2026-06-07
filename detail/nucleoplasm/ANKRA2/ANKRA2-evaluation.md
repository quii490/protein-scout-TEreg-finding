---
type: protein-evaluation
gene: "ANKRA2"
date: 2026-06-03
tags: [protein-scout, nucleoplasm, evaluation, full-reevaluate]
status: scored
---
## ANKRA2

Q9H9E1 | Ankyrin repeat family A protein 2 | 313aa | pLDDT 67.4 | PM=14 | norm=68.3/100

| 维度 | 得分 | 权重 | 加权 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16 |
| 蛋白大小 | 4/10 | ×1 | 4 |
| 研究新颖性 | 10/10 | ×5 | 50 |
| 三维结构 | 7/10 | ×3 | 21 |
| 调控结构域 | 5/10 | ×2 | 10 |
| PPI 网络 | 8/10 | ×3 | 24 |
| **加权总分** | | | **125/180** |
| 互证加分 | | | +0.5 |
| **PubMed strict** | 14 | | |
| **归一化总分 (÷1.83)** | | | **68.3/100** |

**UniProt**: Q9H9E1 — Cytoplasm/cytoskeleton, Membrane (ECO:0000250). GO-CC: cytosol (IDA:UniProtKB), membrane (IDA:UniProtKB), nucleus (IBA:GO_Central). Alias: ANKRA.

**HPA IF 状态**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

### 核定位评定
HPA 主定位 Plasma membrane (Supported)，额外定位 Nucleoplasm + Cell Junctions。UniProt 注释为细胞质/细胞骨架和膜定位，GO-CC 包含 nucleus (IBA:GO_Central) 但非实验性证据。核质定位为 HPA additional location，reliability 为 Supported（低于 Approved）。综合证据显示核定位信号存在但非主要。评为 4/10。

### 蛋白大小
313 aa，34.3 kDa，小型蛋白。仅含 Ankyrin repeat (IPR002110/IPR036770)。Pfam: Ank (PF00023) + Ank_2 (PF12796)。小分子量便于重组表达，但结构域数目有限。评为 4/10。

### 研究新颖性
PubMed strict count = 14（≤20 档）。关键发现：(1) ANKRA2 与 RFX7 协同调控肿瘤抑制基因 (PMID 39181888, 2024)，是 p53 靶基因；(2) 结构基础 — ANKRA2 通过 PxLPxI/L 模体识别 RFX7 和 RFXANK (PMID 31864703, PMID 22649097)，其 ANK 重复形成"转锁"识别机制；(3) 与裸淋巴细胞综合征转录因子 RFX-B 的同源关系 (PMID 15655668)。功能聚焦于转录调控和免疫遗传学，有高质量结构生物学研究。评为 10/10。

### PDB 结构
**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。
9 个实验 PDB 结构：3SO8 (X-ray 1.90A, aa 149-310)、3V2O (1.89A, aa 148-313)、3V2X (1.85A)、3V31 (1.57A)、4LG6 (1.80A)、4QQI (2.03A) 覆盖 C 端 ANK 重复区；8CXG/8CXH/8CXI (EM 3.2-3.4A) 覆盖 N 端 aa 1-135。覆盖度良好，ANK 重复区有高分辨率晶体结构。AlphaFold mean_pLDDT = 67.4，pct_gt_90 = 47.6%。结合多实验结构，结构可信度较高。评为 7/10。

### 调控结构域
InterPro: Ankyrin repeat (IPR002110/IPR036770)。Pfam: Ank (PF00023) + Ank_2 (PF12796)。ANK 重复通过 PxLPxI/L 模体特异性识别 RFX 家族转录因子，在转录调控复合物中起适配器作用。功能明确但结构域类型单一。评为 5/10。

### PPI 网络
STRING: LRP2 (0.997, exp 0.960)、HDAC4 (0.995, exp 0.963)、CCDC8 (0.980, exp 0.949)、RFX7 (0.973, exp 0.960) 等 15 个高分伙伴。IntAct: TSHZ3、KSR1、RFX5、SAMD4A、HDAC4、ZNF362、HDAC5 等 12 条记录。UniProt: CCDC8 (4 exp)、HDAC4 (3 exp)、HDAC5 (2 exp)、RFX7 (2 exp)、SAMD4A (3 exp)、TSHZ3 (3 exp)。PPI 网络由实验验证的高质量互作主导，包括 HDAC 家族组蛋白去乙酰化酶和 RFX 转录因子。评为 8/10。

### 关键文献
- PMID 39181888: p53 target ANKRA2 cooperates with RFX7 to regulate tumor suppressor genes (Cell Death Discov, 2024)
- PMID 31864703: Structural basis for recognition of RFX7 by ANKRA2 and RFXANK (BBRC, 2020)
- PMID 22649097: Sequence-specific recognition of PxLPxI/L motif by ankyrin repeat tumbler lock (Sci Signal, 2012)

### 人工复核建议
PDB 结构覆盖度好（N 端 + C 端均有实验结构），推荐作为结构生物学研究候选。核定位偏弱，主要功能场景可能在细胞质/膜关联的转录因子调控。若目标为核蛋白，需额外验证核转位条件（如 RFX7 共表达是否促进入核）。

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (supported)。来源: https://www.proteinatlas.org/ENSG00000164331-ANKRA2/subcellular

![](https://images.proteinatlas.org/3968/1875_E7_91_red_green.jpg)
![](https://images.proteinatlas.org/3968/1875_E7_92_red_green.jpg)
![](https://images.proteinatlas.org/65263/1151_C11_2_red_green.jpg)
![](https://images.proteinatlas.org/65263/1151_C11_4_red_green.jpg)
![](https://images.proteinatlas.org/65263/1154_C11_1_red_green.jpg)
![](https://images.proteinatlas.org/65263/1154_C11_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H9E1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H9E1 |
| SMART | SM00248; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR002110;IPR036770; |
| Pfam | PF00023;PF12796; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000164331-ANKRA2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CCDC8 | Intact, Biogrid | true |
| HDAC4 | Intact, Biogrid | true |
| HDAC5 | Intact, Biogrid | true |
| RFX7 | Intact, Biogrid | true |
| CUL7 | Biogrid | false |
| LRP2 | Biogrid | false |
| NEK6 | Biogrid | false |
| RFX5 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
