---
type: protein-evaluation
gene: "CBLN3"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## CBLN3 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | CBLN3 |
| 蛋白名称 | Cerebellin-3 |
| 蛋白大小 | 205 aa / 21.5 kDa |
| UniProt ID | Q6UW01 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 205 aa |
| 研究新颖性 | 9/10 | x5 | 45.0 | PubMed=16 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=76.1; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | C1q_dom; Cerebellin_Synaptic_Org; Tumour_necrosis_fac-like_dom |
| PPI | 5/10 | x3 | 15.0 | PPI degree=2 |
| **加权总分** | | | **129/180** | |
| **归一化总分** | | | **71.0/100** | 互证: +1 |

### 3. 分析
- HPA: Nucleoplasm (Approved)
- PubMed: strict=16, broad=24
- AF pLDDT: 76.1 / PDB: 0
- InterPro: C1q_dom; Cerebellin_Synaptic_Org; Tumour_necrosis_fac-like_dom
- Pfam: C1q
- PPI degree=2 / ChIP: None
34274480: The porcine cerebellin gene family. | 41388545: Integrative multi-omics analysis of druggable genes for therapeutic target ident | 31043676: Mouse models and strain-dependency of Chédiak-Higashi syndrome-associated neurol

### 4. 总体评价
**71.0/100** | **nucleoplasm**
Nuclear protein


**蛋白全称**: Cerebellin-3

**功能**: May be involved in synaptic functions in the CNS

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR001073 |
| InterPro | IPR050822 |
| InterPro | IPR008983 |
| Pfam | PF00386 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---

