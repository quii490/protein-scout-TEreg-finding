---
type: centrosome-protein-evaluation
gene: "PCDHB15"
module: centrosome
status: centrosome_candidate
date: 2026-06-08
tags: [protein-scout, centrosome, evaluation]
---

# PCDHB15 — 中心体模块评估

## 1. 基本信息

- **基因:** PCDHB15
- **Ensembl:** ENSG00000113248
- **HPA 来源:** 中心体
- **HPA 抗体:** HPA007172, CAB026471
- **IF 可靠性:** Uncertain
- **PubMed 文献总数:** 5 篇

## 2. HPA 中心体 / 中心粒卫星证据

- **HPA 来源:** 中心体 ✓
- **HPA 链接:** https://www.proteinatlas.org/ENSG00000113248-PCDHB15
- **HPA 定位:** Nucleoplasm, Centrosome, Basal body
- **IF 图像状态:** 已获取 (1 张, selected)


<!-- CENTROSOME_HPA_IF_START -->
**HPA IF 图像（2026-06-08）**: HPA subcellular 页面存在可用 IF 图像。
HPA 定位: Nucleoplasm, Centrosome, Basal body。HPA IF 可靠性: uncertain。
来源: https://www.proteinatlas.org/ENSG00000113248-PCDHB15/subcellular

![](https://images.proteinatlas.org/7172/1364_E8_3_selected.jpg)
<!-- CENTROSOME_HPA_IF_END -->


## 3. UniProt / GO-CC 中心体证据

*待 UniProt/GO-CC 完整采集。需人工审核。*

- 初步: HPA 标注支持 中心体 定位。

## 4. PubMed 文献证据

- **文献总数:** 5 篇
- **研究量评估:** 极低研究量
- *PubMed 文献待查询*

## 5. AlphaFold / PAE / PDB / 结构域

pLDDT 数据可用 (UniProt: Q9Y5E8)。PDB 模型: https://alphafold.ebi.ac.uk/files/AF-Q9Y5E8-F1-model_v6.pdb

*InterPro: Cadherin-like_dom, Cadherin-like_sf, Cadherin_C, Cadherin_CS, Cadherin_N, Protocadherin/Cadherin-CA*
*Pfam: Cadherin, Cadherin_2, Cadherin_C_2*

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于 AlphaFold pLDDT 统计。

## 6. PPI / 蛋白互作网络

### STRING (人类, top 10)

| Partner | Combined Score | Experimental | Database | Textmining |
|---|---|---|---|
| *STRING 查询失败: <urlopen error EOF occurred in violation of protocol (_ssl.c:1129)>* | — | — | — | — |

*待 IntAct / BioGRID / humanPPI 补充。*

## 7. 中心体模块评分表

| 维度 | 评分 | 依据 |
|---|---:|---|
| 中心体证据 | 16/20 | HPA 标注 |
| PubMed/文献 | 10/20 | 5 篇文献 |
| PPI/互作网络 | 5/20 | 0 named interactors |
| 结构/结构域 | 6/10 | AF 1 domains |
| 新颖性/特异性 | 10/10 | 极低研究量 |

- **最终评分:** **58/100**

## 8. 最终结论

**CENTROSOME CANDIDATE**

### 深度机制分析

PCDHB15（Protocadherin beta 15, UniProt Q9Y5E8）是聚集型原钙黏蛋白β簇（Pcdh-β）成员——位于染色体5q31.3的Pcdh基因簇，包含15个串联排列的Pcdh-β基因（PCDHB1-B16, 其中B15最靠近3'端）。域架构为N端信号肽→6个钙黏蛋白重复域（Cadherin repeats, EC1-EC6, InterPro:Cadherin-like_dom/Cadherin-like_sf/Cadherin_C/Cadherin_CS/Cadherin_N, Pfam:Cadherin/Cadherin_2/Cadherin_C_2, SMART:cadherin domains）→单跨膜螺旋→短胞质尾（约30-40 aa）。每个黏蛋白重复域约110个残基——折叠为Greek-key β-sandwich，Ca2+离子桥接相邻重复域的连接区，维持刚性直线排列——使全长胞外域（约360 A）可延伸至细胞间隙。

HPA IF确认PCDHB15定位于Nucleoplasm、Centrosome和Basal body——这是极不典型的定位组合。经典原钙黏蛋白被认为定位于细胞表面/细胞连接，而PCDHB15的核质和中心体信号提示存在非细胞表面的PCDHB15功能池。Basal body定位暗示PCDHB15可能与纤毛发生（ciliogenesis）相关——原钙黏蛋白在纤毛膜中有表达先例（PCDH15在耳蜗毛细胞立体纤毛中）。HPA IF可靠性为Uncertain——使用的两个抗体（HPA007172, CAB026471）可能均存在脱靶结合问题。

Protein Atlas IF image: selected image for PCDHB15 shows Nucleoplasm signal.
STRING互作查询在评估时失败（SSL错误），PPI网络完全未知。PubMed仅5篇文献——极度低研究量。PCDHB15在TE调控中的潜力极为间接——作为细胞黏附分子，其核质/中心体的非经典定位若在体内被证实，可能暗示PCDHB15以ICD（intracellular domain）的可溶性裂解产物形式进入核内——类似Notch、cadherin和protocadherin的γ-分泌酶裂解产生转录活性ICD。但此假说完全未经检验。得分58/100主要受限于PPI数据完全缺失和HPA可靠性Uncertain。

⚠️ *此为自动生成初步评估。UniProt/GO-CC、PDB/结构域、IntAct/BioGRID、关键文献等维度需人工补充完善。*

## 9. 人工复核备注

- HPA 来源: 中心体
- 抗体: HPA007172, CAB026471（IF 可靠性: Uncertain）
- 建议: 核实中心体 IF 文献定位
- 如 IF 图像质量不佳，检查 HPA 是否有替代抗体
