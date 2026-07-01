---
type: protein-evaluation
gene: "NAE1"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## NAE1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | NAE1 |
| 蛋白名称 | NEDD8-activating enzyme E1 regulatory subunit |
| 蛋白大小 | 534 aa / 60.2 kDa |
| UniProt ID | Q13564 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Centrosome; Microtubules; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 534 aa |
| 新颖性 | 7/10 | x5 | 35.0 | PubMed=72 |
| 三维结构 | 10/10 | x3 | 30.0 | pLDDT=96.2; PDB=9 |
| 调控结构域 | 4/10 | x2 | 8.0 | APP-BP1; ThiF/MoeB/HesA; ThiF_NAD_FAD-bd |
| PPI | 7/10 | x3 | 21.0 | PPI degree=117 |
| **加权总分** | | | **139/180** | |
| **归一化总分** | | | **77.0/100** | 互证: +2 |

### 3. 分析
- Centrosome; Microtubules; Nucleoplasm (Approved)
- PubMed strict=72 broad=105
- AF pLDDT=96.2 PDB=9
- InterPro: APP-BP1; ThiF/MoeB/HesA; ThiF_NAD_FAD-bd
- Pfam: ThiF
- PPI degree=117 ChIP: None
37429843: Genome-wide association analysis and Mendelian randomization proteomics identify | 39229723: Crotonylation of NAE1 Modulates Cardiac Hypertrophy via Gelsolin Neddylation. | 35217064: Targeting NAE1-mediated protein hyper-NEDDylation halts cholangiocarcinogenesis 

### 4. 总体评价
**77.0/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: NEDD8-activating enzyme E1 regulatory subunit

**功能**: Regulatory subunit of the dimeric UBA3-NAE1 E1 enzyme. E1 activates NEDD8 by first adenylating its C-terminal glycine residue with ATP, thereafter linking this residue to the side chain of the catalytic cysteine, yielding a NEDD8-UBA3 thioester and free AMP. E1 finally transfers NEDD8 to the catalytic cysteine of UBE2M. Necessary for cell cycle progression through the S-M checkpoint. Overexpression of NAE1 causes apoptosis through deregulation of NEDD8 conjugation. The covalent attachment of NED

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR030667 |
| InterPro | IPR045886 |
| InterPro | IPR000594 |
| InterPro | IPR035985 |
| Pfam | PF00899 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---



### 深度机制分析

NAE1的域架构揭示了其作为异源二聚体E1酶调节亚基的结构基础。InterPro域APP-BP1（IPR030667）定义了NAE1在进化中的同源性——它与APP结合蛋白1（APP-BP1）在序列和结构上密切相关，参与了APP（淀粉样前体蛋白）的细胞内运输和信号传导。关键催化域ThiF/MoeB/HesA（IPR000594）和ThiF_NAD_FAD-bd（IPR035985），加上Pfam域ThiF（PF00899），属于一个古老的ATP依赖性酶超家族，其原型成员参与硫胺素生物合成（ThiF）和钼辅因子生物合成（MoeB）。在这个超家族中，该域催化"腺苷酰化-硫酯形成"两步反应：首先用ATP腺苷酰化泛素样蛋白（UBL）的C端甘氨酸，然后通过一个活性位点半胱氨酸形成E1~UBL硫酯中间体。NAE1的独特之处在于该域本身不具有催化活性——催化活性由伴侣亚基UBA3提供，NAE1的ThiF样域为UBA3提供结构支架和底物识别框架。这种"活性位点反式互补"（active site trans-complementation）的代表性特征是NAE1-UBA3异源二聚体E1系统的核心组织原则。

PPI网络（degree=117）产生了极强的机制收敛性——STRING评分最高的四个伙伴指向了NEDD8级联反应的核心组分。NEDD8（999）是底物UBL，UBA3（999）是催化亚基，UBE2M（999）是E2结合酶，三者均获得最高的STRING评分999分。这一近乎完美的评分模式确定NAE1是NEDDylation通路无可争议的核心组分。APP（998）的出现既反映了NAE1的历史命名来源（APP-BP1同源物），也暗示了NAE1在APP运输和γ-分泌酶处理中的调控角色——NAE1可能通过NEDDylation调控APP的细胞内膜运输。UBE2F（976）是另一个E2，与UBE2M形成冗余和分工——UBE2F偏好Cullin-5的NEDDylation，而UBE2M作用于Cullin 1-4。CUL1（923）、RBX1（873）和CUL4A（867）是CRL（Cullin-RING Ligase）E3连接酶复合物的核心骨架蛋白——它们的NEDDylation状态是CRL活性的关键开关。这组互作伙伴清晰地勾勒出NAE1→UBA3→UBE2M/F→Cullins→RBX1的线性信号传递轴。

