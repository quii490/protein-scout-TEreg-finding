---
type: protein-evaluation
gene: "RLBP1"
date: 2026-05-30
tags: [protein-scout, rejected]
status: rejected
---

## RLBP1 核蛋白评估报告（淘汰）

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | RLBP1 |
| 蛋白名称 | retinaldehyde binding protein 1 |
| UniProt ID | P12271 |
| 蛋白大小 | 317 aa |
| 核定位分数 | 3 |
| PubMed 总数 | 193 |
| 评估日期 | 2026-05-30 |

### 2. 淘汰原因

**淘汰类型**: PubMed 超过阈值

**详细理由**: PubMed 发表数 193 篇，超过 100 篇阈值，研究领域过于拥挤

#
HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

## 3. 关键数据

| 指标 | 数值 |
|------|------|
| PubMed 总数 (strict sum) | 193 |
| PubMed 最大值 | 193 |
| PubMed 近 5 年 | 25 |
| 核定位分数 (weighted max) | 3 |
| 核定位分级 | Tier1_conserved_high_confidence |
| Research hotness | 3.5022 |

### 4. 结论

该基因不满足蛋白评估的基本筛选条件（PubMed ≤ 100 且核定位 > 3），予以淘汰。

### 深度机制分析

RLBP1（UniProt P12271）编码细胞视黄醛结合蛋白1（CRALBP），是视觉循环（visual cycle）中关键的11-顺式视黄醛载体蛋白。其结构核心为CRAL-TRIO脂质结合结构域——一个由约170个氨基酸组成的疏水口袋，采用特征性的sec14-like折叠（alpha/beta混合结构），能够以高亲和力（Kd约10 nM）和特异性结合11-顺式视黄醛和9-顺式视黄醛。CRALBP在视网膜色素上皮（RPE）细胞和Muller胶质细胞中高表达，负责将光异构化产生的全反式视黄醛转运至RPE65异构水解酶系统进行再异构化，并将再生形成的11-顺式视黄醛递送至视杆/视锥细胞的外节盘膜，维持光感受器的持续感光能力。

RLBP1的结构生物学已有充分研究：其apo形式和holo形式（11-顺式视黄醛结合态）的晶体结构揭示了配体结合诱导的构象变化——视黄醛的beta-紫罗兰酮环深埋于疏水口袋底部，而多烯链延伸至口袋入口附近，由保守的Trp和Phe残基通过pi-pi堆积稳定。Polyunsaturated脂肪酸侧链占据一个可变构象的次级口袋，为配体的进出提供结构基础。AlphaFold预测的高置信度与实验晶体结构的良好一致性确认了该蛋白折叠的可靠性。

HPA IF将RLBP1定位于Cytosol（胞质溶胶，supported），核定位分数仅为3，GO注释集中于视觉循环和维生素A代谢，缺乏任何核或染色质相关标注。PubMed文献数193篇（broad约300+）反映了RLBP1作为视网膜疾病核心基因的深度研究现状——其突变导致Bothnia型视网膜营养不良、rod-cone dystrophy和retinitis punctata albescens等多种遗传性视网膜病变，致病机制涉及11-顺式视黄醛供应中断引发的视杆细胞凋亡。

从TE调控筛选角度，RLBP1被淘汰的理由于两项硬指标：PubMed>100（研究热度过高）和核定位≤3（无核功能证据）。CRALBP作为一种高度特化的视黄醛转运蛋白，其功能完全限定在视觉循环的代谢框架内，缺乏任何已知的核/染色质相关功能或互作。将其作为TE调控靶标缺乏分子生物学基础——维生素A代谢物（视黄酸）虽通过RAR/RXR核受体调控基因表达，但这是由视黄醛脱氢酶（RALDH）介导的代谢反应，而非CRALBP的直接功能。

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000140522-RLBP1/subcellular

![](https://images.proteinatlas.org/44083/1361_A4_3_red_green.jpg)
![](https://images.proteinatlas.org/44083/1361_A4_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
