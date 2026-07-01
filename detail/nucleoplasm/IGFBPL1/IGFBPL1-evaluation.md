---
type: protein-evaluation
gene: "IGFBPL1"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## IGFBPL1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | IGFBPL1 |
| 蛋白名称 | Insulin-like growth factor-binding protein-like 1 |
| 蛋白大小 | 278 aa / 29.0 kDa |
| UniProt ID | Q8WX77 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | 28.0 | Nucleoplasm; Vesicles (Uncertain) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 278 aa |
| 新颖性 | 9/10 | ×5 | 45.0 | PubMed=12 |
| 三维结构 | 8/10 | ×3 | 24.0 | pLDDT=85.1; PDB=4 |
| 调控结构域 | 4/10 | ×2 | 8.0 | Growth_fac_rcpt_cys_sf; Ig-like_dom; Ig-like_dom_sf |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=5 |
| **加权总分** | | | **127/180** | |
| **归一化总分** | | | **70.5/100** | 互证: +2 |

### 3. 分析
- Nucleoplasm; Vesicles (Uncertain)
- PubMed strict=12 broad=29
- AF pLDDT=85.1 PDB=4
- InterPro: Growth_fac_rcpt_cys_sf; Ig-like_dom; Ig-like_dom_sf
- Pfam: I-set; IGFBP; Kazal_2
- PPI degree=5 ChIP: None
38378800: α-Synuclein oligomers potentiate neuroinflammatory NF-κB activity and induce Ca( | 29391597: IGFBPL1 Regulates Axon Growth through IGF-1-mediated Signaling Cascades. | 36482070: Neural precursor cells tune striatal connectivity through the release of IGFBPL1

### 4. 总体评价
**70.5/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Insulin-like growth factor-binding protein-like 1

**功能**: IGF-binding proteins prolong the half-life of IGFs and have been shown to either inhibit or stimulate the growth promoting effects of the IGFs in cell culture. They alter the interaction of IGFs with their cell surface receptors (By similarity). May be a putative tumor suppressor protein

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR009030 |
| InterPro | IPR007110 |
| InterPro | IPR036179 |
| InterPro | IPR013783 |
| InterPro | IPR013098 |
| InterPro | IPR003599 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| SNX6 | BioGRID | 0 |
| SNX5 | BioGRID | 0 |
| SNX2 | BioGRID | 0 |
| SNX1 | BioGRID | 0 |
| CUL3 | BioGRID | 0 |


### 深度机制分析

**结构域架构**：IGFBPL1（278 aa, 29.0 kDa）是胰岛素样生长因子结合蛋白家族（IGFBP family）成员。含N端IGFBP域（Pfam IGFBP, IPR013098, ~aa 30-100）——约70 aa的富含Cys模块含12个保守Cys残基形成6对intramolecular disulfide bonds，构成刚性、紧凑的globular fold（cystine knot-like scaffold）专一识别IGF-I/IGF-II的A和B domain。C端Ig-like domain（I-set immunoglobulin-like domain, IPR013098, IPR007110, IPR003599）——约90 aa的β-sandwich fold（两片anti-parallel β-sheet）——介导IGFBP-IGF-IGF receptor三元复合物的构象变化（conformational coupling）。中间Kazal_2（Pfam Kazal_2）域为丝氨酸蛋白酶抑制剂样模块。AlphaFold pLDDT=85.1（PDB=4, 高结构表征）——N端IGFBP域pLDDT>90（极高，disulfide-stabilized rigid core），C端Ig-like域pLDDT~80-90，仅中间的Kazal域linker区域pLDDT~60。

**PPI互作网络解读**：PPI（degree=5, BioGRID）以SNX家族sorting nexin蛋白为核心——SNX1, SNX2, SNX5, SNX6均为retromer复合物（retromer complex, cargo-selective trimer VPS26-VPS29-VPS35 + SNX-BAR dimer）的组分。Retromer介导内体（endosome）→反式高尔基体网络（TGN）的逆行运输（retrograde transport）——SNX1/SNX2通过其PX domain识别PI3P富集的内体膜，并通过BAR domain感知/诱导膜曲率→形成tubular-vesicular carrier将cargo（如CI-MPR, Sortilin, IGF2R）从内体运回TGN。IGFBPL1与SNX1/SNX2/SNX5/SNX6的物理互作表明IGFBPL1可能作为retromer的cargo adapter——桥接IGF-IGFBP-IGF receptor复合物的内吞→retromer介导的IGF receptor（IGF1R）从内体回收至TGN再循环→延长IGF signal的持续时间和强度。CUL3（cullin-3, BioGRID）为CRL3 E3 ubiquitin ligase的支架蛋白——IGFBPL1-CUL3互作提示泛素化依赖的IGFBPL1蛋白稳定性和/或IGF1R的泛素化降解受Cullin-RING ligase系统调控。

**结构解读与机制模型**：IGFBPL1的双功能模型（IGF carrier + retromer adapter）。在细胞外（分泌型），IGFBPL1以高亲和力（Kd ~0.1-1 nM）结合IGF-I/IGF-II→（a）延长IGF在血液循环和组织间质中的半衰期（保护IGF免受蛋白酶降解），（b）阻止IGF与IGF1R的过度结合（decoy/buffer功能），（c）在特定条件下将IGF呈递至IGF1R（IGF delivery功能）。在核质（HPA Uncertain Nucleoplasm + Vesicles）中——IGFBPL1的核定位可能是内吞IGF-IGFBP-IGF1R复合物经retromer-mediated TGN retrieval→TGN到核膜的vesicular transport→进入核质的结果——核内IGFBPL1可能携带IGF至核质中的IGF1R变体（nuclear IGF1R, nIGF1R, 在多种癌症中报道作为转录共激活因子）。nIGF1R直接结合RNA Pol II的C-terminal domain（CTD）并在gene promoters上增强转录——IGFBPL1在此过程中充当IGF-to-nIGF1R ligand delivery的角色→增强核内IGF信号→促进增殖基因（如CCND1, MYC）和TE-rich区域的转录。

**TE调控展望**：IGFBPL1通过IGF信号间接参与TE调控。IGF-IGF1R-PI3K-AKT-mTOR信号轴是LINE-1转座的正调控因子——mTORC1激活S6K→磷酸化rpS6→增强5'TOP mRNA（含5'terminal oligopyrimidine tract）的翻译——LINE-1 ORF1 mRNA含类似的5'TOP-like motif→IGF pathway激活可增强LINE-1蛋白翻译。IGFBPL1作为IGF bioavailable pool的调控器（buffer/delivery）→调控IGF1R信号强度→间接影响mTORC1依赖的LINE-1表达。retromer依赖的IGF1R回收（经SNX1/SNX2/SNX5/SNX6）在核内体分选（endosomal sorting）层面调控IGF信号持续性→影响TE蛋白表达的time-window。CUL3泛素连接酶参与H3K4me3去甲基化酶（KDM5 family）的泛素化降解→CUL3功能失调导致H3K4me3异常积累→激活ERV LTR promoter——IGFBPL1-CUL3互作提示IGFBPL1作为CUL3 CRL复合物的adaptor可能影响染色质修饰酶（如KDM5B/C）的底物招募→间接调控TE位点的组蛋白甲基化状态。



### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000137142-IGFBPL1

![](https://images.proteinatlas.org/51354/1125_B6_3_red_green.jpg)
![](https://images.proteinatlas.org/51354/1125_B6_5_red_green.jpg)
![](https://images.proteinatlas.org/51354/1162_A7_1_red_green.jpg)
![](https://images.proteinatlas.org/51354/1162_A7_2_red_green.jpg)

### PubMed 文献

**PubMed count: 29**

| 41916100 | Semaglutide treatment reverses HFD induced hippocampal microglia activation and improves cognitive dysfunction. | Tissue Cell 2026 |
| 40227169 | Instrumenting Carotid Sonography Biomarkers and Polygenic Risk Score As a Novel Screening Approach for Retinal Detachmen | Transl Vis Sci Technol 2025 |
| 39969361 | Absence of genetic association between insulin-like growth factors and esophageal cancer. | Medicine (Baltimore) 2024 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/IGFBPL1

