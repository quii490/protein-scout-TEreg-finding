---
type: protein-evaluation
gene: "ANKS1B"
date: 2026-06-03
tags: [protein-scout, nucleoplasm, evaluation, full-reevaluate]
status: scored
---
## ANKS1B

Q7Z6G8 | Ankyrin repeat and sterile alpha motif domain-containing protein 1B | 1248aa | pLDDT 56.9 | PM=30 | norm=72.1/100

| 维度 | 得分 | 权重 | 加权 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32 |
| 蛋白大小 | 10/10 | ×1 | 10 |
| 研究新颖性 | 8/10 | ×5 | 40 |
| 三维结构 | 5/10 | ×3 | 15 |
| 调控结构域 | 7/10 | ×2 | 14 |
| PPI 网络 | 7/10 | ×3 | 21 |
| **加权总分** | | | **132/180** |
| 互证加分 | | | +0.5 |
| **PubMed strict** | 30 | | |
| **归一化总分 (÷1.83)** | | | **72.1/100** |

**UniProt**: Q7Z6G8 — Cytoplasm (multiple ECO:0000269 PubMed), Nucleus (4 separate annotations), Postsynaptic density, Dendritic spine, Cajal body. Functions: Isoform 2 regulates nucleoplasmic coilin interactions in neurons; Isoform 3 regulates global protein synthesis by altering nucleolar numbers; Isoform 4 modulates APP processing. GO-CC: Cajal body, centrosome (IDA:HPA), cytosol, dendritic spine, nucleoplasm (IDA:HPA), plasma membrane (IDA:HPA), postsynaptic density.

**HPA IF 状态**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

### 核定位评定
HPA 主定位 Nucleoplasm (Supported)，额外定位 Plasma membrane。UniProt 注释丰富：4 条独立 Nucleus 注释（含 Cajal body 亚核定位）、Cytoplasm、Postsynaptic density、Dendritic spine。GO-CC 包含 nucleoplasm (IDA:HPA) + Cajal body。该蛋白在核内具有特定的亚核定位（Cajal body，参与 snRNP 组装和 RNA 加工），是此 15 个基因中核定位数据最丰富的蛋白之一。唯一扣分是 HPA reliability 仅为 Supported 且 Plasma membrane 额外定位。评为 8/10。

### 蛋白大小
1248 aa，138.1 kDa，大型蛋白。结构域架构丰富：Ankyrin repeat (IPR002110/IPR036770)、SAM (IPR001660/IPR013761)、PTB (IPR006020, phosphotyrosine-binding)、PH-like (IPR011993)。Pfam: Ank_2 (PF12796)、SAM_1 (PF00536)、PID (PF00640, phosphotyrosine interaction domain)。多结构域组合赋予该蛋白多样的信号适配能力。评为 10/10。

### 研究新颖性
PubMed strict count = 30（21-40 档）。该蛋白别名 AIDA-1，在神经科学领域有较好表征：(1) PMID 38129387 (2023) — ANKS1B/AIDA-1 通过控制少突胶质细胞功能调控社会行为 (Nature Communications)；(2) PMID 31388001 (2019) — ANKS1B 单倍剂量不足导致神经发育综合征 (Nature Communications)；(3) PMID 31250731 (2019) — ANKS1B 与 CNS 药物反应表型关联 (Pharmacogenomics)；(4) PMID 41268768 (2025) — 阿尔茨海默病与吸烟的全基因组交互研究涉及 ANKS1B。研究聚焦于突触功能和神经发育，有一定深度但领域相对集中。评为 8/10。

### PDB 结构
**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。
4 个 NMR 实验结构：2EAM (aa 808-874, SAM domain)、2KE7 (aa 808-893)、2KIV (aa 812-946, SAM+linker)、2M38 (aa 1042-1194, PTB domain)。仅覆盖 C 端信号结构域区域，ANK 重复区无实验结构。AlphaFold v6: mean_pLDDT = 56.9，pct_gt_90 = 18.3%，pct_70_90 = 22.6%，pct_lt_50 = 53.0%。整体置信度中等偏下，约 53% 残基 pLDDT < 50。评为 5/10。

### 调控结构域
高多样性结构域组合：ANK 重复（蛋白互作支架）+ SAM（蛋白/RNA 互作，参与聚合物形成）+ PTB/PID（磷酸化酪氨酸结合，RTK 信号）+ PH-like（膜磷脂结合）。SAM + PTB 组合使其作为信号中枢桥接受体酪氨酸激酶信号与下游效应器。Cajal body 定位（coilin 互作）将核内 snRNP 组装功能与细胞质信号转导连接。评为 7/10。

### PPI 网络
STRING: RIN1 (0.627)、RASAL2 (0.626, exp 0.620)、DAB2IP (0.623, exp 0.618)、APP (0.609, 淀粉样前体蛋白，关联阿尔茨海默病)、DLGAP1 (0.566)、CAMK2B/CAMK2A (0.550/0.530) 等 15 个伙伴。IntAct: Dlg4/PSD-95 (co-IP)、Syngap1 (co-IP)、COIL (co-IP, Cajal body 标记蛋白)、APP (Y2H)、SHC1 (co-IP)、DAB2IP (co-IP)、RIN1 (Y2H)、MCC (co-IP)、FLNC (co-IP) 等 15 条记录。COIL 互作直接验证 Cajal body 定位，APP 互作关联阿尔茨海默病病理，Dlg4/Syngap1 互作确定突触后定位。评为 7/10。

### 关键文献
- PMID 38129387: ANKS1B/AIDA-1 regulates social behaviors via oligodendrocyte function (Nat Commun, 2023)
- PMID 31388001: Haploinsufficiency in ANKS1B leads to neurodevelopmental syndrome (Nat Commun, 2019)
- PMID 31250731: ANKS1B gene and CNS drug response phenotypes (Pharmacogenomics, 2019)

### 人工复核建议
该蛋白是 15 个基因中总分最高的（132/180）。多重证据支持核定位（HPA + UniProt 4x Nucleus + Cajal body），结构域多样性丰富（ANK + SAM + PTB + PH），功能场景明确（突触信号 + 核内 RNA 加工）。Cajal body 定位提供了核内 snRNP/RNA 加工的明确场景，可能与 TE 调控存在间接关联。建议作为该批次的高优先级候选。NMR 结构覆盖 C 端 SAM + PTB，可作为结构生物学起点。

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000185046-ANKS1B/subcellular

![](https://images.proteinatlas.org/78230/1896_A9_1_red_green.jpg)
![](https://images.proteinatlas.org/78230/1896_A9_3_red_green.jpg)
![](https://images.proteinatlas.org/78230/1929_H3_1_red_green.jpg)
![](https://images.proteinatlas.org/78230/1929_H3_2_red_green.jpg)
![](https://images.proteinatlas.org/78230/2064_C11_3_red_green.jpg)
![](https://images.proteinatlas.org/78230/2064_C11_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q7Z6G8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
