---
type: protein-evaluation
gene: "MTFMT"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## MTFMT 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | MTFMT |
| 蛋白名称 | Methionyl-tRNA formyltransferase, mitochondrial |
| 蛋白大小 | 389 aa / 43.8 kDa |
| UniProt ID | Q96DP5 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 389 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=28 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=86.2; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Fmt; Formyl_trans_C; Formyl_transf_N |
| PPI | 7/10 | x3 | 21.0 | PPI degree=128 |
| **加权总分** | | | **140/180** | |
| **归一化总分** | | | **77.0/100** | 互证: +1 |

### 3. 分析
- Cytosol; Nucleoplasm (Approved)
- PubMed strict=28 broad=40
- AF pLDDT=86.2 PDB=0
- InterPro: Fmt; Formyl_trans_C; Formyl_transf_N
- Pfam: Formyl_trans_C; Formyl_trans_N
- PPI degree=128 ChIP: None
26425749: Nuclear Gene-Encoded Leigh Syndrome Spectrum Overview. | 27290639: New perspective in diagnostics of mitochondrial disorders: two years' experience | 36983072: Mitochondrial Methionyl-tRNA Formyltransferase Deficiency Alleviates Metaflammat

### 4. 总体评价
**77.0/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Methionyl-tRNA formyltransferase, mitochondrial

**功能**: Methionyl-tRNA formyltransferase that formylates methionyl-tRNA in mitochondria and is crucial for translation initiation

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR005794 |
| InterPro | IPR005793 |
| InterPro | IPR002376 |
| InterPro | IPR036477 |
| InterPro | IPR011034 |
| InterPro | IPR041711 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---



### 深度机制分析

MTFMT的域架构揭示了其作为甲酰基转移酶的完整催化装备。InterPro域Fmt（IPR005794）定义了甲硫氨酰-tRNA甲酰基转移酶的全长序列，包含两个功能上独立但结构上协同的亚域：N端Formyl_transf_N（IPR002376, IPR041711）和C端Formyl_trans_C（IPR005793）。Pfam注释进一步细分为Formyl_trans_N（负责结合甲酰供体10-formyl-THF）和Formyl_trans_C（负责结合甲硫氨酰-tRNA底物）。这两个亚域之间的域间裂缝构成了催化中心。IPR036477（Formyl_transf_N超家族）和IPR011034（Formyl_transf_C-like超家族）分别对应N端和C端亚域的结构超家族分类。这种双域结构的进化保守性（从细菌到人类高度保守）反映了翻译起始中甲酰化步骤的不可替代性——线粒体翻译机制的细菌起源保留了fMet-tRNA的起始需求。

PPI网络（degree=128）描绘了MTFMT在线粒体翻译机器中的核心位置。STRING评分最高的伙伴MARS（962，甲硫氨酰-tRNA合成酶）提供了MTFMT的直接底物——新合成的Met-tRNA(Met)。这是一个高度逻辑的互作：MARS将甲硫氨酸加载到tRNA上，随后MTFMT对甲硫氨酰基进行甲酰化。MTIF2（774，线粒体翻译起始因子2）专一性识别fMet-tRNA并将其递送至线粒体核糖体小亚基，形成了MARS→MTFMT→MTIF2的线性底物通道。NSUN4（781）和MTO1（731）分别参与线粒体rRNA甲基化和tRNA修饰，暗示MTFMT与线粒体核糖体组装和质量控制机器存在功能耦合。NSUN2（709）、NSUN5（716）和NOP2（725）均是RNA甲基转移酶，这些伙伴将MTFMT置于一个更广泛的"线粒体RNA修饰网络"中，其中tRNA甲酰化、rRNA甲基化和tRNA修饰协同确保翻译的精确性和效率。

结构层面，AlphaFold pLDDT 86.2表明折叠总体可靠但存在局部柔性区域（可能是域间连接区域）。PDB条目为0，意味着尚无实验解析的MTFMT结构——这提供了一个重要的结构生物学机会（结构评分7/10反映此缺失）。MTFMT的结构可以从细菌同源物（如大肠杆菌Fmt）进行合理推断：N端亚域采用Rossmann-like折叠，结合10-formyl-THF辅因子；C端亚域形成混合α/β折叠，识别tRNA的受体茎（acceptor stem）和TPsiC环。域间裂缝中的催化残基将甲酰基从10-formyl-THF转移到Met-tRNA的氨基端。人源MTFMT的独特之处在于其含有一个线粒体靶向序列（MTS），在导入线粒体后被切除。值得注意的是，HPA的证据显示MTFMT也存在于核质中——这可能反映了一种"兼职"（moonlighting）功能，即MTFMT在细胞核中参与核编码线粒体基因的表达调控或tRNA的核内加工。

