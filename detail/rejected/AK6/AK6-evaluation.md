---
type: protein-evaluation
gene: "AK6"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation]
status: rejected
---

## AK6 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | AK6 / CINAP |
| 蛋白大小 | 172 aa / 20.1 kDa |
| UniProt ID | Q9Y3D8 |
| 评估日期 | 2026-05-29 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 3/10 | ×4 | 12 | UniProt: Cytoplasm; Nucleus nucleoplasm; Nucleus Cajal body。胞质+核内多区室，非稳定核定位 |

#
HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

## 3. 淘汰原因

**核定位特异性 ≤3 分，直接淘汰。**

| 来源 | 定位 | 结论 |
|---|---|---|
| UniProt | Cytoplasm; Nucleus, nucleoplasm; Nucleus, Cajal body | 胞质+核内多区室 |
| GeneCards | Cytoplasm + Nucleus | 非特异性核定位 |

AK6 (Adenylate kinase isoenzyme 6, 别名 CINAP) 是腺苷酸激酶家族成员，含有 AAA_18 结构域，与 Coffin-Siris 综合征样特征相关。虽在 Cajal body 中有定位，但整体为胞质-核质的穿梭蛋白（172 aa, 20.1 kDa），非染色质/转录调控相关蛋白。PDB 中有 6 个实验结构（1RKB, 3IIJ, 3IIK, 3IIL, 3IIM, 5JZV），但核定位分数低，不满足筛选标准。

### 4. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y3D8
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y3D8

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (supported)。来源: https://www.proteinatlas.org/ENSG00000085231-AK6/subcellular

![](https://images.proteinatlas.org/70217/1801_E4_14_cr59ca0f06bf5b8_red_green.jpg)
![](https://images.proteinatlas.org/70217/1801_E4_1_cr59ca0f06be476_red_green.jpg)
![](https://images.proteinatlas.org/70217/1832_E5_1_red_green.jpg)
![](https://images.proteinatlas.org/70217/1832_E5_3_red_green.jpg)
![](https://images.proteinatlas.org/70217/1893_L15_22_cr6205016d2fe93_red_green.jpg)
![](https://images.proteinatlas.org/70217/1893_L15_29_cr5bc333a09d34e_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
