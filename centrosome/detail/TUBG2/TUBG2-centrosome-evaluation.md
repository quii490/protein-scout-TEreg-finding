---
type: centrosome-protein-evaluation
gene: "TUBG2"
module: centrosome
status: centrosome_candidate
date: 2026-06-08
tags: [protein-scout, centrosome, evaluation]
---

# TUBG2 — 中心体模块评估

## 1. 基本信息

- **基因:** TUBG2
- **Ensembl:** ENSG00000037042
- **HPA 来源:** 中心粒卫星
- **HPA 抗体:** CAB011495, HPA043012
- **IF 可靠性:** Supported
- **PubMed 文献总数:** 17 篇

## 2. HPA 中心体 / 中心粒卫星证据

- **HPA 来源:** 中心粒卫星 ✓
- **HPA 链接:** https://www.proteinatlas.org/ENSG00000037042-TUBG2
- **HPA 定位:** Centriolar satellite, Principal piece
- **IF 图像状态:** 已获取 (1 张, selected)


<!-- CENTROSOME_HPA_IF_START -->
**HPA IF 图像（2026-06-08）**: HPA subcellular 页面存在可用 IF 图像。
HPA 定位: Centriolar satellite, Principal piece。HPA IF 可靠性: supported。
来源: https://www.proteinatlas.org/ENSG00000037042-TUBG2/subcellular

![](https://images.proteinatlas.org/11495/638_A3_3_selected.jpg)
<!-- CENTROSOME_HPA_IF_END -->


## 3. UniProt / GO-CC 中心体证据

*待 UniProt/GO-CC 完整采集。需人工审核。*

- 初步: HPA 标注支持 中心粒卫星 定位。

## 4. PubMed 文献证据

- **文献总数:** 17 篇
- **研究量评估:** 低研究量
- 1. PMID 27015882: Human TUBG2 gene is expressed as two splice variant mRNA and involved in cell growth. (2016 Apr) *FEBS Lett*
2. PMID 22235350: γ-Tubulin 2 nucleates microtubules and is downregulated in mouse early embryogenesis. (2012) *PLoS One*
3. PMID 20162618: Differential expression and cellular distribution of gamma-tubulin and betaIII-tubulin in medulloblastomas and human medulloblastoma cell lines. (2010 May) *J Cell Physiol*

## 5. AlphaFold / PAE / PDB / 结构域

pLDDT 数据可用 (UniProt: Q9NRH3)。PDB 模型: https://alphafold.ebi.ac.uk/files/AF-Q9NRH3-F1-model_v6.pdb

*InterPro: Gamma_tubulin, Tub_FtsZ_C, Tubulin, Tubulin/FtsZ-like_C, Tubulin/FtsZ_2-layer-sand-dom, Tubulin/FtsZ_GTPase_sf, Tubulin_C, Tubulin_CS*
*Pfam: Tubulin, Tubulin_C*

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于 AlphaFold pLDDT 统计。

## 6. PPI / 蛋白互作网络

### STRING (人类, top 10)

| Partner | Combined Score | Experimental | Database | Textmining |
|---|---|---|---|
| TUBG1 | 0.999 | 0.000 | 0.000 | 0.000 |
| TUBGCP2 | 0.999 | 0.000 | 0.000 | 0.000 |
| TUBGCP3 | 0.999 | 0.000 | 0.000 | 0.000 |
| TUBGCP4 | 0.999 | 0.000 | 0.000 | 0.000 |
| MZT1 | 0.999 | 0.000 | 0.000 | 0.000 |
| TUBGCP5 | 0.999 | 0.000 | 0.000 | 0.000 |
| TUBGCP5 | 0.999 | 0.000 | 0.000 | 0.000 |
| TUBGCP4 | 0.999 | 0.000 | 0.000 | 0.000 |
| TUBGCP3 | 0.999 | 0.000 | 0.000 | 0.000 |
| TUBGCP2 | 0.999 | 0.000 | 0.000 | 0.000 |

*待 IntAct / BioGRID / humanPPI 补充。*

## 7. 中心体模块评分表

| 维度 | 评分 | 依据 |
|---|---:|---|
| 中心体证据 | 14/20 | HPA 标注 |
| PubMed/文献 | 8/20 | 17 篇文献 |
| PPI/互作网络 | 18/20 | STRING: 20p + 0 named |
| 结构/结构域 | 6/10 | AF 1 domains |
| 新颖性/特异性 | 8/10 | 低研究量 |

- **最终评分:** **65/100**

## 8. 最终结论

**CENTROSOME CANDIDATE**

⚠️ *此为自动生成初步评估。UniProt/GO-CC、PDB/结构域、IntAct/BioGRID、关键文献等维度需人工补充完善。*

## 9. 人工复核备注

- HPA 来源: 中心粒卫星
- 抗体: CAB011495, HPA043012（IF 可靠性: Supported）
- 建议: 核实中心体 IF 文献定位
- 如 IF 图像质量不佳，检查 HPA 是否有替代抗体
