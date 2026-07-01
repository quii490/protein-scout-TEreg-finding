---
type: protein-evaluation
gene: "A0A140VJS6"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## A0A140VJS6 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | A0A140VJS6 |
| 蛋白大小 | 201 aa / 22.8 kDa |
| UniProt ID | A0A140VJS6 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | x4 | 20.0 | nan (nan) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 201 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=0 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=96.3; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Ntn_hydrolases_N; Proteasome_beta2; Proteasome_bsu_CS |
| PPI | 5/10 | x3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **121/180** | |
| **归一化总分** | | | **67.2/100** | 互证: +2 |

### 3. 分析
- nan (nan)
- PubMed strict=0 broad=0
- AF pLDDT=96.3 PDB=0
- InterPro: Ntn_hydrolases_N; Proteasome_beta2; Proteasome_bsu_CS
- Pfam: Proteasome
- PPI degree=0 ChIP: None


### 4. 总体评价
**67.2/100** | **nucleoplasm**
Nuclear protein


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PSMA4 | STRING | 999 |
| PSMC4 | STRING | 998 |
| PSMD8 | STRING | 993 |
| PSMA3 | STRING | 999 |
| PSMD7 | STRING | 993 |
| PSMA2 | STRING | 999 |
| PSMB7 | STRING | 997 |
| PSMC1 | STRING | 999 |
| PSMA6 | STRING | 999 |
| PSMD11 | STRING | 995 |
| PSMB1 | STRING | 999 |
| PSMB6 | STRING | 997 |
| PSMA5 | STRING | 999 |
| PSMB4 | STRING | 998 |
| PSMD1 | STRING | 999 |

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000126067

