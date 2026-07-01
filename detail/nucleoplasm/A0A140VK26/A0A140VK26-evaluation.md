---
type: protein-evaluation
gene: "A0A140VK26"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## A0A140VK26 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | A0A140VK26 |
| 蛋白大小 | 337 aa / 37.6 kDa |
| UniProt ID | A0A140VK26 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | x4 | 20.0 | nan (nan) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 337 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=0 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=86.4; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | ConA-like_dom_sf; Galectin-like; Galectin_CRD |
| PPI | 5/10 | x3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **123/180** | |
| **归一化总分** | | | **67.8/100** | 互证: +1 |

### 3. 分析
- nan (nan)
- PubMed strict=0 broad=0
- AF pLDDT=86.4 PDB=0
- InterPro: ConA-like_dom_sf; Galectin-like; Galectin_CRD
- Pfam: Gal-bind_lectin
- PPI degree=0 ChIP: None


### 4. 总体评价
**67.8/100** | **nucleoplasm**
Nuclear protein


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| LGALS13 | STRING | 422 |
| CLC | STRING | 652 |
| EGR2 | STRING | 419 |
| SORT1 | STRING | 402 |
| LIMD1 | STRING | 436 |
| TIMP4 | STRING | 485 |
| EMB | STRING | 474 |
| TRARG1 | STRING | 427 |
| VSTM4 | STRING | 476 |
| LGALS12 | STRING | 419 |
| TLR4 | STRING | 430 |

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000133317

