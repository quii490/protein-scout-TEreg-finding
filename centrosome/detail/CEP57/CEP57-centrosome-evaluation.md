---
type: centrosome-protein-evaluation
gene: "CEP57"
module: centrosome
status: centrosome_candidate
date: 2026-06-08
tags: [protein-scout, centrosome, evaluation]
---

# CEP57 — 中心体模块评估

## 1. 基本信息

- **基因:** CEP57
- **Ensembl:** ENSG00000166037
- **HPA 来源:** 中心体+中心粒卫星
- **HPA 抗体:** HPA018315, HPA066403
- **IF 可靠性:** Supported
- **PubMed 文献总数:** 52 篇

## 2. HPA 中心体 / 中心粒卫星证据

- **HPA 来源:** 中心体+中心粒卫星 ✓
- **HPA 链接:** https://www.proteinatlas.org/ENSG00000166037-CEP57
- **HPA 定位:** Centriolar satellite, Centrosome, Cytosol
- **IF 图像状态:** 已获取 (1 张, selected)


<!-- CENTROSOME_HPA_IF_START -->
**HPA IF 图像（2026-06-08）**: HPA subcellular 页面存在可用 IF 图像。
HPA 定位: Centriolar satellite, Centrosome, Cytosol。HPA IF 可靠性: supported。
来源: https://www.proteinatlas.org/ENSG00000166037-CEP57/subcellular

![](https://images.proteinatlas.org/66403/2034_E1_4_selected.jpg)
<!-- CENTROSOME_HPA_IF_END -->


## 3. UniProt / GO-CC 中心体证据

*待 UniProt/GO-CC 完整采集。需人工审核。*

- 初步: HPA 标注支持 中心体+中心粒卫星 定位。

## 4. PubMed 文献证据

- **文献总数:** 52 篇
- **研究量评估:** 中等研究量
- 1. PMID 33492359: Cep57 and Cep57L1 maintain centriole engagement in interphase to ensure centriole duplication cycle. (2021 Mar 1) *J Cell Biol*
2. PMID 30804344: The Cep57-pericentrin module organizes PCM expansion and centriole engagement. (2019 Feb 25) *Nat Commun*
3. PMID 32503940: Cep57 and Cep57l1 function redundantly to recruit the Cep63-Cep152 complex for centriole biogenesis. (2020 Jul 3) *J Cell Sci*

## 5. AlphaFold / PAE / PDB / 结构域

pLDDT 数据可用 (UniProt: Q86XR8)。PDB 模型: https://alphafold.ebi.ac.uk/files/AF-Q86XR8-F1-model_v6.pdb

*InterPro: Centrosomal_MT-associated, Cep57_CLD, Cep57_MT-bd_dom*
*Pfam: Cep57_CLD, Cep57_MT_bd*

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于 AlphaFold pLDDT 统计。

## 6. PPI / 蛋白互作网络

### STRING (人类, top 10)

| Partner | Combined Score | Experimental | Database | Textmining |
|---|---|---|---|
| CEP152 | 0.999 | 0.000 | 0.000 | 0.000 |
| PLK1 | 0.999 | 0.000 | 0.000 | 0.000 |
| CEP152 | 0.998 | 0.000 | 0.000 | 0.000 |
| PLK1 | 0.956 | 0.000 | 0.000 | 0.000 |
| CEP63 | 0.956 | 0.000 | 0.000 | 0.000 |
| BUB1B | 0.935 | 0.000 | 0.000 | 0.000 |
| BUB1B | 0.928 | 0.000 | 0.000 | 0.000 |
| CEP63 | 0.902 | 0.000 | 0.000 | 0.000 |
| CEP152 | 0.882 | 0.000 | 0.000 | 0.000 |
| CEP63 | 0.874 | 0.000 | 0.000 | 0.000 |

*待 IntAct / BioGRID / humanPPI 补充。*

## 7. 中心体模块评分表

| 维度 | 评分 | 依据 |
|---|---:|---|
| 中心体证据 | 18/20 | HPA 标注 |
| PubMed/文献 | 7/20 | 52 篇文献 |
| PPI/互作网络 | 18/20 | STRING: 20p + 0 named |
| 结构/结构域 | 6/10 | AF 1 domains |
| 新颖性/特异性 | 6/10 | 中等研究量 |

- **最终评分:** **68/100**

## 8. 最终结论

**CENTROSOME CANDIDATE**

⚠️ *此为自动生成初步评估。UniProt/GO-CC、PDB/结构域、IntAct/BioGRID、关键文献等维度需人工补充完善。*

## 9. 人工复核备注

- HPA 来源: 中心体+中心粒卫星
- 抗体: HPA018315, HPA066403（IF 可靠性: Supported）
- 建议: 核实中心体 IF 文献定位
- 如 IF 图像质量不佳，检查 HPA 是否有替代抗体
