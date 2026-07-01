---
type: protein-evaluation
gene: "GFM1"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## GFM1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | GFM1 |
| 蛋白名称 | Elongation factor G, mitochondrial |
| 蛋白大小 | 751 aa / 83.5 kDa |
| UniProt ID | Q96RP9 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Mitochondria; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 751 aa |
| 新颖性 | 8/10 | x5 | 40.0 | PubMed=33 |
| 三维结构 | 9/10 | x3 | 27.0 | pLDDT=82.1; PDB=5 |
| 调控结构域 | 4/10 | x2 | 8.0 | EFG_II; EFG_III; EFG_III/V |
| PPI | 8/10 | x3 | 24.0 | PPI degree=442 |
| **加权总分** | | | **144/180** | |
| **归一化总分** | | | **79.2/100** | 互证: +1 |

### 3. 分析
- Mitochondria; Nucleoplasm (Approved)
- PubMed strict=33 broad=60
- AF pLDDT=82.1 PDB=5
- InterPro: EFG_II; EFG_III; EFG_III/V
- Pfam: EFG_C; EFG_III; EFG_IV
- PPI degree=442 ChIP: None
26425749: Nuclear Gene-Encoded Leigh Syndrome Spectrum Overview. | 35581596: UPR(mt) activation improves pathological alterations in cellular models of mitoc | 41317176: Comprehensive and In-Depth Molecular and Pathway Studies of the Hippocampus in A

### 4. 总体评价
**79.2/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

**结构域架构与翻译延长机制**：GFM1属于翻译延长因子G（EF-G）家族，其结构域组织（EFG_II/III/III_V，Pfam EFG_C/EFG_III/EFG_IV）完美映射了经典的GTP酶驱动核糖体易位机制。结构域EFG_II（IPR009022）为效应器结合域，EFG_III和EFG_III/V（IPR035647）构成GTP酶结构域的延伸部分，而EFG_C（C端结构域IV）模仿tRNA的反密码子茎环结构进入核糖体A位点。AlphaFold平均pLDDT为82.1，尽管整体置信度低于高精度蛋白，但5个已解析的PDB实验结构覆盖了关键的GTP结合态和GDP释放态构象，足以阐明其"分子棘轮"催化循环：(1) GTP结合的GFM1识别pre-translocation状态核糖体，(2) GTP水解触发结构域III/IV的大幅度构象重排（~20A位移），(3) 结构域IV推动A位点肽基-tRNA进入P位点，同时P位点脱酰基tRNA进入E位点。该机制与细胞质EF-G高度保守，差异在于线粒体特异性N端靶向序列和内部结构域的进化修饰以适应线粒体核糖体（55S）与细菌核糖体（70S）的结构差异。

**PPI网络与线粒体翻译体整合**：PPI度高达442，高置信互作蛋白几乎全部富集在线粒体翻译装置中。TSFM（993分）是线粒体翻译延长因子Ts，与GFM1形成功能性的GTP-GDP核苷酸交换循环——TSFM催化GFM1上GDP的释放并促进GTP重新结合，是实现多个翻译延长周期的必需伙伴。MRPS9（989分）、MRPL19（987分）、MRPL36（987分）、MRPS5（972分）、MRPS14（961分）分别是线粒体核糖体小亚基（28S）和大亚基（39S）的结构组分。其中MRPS9含有锌指结构域，参与16S rRNA的折叠和mRNA解码中心的结构维持；MRPL19和MRPL36定位于多肽出口隧道附近，可能与新生链的早期共翻译折叠和膜插入偶联。FAU（972分）编码的S30蛋白是40S核糖体亚基的泛素样融合蛋白，其与GFM1的互作提示胞质-线粒体翻译机器的交叉通信。BRIP1（987分）是DEAH-box DNA解旋酶，参与DNA交联修复和同源重组，其与线粒体翻译因子的互作暗示线粒体翻译保真度与核基因组稳定性的功能耦合。

