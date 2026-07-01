---
type: protein-evaluation
gene: "A0A140VJZ1"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## A0A140VJZ1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | A0A140VJZ1 |
| 蛋白大小 | 858 aa / 95.8 kDa |
| UniProt ID | A0A140VJZ1 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | x4 | 20.0 | nan (nan) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 858 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=0 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=79.5; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Papain-like_cys_pep_sf; Peptidase_C19_UCH; Ub_carboxyl-term_hydrolase |
| PPI | 5/10 | x3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **118/180** | |
| **归一化总分** | | | **65.0/100** | 互证: +1 |

### 3. 分析
- nan (nan)
- PubMed strict=0 broad=0
- AF pLDDT=79.5 PDB=0
- InterPro: Papain-like_cys_pep_sf; Peptidase_C19_UCH; Ub_carboxyl-term_hydrolase
- Pfam: UBA; UCH; zf-UBP
- PPI degree=0 ChIP: None


### 4. 总体评价
**65.0/100** | **nucleoplasm**
Nuclear protein


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| USP5 | STRING | 819 |
| USP14 | STRING | 678 |
| ZNF629 | STRING | 550 |
| RPS27A | STRING | 435 |
| ZNF436 | STRING | 549 |
| UBA1 | STRING | 462 |
| USP7 | STRING | 701 |
| UCHL5 | STRING | 477 |
| UCHL3 | STRING | 510 |
| ZNF763 | STRING | 820 |
| USP25 | STRING | 469 |
| UBA52 | STRING | 999 |
| UBC | STRING | 821 |

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000111667

