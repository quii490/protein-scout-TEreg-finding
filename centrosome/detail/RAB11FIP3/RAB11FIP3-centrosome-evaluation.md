---
type: centrosome-protein-evaluation
gene: "RAB11FIP3"
module: centrosome
status: centrosome_candidate
date: 2026-06-08
tags: [protein-scout, centrosome, evaluation]
---

# RAB11FIP3 — 中心体模块评估

## 1. 基本信息

- **基因:** RAB11FIP3
- **Ensembl:** ENSG00000090565
- **HPA 来源:** 中心粒卫星
- **HPA 抗体:** HPA028088, HPA028631, HPA030086
- **IF 可靠性:** Supported
- **PubMed 文献总数:** 53 篇

## 2. HPA 中心体 / 中心粒卫星证据

- **HPA 来源:** 中心粒卫星 ✓
- **HPA 链接:** https://www.proteinatlas.org/ENSG00000090565-RAB11FIP3
- **HPA 定位:** Vesicles, Cytokinetic bridge, Primary cilium
- **IF 图像状态:** 已获取 (1 张, selected)


<!-- CENTROSOME_HPA_IF_START -->
**HPA IF 图像（2026-06-08）**: HPA subcellular 页面存在可用 IF 图像。
HPA 定位: Vesicles, Cytokinetic bridge, Primary cilium。HPA IF 可靠性: supported。
来源: https://www.proteinatlas.org/ENSG00000090565-RAB11FIP3/subcellular

![](https://images.proteinatlas.org/28631/497_F7_2_selected.jpg)
<!-- CENTROSOME_HPA_IF_END -->


## 3. UniProt / GO-CC 中心体证据

*待 UniProt/GO-CC 完整采集。需人工审核。*

- 初步: HPA 标注支持 中心粒卫星 定位。

## 4. PubMed 文献证据

- **文献总数:** 53 篇
- **研究量评估:** 中等研究量
- 1. PMID 25673879: The Arf and Rab11 effector FIP3 acts synergistically with ASAP1 to direct Rabin8 in ciliary receptor targeting. (2015 Apr 1) *J Cell Sci*
2. PMID 30404838: An interaction network between the SNARE VAMP7 and Rab GTPases within a ciliary membrane-targeting complex. (2018 Dec 10) *J Cell Sci*
3. PMID 19327867: Rab11-FIP3 is a Rab11-binding protein that regulates breast cancer cell motility by modulating the actin cytoskeleton. (2009 Jun) *Eur J Cell Biol*

## 5. AlphaFold / PAE / PDB / 结构域

pLDDT 数据可用 (UniProt: O75154)。PDB 模型: https://alphafold.ebi.ac.uk/files/AF-O75154-F1-model_v6.pdb

*InterPro: EF-hand-dom_pair, EF_hand_dom, FIP-RBD_C_sf, Rab-bd_FIP-RBD, Rab11-FIP3/4_dom, Rab11-interacting_regulator*
*Pfam: EF-hand_7, Rab11-FIP3, RBD-FIP*

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于 AlphaFold pLDDT 统计。

## 6. PPI / 蛋白互作网络

### STRING (人类, top 10)

| Partner | Combined Score | Experimental | Database | Textmining |
|---|---|---|---|
| RAB11A | 0.999 | 0.000 | 0.000 | 0.000 |
| RAB11FIP2 | 0.999 | 0.000 | 0.000 | 0.000 |
| RAB11FIP1 | 0.999 | 0.000 | 0.000 | 0.000 |
| RAB3IP | 0.999 | 0.000 | 0.000 | 0.000 |
| RAB11FIP3 | 0.999 | 0.000 | 0.000 | 0.000 |
| RAB11FIP2 | 0.997 | 0.000 | 0.000 | 0.000 |
| ASAP1 | 0.991 | 0.000 | 0.000 | 0.000 |
| RAB11FIP4 | 0.990 | 0.000 | 0.000 | 0.000 |
| RAB3IP | 0.990 | 0.000 | 0.000 | 0.000 |
| ARF6 | 0.986 | 0.000 | 0.000 | 0.000 |

*待 IntAct / BioGRID / humanPPI 补充。*

## 7. 中心体模块评分表

| 维度 | 评分 | 依据 |
|---|---:|---|
| 中心体证据 | 14/20 | HPA 标注 |
| PubMed/文献 | 7/20 | 53 篇文献 |
| PPI/互作网络 | 18/20 | STRING: 20p + 0 named |
| 结构/结构域 | 6/10 | AF 1 domains |
| 新颖性/特异性 | 6/10 | 中等研究量 |

- **最终评分:** **62/100**

## 8. 最终结论

**CENTROSOME CANDIDATE**

⚠️ *此为自动生成初步评估。UniProt/GO-CC、PDB/结构域、IntAct/BioGRID、关键文献等维度需人工补充完善。*

## 9. 人工复核备注

- HPA 来源: 中心粒卫星
- 抗体: HPA028088, HPA028631, HPA030086（IF 可靠性: Supported）
- 建议: 核实中心体 IF 文献定位
- 如 IF 图像质量不佳，检查 HPA 是否有替代抗体
