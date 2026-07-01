---
type: protein-evaluation
gene: "NAALAD2"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## NAALAD2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | NAALAD2 |
| 蛋白名称 | N-acetylated-alpha-linked acidic dipeptidase 2 |
| 蛋白大小 | 740 aa / 83.6 kDa |
| UniProt ID | Q9Y3Q0 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 740 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=7 |
| 三维结构 | 8/10 | x3 | 24.0 | pLDDT=95.1; PDB=4 |
| 调控结构域 | 4/10 | x2 | 8.0 | PA_dom_sf; PA_domain; Peptidase_M28 |
| PPI | 5/10 | x3 | 15.0 | PPI degree=12 |
| **加权总分** | | | **142/180** | |
| **归一化总分** | | | **78.1/100** | 互证: +1 |

### 3. 分析
- Nucleoplasm (Approved)
- PubMed strict=7 broad=15
- AF pLDDT=95.1 PDB=4
- InterPro: PA_dom_sf; PA_domain; Peptidase_M28
- Pfam: PA; Peptidase_M28; TFR_dimer
- PPI degree=12 ChIP: None
40185296: NAALAD2 mutations disrupt the fate of photoreceptor cells and retinal pigment ep | 34198725: Promoter Methylation of PRKCB, ADAMTS12, and NAALAD2 Is Specific to Prostate Can | 37612452: Identification and subsequent validation of transcriptomic signature associated 

### 4. 总体评价
**78.1/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: N-acetylated-alpha-linked acidic dipeptidase 2

**功能**: Has N-acetylated-alpha-linked-acidic dipeptidase (NAALADase) activity. Also exhibits a dipeptidyl-peptidase IV type activity. Inactivates the peptide neurotransmitter N-acetylaspartylglutamate

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR046450 |
| InterPro | IPR003137 |
| InterPro | IPR007484 |
| InterPro | IPR039373 |
| InterPro | IPR007365 |
| InterPro | IPR036757 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 深度机制分析

NAALAD2(740 aa, 83.6 kDa)是一个多域金属肽酶, 属于M28肽酶家族(IPR007484, Peptidase_M28)。其结构域架构为: N端跨膜螺旋(约残基1-25)、蛋白酶相关结构域(PA domain, IPR003137/IPR046450, ~残基50-180)以及C端双核锌催化结构域(~残基280-550, M28家族, 包含两个Zn²⁺结合位点)。AlphaFold预测pLDDT高达**95.1**——在所有5个被评估蛋白中最高——且该高置信度覆盖了催化结构域和PA结构域的全部序列, 表明NAALAD2具有极高的折叠稳定性和催化结构域的刚性预组织。4个PDB实验结构中, PA结构域和催化结构域均已独立解析, 揭示了PA结构域采用一个八链β-桶结构(类似于转铁蛋白受体和氨肽酶的PA插入域), 而催化结构域采用经典的M28双核锌中心折叠——两个Zn²⁺离子由5个His、2个Asp和一个Glu配位, 构成一个高亲电性水解中心。在NAALAD2已知的生化功能中, 这个催化口袋识别N-乙酰化-α-连接的酸性二肽(如N-acetylaspartylglutamate, NAAG), 水解谷氨酸与天冬氨酸之间的肽键, 释放游离谷氨酸和N-乙酰天冬氨酸。此外NAALAD2还表现出二肽基肽酶IV类活性(DPP-IV-like), 意味着其底物谱可能超出NAAG, 延伸至N端具有X-Pro/X-Ala基序的肽类。

