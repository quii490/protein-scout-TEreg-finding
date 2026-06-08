---
type: centrosome-protein-evaluation
gene: "CYTH4"
module: centrosome
status: centrosome_candidate
date: 2026-06-08
tags: [protein-scout, centrosome, evaluation]
---

# CYTH4 — 中心体模块评估

## 1. 基本信息

- **基因:** CYTH4
- **Ensembl:** ENSG00000100055
- **HPA 来源:** 中心粒卫星
- **HPA 抗体:** HPA004065, HPA071573
- **IF 可靠性:** Supported
- **PubMed 文献总数:** 25 篇

## 2. HPA 中心体 / 中心粒卫星证据

- **HPA 来源:** 中心粒卫星 ✓
- **HPA 链接:** https://www.proteinatlas.org/ENSG00000100055-CYTH4
- **HPA 定位:** Plasma membrane, Cytokinetic bridge, Centriolar satellite
- **IF 图像状态:** 已获取 (1 张, selected)


<!-- CENTROSOME_HPA_IF_START -->
**HPA IF 图像（2026-06-08）**: HPA subcellular 页面存在可用 IF 图像。
HPA 定位: Plasma membrane, Cytokinetic bridge, Centriolar satellite。HPA IF 可靠性: supported。
来源: https://www.proteinatlas.org/ENSG00000100055-CYTH4/subcellular

![](https://images.proteinatlas.org/4065/1926_D3_2_selected.jpg)
<!-- CENTROSOME_HPA_IF_END -->


## 3. UniProt / GO-CC 中心体证据

*待 UniProt/GO-CC 完整采集。需人工审核。*

- 初步: HPA 标注支持 中心粒卫星 定位。

## 4. PubMed 文献证据

- **文献总数:** 25 篇
- **研究量评估:** 低研究量
- *PubMed 文献待查询*

## 5. AlphaFold / PAE / PDB / 结构域

pLDDT 数据可用 (UniProt: Q9UIA0)。PDB 模型: https://alphafold.ebi.ac.uk/files/AF-Q9UIA0-F1-model_v6.pdb

*InterPro: PH-like_dom_sf, PH_domain, Sec7_C_sf, Sec7_dom, Sec7_dom_sf*
*Pfam: PH, Sec7*

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于 AlphaFold pLDDT 统计。

## 6. PPI / 蛋白互作网络

### STRING (人类, top 10)

| Partner | Combined Score | Experimental | Database | Textmining |
|---|---|---|---|
| PIK3CD | 0.998 | 0.000 | 0.000 | 0.000 |
| PIK3CB | 0.998 | 0.000 | 0.000 | 0.000 |
| PIK3CB | 0.998 | 0.000 | 0.000 | 0.000 |
| PIK3CG | 0.997 | 0.000 | 0.000 | 0.000 |
| PIK3CB | 0.997 | 0.000 | 0.000 | 0.000 |
| PIK3CG | 0.994 | 0.000 | 0.000 | 0.000 |
| ARF6 | 0.983 | 0.000 | 0.000 | 0.000 |
| ARF1 | 0.983 | 0.000 | 0.000 | 0.000 |
| ARF1 | 0.916 | 0.000 | 0.000 | 0.000 |
| IPCEF1 | 0.784 | 0.000 | 0.000 | 0.000 |

*待 IntAct / BioGRID / humanPPI 补充。*

## 7. 中心体模块评分表

| 维度 | 评分 | 依据 |
|---|---:|---|
| 中心体证据 | 14/20 | HPA 标注 |
| PubMed/文献 | 8/20 | 25 篇文献 |
| PPI/互作网络 | 18/20 | STRING: 20p + 0 named |
| 结构/结构域 | 6/10 | AF 1 domains |
| 新颖性/特异性 | 8/10 | 低研究量 |

- **最终评分:** **65/100**

## 8. 最终结论

**CENTROSOME CANDIDATE**

⚠️ *此为自动生成初步评估。UniProt/GO-CC、PDB/结构域、IntAct/BioGRID、关键文献等维度需人工补充完善。*

## 9. 人工复核备注

- HPA 来源: 中心粒卫星
- 抗体: HPA004065, HPA071573（IF 可靠性: Supported）
- 建议: 核实中心体 IF 文献定位
- 如 IF 图像质量不佳，检查 HPA 是否有替代抗体
