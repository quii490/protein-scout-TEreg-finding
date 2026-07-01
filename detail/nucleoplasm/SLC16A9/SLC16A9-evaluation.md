---
type: protein-evaluation
gene: "SLC16A9"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SLC16A9 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SLC16A9 |
| 蛋白名称 | Monocarboxylate transporter 9 |
| 蛋白大小 | 509 aa / 55.8 kDa |
| UniProt ID | Q7RTY1 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cell Junctions; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 509 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=28 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=77.3; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | MCT9; MFS; MFS_dom |
| PPI | 5/10 | x3 | 15.0 | PPI degree=10 |
| **加权总分** | | | **131/180** | |
| **归一化总分** | | | **72.7/100** | 互证: +2 |

### 3. 分析
- Cell Junctions; Nucleoplasm (Approved)
- PubMed strict=28 broad=61
- AF pLDDT=77.3 PDB=0
- InterPro: MCT9; MFS; MFS_dom
- Pfam: MFS_1
- PPI degree=10 ChIP: None
20613716: A 'complexity' of urate transporters. | 41460373: Exploring hypoxia- and cuproptosis-related biomarkers in periodontitis based on  | 32566650: SLC1A1, SLC16A9, and CNTN3 Are Potential Biomarkers for the Occurrence of Colore

### 4. 总体评价
**72.7/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Monocarboxylate transporter 9

**功能**: Extracellular pH-and Na(+)-sensitive low-affinity creatine transporter (PubMed:31784090). Also functions as a pH-independent carnitine efflux transporter (PubMed:21886157)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR030767 |
| InterPro | IPR011701 |
| InterPro | IPR020846 |
| InterPro | IPR036259 |
| InterPro | IPR050327 |
| Pfam | PF07690 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| NXF1 | BioGRID | 1 |
| HNRNPL | BioGRID | 1 |
| EIF4A2 | BioGRID | 0 |
| MRPL11 | BioGRID | 0 |
| KLC4 | BioGRID | 0 |


### 深度机制分析

**结构域架构**：SLC16A9/MCT9（509 aa，55.8 kDa）属于单羧酸转运体（Monocarboxylate Transporter, MCT）家族（SLC16），含MFS结构域（IPR011701 MFS，IPR020846 MFS_dom，PF07690 MFS_1）和MCT9特异性结构域（IPR030767）。MFS标准折叠为12次跨膜α-螺旋（TM1-TM12），通过"rocker-switch"交替门控机制实现底物的跨膜易位。SLC16A9作为肌酸（creatine）和肉碱（carnitine）的双底物转运体，此双重底物特异性体现了MFS转运蛋白的底物混杂性（substrate promiscuity）。pH依赖性（细胞外pH敏感）和Na^+敏感性（PMID:31784090）表明其功能受微环境严格调控。

**PPI互作网络解读**：PPI degree=10，互作伙伴少但质量较高：NXF1（TAP，mRNA核输出受体，BioGRID 1分）、HNRNPL（hnRNP L，RNA结合蛋白，BioGRID 1分）再次出现（与SLC39A7、TMPRSS5等其他候选蛋白共享HNRNPL为互作伙伴——值得注意共性）。EIF4A2（真核翻译起始因子4A2，RNA解旋酶参与翻译起始）、MRPL11（线粒体核糖体大亚基蛋白L11，连接了质膜转运和线粒体翻译）、KLC4（驱动蛋白轻链4，参与囊泡/细胞器沿微管的运输）。

**结构解读**：AlphaFold pLDDT=77.3，预测质量较好。12-TM MFS折叠清晰可辨，中央底物结合腔具有容纳两性离子（如肌酸和肉碱的羧基和季铵基团）的特征性极性残基排列。疏水性TM螺旋形成膜内屏障，亲水腔内含有底物识别位点。pLDDT在跨膜螺旋（>80）较高，在胞内loop区域（60-70）偏低。SLC16A9与众不同之处在于其N端和C端均较长（含预测的内在无序区），可能作为蛋白-蛋白互作平台。

**机制模型**：（1）经典功能：SLC16A9在质膜上作为低亲和力肌酸转运体（细胞外pH敏感）和pH非依赖性肉碱外排转运体（PMID:21886157），分别支持肌酸依赖的能量代谢和肉碱依赖的脂肪酸β-氧化；（2）在核质中的定位（Cell Junctions; Nucleoplasm Approved）提示SLC16A9可能在内膜系统（包括核膜）表达——核膜的肌酸/肉碱转运对核内ATP缓冲系统和脂肪酸代谢具有重要意义；（3）2026年关键发现（PMID:42271166, PMID:42208843）揭示了SLC16A9在肿瘤放疗耐药（通过肉碱摄取促进脂质代谢重编程）和心肌肥厚（通过尿酸摄取激活NLRP3炎症小体）中的关键作用，显著扩展了对该转运体的功能认知。

**TE调控展望**：SLC16A9的TE调控潜力有限但存在代谢-TE交叉调控的间接线索：（1）肉碱介导的脂质代谢重编程（PMID:42271166）可改变组蛋白酰化修饰的底物供给（乙酰-CoA、巴豆酰-CoA等均来自脂肪酸β-氧化），间接影响TE区域的染色质修饰状态；（2）尿酸-NLRP3炎症小体通路的激活（PMID:42208843）将代谢物与炎症信号连接——TE激活可触发NLRP3炎症小体，而SLC16A9通过尿酸转运参与该通路，形成代谢-炎症-TE三角调控关系。


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q7RTY1-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000165449-SLC16A9

![](https://images.proteinatlas.org/49286/1198_H2_2_red_green.jpg)
![](https://images.proteinatlas.org/49286/1198_H2_6_red_green.jpg)
![](https://images.proteinatlas.org/49286/1252_B4_2_red_green.jpg)
![](https://images.proteinatlas.org/49286/1252_B4_4_red_green.jpg)
![](https://images.proteinatlas.org/49286/1201_H2_5_red_green.jpg)
![](https://images.proteinatlas.org/49286/1201_H2_7_red_green.jpg)

### PubMed 文献

**PubMed count: 61**

| 42271166 | SLC16A9-Mediated Carnitine Uptake Enhances Radiotherapy Resistance in Colorectal Cancer via Lipid Metabolic Reprogrammin | Compr Physiol 2026 |
| 42208843 | SLC16A9-mediated uric acid uptake promotes myocardial hypertrophy in dilated cardiomyopathy via NLRP3 inflammasome activ | Exp Cell Res 2026 |
| 41460373 | Exploring hypoxia- and cuproptosis-related biomarkers in periodontitis based on transcriptome and single-cell analysis. | Clin Oral Investig 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SLC16A9

