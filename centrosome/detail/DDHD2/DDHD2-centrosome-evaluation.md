---
type: centrosome-protein-evaluation
gene: "DDHD2"
module: centrosome
status: centrosome_candidate
date: 2026-06-08
tags: [protein-scout, centrosome, evaluation]
---

# DDHD2 — 中心体模块评估

## 1. 基本信息

- **基因:** DDHD2
- **Ensembl:** ENSG00000085788
- **HPA 来源:** 中心粒卫星
- **HPA 抗体:** CAB015202, HPA023143, HPA023147
- **IF 可靠性:** Supported
- **PubMed 文献总数:** 75 篇

## 2. HPA 中心体 / 中心粒卫星证据

- **HPA 来源:** 中心粒卫星 ✓
- **HPA 链接:** https://www.proteinatlas.org/ENSG00000085788-DDHD2
- **HPA 定位:** Centriolar satellite, Cytosol
- **IF 图像状态:** 已获取 (1 张, selected)


<!-- CENTROSOME_HPA_IF_START -->
**HPA IF 图像（2026-06-08）**: HPA subcellular 页面存在可用 IF 图像。
HPA 定位: Centriolar satellite, Cytosol。HPA IF 可靠性: supported。
来源: https://www.proteinatlas.org/ENSG00000085788-DDHD2/subcellular

![](https://images.proteinatlas.org/23147/194_H6_1_selected.jpg)
<!-- CENTROSOME_HPA_IF_END -->


## 3. UniProt / GO-CC 中心体证据

*待 UniProt/GO-CC 完整采集。需人工审核。*

- 初步: HPA 标注支持 中心粒卫星 定位。

## 4. PubMed 文献证据

- **文献总数:** 75 篇
- **研究量评估:** 较多文献
- *PubMed 文献待查询*

## 5. AlphaFold / PAE / PDB / 结构域

pLDDT 数据可用 (UniProt: O94830)。PDB 模型: https://alphafold.ebi.ac.uk/files/AF-O94830-F1-model_v6.pdb

*InterPro: DDHD_dom, PA-PLA1, SAM, SAM/pointed_sf, WWE_dom, WWE_SEC23-DDH2*
*Pfam: DDHD, SAM_1, WWE, WWE_3*

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于 AlphaFold pLDDT 统计。

## 6. PPI / 蛋白互作网络

### STRING (人类, top 10)

| Partner | Combined Score | Experimental | Database | Textmining |
|---|---|---|---|
| SPG11 | 0.949 | 0.000 | 0.000 | 0.000 |
| DDHD1 | 0.941 | 0.000 | 0.000 | 0.000 |
| PNPLA6 | 0.861 | 0.000 | 0.000 | 0.000 |
| PNPLA6 | 0.856 | 0.000 | 0.000 | 0.000 |
| LSM1 | 0.835 | 0.000 | 0.000 | 0.000 |
| ERLIN2 | 0.691 | 0.000 | 0.000 | 0.000 |
| PNPLA6 | 0.685 | 0.000 | 0.000 | 0.000 |
| PLPP5 | 0.653 | 0.000 | 0.000 | 0.000 |
| DDHD1 | 0.651 | 0.000 | 0.000 | 0.000 |
| ERLIN2 | 0.650 | 0.000 | 0.000 | 0.000 |

*待 IntAct / BioGRID / humanPPI 补充。*

## 7. 中心体模块评分表

| 维度 | 评分 | 依据 |
|---|---:|---|
| 中心体证据 | 14/20 | HPA 标注 |
| PubMed/文献 | 6/20 | 75 篇文献 |
| PPI/互作网络 | 18/20 | STRING: 20p + 0 named |
| 结构/结构域 | 6/10 | AF 1 domains |
| 新颖性/特异性 | 4/10 | 中等研究量 |

- **最终评分:** **59/100**

## 8. 最终结论

**CENTROSOME CANDIDATE**

⚠️ *此为自动生成初步评估。UniProt/GO-CC、PDB/结构域、IntAct/BioGRID、关键文献等维度需人工补充完善。*

## 9. 人工复核备注

- HPA 来源: 中心粒卫星
- 抗体: CAB015202, HPA023143, HPA023147（IF 可靠性: Supported）
- 建议: 核实中心体 IF 文献定位
- 如 IF 图像质量不佳，检查 HPA 是否有替代抗体