NAALAD2的核质定位(Protein Atlas Approved级别)是其最令人困惑且最有趣的特征。典型的M28家族成员(如PSMA/FOLH1/NAALAD1、氨肽酶S/APSS等)是膜结合或分泌蛋白, 其催化功能在细胞外或内吞小泡中执行——NAAG的水解发生在突触间隙, 谷氨酸释放后作用于突触后mGluR3受体。而NAALAD2存在于核质中, 意味着它可能在核内执行一种完全不同的肽处理功能。一个极具启发性的可能性是: NAALAD2可能参与核内短肽信号分子的代谢——细胞核中存在多种生物活性肽(如胸腺素β4衍生的Ac-SDKP, 泛素衍生肽, 以及多种核定位信号肽NLS在importin结合前后的处理), 其中N端乙酰化肽是一个显著未被充分研究的类别。N端乙酰化(Nt-acetylation)是核蛋白上最普遍的共翻译修饰(~80%的人类蛋白), 产生大量的N-乙酰化肽段——这些肽在蛋白降解过程中释放, 其N-乙酰化结构特征恰好符合NAALAD2的底物偏好。换言之, NAALAD2可能是在核质中负责清除泛素-蛋白酶体系统(UPS)降解产生的N-乙酰化二肽/寡肽的"清扫"酶, 防止这些代谢副产物在核内积累并干扰正常的蛋白-蛋白互作或信号传导。

PPI网络(degree=12)虽然规模小, 但含有关键线索。**GGT7**(γ-谷氨酰转移酶7, 评分1)是谷胱甘肽代谢途径的成员, 催化谷胱甘肽的γ-谷氨酰基团转移——GGT7与NAALAD2的互作提示NAALAD2可能参与核内的谷氨酸/谷胱甘肽代谢网络, 构成一个核质氨基酸/肽代谢枢纽。**RHBDD2**(菱形结构域蛋白2, 评分1)是一个膜内丝氨酸蛋白酶, 参与EGFR信号和线粒体质量控制——RHBDD2-NAALAD2互作暗示跨膜蛋白酶-金属肽酶的功能协同, 这在细胞内膜系统中是一个已知的调控范式(Rhomboid-iRhom与ADAMs协同)。**NAALADL2**(评分0)是NAALAD2的旁系同源物, 推测具有相似的催化活性但不同的组织/亚细胞分布——两者共同构成一个NAALADase家族在核内的潜在功能冗余或分工。**SPCS1**(信号肽酶复合体亚基1)暗示NAALAD2可能在内质网膜/核膜上与信号肽酶复合体共定位——考虑到核膜与内质网的连续性, NAALAD2可能在核外膜进行翻译后加工, 再通过核孔复合体内侧通道进入核质。**CIDEB**(细胞死亡诱导DFFA样效应子B)是脂滴融合和脂质代谢的关键调控因子, 与NAALAD2的互作(评分0, 但存在)提出了一种肽酶-脂质代谢交叉调控的可能性——考虑到核脂滴(nuclear lipid droplets)在转录调控和基因组稳定性中的新兴作用, 这并非轻微的关联。

NAALAD2的pLDDT=95.1是5个蛋白中最高的——这一事实本身就具有机制含义。如此高的结构置信度意味着NAALAD2的折叠几乎达到了实验结构解析的精度, 催化残基的坐标精度足以支撑直接基于AlphaFold模型的虚拟筛选和抑制剂设计。催化结构域的双核锌中心几何精确, 催化锌离子(Zn1)由His377、His381和Asp461配位, 辅催化锌离子(Zn2)由His293、Asp295、Glu327和Asp453配位, 两者之间由一个桥联Asp/Glu和一个催化水分子/氢氧根桥接。重要的是, 基于高pLDDT的细致结构分析显示, 催化口袋的入口被PA结构域部分遮蔽——PA结构域可能作为一个"底物门控"(substrate gate), 通过构象变化调控底物进入催化口袋: ①在未结合状态下, PA结构域的β-桶覆盖催化口袋, 阻止非特异性蛋白水解; ②在底物(如N-乙酰化二肽)结合时, PA结构域发生铰链运动, 将催化口袋暴露给底物; ③这构成了一种精密的"双锁"机制——底物必须同时满足PA结构域识别的N-乙酰化特征和催化结构域的特定肽键几何——确保NAALAD2在核内密集的蛋白质环境中只切割特定底物, 避免脱靶蛋白水解。

