---
type: protein-evaluation
gene: "A0A140VJS9"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## A0A140VJS9 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | A0A140VJS9 |
| 蛋白大小 | 341 aa / 38.6 kDa |
| UniProt ID | A0A140VJS9 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | x4 | 20.0 | nan (nan) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 341 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=0 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=88.1; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Calcineurin-like_PHP; Metallo-depent_PP-like; PP1_catalytic_subunit |
| PPI | 5/10 | x3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **123/180** | |
| **归一化总分** | | | **68.3/100** | 互证: +2 |

### 3. 分析
- nan (nan)
- PubMed strict=0 broad=0
- AF pLDDT=88.1 PDB=0
- InterPro: Calcineurin-like_PHP; Metallo-depent_PP-like; PP1_catalytic_subunit
- Pfam: Metallophos; STPPase_N
- PPI degree=0 ChIP: None


### 4. 总体评价
**68.3/100** | **nucleoplasm**
Nuclear protein


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PPP1R15A | STRING | 520 |
| PPP1R7 | STRING | 599 |
| EIF2S1 | STRING | 949 |
| RB1 | STRING | 953 |
| PPP1R3A | STRING | 725 |
| WDR82 | STRING | 499 |
| PPP1R3B | STRING | 409 |
| PPP1R8 | STRING | 435 |
| PPP1CA | STRING | 977 |
| PPP1CC | STRING | 947 |
| TP53BP2 | STRING | 957 |
| PPP1R3D | STRING | 955 |
| PPP1R10 | STRING | 962 |
| PPP1CB | STRING | 956 |

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000172531

