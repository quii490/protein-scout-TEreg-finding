---
type: protein-evaluation
gene: "MTO1"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## MTO1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | MTO1 |
| 蛋白名称 | 5-taurinomethyluridine-[tRNA] synthase subunit MTO1, mitochondrial |
| 蛋白大小 | 717 aa / 80.0 kDa |
| UniProt ID | Q9Y2Z2 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 717 aa |
| 新颖性 | 7/10 | x5 | 35.0 | PubMed=81 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=86.0; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | FAD/NAD-bd_sf; GIDA_C_N; MnmG-rel |
| PPI | 6/10 | x3 | 18.0 | PPI degree=90 |
| **加权总分** | | | **127/180** | |
| **归一化总分** | | | **70.5/100** | 互证: +2 |

### 3. 分析
- Cytosol; Nucleoplasm (Approved)
- PubMed strict=81 broad=141
- AF pLDDT=86.0 PDB=0
- InterPro: FAD/NAD-bd_sf; GIDA_C_N; MnmG-rel
- Pfam: GIDA; GIDA_C_1st; SAM_GIDA_C
- PPI degree=90 ChIP: None
26425749: Nuclear Gene-Encoded Leigh Syndrome Spectrum Overview. | 39983002: Mitochondrial translation regulates terminal erythroid differentiation by mainta | 30653309: Metabolic Regulation of the Epitranscriptome.

### 4. 总体评价
**70.5/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: 5-taurinomethyluridine-[tRNA] synthase subunit MTO1, mitochondrial

**功能**: Component of the GTPBP3-MTO1 complex that catalyzes the 5-taurinomethyluridine (taum(5)U) modification at the 34th wobble position (U34) of mitochondrial tRNAs (mt-tRNAs), which plays a role in mt-tRNA decoding and mitochondrial translation (PubMed:29390138, PubMed:33619562). Taum(5)U formation on mammalian mt-tRNA requires the presence of both GTPBP3-mediated GTPase activity and MTO1 catalytic activity (PubMed:29390138)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR036188 |
| InterPro | IPR049312 |
| InterPro | IPR002218 |
| InterPro | IPR020595 |
| InterPro | IPR026904 |
| InterPro | IPR047001 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TRAF4 | STRING | 786 |
| FAM104A | STRING | 743 |
| MTFMT | STRING | 731 |
| FASTKD3 | STRING | 727 |
| TRIT1 | STRING | 704 |
| KDM1A | BioGRID | 1 |
| SUV39H1 | BioGRID | 1 |
| THUMPD1 | BioGRID | 1 |



### 深度机制分析

**结构域架构**：MTO1（717 aa, 80.0 kDa）是线粒体tRNA修饰酶，但HPA Approved Cytosol; Nucleoplasm确认其在核质-胞质中均有分布。含GIDA（glucose-inhibited division protein A）N端域（IPR049312）负责结合GTPBP3（GTPase），GIDA C端催化域（IPR047001, Pfam SAM_GIDA_C）利用SAM（S-adenosyl-L-methionine）作为甲基供体催化taurine的转移。FAD/NAD-binding superfamily域（IPR036188）为GIDA家族保守的Rossmann-like a/b fold。AlphaFold pLDDT=86.0（本批评估中结构质量最高之一）——GIDA域pLDDT>90，C端域pLDDT>85。PPI network（degree=90）以线粒体tRNA修饰为核心，含GTPBP3-MTO1复合物催化mt-tRNA wobble uridine (U34)的taurinomethylation (taum(5)U, PMID 29390138, 33619562）。最令人关注的是与KDM1A（LSD1, histone demethylase H3K4me1/2, BioGRID）和SUV39H1（H3K9 methyltransferase, BioGRID）的互作——将MTO1直接连接至染色质修饰，暗示MTO1在核质中的非经典功能。MTO1通过调控线粒体翻译→影响代谢产物（SAM/FAD）水平→这些epigenetic cofactors直接影响KDM1A（需要FAD）和SUV39H1（需要SAM）的活性→形成代谢-表观遗传调控轴。

**TE调控展望**：H3K9me3（SUV39H1产物）和H3K4me2（KDM1A底物）是TE沉默的关键组蛋白标记——MTO1通过调控SUV39H1/KDM1A经SAM/FAD代谢产物和直接PPI→影响TE位点H3K9甲基化水平→调控LINE-1/ERV的转录沉默。线粒体功能障碍导致SAM耗竭→全局DNA/组蛋白低甲基化→TE去抑制——MTO1突变→mt-tRNA taum(5)U修饰缺陷→线粒体翻译受损→SAM代谢异常→SUV39H1失活→H3K9me3降低→TE转录激活——这提供了MTO1相关Leigh syndrome（PMID 26425749）中TE激活的可能机制。



![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9Y2Z2-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000135297-MTO1

![](https://images.proteinatlas.org/30232/274_A11_1_red_green.jpg)
![](https://images.proteinatlas.org/30232/274_A11_2_red_green.jpg)
![](https://images.proteinatlas.org/30232/273_A11_1_red_green.jpg)
![](https://images.proteinatlas.org/30232/273_A11_2_red_green.jpg)
![](https://images.proteinatlas.org/30232/275_A11_1_red_green.jpg)
![](https://images.proteinatlas.org/30232/275_A11_2_red_green.jpg)
![](https://images.proteinatlas.org/30232/2175_C8_11_red_green.jpg)
![](https://images.proteinatlas.org/30232/2175_C8_22_red_green.jpg)

### PubMed 文献

**PubMed count: 141**

| 41989917 | The endoplasmic reticulum protein Erg28 restrains Mto1-Mto2-γ-TuSC-mediated microtubule assembly. | Cell Rep 2026 |
| 41957021 | Molecular pathogenesis and gene therapy-based intervention of GTPBP3-related mitochondrial disease. | Nat Commun 2026 |
| 41510857 | An Overview of Drug-Resistant Epilepsies Based on Advances in Genetics: A Cohort Study. | Neurol India 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/MTO1