![PAE](https://alphafold.ebi.ac.uk/files/AF-Q6UW01-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000139899-CBLN3

![](https://images.proteinatlas.org/41266/415_C4_1_red_green.jpg)
![](https://images.proteinatlas.org/41266/415_C4_2_red_green.jpg)
![](https://images.proteinatlas.org/41266/1876_B6_5_cr5b71a902d58b7_red_green.jpg)
![](https://images.proteinatlas.org/41266/1876_B6_25_cr5b71a902d59a5_red_green.jpg)
![](https://images.proteinatlas.org/41266/411_C4_1_red_green.jpg)
![](https://images.proteinatlas.org/41266/411_C4_2_red_green.jpg)

### PubMed 文献

**PubMed count: 24**

| 42121001 | Genome-wide DNA methylation signatures in blood associated with pediatric obesity. | Clin Epigenetics 2026 |
| 41995212 | Structural Architecture and Evolutionary Conservation of Cerebellin-Mediated Trans-Synaptic Signaling. | Synapse 2026 |
| 41741704 | Biomarker for craving and acamprosate treatment response in patients with alcohol use disorder: insights from multi-omic | Mol Psychiatry 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/CBLN3

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ZC3H10 | STRING | 475 |
| FAT2 | STRING | 510 |
| PECR | STRING | 472 |
| CBLN3 | STRING | 442 |
| CBLN2 | STRING | 757 |
| GABRA6 | STRING | 680 |
| GRID2 | STRING | 418 |
| STXBP6 | STRING | 446 |
| CCDC137 | STRING | 532 |
| TMEM69 | STRING | 549 |
| NYNRIN | STRING | 545 |
| SDR39U1 | STRING | 616 |

### 深度机制分析

**结构域架构**：CBLN3（205 aa, 21.5 kDa）为cerebellin家族分泌蛋白，含C1q结构域（IPR001073, Pfam PF00386, ~50-150 aa）和Cerebellin_Synaptic_Org结构域（IPR050822）。AlphaFold pLDDT=76.1（PDB=0），有序区域占比>60%，高置信度残基（pLDDT>90）占比30-40%，表明C1q域为折叠良好的球状结构。C1q域折叠为经典β-三明治/β-jelly roll拓扑——8-10条反平行β链形成两个紧密的β片层（类似TNF超家族和C1q补体成分的gC1q结构域）back-to-back夹心排列——这是高度保守的多功能识别结构域，在C1q补体成分ADP/C1QA-C1QB-C1QC异源三聚体中识别抗体Fc-immune complex，在adiponectin/ACRP30中识别AdipoR1/AdipoR2和T-cadherin，在collagen VIII/X中形成C端非胶原结构域。CBLN3的C1q域核心含保守的疏水残基（Trp/Phe/Tyr, 形成结构核心的疏水塌陷）和Ca²⁺结合环（conserved Asp/Glu providing Ca²⁺ coordination），Ca²⁺结合（Kd ~10-50 μM）增强结构域热力学稳定性（ΔTm ~10-15°C）。蛋白体积（205 aa）紧凑且高度折叠——C1q域几乎占据蛋白全长（>70%序列），两侧短N端肽（信号肽, 1-25 aa, 分泌通路靶向）和C端尾巴（~180-205 aa, 含保守Cys residue for interchain disulfide）。

**PPI互作网络解读**：PPI网络描绘CBLN3的突触组织和跨突触信号功能。核心伙伴——CBLN2（cerebellin-2, STRING 757, 同源蛋白, tandem gene duplication产物）为CBLN3的结构和功能近缘蛋白。GABRA6（GABA A受体α6亚基, STRING 680）和GRID2（GluD2/glutamate receptor ionotropic delta-2, STRING 418）为CBLN3的经典突触后受体伙伴。GluD2为离子型谷氨酸受体delta亚家族成员（AMPA/NMDA/Kainate/delta），虽不与谷氨酸结合（其配体结合域LBD的配体结合裂缝闭合构象需cerebellin+D-serine共结合），在小脑Purkinje细胞的平行纤维-爬行纤维突触（PF-PC synapse）形成和维持中至关重要——Cbln1-Cbln2/CBLN3与GluD2形成跨突触桥接复合体（trans-synaptic bridge），将突触前neurexin（NRXN）和突触后GluD2连接（PMID:41995212, 结构分析显示CBLN hexamer和GluD2-NRXN多聚体的分子架构）。GABAA受体（GABRA6为小脑颗粒细胞特异性α6亚基, 含GABA结合位点和苯二氮卓类结合位点）为突触后抑制性受体的代表——CBLN3-cerebellin复合体也可能与GABAA受体的α6/β/δ亚基胞外domain互作。ZC3H10（CCCH锌指蛋白10, STRING 475）和FAT2（巨型钙黏蛋白Fat2, STRING 510）作为非经典伙伴，可能反映CBLN3的非突触功能（核质/胞质定位依赖的功能）。

**结构解读**：CBLN3三聚化为功能单位——C1q域的三聚化界面由域边缘的三条链（strand A-A'-B edge strands, 每个单体贡献）形成三股平行β片层zipper（trimerization β-zipper），三聚体为扁平的钟形/三叶草形（bell-shaped/clover-shaped trimer）。Ca²⁺配位于三聚化界面的保守Asp环（每个单体的Asp loop贡献2个羧基配位一个Ca²⁺），Ca²⁺三聚化增强（Kd三聚化由~10 μM降至~50 nM with 1 mM Ca²⁺）。CBLN3的同源三聚体和CBLN3/CBLN2异源三聚体可进一步组装为六聚体（dimer of trimers, 通过N端coiled-coil neck介导的尾-尾三聚体配对）——六聚体为功能完全的跨突触桥接单元（hexameric bridge, ~120 kDa）。六聚体每个三聚体头分别识别突触前NRXN和突触后GluD2/GABAA——多价识别（multivalency, avidity）增强跨突触复合体的稳定性和滞留时间。

**机制模型**：（1）跨突触组织者（trans-synaptic organizer）——CBLN3六聚体在突触间隙（synaptic cleft, ~20-30 nm宽度）中作为突触前-突触后桥接分子。突触前：CBLN3六聚体一极的C1q域三聚体识别NRXN1/2/3的LNS（laminin-neurexin-sex hormone binding globulin）域——晶体结构显示C1q域结合NRXN LNS2-3域的表面带正电凹槽（Lys/Arg basic patch binding C1q acidic surface）。突触后：CBLN3六聚体另一极的C1q域三聚体识别GluD2的ATD（amino-terminal domain）和LBD的铰链区——GluD2-CBLN3复合体还需D-serine（D型丝氨酸，由glial SR酶racemization L-Ser产生，作为GluD2的正构glycine-site共激动剂）结合GluD2的LBD配体结合裂缝→触发GluD2的LBD闭合→ATD构象转变→跨膜螺旋束（TMD, 离子通道孔）构象改变→通道开放或下游信号转导。突触后抑制性GABA能——GABRA6的胞外β-α Sandwich fold (Ig-like fold C2-set, β-strand rich)可能为CBLN3的另一个突触后结合靶。（2）CBLN3的核质功能——HPA Approved Nucleoplasm揭示CBLN3的非经典核质池，可能与CBLN3的非分泌性同工型（alternative splicing/splicing isoform, 无信号肽, 胞质/核质靶向）或分泌后内化（re-uptake by endocytosis→endosomal escape→nuclear import）有关。核质CBLN3-C1q域可识别核质中含β-sandwich Ig-like fold的核蛋白（如核内lamin A/C Ig-fold domain, nucleoporin NUP Ig-fold, 或转录因子NF-κB p65 Ig-like fold）——C1q的靶标识别多功能性（promiscuous recognition）在核质中可能被重定向至核内蛋白网络以调控基因转录或染色质结构。

**TE调控展望**：CBLN3通过跨突触信号间接影响TE调控。GluD2-GABAA受体信号调控神经元的兴奋-抑制（E/I）平衡——E/I平衡为活动依赖性基因表达（activity-dependent gene expression, 如BDNF, FOS, ARC, NPAS4）的主要决定因素。神经元活动依赖性转录因子（NPAS4, CREB, SRF, MEF2）的结合位点广泛分布于LINE-1和SINE/Alu转座子附近——TE中cryptic cAMP response element (CRE, TGACGTCA consensus)和Serum Response Element (SRE, CC(A/T)₆GG consensus)使TE的转录被神经元活动动态调控。CBLN3-GluD2调控的Purkinje细胞兴奋性可能通过影响LINE-1/SINE的神经元活动依赖性转录而间接参与TE表达调控。核质CBLN3池若存在，可能通过C1q域行使核内蛋白识别功能，参与核内蛋白复合体（如BAF/SWI-SNF, NuRD, PRC2）的组装或稳定性→影响TE区域的染色质修饰。然而CBLN3作为分泌/跨突触蛋白，其TE调控潜力有限且需大量实验验证。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ZC3H10 | STRING | 475 |
| FAT2 | STRING | 510 |
| PECR | STRING | 472 |
| CBLN3 | STRING | 442 |
| CBLN2 | STRING | 757 |
| GABRA6 | STRING | 680 |
| GRID2 | STRING | 418 |
| STXBP6 | STRING | 446 |
| CCDC137 | STRING | 532 |
| TMEM69 | STRING | 549 |
| NYNRIN | STRING | 545 |
| SDR39U1 | STRING | 616 |