**核-线粒体双重定位的功能演绎**：GFM1获HPA Approved级别核质定位，结合其主要线粒体定位，构成一个经典的双重亚细胞分布模式。线粒体翻译装置的核编码基因普遍保留祖先真细菌的基因结构，但GFM1的核定位可能服务于至少三种非经典功能：(1) 核内新生GFM1 mRNA的自我调控——GFM1蛋白可能作为其自身mRNA的翻译抑制因子，类似于细菌EF-G的自调控回路；(2) 核内核糖体的质量控制——核内存在翻译活性，GFM1可能在pre-60S亚基的核内检查步骤中参与功能验证；(3) 线粒体应激信号的核内转导——PMID 35581596证实UPR(mt)激活改善线粒体疾病细胞模型的病理改变，而GFM1作为翻译延长因子可能直接感知线粒体翻译压力，并通过核定位将信号传递至核转录程序。GFM1突变导致的COXPD1（联合氧化磷酸化缺陷1型）临床表现包括Leigh综合征谱系的严重神经退行性病变，这不仅是ATP合成缺陷的后果，更可能涉及核定位GFM1无法正常执行核内监视功能。

**机制模型与研究意义**：GFM1作为线粒体翻译延长核心因子，通过TSFM核苷酸交换循环驱动多轮GTP依赖的核糖体易位。其核定位提出GFM1参与线粒体-核通信的新假说——在氧化磷酸化负荷下，GFM1蛋白的亚细胞分配可能发生动态改变，部分蛋白重新分布至核质，作为线粒体翻译状态的直接传感器。该蛋白的高PPI网络密度和多重结构域架构使其成为线粒体疾病基因治疗的理想靶点——PMID 41998139已证实AAV递送GFM1可纠正Gfm1(R671C/-)小鼠的COXPD1分子缺陷，为翻译延长因子的体细胞基因替代治疗开辟了先例。未来应关注：(1) 核定位信号鉴定及其功能意义，(2) 核内GFM1是否参与特定的RNA代谢过程，(3) 开发线粒体特异性GFM1活性检测方法以区分线粒体和核功能，(4) 探究GFM1-BRIP1互作在维持线粒体-核基因组完整性中的角色。

### 补充分析 (UniProt API)

**蛋白全称**: Elongation factor G, mitochondrial

**功能**: Mitochondrial GTPase that catalyzes the GTP-dependent ribosomal translocation step during translation elongation. During this step, the ribosome changes from the pre-translocational (PRE) to the post-translocational (POST) state as the newly formed A-site-bound peptidyl-tRNA and P-site-bound deacylated tRNA move to the P and E sites, respectively. Catalyzes the coordinated movement of the two tRNA molecules, the mRNA and conformational changes in the ribosome. Does not mediate the disassembly of

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR041095 |
| InterPro | IPR009022 |
| InterPro | IPR035647 |
| InterPro | IPR047872 |
| InterPro | IPR035649 |
| InterPro | IPR000640 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TSFM | STRING | 993 |
| MRPS9 | STRING | 989 |
| MRPL19 | STRING | 987 |
| MRPL36 | STRING | 987 |
| BRIP1 | STRING | 987 |
| FAU | STRING | 972 |
| MRPS5 | STRING | 972 |
| MRPS14 | STRING | 961 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q96RP9-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000168827-GFM1

![](https://images.proteinatlas.org/61405/1248_D11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/61405/1248_D11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/61405/1168_B9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/61405/1168_B9_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000168827-GFM1

![](https://images.proteinatlas.org/61405/1248_D11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/61405/1248_D11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/61405/1168_B9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/61405/1168_B9_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000168827-GFM1

![](https://images.proteinatlas.org/61405/1248_D11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/61405/1248_D11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/61405/1168_B9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/61405/1168_B9_2_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 60**

| 41998139 | Systemic delivery of AAV-GFM1 corrects COXPD1 molecular alterations in Gfm1(R671C/-) mice. | EMBO Mol Med 2026 |
| 41793476 | miR-214-3p exacerbates mitochondrial dysfunction in parkinson's disease: a multi-omics and mechanistic study. | Exp Brain Res 2026 |
| 41691090 | Machine-learning-guided transcriptomic integration identifies GFM1 as a lactylation-related candidate biomarker in aorti | Sci Rep 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/GFM1