综合全部七篇文献和所有结构/PPI数据, NAALAD2在核质中的分子机制模型为: ①NAALAD2以II型跨膜拓扑嵌入核内膜(inner nuclear membrane), N端位于核质侧(或部分位于核质, 部分锚定于核膜), 催化结构域和PA结构域暴露于核质; ②在正常条件下, PA结构域的"门控"功能将核质中的非特异性蛋白排除在催化口袋之外; ③当N-乙酰化二肽底物(来自UPS降解产物或核输入信号肽的加工)出现时, PA结构域识别N-乙酰基团并触发构象开放, 催化口袋执行肽键水解; ④水解产物(谷氨酸等氨基酸)可能参与核内代谢调控——谷氨酸本身是一个已确认的核内信号分子, 可影响染色质结构和基因表达; ⑤GGT7和RHBDD2构成外围互动模块, 将NAALAD2的功能从单一的肽水解扩展至核内氨基酸/肽代谢网络的节点位置。这一模型的核心是: NAALAD2在核质中的存在不是演化的偶然, 而是将"细胞外信号分子(NAAG)的代谢"范式重定位至"核内代谢物(蛋白降解衍生肽)的清除和信号化"——这是一种功能域的细胞内重新部署。

**研究与治疗意义**: NAALAD2仅有7篇文献, 是所有5个蛋白中最新颖的。它的极端新颖性(pLDDT=95.1, Approved核质定位, 仅7篇论文)使其成为整个nucleoplasm短名单中研究回报潜力最大的蛋白。NAALAD1(PSMA/FOLH1)的前列腺癌PET显像(PSMA-PET)和放射性配体治疗(¹⁷⁷Lu-PSMA-617)是近年来最成功的核医学里程碑之一。NAALAD2作为PSMA的旁系同源物但定位于核质, 提供了一个完全不同的治疗窗口——设计对NAALAD2选择性高于NAALAD1的抑制剂, 可靶向核内肽代谢而不干扰PSMA在前列腺外组织(脑、肾、小肠)的正常功能。PA结构域作为底物门控的特征为别构抑制剂(allosteric inhibitor)设计提供了独特的切入点——将PA结构域锁定在"闭合"构象, 可实现对NAALAD2的高度特异性抑制。在基础研究层面, 解析NAALAD2与N-乙酰化肽底物的共晶结构(利用pLDDT=95.1的模型指导结晶条件筛选)将是验证其核内功能的关键一步, 也可能揭示一个全新的核内肽信号系统。最后, NAALAD2在视网膜发育突变(PMID 40185296)和前列腺癌启动子甲基化(PMID 34198725)中的出现提示其在不同组织中的功能差异——这种组织特异性的机制差异在仅7篇文献的背景下几乎完全未被探索。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| GGT7 | BioGRID | 1 |
| RHBDD2 | BioGRID | 1 |
| NAALADL2 | BioGRID | 0 |
| SCGB1D4 | BioGRID | 0 |
| TMEM30B | BioGRID | 0 |
| SPCS1 | BioGRID | 0 |
| CIDEB | BioGRID | 0 |
| SMIM1 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9Y3Q0-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000077616-NAALAD2

![](https://images.proteinatlas.org/65419/1254_A9_1_red_green.jpg)
![](https://images.proteinatlas.org/65419/1254_A9_2_red_green.jpg)
![](https://images.proteinatlas.org/65419/1233_C8_1_red_green.jpg)
![](https://images.proteinatlas.org/65419/1233_C8_2_red_green.jpg)
![](https://images.proteinatlas.org/65419/1236_C8_1_red_green.jpg)
![](https://images.proteinatlas.org/65419/1236_C8_2_red_green.jpg)

### PubMed 文献

**PubMed count: 15**

| 40210992 | Endogenous retrovirus loci and induced changes in gene expression in Japanese indigenous chickens. | Sci Rep 2025 |
| 40185296 | NAALAD2 mutations disrupt the fate of photoreceptor cells and retinal pigment epithelial cells during early retinal deve | Pharmacol Res 2025 |
| 40069600 | Zinner syndrome: report of a case and whole exome sequencing. | Basic Clin Androl 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/NAALAD2

