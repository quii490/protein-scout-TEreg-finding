---
type: centrosome-protein-evaluation
gene: "CNTRL"
module: centrosome
status: centrosome_candidate
date: 2026-06-08
tags: [protein-scout, centrosome, evaluation]
---

# CNTRL — 中心体模块评估

## 1. 基本信息

- **基因:** CNTRL
- **Ensembl:** ENSG00000119397
- **HPA 来源:** 中心体+中心粒卫星
- **HPA 抗体:** HPA020468, HPA020480, HPA051583
- **IF 可靠性:** Supported
- **PubMed 文献总数:** 88 篇

## 2. HPA 中心体 / 中心粒卫星证据

- **HPA 来源:** 中心体+中心粒卫星 ✓
- **HPA 链接:** https://www.proteinatlas.org/ENSG00000119397-CNTRL
- **HPA 定位:** Golgi apparatus, Plasma membrane, Centriolar satellite
- **IF 图像状态:** 已获取 (1 张, selected)


<!-- CENTROSOME_HPA_IF_START -->
**HPA IF 图像（2026-06-08）**: HPA subcellular 页面存在可用 IF 图像。
HPA 定位: Golgi apparatus, Plasma membrane, Centriolar satellite。HPA IF 可靠性: supported。
来源: https://www.proteinatlas.org/ENSG00000119397-CNTRL/subcellular

![](https://images.proteinatlas.org/20468/2055_E1_4_selected.jpg)
<!-- CENTROSOME_HPA_IF_END -->


## 3. UniProt / GO-CC 中心体证据

*待 UniProt/GO-CC 完整采集。需人工审核。*

- 初步: HPA 标注支持 中心体+中心粒卫星 定位。

## 4. PubMed 文献证据

- **文献总数:** 88 篇
- **研究量评估:** 较多文献
- 1. PMID 16246720: Molecular links between centrosome and midbody. (2005 Oct 28) *Mol Cell*
2. PMID 41370122: Disruption of the centriolin/Cep110 gene (CNTRL) with CRISPR/Cas9 leads to cell cycle arrest and cell death of rhabdomyosarcoma cells in vitro. (2026 Feb 1) *Mol Biol Cell*
3. PMID 17140400: Hook2 localizes to the centrosome, binds directly to centriolin/CEP110 and contributes to centrosomal function. (2007 Jan) *Traffic*

## 5. AlphaFold / PAE / PDB / 结构域

pLDDT 数据可用 (UniProt: Q7Z7A1)。PDB 模型: https://alphafold.ebi.ac.uk/files/AF-Q7Z7A1-F1-model_v6.pdb

*InterPro: Leu-rich_rpt, Leu-rich_rpt_typical-subtyp, LRR_dom_sf, SDS22/Internalin_LRR*
*Pfam: LRR_9*

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于 AlphaFold pLDDT 统计。

## 6. PPI / 蛋白互作网络

### STRING (人类, top 10)

| Partner | Combined Score | Experimental | Database | Textmining |
|---|---|---|---|
| CEP128 | 0.992 | 0.000 | 0.000 | 0.000 |
| NIN | 0.992 | 0.000 | 0.000 | 0.000 |
| CNTRL | 0.984 | 0.000 | 0.000 | 0.000 |
| ODF2 | 0.983 | 0.000 | 0.000 | 0.000 |
| CCDC68 | 0.979 | 0.000 | 0.000 | 0.000 |
| NIN | 0.978 | 0.000 | 0.000 | 0.000 |
| CCDC120 | 0.976 | 0.000 | 0.000 | 0.000 |
| CCDC68 | 0.974 | 0.000 | 0.000 | 0.000 |
| CCDC120 | 0.972 | 0.000 | 0.000 | 0.000 |
| CCDC120 | 0.970 | 0.000 | 0.000 | 0.000 |

*待 IntAct / BioGRID / humanPPI 补充。*

## 7. 中心体模块评分表

| 维度 | 评分 | 依据 |
|---|---:|---|
| 中心体证据 | 18/20 | HPA 双来源标注（中心体 + 中心粒卫星）。定位: Golgi apparatus, Plasma membrane, Centriolar satellite |
| PubMed/文献 | 6/20 | 88 篇文献 |
| PPI/互作网络 | 15/20 | STRING 互作数据 |
| 结构/结构域 | 5/10 | 待结构数据采集 |
| 新颖性/特异性 | 4/10 | 较多文献 |

- **最终评分:** **61/100**

## 8. 最终结论

**CENTROSOME CANDIDATE**

⚠️ *此为自动生成初步评估。UniProt/GO-CC、PDB/结构域、IntAct/BioGRID、关键文献等维度需人工补充完善。*

## 9. 人工复核备注

- HPA 来源: 中心体+中心粒卫星
- 抗体: HPA020468, HPA020480, HPA051583（IF 可靠性: Supported）
- 建议: 核实中心体 IF 文献定位
- 如 IF 图像质量不佳，检查 HPA 是否有替代抗体
