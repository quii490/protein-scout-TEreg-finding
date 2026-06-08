---
type: centrosome-protein-evaluation
gene: "MAP3K11"
module: centrosome
status: centrosome_candidate
date: 2026-06-08
tags: [protein-scout, centrosome, evaluation]
---

# MAP3K11 — 中心体模块评估

## 1. 基本信息

- **基因:** MAP3K11
- **Ensembl:** ENSG00000173327
- **HPA 来源:** 中心粒卫星
- **HPA 抗体:** CAB010165
- **IF 可靠性:** Supported
- **PubMed 文献总数:** 74 篇

## 2. HPA 中心体 / 中心粒卫星证据

- **HPA 来源:** 中心粒卫星 ✓
- **HPA 链接:** https://www.proteinatlas.org/ENSG00000173327-MAP3K11
- **HPA 定位:** Centriolar satellite, Cytosol
- **IF 图像状态:** 已获取 (1 张, selected)


<!-- CENTROSOME_HPA_IF_START -->
**HPA IF 图像（2026-06-08）**: HPA subcellular 页面存在可用 IF 图像。
HPA 定位: Centriolar satellite, Cytosol。HPA IF 可靠性: supported。
来源: https://www.proteinatlas.org/ENSG00000173327-MAP3K11/subcellular

![](https://images.proteinatlas.org/10165/970_H1_3_selected.jpg)
<!-- CENTROSOME_HPA_IF_END -->


## 3. UniProt / GO-CC 中心体证据

*待 UniProt/GO-CC 完整采集。需人工审核。*

- 初步: HPA 标注支持 中心粒卫星 定位。

## 4. PubMed 文献证据

- **文献总数:** 74 篇
- **研究量评估:** 较多文献
- 1. PMID 25091198: Emergence of structure through protein-protein interactions and pH changes in dually predicted coiled-coil and disordered regions of centrosomal proteins. (2014 Oct) *Biochim Biophys Acta*

## 5. AlphaFold / PAE / PDB / 结构域

pLDDT 数据可用 (UniProt: Q16584)。PDB 模型: https://alphafold.ebi.ac.uk/files/AF-Q16584-F1-model_v6.pdb

*InterPro: Kinase-like_dom_sf, MLK1-3_SH3, MLK1-4, Prot_kinase_dom, Protein_kinase_ATP_BS, Ser-Thr/Tyr_kinase_cat_dom, Ser/Thr_kinase_AS, Ser/Thr_Kinases-Pseudokinases*
*Pfam: PK_Tyr_Ser-Thr, SH3_9*

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于 AlphaFold pLDDT 统计。

## 6. PPI / 蛋白互作网络

### STRING (人类, top 10)

| Partner | Combined Score | Experimental | Database | Textmining |
|---|---|---|---|
| MAP2K7 | 0.999 | 0.000 | 0.000 | 0.000 |
| MAP2K7 | 0.997 | 0.000 | 0.000 | 0.000 |
| MAPK8IP2 | 0.996 | 0.000 | 0.000 | 0.000 |
| MAPK8IP3 | 0.994 | 0.000 | 0.000 | 0.000 |
| CDC42 | 0.993 | 0.000 | 0.000 | 0.000 |
| MAP3K11 | 0.992 | 0.000 | 0.000 | 0.000 |
| MAP2K7 | 0.985 | 0.000 | 0.000 | 0.000 |
| MAPK8IP2 | 0.985 | 0.000 | 0.000 | 0.000 |
| MAPK8IP3 | 0.984 | 0.000 | 0.000 | 0.000 |
| MAPK8IP3 | 0.966 | 0.000 | 0.000 | 0.000 |

*待 IntAct / BioGRID / humanPPI 补充。*

## 7. 中心体模块评分表

| 维度 | 评分 | 依据 |
|---|---:|---|
| 中心体证据 | 14/20 | HPA 标注 |
| PubMed/文献 | 6/20 | 74 篇文献 |
| PPI/互作网络 | 18/20 | STRING: 20p + 0 named |
| 结构/结构域 | 6/10 | AF 1 domains |
| 新颖性/特异性 | 4/10 | 中等研究量 |

- **最终评分:** **59/100**

## 8. 最终结论

**CENTROSOME CANDIDATE**

⚠️ *此为自动生成初步评估。UniProt/GO-CC、PDB/结构域、IntAct/BioGRID、关键文献等维度需人工补充完善。*

## 9. 人工复核备注

- HPA 来源: 中心粒卫星
- 抗体: CAB010165（IF 可靠性: Supported）
- 建议: 核实中心体 IF 文献定位
- 如 IF 图像质量不佳，检查 HPA 是否有替代抗体
