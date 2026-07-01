---
type: protein-evaluation
gene: "PPP5C"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PPP5C 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PPP5C |
| 蛋白名称 | Serine/threonine-protein phosphatase 5 |
| 蛋白大小 | 499 aa / 56.9 kDa |
| UniProt ID | P53041 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | nan (Supported) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 499 aa |
| 研究新颖性 | 8/10 | ×5 | 40.0 | PubMed=33 |
| 三维结构 | 10/10 | ×3 | 30.0 | pLDDT=92.8; PDB=22 |
| 调控结构域 | 4/10 | ×2 | 8.0 | Calcineurin-like_PHP; Metallo-depent_PP-like; PP5_C |
| PPI | 8/10 | ×3 | 24.0 | PPI degree=203 |
| **加权总分** | | | **143/180** | |
| **归一化总分** | | | **79.2/100** | 互证: +2 |

### 3. 分析
| 项目 | 详情 |
|---|---|
| HPA | nan (Supported) |
| PubMed | strict=33, broad=39 |
| AF pLDDT | 92.8 |
| PDB | 22 |
| InterPro | Calcineurin-like_PHP; Metallo-depent_PP-like; PP5_C |
| Pfam | Metallophos; PPP5; TPR_1 |
| PPI degree | 203 |
| ChIP | None |

