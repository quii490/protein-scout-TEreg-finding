---
type: centrosome-protein-evaluation
gene: "DNAL1"
module: centrosome
status: centrosome_candidate
date: 2026-06-08
tags: [protein-scout, centrosome, evaluation]
---

# DNAL1 — 中心体模块评估

## 1. 基本信息

- **基因:** DNAL1
- **Ensembl:** ENSG00000119661
- **HPA 来源:** 中心体+中心粒卫星
- **HPA 抗体:** HPA053129, HPA060974
- **IF 可靠性:** Approved
- **PubMed 文献总数:** 34 篇

## 2. HPA 中心体 / 中心粒卫星证据

- **HPA 来源:** 中心体+中心粒卫星 ✓
- **HPA 链接:** https://www.proteinatlas.org/ENSG00000119661-DNAL1
- **HPA 定位:** Nucleoplasm, Centriolar satellite, Centrosome
- **IF 图像状态:** 已获取 (1 张, selected)


<!-- CENTROSOME_HPA_IF_START -->
**HPA IF 图像（2026-06-08）**: HPA subcellular 页面存在可用 IF 图像。
HPA 定位: Nucleoplasm, Centriolar satellite, Centrosome。HPA IF 可靠性: approved。
来源: https://www.proteinatlas.org/ENSG00000119661-DNAL1/subcellular

![](https://images.proteinatlas.org/53129/2161_F8_8_selected.jpg)
<!-- CENTROSOME_HPA_IF_END -->


## 3. UniProt / GO-CC 中心体证据

*待 UniProt/GO-CC 完整采集。需人工审核。*

- 初步: HPA 标注支持 中心体+中心粒卫星 定位。

## 4. PubMed 文献证据

- **文献总数:** 34 篇
- **研究量评估:** 中等研究量
- 1. PMID 20301301: Primary Ciliary Dyskinesia. (1993) **
2. PMID 15845866: Identification and analysis of axonemal dynein light chain 1 in primary ciliary dyskinesia patients. (2005 Jul) *Am J Respir Cell Mol Biol*
3. PMID 39180133: Characterization of pathogenic genetic variants in Russian patients with primary ciliary dyskinesia using gene panel sequencing and transcript analysis. (2024 Aug 23) *Orphanet J Rare Dis*

## 5. AlphaFold / PAE / PDB / 结构域

pLDDT 数据可用 (UniProt: Q4LDG9)。PDB 模型: https://alphafold.ebi.ac.uk/files/AF-Q4LDG9-F1-model_v6.pdb

*InterPro: Leu-rich_rpt, Leu-rich_rpt_4, LRR_dom_sf*
*Pfam: LRR_4*

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于 AlphaFold pLDDT 统计。

## 6. PPI / 蛋白互作网络

### STRING (人类, top 10)

| Partner | Combined Score | Experimental | Database | Textmining |
|---|---|---|---|
| DNAI2 | 0.997 | 0.000 | 0.000 | 0.000 |
| DNAL1 | 0.979 | 0.000 | 0.000 | 0.000 |
| DNAL1 | 0.968 | 0.000 | 0.000 | 0.000 |
| CCDC114 | 0.965 | 0.000 | 0.000 | 0.000 |
| DNAI2 | 0.963 | 0.000 | 0.000 | 0.000 |
| DNAH2 | 0.960 | 0.000 | 0.000 | 0.000 |
| DNAH2 | 0.920 | 0.000 | 0.000 | 0.000 |
| MAP1LC3A | 0.914 | 0.000 | 0.000 | 0.000 |
| DNAH7 | 0.909 | 0.000 | 0.000 | 0.000 |
| DNAI2 | 0.903 | 0.000 | 0.000 | 0.000 |

*待 IntAct / BioGRID / humanPPI 补充。*

## 7. 中心体模块评分表

| 维度 | 评分 | 依据 |
|---|---:|---|
| 中心体证据 | 18/20 | HPA 双来源标注（中心体 + 中心粒卫星）。定位: Nucleoplasm, Centriolar satellite, Centrosome |
| PubMed/文献 | 7/20 | 34 篇文献 |
| PPI/互作网络 | 15/20 | STRING 互作数据 |
| 结构/结构域 | 5/10 | 待结构数据采集 |
| 新颖性/特异性 | 6/10 | 中等研究量 |

- **最终评分:** **64/100**

## 8. 最终结论

**CENTROSOME CANDIDATE**

⚠️ *此为自动生成初步评估。UniProt/GO-CC、PDB/结构域、IntAct/BioGRID、关键文献等维度需人工补充完善。*

## 9. 人工复核备注

- HPA 来源: 中心体+中心粒卫星
- 抗体: HPA053129, HPA060974（IF 可靠性: Approved）
- 建议: 核实中心体 IF 文献定位
- 如 IF 图像质量不佳，检查 HPA 是否有替代抗体