综合所有证据得出的分子机制模型如下：MTFMT是"线粒体翻译起始的化学守门人"。在线粒体基质中，MARS合成Met-tRNA(Met)后，MTFMT立即捕获该产物，利用10-formyl-THF作为甲酰供体催化甲硫氨酰基的N端甲酰化。产生的fMet-tRNA(Met)被MTIF2专一性识别并递送至28S线粒体核糖体小亚基的P位点，启动13种线粒体编码蛋白的翻译。这一甲酰化步骤是线粒体翻译起始的限速和质量控制关卡：未甲酰化的Met-tRNA不被MTIF2有效识别，从而阻止异常的翻译起始。MTFMT缺失导致线粒体翻译全面停滞，表现为Leigh综合征谱系疾病（PMID: 26425749），其特征是ATP合成缺陷、乳酸酸中毒和神经退行性变。在核质中，MTFMT的非经典功能可能与核tRNA的甲酰化状态监测有关，调控核编码线粒体蛋白（约1500种）的表达反馈——这是一种推测性的核-线粒体逆行信号机制。在代谢炎症（metaflammation）中（PMID: 36983072），MTFMT缺失反而减轻炎症，这揭示了一个悖论：线粒体翻译的部分抑制可能通过降低线粒体应激信号（如甲酰肽释放）产生抗炎效果。

MTFMT的治疗价值体现在多个层面。在Leigh综合征和其他线粒体疾病中，增强残余MTFMT活性或绕过甲酰化步骤（通过基因治疗递送功能拷贝）可能恢复线粒体翻译。来自肿瘤免疫学的一个令人振奋的线索（PMID: 39086034）：肿瘤来源的线粒体甲酰肽（包括fMet-peptides）通过FPR1受体抑制抗肿瘤免疫。MTFMT是这些免疫抑制性甲酰肽的来源——靶向MTFMT可能减少肿瘤微环境中的甲酰肽水平，从而解除免疫抑制。MTFMT抑制剂因此可能具有双重适应症：在代谢炎症中减轻炎症，同时在肿瘤中增强免疫治疗应答。考虑到MTFMT独特性地存在于线粒体中（所有细胞质和核翻译均使用未甲酰化的Met），选择性靶向MTFMT可能具备较高的治疗窗口——仅影响13种线粒体编码蛋白，而不影响细胞质约20000种蛋白的翻译。获得人源MTFMT的高分辨率结构（目前PDB=0）是结构导向药物设计的首要任务。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| MARS | STRING | 962 |
| NSUN4 | STRING | 781 |
| MTIF2 | STRING | 774 |
| MTO1 | STRING | 731 |
| NOP2 | STRING | 725 |
| WARS2 | STRING | 724 |
| NSUN5 | STRING | 716 |
| NSUN2 | STRING | 709 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q96DP5-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000103707-MTFMT

![](https://images.proteinatlas.org/40710/424_G4_1_red_green.jpg)
![](https://images.proteinatlas.org/40710/424_G4_2_red_green.jpg)
![](https://images.proteinatlas.org/40710/429_G4_1_red_green.jpg)
![](https://images.proteinatlas.org/40710/429_G4_2_red_green.jpg)
![](https://images.proteinatlas.org/40710/418_G4_1_red_green.jpg)
![](https://images.proteinatlas.org/40710/418_G4_2_red_green.jpg)

### PubMed 文献

**PubMed count: 40**

| 26425749 | Nuclear Gene-Encoded Leigh Syndrome Spectrum Overview. |  1993 |
| 39123753 | Methionine Improves Boar Sperm Quality by Promoting Mitochondrial Translation during Liquid Storage. | Animals (Basel) 2024 |
| 39086034 | Tumor-derived mitochondrial formyl peptides suppress tumor immunity through modification of the tumor microenvironment. | Cancer Sci 2024 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/MTFMT