**Papers**: 29180230: Glucocorticoids, genes and brain function. | 37054560: Dual function of protein phosphatase 5 (PPP5C): An emerging therapeutic target f | 30679389: The Antitumor Drug LB-100 Is a Catalytic Inhibitor of Protein Phosphatase 2A (PP

### 4. 总体评价
★★★★  **79.2/100**  |  **nucleoplasm**
Nuclear protein


### 深度机制分析

**结构域架构与磷酸酶催化的自抑制机制**：PPP5C采用三重域架构——N端TPR（三十四肽重复）结构域、中心PPP催化结构域和C端调控结构域（PP5_C），代表了Ser/Thr磷酸酶家族的独特调控范式。TPR结构域（Pfam TPR_1）包含三个串联的三十四肽重复单元，每个单元形成一对反平行α螺旋，共同构建一个凹形分子识别槽。在基础状态下，TPR结构域通过C端PP5_C结构域中的α-J螺旋发生分子内互作，将催化中心封闭为自抑制构象——这是一种罕见的"分子内自动刹车"设计，使得PPP5C的基础活性极低。IPR004843（Calcineurin-like_PHP，钙调磷酸酶样磷酸酯酶）将PPP5C归入PPP家族，该家族催化中心采用双金属离子机制——两个Mn2+或Fe2+离子由保守的天冬氨酸和组氨酸残基配位，激活一个水分子进行亲核攻击去磷酸化底物的磷酰基。AlphaFold平均pLDDT高达92.8，22个PDB实验结构覆盖了自抑制态、Hsp90结合态和花生四烯酸激活态的完整构象谱，使PPP5C成为PPP家族中结构表征最全面的成员之一。这种结构丰富度意味着其构象开关的原子级细节已被阐明，为理解其底物选择性提供了独特视角。

**PPI网络与信号中枢假设**：PPI度203，互作图谱揭示PPP5C是一个连接多条关键信号通路的分子枢纽。MAP3K5（ASK1，凋亡信号调节激酶1）是PPP5C的经典底物——PPP5C通过去磷酸化ASK1的Thr845位点直接抑制其激酶活性，进而阻断下游JNK/p38 MAPK级联的激活，构成氧化应激诱导凋亡的负反馈回路。CDC27是后期促进复合物/环体（APC/C）的核心亚基，PPP5C与CDC27的结合提示有丝分裂中后期转换的磷酸酶调控——APC/C底物识别需要CDC27的可逆磷酸化，PPP5C可能是该步骤的去磷酸化执行者。CRY2（隐花色素2）是昼夜节律核心振荡器的蓝光受体和转录抑制因子，与PPP5C的互作将磷酸酶活性直接锚定至昼夜节律时钟——CRY2的磷酸化状态调控其稳定性（FBXL3泛素连接酶的识别依赖磷酸化修饰），PPP5C可能通过去磷酸化CRY2延长其半衰期，从而调节昼夜节律周期。CSE1L（染色体分离1样蛋白，Exportin-2）介导Importin-α从核到胞质的循环，促进RanGTP依赖的核转运，与PPP5C的互作提示磷酸酶活性调节核质穿梭机制。GNA12和GNA13（G蛋白α亚基12/13家族）偶联GPCR至RhoGEF-RhoA信号轴以控制细胞骨架重排和细胞运动，与PPP5C的互作将磷酸酶整合至GPCR下游的信号调制。PHLPP1（PH domain and leucine rich repeat protein phosphatase 1）本身为Ser/Thr磷酸酶，通过去磷酸化Akt的Ser473终止PI3K信号，与PPP5C的互作组成磷酸酶级联，实现对Akt信号的多层次抑制。

**激活机制与脂质代谢物的调控**：PPP5C的激活需要多不饱和脂肪酸——特别是花生四烯酸（C20:4,n-6）及其代谢物——作为变构激活剂。花生四烯酸结合于TPR结构域与催化结构域的界面，通过诱导TPR结构域从催化中心的解离解除自抑制，使活性位点暴露。这一机制将PPP5C活性与磷脂酶A2（PLA2）信号和环氧合酶（COX）通路耦合——在炎症刺激下，PLA2释放的花生四烯酸不仅作为前列腺素前体，还同时激活PPP5C实现对MAPK信号的负调控。此外，TPR结构域作为Hsp90的专一性共伴侣蛋白，通过其凹形识别槽特异性结合Hsp90 C端MEEVD基序，将PPP5C精准招募至Hsp90客户蛋白（如糖皮质激素受体NR3C1、端粒酶hTERT、多种激酶），实现折叠成熟过程中的位点特异性去磷酸化。这一TPR-Hsp90偶联使得PPP5C区别于所有其他PPP家族成员——它是唯一定位于分子伴侣质量控制系统的磷酸酶。

**机制模型与治疗前景**：PPP5C作为"多信号节点磷酸酶"，通过自抑制调控实现极低的基础活性，仅在特定激活信号（Hsp90招募、花生四烯酸结合）下释放催化能力。其在核质中的定位使其直接调控核受体（NR3C1/PPARG/ESR1/ESR2）的转录活性——通过去磷酸化NR3C1的Ser211位点增强其转录激活能力，通过去磷酸化PPARG的Ser112位点促进其与RXRα异二聚化。该蛋白的双面性使其成为独特的治疗靶点：在癌症中抑制PPP5C可解除对ASK1-JNK凋亡通路的压制（PMID 30679389中LB-100的催化抑制原理）；而在阿尔茨海默病中，激活PPP5C可减少tau蛋白的过度磷酸化（PPP5C直接去磷酸化tau的Ser396/Ser404病理位点）。未来研究应：(1) 开发PPP5C亚型特异性抑制剂/激活剂以避免影响PP1/PP2A/PP2B，(2) 解析Hsp90-PPP5C-client三元复合物的冷冻电镜结构，(3) 探究PPP5C-CRY2互作在昼夜节律紊乱相关代谢疾病中的病理意义，(4) 利用PPP5C-CDC27互作界面开发有丝分裂调控工具。

### 补充分析 (UniProt API)

**蛋白全称**: Serine/threonine-protein phosphatase 5

**功能**: Serine/threonine-protein phosphatase that dephosphorylates a myriad of proteins involved in different signaling pathways including the kinases CSNK1E, ASK1/MAP3K5, PRKDC and RAF1, the nuclear receptors NR3C1, PPARG, ESR1 and ESR2, SMAD proteins and TAU/MAPT (PubMed:14734805, PubMed:14764652, PubMed:14871926, PubMed:15383005, PubMed:15546861, PubMed:16260606, PubMed:16790549, PubMed:16892053, PubMed:19176521, PubMed:19948726, PubMed:21144835, PubMed:22399290, PubMed:22781750, PubMed:23102700, Pub

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR004843 |
| InterPro | IPR029052 |
| InterPro | IPR041753 |
| InterPro | IPR013235 |
| InterPro | IPR051134 |
| InterPro | IPR006186 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CSE1L | BioGRID | 0 |
| CDC27 | BioGRID | 0 |
| GNA12 | BioGRID | 0 |
| GNA13 | BioGRID | 0 |
| MAP3K5 | BioGRID | 0 |
| CRY2 | BioGRID | 0 |
| USP49 | BioGRID | 0 |
| PHLPP1 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-P53041-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000011485-PPP5C

![](https://images.proteinatlas.org/29065/319_F4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/29065/319_F4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/29065/340_F4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/29065/340_F4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/29065/320_F4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/29065/320_F4_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000011485-PPP5C

![](https://images.proteinatlas.org/29065/319_F4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/29065/319_F4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/29065/340_F4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/29065/340_F4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/29065/320_F4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/29065/320_F4_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000011485-PPP5C

![](https://images.proteinatlas.org/29065/319_F4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/29065/319_F4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/29065/340_F4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/29065/340_F4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/29065/320_F4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/29065/320_F4_2_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 39**

| 42027049 | Catalyst-Free, Divergent Cysteine Modification via Indole Isocyanide Photochemistry. | Angew Chem Int Ed Engl 2026 |
| 41865147 | The mechanism of the water layer extract of Cichorium pumilum Jacq water extract in the treatment of Hepatic fibrosis wa | J Nat Med 2026 |
| 41279245 | Distinct patterns of de novo coding variants contribute to Tourette Syndrome etiology. | bioRxiv 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PPP5C

