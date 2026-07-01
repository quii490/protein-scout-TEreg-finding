---
type: protein-evaluation
gene: "TPI1"
date: 2026-05-30
tags: [protein-scout, rejected]
status: rejected
---

## TPI1 核蛋白评估报告（淘汰）

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | TPI1 |
| 蛋白名称 | triosephosphate isomerase 1 |
| UniProt ID | P60174 |
| 蛋白大小 | 249 aa |
| 核定位分数 | 4 |
| PubMed 总数 | 151 |
| 评估日期 | 2026-05-30 |

### 2. 淘汰原因

**淘汰类型**: PubMed 超过阈值

**详细理由**: PubMed 发表数 151 篇，超过 100 篇阈值，研究领域过于拥挤

#
HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

## 3. 关键数据

| 指标 | 数值 |
|------|------|
| PubMed 总数 (strict sum) | 151 |
| PubMed 最大值 | 151 |
| PubMed 近 5 年 | 69 |
| 核定位分数 (weighted max) | 4 |
| 核定位分级 | Tier1_conserved_high_confidence |
| Research hotness | 4.654 |

### 4. 结论

该基因不满足蛋白评估的基本筛选条件（PubMed ≤ 100 且核定位 > 3），予以淘汰。

### 深度机制分析

TPI1（triosephosphate isomerase 1, 249 aa, UniProt P60174）。REJECTED——PubMed=151篇超过阈值（>100）。定位于Nucleoplasm（HPA Approved），但该蛋白是糖酵解途径中磷酸二羟丙酮（DHAP）与3-磷酸甘油醛（G3P）的可逆异构化酶，是有史以来催化效率最高的酶之一（kcat/KM接近扩散极限，~10^9 M^-1s^-1）。PDB已解析大量高分辨率结构，催化机制（烯二醇中间体，Glu165/Lys13/His95催化三联体）已详尽阐明。

从酶学角度，TPI1的催化完美性（"catalytically perfect enzyme"）是其核心生化特征——反应速率受底物扩散控制而非化学转化步骤。其基因突变导致常染色体隐性遗传的磷酸三糖异构酶缺乏症（OMIM: 615512），临床表现包括溶血性贫血和进行性神经退行性变。糖酵解酶是经典的"兼职"（moonlighting）候选蛋白——已有报道TPI1可作为自身抗原、结合纤连蛋白、并在细胞核中发挥非经典功能，但核功能的具体分子机制仍不清晰。

从TE调控角度，TPI1的高热度和非核主功能使其不适合作为本项目的TE调控候选。糖酵解酶的核定位常常是"被动扩散"效应（蛋白<40 kDa可通过NPC被动进入）而非主动核转运，糖酵解与TE调控的功能联系尚无理论框架支持。

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000111669-TPI1/subcellular

![](https://images.proteinatlas.org/50924/712_A10_1_red_green.jpg)
![](https://images.proteinatlas.org/50924/712_A10_2_red_green.jpg)
![](https://images.proteinatlas.org/50924/804_A10_1_red_green.jpg)
![](https://images.proteinatlas.org/50924/804_A10_3_red_green.jpg)
![](https://images.proteinatlas.org/50924/964_A10_1_red_green.jpg)
![](https://images.proteinatlas.org/50924/964_A10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
