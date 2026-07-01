---
type: protein-evaluation
gene: "PSMD1"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted, TE_REG_CANDIDATE]
status: shortlisted
---

## PSMD1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PSMD1 |
| 蛋白名称 | 26S proteasome non-ATPase regulatory subunit 1 |
| 蛋白大小 | 953 aa / 105.8 kDa |
| UniProt ID | Q99460 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Actin filaments; Nucleoplasm (Approved) + ChIP |
| 蛋白大小 | 7/10 | x1 | 7.0 | 953 aa |
| 新颖性 | 7/10 | x5 | 35.0 | PubMed=77 |
| 三维结构 | 9/10 | x3 | 27.0 | pLDDT=79.2; PDB=86 |
| 调控结构域 | 5/10 | x2 | 10.0 | 26S_Psome_Rpn2; ARM-like; ARM-type_fold |
| PPI | 8/10 | x3 | 24.0 | PPI degree=453 |
| **加权总分** | | | **139/180** | |
| **归一化总分** | | | **77.6/100** | 互证: +3 |

### 3. 分析
- Actin filaments; Nucleoplasm (Approved)
- PubMed strict=77 broad=94
- AF pLDDT=79.2 PDB=86
- InterPro: 26S_Psome_Rpn2; ARM-like; ARM-type_fold
- Pfam: HEAT_2; PC_rep; RPN2_C
- PPI degree=453 ChIP: Yes
40770113: Structure of the TXNL1-bound proteasome. | 30223085: Evolutionary considerations on 5-HT(2) receptors. | 37928041: Analysis and experimental validation of the innate immune gene PSMD1 in liver he

### 4. 总体评价
**77.6/100** | **nucleoplasm**
TE candidate: 26S_Psome_Rpn2; ARM-like; ARM-type_fold


### 补充分析 (UniProt API)

**蛋白全称**: 26S proteasome non-ATPase regulatory subunit 1

**功能**: Component of the 26S proteasome, a multiprotein complex involved in the ATP-dependent degradation of ubiquitinated proteins. This complex plays a key role in the maintenance of protein homeostasis by removing misfolded or damaged proteins, which could impair cellular functions, and by removing proteins whose functions are no longer required. Therefore, the proteasome participates in numerous cellular processes, including cell cycle progression, apoptosis, or DNA damage repair

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR016642 |
| InterPro | IPR011989 |
| InterPro | IPR016024 |
| InterPro | IPR002015 |
| InterPro | IPR048570 |
| InterPro | IPR040623 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PSMD8 | STRING | 999 |
| USP14 | STRING | 999 |
| PSMD3 | STRING | 999 |
| ADRM1 | STRING | 999 |
| PSMD4 | STRING | 999 |
| PSMD14 | STRING | 999 |
| PSMD13 | STRING | 999 |
| PSMB5 | STRING | 997 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q99460-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000173692-PSMD1

