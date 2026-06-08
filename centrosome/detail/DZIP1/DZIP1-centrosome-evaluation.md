---
type: centrosome-protein-evaluation
gene: "DZIP1"
module: centrosome
status: centrosome_candidate
date: 2026-06-08
tags: [protein-scout, centrosome, evaluation]
---

# DZIP1 — 中心体模块评估

## 1. 基本信息

- **基因:** DZIP1
- **Ensembl:** ENSG00000134874
- **HPA 来源:** 中心体
- **HPA 抗体:** HPA054891, HPA057272
- **IF 可靠性:** Supported
- **PubMed 文献总数:** 66 篇

## 2. HPA 中心体 / 中心粒卫星证据

- **HPA 来源:** 中心体 ✓
- **HPA 链接:** https://www.proteinatlas.org/ENSG00000134874-DZIP1
- **HPA 定位:** Nucleoplasm, Centrosome, Basal body
- **IF 图像状态:** 已获取 (1 张, selected)


<!-- CENTROSOME_HPA_IF_START -->
**HPA IF 图像（2026-06-08）**: HPA subcellular 页面存在可用 IF 图像。
HPA 定位: Nucleoplasm, Centrosome, Basal body。HPA IF 可靠性: supported。
来源: https://www.proteinatlas.org/ENSG00000134874-DZIP1/subcellular

![](https://images.proteinatlas.org/57272/2171_B9_120_selected.jpg)
<!-- CENTROSOME_HPA_IF_END -->


## 3. UniProt / GO-CC 中心体证据

*待 UniProt/GO-CC 完整采集。需人工审核。*

- 初步: HPA 标注支持 中心体 定位。

## 4. PubMed 文献证据

- **文献总数:** 66 篇
- **研究量评估:** 较多文献
- 1. PMID 39990491: Centrosome-assisted assembly of the Balbiani body. (2025 Feb 12) *bioRxiv*
2. PMID 32491167: Role of DZIP1-CBY-FAM92 transition zone complex in the basal body to membrane attachment and ciliary budding. (2020 Jun 30) *Biochem Soc Trans*
3. PMID 33811421: DZIP1 regulates mammalian cardiac valve development through a Cby1-β-catenin mechanism. (2021 Oct) *Dev Dyn*

## 5. AlphaFold / PAE / PDB / 结构域

pLDDT 数据可用 (UniProt: Q86YF9)。PDB 模型: https://alphafold.ebi.ac.uk/files/AF-Q86YF9-F1-model_v6.pdb

*InterPro: DZIP1_dom, DZIP1_N, DZIP_RILPL, Znf_C2H2_type*
*Pfam: Dzip-like_N, DZIP1*

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于 AlphaFold pLDDT 统计。

## 6. PPI / 蛋白互作网络

### STRING (人类, top 10)

| Partner | Combined Score | Experimental | Database | Textmining |
|---|---|---|---|
| CBY1 | 0.949 | 0.000 | 0.000 | 0.000 |
| DAZ1 | 0.944 | 0.000 | 0.000 | 0.000 |
| RAB8A | 0.871 | 0.000 | 0.000 | 0.000 |
| DZIP1 | 0.807 | 0.000 | 0.000 | 0.000 |
| HMMR | 0.773 | 0.000 | 0.000 | 0.000 |
| CBY1 | 0.752 | 0.000 | 0.000 | 0.000 |
| DAZ1 | 0.653 | 0.000 | 0.000 | 0.000 |
| CEP164 | 0.653 | 0.000 | 0.000 | 0.000 |
| PPP2R5A | 0.645 | 0.000 | 0.000 | 0.000 |
| TTC29 | 0.639 | 0.000 | 0.000 | 0.000 |

*待 IntAct / BioGRID / humanPPI 补充。*

## 7. 中心体模块评分表

| 维度 | 评分 | 依据 |
|---|---:|---|
| 中心体证据 | 16/20 | HPA 标注 |
| PubMed/文献 | 6/20 | 66 篇文献 |
| PPI/互作网络 | 18/20 | STRING: 20p + 0 named |
| 结构/结构域 | 6/10 | AF 1 domains |
| 新颖性/特异性 | 4/10 | 中等研究量 |

- **最终评分:** **62/100**

## 8. 最终结论

**CENTROSOME CANDIDATE**

⚠️ *此为自动生成初步评估。UniProt/GO-CC、PDB/结构域、IntAct/BioGRID、关键文献等维度需人工补充完善。*

## 9. 人工复核备注

- HPA 来源: 中心体
- 抗体: HPA054891, HPA057272（IF 可靠性: Supported）
- 建议: 核实中心体 IF 文献定位
- 如 IF 图像质量不佳，检查 HPA 是否有替代抗体
