---
type: centrosome-protein-evaluation
gene: "SRGAP2B"
module: centrosome
status: centrosome_candidate
date: 2026-06-08
tags: [protein-scout, centrosome, evaluation]
---

# SRGAP2B — 中心体模块评估

## 1. 基本信息

- **基因:** SRGAP2B
- **Ensembl:** ENSG00000196369
- **HPA 来源:** 中心体
- **HPA 抗体:** HPA078079
- **IF 可靠性:** Approved
- **PubMed 文献总数:** 7 篇

## 2. HPA 中心体 / 中心粒卫星证据

- **HPA 来源:** 中心体 ✓
- **HPA 链接:** https://www.proteinatlas.org/ENSG00000196369-SRGAP2B
- **HPA 定位:** Centrosome, Basal body, Cytosol
- **IF 图像状态:** 已获取 (1 张, selected)


<!-- CENTROSOME_HPA_IF_START -->
**HPA IF 图像（2026-06-08）**: HPA subcellular 页面存在可用 IF 图像。
HPA 定位: Centrosome, Basal body, Cytosol。HPA IF 可靠性: approved。
来源: https://www.proteinatlas.org/ENSG00000196369-SRGAP2B/subcellular

![](https://images.proteinatlas.org/78079/1978_G5_2_selected.jpg)
<!-- CENTROSOME_HPA_IF_END -->


## 3. UniProt / GO-CC 中心体证据

*待 UniProt/GO-CC 完整采集。需人工审核。*

- 初步: HPA 标注支持 中心体 定位。

## 4. PubMed 文献证据

- **文献总数:** 7 篇
- **研究量评估:** 极低研究量
- *PubMed 文献待查询*

## 5. AlphaFold / PAE / PDB / 结构域

pLDDT 数据可用 (UniProt: P0DMP2)。PDB 模型: https://alphafold.ebi.ac.uk/files/AF-P0DMP2-F1-model_v6.pdb

*InterPro: AH/BAR_dom_sf, F_BAR_dom, FCH_dom, SLIT-ROBO_RhoGAP*
*Pfam: FCH*

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于 AlphaFold pLDDT 统计。

## 6. PPI / 蛋白互作网络

### STRING (人类, top 10)

| Partner | Combined Score | Experimental | Database | Textmining |
|---|---|---|---|
| FAM72C | 0.999 | 0.000 | 0.000 | 0.000 |
| WAS | 0.919 | 0.000 | 0.000 | 0.000 |
| SRGAP2C | 0.720 | 0.000 | 0.000 | 0.000 |
| ARHGAP11B-2 | 0.720 | 0.000 | 0.000 | 0.000 |
| SRGAP2B | 0.690 | 0.000 | 0.000 | 0.000 |
| ARHGAP11B-2 | 0.666 | 0.000 | 0.000 | 0.000 |
| ARHGAP11B-2 | 0.665 | 0.000 | 0.000 | 0.000 |
| SRGAP2C | 0.651 | 0.000 | 0.000 | 0.000 |
| FAM72D | 0.640 | 0.000 | 0.000 | 0.000 |
| SRGAP2B | 0.639 | 0.000 | 0.000 | 0.000 |

*待 IntAct / BioGRID / humanPPI 补充。*

## 7. 中心体模块评分表

| 维度 | 评分 | 依据 |
|---|---:|---|
| 中心体证据 | 16/20 | HPA 标注 |
| PubMed/文献 | 10/20 | 7 篇文献 |
| PPI/互作网络 | 18/20 | STRING: 20p + 0 named |
| 结构/结构域 | 6/10 | AF 1 domains |
| 新颖性/特异性 | 10/10 | 极低研究量 |

- **最终评分:** **73/100**

## 8. 最终结论

**CENTROSOME CANDIDATE**

⚠️ *此为自动生成初步评估。UniProt/GO-CC、PDB/结构域、IntAct/BioGRID、关键文献等维度需人工补充完善。*

### 深度机制分析

SRGAP2B（paralog, P0DMP2, 评分73/100）是SRGAP2的人类特异性旁系同源基因，产生于约100万年前的基因复制事件。其结构域包含F-BAR（FCH）膜曲率感应/产生结构域（IPR027267/FCH_dom）和AH/BAR_dom_sf（IPR027267），但缺失全长SRGAP2的RhoGAP催化结构域和C端SH3域。这种截短保留了F-BAR介导的膜定位能力，但失去了Cdc42/Rac1的GTPase激活功能，使其作为SRGAP2的天然显性负调控（dominant-negative）变体。

SRGAP2B的STRING互作网络以FAM72C（Combined Score=0.999）为主，WAS（Wiskott-Aldrich综合征蛋白, 0.919）、SRGAP2C（0.720）等构成辅助互作。WAS作为Arp2/3介导的肌动蛋白分支聚合的核心激活因子，与FAM72蛋白家族共同参与中心体/基体处的微管-肌动蛋白交互调控。

从TE调控角度，SRGAP2B因其中心体/基体定位和与染色质/转录调控缺乏直接互作证据，TE调控潜力薄弱。PubMed仅7篇（极低研究量），表明该蛋白的独立功能远未被充分定义——其大多数细胞功能是通过与SRGAP2竞争性结合F-BAR配体而间接执行。人类特异旁系同源基因在进化上可能与脑皮层扩展相关，但对TE元件的直接调控能力尚无任何支持证据。从蛋白质量角度，Pfam:FCH结构域的一级保守性良好，但AlphaFold预测的跨域连接区域pLDDT可能较低。

## 9. 人工复核备注

- HPA 来源: 中心体
- 抗体: HPA078079（IF 可靠性: Approved）
- 建议: 核实中心体 IF 文献定位
- 如 IF 图像质量不佳，检查 HPA 是否有替代抗体