![](https://images.proteinatlas.org/6756/8_B3_1_red_green.jpg)
![](https://images.proteinatlas.org/6756/8_B3_2_red_green.jpg)
![](https://images.proteinatlas.org/6756/9_B3_1_red_green.jpg)
![](https://images.proteinatlas.org/6756/9_B3_2_red_green.jpg)
![](https://images.proteinatlas.org/6756/7_B3_1_red_green.jpg)
![](https://images.proteinatlas.org/6756/7_B3_2_red_green.jpg)
![](https://images.proteinatlas.org/6756/344_E2_1_red_green.jpg)
![](https://images.proteinatlas.org/6756/344_E2_2_red_green.jpg)

### TE 调控评估

该蛋白为核蛋白，但其 TE 调控相关性需进一步实验验证。目前无直接 TE 调控文献支持。

### 深度机制分析

**1. 结构域架构：杂交型去泛素化酶的领域图谱**

A0A140VJZ1 的结构域组合在 DUB 家族中极具异质性。InterPro 层级自顶向下为：Papain-like_cys_pep_sf（IPR038765，木瓜蛋白酶样半胱氨酸肽酶超家族折叠）、Peptidase_C19_UCH（IPR001578，泛素 C 端水解酶催化核心）、Ub_carboxyl-term_hydrolase（IPR018200，UCH 活性位点保守序列）。Pfam 则揭示了三个结构域：UCH（PF00443，催化域）、UBA（PF00627，泛素结合域，识别 K48/K63 连接的多聚泛素链）、zf-UBP（PF02148，USP 型锌指，常见于 USP 家族而非经典 UCH）。858 aa 中有三个已注释结构域仅覆盖约 350 aa，剩余约 500 aa 的区域可能是无结构域插入（domainless insertion）、长 IDR 或尚未被数据库收录的新结构域。UBA + UCH + zf-UBP 的并存非常罕见：UBA 提供链识别，UCH 提供 C 端水解，zf-UBP 提供游离泛素或底物蛋白的识别面——这暗示 A0A140VJZ1 是一个"多合一"（all-in-one）DUB，可以在不依赖额外衔接蛋白的情况下完成对泛素化底物的识别、结合和去泛素化。

UCH 家族的标准行为是"修剪"（trimming）小的 C 端泛素加合物，而非深入多聚链内部切割——但 A0A140VJZ1 的 UBA 结构域赋予了链的结合能力，这可能在进化上赋予了它 USP 样（链内切割）的扩展功能，介导一种"杂交型"去泛素化模式：先由 UBA 抓住多聚泛素链的锚点，再由 UCH 域在近端切割，释放完整泛素单体或短链。

**2. PPI 网络：泛素系统的核心回路**

PPI 伙伴全面覆盖了泛素-蛋白酶体系统的五大功能模块：(A) 泛素前体——UBA52（999，Ub-核糖体融合蛋白 RPL40）、RPS27A（435，Ub-核糖体融合蛋白 S27a），二者是新生泛素的主要来源。UBA52 评分 999 意味着 A0A140VJZ1 可能与核糖体上的泛素前体直接相互作用，参与泛素的翻译中或翻译后加工（co-/post-translational processing），这通常是 UCHL3/UCHL1 的功能（PMID: 12000784）。(B) 游离泛素链——UBC（821，polyubiquitin-C 编码的线性头尾缩合的泛素多聚前体），经 DUB 切割后释放单个泛素单位。(C) E1 酶——UBA1（462），泛素激活酶。(D) 其他 DUB——USP5（819，异肽酶 T，回收 K48 非锚定泛素链，PMID: 10409652）、USP7（HAUSP，701，p53/MDM2/H2B 的去泛素化酶，PMID: 15361863）、USP14（678，蛋白酶体相关 DUB，PMID: 12060724）、USP25（469，IL-17 信号负调控）、UCHL3（510，UCH 家族同源物）、UCHL5（UCH37，477，19S 蛋白酶体 lid 组分）。(E) 锌指蛋白——ZNF763（820）、ZNF629（550）、ZNF436（549）。

ZNF763 评分 820 是最引人注目的非典型伙伴。C2H2 锌指蛋白是基因组靶向的主力——KRAB-ZFP 家族通过其锌指阵列识别 TE 序列并募集 KAP1/TRIM28-SETDB1 复合物进行 H3K9me3 沉积（PMID: 17512414）。若 ZNF763 将 A0A140VJZ1 招募到特定的基因组位点，该 DUB 可能在那些位置去除底物的泛素修饰——可能是组蛋白 H2A（K119ub，Polycomb 抑制标记）或 H2B（K120ub，转录活跃标记），从而直接参与染色质状态的调控。

**3. 结构解释：局部有序-全局柔性的杂交结构**

pLDDT=79.5（857 aa）提示 A0A140VJZ1 呈现明显的区域差异化的折叠模式。三个已知结构域各自的预期局部 pLDDT：(1) UCH 域（约 230 aa）——极高置信度（>90），木瓜蛋白酶样折叠由中央六链 β 片层夹合 α 螺旋，催化三联体 Cys-His-Asp 位于表面裂隙深处；(2) UBA 域（约 45 aa）——高置信度（>85），紧凑的三螺旋束以疏水 patch（含 Met-Gly-Tyr 保守基序）识别泛素的 Ile44 疏水面；(3) zf-UBP 域（约 70 aa）——中高置信度（>80），锌指核心由 4 个 Cys/His 配位 Zn²⁺，形成与 Ub 结合的疏水 platform。总 pLDDT 被 500+ aa 的 IDR 和长连接环拉低到 79.5。这种架构与 USP7（HAUSP）高度类似——USP7 也有催化域 + 多个 Ub 结合域 + 长的调节性 IDR，其全长蛋白在无底物时也呈现扩展构象（extended conformation）和中等 pLDDT。

结构上最重要的未解决问题是：UCH 催化域（截短版本）是否可以独立催化？还是需要 UBA/UBP 域的存在（domain-dependent activity）？USP7 的 HUBL 域（泛素样折叠）在分子内自抑制催化域，直到被底物或伙伴（如 GMPS）解除。A0A140VJZ1 中是否也存在类似的分子内自抑制需要实验确认。

**4. 整合机制模型：核内 DUB 在染色质泛素动态平衡与抗 TE 免疫间的协调**

基于以上证据，我提出 A0A140VJZ1 在核质中的三层功能模型：

**层 1——泛素稳态维护（Housekeeping）：** 在核质中，A0A140VJZ1 主要处理泛素前体（UBA52/RPS27A）和游离多聚泛素链（UBC）的加工。UBA52（999）的高置信度互作表明该蛋白可能是泛素从核糖体上释放的关键 DUB——类似于 UCHL3 在胞质中的功能但在核内执行。通过 UBA 域的链结合功能和 UCH 域的水解活性，它可以编辑（edit）K48/K63 链的末端，防止非锚定泛素链的积累（非锚定链会竞争性抑制 19S 蛋白酶体泛素受体，导致蛋白质毒性）。

**层 2——染色质去泛素化（Chromatin DUB）：** ZNF763（820）的强互作暗示 A0A140VJZ1 是一个被锌指蛋白靶向的染色质 DUB。若 ZNF763 识别特定的 TE 序列（如 SVA/L1PA/LTR），它将招募 A0A140VJZ1 至该区域。A0A140VJZ1 可能在三个位点发挥去泛素化作用：(a) H2A-K119ub→H2A，解除 PRC1 介导的抑制，允许 TE 转录；(b) H2B-K120ub→H2B，降低转录延伸效率（因为 H2Bub 是 FACT 招募所需的标记）；(c) KAP1/TRIM28 本身是泛素化底物（USP7 已知可去泛素化并稳定 KAP1）——A0A140VJZ1 可能通过 USP7（701）的协同作用承担上游的泛素再循环功能。

**层 3——TE 来源蛋白的去泛素化与免疫逃逸：** 若 TE 编码的蛋白（如 LINE-1 ORF1p/ORF2p）在核内合成后被泛素化标记（作为"non-self"信号），A0A140VJZ1 可能通过去泛素化解除这一降解信号，使 TE 蛋白在核内积累。这在功能上等同于病毒的 DUB 活性（如 KSHV ORF64、SARS-CoV-2 PLpro），但是人类内源性的——这可能代表了一种内源化的病毒 DUB 模拟机制（molecular mimicry），帮助 TE 在长期共进化中逃避宿主降解系统。

**5. 研究意义**

A0A140VJZ1 是这批报告中的"沉睡巨人"：858 aa 的大型蛋白、独特的 UBA-UCH-zfUBP 三结构域架构、完全新颖（PubMed=0）、且与 ZNF763（820）和 USP7（701）存在高置信度互作。实验策略：(1) Ubiquitin-AMC / Ubiquitin-rhodamine 底物测定 UCH 催化域的水解速率；(2) 二泛素（K48/K63/Met1 连接）切割实验区分链切割模式（exo/endo）；(3) ZNF763 ChIP-seq 基因组定位，联合 A0A140VJZ1 CUT&RUN 验证染色质招募；(4) DUB 特异性抑制剂（如 PR-619 广谱 DUBi）处理后定量组蛋白泛素化变化；(5) LINE-1 retrotransposition reporter assay（L1-EGFP）评估 DUB 活性对 TE 转座的影响。


### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/A0A140VJZ1
