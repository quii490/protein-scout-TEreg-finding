---
type: centrosome-protein-evaluation
gene: "RMDN1"
module: centrosome
status: centrosome_candidate
date: 2026-06-08
tags: [protein-scout, centrosome, evaluation]
---

# RMDN1 — 中心体模块评估

## 1. 基本信息

- **基因:** RMDN1
- **Ensembl:** ENSG00000176623
- **HPA 来源:** 中心体
- **HPA 抗体:** HPA026495
- **IF 可靠性:** Supported
- **PubMed 文献总数:** 7 篇

## 2. HPA 中心体 / 中心粒卫星证据

- **HPA 来源:** 中心体 ✓
- **HPA 链接:** https://www.proteinatlas.org/ENSG00000176623-RMDN1
- **HPA 定位:** Actin filaments, Centrosome
- **IF 图像状态:** 已获取 (1 张, selected)


<!-- CENTROSOME_HPA_IF_START -->
**HPA IF 图像（2026-06-08）**: HPA subcellular 页面存在可用 IF 图像。
HPA 定位: Actin filaments, Centrosome。HPA IF 可靠性: supported。
来源: https://www.proteinatlas.org/ENSG00000176623-RMDN1/subcellular

![](https://images.proteinatlas.org/26495/604_A1_2_selected.jpg)
<!-- CENTROSOME_HPA_IF_END -->


## 3. UniProt / GO-CC 中心体证据

*待 UniProt/GO-CC 完整采集。需人工审核。*

- 初步: HPA 标注支持 中心体 定位。

## 4. PubMed 文献证据

- **文献总数:** 7 篇
- **研究量评估:** 极低研究量
- *PubMed 文献待查询*

## 5. AlphaFold / PAE / PDB / 结构域

pLDDT 数据可用 (UniProt: Q96DB5)。PDB 模型: https://alphafold.ebi.ac.uk/files/AF-Q96DB5-F1-model_v6.pdb

*InterPro: RMD1-3_a_helical_rpt, TPR-like_helical_dom_sf*
*Pfam: RMD1-3*

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于 AlphaFold pLDDT 统计。

## 6. PPI / 蛋白互作网络

### STRING (人类, top 10)

| Partner | Combined Score | Experimental | Database | Textmining |
|---|---|---|---|
| ELOC | 0.908 | 0.000 | 0.000 | 0.000 |
| ELOC | 0.653 | 0.000 | 0.000 | 0.000 |
| RMDN1 | 0.645 | 0.000 | 0.000 | 0.000 |
| MRPL13 | 0.607 | 0.000 | 0.000 | 0.000 |
| RMDN1 | 0.592 | 0.000 | 0.000 | 0.000 |
| ELOC | 0.587 | 0.000 | 0.000 | 0.000 |
| RRS1 | 0.583 | 0.000 | 0.000 | 0.000 |
| RMDN1 | 0.554 | 0.000 | 0.000 | 0.000 |
| FAM91A1 | 0.549 | 0.000 | 0.000 | 0.000 |
| RMDN1 | 0.524 | 0.000 | 0.000 | 0.000 |

*待 IntAct / BioGRID / humanPPI 补充。*

## 7. 中心体模块评分表

| 维度 | 评分 | 依据 |
|---|---:|---|
| 中心体证据 | 16/20 | HPA 标注 |
| PubMed/文献 | 10/20 | 7 篇文献 |
| PPI/互作网络 | 12/20 | STRING: 20p + 0 named |
| 结构/结构域 | 6/10 | AF 1 domains |
| 新颖性/特异性 | 10/10 | 极低研究量 |

- **最终评分:** **66/100**

## 8. 最终结论

**CENTROSOME CANDIDATE**

### 深度机制分析

RMDN1（Regulator of microtubule dynamics 1, UniProt Q96DB5, 别名PTPIP51/RMD1/C1orf187）是微管动力学调控蛋白，域架构为N端RMD1-3串联重复域（InterPro:RMD1-3_a_helical_rpt, Pfam:RMD1-3/DUF2665）——该域由约三个α-螺旋repeat单元组成，形成TPR样（TetratricoPeptide Repeat-like）超螺旋束折叠（IPR011990/TPR-like_helical_dom_sf）。TPR样折叠通过α-螺旋堆积形成疏水沟槽——介导蛋白-蛋白互作，特别是识别Hsp90和Hsp70分子伴侣的C端EEVD基序。RMDN1是蛋白酪氨酸磷酸酶PTPIP51（Protein tyrosine phosphatase interacting protein 51）的互作蛋白——得名于此。

HPA IF确认RMDN1定位于Actin filaments和Centrosome（Supported）——支持的中心体定位（HPA抗体HPA026495, 可靠性Supported）是筛选为CENTROSOME CANDIDATE的关键依据。STRING互作图谱以ELOC/Elongin C（combined score=0.908）为核心——ELOC是转录延伸因子复合体（Elongin BC, 与RNA Pol II结合）和CRL E3泛素连接酶复合物（Cullin2/5-RING）的共享亚基。ELOC作为枢纽蛋白间接联系RMDN1与转录调控和蛋白降解。MRPL13（线粒体核糖体蛋白L13, score=0.607）和RRS1（核糖体生物发生因子, score=0.583）的关联提示RMDN1与翻译机器的潜在互作。FAM91A1（score=0.549）是高尔基体/内膜相关蛋白。

RMDN1在中心体的功能尚未被实验解析。RMD1-3域的TPR样折叠提示它可能作为分子伴侣平台——在中心体处协助微管蛋白（tubulin）二聚体组装至微管正端/+TIP复合物或协助中心粒复制/延伸因子的蛋白折叠。ELOC-STRT互作将RMDN1与CRL2 E3连接酶通路联系——从而可能参与中心体蛋白的泛素化降解。PubMed仅7篇——极度低研究量。Score=66/100（中心体模块）。RMDN1在TE调控中的潜力为零——作为微管/中心体蛋白，其功能完全定位于胞质微管网络组织。

⚠️ *此为自动生成初步评估。UniProt/GO-CC、PDB/结构域、IntAct/BioGRID、关键文献等维度需人工补充完善。*

## 9. 人工复核备注

- HPA 来源: 中心体
- 抗体: HPA026495（IF 可靠性: Supported）
- 建议: 核实中心体 IF 文献定位
- 如 IF 图像质量不佳，检查 HPA 是否有替代抗体
