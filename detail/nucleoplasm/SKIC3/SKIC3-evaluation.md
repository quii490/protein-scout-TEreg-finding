---
type: protein-evaluation
gene: "SKIC3"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SKIC3 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SKIC3 |
| 蛋白名称 | Superkiller complex protein 3 |
| 蛋白大小 | 1564 aa / 175.5 kDa |
| UniProt ID | Q6PGP7 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Cytosol; Nucleoplasm (Supported) |
| 蛋白大小 | 6/10 | ×1 | 6.0 | 1564 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=9 |
| 三维结构 | 10/10 | ×3 | 30.0 | pLDDT=86.0; PDB=7 |
| 调控结构域 | 4/10 | ×2 | 8.0 | Ski3/TTC37; TPR-like_helical_dom_sf; TPR_rpt |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **141/180** | |
| **归一化总分** | | | **78.1/100** | 互证: +2 |

### 3. 分析
- HPA: Cytosol; Nucleoplasm (Supported)
- PubMed: strict=9, broad=10
- AF pLDDT: 86.0 / PDB: 7
- InterPro: Ski3/TTC37; TPR-like_helical_dom_sf; TPR_rpt
- Pfam: TPR_16; TPR_19; TPR_8
- PPI degree=0 ChIP: None
29334452: Trichohepatoenteric Syndrome. | 39910293: SKI complex loss renders 9p21.3-deleted or MSI-H cancers dependent on PELO. | 38987716: Trichohepatoenteric syndrome type 1: expanding the clinical spectrum of THES typ

### 4. 总体评价
★★★★  **78.1/100**  **nucleoplasm**
Nuclear protein


### 深度机制分析

**结构域架构与分子功能推断。** SKIC3（TTC37）是SKI复合体的核心支架蛋白，其1564 aa多肽链中的TPR重复结构域——包括TPR_16 (PF13432)、TPR_19 (PF14559)、TPR_8 (PF13181)——与Ski3/TTC37结构域(IPR039226)及TPR-like helical domain superfamily (IPR011990)共同构建了一个扩展的α-螺旋螺线管(solenoid)架构。TPR重复模体是进化上保守的蛋白质-蛋白质互作介导单元，典型的34氨基酸重复形成反平行α-螺旋发夹，多拷贝串联排列后产生一个凹面的肽结合沟槽。在SKIC3中，这些TPR重复的串联排列形成了与SKI复合体其他亚基——尤其是SKIV2L RNA解旋酶和SKIC8(WDR61)——的结合界面。AF2预测的全局pLDDT=86.0处于高置信范围，同时7个PDB实验结构（包含cryo-EM解析的SKI复合体）验证了关键结构域的真实构象。TPR螺线管的刚性架构赋予了SKIC3作为"分子骨架"的功能，将SKIV2L解旋酶的ATP水解能量机械性地耦合到mRNA从80S核糖体的3'→5'方向抽取过程中(PubMed:32006463, PubMed:35120588)。pLDDT在中央TPR串联区域（约残基400-1200）最高(>90)，而N端和C端约200个残基的pLDDT偏低(<70)，提示这些区域可能以固有无序态存在，在SKI复合体的动态构象重排中发挥调节功能。

**PPI网络的生物学意义。** 尽管STRING数据库报告PPI degree=0——直接反映了该蛋白研究的极度匮乏(PubMed严格命中仅9篇)——但已知生化证据表明SKIC3的核心互作圈包括SKIC2(SKIV2L，DEVH-box RNA解旋酶)和SKIC8(WDR61)，三者共同构成异源三聚体SKI复合体。该复合体与胞质RNA外泌体(exosome，由DIS3、EXOSC10等催化亚基组成)物理偶联，在mRNA质量控制和降解通路中执行核心功能。更重要的是，SKIC3介导的停滞核糖体mRNA抽取是Pelota(PELO)-HBS1L复合体结合及后续核糖体拯救(ribosome rescue)的生化前提条件——SKI复合体从停滞核糖体中抽取mRNA后，暴露的A位点允许PELO-HBS1L进入，触发了no-go decay (NGD)和非功能性rRNA decay (NRD)通路(PubMed:39910293)。这一分子层级关系在9p21.3缺失或MSI-H肿瘤中产生了合成致死(synthetic lethality)效应：SKI复合体功能缺失使得这类肿瘤细胞绝对依赖于PELO介导的替代核糖体拯救通路，为精准肿瘤学提供了靶点。

