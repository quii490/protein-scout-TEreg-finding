---
type: centrosome-protein-evaluation
gene: "MICALL1"
module: centrosome
status: centrosome_candidate
date: 2026-06-08
tags: [protein-scout, centrosome, evaluation]
---

# MICALL1 — 中心体模块评估

## 1. 基本信息

- **基因:** MICALL1
- **Ensembl:** ENSG00000100139
- **HPA 来源:** 中心粒卫星
- **HPA 抗体:** HPA043480, HPA051956
- **IF 可靠性:** Supported
- **PubMed 文献总数:** 54 篇

## 2. HPA 中心体 / 中心粒卫星证据

- **HPA 来源:** 中心粒卫星 ✓
- **HPA 链接:** https://www.proteinatlas.org/ENSG00000100139-MICALL1
- **HPA 定位:** Cell Junctions, Centriolar satellite, Cytosol
- **IF 图像状态:** 已获取 (1 张, selected)


<!-- CENTROSOME_HPA_IF_START -->
**HPA IF 图像（2026-06-08）**: HPA subcellular 页面存在可用 IF 图像。
HPA 定位: Cell Junctions, Centriolar satellite, Cytosol。HPA IF 可靠性: supported。
来源: https://www.proteinatlas.org/ENSG00000100139-MICALL1/subcellular

![](https://images.proteinatlas.org/43480/472_H6_1_selected.jpg)
<!-- CENTROSOME_HPA_IF_END -->


## 3. UniProt / GO-CC 中心体证据

*待 UniProt/GO-CC 完整采集。需人工审核。*

- 初步: HPA 标注支持 中心粒卫星 定位。

## 4. PubMed 文献证据

- **文献总数:** 54 篇
- **研究量评估:** 中等研究量
- 1. PMID 32143977: Endocytic membrane trafficking in the control of centrosome function. (2020 Aug) *Curr Opin Cell Biol*
2. PMID 31615969: MICAL-L1 coordinates ciliogenesis by recruiting EHD1 to the primary cilium. (2019 Nov 14) *J Cell Sci*
3. PMID 35510564: Differential requirements for the Eps15 homology domain proteins EHD4 and EHD2 in the regulation of mammalian ciliogenesis. (2022 Jul) *Traffic*

## 5. AlphaFold / PAE / PDB / 结构域

pLDDT 数据可用 (UniProt: Q8N3F8)。PDB 模型: https://alphafold.ebi.ac.uk/files/AF-Q8N3F8-F1-model_v6.pdb

*InterPro: bMERB_dom, CH_dom, CH_dom_sf, F-actin_Monoox_Mical, Znf_LIM*
*Pfam: bMERB_dom, CH, LIM*

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于 AlphaFold pLDDT 统计。

## 6. PPI / 蛋白互作网络

### STRING (人类, top 10)

| Partner | Combined Score | Experimental | Database | Textmining |
|---|---|---|---|
| EIF3K | 0.999 | 0.000 | 0.000 | 0.000 |
| EIF3E | 0.999 | 0.000 | 0.000 | 0.000 |
| EIF3M | 0.999 | 0.000 | 0.000 | 0.000 |
| EIF3M | 0.999 | 0.000 | 0.000 | 0.000 |
| EIF3K | 0.999 | 0.000 | 0.000 | 0.000 |
| EIF3M | 0.999 | 0.000 | 0.000 | 0.000 |
| EHD1 | 0.997 | 0.000 | 0.000 | 0.000 |
| FAU | 0.995 | 0.000 | 0.000 | 0.000 |
| FAU | 0.995 | 0.000 | 0.000 | 0.000 |
| FAU | 0.995 | 0.000 | 0.000 | 0.000 |

*待 IntAct / BioGRID / humanPPI 补充。*

## 7. 中心体模块评分表

| 维度 | 评分 | 依据 |
|---|---:|---|
| 中心体证据 | 14/20 | HPA 中心粒卫星标注。定位: Cell Junctions, Centriolar satellite, Cytosol |
| PubMed/文献 | 7/20 | 54 篇文献 |
| PPI/互作网络 | 15/20 | STRING 互作数据 |
| 结构/结构域 | 5/10 | 待结构数据采集 |
| 新颖性/特异性 | 6/10 | 中等研究量 |

- **最终评分:** **58/100**

## 8. 最终结论

**CENTROSOME CANDIDATE**

⚠️ *此为自动生成初步评估。UniProt/GO-CC、PDB/结构域、IntAct/BioGRID、关键文献等维度需人工补充完善。*

## 9. 人工复核备注

- HPA 来源: 中心粒卫星
- 抗体: HPA043480, HPA051956（IF 可靠性: Supported）
- 建议: 核实中心体 IF 文献定位
- 如 IF 图像质量不佳，检查 HPA 是否有替代抗体
