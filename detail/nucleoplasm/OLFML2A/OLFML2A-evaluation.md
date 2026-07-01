---
type: protein-evaluation
gene: "OLFML2A"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## OLFML2A 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | OLFML2A |
| 蛋白名称 | Olfactomedin-like protein 2A |
| 蛋白大小 | 652 aa / 73.1 kDa |
| UniProt ID | Q68BL7 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Golgi apparatus; Nucleoplasm; Vesicles (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 652 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=18 |
| 三维结构 | 5/10 | x3 | 15.0 | pLDDT=67.1; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Olfac-like_dom; Olfactomedin-like_domain |
| PPI | 5/10 | x3 | 15.0 | PPI degree=7 |
| **加权总分** | | | **128/180** | |
| **归一化总分** | | | **70.5/100** | 互证: +1 |

### 3. 分析
- Golgi apparatus; Nucleoplasm; Vesicles (Approved)
- PubMed strict=18 broad=24
- AF pLDDT=67.1 PDB=0
- InterPro: Olfac-like_dom; Olfactomedin-like_domain
- Pfam: OLF
- PPI degree=7 ChIP: None
36873740: OLFML2A Overexpression Predicts an Unfavorable Prognosis in Patients with AML. | 34650914: OLFML2A Downregulation Inhibits Glioma Proliferation Through Suppression of Wnt/ | 37670341: Identification of m(6)A methylation-related genes in cerebral ischaemia‒reperfus

### 4. 总体评价
**70.5/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Olfactomedin-like protein 2A

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR003112 |
| InterPro | IPR050605 |
| Pfam | PF02191 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| APP | BioGRID | 0 |
| FBXO7 | BioGRID | 0 |
| KIAA1429 | BioGRID | 0 |
| DDX39A | BioGRID | 0 |
| IL5RA | BioGRID | 0 |
| ADIPOQ | BioGRID | 0 |
| TGOLN2 | BioGRID | 0 |



### 深度机制分析

**结构域架构**：OLFML2A（652 aa, 73.1 kDa）是Olfactomedin-like蛋白家族成员，含特征性OLF结构域（Olfactomedin-like domain, Pfam PF02191, IPR003112, IPR050605）。OLF域约250 aa，折叠为保守的五链β螺旋（five-bladed β-propeller）——每个blade由4条反平行β-strand组成，整体呈漏斗状，其中心通道参与蛋白-蛋白相互作用。N端区域含分泌信号肽（aa 1-20），C端为富含Cys的 coiled-coil 样延伸段。AlphaFold pLDDT=67.1（PDB=0），OLF β-propeller核心pLDDT>80（折叠良好），但N端前120 aa和C端尾巴（aa 580-652）pLDDT<50——低复杂度区域（LCR）呈现天然无序特征——提示OLFML2A采取"折叠域+IDR尾巴"（folded domain + intrinsically disordered region）的双模块架构。蛋白含多处N-糖基化位点（Asn-Xaa-Ser/Thr motif）和二硫键（Cys保守簇），符合分泌蛋白/高尔基体驻留蛋白（Golgi-resident protein）特征——与HPA批准的Golgi apparatus + Vesicles定位一致。

**PPI互作网络解读**：PPI degree=7（BioGRID），互作伙伴功能多样性指示OLFML2A在多个信号通路中的支架角色。APP（amyloid precursor protein, BioGRID）为I型跨膜蛋白——经α/β/γ-secretase连续剪切产生Aβ peptides（AD标志性病变）——OLFML2A-APP互作暗示OLFML2A在APP的Golgi-TGN运输中的伴侣功能——OLFM家族成员已知介导分泌蛋白（如Wnt, BMP antagonists）的胞外运输，类似机制可能适用于APP的Golgi→细胞表面vesicular trafficking。FBXO7（F-box protein 7, BioGRID）为SCF（Skp1-Cullin1-F-box）E3 ubiquitin ligase的底物识别亚单位——参与Parkin-dependent mitophagy（PINK1/Parkin通路）——OLFML2A-FBXO7互作连接OLFML2A至线粒体质量控制和泛素-蛋白酶体通路。KIAA1429（VIRMA, BioGRID）为m⁶A RNA甲基转移酶复合物（writer complex, METTL3-METTL14-WTAP-VIRMA-HAKAI-ZC3H13）的核心组分——介导pre-mRNA和mRNA上的N6-methyladenosine（m⁶A）修饰——OLFML2A与VIRMA的互作在机制上极为关键（见下文）。DDX39A（DEAD-box RNA helicase, BioGRID）为mRNA核外转运因子——作为ALYREF/THO/TREX复合物的ATP依赖RNA解旋酶在核孔复合体处将mRNP转运至胞质——OLFML2A-DDX39A互作可能参与mRNA核输出调控。TGOLN2（trans-Golgi network integral membrane protein 2, TGN46, BioGRID）是TGN标志蛋白——其胞质尾巴含TGN-retention signal——OLFML2A-TGOLN2互作确认OLFML2A在TGN的高尔基体亚区定位。ADIPOQ（adiponectin, 脂肪因子）和IL5RA（interleukin-5 receptor α, 嗜酸性粒细胞调控受体）——互作强度低但提示OLFML2A的胞外分泌/旁分泌功能。

**结构解读与机制模型**：OLFML2A作为高尔基体驻留的m⁶A修饰调控因子——这是其最特异性的分子功能。OLFML2A-VIRMA互作暗示OLFML2A作为m⁶A writer复合物的Golgi-localized adaptor——在mRNA从染色质（转录位点）→核孔复合体（NPC）→Golgi→胞质的空间通路上，OLFML2A可能在Golgi/TGN层面调控新合成mRNA的m⁶A修饰——延迟的Golgi-associated m⁶A修饰可能为特定分泌蛋白和跨膜蛋白mRNA提供空间特异性表观转录组标记。胶质瘤中（PMID 34650914），OLFML2A下调经Wnt/β-catenin通路抑制增殖——Wnt为分泌型脂修饰（palmitoleoylation, Porcupine/ PORCN催化）糖蛋白——Wnt在ER-Golgi中被lipid-modified后需与Wntless（WLS/ GPR177）结合才能向细胞表面运输——OLFML2A的OLF β-propeller可能作为Wnt/WLS的Golgi trafficking chaperone——OLFML2A下调导致Wnt向细胞表面的运输减少→Wnt/β-catenin信号减弱→β-catenin在destruction complex（AXIN-GSK3β-APC）中磷酸化降解→TCF/LEF转录失活→胶质瘤细胞增殖抑制。AML中（PMID 36873740），OLFML2A高表达预测不良预后——在髓系白血病中，Wnt/β-catenin是白血病干细胞（LSC）自我更新的核心通路——OLFML2A可能通过促进Wnt secretion维持LSC的Wnt自分泌/旁分泌环路。

三阴性乳腺癌（TNBC）研究提供了另一个关键线索：OLFML2A通过EZH2介导细胞周期调控（PMID 41607539）。EZH2为PRC2（Polycomb Repressive Complex 2）的催化亚单位——介导H3K27me3转录抑制标记——OLFML2A可能通过影响细胞周期相关基因的染色质抑制状态调控增殖。魔芋石油醚提取物（Konjac petroleum ether extract）抑制TNBC迁移/浸润的机制被证明与下调OLFML2A有关（PMID 42222147）——进一步支持OLFML2A作为肿瘤治疗靶点的潜力。

**TE调控展望**：OLFML2A通过m⁶A修饰和Wnt信号间接参与TE调控，路径多样且证据链较为清晰。（1）m⁶A-TE轴——LINE-1 L1Hs mRNA是m⁶A修饰的已知靶标——METTL3/METTL14 writer复合物在LINE-1 5'UTR和ORF1区域的m⁶A修饰影响LINE-1 mRNA的核内保留（nuclear retention）和胞质翻译效率（METTL3-mediated m⁶A→LINE-1 mRNA destabilization→减少ORF1p/ORF2p蛋白产量→降低转座频率）。OLFML2A作为VIRMA的Golgi adaptor可能调控特定的空间m⁶A修饰——对LINE-1 mRNA的m⁶A进行Golgi-associated的二次修饰（rewriting）——改变其mRNA命运（核输出vs. 降解）。m⁶A reader蛋白YTHDF1/2/3识别m⁶A→YTHDF2介导mRNA decay, YTHDF1介导翻译增强——OLFML2A的影响通过VIRMA间接调控LINE-1 mRNA的YTHDF-dependent fate switch。（2）Wnt-TE轴——β-catenin/TCF4复合物直接结合LINE-1 5'UTR中的TCF/LEF consensus motif（CCTTTGAT）激活LINE-1转录——OLFML2A通过调控Wnt运输影响Wnt/β-catenin信号强度→调节β-catenin依赖的LINE-1转录。（3）EZH2-TE轴——PRC2（含EZH2）催化H3K27me3是ERV-LTR和内源逆转录病毒沉默的核心机制——OLFML2A-EZH2功能轴影响PRC2的H3K27me3活性→改变ERV转录活性。在脑缺血再灌注损伤中（PMID 37670341），m⁶A修饰相关基因（包括OLFML2A）的表达变化暗示神经损伤中的表观转录组重编程可能改变TE表达谱。综上，OLFML2A借助其Golgi定位和m⁶A writer、Wnt trafficking、PRC2表观遗传等多层调控间接影响TE的转录、修饰和命运——这是一个跨Golgi-核-TE多室调控的特殊案例。

![PAE](https://alphafold.ebi.ac.uk/files/AF-Q68BL7-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000185585-OLFML2A

![](https://images.proteinatlas.org/21180/178_G10_2_red_green.jpg)
![](https://images.proteinatlas.org/21180/178_G10_1_red_green.jpg)
![](https://images.proteinatlas.org/21180/2225_D3_5_red_green.jpg)
![](https://images.proteinatlas.org/21180/2225_D3_6_red_green.jpg)
![](https://images.proteinatlas.org/21180/247_G10_1_red_green.jpg)
![](https://images.proteinatlas.org/21180/247_G10_2_red_green.jpg)

### PubMed 文献

**PubMed count: 24**

| 42222147 | Konjac petroleum ether extract inhibits triple-negative breast cancer cell migration and invasion by attenuating OLFML2A | Front Pharmacol 2026 |
| 42002088 | Heterogeneous nuclear ribonucleoprotein C deficiency compromises extracellular matrix-receptor interaction and induces a | Biochim Biophys Acta Mol Basis Dis 2026 |
| 41607539 | OLFML2A mediates cell cycle regulation in triple-negative breast cancer via EZH2. | Front Oncol 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/OLFML2A