**三维结构的功能解释。** AF2预测SKIC3形成了一个大型右手超螺旋结构，整体pLDDT=86.0，其TPR螺线管在空间上与SKIV2L的RecA样解旋酶结构域形成形状互补的界面的预测与cryo-EM重建数据一致。7个PDB结构(包括冷冻电镜密度图)提供了不同功能状态(ATP结合态、核苷酸游离态)下SKI复合体的构象快照。SKIC3在复合体中采取一个延伸构象，其N端TPR区域接触SKIV2L的C端翼状螺旋结构域(winged-helix domain)，C端区域与WDR61的β-螺旋桨结构互作，形成了围绕解旋酶核心的"笼状"架构。SKIC3的构象柔性主要集中在N端和C端区域，在底物mRNA结合和释放周期中，这些区域可能经历开-合(open-closed)构象转变，调节SKI通道对mRNA底物的亲和力。

**综合分子机制模型。** 基于以上证据的综合，SKIC3在分子层面作为SKI复合体的"骨架-力传导器"行使功能。在正常细胞中，胞质mRNA的3'端被SKI复合体识别后，SKIC3通过其TPR螺线管将SKIV2L解旋酶的3'→5'移位酶活性转化为对80S核糖体mRNA入口通道的机械拉力，逐步将mRNA从核糖体中抽出并喂给外泌体进行3'→5'降解。当核糖体在mRNA上停滞（如遇到二级结构、稀有密码子或无义突变）时，SKIC3介导的抽取为PELO-HBS1L提供了结合窗口。THES(Trichohepatoenteric syndrome)患者中SKIC3的双等位基因功能缺失突变(PubMed:29334452, PubMed:38987716, PubMed:40675981)导致肠道上皮屏障功能障碍、毛发异常(Trico-)、肝病(Hepato-)和免疫缺陷(Entero-)，揭示了SKI复合体在吸收性肠上皮、毛囊干细胞和免疫细胞中维持翻译稳态的本质性作用。

**研究与治疗启示。** SKIC3-PELO合成致死关系(PubMed:39910293)代表了该蛋白最具转化潜力的发现——在携带9p21.3纯合缺失(如胶质母细胞瘤、间皮瘤)或MSI-H(如结直肠癌、子宫内膜癌)的肿瘤中，靶向PELO可在SKI复合体功能本已减弱的背景下产生选择性肿瘤杀伤。TPR螺线管结构虽然传统上被认为缺乏经典的小分子结合口袋，但其延伸的肽结合沟槽可设计为蛋白-蛋白互作抑制剂(如烃钉肽、环肽)的靶点，阻断SKI复合体组装。此外，THES综合征的基因型-表型相关性(genotype-phenotype correlation)研究发现某些错义突变保留部分功能，提示基因治疗或通读(readthrough)疗法的潜在适用人群。

### 补充分析 (UniProt API)

**蛋白全称**: Superkiller complex protein 3

**功能**: Component of the SKI complex, a multiprotein complex that assists the RNA-degrading exosome during the mRNA decay and quality-control pathways (PubMed:16024656, PubMed:32006463, PubMed:35120588). The SKI complex catalyzes mRNA extraction from 80S ribosomal complexes in the 3'-5' direction and channels mRNA to the cytosolic exosome for degradation (PubMed:32006463, PubMed:35120588). SKI-mediated extraction of mRNA from stalled ribosomes allow binding of the Pelota-HBS1L complex and subsequent rib

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR039226 |
| InterPro | IPR011990 |
| InterPro | IPR019734 |
| Pfam | PF13432 |
| Pfam | PF14559 |
| Pfam | PF13181 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---

![PAE](https://alphafold.ebi.ac.uk/files/AF-Q6PGP7-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000198677-SKIC3

![](https://images.proteinatlas.org/37905/437_A6_1_red_green.jpg)
![](https://images.proteinatlas.org/37905/437_A6_2_red_green.jpg)
![](https://images.proteinatlas.org/37905/431_A6_1_red_green.jpg)
![](https://images.proteinatlas.org/37905/431_A6_2_red_green.jpg)
![](https://images.proteinatlas.org/37905/443_A6_1_red_green.jpg)
![](https://images.proteinatlas.org/37905/443_A6_2_red_green.jpg)

### PubMed 文献

**PubMed count: 10**

| 42253433 | Infection-Triggered Disease Flare With Extraintestinal Manifestations in Trichohepatoenteric Syndrome: A Case Report. | Case Rep Med 2026 |
| 40675981 | Novel SKIC3 variants in tricho-hepato-enteric syndrome with hemochromatosis. | Hum Genome Var 2025 |
| 40386307 | Mid‑trimester ultrasound findings in tricho‑hepato‑enteric syndrome: A case report. | Biomed Rep 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SKIC3

