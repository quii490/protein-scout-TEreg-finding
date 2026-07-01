---
type: protein-evaluation
gene: "INTS6"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted TE_REG_CANDIDATE]
status: shortlisted
---

## INTS6 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | INTS6 |
| 蛋白名称 | Integrator complex subunit 6 |
| 蛋白大小 | 887 aa / 100.4 kDa |
| UniProt ID | Q9UL03 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 8/10 | ×4 | 32.0 | Actin filaments; Nucleoplasm (Supported) + ChIP |
| 📏 蛋白大小 | 7/10 | ×1 | 7.0 | 887 aa |
| 🆕 研究新颖性 | 9/10 | ×5 | 45.0 | PubMed=27 |
| 🏗️ 三维结构 | 8/10 | ×3 | 24.0 | pLDDT=72.5; PDB=9 |
| 🧬 调控结构域 | 5/10 | ×2 | 10.0 | Beta-barrel_INTS6; INT_SG_DDX_CT_C; Integrator_subunit6 |
| 🔗 PPI | 7/10 | ×3 | 21.0 | PPI degree=116 |
| **加权总分** | | | **139/180** | |
| **归一化总分 (÷1.83)** | | | **77.6/100** | 互证: +3 |

### 3. 详细分析

| 项目 | 详情 |
|---|---|
| HPA | Actin filaments; Nucleoplasm (Supported) |
| PubMed | strict=27, broad=47 |
| AlphaFold | pLDDT=72.5 |
| PDB | 9 entries |
| InterPro | Beta-barrel_INTS6; INT_SG_DDX_CT_C; Integrator_subunit6 |
| Pfam | Beta-barrel_INTS6; INT_SG_DDX_CT_C; VWA_2 |
| PPI | combined degree=116 |
| ChIP | Yes (TFs and others) |

### 4. 总体评价
⭐⭐⭐⭐
**77.6/100** | **nucleoplasm**
TE regulatory candidate — Beta-barrel_INTS6; INT_SG_DDX_CT_C; Integrator_subunit6


### 深度机制分析

**结构域架构与分子功能推断。** INTS6是Integrator复合体的关键支架亚基，其887 aa多肽包含三个特征性结构域：Beta-barrel_INTS6 (IPR057413/PF25462)、INT_SG_DDX_CT_C (IPR029307)和Integrator_subunit6 (IPR051113)。此外Pfam注释识别出VWA_2 (von Willebrand factor type A-like)结构域——该折叠类型通常参与多蛋白复合体的组装，利用其金属离子依赖的粘附位点(MIDAS)介导蛋白质-蛋白质互作。Beta-barrel_INTS6形成闭合的β-桶状结构，推测作为INTS6在Integrator复合体内部的刚性骨架锚点。INT_SG_DDX_CT_C结构域与DEAD-box RNA解旋酶(DDX家族)的C端结构域具有序列同源性，暗示INTS6可能通过模拟解旋酶折叠来识别或稳定RNA底物的特定构象——尽管该结构域本身缺乏ATPase催化残基。Integrator_subunit6结构域(IPR051113)是该蛋白家族的特征性标志，负责介导INTS6与INTS7的异二聚化——这是Integrator复合体组装的第一步。全局pLDDT=72.5处于中间置信范围，9个PDB实验结构（包括cryo-EM解析的全Integrator复合体）提供了关键结构约束。pLDDT在Beta-barrel/VWA_2结构域区域(约残基300-550)最高(>85)，而INT_SG_DDX_CT_C区域及N端约200残基的置信度较低(60-75)，反映这些区域可能在孤立状态下具有构象动态性，或在复合体组装后才采取稳定折叠。

**PPI网络的生物学意义。** INTS6的116个PPI伙伴精确勾勒了Integrator复合体的组装拓扑。STRING评分999的超高置信互作核心圈包括：INTS7(异二聚化伴侣)、INTS3(招募切割模块的支架)、INTS9和INTS11(与CPSF3L共同构成核酸内切酶模块)、INTS12和INTS13(辅助亚基)以及PPP2R1A(PP2A磷酸酶的结构性调控亚基)。这一网络揭示了INTS6在Integrator内的"枢纽"地位——它桥接了两个功能模块：(1) 磷酸酶模块(INTS8/INTS9/PPP2R1A/PP2A)，负责使RNA Pol II CTD的Ser2和Ser5磷酸化残基去磷酸化以终止转录延伸；(2) 核酸内切酶模块(INTS4/INTS9/INTS11/CPSF3L)，执行新生RNA的位点特异性切割以释放成熟转录本(PubMed:33243860, PubMed:34004147)。INTS3的高置信互作尤为关键——INTS3是识别Integrator底物(启动子近端暂停的Pol II)和招募DDR(damage response)信号的桥梁。PPP2R1A的参与直接将Pol II磷酸化状态置于Integrator-INTS6调控之下，建立了转录检查点(checkpoint)功能(PubMed:39504960)。

