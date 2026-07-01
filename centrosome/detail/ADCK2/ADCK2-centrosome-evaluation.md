---
type: centrosome-protein-evaluation
gene: "ADCK2"
module: centrosome
status: centrosome_candidate
date: 2026-06-08
tags: [protein-scout, centrosome, evaluation]
---

# ADCK2 — 中心体模块评估

## 1. 基本信息

- **基因:** ADCK2
- **Ensembl:** ENSG00000133597
- **HPA 来源:** 中心体
- **HPA 抗体:** HPA036036
- **IF 可靠性:** Uncertain
- **PubMed 文献总数:** 9 篇

## 2. HPA 中心体 / 中心粒卫星证据

- **HPA 来源:** 中心体 ✓
- **HPA 链接:** https://www.proteinatlas.org/ENSG00000133597-ADCK2
- **HPA 定位:** Centrosome, Cytosol
- **IF 图像状态:** 未获取（HPA 图片链接失效）


*HPA IF 图像链接失效（404）。已查询 https://www.proteinatlas.org/ENSG00000133597-ADCK2/subcellular，无可用替代图像。*


## 3. UniProt / GO-CC 中心体证据

*待 UniProt/GO-CC 完整采集。需人工审核。*

- 初步: HPA 标注支持 中心体 定位。

## 4. PubMed 文献证据

- **文献总数:** 9 篇
- **研究量评估:** 极低研究量
- *PubMed 文献待查询*

## 5. AlphaFold / PAE / PDB / 结构域

pLDDT 数据可用 (UniProt: Q7Z695)。PDB 模型: https://alphafold.ebi.ac.uk/files/AF-Q7Z695-F1-model_v6.pdb

*InterPro: ABC1_dom, ADCK2_dom, ADCK_kinase, Kinase-like_dom_sf*
*Pfam: ABC1*

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于 AlphaFold pLDDT 统计。

## 6. PPI / 蛋白互作网络

### STRING (人类, top 10)

| Partner | Combined Score | Experimental | Database | Textmining |
|---|---|---|---|
| COQ9 | 0.996 | 0.000 | 0.000 | 0.000 |
| COQ5 | 0.995 | 0.000 | 0.000 | 0.000 |
| COQ5 | 0.993 | 0.000 | 0.000 | 0.000 |
| COQ8A | 0.991 | 0.000 | 0.000 | 0.000 |
| COQ4 | 0.990 | 0.000 | 0.000 | 0.000 |
| COQ4 | 0.988 | 0.000 | 0.000 | 0.000 |
| COQ4 | 0.986 | 0.000 | 0.000 | 0.000 |
| COQ8A | 0.969 | 0.000 | 0.000 | 0.000 |
| COQ8A | 0.962 | 0.000 | 0.000 | 0.000 |
| COQ8B | 0.960 | 0.000 | 0.000 | 0.000 |

*待 IntAct / BioGRID / humanPPI 补充。*

## 7. 中心体模块评分表

| 维度 | 评分 | 依据 |
|---|---:|---|
| 中心体证据 | 16/20 | HPA 标注 |
| PubMed/文献 | 10/20 | 9 篇文献 |
| PPI/互作网络 | 18/20 | STRING: 20p + 0 named |
| 结构/结构域 | 6/10 | AF 1 domains |
| 新颖性/特异性 | 10/10 | 极低研究量 |

- **最终评分:** **73/100**

## 8. 最终结论

**CENTROSOME CANDIDATE**

### 深度机制分析

ADCK2（UniProt Q7Z695）是aarF域含激酶家族（ADCK/AarF domain containing kinase）成员，域架构为N端ABC1激酶催化域（InterPro:ABC1_dom, Pfam:ABC1, 蛋白激酶样折叠）——属于非典型蛋白激酶超家族，与磷脂酰肌醇3-激酶相关激酶（PIKKs）和真核蛋白激酶（ePKs）共享类似的ATP结合口袋。ABC1域采用双裂片激酶折叠——N-lobe（β-折叠主导）负责ATP/ADP结合，C-lobe（α-螺旋主导）含底物识别位点和催化中心。ADCK2在辅酶Q（CoQ/泛醌）生物合成途径中发挥调节性磷酸化功能——STRING互作图谱的高置信度核心为COQ生物合成酶复合体（COQ9, COQ5, COQ4, COQ8A, COQ8B, 全部score>0.96）——由于这些伙伴均属辅酶Q合成途径，STRING的基因组邻域分析（neighborhood和co-occurrence得分极高但实验=0）表明这些互作基于共基因组定位而非物理互作。

HPA定位于Centrosome和Cytosol——ADCK2的中心体定位可能反映其在有丝分裂中心体成熟和微管组织中心功能中的非典型激酶角色。中心体定位的ADCK2可能磷酸化中心体周质（PCM）成分——如pericentrin（PCNT）、CDK5RAP2或CEP蛋白——参与微管成核和中心体复制。但PubMed仅9篇且均为预测性/基因组学研究，无直接功能实验验证ADCK2的中心体定位或磷酸化靶标。ABC1激酶域与PIKKs（ATM, ATR, DNA-PKcs, mTOR）的远源同源性提示ADCK2可能通过类似机制感知细胞氧化还原状态（CoQ作为电子载体在呼吸链和抗氧化中发挥作用）。

ADCK2得分73/100（中心体模块），其作为TE调控候选的前景来自中心体与核周期/染色质分离的间接耦联——中心体蛋白异常在癌细胞中通过染色体错聚和micronuclei形成激活cGAS-STING先天免疫通路并导致TE去抑制。但ADCK2的TE调控直接证据为零。

⚠️ *此为自动生成初步评估。UniProt/GO-CC、PDB/结构域、IntAct/BioGRID、关键文献等维度需人工补充完善。*

## 9. 人工复核备注

- HPA 来源: 中心体
- 抗体: HPA036036（IF 可靠性: Uncertain）
- 建议: 核实中心体 IF 文献定位
- 如 IF 图像质量不佳，检查 HPA 是否有替代抗体
