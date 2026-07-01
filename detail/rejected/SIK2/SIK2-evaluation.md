---
type: protein-evaluation
gene: "SIK2"
date: 2026-05-30
tags: [protein-scout, rejected]
status: rejected
---

## SIK2 核蛋白评估报告（淘汰）

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | SIK2 |
| 蛋白名称 | salt inducible kinase 2 |
| UniProt ID | Q9H0K1 |
| 蛋白大小 | 926 aa |
| 核定位分数 | 4 |
| PubMed 总数 | 244 |
| 评估日期 | 2026-05-30 |

### 2. 淘汰原因

**淘汰类型**: PubMed 超过阈值

**详细理由**: PubMed 发表数 244 篇，超过 100 篇阈值，研究领域过于拥挤

#
HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

## 3. 关键数据

| 指标 | 数值 |
|------|------|
| PubMed 总数 (strict sum) | 244 |
| PubMed 最大值 | 132 |
| PubMed 近 5 年 | 89 |
| 核定位分数 (weighted max) | 4 |
| 核定位分级 | Tier1_conserved_high_confidence |
| Research hotness | 7.6894 |

### 深度机制分析

SIK2（盐诱导激酶2）属于AMPK相关激酶家族（AMPK-RK），是渗透应激和激素信号传导的丝氨酸/苏氨酸蛋白激酶（Q9H0K1）。其失活的主要原因为Pubmed文献达到244篇，远超100篇阈值。然而其核质定位信号（HPA approved）和激酶活性意味着SIK2的TE调控潜力仍需从机制层面加以评述。SIK2的域架构以N端激酶催化结构域为核心，其后为泛素相关结构域（UBA）和富含丝氨酸/天冬酰胺的C端调节区——但其UniProt域注释尚未在已检索的evaluation数据中完全展开。

SIK2的核心信号范式为：在基础状态下，SIK2被LKB1（STK11）在其T-loop的Thr175位点磷酸化激活；随后SIK2磷酸化CRTC2（CREB调节转录共激活因子2）和HDAC4/5，将这些转录调节因子扣押于胞质14-3-3结合位点，从而抑制CREB驱动的糖异生基因表达（肝脏）和MEF2驱动的肌特异性基因程序（肌肉）。在胰岛素信号刺激下，PKA通过磷酸化SIK2的抑制性位点阻断其活性，释放CRTC2核转位并激活血糖合成——这一负反馈环路构成了II型糖尿病代谢调控的核心机制。最近的研究（超过100篇文献的丰富库）进一步扩展了SIK2在脂肪细胞分化、黑色素生成、免疫细胞极化中的角色——但其功能均严格限定于胞质激酶信号传导。

PPI网络虽然未在淘汰报告中详细展开，但基于其激酶活性可合理推断其核心互作伙伴包括LKB1（上游激酶）、14-3-3蛋白（磷酸化底物结合平台）、CRTC1/2/3（直接磷酸化底物）、HDAC4/5/7（IIa类HDAC磷酸化靶标）以及PKA全酶（负反馈输入）。IntAct实验库中应有对应互作记录。

尽管HPA IF将SIK2定位于核质（approved），244篇文献的压倒性研究基础表明该蛋白的功能机制已高度饱和，不符合新颖性要求。其核定位可能仅代表CRTC2磷酸化后在核孔复合体附近的瞬时穿梭，而非构成性核居留功能。作为淘汰蛋白，SIK2的机制价值在于其激酶信号通路范式的完整性，而非TE调控的任何潜在贡献。

该基因不满足蛋白评估的基本筛选条件（PubMed ≤ 100 且核定位 > 3），予以淘汰。

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000170145-SIK2/subcellular

![](https://images.proteinatlas.org/71049/1891_I13_30_cr5bbddf6e02489_red_green.jpg)
![](https://images.proteinatlas.org/71049/1891_I13_8_cr5bbddf6e0153f_red_green.jpg)
![](https://images.proteinatlas.org/71049/1913_F19_31_red_green.jpg)
![](https://images.proteinatlas.org/71049/1913_F19_33_red_green.jpg)
![](https://images.proteinatlas.org/71049/1928_G12_1_red_green.jpg)
![](https://images.proteinatlas.org/71049/1928_G12_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