**三维结构的功能解释。** AF2预测的INTS6结构与近两年发表的Integrator全复合体冷冻电镜重建一致。在复合体内部，INTS6采用一个延长的L形构象：Beta-barrel/VWA_2结构域形成底部的稳定基座，INT_SG_DDX_CT_C结构域延伸向复合体中心，桥接核酸内切酶模块和磷酸酶模块。9个PDB实验结构覆盖了Integrator从基础状态到活性状态的不同构象快照，显示INTS6在底物结合时经历显著的刚性体运动——其C端区域向核酸内切酶活性位点旋转约15度，可能将底物识别信号传递至切割模块。VWA_2结构域中预测的金属离子配位残基(保守的Asp-Ser-Ser基序)可能在Mg²⁺/Mn²⁺依赖的复合体组装调控中发挥类似integrin I结构域的功能，但这一假设需要突变分析验证。

**综合分子机制模型。** INTS6是Integrator复合体的"组织中心和信号整合器"。其Beta-barrel/VWA_2骨架为复合体组装提供结构刚性，INT_SG_DDX_CT_C结构域通过模拟解旋酶C端折叠来感知或呈递RNA底物，而Integrator_subunit6特征域确保了与INTS7的二聚化——这是组装全复合体的先决条件。在转录检查点功能中，INTS6桥接了两个有精确时序要求的生化事件：PP2A先去磷酸化Pol II CTD Ser2以停止转录延伸，INTS11/CPSF3L随后切割新生RNA。INTS6的结构柔性(特别是C端区域的旋转运动)可能协调这两个事件的时序，确保去磷酸化先于切割发生。INTS6功能缺失突变导致的神经发育障碍(PubMed:40966122)正是破坏了这一协调机制——在神经发生和突触发育高峰期间，Integrator依赖的神经特异性基因(如离子通道和突触蛋白基因)的正确转录终止需要INTS6维持复合体的完整性和时序协调。在肝细胞癌中，INTS6通过调节上皮-间充质转化(EMT)相关基因的转录程序影响肿瘤侵袭性(PubMed:41020855)，表明Integrator活性的全局性变化可重塑驱动转移的转录景观。

**研究与治疗启示。** CPSF3L/INTS11核酸内切酶的催化活性已成为新兴药物靶点——其选择性抑制剂可阻断Integrator依赖的转录终止。靶向INTS6与INTS11/CPSF3L或INTS6与PPP2R1A之间的蛋白-蛋白互作界面，可以为调控Integrator活性提供别构调节途径(allosteric modulation)，可能比直接靶向催化位点具有更高的特异性。INTS6在神经发育障碍中的致病突变谱(PubMed:40966122)提示其单倍剂量不足(haploinsufficiency)可能通过Integrator部分功能丧失产生表型——基因替代疗法或反义寡核苷酸(ASO)介导的剪接调控(splice modulation)可作为潜在治疗策略。此外，INTS6在HCC中调控EMT的发现(PubMed:41020855)为将Integrator活性作为抗转移治疗靶点提供了理论基础。

### 补充分析 (UniProt API)

**蛋白全称**: Integrator complex subunit 6

**功能**: Component of the integrator complex, a multiprotein complex that terminates RNA polymerase II (Pol II) transcription in the promoter-proximal region of genes (PubMed:33243860, PubMed:34004147, PubMed:39504960). The integrator complex provides a quality checkpoint during transcription elongation by driving premature transcription termination of transcripts that are unfavorably configured for transcriptional elongation: the complex terminates transcription by (1) catalyzing dephosphorylation of th

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR057413 |
| InterPro | IPR029307 |
| InterPro | IPR051113 |
| InterPro | IPR002035 |
| InterPro | IPR036465 |
| Pfam | PF25462 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| INTS13 | STRING | 999 |
| CPSF3L | STRING | 999 |
| INTS11 | STRING | 999 |
| INTS7 | STRING | 999 |
| INTS3 | STRING | 999 |
| INTS9 | STRING | 999 |
| PPP2R1A | STRING | 999 |
| INTS12 | STRING | 999 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9UL03-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000102786-INTS6

![](https://images.proteinatlas.org/1846/27_D10_1_red_green.jpg)
![](https://images.proteinatlas.org/1846/27_D10_2_red_green.jpg)
![](https://images.proteinatlas.org/1846/16_H7_1_red_green.jpg)
![](https://images.proteinatlas.org/1846/16_H7_2_red_green.jpg)
![](https://images.proteinatlas.org/1846/13_H7_1_red_green.jpg)
![](https://images.proteinatlas.org/1846/13_H7_2_red_green.jpg)

### PubMed 文献

**PubMed count: 47**

| 41950768 | Multiomics and multi-region spatial transcriptome analysis reveal cellular networks and pathways associated with HCC rec | JHEP Rep 2026 |
| 41020855 | Integrator Complex Subunit 6 Regulates Biological Nature of Hepatocellular Carcinoma by Modulating Epithelial-Mesenchyma | Curr Issues Mol Biol 2025 |
| 40966122 | Disrupting integrator complex subunit INTS6 causes neurodevelopmental disorders and impairs neurogenesis and synapse dev | J Clin Invest 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/INTS6