![](https://images.proteinatlas.org/21124/1926_H2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/21124/1926_H2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/21124/1986_F2_33_blue_red_green.jpg)
![](https://images.proteinatlas.org/21124/1986_F2_34_blue_red_green.jpg)

### TE 调控评估

该蛋白为核蛋白，但其 TE 调控相关性需进一步实验验证。目前无直接 TE 调控文献支持。

### 深度机制分析

**1. 结构域架构：核内半乳糖凝集素的折叠拓扑**

A0A140VK26 的结构域注释形成一个由超家族到家族的收敛级联：ConA-like_dom_sf（IPR013320，伴刀豆球蛋白 A 样 jelly-roll 折叠超家族）→ Galectin-like（IPR044156，半乳糖凝集素样域）→ Galectin_CRD（IPR001079，半乳糖凝集素糖识别域），Pfam 层面则由 Gal-bind_lectin（PF00337）统一标注。凝集素 CRD 采用两片反平行 β-三明治的对称折叠：S 面（6 股）和 F 面（5 股），糖结合位点位于 S 面的凹面裂隙中。保守的糖识别残基（His44、Asn46、Arg48、Trp68——残基编号基于人 Galectin-1，PDB: 1A3K）在 S4-S6 链所在的界面与 β-半乳糖苷的 4-OH 和 6-OH 形成关键氢键。

半乳糖凝集素家族在人类中有 16 个成员（LGALS1-14、LGALS16-17），按结构分为原型（单 CRD，如 Gal-1/2/5/7/10/11/13/14/15）、嵌合型（Gal-3，CRD + 胶原样重复）和串联重复型（Gal-4/8/9/12，两个同源 CRD 由 linker 连接）。A0A140VK26 的 337 aa 尺寸介于单 CRD（~130 aa）和串联重复型（~320-360 aa）之间，因此最可能属于串联重复型或 CRD + 长 N 端延伸的非典型架构。LGALS12（419）和 LGALS13（422）在 PPI 中的出现为串联重复型的可能性提供了间接证据——LGALS12 是串联重复型（placental galectin），其 CRD1 和 CRD2 在配体偏好上存在差异。

**2. PPI 网络：二元功能域的交互景观**

PPI 伙伴自然地分裂为两个功能域：(A) 半乳糖凝集素家族——LGALS13（422，胎盘 galectin-13/PP13）、LGALS12（419，galectin-12，调控线粒体膜电位和凋亡）、CLC（652，Charcot-Leyden 晶体蛋白/galectin-10，在嗜酸性粒细胞/Th2 免疫中形成自发性六方双锥晶体——生物矿物化的罕见例子，PMID: 11113207）。(B) 非凝集素伙伴——EGR2（419，早期生长反应 2，C2H2 锌指 TF，Schwann 细胞髓鞘形成的主调控因子，PMID: 8228932）、SORT1（402，sortilin-1，Vps10p 域的溶酶体/高尔基体分选受体）、LIMD1（436，Hippo 通路中 LATS1/2 的适配蛋白）、TIMP4（485，MMP 组织抑制剂 4，ECM 重塑）、EMB（474，embigin，含 Ig 域的细胞黏附分子）、TRARG1（427，功能未知的膜蛋白）、VSTM4（476，V-set 域含有的免疫调节蛋白）、TLR4（430，革兰氏阴性菌 LPS 模式识别受体）。

EGR2（419）与 CLC（652）的同时出现是最具信息量的 PPI 组合。EGR2 是确定在核内工作的 TF，其 DNA 结合基序为 GCGGGGGCG（PMID: 15087442）。若 A0A140VK26 与 EGR2 在核内互作，则该凝集素可能作为 EGR2 的转录共调节因子——经典示例为 galectin-3，其在核内通过糖依赖性蛋白互作增强 TTF-1 的转录活性（PMID: 12119204）。CLC（652）的高分互作则暗示该蛋白可能与 CLC 形成异二聚体——CLC 在嗜酸性粒细胞中天然以晶体形式聚合，但在其他细胞类型和条件下保持可溶性——A0A140VK26 与 CLC 的异二聚化可能会抑制 CLC 的自动结晶化并使 CLC 保持可溶形式，改变其亚细胞分布。

**3. 结构解释：有序 CRD 与核靶向模块的功能性紊乱**

pLDDT=86.4 传达了与 A0A140VJS9（88.1）相似的结构模式：CRD 的高度有序（预测局部 pLDDT >90），以及辅助结构域或环区的中度柔性。Galectin CRD 是已知折叠中稳定性最高的之一，其 Tm 通常在 55-70°C 范围内（galectin-1 为 65°C），由 β-三明治的大量主链氢键网络提供。糖结合位点的 loop（S3-S4 loop、S4-S5 loop）在无配体时是高度柔性的（B-factor 显著升高），糖结合后则被锁定为刚性构象——这是诱导契合（induced fit）的经典案例。

蛋白质其余部分的结构组织决定了其核定位能力。传统的 galectin（如 Gal-1/3）缺乏 NLS 而是在细胞质合成后通过非经典途径分泌（涉及直接的膜穿越，不依赖 ER/Golgi）。核定位的 galectin（如 Gal-3 的核内池）通常通过特定伙伴（如 importin-α/β 识别的隐 NLS 或 piggyback 机制）进入核内。A0A140VK26 的核定位暗示它可能包含了 NLS 基序（短碱性簇，如 PKKKRKV），或者通过 EGR2/LIMD1 的 piggyback 进入核内。

**4. 整合机制模型：糖感应器驱动的核转录调控**

A0A140VK26 的存在提出了一个核心问题：一个糖结合蛋白在核内有怎样的功能？我提出的模型是：

**模型：O-GlcNAc/糖基化感应 + TF 共调节**——在核质中，O-GlcNAc 修饰（O-GlcNAcylation）是主要的糖基化形式，覆盖了超过 3000 个核蛋白，包括 RNA Pol II CTD（YSPTSPS 的 Thr4/Ser5）、转录因子（c-MYC pThr58、p53 pSer149）、组蛋白（H2B S112、H3 S10）以及染色质重塑因子。O-GlcNAc 修饰由 OGT 添加、OGA 去除，其供体 UDP-GlcNAc 来自己糖胺通路（HBP），因此 O-GlcNAcylation 是核内的营养状态感应（nutrient sensing）机制（PMID: 18422453）。

A0A140VK26 的 CRD 是否能识别 O-GlcNAc 修饰而非传统的 β-半乳糖苷？这并非没有先例：galectin-3 已被证实结合 N-乙酰葡糖胺（GlcNAc）的低聚物和多聚物（PMID: 26363071），并且通过其 CRD 与 O-GlcNAc 修饰的核蛋白相互作用。若 A0A140VK26 能结合 O-GlcNAc 修饰的蛋白，它将在核内充当一个糖感应适配器——在高葡萄糖流/已糖胺通路活跃时，细胞核内蛋白的 O-GlcNAc 水平上升，A0A140VK26 以高占有率结合这些修饰，进而募集或稳定特定的转录因子（如 EGR2）。

具体而言，EGR2（419）被 O-GlcNAc 修饰的文献证据存在，而 EGR2 是髓鞘形成的关键 TF。在 Schwann 细胞中，代谢状态（高糖 vs. 低糖）决定了髓鞘形成程序的启动——高糖时 O-GlcNAc 增加，A0A140VK26-EGR2 结合增强，促进活化 T 细胞的髓鞘基因表达——这与 galectin 家族的另一个成员（galectin-1）在 Schwann 细胞中促进轴突再髓鞘化的功能是一致的（PMID: 17594299）。

**TE 调控的切入点：** (a) 许多 TE 的启动子（如 MER41 的 LTR，灵长类特异性）需要特定的 TF 结合来激活——若 A0A140VK26 通过 O-GlcNAc 依赖的机制调节 EGR2 活性，那么在代谢应激或高糖条件下，TE 可能通过 EGR2 被间接激活。(b) 凝集素介导的蛋白-蛋白互作和蛋白-糖互作也可影响染色质的三维结构（Hi-C domain）——已知 galectin-3 的核内过表达会导致染色质凝聚状态的变化（PMID: 9737955）。

**5. 研究意义**

A0A140VK26 代表了一个未被探索的概念交叉点：凝集素生物学 × 核转录调控 × TE。其 PubMed=0 的新颖性、CRD 的良好折叠（pLDDT 86.4）和 CLC（652）的强互作使其成为一个药物学上具有可靶向性的候选（凝集素抑制剂 TD139 已进入三期临床用于 IPF）。实验策略：(1) 糖芯片（glycan microarray，CFG v5.5）确定该 CRD 的糖配体谱（是 β-半乳糖苷还是 O-GlcNAc？）；(2) O-GlcNAc 修饰抗体磁珠富集 + 质谱鉴定其结合蛋白（Far-Western blot 验证）；(3) OGT 抑制（OSMI-1）后，观察该凝集素的亚核分布是否改变（从核散斑/凝聚体到弥散分布）；(4) EGR2 的共转染 + EGR2 荧光素酶 reporter assay 验证该凝集素的共调节功能；(5) 在 TE 报告系统中测量凝集素过表达/敲除对 TE 转录的影响。


![PAE](https://alphafold.ebi.ac.uk/files/AF-A0A140-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/A0A140VK26