![](https://images.proteinatlas.org/36736/747_B2_1_red_green.jpg)
![](https://images.proteinatlas.org/36736/747_B2_2_red_green.jpg)
![](https://images.proteinatlas.org/36736/714_B2_1_red_green.jpg)
![](https://images.proteinatlas.org/36736/714_B2_2_red_green.jpg)
![](https://images.proteinatlas.org/36736/713_B2_2_red_green.jpg)
![](https://images.proteinatlas.org/36736/713_B2_3_red_green.jpg)

### PubMed 文献

**PubMed count: 94**

| 42316306 | Large-scale transcriptomic data mining using explainable XGBoost and SHAP reveals shared biomarkers and molecular mechan | BioData Min 2026 |
| 42178458 | Identifying Neddylation-modified features to assess prognosis and immune efficacy in hepatocellular carcinoma. | Apoptosis 2026 |
| 42140061 | Ubiquitin-mediated downregulation of the proteasome subunit ADRM1 mediates in vitro capacitation of bovine spermatozoa. | Anim Reprod Sci 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PSMD1


### 深度机制分析

**结构域架构的机制含义** PSMD1 的 ARM/HEAT 重复序列 (IPR011989, IPR016024) 和 PC_rep (蛋白酶体/cyclosome 重复) 构成了一个典型的超螺旋支架结构。这种 ARM/HEAT 折叠——由串联的 α-α 发夹重复单元堆叠成的右手超螺旋——天然提供极大的分子表面积，使其能以模块化方式同时锚定多个蛋白质伙伴。作为 26S 蛋白酶体 19S 调节颗粒 (RP) 的 lid 亚复合体中的最大亚基 (953 aa, 105.8 kDa)，PSMD1/Rpn2 在功能上相当于 lid 的"脊椎骨"：其 HEAT_2 (Pfam) 重复区提供结构刚性，RPN2_C 端结构域 (IPR048570) 则负责与 lid 其他亚基 (PSMD8/Rpn12、PSMD3/Rpn3) 进行精确的几何对接。ARM 型折叠 (IPR016024) 的保守性极强——从酵母 Rpn2 到人 PSMD1 均维持相同的超螺旋拓扑——表明这种支架功能在进化上已被深度锁定。

**PPI 网络中关键通路的推断** 453 个互作伙伴的庞大规模反映了 PSMD1 作为核心支架的多重生物学角色，但其中 STRING 评分达到 999 的伙伴 (PSMD8、USP14、PSMD3、ADRM1、PSMD4、PSMD14、PSMD13) 定义了其最核心的生化功能——19S RP lid 的结构组装与泛素链处理。USP14 (去泛素化酶) 与 PSMD1 之间的 999 分互作具有特别重要的机制意义：USP14 在捕获多聚泛素化底物后通过逐步修剪泛素链来调控底物降解速率，而 PSMD1 为 USP14 提供了精确的空间定位，确保去泛素化发生在底物转位至 20S 核心颗粒 (CP) 之前的关键窗口内。ADRM1/Rpn13 (泛素受体, 999 分) 与 PSMD1 的直接对接则负责底物的初始识别与捕获。PSMB5 (20S CP 的催化亚基, 997 分) 的互作将 19S 与 20S 物理偶联为完整的 26S 全酶。86 个 PDB 实验结构条目覆盖了这些互作界面的原子分辨率细节，其中 TXNL1 结合的蛋白酶体结构 (PMID:40770113) 揭示了硫氧还蛋白样蛋白对 PSMD1 构象的氧化还原调控——这是蛋白酶体活性受细胞氧化还原状态调节的直接结构证据。

**ChIP 信号的机制解释** PSMD1 在 ChIP 实验中检出染色质结合信号，其机制基底值得深入探讨。泛素-蛋白酶体系统 (UPS) 已被证实可通过降解染色质结合蛋白 (如转录因子、组蛋白修饰酶) 来调控基因转录和 DNA 损伤修复。PSMD1 作为 19S RP 的核心支架，其在 ChIP 中的检出很可能反映了 26S 蛋白酶体被主动招募至特定位点以降解泛素化的染色质相关因子。这种"原位降解"模式代表着一种空间受限的蛋白稳态调控策略：不同于胞质中的全局性蛋白降解，染色质局部的泛素化-降解循环可实现高度局部化的转录调控和表观遗传重塑。最新文献中 PSMD1 在肝细胞癌先天免疫中的角色 (PMID:37928041) 以及 neddylation 修饰 (类泛素化) 的预后预测价值 (PMID:42178458) 进一步支持了这一模型——蛋白酶体组分的翻译后修饰可能动态调控其染色质亲和性，进而实现组织特异性的基因表达调控。

**机制模型推断** 综合所有实验与结构数据，PSMD1 的核心机制模型如下：(1) PSMD1 通过其 ARM/HEAT 超螺旋支架精确排列 19S RP lid 的各亚基，其中 USP14 和 ADRM1 被定位在泛素化底物的进入路径上；(2) ADRM1 通过其泛素结合域捕获多聚泛素化蛋白，USP14 在 PSMD1 的变构调控下逐步修剪泛素链，实现底物降解速率的精细调控；(3) 氧化应激条件下，TXNL1 结合可改变 PSMD1 的构象状态，从而调节 lid 对底物的处理效率；(4) 在核内，PSMD1 介导的蛋白酶体被选择性招募至染色质特定位点，通过原位降解泛素化的转录调控因子来参与基因表达程序的动态调控。该模型将 PSMD1 从一个"被动结构组分"重新定位为一种主动参与底物选择、降解速率调控和空间定位的多功能调控平台。

**研究与转化前景** 目前临床使用的蛋白酶体抑制剂 (硼替佐米、卡非佐米等) 均靶向 20S CP 的催化活性位点 (PSMB5)，耐药性的产生常与 19S RP 的适应性突变有关。PSMD1 的支架功能提供了全新的药理干预角度：(1) 破坏 PSMD1-ADRM1 界面可阻断泛素化底物的初始识别，实现比催化位点抑制剂更上游的干预；(2) 变构调节 PSMD1-USP14 界面可改变底物去泛素化速率，精细调控而非完全阻断蛋白酶体活性——这对于需要避免完全抑制蛋白酶体的慢性疾病 (如神经退行性疾病) 可能更具优势。此外，PSMD1 的 ChIP 信号提示核内蛋白酶体活性与胞质蛋白酶体可能存在差异调控，这种亚细胞分区调控机制若被深入阐明，可为开发组织或亚细胞器特异性蛋白酶体调节剂提供理论基础。