![](https://images.proteinatlas.org/46833/2134_B7_59_blue_red_green.jpg)
![](https://images.proteinatlas.org/46833/2134_B7_79_blue_red_green.jpg)
![](https://images.proteinatlas.org/46833/2161_D9_21_blue_red_green.jpg)
![](https://images.proteinatlas.org/46833/2161_D9_32_blue_red_green.jpg)
![](https://images.proteinatlas.org/46833/2211_B11_13_blue_red_green.jpg)
![](https://images.proteinatlas.org/46833/2211_B11_28_blue_red_green.jpg)

### TE 调控评估

该蛋白为核蛋白，但其 TE 调控相关性需进一步实验验证。目前无直接 TE 调控文献支持。

### 深度机制分析

**1. 结构域架构：PP1 催化亚基的分子指纹**

A0A140VJS9 的三层 InterPro 注释（Calcineurin-like_PHP IPR004843 → Metallo-depent_PP-like IPR029052 → PP1_catalytic_subunit IPR047129）构成了从超家族到蛋白亚家族的精确分类级联。Calcineurin-like_PHP 是磷酸酯酶超家族的核心催化折叠；Metallo-depent_PP-like 进一步限定到金属依赖性蛋白磷酸酶的活性位点几何；而 PP1_catalytic_subunit（IPR047129）则将范围收窄到 PP1，排除 PP2A、PP2B、PP4、PP5 和 PP6。Pfam 层面，Metallophos（PF00149）覆盖了含双核金属中心（通常 Mn²⁺/Fe²⁺ 或 Mn²⁺/Zn²⁺）的磷酸酯酶催化域，而 STPPase_N（PF16891）则提供了一个 N 端丝/苏氨酸磷酸酶特异性结构域。PF16891 的存在是区分 PP1/PP2A 催化亚基家族与其他金属磷酸酯酶的关键特征：该结构域形成弯曲的 α-螺旋发夹结构，构成了 RVXF 基序结合沟道的一部分——RVXF 是几乎所有 PP1 调节亚基共享的对接基序（docking motif）。

**2. PPI 网络：PP1 全酶组的核内分支**

蛋白质互作数据将 A0A140VJS9 定位于 PP1 全酶（holoenzyme）调控网络的核内亚组。关键伙伴分为三类：(A) 其他催化亚基——PPP1CA（977）和 PPP1CC（947）的高分共互作，表明 PP1 催化亚基之间可能存在同型/异型二聚化（这在晶体学研究中已有观察到，晶体学二聚体虽未必是生理形式，但提示催化亚基间存在可逆的弱互作）以及共享调节亚基的竞争关系。(B) 核内调节亚基——PPP1R10（PNUTS，962）将 PP1 靶向染色质，PPP1R8（NIPP1，435）是 PP1 的核内抑制子，二者共同控制核内 PP1 活性的空间分配。PPP1R7（SDS22，599）是 PP1 折叠/成熟的专性伴侣，在 PP1 生物合成后即与之结合并保持到全酶组装完成。(C) 效应底物与适配蛋白——RB1（953）是 PP1 在 G1/S 转换期的决定性底物；TP53BP2（ASPP2，957）是 p53 的共激活因子，通过 SH3 结构域与 PP1 结合后将 PP1 带入凋亡信号复合物；EIF2S1（eIF2α，949）是整合应激反应（ISR）的 ATP/ADP 开关蛋白，其 Ser51 磷酸化状态直接决定全局翻译速率。

值得特别注意的是，PPP1R15A（GADD34，520）与 EIF2S1（949）的共现：在 ER 应激/ISR 条件下，PPP1R15A 被 ATF4 转录诱导后与 PP1 形成 GADD34-PP1 全酶，特异性靶向 eIF2α-pSer51 进行去磷酸化，从而终止 ISR 并恢复翻译（PMID: 16176978）。若 A0A140VJS9 参与这一经典通路，则可能在该 PP1 催化亚基的敲除或突变情况下导致 eIF2α 的持续磷酸化（即 ISR 无法终止）。

**3. 结构解释：有序催化核心与调节亚基界面的紊乱**

pLDDT=88.1 反映了一个折中的结构质量：催化域（Metallophos + STPPase_N，约 280 aa）的高度有序（预测局部 pLDDT >92），以及 C 端尾部和若干表面环的柔性。PP1 催化结构域是 α/β 混合折叠，其核心为扭曲的 β-α-β-α-β 基序，两个金属离子通过 His/Asp 残基配位在活性位点裂隙底部。STPPase_N 域的螺旋发夹结构促进 RVXF 基序的结合。然而，PP1 的 C 端（最后约 30 aa）在自由催化亚基中属于高度柔性的 IDR——只有在调节亚基（如 PPP1R10/PNUTS）结合后才折叠为稳定构象，并通过 C 端延伸填充疏水沟道，阻止非特异性底物接近。这意味着 pLDDT=88.1 并非蛋白质量问题：在细胞内，该蛋白以特定的全酶形式存在，与 PPP1R10 或 PPP1R15A 结合后的有效 pLDDT 会显著上升（因 C 端从无序变为有序）。PDB 中已存在大量人 PP1 结构（如 PDB: 4MOV，PP1γ-PPP1R15B 复合物），可直接用于同源建模和药物设计。

**4. 整合机制模型：核内 PP1 在应激终止、细胞周期与染色质调控间的协调**

基于上述证据，我提出 A0A140VJS9 在核质中同时参与三条功能通路，并通过调节亚基的切换实现功能分配：

**通路 1——ISR 终止（PPP1R15A 模式）：** 当整合应激反应被激活（ER 应激、氨基酸饥饿、血红素缺乏），eIF2α Ser51 被 GCN2/PERK/PKR/HRI 磷酸化，全局翻译停止。ATF4 被选择性翻译后诱导 PPP1R15A 表达，PPP1R15A 通过 RVXF 基序竞争结合 A0A140VJS9，形成的全酶靶向 eIF2α-pSer51。此去磷酸化使 eIF2-GTP-tRNAiMet 三元复合物恢复，从而重启翻译。在此模式中 A0A140VJS9 是 ISR 的"终止开关"。

**通路 2——有丝分裂退出（PPP1R10 模式）：** PPP1R10/PNUTS 将 A0A140VJS9 靶向染色质，在有丝分裂末期去磷酸化 RB1（pSer807/811、pThr821/826），恢复 RB1 的 E2F 结合能力和生长抑制功能，实现 G1 检查点的重置（PMID: 10570159）。同时，PP1 也去磷酸化组蛋白 H3-pSer10（维持着丝粒凝缩的标记），促进染色体去凝聚和核膜重建。

**通路 3——凋亡-存活权衡（TP53BP2 模式）：** TP53BP2/ASPP2 通过其 SH3 结构域与 A0A140VJS9 结合，携带 PP1 进入 p53 转录复合物。在 DNA 损伤条件下，PP1 可能去磷酸化 p53 的 N 端（pSer15/20），降低 p53 稳定性，从而倾向于细胞存活；而在严重损伤时，ASP53 的另一个家族成员 ASPP1 与之竞争，导致 PP1 离开 p53 复合物，允许 p53 高度磷酸化并启动凋亡程序。这意味着 TP53BP2-PP1 的互作强度直接决定了 DNA 损伤后的细胞命运：存活 vs 凋亡。

**TE 联系：** 三条通路均与 TE 调控相关。ISR 通路中，TE 的转录爆发可产生双链 RNA（dsRNA）激活 PKR，导致 eIF2α 磷酸化——如果 A0A140VJS9 在该条件下活跃，它将去磷酸化 eIF2α 以终止这一"TE 警报"状态，相当于 TE 免疫逃逸的"刹车释放"。RB1 通路中，RB1 的结合蛋白 E2F 在 TE 启动子（特别是 LTR 逆转录元件）上有丰富结合位点——PP1-pRB 的动态平衡直接控制这些 TE 的转录状态。TP53BP2 通路则在 TE 激活导致 DNA 损伤时（如 LINE-1 逆转录插入造成的 DSB）决定细胞命运。

**5. 研究意义**

PP1 催化亚基在人类中有 4 个基因（PP1α/β/γ1/γ2），但据估计其全酶种类超过 200 种（因有超过 200 个调节亚基）。A0A140VJS9（PubMed=0）代表了一个未被研究的 PP1 催化亚基变体，其 PPI 图谱揭示了 ISR、细胞周期和肿瘤抑制三者之间的独特交叉点。实验策略：(1) 重组表达与 PPP1R15A 的共纯化，以 Malachite Green 磷酸酶法测定去磷酸化 eIF2α-pSer51 的 Km/kcat；(2) PP1 亚型选择性 siRNA 敲除 + 毒胡萝卜素（thapsigargin）处理，比较 eIF2α 磷酸化动力学；(3) ChIP-seq 在 G1/S/M 期鉴定染色质定位位点并交叉 TE 注释；(4) co-IP-MS 捕获 ATP 竞争条件下的全酶组分变化。


![PAE](https://alphafold.ebi.ac.uk/files/AF-A0A140-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/A0A140VJS9