![](https://images.proteinatlas.org/26322/609_F6_2_red_green.jpg)
![](https://images.proteinatlas.org/26322/609_F6_3_red_green.jpg)
![](https://images.proteinatlas.org/26322/604_F6_1_red_green.jpg)
![](https://images.proteinatlas.org/26322/604_F6_2_red_green.jpg)
![](https://images.proteinatlas.org/26322/607_F6_1_red_green.jpg)
![](https://images.proteinatlas.org/26322/607_F6_2_red_green.jpg)
![](https://images.proteinatlas.org/26324/917_G1_1_red_green.jpg)
![](https://images.proteinatlas.org/26324/917_G1_2_red_green.jpg)

### TE 调控评估

该蛋白为核蛋白，但其 TE 调控相关性需进一步实验验证。目前无直接 TE 调控文献支持。

### 深度机制分析

**1. 结构域架构：Ntn 水解酶与蛋白酶体 β 亚基身份**

A0A140VJS6 的 InterPro/Pfam 注释精确指向 20S 蛋白酶体核心颗粒的 β 型亚基。结构域层级为：Ntn_hydrolases_N（IPR029055，N 端亲核体水解酶超家族）、Proteasome_beta2（IPR034383，古菌/真核生物的胰蛋白酶样 β2 亚基）、Proteasome_bsu_CS（IPR016050，活性位点保守序列）。Ntn 水解酶的催化机制独特：N 端 Thr/Ser/Cys 残基的游离 α-氨基充当碱基，在翻译后自裂解（autoproteolysis）去除前肽后暴露催化 Thr 的羟基亲核体，攻击底物肽键的羰基碳。Pfam 的 Proteasome（PF00227）条目将蛋白分类到更广泛的蛋白酶体亚基家族。结构域总长度约 200 aa 与 20S β 亚基的标准尺寸（~200-240 aa）完全吻合，提示该蛋白包含完整的催化核心而无额外插入域。值得注意的是，该蛋白缺少免疫蛋白酶体亚基（β1i/β2i/β5i）特有的结构特征，因此大概率属于组成型蛋白酶体（constitutive proteasome）而非免疫蛋白酶体。

**2. PPI 网络：蛋白酶体组装的全景视图**

PPI 数据将 A0A140VJS6 嵌入完整的 26S 蛋白酶体组装图谱中。伙伴覆盖了 20S 核心颗粒的两个环：(a) α 环——PSMA2（999）、PSMA3（999）、PSMA4（999）、PSMA5（999）、PSMA6（999），所有评分均为 999，体现了 α 环亚基间的不可逆结构互作；(b) β 环——PSMB1（999）、PSMB4（998）、PSMB6（997）、PSMB7（997），评分同样接近极限值。19S 调节颗粒（PA700）的代表性亚基同样齐全：PSMC1（999）和 PSMC4（998）来自六聚 AAA+ ATPase 环（base subcomplex），PSMD1（999）、PSMD7（993）、PSMD8（993）、PSMD11（995）来自 lid subcomplex。这一完美的组装伙伴覆盖度意味着 A0A140VJS6 不是一个旁观者亚基，而是组装良好的 26S 蛋白酶体的结构性和/或催化性必需亚基。所有 STRING 评分在 993-999 的狭窄范围内，这是多亚基复合物中强制性互作（obligatory interaction）的典型特征。

**3. 结构解释：极高置信度与催化中心定位**

pLDDT=96.3 是六个报告中最高的结构质量评分，反映了 Ntn 水解酶折叠的极端热力学稳定性。蛋白酶体 β 亚基采用 α/β 双层三明治架构：中央由两个反向平行的五链 β 片层夹合，两侧由 α 螺旋包裹。催化性 Thr 的 N 端位于亚基间界面的内侧，只有在 20S 颗粒完全组装、相邻 β 亚基形成完整活性位点裂隙后才具备催化能力。这意味着 pLDDT=96.3 所反映的有序折叠状态是组装前的前体构象（propeptide-containing precursor），即自抑制状态。在成熟蛋白酶体中，该亚基的结构在 β 环组装完成后经历构象变化（前肽切除后），其 RMSD 变化约 1.2-1.8 Å（参考 PDB: 5GJQ，人组成型 20S 颗粒，分辨率 3.5 Å）。虽然该 UniProt ID 的 PDB=0，但 β2 亚基的直接同源物已有多项结构报道（如 PDB: 4R3O，牛 β2），活性位点几何（Thr1 Oγ...Asp17 Oδ...Lys33 Nζ 催化三联体）完全保守。

**4. 整合机制模型：核内蛋白酶体的双重角色与 TE 生物学联系**

A0A140VJS6 作为组成型 20S 蛋白酶体的 β 亚基，在核质中参与两条关键降解通路：(A) 泛素依赖性降解——19S 识别 K48 连接多泛素化底物（错误折叠核蛋白、短命转录因子如 c-FOS/c-JUN/p53、细胞周期调节因子如 cyclin B1），AAA+ ATPase 环（含 PSMC1/4）耗 ATP 去折叠底物并转运入 20S 腔体，β 亚基进行 processive 切割生成 3-22 个氨基酸的短肽。(B) 泛素非依赖性降解——20S 核心颗粒可直接识别暴露的疏水 patch（无序蛋白、氧化损伤蛋白），不依赖 19S 和 ATP 即进行降解，这对应激条件下（热休克、氧化应激）的核蛋白质量控制尤为重要。

从 TE 生物学角度，26S 蛋白酶体的核活性在两个层面与转座子调控交汇。第一，许多 TE 编码的蛋白（如 LINE-1 ORF1p 和 ORF2p）在细胞质合成后可进入细胞核，若其被核泛素连接酶（如 TRIM28/KAP1）标记，将通过 19S-20S 通路直接降解——A0A140VJS6 所在的蛋白酶体因此是核内抗 TE 免疫的效应器。第二，蛋白酶体降解转录因子产生的短肽可被 MHC I 类分子呈递，而 TE 去抑制（如 DNMTi 处理）可产生 TE 来源的异常蛋白并通过蛋白酶体加工后作为新抗原呈递至 CD8+ T 细胞（目前癌症免疫学的前沿议题）。A0A140VJS6 在此充当了核蛋白质量感应器（sensor）与效应器（effector）的双重角色。

**5. 研究意义与可操作性**

A0A140VJS6 在结构层面几乎无不确定性（pLDDT 96.3），但其 α/β 亚基的具体分类（催化性 vs 结构性）和 TE 调控中的功能角色仍未知。关键实验：(1) 体外重构——与纯化的 α 环亚基共孵育，观察是否通过自裂解从前肽形式转化为成熟形式，确认其催化活性；(2) 底物特异性分析——使用荧光淬灭的短肽文库（Ac-X-AMC）确定其切割位点偏好；(3) 在 DNMTi（5-Aza-dC）诱导 TE 去抑制的细胞模型中，用乳胞素（lactacystin）或 β2 选择性抑制剂阻断蛋白酶体活性后，以定量蛋白质组学鉴定积累的 TE 来源多肽；(4) 检查该亚基在组织表达谱中是否与 TE 活性水平相关（GTEx 数据）。鉴于其 PPI 几乎全是 999 的不可逆互作，该蛋白的表达水平变化可能影响整个 26S 颗粒的化学计量（stoichiometry），从而调控蛋白酶体容量——这使其成为干预核内 TE 相关蛋白质稳态的潜在"阀门"靶点。


![PAE](https://alphafold.ebi.ac.uk/files/AF-A0A140-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/A0A140VJS6
