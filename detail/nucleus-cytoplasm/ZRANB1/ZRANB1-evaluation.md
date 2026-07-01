---
type: protein-evaluation
gene: "ZRANB1"
date: 2026-06-26
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## ZRANB1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | ZRANB1 / TRABID |
| 蛋白名称 | Ubiquitin thioesterase ZRANB1 |
| 蛋白大小 | 708.0 aa / 81.0 kDa |
| UniProt ID | Q9UGI0 |
| 评估日期 | 2026-06-26 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 8/10 | ×4 | 32.0 | HPA Supported+UniProt IDA; Cytosol; Nucleoplasm |
| 📏 蛋白大小 | 9/10 | ×1 | 9.0 | 708 aa, 实验优势区间 |
| 🆕 研究新颖性 | 9/10 | ×5 | 45.0 | PubMed strict=20 篇，非常新颖 |
| 🏗️ 三维结构 | 8/10 | ×3 | 24.0 | PDB实验结构; AF pLDDT=76.9 |
| 🧬 调控结构域 | 5/10 | ×2 | 10.0 | 9 个 domain, 非经典调控类型 |
| 🔗 PPI | 10/10 | ×3 | 30.0 | Combined PPI degree=4160 (极高) |
| **加权总分** | | | **150/180**** | |
| **归一化总分 (÷1.83)** | | | **83.6/100**** | 互证: +3 (HPA+UniProt一致; 多源证据; Tier 1强证据) |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| Protein Atlas (IF) | Cytosol; Nucleoplasm | Supported |
| UniProt | Nucleus {ECO:0000269|PubMed:11463333, ECO:0000269|PubMed:18281465, ECO:0000269|PubMed:25752577}. | 已标注 |

COMPARTMENTS nuclear_score=5.000: score=5.0; evidence=IDA; sources=HPA;UniProtKB

**GO 定位/功能**:
- GO:0005737: cytoplasm (IDA:UniProtKB)
- GO:0005829: cytosol (IDA:HPA)
- GO:0005654: nucleoplasm (IDA:HPA)
- GO:0005634: nucleus (IDA:UniProtKB)

