---
type: centrosome-protein-evaluation
gene: "CEP85"
module: centrosome
status: centrosome_candidate
date: 2026-06-08
tags: [protein-scout, centrosome, evaluation]
---

# CEP85 — 中心体模块评估

## 1. 基本信息

- **基因:** CEP85
- **Ensembl:** ENSG00000130695
- **HPA 来源:** 中心体
- **HPA 抗体:** HPA028252
- **IF 可靠性:** Approved
- **PubMed 文献总数:** 10 篇

## 2. HPA 中心体 / 中心粒卫星证据

- **HPA 来源:** 中心体 ✓
- **HPA 链接:** https://www.proteinatlas.org/ENSG00000130695-CEP85
- **HPA 定位:** Nucleoli, Golgi apparatus, Vesicles
- **IF 图像状态:** 已获取 (1 张, selected)


<!-- CENTROSOME_HPA_IF_START -->
**HPA IF 图像（2026-06-08）**: HPA subcellular 页面存在可用 IF 图像。
HPA 定位: Nucleoli, Golgi apparatus, Vesicles。HPA IF 可靠性: approved。
来源: https://www.proteinatlas.org/ENSG00000130695-CEP85/subcellular

![](https://images.proteinatlas.org/28252/281_B3_2_selected.jpg)
<!-- CENTROSOME_HPA_IF_END -->


## 3. UniProt / GO-CC 中心体证据

*待 UniProt/GO-CC 完整采集。需人工审核。*

- 初步: HPA 标注支持 中心体 定位。

## 4. PubMed 文献证据

- **文献总数:** 10 篇
- **研究量评估:** 极低研究量
- 1. PMID 32107292: Direct interaction between CEP85 and STIL mediates PLK4-driven directed cell migration. (2020 Apr 23) *J Cell Sci*
2. PMID 30611117: Cep85 Relays Plk1 Activity to Phosphorylated Nek2A for Its Timely Activation in Centrosome Disjunction. (2019 Jan 25) *iScience*
3. PMID 41020723: Identification and validation of centrosome-related features predicting prognosis in hepatocellular carcinoma. (2025 Sep 29) *Comput Methods Biomech Biomed Engin*

## 5. AlphaFold / PAE / PDB / 结构域

pLDDT 数据可用 (UniProt: Q6P2H3)。PDB 模型: https://alphafold.ebi.ac.uk/files/AF-Q6P2H3-F1-model_v6.pdb

*InterPro: CC4_CEP85, Cep85/Cep85L*
*Pfam: CC4_CEP85*

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于 AlphaFold pLDDT 统计。

## 6. PPI / 蛋白互作网络

### STRING (人类, top 10)

| Partner | Combined Score | Experimental | Database | Textmining |
|---|---|---|---|
| CEP192 | 0.999 | 0.000 | 0.000 | 0.000 |
| CEP152 | 0.999 | 0.000 | 0.000 | 0.000 |
| STIL | 0.999 | 0.000 | 0.000 | 0.000 |
| CEP152 | 0.979 | 0.000 | 0.000 | 0.000 |
| CEP192 | 0.958 | 0.000 | 0.000 | 0.000 |
| CEP192 | 0.910 | 0.000 | 0.000 | 0.000 |
| SOX13 | 0.881 | 0.000 | 0.000 | 0.000 |
| OFD1 | 0.852 | 0.000 | 0.000 | 0.000 |
| RTTN | 0.850 | 0.000 | 0.000 | 0.000 |
| CEP192 | 0.847 | 0.000 | 0.000 | 0.000 |

*待 IntAct / BioGRID / humanPPI 补充。*

## 7. 中心体模块评分表

| 维度 | 评分 | 依据 |
|---|---:|---|
| 中心体证据 | 16/20 | HPA 标注 |
| PubMed/文献 | 10/20 | 10 篇文献 |
| PPI/互作网络 | 18/20 | STRING: 20p + 0 named |
| 结构/结构域 | 6/10 | AF 1 domains |
| 新颖性/特异性 | 10/10 | 极低研究量 |

- **最终评分:** **73/100**

## 8. 最终结论

**CENTROSOME CANDIDATE**

⚠️ *此为自动生成初步评估。UniProt/GO-CC、PDB/结构域、IntAct/BioGRID、关键文献等维度需人工补充完善。*

## 9. 人工复核备注

- HPA 来源: 中心体
- 抗体: HPA028252（IF 可靠性: Approved）
- 建议: 核实中心体 IF 文献定位
- 如 IF 图像质量不佳，检查 HPA 是否有替代抗体
