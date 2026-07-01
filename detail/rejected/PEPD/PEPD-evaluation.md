---
type: protein-evaluation
gene: "PEPD"
date: 2026-05-30
tags: [protein-scout, rejected]
status: rejected
---

## PEPD 核蛋白评估报告（淘汰）

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | PEPD |
| 蛋白名称 | peptidase D |
| UniProt ID | P12955 |
| 蛋白大小 | 493 aa |
| 核定位分数 | 3 |
| PubMed 总数 | 685 |
| 评估日期 | 2026-05-30 |

### 2. 淘汰原因

**淘汰类型**: PubMed 超过阈值

**详细理由**: PubMed 发表数 685 篇，超过 100 篇阈值，研究领域过于拥挤

#
HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

## 3. 关键数据

| 指标 | 数值 |
|------|------|
| PubMed 总数 (strict sum) | 685 |
| PubMed 最大值 | 685 |
| PubMed 近 5 年 | 68 |
| 核定位分数 (weighted max) | 3 |
| 核定位分级 | Tier1_conserved_high_confidence |
| Research hotness | 4.2767 |

### 4. 结论

该基因不满足蛋白评估的基本筛选条件（PubMed ≤ 100 且核定位 > 3），予以淘汰。

### 深度机制分析

PEPD（493 aa）为脯氨酸肽酶（Prolidase/Xaa-Pro dipeptidase），属于M24金属肽酶家族。其结构域包含肽酶M24催化域（InterPro:IPR000994、IPR036005），催化Xaa-Pro二肽的水解以完成胶原蛋白降解循环的最后一步。PEPD定位于核质（Nucleoplasm, HPA approved），UniProt ID为P12955，活性依赖双核锰/锌金属中心。该酶的高底物特异性体现在其对C端脯氨酸残基的需求——只有游离的Xaa-Pro二肽才能进入活性位点裂隙。

核质定位的代谢酶"兼职"（moonlighting）现象日益受到关注。PEPD作为脯氨酸代谢的关键酶，其核内定位提示可能参与核内脯氨酸/羟脯氨酸池的调节。脯氨酸及羟脯氨酸是HIF-1α羟基化修饰的底物类似物——脯氨酰羟化酶（PHD）对HIF-1α的羟基化需要2-酮戊二酸和氧分子，而脯氨酸代谢产物的积累可竞争性反馈调控PHD活性，间接影响HIF-1α稳定性及下游低氧响应基因转录。

从TE调控角度，HIF-1α已被证实结合多种ERV LTR上的HRE（低氧响应元件）并激活转录。PEPD通过调节核内核苷酸/氨基酸代谢微环境，可能间接影响PHD催化效率和HIF通路活性，从而调控ERV的HIF依赖性转录。但该蛋白因PubMed发表数685篇（远超100篇阈值）已被淘汰，研究饱和度极高，TE调控潜力在已知维度上的拓展空间有限。

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000124299-PEPD/subcellular

![](https://images.proteinatlas.org/15599/1125_G2_1_red_green.jpg)
![](https://images.proteinatlas.org/15599/1125_G2_2_red_green.jpg)
![](https://images.proteinatlas.org/15599/1395_A10_4_red_green.jpg)
![](https://images.proteinatlas.org/15599/1395_A10_7_red_green.jpg)
![](https://images.proteinatlas.org/72045/1424_D6_3_red_green.jpg)
![](https://images.proteinatlas.org/72045/1424_D6_5_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