结构层面，AlphaFold pLDDT高达96.2是本次分析五个蛋白中的最高值，9个PDB结构为深入的结构-功能分析提供了坚实基础。这个极高的pLDDT反映了NAE1-UBA3异源二聚体在进化中经历的强烈结构约束——NAE1必须以高度精确的几何结构结合UBA3、NEDD8和ATP。9个PDB结构覆盖了反应循环的多个关键构象态，包括：NAE1-UBA3-NEDD8-ATP四元复合物（腺苷酰化步骤）、NAE1-UBA3~NEDD8硫酯中间体、以及NAE1-UBA3-UBE2M三元复合物（E1-to-E2转硫酯步骤）。这些结构揭示了NAE1的ThiF-like域如何通过其疏水沟槽识别NEDD8的C端尾巴，同时以别构方式激活UBA3的催化Cys。结构评分10/10更得益于该蛋白在人类蛋白质组中的结构覆盖度处于顶尖水平。

综合所有证据的分子机制模型清晰定义了NAE1作为"NEDDylation信号钟的装配平台"。在分子层面，NAE1与UBA3形成紧密的异源二聚体，构成了NEDD8激活酶（NAE）。该循环分为三步：第一步（腺苷酰化），NAE1的ThiF-like域结合并正确定向NEDD8的C端Gly76，同时UBA3结合ATP-Mg2+，催化NEDD8-C末端的腺苷酰化，形成NEDD8~AMP中间体并释放PPi。第二步（硫酯形成），UBA3的催化Cys残基亲核攻击腺苷酰化中间体，释放AMP并形成UBA3~NEDD8硫酯键。第三步（E1→E2转硫酯），NAE1-UBA3~NEDD8复合物招募E2酶UBE2M或UBE2F，通过转硫酯反应将NEDD8转移到E2的催化Cys上。最终的E2~NEDD8复合物随后与CRL E3连接酶（CUL1-5/RBX1-2）合作，将NEDD8共价连接到Cullin亚基的保守Lys残基上，引发Cullin的构象重排，从而激活CRL的泛素连接酶活性。在核质中，NAE1-UBA3定位于中心体和微管（HPA Approved定位），提示NEDDylation可能在有丝分裂纺锤体组装和中心体复制中发挥关键作用——特别是CRL1（SCF复合物）的关键底物包括多种细胞周期调节因子（p27, cyclin E, CDT1）。PMID: 42144028证实NAE1通过NEDDylation介导的CDT1降解抑制DNA重复制，为这一核质功能提供了直接证据。

NAE1的科研与治疗潜力的深度和广度在五个蛋白中最高。PubMed 72篇严格文献（虽然新颖性7/10相对较低，但反映了该领域的临床转化进展）集中于两个方向：（1）MLN4924（pevonedistat）——首个小分子NAE抑制剂，通过共价结合NEDD8-AMP加合物模拟物阻断NAE活性，已在AML（急性髓系白血病）临床试验中显示出显著的抗肿瘤活性；（2）NAE1的组织特异性功能——在心肌肥大中，NAE1的巴豆酰化修饰（crotonylation，非组蛋白新型酰化修饰）调控gelsolin的NEDDylation，从而调控心肌细胞骨架重组（PMID: 39229723）。最新的颠覆性发现（PMID: 42056084）揭示NAE1-UBA3-UBE2M同样是URM1修饰（一种古老的tRNA硫醇化相关UBL）的E1-E2酶系统——这意味着NAE1是NEDD8和URM1双重UBL途径的共享激活平台，大大扩展了其底物谱和功能范围。在胆管癌中（PMID: 35217064），NAE1介导的蛋白超NEDDylation驱动肿瘤发生，为MLN4924的实体瘤适应症提供了理论支持。核质定位、高结构覆盖度（pLDDT 96.2, PDB=9）、与CRL超家族的深度连接以及已进入临床的抑制剂这三重优势，使NAE1成为五个蛋白中转化潜力最强的药物靶点。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| NEDD8 | STRING | 999 |
| UBE2M | STRING | 999 |
| UBA3 | STRING | 999 |
| APP | STRING | 998 |
| UBE2F | STRING | 976 |
| CUL1 | STRING | 923 |
| RBX1 | STRING | 873 |
| CUL4A | STRING | 867 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q13564-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000159593-NAE1

![](https://images.proteinatlas.org/41178/539_G8_1_red_green.jpg)
![](https://images.proteinatlas.org/41178/539_G8_2_red_green.jpg)
![](https://images.proteinatlas.org/41178/552_G8_1_red_green.jpg)
![](https://images.proteinatlas.org/41178/552_G8_2_red_green.jpg)
![](https://images.proteinatlas.org/41178/534_G8_1_red_green.jpg)
![](https://images.proteinatlas.org/41178/534_G8_2_red_green.jpg)
![](https://images.proteinatlas.org/42041/489_F10_1_red_green.jpg)
![](https://images.proteinatlas.org/42041/489_F10_2_red_green.jpg)

### PubMed 文献

**PubMed count: 105**

| 42270428 | Erratum: Jing and Wu et al., "Neddylation E1 Obligatory Subunit Nae1 Is Critical to Neuromuscular Junction Development a | J Neurosci 2026 |
| 42144028 | Neocryptomerin targets NAE1 to induce DNA re-replication and DNA damage by inhibiting neddylation-mediated CDT1 degradat | Pharmacol Res 2026 |
| 42056084 | NAE1/UBA3-UBE2M are E1 and E2 enzymes for the URM1 modification. | Nat Commun 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/NAE1

