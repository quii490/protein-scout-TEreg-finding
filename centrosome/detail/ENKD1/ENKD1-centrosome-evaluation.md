---
type: centrosome-protein-evaluation
gene: "ENKD1"
module: centrosome
status: centrosome_candidate
date: 2026-06-08
tags: [protein-scout, centrosome, evaluation]
---

# ENKD1 — 中心体模块评估

## 1. 基本信息

- **基因:** ENKD1
- **Ensembl:** ENSG00000124074
- **HPA 来源:** 中心体
- **HPA 抗体:** HPA041163, HPA041478
- **IF 可靠性:** Supported
- **PubMed 文献总数:** 12 篇

## 2. HPA 中心体 / 中心粒卫星证据

- **HPA 来源:** 中心体 ✓
- **HPA 链接:** https://www.proteinatlas.org/ENSG00000124074-ENKD1
- **HPA 定位:** Plasma membrane, Primary cilium, Centrosome
- **IF 图像状态:** 已获取 (1 张, selected)


<!-- CENTROSOME_HPA_IF_START -->
**HPA IF 图像（2026-06-08）**: HPA subcellular 页面存在可用 IF 图像。
HPA 定位: Plasma membrane, Primary cilium, Centrosome。HPA IF 可靠性: supported。
来源: https://www.proteinatlas.org/ENSG00000124074-ENKD1/subcellular

![](https://images.proteinatlas.org/41163/534_F8_2_selected.jpg)
<!-- CENTROSOME_HPA_IF_END -->


## 3. UniProt / GO-CC 中心体证据

*待 UniProt/GO-CC 完整采集。需人工审核。*

- 初步: HPA 标注支持 中心体 定位。

## 4. PubMed 文献证据

- **文献总数:** 12 篇
- **研究量评估:** 低研究量
- 1. PMID 35072334: ENKD1 is a centrosomal and ciliary microtubule-associated protein important for primary cilium content regulation. (2022 Jul) *FEBS J*
2. PMID 35301795: ENKD1 promotes CP110 removal through competing with CEP97 to initiate ciliogenesis. (2022 May 4) *EMBO Rep*
3. PMID 36960713: Upregulation of ENKD1 disrupts cellular homeostasis to promote lymphoma development. (2023 Jun) *J Cell Physiol*

## 5. AlphaFold / PAE / PDB / 结构域

pLDDT 数据可用 (UniProt: Q9H0I2)。PDB 模型: https://alphafold.ebi.ac.uk/files/AF-Q9H0I2-F1-model_v6.pdb

*InterPro: Enkurin_dom, Enkurin_domain-protein*
*Pfam: Enkurin*

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于 AlphaFold pLDDT 统计。

## 6. PPI / 蛋白互作网络

### STRING (人类, top 10)

| Partner | Combined Score | Experimental | Database | Textmining |
|---|---|---|---|
| GFOD2 | 0.760 | 0.000 | 0.000 | 0.000 |
| CLHC1 | 0.561 | 0.000 | 0.000 | 0.000 |
| TMEM129 | 0.560 | 0.000 | 0.000 | 0.000 |
| SCRN1 | 0.520 | 0.000 | 0.000 | 0.000 |
| CALY | 0.474 | 0.000 | 0.000 | 0.000 |
| ANKRD13D | 0.454 | 0.000 | 0.000 | 0.000 |
| C1orf35 | 0.439 | 0.000 | 0.000 | 0.000 |
| PNMA1 | 0.430 | 0.000 | 0.000 | 0.000 |
| SLC49A3 | 0.427 | 0.000 | 0.000 | 0.000 |
| STAC3 | 0.420 | 0.000 | 0.000 | 0.000 |

*待 IntAct / BioGRID / humanPPI 补充。*

## 7. 中心体模块评分表

| 维度 | 评分 | 依据 |
|---|---:|---|
| 中心体证据 | 16/20 | HPA 标注 |
| PubMed/文献 | 8/20 | 12 篇文献 |
| PPI/互作网络 | 12/20 | STRING: 20p + 0 named |
| 结构/结构域 | 6/10 | AF 1 domains |
| 新颖性/特异性 | 8/10 | 低研究量 |

- **最终评分:** **62/100**

## 8. 最终结论

**CENTROSOME CANDIDATE**

⚠️ *此为自动生成初步评估。UniProt/GO-CC、PDB/结构域、IntAct/BioGRID、关键文献等维度需人工补充完善。*

### 深度机制分析

ENKD1（346 aa, pLDDT=76.3, 评分62/100）是Enkurin结构域蛋白1，定位于中心体、初级纤毛基部和质膜（HPA supported）。其结构域包含Enkurin保守结构域（IPR027012、PF13864），属于Enkurin蛋白家族。ENKD1已被鉴定为中心体和纤毛微管相关蛋白（PMID:35072334），在纤毛发生中通过竞争CEP97促进CP110从母中心粒移除以启动纤毛轴丝延伸（PMID:35301795）。此外，ENKD1通过TRIM21介导的RUBCN降解抑制LC3相关吞噬和抗菌免疫（PMID:41187080），且HDAC6介导的ENKD1去乙酰化调控有丝分裂纺锤体行为（PMID:40155750）。

该蛋白的STRING互作网络以GFOD2（Combined Score=0.760）、CLHC1（0.561）、TMEM129（0.560）为主，IntAct实验互作包含CEP70（中心体蛋白70, 酵母双杂交验证, PMID:16189514）、DVL2（Dishevelled-2）以及多个PDZ蛋白（PDLIM7）和转录因子（TSC22D4、RBPMS）。DVL2是Wnt信号通路的核心组分，与中心体/纤毛基部的初级纤毛信号转导密切相关。

从TE调控角度，ENKD1主要通过纤毛/中心体通路与TE调控产生间接关联。初级纤毛是Hedgehog（Hh）和Wnt信号转导的关键细胞平台——Hh通路通过GLI转录因子调控多种靶基因，包括受ERV LTR调控的基因。ENKD1通过调节中心体CP110水平和纤毛发生，可能影响Hh信号在纤毛基质内的转导效率。然而，其TE调控潜力微弱：PubMed仅12篇（极低研究量）、Nucleoplasm定位为阴性（HPA:Plasma membrane/Centrosome/Primary cilium）、无直接染色质互作证据。评分62/100属于中等优先级候选，但定位决定其作为TE调控靶标的价值低于直接的核蛋白。

## 9. 人工复核备注

- HPA 来源: 中心体
- 抗体: HPA041163, HPA041478（IF 可靠性: Supported）
- 建议: 核实中心体 IF 文献定位
- 如 IF 图像质量不佳，检查 HPA 是否有替代抗体
