---
type: centrosome-protein-evaluation
gene: "SNTB2"
module: centrosome
status: centrosome_candidate
date: 2026-06-08
tags: [protein-scout, centrosome, evaluation]
---

# SNTB2 — 中心体模块评估

## 1. 基本信息

- **基因:** SNTB2
- **Ensembl:** ENSG00000168807
- **HPA 来源:** 中心粒卫星
- **HPA 抗体:** HPA001394
- **IF 可靠性:** Approved
- **PubMed 文献总数:** 15 篇

## 2. HPA 中心体 / 中心粒卫星证据

- **HPA 来源:** 中心粒卫星 ✓
- **HPA 链接:** https://www.proteinatlas.org/ENSG00000168807-SNTB2
- **HPA 定位:** Nucleoplasm, Golgi apparatus, Plasma membrane
- **IF 图像状态:** 已获取 (1 张, selected)


<!-- CENTROSOME_HPA_IF_START -->
**HPA IF 图像（2026-06-08）**: HPA subcellular 页面存在可用 IF 图像。
HPA 定位: Nucleoplasm, Golgi apparatus, Plasma membrane。HPA IF 可靠性: approved。
来源: https://www.proteinatlas.org/ENSG00000168807-SNTB2/subcellular

![](https://images.proteinatlas.org/1394/1183_H9_4_selected.jpg)
<!-- CENTROSOME_HPA_IF_END -->


## 3. UniProt / GO-CC 中心体证据

*待 UniProt/GO-CC 完整采集。需人工审核。*

- 初步: HPA 标注支持 中心粒卫星 定位。

## 4. PubMed 文献证据

- **文献总数:** 15 篇
- **研究量评估:** 低研究量
- *PubMed 文献待查询*

## 5. AlphaFold / PAE / PDB / 结构域

pLDDT 数据可用 (UniProt: Q13425)。PDB 模型: https://alphafold.ebi.ac.uk/files/AF-Q13425-F1-model_v6.pdb

*InterPro: PDZ, PDZ_sf, PH-like_dom_sf, PH_domain, PHsplit_syntrophin, Syntrophin, Syntrophin_4th*
*Pfam: PDZ, PH, PH_17, Syntrophin_4th*

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于 AlphaFold pLDDT 统计。

## 6. PPI / 蛋白互作网络

### STRING (人类, top 10)

| Partner | Combined Score | Experimental | Database | Textmining |
|---|---|---|---|
| DAG1 | 0.999 | 0.000 | 0.000 | 0.000 |
| DAG1 | 0.999 | 0.000 | 0.000 | 0.000 |
| DMD | 0.998 | 0.000 | 0.000 | 0.000 |
| SNTB1 | 0.996 | 0.000 | 0.000 | 0.000 |
| UTRN | 0.992 | 0.000 | 0.000 | 0.000 |
| DMD | 0.990 | 0.000 | 0.000 | 0.000 |
| UTRN | 0.990 | 0.000 | 0.000 | 0.000 |
| DTNA | 0.988 | 0.000 | 0.000 | 0.000 |
| DAG1 | 0.985 | 0.000 | 0.000 | 0.000 |
| DMD | 0.985 | 0.000 | 0.000 | 0.000 |

*待 IntAct / BioGRID / humanPPI 补充。*

## 7. 中心体模块评分表

| 维度 | 评分 | 依据 |
|---|---:|---|
| 中心体证据 | 14/20 | HPA 中心粒卫星标注。定位: Nucleoplasm, Golgi apparatus, Plasma membrane |
| PubMed/文献 | 8/20 | 15 篇文献 |
| PPI/互作网络 | 15/20 | STRING 互作数据 |
| 结构/结构域 | 5/10 | 待结构数据采集 |
| 新颖性/特异性 | 8/10 | 低研究量 |

- **最终评分:** **61/100**

## 8. 最终结论

**CENTROSOME CANDIDATE**

⚠️ *此为自动生成初步评估。UniProt/GO-CC、PDB/结构域、IntAct/BioGRID、关键文献等维度需人工补充完善。*

## 9. 人工复核备注

- HPA 来源: 中心粒卫星
- 抗体: HPA001394（IF 可靠性: Approved）
- 建议: 核实中心体 IF 文献定位
- 如 IF 图像质量不佳，检查 HPA 是否有替代抗体