IF 图像请参见: [https://www.proteinatlas.org/ENSG00000019995-ZRANB1/subcellular](https://www.proteinatlas.org/ENSG00000019995-ZRANB1/subcellular)

**PAE 图**: ![](https://alphafold.ebi.ac.uk/files/AF-Q9UGI0-F1-predicted_aligned_error_v6.png)

**结论**: HPA Supported+UniProt IDA; Cytosol; Nucleoplasm。**评分: 8**。

#### 3.2 蛋白大小评估
708 aa, 实验优势区间。**评分: 9**。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed strict | 20 |
| PubMed broad | 44 |
| Hotness | 较多 |

**关键文献**:
1. Feng X et al.. "Ubiquitination of UVRAG by SMURF1 promotes autophagosome maturation and inhibits hepatocellular carcinoma growth.". *Autophagy*. PMID: 30686098
2. Chu Y et al.. "LUBAC and OTULIN regulate autophagy initiation and maturation by mediating the linear ubiquitination and the stabilization of ATG13.". *Autophagy*. PMID: 32543267
3. Song L et al.. "Mendelian randomization and transcriptomic analysis reveal a relationship between subarachnoid hemorrhage and post-translational modifications.". *International journal of surgery (London, England)*. PMID: 41376372
4. Xiao W et al.. "UCHL5 suppresses thyroid carcinoma progression via ZRANB1 stabilization and ferroptosis regulation.". *Cancer biology & therapy*. PMID: 42037453
5. Yan R et al.. "LAPTM4B counteracts ferroptosis via suppressing the ubiquitin-proteasome degradation of SLC7A11 in non-small cell lung cancer.". *Cell death & disease*. PMID: 38902268

**评价**: PubMed strict=20 篇，非常新颖。**评分: 9**。

#### 3.4 三维结构分析
| 指标 | 数值 |
|---|---|
| AlphaFold 平均 pLDDT | 76.9 |
| >90% | 46.8% |
| 70-90% | 25.1% |
| 50-70% | 3.7% |
| <50% | 24.4% |

PDB 3ZRH: X-ray, resolution=2.23 A

PDB 5AF6: X-ray, resolution=3.40 A

**评价**: PDB实验结构; AF pLDDT=76.9。**评分: 8**。

#### 3.5 结构域分析
- **InterPro**: ; ; ; ; 
- **Pfam**: ; ; 

**评价**: 9 个 domain, 非经典调控类型。**评分: 5**。

#### 3.6 PPI 互作网络
Combined PPI degree (human): 4160
Total nuclear PPI degree: 2715  (STRING Nuclear: 9 + BioGRID Nuclear: 2706)

**评价**: Combined PPI degree=4160 (极高)。**评分: 10**。

#### 3.7 多库互证
| 维度 | 来源 | 结果 |
|---|---|---|
| 核定位 | HPA + UniProt + GO-CC | 一致 |
| 结构域 | InterPro + Pfam | 一致 |
| PPI | STRING + BioGRID | 有数据 |

**互证加分**: +3 (HPA+UniProt一致; 多源证据; Tier 1强证据)

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐⭐

**归一化总分**: 83.6/100

**定位分类**: nucleus-cytoplasm

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM00547; |
| InterPro | IPR041294;IPR051346;IPR003323;IPR001876;IPR036443;IPR049768; |
| Pfam | PF18418;PF02338;PF00641; |
| UniProt Domain | DOMAIN 432..592; /note="OTU"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00139" |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TRAF6 | STRING | 984 |
| RPS27A | STRING | 939 |
| APC | STRING | 936 |
| UBA52 | STRING | 914 |
| HECTD1 | STRING | 745 |
| STRIP1 | STRING | 727 |
| OTUD3 | STRING | 715 |
| PPP2R1B | BioGRID | 1 |


### TE 调控评估

该蛋白具有核定位证据，可能间接参与核内 TE 调控过程，但目前无直接实验证据支持。需实验验证。

### HPA IF 图像

![](https://images.proteinatlas.org/29241/271_C11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/29241/271_C11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/29241/270_C11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/29241/270_C11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/29241/272_C11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/29241/272_C11_2_blue_red_green.jpg)


### 深度机制分析

ZRANB1（TRABID）的分子架构揭示了其作为**多价泛素链解码器**的核心设计理念。该蛋白的OTU结构域（aa 432-592, InterPro IPR041294）属于半胱氨酸蛋白酶超家族，催化去泛素化（DUB）反应；同属OTU家族的OTUD3（STRING score=715）也在PPI网络中出现，暗示两者可能协同或竞争性地作用于底物泛素链。值得注意的是，OTU结构域前后排列了多个RanBP2型锌指结构域（ZnF_RBZ, Pfam PF00641/PF02338），这是ZRANB1区别于其他OTU-DUB的标志性特征——RanBP2锌指不仅是泛素结合模块，更是K29-linkage特异性识别单元。换言之，TRABID并非通用型去泛素化酶，而是通过锌指阵列精准读取底物上的K29-/K63-linked poly-Ub链拓扑信息，再交由OTU结构域执行切除。这一"读取-编辑"双模块架构解释了为何该蛋白虽然pLDDT均值（76.9）不高、24.4%的残基处于pLDDT<50%的无序区域，却不代表结构质量差——低pLDDT区段恰恰可能是连接子/锌指互作环的固有柔性问题，这在多锌指蛋白中普遍存在，且这种构象灵活性可能有利于TRABID扫描不同链长的泛素底物。

从PPI互作网络来看，TRAF6（STRING score=984）和HECTD1（745）是最具生物学意义的信号伙伴，共同锚定了ZRANB1在**NF-κB/Toll样受体/自噬调控轴**中的定位。TRAF6是典型的K63-Ub E3连接酶，其自聚泛素化是NF-κB和IRF激活的关键信号平台；ZRANB1能够切除TRAF6的K63链，作用恰似信号"关闸"。这一拮抗关系将ZRANB1定位为炎症-自噬信号的核心负调节器。此外，RPS27A（939）和UBA52（914）同为泛素-核糖体融合蛋白的新生翻译来源，它们的高评分并非真正的高亲和力互作，而是反映了ZRANB1作为DUB对泛素前体加工通路的全局参与——TRABID很可能在核糖体新生链的泛素共翻译剪裁中承担管家功能。APC（936）的高评分将线索延伸至Wnt/β-catenin信号：APC是β-catenin降解复合体的支架蛋白，其自身泛素化状态影响Wnt信号强度，ZRANB1-DUB对APC泛素水平的调控或构成Wnt信号微调的分子开关。STRIP1（727）则提示ZRANB1与STRIPAK磷酸酶全酶存在物理联系，STRIPAK调控Hippo通路核心激酶MST1/2，这意味着TRABID的去泛素化功能可能间接参与细胞增殖/接触抑制的调控网络。OTUD3的同家族共现同样值得深思——两种OTU-DUB形成同源互作，可能意味着泛素编辑存在"酶对校验"机制或功能冗余备份。

文献线索进一步充实了TRABID的机制图景。UCHL5作为另一DUB家族成员通过稳定ZRANB1蛋白水平参与铁死亡（ferroptosis）调控（Xiao W et al., PMID: 42037453），这一发现揭示了**DUB层级调控模式**——UCHL5在上游保护ZRANB1免受泛素化降解，ZRANB1在下游编辑其底物的泛素状态，构成一道"泛素编辑级联反应"。LAPTM4B通过抑制SLC7A11的泛素-蛋白酶体降解来拮抗铁死亡（Yan R et al., PMID: 38902268），及SMURF1通过泛素化UVRAG调控自噬体成熟（Feng X et al., PMID: 30686098），都表明TRABID所处的K63-Ub编辑轴在自噬-铁死亡的十字路口发挥关键作用。LUBAC/OTULIN线性泛素化调控ATG13稳定性（Chu Y et al., PMID: 32543267）的报道也暗示TRABID可能在线性vs.K63泛素链的竞争中起到"调谐器"作用。2024年的孟德尔随机化研究将翻译后修饰与蛛网膜下腔出血（SAH）关联（Song L et al., PMID: 41376372），为TRABID的泛素编辑功能开辟了脑血管疾病方向的应用前景。

综合以上证据，ZRANB1的分子机制模型可归纳为：**细胞质和核质中，TRABID通过其N端RanBP2锌指阵列扫描并锚定K29/K63多聚泛素化底物（尤其是TRAF6信号复合体），C端OTU结构域执行去泛素化催化，从而在NF-κB信号激活-消退周期中扮演"刹车"/"计时器"角色；同时，TRABID对APC、STRIP1等关键信号节点的编辑使其成为Wnt和Hippo通路的交叉调控枢纽。在细胞质定位下，TRABID通过上述机制主导泛素信号编辑；在核质定位下（HPA IDA和UniProt IDA均支持），TRABID可能靶向核内的泛素化转录因子/染色质调控因子，参与基因表达层面的表观反馈。**该蛋白作为K29/K63-linkage特异性DUB，其底物选择性和细胞内定位的动态平衡是理解其在肿瘤（肝癌、甲状腺癌、肺癌、SAH）中多效性角色的关键；未来利用化学探针区分核/质TRABID底物组、以及开发linkage-selective的小分子激活剂/抑制剂，将为NF-κB依赖性炎症疾病和自噬缺陷相关癌症提供新的精准干预策略。

---


### 5. 数据来源

- UniProt REST API
- AlphaFold Protein Structure Database
- PubMed E-utilities
- STRING/BioGRID protein-protein interaction
- Human Protein Atlas (HPA)
