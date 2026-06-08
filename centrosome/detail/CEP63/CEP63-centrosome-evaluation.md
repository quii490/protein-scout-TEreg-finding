---
type: centrosome-protein-evaluation
gene: "CEP63"
module: centrosome
status: centrosome_candidate
date: 2026-06-08
tags: [protein-scout, centrosome, evaluation]
---

# CEP63 — 中心体模块评估

## 1. 基本信息

- **基因:** CEP63
- **Ensembl:** ENSG00000182923
- **HPA 来源:** 中心体
- **HPA 抗体:** HPA036264, HPA058154
- **IF 可靠性:** Supported
- **PubMed 文献总数:** 54 篇

## 2. HPA 中心体 / 中心粒卫星证据

- **HPA 来源:** 中心体 ✓
- **HPA 链接:** https://www.proteinatlas.org/ENSG00000182923-CEP63
- **HPA 定位:** Nucleoplasm, Centrosome, Basal body
- **IF 图像状态:** 未获取（已查询 HPA）


*HPA IF 图像未获取。已查询: https://www.proteinatlas.org/ENSG00000182923-CEP63/subcellular。HPA XML 中无可用 IF 图像 URL。*


## 3. UniProt / GO-CC 中心体证据

*待 UniProt/GO-CC 完整采集。需人工审核。*

- 初步: HPA 标注支持 中心体 定位。

## 4. PubMed 文献证据

- **文献总数:** 54 篇
- **研究量评估:** 中等研究量
- 1. PMID 32152252: Requirement of the Cep57-Cep63 Interaction for Proper Cep152 Recruitment and Centriole Duplication. (2020 Apr 28) *Mol Cell Biol*
2. PMID 23936128: Cep63 and cep152 cooperate to ensure centriole duplication. (2013) *PLoS One*
3. PMID 32503940: Cep57 and Cep57l1 function redundantly to recruit the Cep63-Cep152 complex for centriole biogenesis. (2020 Jul 3) *J Cell Sci*

## 5. AlphaFold / PAE / PDB / 结构域

pLDDT 数据可用 (UniProt: Q96MT8)。PDB 模型: https://alphafold.ebi.ac.uk/files/AF-Q96MT8-F1-model_v6.pdb

*InterPro: CEP63/Deup1_CC, CEP63/Deup1_N*
*Pfam: CC_CEP152-bind, CEP63*

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于 AlphaFold pLDDT 统计。

## 6. PPI / 蛋白互作网络

### STRING (人类, top 10)

| Partner | Combined Score | Experimental | Database | Textmining |
|---|---|---|---|
| CEP192 | 0.999 | 0.000 | 0.000 | 0.000 |
| CEP152 | 0.999 | 0.000 | 0.000 | 0.000 |
| CEP152 | 0.998 | 0.000 | 0.000 | 0.000 |
| PLK4 | 0.988 | 0.000 | 0.000 | 0.000 |
| CEP152 | 0.988 | 0.000 | 0.000 | 0.000 |
| CEP152 | 0.968 | 0.000 | 0.000 | 0.000 |
| CEP192 | 0.958 | 0.000 | 0.000 | 0.000 |
| PLK1 | 0.956 | 0.000 | 0.000 | 0.000 |
| CEP63 | 0.956 | 0.000 | 0.000 | 0.000 |
| CCDC14 | 0.953 | 0.000 | 0.000 | 0.000 |

*待 IntAct / BioGRID / humanPPI 补充。*

## 7. 中心体模块评分表

| 维度 | 评分 | 依据 |
|---|---:|---|
| 中心体证据 | 16/20 | HPA 标注 |
| PubMed/文献 | 7/20 | 54 篇文献 |
| PPI/互作网络 | 18/20 | STRING: 20p + 0 named |
| 结构/结构域 | 6/10 | AF 1 domains |
| 新颖性/特异性 | 6/10 | 中等研究量 |

- **最终评分:** **65/100**

## 8. 最终结论

**CENTROSOME CANDIDATE**

⚠️ *此为自动生成初步评估。UniProt/GO-CC、PDB/结构域、IntAct/BioGRID、关键文献等维度需人工补充完善。*

## 9. 人工复核备注

- HPA 来源: 中心体
- 抗体: HPA036264, HPA058154（IF 可靠性: Supported）
- 建议: 核实中心体 IF 文献定位
- 如 IF 图像质量不佳，检查 HPA 是否有替代抗体
